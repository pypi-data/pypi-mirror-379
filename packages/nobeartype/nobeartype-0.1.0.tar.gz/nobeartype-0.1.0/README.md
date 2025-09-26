# nobeartype

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
(<function my_bad_func at 0x...>,)
>>> assert len(nobeartype) == 1

>>> NoBearType.clear()   # doctest: +ELLIPSIS
>>> assert len(nobeartype) == 0
>>> nobeartype.registry()
()

```

## Testing

`python -m doctest` is my test suite. Coverage is 100%.
