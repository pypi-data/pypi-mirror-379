"""A collection of update operations for objects.

They are used for updates like this:

>>> db.update(delete("foo"), where("foo") == 2)

This would delete the ``foo`` field from all documents where ``foo`` equals 2.
"""

from collections.abc import Callable
from operator import abs as _abs, mod as _mod, not_ as invert, pow as _pow
from typing import Any


def delete(field: str) -> Callable[..., None]:
    """Delete a given field from the document.

    Args:
        field: The field to delete.

    Returns:
        A function that takes a document and deletes the given field.
    """

    def transform(doc: object) -> None:
        delattr(doc, field)

    return transform


def add(field: str, n: int) -> Callable[..., None]:
    """Add ``n`` to a given field in the document.

    Args:
        field: The field to add to.
        n: The amount to add.

    Returns:
        A function that takes a document and adds ``n`` to the given field.
    """

    def transform(doc: object) -> None:
        attr: Any = getattr(doc, field)
        if isinstance(attr, (int | float)):
            setattr(doc, field, attr + n)

    return transform


def subtract(field: str, n: int) -> Callable[..., None]:
    """Subtract ``n`` to a given field in the document.

    Args:
        field: The field to subtract from.
        n: The amount to subtract.

    Returns:
        A function that takes a document and subtracts ``n`` from the given field.
    """

    def transform(doc: object) -> None:
        attr: Any = getattr(doc, field)
        if isinstance(attr, (int | float)):
            setattr(doc, field, attr - n)

    return transform


def multiply(field: str, n: int) -> Callable[..., None]:
    """Multiply a given field in the document by n.

    Args:
        field: The field to multiply.
        n: The amount to multiply by.

    Returns:
        A function that takes a document and multiplies the given field by n.
    """

    def transform(doc: object) -> None:
        attr: Any = getattr(doc, field)
        if isinstance(attr, (int | float)):
            setattr(doc, field, attr * n)

    return transform


def div(field: str, n: int, floor: bool = False) -> Callable[..., None]:
    """Divide a given field in the document by n.

    Args:
        field: The field to divide.
        n: The amount to divide by. Must not be zero
        floor: If True, use floor division.

    Returns:
        A function that takes a document and divides the given field by n.
    """

    def transform(doc: object) -> None:
        attr: Any = getattr(doc, field)
        if isinstance(attr, (int | float)) and n != 0:
            if floor:
                setattr(doc, field, attr // n)
            else:
                setattr(doc, field, attr / n)

    return transform


def increment(field: str) -> Callable[..., None]:
    """Increment a given field in the document by 1.

    Args:
        field: The field to increment.

    Returns:
        A function that takes a document and increments the given field by 1.
    """
    return add(field=field, n=1)


def decrement(field: str) -> Callable[..., None]:
    """Decrement a given field in the document by 1.

    Args:
        field: The field to decrement.

    Returns:
        A function that takes a document and decrements the given field by 1.
    """
    return subtract(field=field, n=1)


def setter(field: str, v: Any) -> Callable[..., None]:
    """Set a given field to ``val``.

    Args:
        field: The field to set.
        v: The value to set the field to.

    Returns:
        A function that takes a document and sets the given field to ``val``.
    """

    def transform(doc: Any) -> None:
        setattr(doc, field, v)

    return transform


def if_else(
    field: str,
    cond: Callable[[Any], bool],
    then: Callable[..., None],
    otherwise: Callable[..., None],
) -> Callable[..., None]:
    """Apply one of two operations based on the value of a field in the document.

    Args:
        field: The field to check.
        cond: A callable that takes the field's value and returns a boolean.
        then: The operation to apply if the condition is true.
        otherwise: The operation to apply if the condition is false.

    Returns:
        A function that takes a document and applies either `then` or `otherwise`
        operation based on the condition.
    """

    def transform(doc: Any) -> None:
        if cond(getattr(doc, field)):
            then(doc)
        else:
            otherwise(doc)

    return transform


def upper(field: str) -> Callable[..., None]:
    """Convert a string field to uppercase.

    Args:
        field: The field to convert.

    Returns:
        A function that takes a document and converts the given field to uppercase.
    """

    def transform(doc: object) -> None:
        attr: Any = getattr(doc, field)
        if isinstance(attr, str):
            setattr(doc, field, attr.upper())

    return transform


def lower(field: str) -> Callable[..., None]:
    """Convert a string field to lowercase.

    Args:
        field: The field to convert.

    Returns:
        A function that takes a document and converts the given field to lowercase.
    """

    def transform(doc: object) -> None:
        attr: Any = getattr(doc, field)
        if isinstance(attr, str):
            setattr(doc, field, attr.lower())

    return transform


def replace(field: str, old: str, new: str) -> Callable[..., None]:
    """Replace occurrences of a substring in a string field.

    Args:
        field: The field to modify.
        old: The substring to replace.
        new: The substring to replace with.

    Returns:
        A function that takes a document and replaces occurrences of `old` with `new` in the given field.
    """

    def transform(doc: object) -> None:
        attr: Any = getattr(doc, field)
        if isinstance(attr, str):
            setattr(doc, field, attr.replace(old, new))

    return transform


def format(field: str, *args: Any, **kwargs: Any) -> Callable[..., None]:
    """Format a string field using the provided arguments.

    Args:
        field: The field to format.
        *args: Positional arguments for formatting.
        **kwargs: Keyword arguments for formatting.

    Returns:
        A function that takes a document and formats the given field using the provided arguments.
    """

    def transform(doc: object) -> None:
        attr: Any = getattr(doc, field)
        if isinstance(attr, str):
            setattr(doc, field, attr.format(*args, **kwargs))

    return transform


def pow(field: str, n: int) -> Callable[..., None]:
    """Raise a given field in the document to the power of n.

    Args:
        field: The field to raise.
        n: The exponent.

    Returns:
        A function that takes a document and raises the given field to the power of n.
    """

    def transform(doc: object) -> None:
        attr: Any = getattr(doc, field)
        if isinstance(attr, (int | float)):
            setattr(doc, field, _pow(attr, n))

    return transform


def clamp(field: str, min_value: int, max_value: int) -> Callable[..., None]:
    """Clamp a given field in the document to be within min_value and max_value.

    Args:
        field: The field to clamp.
        min_value: The minimum value to clamp to.
        max_value: The maximum value to clamp to.

    Returns:
        A function that takes a document and clamps the given field to be within min_value and max_value.
    """

    def transform(doc: object) -> None:
        attr: Any = getattr(doc, field)
        if isinstance(attr, (int | float)):
            setattr(doc, field, max(min_value, min(max_value, attr)))

    return transform


def mod(field: str, n: int) -> Callable[..., None]:
    """Modulus a given field in the document by n.

    Args:
        field: The field to modulus.
        n: The amount to modulus by.

    Returns:
        A function that takes a document and modulus the given field by n.
    """

    def transform(doc: object) -> None:
        attr: Any = getattr(doc, field)
        if isinstance(attr, (int | float)) and n != 0:
            setattr(doc, field, _mod(attr, n))

    return transform


def toggle(field: str) -> Callable[..., None]:
    """Toggle a boolean field.

    Args:
        field: The field to toggle.

    Returns:
        A function that takes a document and toggles the boolean field.
    """

    def transform(doc: object) -> None:
        attr: Any = getattr(doc, field)
        if isinstance(attr, bool):
            setattr(doc, field, invert(attr))

    return transform


def abs(field: str) -> Callable[..., None]:
    """Set a field to its absolute value.

    Args:
        field: The field to set.

    Returns:
        A function that takes a document and sets the field to its absolute value.
    """

    def transform(doc: object) -> None:
        attr: Any = getattr(doc, field)
        if isinstance(attr, (int | float)):
            setattr(doc, field, _abs(attr))

    return transform


def default(field: str, v: Any, replace_none: bool = False) -> Callable[..., None]:
    """Set a field to a default value if it does not exist.

    Args:
        field: The field to set.
        v: The default value to set the field to.
        replace_none: If True, also replace None values.

    Returns:
        A function that takes a document and sets the field to the default value if it does not exist.
    """

    def transform(doc: object) -> None:
        if not hasattr(doc, field) or (replace_none and getattr(doc, field) is None):
            setattr(doc, field, v)

    return transform


def push(field: str, v: Any, index: int = -1) -> Callable[..., None]:
    """Push a value to a list field in the document at a specific index.

    Args:
        field: The field to push to.
        v: The value to push.
        index: The index to insert the value at. Defaults to -1 (the end of the list).

    Returns:
        A function that takes a document and pushes the value to the list field at the specified index
    """

    def transform(doc: object) -> None:
        if not hasattr(doc, field):
            setattr(doc, field, [])
        attr: Any = getattr(doc, field)
        if isinstance(attr, list):
            if index == -1 or index >= len(attr):
                attr.append(v)
            else:
                attr.insert(index, v)

    return transform


def append(field: str, v: Any) -> Callable[..., None]:
    """Append a value to a list field in the document.

    Args:
        field: The field to append to.
        v: The value to append.

    Returns:
        A function that takes a document and appends the value to the list field.
    """

    def transform(doc: object) -> None:
        push(field, v, index=-1)(doc)

    return transform


def prepend(field: str, v: Any) -> Callable[..., None]:
    """Prepend a value to a list field in the document.

    Args:
        field: The field to prepend to.
        v: The value to prepend.

    Returns:
        A function that takes a document and prepends the value to the list field.
    """

    def transform(doc: object) -> None:
        push(field, v, index=0)(doc)

    return transform


def extend(field: str, vals: list) -> Callable[..., None]:
    """Extend a list field in the document with another list.

    Args:
        field: The field to extend.
        vals: The list of values to extend with.

    Returns:
        A function that takes a document and extends the list field with the given list.
    """

    def transform(doc: object) -> None:
        if not hasattr(doc, field):
            setattr(doc, field, [])
        attr: Any = getattr(doc, field)
        if isinstance(attr, list):
            attr.extend(vals)

    return transform


def pop(field: str, index: int = -1) -> Callable[..., None]:
    """Pop a value from a list field in the document.

    Args:
        field: The field to pop from.
        index: The index to pop. Defaults to -1 (the last item).

    Returns:
        A function that takes a document and pops a value from the list field.
    """

    def transform(doc: object) -> None:
        if hasattr(doc, field):
            attr: Any = getattr(doc, field)
            if isinstance(attr, list) and -len(attr) <= index < len(attr):
                attr.pop(index)

    return transform


__all__ = [
    "abs",
    "add",
    "append",
    "clamp",
    "decrement",
    "default",
    "delete",
    "div",
    "extend",
    "format",
    "if_else",
    "increment",
    "lower",
    "mod",
    "multiply",
    "pop",
    "pow",
    "prepend",
    "push",
    "replace",
    "setter",
    "subtract",
    "toggle",
    "upper",
]
