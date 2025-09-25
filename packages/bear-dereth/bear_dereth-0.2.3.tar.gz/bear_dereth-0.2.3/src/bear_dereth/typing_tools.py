"""A set of type aliases and utility functions for type validation and inspection."""

from abc import ABC, abstractmethod
from collections.abc import Callable, Mapping, MutableMapping
from types import NoneType
from typing import TYPE_CHECKING, Any, Literal, TypeGuard, get_args

from bear_dereth.exceptions import ObjectTypeError

LitInt = Literal["int"]
LitFloat = Literal["float"]
LitStr = Literal["str"]
LitBool = Literal["bool"]

LitFalse = Literal[False]
LitTrue = Literal[True]

OptInt = int | None
OptFloat = float | None
OptStr = str | None
OptBool = bool | None
OptStrList = list[str] | None
OptStrDict = dict[str, str] | None


def num_type_params(cls: type) -> int:
    """Get the number of type parameters of a subclass that inherits from a generic class.

    Args:
        cls (object): The class object from which to retrieve the number of type parameters.

    Returns:
        int: The number of type parameters.

    Raises:
        TypeError: If the class does not have type parameters.
        AttributeError: If the class does not have the expected type parameters.
    """
    try:
        args: tuple[Any, ...] = get_args(cls.__orig_bases__[0])
    except (AttributeError, TypeError):
        raise TypeError(f"{cls.__name__} does not have type parameters.") from None
    return len(args)


def type_param(cls: type, index: int = 0) -> type:
    """Get the type parameter of a subclass that inherits from a generic class.

    Args:
        cls (object): The class object from which to retrieve the type parameter.
        index (int): The index of the type parameter to retrieve. Defaults to 0.

    Returns:
        type: The type parameter at the specified index.

    Raises:
        IndexError: If the specified index is out of range for the type parameters.
        TypeError: If the class does not have type parameters.
        AttributeError: If the class does not have the expected type parameters.
    """
    try:
        args: tuple[Any, ...] = get_args(cls.__orig_bases__[0])
    except IndexError:
        raise IndexError(f"Index {index} is out of range for type parameters of {cls.__name__}.") from None
    except (AttributeError, TypeError):
        raise TypeError(f"{cls.__name__} does not have type parameters.") from None
    if args[index] is NoneType:
        raise TypeError(f"Type parameter at index {index} is NoneType for {cls.__name__}.")
    return args[index]


def coerce_to_type[T](val: Any, to_type: Callable[[Any], T]) -> T:
    """Coerce a value to the specified type if possible.

    Args:
        val (Any): The value to coerce.
        to_type (type): The type to which the value should be coerced.

    Returns:
        Any: The coerced value.

    Raises:
        ValueError: If the value cannot be coerced to the specified type.
    """
    try:
        return to_type(val)
    except (ValueError, TypeError) as e:
        raise ValueError(f"Cannot coerce value {val} of type {type(val).__name__} to {to_type.__name__}.") from e


def mapping_to_type[T](mapping: Mapping, key: str, to_type: Callable[[Any], T], default: Any = None) -> T:
    """Get a value from a mapping and coerce it to the specified type if possible.

    Args:
        mapping (Mapping): The mapping from which to retrieve the value.
        key (str): The key of the value to retrieve.
        to_type (type): The type to which the value should be coerced.
        default (Any): The default value to return if the key is not found. Defaults to None.

    Returns:
        Any: The coerced value.

    Raises:
        ValueError: If the value cannot be coerced to the specified type.
    """
    if key not in mapping:
        if default is not None:
            return coerce_to_type(val=default, to_type=to_type)
        raise KeyError(f"Key {key} not found in mapping and no default provided.")
    return coerce_to_type(val=mapping[key], to_type=to_type)


def validate_type(val: Any, expected: type, exception: type[ObjectTypeError] | None = None) -> None:
    """Validate the type of the given value.

    Args:
        val (Any): The value to validate.
        expected (type): The expected type of the value.
        exception (type[ObjectTypeError] | None): The exception to raise if the type
            does not match. If None, a TypeError is raised.
    """
    if not isinstance(val, expected):
        if exception is None:
            raise TypeError(f"Expected object of type {expected.__name__}, but got {type(val).__name__}.")
        raise exception(expected=expected, received=type(val))


class ArrayLike(ABC):
    """A protocol representing array-like structures (list, tuple, set)."""

    @abstractmethod
    def __iter__(self) -> Any: ...

    @classmethod
    @abstractmethod
    def __subclasshook__(cls, subclass: type) -> bool:
        return subclass in (list, tuple, set)


def is_array_like(instance: Any) -> TypeGuard[ArrayLike]:
    """Check if an instance is array-like (list, tuple, set)."""
    return isinstance(instance, (list | tuple | set))


def TypeHint[T](hint: type[T]) -> type[T]:  # noqa: N802
    """Add type hints from a specified class to a base class:

    >>> class Foo(TypeHint(Bar)):
    ...     pass

    This would add type hints from class ``Bar`` to class ``Foo``.
    """
    if TYPE_CHECKING:
        return hint  # This adds type hints for type checkers

    class _TypeHintBase: ...

    return _TypeHintBase


def is_mapping(doc: Any) -> TypeGuard[MutableMapping]:
    """Check if a document is a mutable mapping (like a dict)."""
    return isinstance(doc, MutableMapping)


def is_object(doc: Any) -> TypeGuard[object]:
    """Check if a document is a non-mapping object."""
    return isinstance(doc, object) and not isinstance(doc, MutableMapping)


def a_or_b(a: Callable, b: Callable) -> Callable[..., None]:
    """Return a function that applies either a or b based on the type of the document."""

    def wrapper(doc: Any) -> None:
        if is_mapping(doc):
            a(doc)
        if is_object(doc):
            b(doc)

    return wrapper
