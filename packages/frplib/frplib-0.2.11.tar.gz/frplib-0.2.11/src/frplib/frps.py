from __future__ import annotations

import math
import random

from abc               import ABC, abstractmethod
from collections       import defaultdict
from collections.abc   import Iterable
from decimal           import Decimal
from functools         import reduce
from typing            import Callable, cast, overload, Union
from typing_extensions import Self, Any, TypeAlias, TypeGuard

from rich.table        import Table
from rich              import box as rich_box
from rich.panel        import Panel

from frplib.env        import environment
from frplib.exceptions import (ConditionMustBeCallable, ComplexExpectationWarning, ContractError,
                               ConstructionError, FrpError, KindError, MismatchedDomain,)
from frplib.kinds      import Kind, kind, ConditionalKind, permutations_of
from frplib.numeric    import Numeric, Nothing, show_tuple, as_real
from frplib.protocols  import Projection, SupportsExpectation, SupportsKindOf
from frplib.quantity   import as_quant_vec
from frplib.statistics import Statistic, statistic, compose2, infinity, tuple_safe, Proj, Prepend
from frplib.symbolic   import Symbolic
from frplib.utils      import const, is_tuple, scalarize
from frplib.vec_tuples import (VecTuple, as_scalar, as_scalar_weak, as_vec_tuple, vec_tuple, value_set_from)


#
# Types
#

QuantityType: TypeAlias = Union[Numeric, Symbolic, Nothing]
ValueType: TypeAlias = VecTuple[QuantityType]  # ATTN

# Invariance of dict type causes incorrect type errors when constructing conditional FRPs
# So we make the input type include the most common special cases individually
# NOTE: This assumes NumericD for Numeric, which is why Decimal is used
CondFrpInput: TypeAlias = Union[Callable[[ValueType], 'FRP'], dict[ValueType, 'FRP'], dict[QuantityType, 'FRP'], dict[int, 'FRP'], dict[Decimal, 'FRP'], dict[Symbolic, 'FRP'], ConditionalKind, 'FRP']

#
# Helpers
#

def join_values(values: Iterable[ValueType]) -> ValueType:
    combined = []
    for value in values:
        combined.extend(list(value))
    return VecTuple(combined)

def drop_input(codim):
    "A simple projection factory for extracting targets from Conditional Kinds."
    def f(v):
        return v[codim:]
    return f

def scalar_safe(f):
    "Wraps a scalar function so that it can accept scalars or tuples."
    def g(v):
        return f(as_scalar_weak(v))

    return g

def vector_safe(f):
    "Wraps a function taking a single VecTuple so that it can accept more flexible inputs."
    def g(v):
        return f(as_vec_tuple(v))

    return g


#
# FRP Demos
#
# FRP.sample can return either all the sampled values
# or a summary table. The latter is the default and
# is basically just a dict[ValueType, int], but we
# enhance this with representations and some other
# information
#

FrpDemo: TypeAlias = list[ValueType]

class FrpDemoSummary:
    # At most one of these should be non-None
    def __init__(
            self,
            *,
            summary: Self | dict[ValueType, int] | None = None,
            sample_size: int | None = None,
            samples: FrpDemo | None = None
    ) -> None:
        self._summary: dict[ValueType, int] = defaultdict(int)
        self._size = 0

        if summary and isinstance(summary, FrpDemoSummary):
            self._size = summary._size
            self._summary = {k: v for k, v in summary._summary.items()}
        elif summary and isinstance(summary, dict):
            self._size = len(summary)
            self._summary = {k: v for k, v in summary.items()}
        elif samples:
            for sample in samples:
                self.add(sample)

    def add(self, value: ValueType) -> Self:
        self._summary[value] += 1
        self._size += 1
        return self

    def rich_table(self, title: str | None = None):
        # ATTN: Put styles in a more central place (environment?), e.g., environment.styles['values']
        if title is None:
            title = 'Summary of Output Values'
        table = Table(title=title, box=rich_box.SQUARE_DOUBLE_HEAD)
        table.add_column('Values', justify='left', style='#4682b4', no_wrap=True)
        table.add_column('Count', justify='right')
        table.add_column('Proportion', justify='right', style='#6a6c6e')

        values = sorted(self._summary.keys(), key=tuple)  # Dictionary order
        n = float(self._size)
        for value in values:
            table.add_row(show_tuple(value.map(lambda x: "{0:.4g}".format(x))),
                          str(self._summary[value]),
                          "{0:.4g}%".format(round(100 * self._summary[value] / n, 6)))

        return table

    def ascii_table(self, title: str | None = None) -> str:
        out: list[str] = []
        if title is None:
            title = 'Summary of output values:'
        out.append(title)

        values = sorted(self._summary.keys(), key=tuple)  # Dictionary order
        n = float(self._size)
        widths = {'value': 0, 'count': 0, 'prop': 0}
        rows = []
        for value in values:
            cells = {
                'value': show_tuple(value.map(lambda x: "{0:.5g}".format(x))),  # str(VecTuple(value)),
                'count': "{0:,d}".format(self._summary[value]),
                'prop': "({0:.4f}%)".format(round(100 * self._summary[value] / n, 6))
            }
            rows.append(cells)
            widths = {k: max(len(cells[k]), widths[k]) for k in widths}
        for row in rows:
            out.append("{value:<{w[0]}s}    {count:>{w[1]}s}"
                       "    {prop:>{w[2]}s}".format(**row, w=list(widths.values())))
        return "\n".join(out)

    def table(self, ascii=False, title: str | None = None) -> str:
        if ascii:
            return self.ascii_table(title)
        return self.rich_table(title)

    def __len__(self) -> int:
        return self._size

    def __frplib_repr__(self):
        return self.table(environment.ascii_only)

    def __str__(self) -> str:
        return self.table(ascii=True)

    def __repr__(self) -> str:
        if environment.is_interactive:
            return str(self)
        return f'{self.__class__.__name__}(summary={repr(self._summary)}, sample_size={self._size})'


#
# FRP Expressions
#
# When an FRP is constructed from an expression rather than a Kind,
# we record the expression (including the FRP objects themselves,
# which are logically immutable and thus held) and use that as a recipe
# for both sampling and constructing a value.
#

class FrpExpression(ABC):
    def __init__(self) -> None:
        self._cached_kind: Kind | None = None
        self._cached_value: ValueType | None = None

    @abstractmethod
    def sample1(self) -> ValueType:
        "Draw a sample from the underlying FRP's kind or get its value"
        ...

    @abstractmethod
    def value(self) -> ValueType:
        "Draw a sample from the underlying FRP's kind or get its value"
        ...

    @abstractmethod
    def kind(self) -> Kind:
        ...

    def kind_of(self) -> Kind:
        return self.kind()

    @abstractmethod
    def clone(self) -> FrpExpression:
        ...

    @abstractmethod
    def _refresh_cached_value(self) -> ValueType | None:
        ...

class TransformExpression(FrpExpression):
    def __init__(
            self,
            transform: Callable[[ValueType], ValueType],
            target: FrpExpression
    ) -> None:
        super().__init__()
        self._transform = transform   # This will typically be a statistic
        self._target = target

    def sample1(self) -> ValueType:
        return self._transform(self._target.sample1())

    def value(self) -> ValueType:
        if self._cached_value is None:
            try:
                self._cached_value = self._transform(self._target.value())
            except Exception:  # ATTN: might be easiest to just evaluate the value at transform time
                if isinstance(self._transform, Statistic):
                    label = self._transform.name   # type: ignore
                else:
                    label = str(self._transform)
                raise MismatchedDomain(f'Statistic {label} is incompatible with this FRP,'
                                       f'could not evaluate it on the FRPs value.')
        return self._cached_value

    def kind(self) -> Kind:
        if self._cached_kind is None:
            self._cached_kind = self._target.kind() ^ self._transform
        return self._cached_kind

    def clone(self) -> 'TransformExpression':
        new_expr = TransformExpression(self._transform, self._target.clone())
        new_expr._cached_kind = self._cached_kind
        return new_expr

    def _refresh_cached_value(self) -> ValueType | None:
        if self._cached_value is None:
            val = self._target._refresh_cached_value()
            if val is not None:
                self._cached_value = self._transform(val)
        return self._cached_value

class IMixtureExpression(FrpExpression):
    def __init__(self, terms: Iterable['FrpExpression']) -> None:
        super().__init__()
        self._operands = list(terms)

        # Cache kind or value if appropriate
        # We only cache these if they are available for every term.
        # Moreover, we ensure that the kind is not too large,
        # as determined by FRP's complexity threshold.
        # We stop as soon as these conditions are not satisfied.
        threshold = math.log2(FRP.COMPLEXITY_THRESHOLD)
        logsize = 0.0
        cache_kind = True
        cache_value = True

        combined_values: list = []
        combined_kind = Kind.empty
        for f in self._operands:
            if cache_value:
                if f._cached_value is not None:
                    combined_values.extend(f._cached_value)
                else:
                    cache_value = False
            if cache_kind:
                if f._cached_kind is not None:
                    if f._cached_kind.size > 0:  # Empty Kind is identity element
                        logsize += math.log2(f._cached_kind.size)
                        if logsize <= threshold:
                            combined_kind = combined_kind * f._cached_kind
                        else:
                            cache_kind = False
                else:
                    cache_kind = False
            elif not cache_value:
                break

        if cache_value:
            self._cached_value = as_quant_vec(combined_values)
        if cache_kind:
            self._cached_kind = combined_kind

    def sample1(self) -> ValueType:
        if len(self._operands) == 0:
            return VecTuple(())
        return join_values(operand.sample1() for operand in self._operands)

    def value(self) -> ValueType:
        if len(self._operands) == 0:
            return VecTuple(())
        if self._cached_value is None:
            self._cached_value = join_values(operand.value() for operand in self._operands)
        return self._cached_value

    def kind(self) -> Kind:
        if len(self._operands) == 0:
            return Kind.empty
        if self._cached_kind is None:
            kinds = [operand.kind() for operand in self._operands]
            combined_kind = Kind.empty
            for child in kinds:
                combined_kind = combined_kind * child
            self._cached_kind = combined_kind
        return self._cached_kind

    def clone(self) -> 'IMixtureExpression':
        new_expr = IMixtureExpression([term.clone() for term in self._operands])
        new_expr._cached_kind = self._cached_kind
        return new_expr

    @property
    def expectation(self):
        cached = [k._cached_kind for k in self._operands]
        if all(k is not None for k in cached):
            return as_vec_tuple([k.expectation for k in cached])   # type: ignore
        elif all(isinstance(term, SupportsExpectation) for term in self._operands):
            return as_vec_tuple([term.expectation for term in self._operands])  # type: ignore
        raise ComplexExpectationWarning('The expectation of this FRP could not be computed '
                                        'without first finding its kind.')

    def _refresh_cached_value(self) -> ValueType | None:
        if self._cached_value is None:
            vals = []
            has_cached = True
            for op in self._operands:
                cv = op._refresh_cached_value()
                if cv is None:
                    has_cached = False
                    break
                vals.append(cv)

            if has_cached:
                self._cached_value = VecTuple.join(vals)
        return self._cached_value

    @classmethod
    def append(cls, mixture: 'IMixtureExpression', other: 'FrpExpression') -> 'IMixtureExpression':
        "Returns a new IMixture with target as the last term."
        return IMixtureExpression([*mixture._operands, other])

    @classmethod
    def prepend(cls, mixture: 'IMixtureExpression', other: 'FrpExpression') -> 'IMixtureExpression':
        "Returns a new IMixture with target as the last term."
        return IMixtureExpression([other, *mixture._operands])

    @classmethod
    def join(cls, mixture1: 'IMixtureExpression', mixture2: 'IMixtureExpression') -> 'IMixtureExpression':
        "Returns a new IMixture with target as the last term."
        return IMixtureExpression([*mixture1._operands, *mixture2._operands])

class IMixPowerExpression(FrpExpression):
    def __init__(self, term: 'FrpExpression', pow: int) -> None:
        super().__init__()
        self._term = term
        self._pow = pow
        if term._cached_kind is not None:
            if term._cached_kind.size == 0:
                self._cached_kind = term._cached_kind  # Empty Kind is identity for *
            elif pow * math.log2(term._cached_kind.size) <= math.log2(FRP.COMPLEXITY_THRESHOLD):
                self._cached_kind = term._cached_kind ** pow

    def sample1(self) -> ValueType:
        draws = [self._term.sample1() for _ in range(self._pow)]
        return join_values(draws)

    def value(self) -> ValueType:
        if self._cached_value is None:
            self._cached_value = self.sample1()
        return self._cached_value

    def kind(self) -> Kind:
        if self._cached_kind is None:
            self._cached_kind = self._term.kind() ** self._pow
        return self._cached_kind

    def clone(self) -> 'IMixPowerExpression':
        new_expr = IMixPowerExpression(self._term.clone(), self._pow)
        new_expr._cached_kind = self._cached_kind
        return new_expr

    @property
    def expectation(self):
        if self._term._cached_kind is not None:
            exp = self._term._cached_kind.expectation
            return as_vec_tuple([exp] * self._pow)
        elif isinstance(self._term, SupportsExpectation):
            exp = self._term.expectation
            return as_vec_tuple([exp] * self._pow)
        raise ComplexExpectationWarning('The expectation of this FRP could not be computed '
                                        'without first finding its kind.')

    def _refresh_cached_value(self) -> ValueType | None:
        # Because these are cloned, there's nothing to probe here
        return self._cached_value

class MixtureExpression(FrpExpression):
    # ATTN: the target should be passed to conditional_frp before this
    def __init__(self, mixer: FrpExpression, target: 'ConditionalFRP') -> None:
        super().__init__()
        self._mixer = mixer
        self._target = target

    def sample1(self, want_value=False) -> ValueType:
        mixer_value = self._mixer.sample1()
        target_frp = self._target(mixer_value)
        return FRP.sample1(target_frp)  # Input pass through includes mixer_value

    def value(self) -> ValueType:
        if self._cached_value is None:
            mixer_value = self._mixer.value()
            target_frp = self._target(mixer_value)
            self._cached_value = target_frp.value  # Input pass through includes mixer_value
        return self._cached_value

    def kind(self) -> Kind:
        if self._cached_kind is None:
            self._cached_kind = self._mixer.kind() >> kind(self._target)  # Fixes Bug 41
        return self._cached_kind

    def clone(self) -> 'MixtureExpression':
        new_expr = MixtureExpression(self._mixer.clone(), self._target.clone())
        new_expr._cached_kind = self._cached_kind
        return new_expr

    def _refresh_cached_value(self) -> ValueType | None:
        if self._cached_value is None:
            mix_val = self._mixer._refresh_cached_value()
            if mix_val is not None:
                target_val = self._target(mix_val)._get_cached_value()
                if target_val is not None:
                    self._cached_value = target_val
        return self._cached_value

class ConditionalExpression(FrpExpression):
    def __init__(self, target: FrpExpression, condition: Callable[[ValueType], Any]) -> None:  # Any is morally bool
        super().__init__()
        self._condition = condition   # This will typically be a statistic returning a bool
        self._target = target

        if self._target._cached_kind is not None:
            self._cached_kind = self._target._cached_kind | condition

    def sample1(self) -> ValueType:
        while True:  # If condition is always false, this will not terminate
            val = self._target.sample1()
            if bool(as_scalar(self._condition(val))):
                return val

    def value(self) -> ValueType:
        # ATTN: Logical oddity about having value() for this type as it is counterfactual
        # Same with computation earlier; it bears thinking about
        # Perhaps this should just be sample1 always?  Or some sort of Bottom
        if self._cached_value is not None:
            return self._cached_value
        val = self._target.value()

        if as_scalar(self._condition(val)):
            return val
        else:
            self._cached_kind = Kind.empty
            return vec_tuple()  # "Value" of Empty FRP

    def kind(self) -> Kind:
        if self._cached_kind is None:
            if self.value() == vec_tuple():
                self._cached_kind = Kind.empty
            else:
                self._cached_kind = self._target.kind() | self._condition
        return self._cached_kind

    def clone(self) -> 'ConditionalExpression':
        new_expr = ConditionalExpression(self._target.clone(), self._condition)
        new_expr._cached_kind = self._cached_kind
        return new_expr

    def _refresh_cached_value(self) -> ValueType | None:
        if self._cached_value is None:
            val = self._target._refresh_cached_value()
            if val is not None:
                satisfies = bool(as_scalar(self._condition(val)))
                self._cached_value = val if satisfies else vec_tuple()
        return self._cached_value

class PureExpression(FrpExpression):
    """An expression representing a specific FRP.

    This acts as a leaf in the expression tree. Note that FRPs are logically
    immutable, and we keep the *specific* FRP as part of the expression.
    As a result, values should propagate properly through the entire expression
    tree. If the target FRP is Kinded, we store the Kind, and we also
    cache the value. See class method `fromKind` to create a PureExpression
    from a Kind with a fresh FRP.

    """
    def __init__(self, frp: FRP) -> None:
        super().__init__()
        self._target = frp
        if frp.is_kinded():
            self._cached_kind = frp.kind
        if frp._value is not None:
            self._cached_value = frp._value

    @classmethod
    def from_kind(cls, k: Kind) -> PureExpression:
        "Returns a PureExpression based on a *fresh* FRP built from the given Kind."
        return PureExpression(frp(k))

    def sample1(self, want_value=False) -> ValueType:
        return FRP.sample1(self._target)

    def value(self) -> ValueType:
        if self._cached_value is None:
            self._cached_value = self._target.value  # For checks in other expressions
        return self._cached_value

    def kind(self) -> Kind:
        if self._cached_kind is None:
            self._cached_kind = self._target.kind    # For checks in other expressions
        return self._cached_kind

    def clone(self) -> 'PureExpression':
        new_expr = PureExpression(self._target.clone())
        new_expr._target._kind = self._target._kind
        return new_expr

    @property
    def expectation(self):
        if self._target.is_kinded():
            return self._target.kind.expectation
        raise ComplexExpectationWarning('The expectation of this FRP could not be computed '
                                        'without first finding its kind.')

    def _refresh_cached_value(self) -> ValueType | None:
        if self._cached_value is None:
            val = self._target._value or (self._target._expr and self._target._expr._refresh_cached_value())
            if val is not None:
                self._cached_value = val  # type: ignore
        return self._cached_value


def as_expression(frp: FRP) -> FrpExpression:
    """Returns an FRP expression that is equivalent to this FRP.

    If kinded, then we merely wrap the FRP itself. However, if the
    FRP is defined by an expression, we reproduce that expression,
    caching the kind and value if they are available.

    """
    if frp.is_kinded():
        return PureExpression(frp)
    assert frp._expr is not None
    return frp._expr


#
# Conditional FRPs
#

class ConditionalFRP:
    """A unified representation of a conditional FRP.

    A conditional FRP is a mapping from a set of values of common
    dimension to FRPs of common dimension. This can be based on
    either a dictionary or on a function, but note that the function
    should return the *same* FRP each time it is called with any
    particular value. (In fact, values are cached here to make it
    easier to define function based condtional FRPs.)

    """
    def __init__(
            self,
            mapping: CondFrpInput,  # Callable[[ValueType], FRP] | dict[ValueType, FRP] | dict[QuantityType, FRP] | ConditionalKind,
            *,
            codim: int | None = None,  # If set to 1, will pass a scalar not a tuple to fn (not dict)
            dim: int | None = None,
            domain: Iterable[ValueType] | Iterable[QuantityType] | Callable[[ValueType], bool] | None = None,
            target_dim: int | None = None,
            auto_clone: bool = False
    ) -> None:
        if isinstance(mapping, ConditionalKind):
            codim = mapping._codim if codim is None else codim
            dim = mapping._dim if dim is None else dim
            target_dim = mapping._target_dim if target_dim is None else target_dim
            if domain is None and not mapping._trivial_domain:
                domain = mapping._domain_set if mapping._has_domain_set else mapping._domain
            mapping = mapping.map(frp)  # convert target Kinds to FRPs
        elif isinstance(mapping, FRP):
            target_dim = target_dim or mapping.dim
            mapping = const(mapping)

        self._auto_clone = auto_clone

        has_domain_set = False
        if domain is not None:
            if callable(domain):
                self._domain: Callable[[ValueType], bool] = domain
            else:
                _domain_set: set = value_set_from(domain)  # Accessed in the following closure
                self._domain_set: set = _domain_set
                self._domain = lambda v: v in _domain_set
                has_domain_set = True
            self._trivial_domain = False
        else:
            # Infer domain set in the dict case later if possible
            self._domain = const(True)  # If unknown, accept everything
            self._trivial_domain = True

        if isinstance(mapping, dict):
            self._is_dict = True
            self._mapping: dict[ValueType, FRP] = {}
            self._targets: dict[ValueType, FRP] = {}  # NB: Trading space for time by keeping these
            for k, v in mapping.items():
                if not is_frp(v):
                    raise ConstructionError(f'Dictionary for a conditional FRP should map to FRPs, but {v} is not an FRP')
                kin = as_quant_vec(k)
                vout = v.transform(Prepend(kin))  # Input pass through
                self._mapping[kin] = vout
                self._targets[kin] = v
            self._original_fn: Callable[[ValueType], FRP] | None = None

            # Attempt to infer codimension and domain if needed and possible.
            # We allow a) the dictionary to have extra keys, b) the FRPs to have
            # multiple dims if dim is supplied, c) the supplied domain to be a
            # subset of mapping's keys, d) the keys to have different dimensions
            # if codim is supplied.
            maybe_codims: set[int] = set()
            for k, v in self._mapping.items():
                maybe_codims.add(k.dim)

            if codim is None:
                if len(maybe_codims) == 1:
                    _codim: int | None = list(maybe_codims)[0]
                elif has_domain_set:
                    domain_dims = set(x.dim for x in self._domain_set)
                    if len(domain_dims) == 1:  # Known to have elements of only one dimension
                        _codim = list(domain_dims)[0]
                    else:
                        # This should not happen so raise an error
                        raise ConstructionError('Domain set for conditional FRP contains disparate dimensions')
                else:
                    _codim = None  # Cannot infer a single codim, accept any type of values
            else:
                _codim = codim

            maybe_dims: set[int] = set()
            all_dims = True
            for k, v in self._mapping.items():
                if _codim is None or k.dim == _codim:
                    if v.is_kinded() or v._get_cached_value() is not None:
                        maybe_dims.add(v.dim)  # Do not compute the FRP's value if not available
                    else:
                        # If not all kinded, we give up on infering dim (resolves ISSUE 27)
                        all_dims = False
                        break
                    # ATTN: Also, do we need to restrict to common dims here?

            if dim is None and target_dim is None:
                if len(maybe_dims) == 1 and all_dims:
                    _dim: int | None = list(maybe_dims)[0]
                else:
                    _dim = None
            elif dim is None:
                _dim = _codim + target_dim if _codim is not None else None  # type: ignore
            elif target_dim is None:
                if dim < min(maybe_dims):
                    raise ConstructionError('Specified dim for conditional FRP too small (must include input length), '
                                            'perhaps you meant to give the target_dim instead')
                _dim = dim
            elif _codim is not None and _codim != dim - target_dim:
                raise ConstructionError('Both dim and target_dim given but inconsistent, '
                                        'should have codim + target_dim = dim')
            else:  # both dim and target_dim supplied, either consistent with codim or with no codim
                if _codim is None:
                    if target_dim >= dim:
                        raise ConstructionError(f'target_dim {target_dim} should be smaller than dim {dim} '
                                                'for a Conditional FRP')
                    _codim = dim - target_dim  # Use this to infer codim, it's equivalent
                _dim = dim

            if domain is None:  # Infer domain set from keys
                if _codim is not None:
                    _domain_set = set(k for k in self._mapping.keys() if len(k) == _codim)
                else:
                    _domain_set = set(self._mapping.keys())
                self._domain_set = _domain_set
                self._domain = lambda v: v in _domain_set
                has_domain_set = True
                self._trivial_domain = False  # non-trivial domain specified implicitly
            elif has_domain_set:  # check that domains are consistent
                if _codim is not None:
                    mapping_domain = set(k for k in self._mapping.keys() if len(k) == _codim)
                else:
                    mapping_domain = set(self._mapping.keys())
                if not (self._domain_set <= mapping_domain):
                    raise ConstructionError('The supplied domain for a conditional FRP is not a subset of '
                                            'with the keys of the given dictionary.')

            self._codim: int | None = _codim
            self._dim: int | None = _dim
            self._has_domain_set = has_domain_set
            if target_dim is not None:
                self._target_dim: int | None = target_dim
            elif _codim is not None and _dim is not None:
                self._target_dim = _dim - _codim
            else:
                self._target_dim = None

            def fn(*args) -> FRP:
                n = len(args)
                if n == 1 and is_tuple(args[0]):
                    args = args[0]
                    n = len(args)
                value = as_quant_vec(args)  # ATTN: should this be as_vec_tuple??

                if self._codim is not None and n != self._codim:
                    raise MismatchedDomain(f'A value of invalid dimension {n} was passed to a'
                                           f' conditional FRP of codimension {self._codim}.')
                if (not self._trivial_domain and not self._domain(value)) or value not in self._mapping:
                    raise MismatchedDomain(f'Supplied value {value} not in domain of conditional FRP.')

                full = self._mapping[value]
                if self._auto_clone:
                    full = full.clone()
                return full

            def tfn(*args) -> FRP:
                n = len(args)
                if n == 1 and is_tuple(args[0]):
                    args = args[0]
                    n = len(args)
                value = as_quant_vec(args)  # ATTN: should this be as_vec_tuple??

                if self._codim is not None and n != self._codim:
                    raise MismatchedDomain(f'A value of invalid dimension {n} was passed to a'
                                           f' conditional FRP of codimension {self._codim}.')
                if (not self._trivial_domain and not self._domain(value)) or value not in self._targets:
                    raise MismatchedDomain(f'Supplied value {value} not in domain of conditional FRP.')

                target = self._targets[value]
                if self._auto_clone:
                    target = target.clone()
                return target

            self._fn: Callable[..., FRP] = fn
            self._target_fn: Callable[..., FRP] = tfn

        elif callable(mapping):         # Check to please mypy
            self._is_dict = False
            self._mapping = {}  # Cache, if used
            self._targets = {}  # NB: Trading space for time by keeping these
            self._original_fn = mapping

            if codim is None:
                domain_dims = set()
                if has_domain_set:
                    domain_dims = set(x.dim for x in self._domain_set)

                if has_domain_set and len(domain_dims) == 1:  # Known to have elements of only one dimension
                    _codim = list(domain_dims)[0]
                else:
                    _codim = None  # Cannot infer a single codim, accept any type of values
            else:
                _codim = codim

            mapping_t = tuple_safe(mapping, arities=_codim, convert=frp)
            arities = getattr(mapping_t, 'arity')

            if codim is None and arities[0] == arities[1]:
                _codim = arities[0]

            if _codim == 1:  # Account for scalar functions from user
                if domain is not None and not has_domain_set:
                    # domain is a function assumed to take a scalar, so we unwrap it
                    original_domain = self._domain
                    self._domain = lambda v: original_domain(as_scalar_weak(v))

            if dim is None and target_dim is None:
                _dim = None
            elif dim is None:
                _dim = _codim + target_dim if _codim is not None else None  # type: ignore
            elif target_dim is None:
                if _codim is not None and dim <= _codim:
                    raise ConstructionError('Specified dim for conditional FRPtoo small (must include input length), '
                                            'perhaps you meant to give the target_dim instead')
                _dim = dim
            elif _codim is not None and _codim != dim - target_dim:
                raise ConstructionError('Both dim and target_dim given but inconsistent, '
                                        'should have codim + target_dim = dim')
            else:
                if _codim is None:
                    if target_dim >= dim:
                        raise ConstructionError(f'target_dim {target_dim} should be smaller than dim {dim} '
                                                'for a Conditional FRP')
                    _codim = dim - target_dim  # Use this to infer codim, it's equivalent
                _dim = dim

            self._codim = _codim
            self._dim = _dim
            self._has_domain_set = has_domain_set
            if target_dim is not None:
                self._target_dim = target_dim
            elif _codim is not None and _dim is not None:
                self._target_dim = _dim - _codim
            else:
                self._target_dim = None

            assert callable(mapping)  # For mypy

            def fn(*args) -> FRP:
                n = len(args)
                if n == 1 and is_tuple(args[0]):
                    args = args[0]
                    n = len(args)
                value = as_quant_vec(args)  # ATTN: should this be as_vec_tuple??

                if self._codim is not None and n != self._codim:
                    raise MismatchedDomain(f'A value of invalid dimension {n} was passed to a'
                                           f' conditional FRP of codimension {self._codim}.')
                if not self._trivial_domain and not self._domain(value):
                    raise MismatchedDomain(f'Supplied value {value} not in domain of conditional FRP.')

                if not self._auto_clone and value in self._mapping:
                    return self._mapping[value]
                try:
                    result = cast('FRP', mapping_t(value))
                except Exception as e:
                    raise MismatchedDomain(f'encountered a problem passing {value} to a conditional FRP:\n  {str(e)}')

                extended = result.transform(Prepend(value))  # Input pass through

                if self._auto_clone:
                    extended = extended.clone()
                else:
                    self._mapping[value] = extended   # Cache, fn should be pure
                    self._targets[value] = result     # Store unextended to ease some operations
                return extended

            def tfn(*args) -> FRP:
                n = len(args)
                if n == 1 and is_tuple(args[0]):
                    args = args[0]
                    n = len(args)
                value = as_quant_vec(args)  # ATTN: should this be as_vec_tuple??

                if self._codim is not None and n != self._codim:
                    raise MismatchedDomain(f'A value of invalid dimension {n} was passed to a'
                                           f' conditional FRP of codimension {self._codim}.')
                if not self._trivial_domain and not self._domain(value):
                    raise MismatchedDomain(f'Supplied value {value} not in domain of conditional FRP.')

                if not self._auto_clone and value in self._targets:
                    return self._targets[value]
                try:
                    result = cast('FRP', mapping_t(value))
                except Exception as e:
                    raise MismatchedDomain(f'encountered a problem passing {value} to a conditional FRP:\n  {str(e)}')

                if self._auto_clone:
                    result = result.clone()
                else:
                    extended = result.transform(Prepend(value))  # Input pass through
                    self._mapping[value] = extended   # Cache, fn should be pure
                    self._targets[value] = result     # Store unextended to ease some operations
                return result   # on auto_clone do a clone() here

            self._fn = fn
            self._target_fn = tfn

    def __call__(self, *value) -> FRP:
        return self._fn(*value)

    def __getitem__(self, *value) -> FRP:
        "Returns this conditional Kind's target associated with the key."
        return self._target_fn(*value)

    def target(self, *value) -> FRP:
        return self._target_fn(*value)

    @property
    def dim(self):
        return self._dim

    @property
    def codim(self):
        return self._codim

    @property
    def type(self):
        codim = f'{self._codim}' if self._codim is not None else '*'

        if self._dim is not None:
            dim = f'{self._dim}'
        elif self._codim is None and self._dim is None and self._target_dim is not None:
            dim = f'* + {self._target_dim}'
        else:
            dim = '*'

        return f'{codim} -> {dim}'

    def is_in_domain(self, v):
        """Tests whether a value belongs to the specified domain of a Conditional Kind.

        If the domain was not specified, this will return True for every value.

        """
        return self._domain(as_vec_tuple(v))

    def conditional_kind_of(self) -> 'ConditionalKind':
        "Computes the conditional Kind of this conditional FRP. Warning: Evaluates target Kinds."
        if self._is_dict:
            c_kind = {k: kind(v) for k, v in self._targets.items()}
            return ConditionalKind(c_kind, codim=self._codim, dim=self._dim, domain=c_kind.keys())

        def c_kind_fn(value):
            return kind(self._target_fn(value))

        if self._has_domain_set:
            domain = self._domain_set

            # If we've evaluated the whole domain, convert to a dictionary
            if domain == set(self._targets.keys()):
                c_kind = {k: kind(v) for k, v in self._targets.items()}
                return ConditionalKind(c_kind, codim=self._codim, dim=self._dim, domain=domain)
        else:
            domain = self._domain   # type: ignore

        return ConditionalKind(c_kind_fn, codim=self._codim, dim=self._dim, domain=domain)

    def clone(self) -> 'ConditionalFRP':
        if self._is_dict:
            cloned = {k: v.clone() for k, v in self._targets.items()}
            return ConditionalFRP(cloned, codim=self._codim, dim=self._dim, domain=self._domain,
                                  auto_clone=self._auto_clone)
        else:
            # NB! We clone here out of caution, in case a function returns an existing FRP
            # The ConditionalFRP will cache the results for each one, so clone will only
            # be called at most one extra time, assuming cache is True..

            def fn(value):
                return self._target_fn(value).clone()

            return ConditionalFRP(fn, codim=self._codim, dim=self._dim, domain=self._domain,
                                  auto_clone=self._auto_clone)

    @property
    def expectation(self) -> Statistic:
        """Returns a statistic from values to the expectation of the corresponding target FRP.

        Note that for a lazily evaluated FRP, it may be costly to compute the expectation
        so this will fail with a warning. See the forced_expectation and approximate_expectation
        methods for alternatives in that case.

        This sets the codim and dim of the statistic based on what is known about
        this conditional FRP. They may be None if unavailable; codim will typically be a tuple.
        The domain of the returned function is also specified as an attribute.

        """
        if self._codim is not None and self._dim is not None:
            my_dim = self._dim - self._codim
        elif self._target_dim is not None:
            my_dim = self._target_dim
        else:
            my_dim = None

        @statistic(codim=self._codim, dim=my_dim)
        def fn(*x):
            "the expectation of a conditional FRP as a function of its values"
            frp = self._target_fn(*x)
            return frp.expectation

        setattr(fn, 'domain', self._domain if not self._trivial_domain else None)

        return fn

    def forced_expectation(self) -> Statistic:
        """Returns a statistic from values to the expectation of the corresponding FRP.

        This forces computation of the expectation even if doing so
        is computationally costly. See expectation and approximate_expectation
        properties for alternatives in that case.

        This sets the codim and dim of the statistic based on what is known about
        this conditional FRP. They may be None if unavailable; codim will typically be a tuple.
        The domain of the returned function is also specified as an attribute.

        """
        if self._codim is not None and self._dim is not None:
            my_dim = self._dim - self._codim
        elif self._target_dim is not None:
            my_dim = self._target_dim
        else:
            my_dim = None

        @statistic(codim=self._codim, dim=my_dim)
        def fn(*x):
            "the expectation of a conditional FRP as a function of its values"
            frp = self._target_fn(*x)
            return frp.forced_expectation()

        setattr(fn, 'domain', self._domain if not self._trivial_domain else None)

        return fn

    def approximate_expectation(self, tolerance=0.01) -> Statistic:
        """Returns a statistic from values to the approximate expectation of the corresponding FRP.

        The approximation is computed to the specified tolerance
        using an appropriate number of samples. See expectation and
        approximate_expectation properties for alternatives in that
        case.

        This sets the codim and dim of the statistic based on what is known about
        this conditional FRP. They may be None if unavailable; codim will typically be a tuple.
        The domain of the returned function is also specified as an attribute.

        """
        if self._codim is not None and self._dim is not None:
            my_dim = self._dim - self._codim
        elif self._target_dim is not None:
            my_dim = self._target_dim
        else:
            my_dim = None

        @statistic(codim=self._codim, dim=my_dim)
        def fn(*x):
            "the expectation of a conditional FRP as a function of its values"
            frp = self._target_fn(*x)
            return frp.approximate_expectation(tolerance)

        setattr(fn, 'domain', self._domain if not self._trivial_domain else None)

        return fn

    @property
    def conditional_entropy(self) -> Statistic:
        """Returns a statistic from values to the entropy of the corresponding target FRP.

        This sets the codim of the statistic based on what is known about
        this conditional FRP. This may be None if unavailable; codim will typically be a tuple.
        The domain of the returned function is also specified as an attribute.

        """
        @statistic(codim=self._codim, dim=1)
        def fn(*x):
            "the expectation of a conditional FRP as a function of its values"
            frp = self._target_fn(*x)
            return frp.entropy

        setattr(fn, 'domain', self._domain if not self._trivial_domain else None)

        return fn

    def __str__(self) -> str:
        # if dict put out a table of values and FRP summaries in dictionary order
        # if callable, put out what information we have
        tbl = '\n'.join('  {value:<16s}  {frp:<s}'.format(value=str(k), frp='A fresh FRP' if v.is_fresh else str(v))
                        for k, v in sorted(self._targets.items(), key=lambda item: tuple(item[0]))
                        if self._domain(k))
        dlabel = f' with domain={str(self._domain_set)}.' if self._has_domain_set else ''
        tlabel = f' of type {self.type}'

        if self._is_dict or (self._has_domain_set and self._domain_set == set(self._mapping.keys())):
            return f'A conditional FRP{tlabel} with wiring:\n{tbl}'
        elif tbl:
            cont = '  {value:<16s}  {frp:<s}'.format(value='...', frp='...more FRPs')
            mlabel = f'\nIt\'s wiring includes:\n{tbl}\n{cont}'
            return f'A conditional FRP{tlabel} as a function{dlabel or mlabel or "."}'
        else:
            return f'A conditional FRP as a function{dlabel or "."}'

    def __frplib_repr__(self):
        if environment.ascii_only:
            return str(self)
        return Panel(str(self), expand=False, box=rich_box.SQUARE)

    def __repr__(self) -> str:
        if environment.is_interactive:
            return str(self)
        label = ''
        if self._codim is not None:
            label = label + f', codim={repr(self._codim)}'
        if self._dim is not None:
            label = label + f', dim={repr(self._dim)}'
        if self._target_dim is not None:
            label = label + f', dim={repr(self._target_dim)}'
        if self._has_domain_set:
            label = label + f', domain={repr(self._domain_set)}'
        else:
            label = label + f', domain={repr(self._domain)}'
        label += f', auto_clone={self._auto_clone}'
        if self._is_dict or (self._has_domain_set and self._domain_set == set(self._mapping.keys())):
            return f'ConditionalFRP({repr(self._targets)}{label})'
        else:
            return f'ConditionalFRP({repr(self._target_fn)}{label})'

    # FRP operations lifted to Conditional FRPs

    def transform(self, statistic):
        if not isinstance(statistic, Statistic):
            raise FrpError('A conditional FRP can be transformed only by a Statistic.'
                           ' Consider passing this tranform to `conditional_frp` first.')
        lo, hi = statistic.codim
        if self._dim is not None and (self._dim < lo or self._dim > hi):
            raise FrpError(f'Statistic {statistic.name} is incompatible with this conditional FRP: '
                           f'acceptable dimensions [{lo},{hi}] but dimension is {self._dim}.')

        if self._trivial_domain:
            domain: set[ValueType] | Callable[[ValueType], bool] | None = None
        elif self._has_domain_set:
            domain = self._domain_set
        else:
            domain = self._domain

        s_dim = statistic.dim

        if self._is_dict:
            f_mapping = {k: statistic(v) for k, v in self._mapping.items()}
            return ConditionalFRP(f_mapping, codim=self._codim, target_dim=s_dim, domain=domain,
                                  auto_clone=self._auto_clone)

        if self._dim is not None:
            def transformed(*value):
                return statistic(self._fn(*value))
        else:  # We have not vetted the dimension, so apply with care
            def transformed(*value):
                try:
                    return statistic(self._fn(*value))
                except Exception:
                    raise FrpError(f'Statistic {statistic.name} appears incompatible with this conditional FRP.')

        return ConditionalFRP(transformed, codim=self._codim, target_dim=s_dim, domain=domain,
                              auto_clone=self._auto_clone)

    def __xor__(self, statistic):
        return self.transform(statistic)

    def transform_targets(self, statistic):
        if not isinstance(statistic, Statistic):
            raise FrpError('A conditional FRP can be transformed only by a Statistic.'
                           ' Consider passing this tranform to `conditional_frp` first.')
        lo, hi = statistic.codim
        have_dim_codim = self._dim is not None and self._codim is not None
        if have_dim_codim or self._target_dim is not None:
            d = self._dim - self._codim if have_dim_codim else self._target_dim  # type: ignore
            if d < lo or d > hi:                                                 # type: ignore
                raise FrpError(f'Statistic {statistic.name} is incompatible with this conditional FRP: '
                               f'acceptable dimension [{lo},{hi}] but target FRP dimension {d}.')

        if self._trivial_domain:
            domain: set[ValueType] | Callable[[ValueType], bool] | None = None
        elif self._has_domain_set:
            domain = self._domain_set
        else:
            domain = self._domain

        s_dim = statistic.dim

        if self._is_dict:
            f_mapping = {k: statistic(v) for k, v in self._targets.items()}
            return ConditionalFRP(f_mapping, codim=self._codim, target_dim=s_dim, domain=domain,
                                  auto_clone=self._auto_clone)

        if self._dim is not None:
            def transformed(*value):
                return statistic(self._target_fn(*value))
        else:  # We have not vetted the dimension, so apply with care
            def transformed(*value):
                try:
                    return statistic(self._target_fn(*value))
                except Exception:
                    raise FrpError(f'Statistic {statistic.name} appears incompatible with this conditional FRP.')

        return ConditionalFRP(transformed, codim=self._codim, target_dim=s_dim, domain=domain,
                              auto_clone=self._auto_clone)

    def __rshift__(self, cfrp):
        if not isinstance(cfrp, ConditionalFRP):
            return NotImplemented

        if self._dim != cfrp._codim:
            raise FrpError('Incompatible mixture of conditional FRPs, '
                           f'{self.type} does not match {cfrp.type}')

        if self._has_domain_set:
            domain: set[ValueType] | Callable[[ValueType], bool] | None = self._domain_set
        elif not self._trivial_domain:
            domain = self._domain
        else:
            domain = None

        # ATTN: Can optimize for the case where self._codim is not None
        # proj = drop_input(self._codim)

        if self._is_dict or (self._has_domain_set and self._domain_set == set(self._mapping.keys())):
            mapping = {given: (frp >> cfrp).transform(drop_input(len(given)))
                       for given, frp in self._mapping.items()}
            return ConditionalFRP(mapping, codim=self._codim, dim=cfrp._dim, domain=domain,
                                  auto_clone=self._auto_clone)

        def mixed(*given):
            return (self(*given) >> cfrp).transform(drop_input(len(given)))
        return ConditionalFRP(mixed, codim=self._codim, dim=cfrp._dim, domain=domain,
                              auto_clone=self._auto_clone)

    def __mul__(self, cfrp):
        if not isinstance(cfrp, ConditionalFRP):
            return NotImplemented

        if self._codim is None or cfrp._codim != self._codim:
            raise FrpError('For conditional FRPs, * requires both to have same codimensions')

        if self._dim is None or cfrp._dim is None:
            mdim: int | None = None
        else:
            mdim = self._dim + cfrp._dim - cfrp._codim

        if self._has_domain_set and cfrp._has_domain_set:
            domain = self._domain_set & cfrp._domain_set
        else:
            # ATTN: domain function should also be checked and used where appropriate
            domain = None

        if self._is_dict and cfrp._is_dict:
            s_domain = (self._has_domain_set and self._domain_set) or self._mapping.keys()
            c_domain = (cfrp._has_domain_set and cfrp._domain_set) or cfrp._mapping.keys()
            intersecting = s_domain & c_domain
            mapping = {given: self._targets[given] * cfrp._targets[given] for given in intersecting}

            return ConditionalFRP(mapping, codim=self._codim, dim=mdim, domain=domain,
                                  auto_clone=self._auto_clone)

        def mixed(*given):
            return self._target_fn(*given) * cfrp._target_fn(*given)

        return ConditionalFRP(mixed, codim=self._codim, dim=mdim, domain=domain,
                              auto_clone=self._auto_clone)

    def __pow__(self, n, modulo=None):
        if not isinstance(n, int):
            return NotImplemented

        if n < 0:
            raise FrpError('For conditional FRPs, ** requires a non-negative power')

        if self._target_dim is None:
            tdim: int | None = None
        else:
            tdim = self._target_dim * n

        if self._has_domain_set:
            domain = self._domain_set
        else:
            domain = None

        if self._is_dict:
            s_domain = domain or self._mapping.keys()
            mapping = {given: self._targets[given] ** n for given in s_domain}

            return ConditionalFRP(mapping, codim=self._codim, target_dim=tdim, domain=domain or self._domain,
                                  auto_clone=self._auto_clone)

        def mixed(*given):
            return self._target_fn(*given) ** n

        return ConditionalFRP(mixed, codim=self._codim, target_dim=tdim, domain=domain or self._domain,
                              auto_clone=self._auto_clone)

# # Original
# def conditional_frp(
#         mapping: CondFrpInput | ConditionalFRP | None = None,  # Callable[[ValueType], 'FRP'] | dict[ValueType, 'FRP'] | dict[QuantityType, 'FRP'] | ConditionalKind | None = None,
#         *,
#         codim: int | None = None,  # If set to 1, will pass a scalar not a tuple to fn (not dict)
#         dim: int | None = None,
#         domain: Iterable[ValueType] | Iterable[QuantityType] | Callable[[ValueType], bool] | None = None,
#         target_dim: int | None = None,
#         auto_clone: bool = False   # ATTN: Not yet used, if True, clone on every evaluation, e.g., in simulation
# ) -> ConditionalFRP | Callable[..., ConditionalFRP]:

@overload
def conditional_frp(
        mapping: None = None,  # Callable[[ValueType], 'FRP'] | dict[ValueType, 'FRP'] | dict[QuantityType, 'FRP'] | ConditionalKind | None = None,
        *,
        codim: int | None = None,  # If set to 1, will pass a scalar not a tuple to fn (not dict)
        dim: int | None = None,
        domain: Iterable[ValueType] | Iterable[QuantityType] | Callable[[ValueType], bool] | None = None,
        target_dim: int | None = None,
        auto_clone: bool = False   # ATTN: Not yet used, if True, clone on every evaluation, e.g., in simulation
) -> Callable[..., ConditionalFRP]:
    ...

@overload
def conditional_frp(
        mapping: CondFrpInput | ConditionalFRP,  # Callable[[ValueType], 'FRP'] | dict[ValueType, 'FRP'] | dict[QuantityType, 'FRP'] | ConditionalKind | None = None,
        *,
        codim: int | None = None,  # If set to 1, will pass a scalar not a tuple to fn (not dict)
        dim: int | None = None,
        domain: Iterable[ValueType] | Iterable[QuantityType] | Callable[[ValueType], bool] | None = None,
        target_dim: int | None = None,
        auto_clone: bool = False   # ATTN: Not yet used, if True, clone on every evaluation, e.g., in simulation
) -> ConditionalFRP:
    ...

def conditional_frp(
        mapping = None,  # Callable[[ValueType], 'FRP'] | dict[ValueType, 'FRP'] | dict[QuantityType, 'FRP'] | ConditionalKind | None = None,
        *,
        codim = None,  # If set to 1, will pass a scalar not a tuple to fn (not dict)
        dim = None,
        domain = None,
        target_dim = None,
        auto_clone = False
):
    """Converts a mapping from values to FRPs into a conditional FRP.

    The mapping can be a dictionary associating values (scalars or vector tuples)
    to FRPs, a function associating values to FRPs, or a conditional Kind.
    This can also be used as a decorator on a function definition.

    The dictionaries can be specified with scalar keys as these are automatically
    wrapped in a tuple. If you want the function to accept a scalar argument
    rather than a tuple (even 1-dimensional), you should supply codim=1.

    The function *should* return the *same* FRP each time it is called with any
    particular value, but by default, results are cached, so this should not
    cause problems if violated.  The auto_clone option provides  a mechanism
    for cloning on every evaluation, see below.

    Currently, a function being wrapped should take a single argument
    which will be a tuple, or if codim=1, a scalar.

    Parameters:

    codim: int | None -- the codimension of the conditional FRP, i.e., the dimension
        of the input values. If not specified (None), then any length tuple
        is accepted. If set explicitly to 1, then a wrapped function should accept
        a scalar argument.  (Default: None)

    dim: int | None -- the final dimension of the mixture FRP. If None, the dimension
        is unknown and unconstrained.

    target_dim: int | None -- the dimension of the target FRPs. This can be supplied
        in lieu of dim and is often more convenient.

    domain -- the domain of the conditional FRP; either an iterable or a predicate
        that returns true for a valid input.

    auto_clone: bool -- if True, every evaluation of the mapping or targets
        are automatically cloned. The primary use case for this option, which
        defaults to False, is for simulations one wants to reuse the conditional
        FRPs. (Default: False)

    If mapping is missing, this function can acts as a decorator on the
    function definition following. If mapping is a conditional FRP and none
    of its attributes are being changed by the other arguments, return it as is.

    Returns a ConditionalFRP (if mapping given) or a decorator.

    """
    if mapping is not None:
        # Accept ConditionalFRP and ConditionalKind (which are callable)
        # and a general callable but not Statistics
        if isinstance(mapping, Statistic):
            raise ConstructionError('Cannot create Conditional FRP from a Statistic.')
        elif not callable(mapping) and not isinstance(mapping, dict):
            raise ConstructionError('Cannot create Conditional FRP from the given '
                                    f'object of type {type(mapping).__name__}')

        if isinstance(mapping, ConditionalFRP):
            if codim is None and dim is None and target_dim is None and\
               domain is None and auto_clone == mapping._auto_clone:
                return mapping  # No changes so return as is, for cloning use clone

            codim = mapping._codim if codim is None else codim
            dim = mapping._dim if dim is None else dim
            target_dim = mapping._target_dim if target_dim is None else target_dim
            if domain is None and not mapping._trivial_domain:
                domain = mapping._domain_set if mapping._has_domain_set else mapping._domain
            if mapping._is_dict:
                mapping = mapping._targets
            else:
                mapping = mapping.target

        return ConditionalFRP(mapping, codim=codim, dim=dim, target_dim=target_dim,
                              domain=domain, auto_clone=auto_clone)

    def decorator(fn: Callable) -> ConditionalFRP:
        return ConditionalFRP(fn, codim=codim, dim=dim, target_dim=target_dim,
                              domain=domain, auto_clone=auto_clone)
    return decorator


#
# FRPs
#

class EmptyFrpDescriptor:  # Enables FRP.empty to belong to FRP class
    def __get__(self, obj, objtype=None):
        return objtype(Kind.empty)

#
# FRPs are logically immutable but the _kind and _expression properties
# are computed lazily and thus can be mutated. If available, only the
# _kind is needed to sample, but if this is too complex, we use the
# _expression steps to generate samples. See FrpExpression and its
# subclasses.
#

class FRP:
    COMPLEXITY_THRESHOLD = 16384  # Maximum size to maintain kindedness (was 1024)
    EVOLUTION_THRESHOLD = 128     # Evolving FRP for more steps activates intermediates

    def __init__(self, create_from: FRP | FrpExpression | Kind | str) -> None:
        if not create_from:  # Kind.empty or FRP.empty or ''
            self._kind: Kind | None = Kind.empty
            self._expr: FrpExpression | None = None
            self._value: ValueType | None = vec_tuple()
            return

        if isinstance(create_from, FRP):
            # Note: unlike frp() which is idempotent on FRPs, this gives a fresh copy
            if create_from._expr is not None:
                expr = create_from._expr
                if create_from.is_kinded():
                    expr._cached_kind = create_from.kind
                expr._cached_value = None
                create_from = expr
            elif create_from.is_kinded():
                create_from = create_from.kind
            else:
                raise ConstructionError('Cannot create an FRP without a Kind or expression')

        if isinstance(create_from, FrpExpression):
            self._expr = create_from
            self._kind = create_from._cached_kind    # Computed Lazily
            self._value = None
        else:
            self._kind = Kind(create_from)
            self._expr = None
            self._value = None

    @classmethod
    def activate(cls, frp: FRP) -> FRP:
        frp.value  # Force the value
        return frp

    @classmethod
    def sample(cls, n: int, frp: FRP | Kind | SupportsKindOf | str, summary=True) -> FrpDemoSummary | FrpDemo:
        """Run a demo of `n` FRPs and tabulate the results.

        If an FRP is given, the FRPs in the demo are clones of the given FRP.
        If a Kind is given, the FRPs in the demo have that Kind.
        If given a string that can be converted a Kind, use the conversion.

        If summary is True, then the table gives counts and proportions.
        Otherwise, it lists all the individual FRP's values.

        Examples:
        + FRP.sample(10_000, X_an_FRP)
        + FRP.sample(10_000, K_a_Kind)
        + FRP.sample(10, X_an_FRP, summary=False)

        """
        if isinstance(frp, Kind):
            return _sample_from_kind(n, frp, summary)

        if isinstance(frp, FRP):
            if frp._kind is not None:
                return _sample_from_kind(n, frp._kind, summary)
            assert frp._expr is not None
            return _sample_from_expr(n, frp._expr, summary)

        if isinstance(frp, SupportsKindOf):
            return _sample_from_kind(n, frp.kind_of(), summary)

        if isinstance(frp, str):
            return _sample_from_kind(n, kind(frp), summary)

        raise FrpError(f'I do not know how to sample from a {type(frp)}')

    @classmethod
    def sample1(cls, frp: FRP) -> ValueType:
        one_sample = cast(FrpDemo, cls.sample(1, frp, summary=False))
        return as_vec_tuple(one_sample[0])  # ATTN: Wrapping not needed after Quantity conversion

    @property
    def value(self) -> ValueType:
        if self._value is None:
            self._value = VecTuple(self._get_value())  # ATTN: VecTuple not be needed after Quantity conversion
        return self._value

    @property
    def size(self) -> int:
        "Returns the size of the FRP's kind. The kind is computed if not yet available."
        if self._kind is None:
            assert self._expr is not None
            self._kind = self._expr.kind()
        return self._kind.size

    @property
    def dim(self) -> int:
        "Returns the FRP's dimension. The value is computed if the Kind is not available."
        if self._kind is None:
            if self._expr is not None and self._expr._cached_kind is not None:
                return self._expr._cached_kind.dim
            elif self._expr is not None and self._expr._cached_value is not None:
                return len(self._expr._cached_value)
            else:
                return len(self.value)  # The value is likely cheaper than the kind to produce here
        return self._kind.dim

    @property
    def codim(self):
        "The codimension of this FRP."
        return 0

    @property
    def type(self):
        return f'0 -> {self.dim}'

    @property
    def kind(self) -> Kind:
        if self._kind is None:
            assert self._expr is not None
            self._kind = self._expr.kind()
        return self._kind

    @property
    def is_fresh(self) -> bool:
        """True if this FRP does not yet have a value.

        Note that by default frp() produces ``eager'' FRPs that may be
        implicitly activated when it is convenient.

        """
        val = self._get_cached_value()
        return val is None

    @property
    def expectation(self):
        """Returns the expectation of this FRP, unless computationally inadvisable.

        For lazily-computed FRPs, this attempts to compute the expectation *without*
        computing the kind explicitly. This is often but not always possible.
        If computing the kind is required, this raises a ComplexExpectationWarning
        exception.

        To force computation of the expectation in this case, use the
        forced_expectation property. See also the approximate_expectation()
        method, which may be good enough.

        """
        if self.is_kinded():
            return self.kind.expectation
        else:
            assert self._expr is not None
            return _expectation_from_expr(self._expr)

    def forced_expectation(self):
        "Returns the expectation of this FRP, computing the kind if necessary to do so."
        try:
            return self.expectation
        except ComplexExpectationWarning:
            return self.kind.expectation

    def approximate_expectation(self, tolerance=0.01) -> ValueType:
        "Computes an approximation to this FRP's expectation to the specified tolerance."
        n = int(math.ceil(tolerance ** -2))
        return scalarize(sum(FRP.sample(n, self, summary=False)) / as_real(n))  # type: ignore

    @property
    def entropy(self) -> QuantityType:
        "The entropy of this FRP. Currently, this requires that the Kind be computable."
        if self.is_kinded():
            return self.kind.entropy
        else:
            assert self._expr is not None
            if self._expr._cached_kind is not None:
                return self._expr._cached_kind.entropy
            raise FrpError("entropy current requires that an FRP's Kind be computable; that is not apparent here.")

    empty = EmptyFrpDescriptor()

    def __str__(self) -> str:
        if self._kind == Kind.empty:
            return 'The empty FRP with value <>'
        if self._kind is not None:
            return (f'An FRP with value {show_tuple(self.value, max_denom=10)}')
        return f'An FRP with value {show_tuple(self.value, max_denom=10)}. (It may be slow to evaluate its kind.)'

    def __frplib_repr__(self) -> str:
        if self._kind == Kind.empty:
            return ('The [bold]empty FRP[/] of dimension [#3333cc]0[/] with value [bold #4682b4]<>[/]')
        if self._kind is not None:
            return (f'An [bold]FRP[/] with value [bold #4682b4]{self.value}[/]')
        return f'An [bold]FRP[/] with value [bold #4682b4]{self.value}[/]. (It may be slow to evaluate its kind.)'

    def __repr__(self) -> str:
        if environment.is_interactive:
            return f'FRP(value={show_tuple(self.value, max_denom=10)})'
        return super().__repr__()

    def __bool__(self) -> bool:
        return self.dim > 0

    def __iter__(self):
        yield from self.value

    def _get_value(self):
        "Like FRP.sample1 but gets actual value from an expression. Only call if _value is None."
        # An expression can have a stored Kind, so we check its value first
        if self._expr is not None:
            return self._expr.value()

        if self._kind is not None:
            return FRP.sample1(self)

        # This would be a violation of the invariant that at least one of _kind or _expr exists
        raise FrpError('FRP is missing both expression and Kind, so cannot get a value.')

    def _get_cached_value(self):
        """Refreshes cached value of an expression tree without generating a value.

        If an expression has a cached value, this will update an empty ._value field .

        """
        if self._value is None and self._expr is not None:
            val = self._expr._refresh_cached_value()
            if val is not None:
                self._value = val
        return self._value

    def is_kinded(self):
        """Returns true if this FRP has a Kind that can be efficiently obtained.

        This will be True if the FRP was constructed directly from a Kind,
        but also if the FRP is built from an expression whose Kind has already
        been found.

        When this returns True, it is safe to use self.kind to look at the
        Kind of this FRP as it will not spawn a potentially long calculation.
        One should use the .kind property, not other internal fields, as
        the Kind might be obtained in several ways.

        """
        return self._kind is not None or (self._expr is not None and self._expr._cached_kind is not None)

    def clone(self) -> FRP:
        if self.is_kinded():
            new_frp = FRP(self.kind)
        else:
            assert self._expr is not None   # Grrr mypy...
            new_frp = FRP(self._expr.clone())
            new_frp._kind = self._kind or self._expr._cached_kind  # If already computed, use it.
        return new_frp

    # Operations and Operators on FRPs that mirrors the same for Kinds
    # These all produce new FRPs. We use an expression for the FRPs
    # because these operations relate both the kinds *and* the values.
    # ATTN: when a Kind is useful but not demand, we will compute
    # the kind if the complexity is below a threshold.

    def independent_mixture(self, frp: FRP) -> FRP:
        if self.is_fresh or frp.is_fresh:
            value = None
        else:
            value = join_values([self.value, frp.value])

        our_kind: Union[Kind, None] = None
        if self.is_kinded() and frp.is_kinded():
            k1 = self.kind
            k2 = frp.kind
            if k1.size * k2.size <= self.COMPLEXITY_THRESHOLD:
                our_kind = k1 * k2

        # ATTN:Issue 43 if self and frp are expressions that happen
        # to be Kinded, we probably want to create this as an
        # expression. Moreover, it's not obviously a good idea to
        # generate the values in the first case.

        if our_kind is not None and value is not None:
            spec: Union[Kind, IMixtureExpression] = our_kind
        else:
            if isinstance(self._expr, IMixtureExpression) and isinstance(frp._expr, IMixtureExpression):
                spec = IMixtureExpression.join(self._expr, frp._expr)
            elif isinstance(self._expr, IMixtureExpression):
                spec = IMixtureExpression.append(self._expr, as_expression(frp))
            elif isinstance(frp._expr, IMixtureExpression):
                spec = IMixtureExpression.prepend(frp._expr, as_expression(self))
            else:
                spec = IMixtureExpression([as_expression(self), as_expression(frp)])

            spec._cached_kind = our_kind
            spec._cached_value = value

        result = FRP(spec)
        if value is not None:
            result._value = value
        if our_kind is not None and result._kind is None:
            result._kind = our_kind
        return result

    def __mul__(self, other):   # Self -> FRP -> FRP
        "Mixes FRP with another independently"
        if not isinstance(other, FRP):
            return NotImplemented
        return self.independent_mixture(other)

    def __pow__(self, n, modulo=None):  # Self -> int -> FRP
        is_kinded = self.is_kinded()
        if is_kinded and (self.size == 0 or math.log2(self.size) * n <= math.log2(self.COMPLEXITY_THRESHOLD)):
            return FRP(self.kind ** n)

        if not is_kinded and isinstance(self._expr, IMixPowerExpression):
            expr = IMixPowerExpression(self._expr._term, self._expr._pow + n)
        else:
            expr = IMixPowerExpression(as_expression(self), n)
        return FRP(expr)

    def __rshift__(self, c_frp):
        "Mixes this FRP with a Conditional FRP (or a function/dict giving an FRP for each value)"
        if isinstance(c_frp, ConditionalKind):
            raise FrpError('A mixture with an FRP requires a conditional FRP on the right of >> '
                           'but a conditional Kind was given. Try kind(f) >> c or f >> conditional_frp(c).')

        if not callable(c_frp) and not isinstance(c_frp, dict):
            return NotImplemented

        if not isinstance(c_frp, ConditionalFRP):
            try:
                c_frp = conditional_frp(c_frp)
            except ConstructionError:
                return NotImplemented
            except Exception as e:
                raise FrpError(f'In an mixture with an FRP, there was a problem '
                               f'obtaining a conditional FRP:\n  {str(e)}')

        mix_kind: Kind | None = None
        mixer_val = self._get_cached_value()
        if mixer_val is not None:
            try:
                target_val = c_frp.target(mixer_val)._get_cached_value()
            except Exception as e:
                raise FrpError(f'In a mixture, conditional FRP appears incompatible with mixer '
                               f'at value {mixer_val}:\n  {str(e)}')
        else:
            target_val = None

        if self.is_kinded():
            my_kind = self.kind
            dim = my_kind.dim
            if c_frp._codim is not None and c_frp._codim != dim:
                FrpError(f'Incompatible mixture of dim {dim} FRP with codim {c_frp._codim} conditional FRP')

            make_kinded = True
            targets = {}
            for branch in my_kind._branches:
                try:
                    target = c_frp.target(branch.vs)
                except Exception as e:
                    raise FrpError(f'In a mixture, conditional FRP appears incompatible with mixer '
                                   f'at value {branch.vs}:\n  {str(e)}')

                if not target.is_kinded() or (dim * target.kind.dim > self.COMPLEXITY_THRESHOLD):
                    make_kinded = False
                    break
                targets[branch.vs] = target

            if make_kinded:   # Return a Kinded FRP
                c_kind = ConditionalKind({val: frp.kind for val, frp in targets.items()}, codim=dim)
                mix_kind = my_kind >> c_kind

        if mix_kind is not None and target_val is not None:
            result = FRP(mix_kind)
            result._value = VecTuple.concat(mixer_val, target_val)
        else:
            expr = MixtureExpression(as_expression(self), c_frp)
            result = FRP(expr)
            if target_val is not None:
                result._value = VecTuple.concat(mixer_val, target_val)
            if mix_kind is not None:
                result._kind = mix_kind
        return result

    def transform(self, f_mapping):
        "Applies a transform/Statistic to an FRP"
        if isinstance(f_mapping, Statistic):
            if self.is_kinded():  # ensures dim check is cheap
                fdim_lo, fdim_hi = f_mapping.codim
                if self.dim < fdim_lo or self.dim > fdim_hi:
                    raise MismatchedDomain(f'Statistic {f_mapping.name} is incompatible with this FRP: '
                                           f'acceptable dimension [{fdim_lo},{fdim_hi}] but FRP dimension {self.dim}.')
            else:  # check compatibility if value available but do not generate it
                val = self._get_cached_value()
                if val is not None:
                    try:
                        f_mapping(val)
                    except Exception:
                        raise MismatchedDomain(f'Statistic {f_mapping.name} is incompatible with this FRP: '
                                               f'could not evaluate it on the FRPs value.')
            stat = f_mapping
        elif callable(f_mapping) and not isinstance(f_mapping, (ConditionalKind, ConditionalFRP)):
            stat = Statistic(f_mapping)
        else:
            raise ConstructionError('Transforming an FRP requires a statistic or related function')

        val = self._get_cached_value()
        kinded = self.is_kinded()
        if kinded and val is not None:
            result = FRP(self.kind ^ stat)
            result._value = stat(val)
        else:
            result = FRP(TransformExpression(stat, as_expression(self)))
            if kinded:
                result._kind = self.kind ^ stat
            if val is not None:
                result._value = stat(val)
        return result

    def __xor__(self, f_mapping):
        "Applies a transform/Statistic to an FRP"
        return self.transform(f_mapping)

    def __rfloordiv__(self, c_frp):
        "Conditioning on self; other is a conditional FRP."
        d = self.dim
        return self >> c_frp ^ Proj[(d + 1):]

    @overload
    def marginal(self, *__indices: int) -> FRP:
        ...

    @overload
    def marginal(self, __subspace: Iterable[int] | Projection | slice) -> FRP:
        ...

    def marginal(self, *index_spec) -> FRP:
        dim = self.dim

        # Unify inputs
        if len(index_spec) == 0:
            return FRP.empty
        if isinstance(index_spec[0], Iterable):
            indices: tuple[int, ...] = tuple(index_spec[0])
        elif isinstance(index_spec[0], Projection):
            indices = tuple(index_spec[0].subspace)
        elif isinstance(index_spec[0], slice):
            start, stop, step = index_spec[0].indices(dim + 1)
            indices = tuple(range(max(start, 1), stop, step))
        else:
            indices = index_spec

        if len(indices) == 0:
            return FRP.empty

        # Check dimensions (allow negative indices python style)
        if any([index == 0 or index < -dim or index > dim for index in indices]):
            raise FrpError( f'All marginalization indices in {indices} should be between 1..{dim} or -{dim}..-1')

        # Marginalize
        def marginalize(value):
            return as_vec_tuple(map(lambda i: value[i - 1] if i > 0 else value[i], indices))

        if self.is_kinded():
            stat = Statistic(marginalize, codim=0, dim=len(indices))
            return stat(self)

        assert self._expr is not None
        expr = TransformExpression(marginalize, self._expr)
        if self._value is not None:
            expr._cached_value = marginalize(self._value)
        if self._kind is not None:
            expr._cached_kind = self._kind.map(marginalize)

        return FRP(expr)

    def __getitem__(self, indices):
        "Marginalizing this kind; other is a projection index or list of indices (1-indexed)"
        return self.marginal(indices)

    def __or__(self, predicate):
        "Applies a conditional filter to an FRP"
        if isinstance(predicate, Statistic):
            condition: Callable = predicate
        elif callable(predicate):
            condition = tuple_safe(predicate)   # ATTN: update?  Condition(predicate) ??
        else:
            raise ConditionMustBeCallable('A conditional constraint requires a condition after the given bar.')

        # If this FRP is fresh, we use a conditional expression to preserve both the
        # Kind and the value when it is determined. This avoids forcing an empty
        # FRP when nothing suggests it.
        #
        # There is a question about the value and meaning of conditionally constrained FRPs.
        # We want the constrained FRP to be consistent with the original and still reflect
        # the correct Kind, including for cloning. Sometimes these are in conflict.
        # When the value is inconsistent, we set value and Kind to empty; at that point,
        # cloning and kind() will not get back to the general Kind; it will have collapsed.

        if self.is_kinded() and not self.is_fresh:
            relevant = condition(self.value)  # We evaluate the value here
            # Fixing Bug 11 27 Jul 2024  Require the condition/fn to return a scalar here
            if isinstance(relevant, tuple):
                if len(relevant) > 1:
                    raise FrpError(f'Condition after given | should return a scalar; got {relevant}.')
                relevant = relevant[0]

            if not relevant:
                return FRP.empty
            conditional = FRP(self.kind | condition)
            conditional._value = self._value
            return conditional

        conditional = FRP(ConditionalExpression(as_expression(self), condition))
        if self._kind:
            conditional._kind = self._kind | condition

        if self._value is not None and condition(self._value):
            conditional._value = self._value

        return conditional

    def __rmatmul__(self, statistic):
        "Returns a transformed FRP with the original FRP as context for conditionals."
        if isinstance(statistic, Statistic):
            return TaggedFRP(self, statistic)
        return NotImplemented

#
# Constructors and Tests
#

@overload
def frp(spec: ConditionalFRP | ConditionalKind) -> ConditionalFRP:
    ...

@overload
def frp(spec: FRP | FrpExpression | Kind | str ) -> FRP:
    ...

def frp(spec):
    """A generic constructor for FRPs from a variety of objects.

    Parameter `spec` can be a string, a Kind, an FRP, or an FRP
    expression. When `spec` is an FRP, it is returned as is;
    use `clone` to get a fresh copy. Otherwise, returns
    a fresh FRP matching spec.

    """
    if isinstance(spec, FRP):
        return spec

    if isinstance(spec, str):
        return FRP(kind(spec))

    # frp on a conditional Kind produces a conditional FRP, analogously
    # to how kind on a conditional FRP produces a conditional Kind.
    # This is not strictly, speaking, ideal, but using kind() and frp()
    # this way is convenient for the user, so we'll keep it.
    if isinstance(spec, (ConditionalFRP, ConditionalKind)):
        # type 0 -> n ConditionalX converted to a regular FRP
        # ATTN? Should this special case be dropped?
        if spec._codim == 0:
            return frp(spec.target())
        return conditional_frp(spec)

    if not isinstance(spec, (FRP, FrpExpression, Kind)):
        raise FrpError(f'Cannot construct an FRP from object of type {type(spec).__name__}.')

    try:
        return FRP(spec)
    except Exception as e:
        raise FrpError(f'Could not create an FRP from {spec}:\n  {str(e)}')

def is_frp(x) -> TypeGuard[FRP]:
    return isinstance(x, FRP)

def is_conditional_frp(x) -> TypeGuard[Union[FRP, ConditionalFRP]]:
    return isinstance(x, FRP) or isinstance(x, ConditionalFRP)

#
# Tagged FRPs for context in conditionals
#
# phi@X acts exactly like phi(X) except in a conditional, where
#    phi@X | (s(X) == v)
# is like
#    (X * phi(X) | (s(Proj[:(d+1)](__)) == v))[(d+1):]
# but simpler
#

class TaggedFRP(FRP):
    def __init__(self, createFrom: FRP | FrpExpression | Kind, stat: Statistic):
        if is_frp(createFrom):
            original = createFrom
        elif isinstance(createFrom, (Kind, FrpExpression)):
            original = frp(createFrom)
        else:
            raise FrpError(f'Cannot create an FRP from a value of type {type(createFrom).__name__}')
        super().__init__(original.transform(stat))

        self._original = original
        self._stat = stat

        lo, hi = stat.codim
        if original.dim < lo or original.dim > hi:
            raise MismatchedDomain(f'Statistic {stat.name} is incompatible with this Kind, '
                                   f'which has dimension {self.dim} out of expected range '
                                   f'[{lo}, {"infinity" if hi == infinity else hi}].')

    def __or__(self, condition):
        return self._original.__or__(condition).transform(self._stat)

    def transform(self, statistic):
        # maybe some checks here
        new_stat = compose2(statistic, self._stat)
        return TaggedFRP(self._original, new_stat)

    def _untagged(self):
        return (self._stat, self._original)


#
# Utilities and Additional Factories and Combinators
#

@overload
def independent_mixture(ks: Iterable[Kind]) -> Kind:
    ...

@overload
def independent_mixture(ks: Iterable[FRP]) -> FRP:
    ...

def independent_mixture(ks):
    "Returns the independent mixture of the Kinds or FRPs in the given sequence."
    return reduce(lambda k1, k2: k1 * k2, ks)

@overload
def evolve(start: Kind, next_state: ConditionalKind, n_steps: int = 1, transform: Union[None, Callable] = None) -> Kind:
    ...

@overload
def evolve(start: FRP, next_state: ConditionalFRP, n_steps: int = 1, transform: Union[None, Callable] = None) -> FRP:
    ...

def evolve(start, next_state, n_steps=1, transform = None):
    """Evolves a Markovian system through a specified number of steps.

    In typical use, start will be the Kind of the system's initial state,
    and next_state the conditional Kind that describes state transitions.
    This also works when start and next_state are an FRP and a
    conditional FRP.

    Parameters:
    ----------
      start: Kind | FRP - represents the initial state
      next_state: ConditionalKid | ConditionalFRP - state transition
      n_steps: int -- the number of steps to process, >= 0
      transform: Callable | None -- if supplied, a function of a
          Kind or FRP that is applied at each step.

    The most common use cases for the transform argument are (i) to
    apply clean() to Kinds where large numbers of branches with
    negligible weight slow down the computation over many steps,
    and (ii) to apply FRP.activate to the updated state to prevent
    building up too large of an unevaluated FRP expression for a
    fresh FRP.

    The latter issue arises because fresh FRPs internally maintain
    an abstract form of the expression that generated them so that
    related FRPs can be co-activated. Over sufficiently large
    simulations, these internal expressions can grow large enough
    to exceed Python's recursion limit. The solution is to
    activate the intermediate FRPs, which prevents large expressions.
    Passing FRP.activate as the transform argument solves this problem.
    Alternatively, if n_steps is bigger than FRP.EVOLUTION_THRESHOLD,
    the intermediate (but not the last) FRP will be activated
    automatically. It is generally preferable to use the automatic
    solution, but when a transform argument is given, this automatic
    activation does not occur.

    Returns the state of the system (Kind or FRP) after n_steps steps.

    Examples:

    + If init is the Kind of the initial state and transition is the
      conditional Kind of the next state given the initial state,
      then

          evolve(init, transition, 100)

      gives the Kind of the state after 100 steps.

    + As in the last item, evolve(init, transition, 100, transform=clean)
      will eliminate branches with very small weights that can
      dominate the calculations in some cases.

    + If start is an FRP and moves is a conditional FRP of the next
      state given the current state, then

          evolve(start, moves, 1000)

      gives the FRP representing the state after 1000 moves. Because
      1000 is large, the returned FRP will be fresh, but the intermediate
      mixture FRPs (which are not seen) will not be.

    + As in the last item, evolve(start, moves, 1000, transform=FRP.activate)
      will activate all of the produced FRPs, including the last but
      excluding start.

    + evolve(a, c, 200, transform=stat)  will transform each result by
      statistic stat. Note that in this case, stat must preserve or
      create the structure expected by c.

    """
    if isinstance(start, Kind) and isinstance(next_state, ConditionalKind):
        have = 'Kind'
    elif is_frp(start) and isinstance(next_state, ConditionalFRP):
        have = 'FRP'
    else:
        raise ContractError('evolve requires either a Kind and Conditional Kind or '
                            'an FRP and conditional FRP')

    current = start
    if transform is not None:
        for _ in range(n_steps):
            current = transform(next_state // current)
    elif n_steps > FRP.EVOLUTION_THRESHOLD and have == 'FRP':
        for step in range(n_steps):
            current = next_state // current
            if step < n_steps - 1:
                current.value      # Activate intermediate FRPs
    else:
        for _ in range(n_steps):
            current = next_state // current
    return current

@overload
def average_conditional_entropy(kX: FRP, cZ: ConditionalFRP) -> Numeric:
    ...

@overload
def average_conditional_entropy(kX: Kind, cZ: ConditionalKind) -> Numeric:
    ...

def average_conditional_entropy(kX, cZ):
    """Returns the average (predicted) conditional entropy of the mixture kX >> cZ.

    This can operate either on a Kind and Conditional Kind or on an FRP and a
    conditional FRP.

    If kX represents an FRP X and Y = cZ // X, then in mathematical notation
    this returns the average conditional entropy H(Y | X).

    (For reference, cZ.conditional_entropy(x) gives H(Y | X = x).)

    """
    cond_entropy = kX ^ cZ.conditional_entropy  # A Kind or FRP
    return as_scalar(cond_entropy.expectation)

@overload
def mutual_information(kX: FRP, cZ: ConditionalFRP) -> Numeric:
    ...

@overload
def mutual_information(kX: Kind, cZ: ConditionalKind) -> Numeric:
    ...

def mutual_information(kX, cZ):
    """Returns the mutual information I(Y; X) where Y and X are derived from a mixture.

    We get a Kind/FRP kX and a conditional Kind/FRP cZ where kY is defined
    by
          kY = cZ // kX

    We compute I(Y; X) = H(Y) - H(Y | X)

    This can operate either on a Kind and Conditional Kind or on an FRP and a
    conditional FRP.

    """
    kY = cZ // kX   # A Kind or FRP
    return as_scalar(kY.entropy - average_conditional_entropy(kX, cZ))

class FisherYates(FrpExpression):
    def __init__(self, items: Iterable):
        super().__init__()
        self.items = tuple(items)
        self.n = len(self.items)

    def sample1(self):
        permuted = list(self.items)
        for i in range(self.n - 1):
            j = random.randrange(i, self.n)
            permuted[j], permuted[i] = permuted[i], permuted[j]  # swap
        return VecTuple(permuted)

    def value(self):
        if self._cached_value is None:
            self._cached_value = self.sample1()
        return self._cached_value

    def kind(self) -> Kind:
        if self.n <= 10:
            return permutations_of(self.items)
        raise KindError(f'The kind of a large ({self.n} > 10) permutation is too costly to compute.')

    def clone(self) -> 'FisherYates':
        self._cached_value = None
        self.value()
        return self

    def _refresh_cached_value(self) -> ValueType | None:
        return self._cached_value

def shuffle(items: Iterable) -> FRP:
    return frp(FisherYates(items))


#
# Low-level Helpers
#

def _sample_from_kind(n: int, kind: Kind, summary: bool) -> FrpDemoSummary | FrpDemo:
    if summary:
        table = FrpDemoSummary()
        for _ in range(n):
            table.add(VecTuple(kind.sample1()))  # ATTN: VecTuple wrapping unneeded after Quantity conversion
        return table
    return kind.sample(n)   # ATTN: should VecTuple wrap here for now

def _sample_from_expr(n: int, expr: FrpExpression, summary: bool) -> FrpDemoSummary | FrpDemo:
    if summary:
        table = FrpDemoSummary()
        for _ in range(n):
            table.add(VecTuple(expr.sample1()))  # ATTN: VecTuple wrapping unneeded after Quantity conversion
        return table
    values = []
    for _ in range(n):
        values.append(VecTuple(expr.sample1()))
    return values

def _expectation_from_expr(expr: FrpExpression):
    # ATTN: Expand the range of things that this works for
    # For instance, mixture powers or PureExpressions where the kind is available
    # should be automatic
    if expr._cached_kind is not None:
        return expr._cached_kind.expectation
    raise ComplexExpectationWarning('The expectation of this FRP could not be computed without first finding its kind.')


#
# Info tags
#

setattr(frp, '__info__', 'frp-factories')
setattr(conditional_frp, '__info__', 'frp-factories')
setattr(shuffle, '__info__', 'frp-factories')
setattr(independent_mixture, '__info__', 'frp-combinators')
setattr(evolve, '__info__', 'actions')
