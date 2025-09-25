from collections.abc import Callable
from typing import Any

from bear_dereth.typing_tools import a_or_b

from ._mapping_ops import (
    abs as map_abs,
    add as map_add,
    append as map_append,
    clamp as map_clamp,
    default as map_default,
    delete as map_delete,
    div as map_div,
    extend as map_extend,
    format as map_format,
    if_else as map_if_else,
    lower as map_lower,
    mod as map_mod,
    multiply as map_multiply,
    pop as map_pop,
    pow as map_pow,
    prepend as map_prepend,
    push as map_push,
    replace as map_replace,
    setter as map_set,
    subtract as map_subtract,
    toggle as map_toggle,
    upper as map_upper,
)
from ._obj_ops import (
    abs as obj_abs,
    add as obj_add,
    append as obj_append,
    clamp as obj_clamp,
    default as obj_default,
    delete as obj_delete,
    div as obj_div,
    extend as obj_extend,
    format as obj_format,
    if_else as obj_if_else,
    lower as obj_lower,
    mod as obj_mod,
    multiply as obj_multiply,
    pop as obj_pop,
    pow as obj_pow,
    prepend as obj_prepend,
    push as obj_push,
    replace as obj_replace,
    setter as obj_set,
    subtract as obj_subtract,
    toggle as obj_toggle,
    upper as obj_upper,
)


def add(field: str, n: int) -> Callable[..., None]:
    """Add ``n`` to a given field in the document.

    Args:
        field: The field to add to.
        n: The amount to add.

    Returns:
        A function that takes a document and adds ``n`` to the given field.
    """
    return a_or_b(map_add(field, n), obj_add(field, n))


def subtract(field: str, n: int) -> Callable[..., None]:
    """Subtract ``n`` to a given field in the document.

    Args:
        field: The field to subtract from.
        n: The amount to subtract.

    Returns:
        A function that takes a document and subtracts ``n`` from the given field.
    """
    return a_or_b(map_subtract(field, n), obj_subtract(field, n))


def increment(field: str) -> Callable[..., None]:
    """Increment a given field in the document by 1.

    Args:
        field: The field to increment.

    Returns:
        A function that takes a document and increments the given field by 1.
    """
    return add(field, 1)


def decrement(field: str) -> Callable[..., None]:
    """Decrement a given field in the document by 1.

    Args:
        field: The field to decrement.

    Returns:
        A function that takes a document and decrements the given field by 1.
    """
    return subtract(field, 1)


def multiply(field: str, n: int) -> Callable[..., None]:
    """Multiply a given field in the document by n.

    Args:
        field: The field to multiply.
        n: The amount to multiply by.

    Returns:
        A function that takes a document and multiplies the given field by n.
    """
    return a_or_b(map_multiply(field, n), obj_multiply(field, n))


def div(field: str, n: int) -> Callable[..., None]:
    """Divide a given field in the document by n.

    Args:
        field: The field to divide.
        n: The amount to divide by. Must not be zero.

    Returns:
        A function that takes a document and divides the given field by n.
    """
    return a_or_b(map_div(field, n), obj_div(field, n))


def delete(field: str) -> Callable[..., None]:
    """Delete a given field from the document.

    Args:
        field: The field to delete.

    Returns:
        A function that takes a document and deletes the given field.
    """
    return a_or_b(map_delete(field), obj_delete(field))


def setter(field: str, v: Any) -> Callable[..., None]:
    """Set a given field in the document to a value.

    Args:
        field: The field to set.
        v: The value to set the field to.

    Returns:
        A function that takes a document and sets the given field to ``val``.
    """
    return a_or_b(map_set(field, v), obj_set(field, v))


def if_else(
    field: str,
    cond: Callable[[Any], bool],
    then: Callable[..., None],
    otherwise: Callable[..., None],
) -> Callable[..., None]:
    """Apply either `then` or `otherwise` operation based on a condition on a given field.

    Args:
        field: The field to check the condition against.
        cond: A callable that takes the field's value and returns a boolean.
        then: The operation to apply if the condition is true.
        otherwise: The operation to apply if the condition is false.

    Returns:
        A function that takes a document and applies either `then` or `otherwise` operation.
    """
    return a_or_b(map_if_else(field, cond, then, otherwise), obj_if_else(field, cond, then, otherwise))


def upper(field: str) -> Callable[..., None]:
    """Convert a string field to uppercase.

    Args:
        field: The field to convert.

    Returns:
        A function that takes a document and converts the given field to uppercase.
    """
    return a_or_b(map_upper(field), obj_upper(field))


def lower(field: str) -> Callable[..., None]:
    """Convert a string field to lowercase.

    Args:
        field: The field to convert.

    Returns:
        A function that takes a document and converts the given field to lowercase.
    """
    return a_or_b(map_lower(field), obj_lower(field))


def replace(field: str, old: str, new: str) -> Callable[..., None]:
    """Replace occurrences of a substring in a string field.

    Args:
        field: The field to modify.
        old: The substring to replace.
        new: The substring to replace with.

    Returns:
        A function that takes a document and replaces occurrences of `old` with `new` in the given field.
    """
    return a_or_b(map_replace(field, old, new), obj_replace(field, old, new))


def format(field: str, *args: Any, **kwargs: Any) -> Callable[..., None]:
    """Format a string field using the provided arguments.

    Args:
        field: The field to format.
        *args: Positional arguments for formatting.
        **kwargs: Keyword arguments for formatting.

    Returns:
        A function that takes a document and formats the given field using the provided arguments.
    """
    return a_or_b(map_format(field, *args, **kwargs), obj_format(field, *args, **kwargs))


def pow(field: str, n: int) -> Callable[..., None]:
    """Raise a given field in the document to the power of n.

    Args:
        field: The field to raise.
        n: The exponent.

    Returns:
        A function that takes a document and raises the given field to the power of n.
    """
    return a_or_b(map_pow(field, n), obj_pow(field, n))


def clamp(field: str, min_value: int, max_value: int) -> Callable[..., None]:
    """Clamp a given field in the document to be within min_value and max_value.

    Args:
        field: The field to clamp.
        min_value: The minimum value to clamp to.
        max_value: The maximum value to clamp to.

    Returns:
        A function that takes a document and clamps the given field to be within min_value and max_value.
    """
    return a_or_b(map_clamp(field, min_value, max_value), obj_clamp(field, min_value, max_value))


def mod(field: str, n: int) -> Callable[..., None]:
    """Modulus a given field in the document by n.

    Args:
        field: The field to modulus.
        n: The amount to modulus by.

    Returns:
        A function that takes a document and modulus the given field by n.
    """
    return a_or_b(map_mod(field, n), obj_mod(field, n))


def toggle(field: str) -> Callable[..., None]:
    """Toggle a boolean field.

    Args:
        field: The field to toggle.

    Returns:
        A function that takes a document and toggles the boolean field.
    """
    return a_or_b(map_toggle(field), obj_toggle(field))


def abs(field: str) -> Callable[..., None]:
    """Set a field to its absolute value.

    Args:
        field: The field to set.

    Returns:
        A function that takes a document and sets the field to its absolute value.
    """
    return a_or_b(map_abs(field), obj_abs(field))


def default(field: str, v: Any, replace_none: bool = False) -> Callable[..., None]:
    """Set a field to a default value if it does not exist.

    Args:
        field: The field to set.
        v: The default value to set the field to.
        replace_none: If True, also replace None values.

    Returns:
        A function that takes a document and sets the field to the default value if it does not exist.
    """
    return a_or_b(map_default(field, v, replace_none), obj_default(field, v, replace_none))


def push(field: str, v: Any, index: int = -1) -> Callable[..., None]:
    """Push a value to a list field in the document at a specific index.

    Args:
        field: The field to push to.
        v: The value to push.
        index: The index to insert the value at. Defaults to -1 (the end of the list).

    Returns:
        A function that takes a document and pushes the value to the list field at the specified index
    """
    return a_or_b(map_push(field, v, index), obj_push(field, v, index))


def append(field: str, v: Any) -> Callable[..., None]:
    """Append a value to a list field in the document.

    Args:
        field: The field to append to.
        v: The value to append.

    Returns:
        A function that takes a document and appends the value to the list field.
    """
    return a_or_b(map_append(field, v), obj_append(field, v))


def prepend(field: str, v: Any) -> Callable[..., None]:
    """Prepend a value to a list field in the document.

    Args:
        field: The field to prepend to.
        v: The value to prepend.

    Returns:
        A function that takes a document and prepends the value to the list field.
    """
    return a_or_b(map_prepend(field, v), obj_prepend(field, v))


def extend(field: str, vals: list) -> Callable[..., None]:
    """Extend a list field in the document with another list.

    Args:
        field: The field to extend.
        vals: The list of values to extend with.

    Returns:
        A function that takes a document and extends the list field with the given list.
    """
    return a_or_b(map_extend(field, vals), obj_extend(field, vals))


def pop(field: str, index: int = -1) -> Callable[..., None]:
    """Pop a value from a list field in the document.

    Args:
        field: The field to pop from.
        index: The index to pop. Defaults to -1 (the last item).

    Returns:
        A function that takes a document and pops a value from the list field.
    """
    return a_or_b(map_pop(field, index), obj_pop(field, index))


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
