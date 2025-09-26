from amaranth.lib.data import StructLayout
from amaranth import *
from amaranth import tracer
from amaranth_types import SrcLoc, ValueLike
from typing import TYPE_CHECKING, Optional, Iterator

from transactron.utils.typing import ValueBundle
from transactron.utils.dependencies import DependencyContext
from transactron.utils.transactron_helpers import get_caller_class_name, get_src_loc
from .keys import *
from contextlib import contextmanager
from .body import Body, TBody
from .keys import TransactionsKey
from .tmodule import TModule
from .transaction_base import TransactionBase


if TYPE_CHECKING:
    from .method import Method  # noqa: F401


__all__ = ["Transaction"]


class Transaction(TransactionBase["Transaction | Method"]):
    """Transaction.

    A `Transaction` represents a task which needs to be regularly done.
    Execution of a `Transaction` always lasts a single clock cycle.
    A `Transaction` signals readiness for execution by setting the
    `ready` signal. If the conditions for its execution are met, it
    can be run by the `TransactionManager`.

    A `Transaction` can, as part of its execution, call a number of
    `Method`\\s. A `Transaction` can be run only if every `Method`
    it calls is ready.

    A `Transaction` cannot execute concurrently with another, conflicting
    `Transaction`. Conflicts between `Transaction`\\s are either explicit
    or implicit. An explicit conflict is added using the `add_conflict`
    method. Implicit conflicts arise between pairs of `Transaction`\\s
    which use the same `Method`.

    A module which defines a `Transaction` should use `body` to
    describe used methods and the transaction's effect on the module state.
    The used methods should be called inside the `body`'s
    `with` block.

    Attributes
    ----------
    name: str
        Name of this `Transaction`.
    ready: Signal, in
        Signals that the transaction wants to run. If omitted, the transaction
        is always ready. Defined in the constructor.
    runnable: Signal, out
        Signals that all used methods are ready.
    run: Signal, out
        Signals that the transaction is run by the `TransactionManager`.
    """

    _body_ptr: Optional["Body"] = None

    def __init__(self, *, name: Optional[str] = None, src_loc: int | SrcLoc = 0):
        """
        Parameters
        ----------
        name: str or None
            Name hint for this `Transaction`. If `None` (default) the name is
            inferred from the variable name this `Transaction` is assigned to.
            If the `Transaction` was not assigned, the name is inferred from
            the class name where the `Transaction` was constructed.
        src_loc: int | SrcLoc
            How many stack frames deep the source location is taken from.
            Alternatively, the source location to use instead of the default.
        """
        super().__init__(src_loc=get_src_loc(src_loc))
        self.owner, owner_name = get_caller_class_name(default="$transaction")
        self.name = name or tracer.get_var_name(depth=2, default=owner_name)
        DependencyContext.get().add_dependency(TransactionsKey(), self)
        self.ready = Signal(name=self.owned_name + "_ready")
        self.runnable = Signal(name=self.owned_name + "_runnable")
        self.run = Signal(name=self.owned_name + "_run")

    @property
    def _body(self) -> TBody:
        if self._body_ptr is not None:
            return TBody(self._body_ptr)
        raise RuntimeError(f"Method '{self.name}' not defined")

    def _set_impl(self, m: TModule, value: Body):
        if self._body_ptr is not None:
            raise RuntimeError(f"Transaction '{self.name}' already defined")
        if value.data_in.shape().size != 0 or value.data_out.shape().size != 0:
            raise ValueError(f"Transaction body {value.name} has invalid interface")
        self._body_ptr = value
        m.d.comb += self.ready.eq(value.ready)
        m.d.comb += self.runnable.eq(value.runnable)
        m.d.comb += self.run.eq(value.run)

    @contextmanager
    def body(self, m: TModule, *, ready: ValueLike = C(1)) -> Iterator["Transaction"]:
        """Defines the `Transaction` body.

        This context manager allows to conveniently define the actions
        performed by a `Transaction` when it's running. Each assignment
        added to a domain under `body` is guarded by the `run` signal.
        Combinational assignments which do not need to be guarded by
        `run` can be added to `m.d.top_comb` or `m.d.av_comb` instead of
        `m.d.comb`. `Method` calls can be performed under `body`.

        Parameters
        ----------
        m: TModule
            The module where the `Transaction` is defined.
        ready: Signal
            Indicates that the `Transaction` wants to be executed. By
            default it is `Const(1)`, so it wants to be executed in
            every clock cycle.
        """
        impl = Body(
            name=self.name,
            owner=self.owner,
            i=StructLayout({}),
            o=StructLayout({}),
            src_loc=self.src_loc,
        )
        self._set_impl(m, impl)

        m.d.av_comb += impl.ready.eq(ready)
        with impl.context(m):
            with m.AvoidedIf(impl.run):
                yield self

    def __repr__(self) -> str:
        return "(transaction {})".format(self.name)

    def debug_signals(self) -> ValueBundle:
        return [self.ready, self.runnable, self.run]
