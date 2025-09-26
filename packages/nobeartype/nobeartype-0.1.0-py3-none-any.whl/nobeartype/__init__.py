from __future__ import annotations

from functools import wraps
from weakref import WeakKeyDictionary, WeakValueDictionary

from beartype import BeartypeConf, BeartypeStrategy, beartype
from beartype.typing import Any, Callable, ClassVar, TypeVar
from typing_extensions import ParamSpec

P = ParamSpec("P")
R = TypeVar("R", bound=Any)

_OC = Callable[..., object]
_WKD = WeakKeyDictionary
_WVD = WeakValueDictionary


class NoBearType:
    """
    Disable beartype's runtime type checking for a specific function, protecting it in case global runtime checking is on.
    This is needed if your functions expose return types from external libraries like flask which beartype can't inspect.

    IMHO, when using beartype it's best to enable it on a per-function basis or after import in your testing suite: `beartype_package('foo')`

    You *could* use `beartype_this_package()` in `foo.__init__.py.` That's pretty hardcore, though.

    ```pycon
    >>> from beartype import beartype
    >>> nobeartype = NoBearType()

    >>> # Contrived - @beartype would be applied at the import hook level
    >>> @beartype
    ... @nobeartype
    ... def my_bad_func() -> int:
    ...    '''Really bad stuff'''
    ...    return "Foo" # no type error

    >>> my_bad_func()
    'Foo'
    >>> my_bad_func.__doc__  # still wrapped
    'Really bad stuff'

    >>> @beartype
    ... def my_bad_func_unprotected() -> int:
    ...    return "Foo" # type error
    >>> my_bad_func_unprotected()
    Traceback (most recent call last):
        ...
    beartype.roar.BeartypeCallHintReturnViolation: Function ... return 'Foo' violates type hint <class 'int'>, as str 'Foo' not instance of int.

    >>> NoBearType.registry()   # doctest: +ELLIPSIS
    {<function my_bad_func at 0x...>}
    >>> assert len(nobeartype) == 1

    >>> NoBearType.clear()   # doctest: +ELLIPSIS
    >>> assert len(nobeartype) == 0
    >>> nobeartype.registry()
    set()

    ```
    """

    _registry: ClassVar[set[_OC]] = set[_OC]()

    def __call__(self, func: Callable[P, R]) -> Callable[P, R]:
        no_bear_type = beartype(conf=BeartypeConf(strategy=BeartypeStrategy.O0))

        @wraps(func)
        @no_bear_type
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            return func(*args, **kwargs)

        self._registry.add(func)
        return wrapper

    @classmethod
    def __len__(cls) -> int:
        return len(cls._registry)

    @classmethod
    def __contains__(cls, func: _OC) -> bool:
        return func in cls._registry

    @classmethod
    def registry(cls) -> set[_OC]:
        return cls._registry

    @classmethod
    def clear(cls) -> None:
        cls._registry.clear()

    @classmethod
    def deregister(cls, func: _OC) -> _OC | None:
        return cls._registry.discard(func)


nobeartype: NoBearType = NoBearType()

if __name__ == "__main__":
    import doctest

    _ = doctest.testmod(
        verbose=True, optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
    )
