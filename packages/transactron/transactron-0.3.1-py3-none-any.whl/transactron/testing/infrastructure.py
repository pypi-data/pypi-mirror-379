import sys
import pytest
import logging
import os
import random
import functools
from contextlib import contextmanager, nullcontext
from collections.abc import Callable
from typing import Any, cast, Optional
from amaranth import *
from amaranth.sim import *
from amaranth.sim._async import SimulatorContext
from amaranth_types import HasElaborate

from transactron.utils.dependencies import DependencyContext, DependencyManager
from .profiler import profiler_process, Profile
from .logging import make_logging_process, parse_logging_level, _LogFormatter
from .tick_count import make_tick_count_process
from .method_mock import MethodMock
from transactron.core.keys import TransactionManagerKey
from transactron.core.context import TransactronContextElaboratable
from transactron.utils import auto_debug_signals, HasDebugSignals


__all__ = ["PysimSimulator", "TestCaseWithSimulator"]


class _TestModule(Elaboratable):
    def __init__(self, tested_module: HasElaborate, add_transaction_module: bool):
        self.tested_module = (
            TransactronContextElaboratable(tested_module, dependency_manager=DependencyContext.get())
            if add_transaction_module
            else tested_module
        )
        self.add_transaction_module = add_transaction_module

    def elaborate(self, platform) -> HasElaborate:
        m = Module()

        # so that Amaranth allows us to use add_clock
        _dummy = Signal()
        m.d.sync += _dummy.eq(1)

        m.submodules.tested_module = self.tested_module

        m.domains.sync_neg = ClockDomain(clk_edge="neg", local=True)

        return m


class PysimSimulator(Simulator):
    def __init__(
        self,
        module: HasElaborate,
        max_cycles: float = 10e4,
        add_transaction_module=True,
        traces_file=None,
        clk_period=1e-6,
    ):
        test_module = _TestModule(module, add_transaction_module)
        self.tested_module = tested_module = test_module.tested_module
        super().__init__(test_module)

        self.add_clock(clk_period)
        self.add_clock(clk_period, domain="sync_neg")

        if isinstance(tested_module, HasDebugSignals):
            extra_signals = tested_module.debug_signals
        else:
            extra_signals = functools.partial(auto_debug_signals, tested_module)

        if traces_file:
            traces_dir = "test/__traces__"
            os.makedirs(traces_dir, exist_ok=True)
            # Signal handling is hacky and accesses Simulator internals.
            # TODO: try to merge with Amaranth.
            if isinstance(extra_signals, Callable):
                extra_signals = extra_signals()
            clocks = [d.clk for d in cast(Any, self)._design.fragment.domains.values()]

            self.ctx = self.write_vcd(
                f"{traces_dir}/{traces_file}.vcd",
                f"{traces_dir}/{traces_file}.gtkw",
                traces=[clocks, extra_signals],
            )
        else:
            self.ctx = nullcontext()

        async def timeout_testbench(sim: SimulatorContext):
            await sim.delay(clk_period * max_cycles)
            assert False, "simulation timed out"

        self.add_testbench(timeout_testbench, background=True)

    def run(self) -> None:
        with self.ctx:
            super().run()


class TestCaseWithSimulator:
    dependency_manager: DependencyManager

    @contextmanager
    def _configure_dependency_context(self):
        self.dependency_manager = DependencyManager()
        with DependencyContext(self.dependency_manager):
            yield Tick()

    def add_mock(self, sim: PysimSimulator, val: MethodMock):
        sim.add_process(val.output_process)
        if val.validate_arguments is not None:
            sim.add_process(val.validate_arguments_process)
        sim.add_testbench(val.effect_process, background=True)

    def _add_class_mocks(self, sim: PysimSimulator) -> None:
        for key in dir(self):
            val = getattr(self, key)
            if hasattr(val, "_transactron_testing_process"):
                sim.add_process(val)
            elif hasattr(val, "_transactron_method_mock"):
                self.add_mock(sim, val())

    def _add_local_mocks(self, sim: PysimSimulator, frame_locals: dict) -> None:
        for key, val in frame_locals.items():
            if hasattr(val, "_transactron_testing_process"):
                sim.add_process(val)
            elif hasattr(val, "_transactron_method_mock"):
                self.add_mock(sim, val())

    def _add_all_mocks(self, sim: PysimSimulator, frame_locals: dict) -> None:
        self._add_class_mocks(sim)
        self._add_local_mocks(sim, frame_locals)

    def _configure_traces(self):
        traces_file = None
        if "__TRANSACTRON_DUMP_TRACES" in os.environ:
            traces_file = self._transactron_current_output_file_name
        self._transactron_infrastructure_traces_file = traces_file

    @contextmanager
    def _configure_profiles(self):
        profile = None
        if "__TRANSACTRON_PROFILE" in os.environ:

            def f():
                nonlocal profile
                try:
                    transaction_manager = DependencyContext.get().get_dependency(TransactionManagerKey())
                    profile = Profile()
                    return profiler_process(transaction_manager, profile)
                except KeyError:
                    pass
                return None

            self._transactron_sim_processes_to_add.append(f)

        yield

        if profile is not None:
            profile_dir = "test/__profiles__"
            profile_file = self._transactron_current_output_file_name
            os.makedirs(profile_dir, exist_ok=True)
            profile.encode(f"{profile_dir}/{profile_file}.json")

    @contextmanager
    def _configure_logging(self):
        def on_error():
            assert False, "Simulation finished due to an error"

        log_level = parse_logging_level(os.environ["__TRANSACTRON_LOG_LEVEL"])
        log_filter = os.environ["__TRANSACTRON_LOG_FILTER"]
        self._transactron_sim_processes_to_add.append(lambda: make_logging_process(log_level, log_filter, on_error))

        ch = logging.StreamHandler()
        formatter = _LogFormatter()
        ch.setFormatter(formatter)

        root_logger = logging.getLogger()
        handlers_before = root_logger.handlers.copy()
        root_logger.handlers.append(ch)
        yield
        root_logger.handlers = handlers_before

    @contextmanager
    def reinitialize_fixtures(self):
        # File name to be used in the current test run (either standard or hypothesis iteration)
        # for standard tests it will always have the suffix "_0". For hypothesis tests, it will be suffixed
        # with the current hypothesis iteration number, so that each hypothesis run is saved to a
        # the different file.
        self._transactron_current_output_file_name = (
            self._transactron_base_output_file_name + "_" + str(self._transactron_hypothesis_iter_counter)
        )
        self._transactron_sim_processes_to_add: list[Callable[[], Optional[Callable]]] = []
        with self._configure_dependency_context():
            self._configure_traces()
            with self._configure_profiles():
                with self._configure_logging():
                    self._transactron_sim_processes_to_add.append(make_tick_count_process)
                    yield
        self._transactron_hypothesis_iter_counter += 1

    @pytest.fixture(autouse=True)
    def fixture_initialize_testing_env(self, request):
        # Hypothesis creates a single instance of a test class, which is later reused multiple times.
        # This means that pytest fixtures are only run once. We can take advantage of this behaviour and
        # initialise hypothesis related variables.

        # The counter for distinguishing between successive hypothesis iterations, it is incremented
        # by `reinitialize_fixtures` which should be started at the beginning of each hypothesis run
        self._transactron_hypothesis_iter_counter = 0
        # Base name which will be used later to create file names for particular outputs
        self._transactron_base_output_file_name = ".".join(request.node.nodeid.split("/"))
        with self.reinitialize_fixtures():
            yield

    @contextmanager
    def run_simulation(self, module: HasElaborate, max_cycles: float = 10e4, add_transaction_module=True):
        clk_period = 1e-6
        sim = PysimSimulator(
            module,
            max_cycles=max_cycles,
            add_transaction_module=add_transaction_module,
            traces_file=self._transactron_infrastructure_traces_file,
            clk_period=clk_period,
        )
        self._add_all_mocks(sim, sys._getframe(2).f_locals)

        yield sim

        for f in self._transactron_sim_processes_to_add:
            ret = f()
            if ret is not None:
                sim.add_process(ret)

        sim.run()

    async def tick(self, sim: SimulatorContext, cycle_cnt: int = 1):
        """
        Waits for the given number of cycles.
        """
        for _ in range(cycle_cnt):
            await sim.tick()

    async def random_wait(self, sim: SimulatorContext, max_cycle_cnt: int, *, min_cycle_cnt: int = 0):
        """
        Wait for a random amount of cycles in range [min_cycle_cnt, max_cycle_cnt]
        """
        await self.tick(sim, random.randrange(min_cycle_cnt, max_cycle_cnt + 1))

    async def random_wait_geom(self, sim: SimulatorContext, prob: float = 0.5, max_cycle_cnt: int = 2**16):
        """
        Wait till the first success, where there is `prob` probability for success in each cycle.
        """
        cycle_cnt = 0
        while random.random() > prob and cycle_cnt < max_cycle_cnt:
            await sim.tick()
            cycle_cnt += 1
