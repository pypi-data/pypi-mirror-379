from collections.abc import Callable
from copy import deepcopy
from types import SimpleNamespace
from typing import Any

import pytest

import bear_dereth.operations as ops

TransformFactory = Callable[[], Callable[[Any], None]]


def make_docs(**values: Any) -> tuple[dict[str, Any], SimpleNamespace]:
    """Create a mapping and an object with the same initial values."""
    mapping = {key: deepcopy(val) for key, val in values.items()}
    obj = SimpleNamespace(**{key: deepcopy(val) for key, val in values.items()})
    return mapping, obj


def apply_to_docs(factory: TransformFactory, **initial: Any) -> tuple[dict[str, Any], SimpleNamespace]:
    """Create docs, apply the transform to both, and return the results."""
    mapping, obj = make_docs(**initial)
    transform = factory()
    transform(mapping)
    transform(obj)
    return mapping, obj


@pytest.mark.parametrize(
    ("factory", "field", "initial", "expected"),
    [
        (lambda: ops.add("value", 5), "value", 10, 15),
        (lambda: ops.subtract("value", 3), "value", 10, 7),
        (lambda: ops.increment("value"), "value", 0, 1),
        (lambda: ops.decrement("value"), "value", 3, 2),
        (lambda: ops.multiply("value", 4), "value", 2, 8),
        (lambda: ops.div("value", 4), "value", 10, 2.5),
        (lambda: ops.pow("value", 3), "value", 2, 8),
        (lambda: ops.mod("value", 3), "value", 10, 1),
        (lambda: ops.abs("value"), "value", -9, 9),
        (lambda: ops.clamp("value", 0, 5), "value", 10, 5),
        (lambda: ops.toggle("flag"), "flag", True, False),
    ],
)
def test_numeric_and_boolean_operations_apply_to_mapping_and_objects(
    factory: TransformFactory,
    field: str,
    initial: Any,
    expected: Any,
) -> None:
    mapping, obj = apply_to_docs(factory, **{field: initial})
    if isinstance(expected, float):
        assert mapping[field] == pytest.approx(expected)
        assert getattr(obj, field) == pytest.approx(expected)
    else:
        assert mapping[field] == expected
        assert getattr(obj, field) == expected


def test_string_operations_apply_to_mapping_and_objects() -> None:
    mapping, obj = apply_to_docs(lambda: ops.upper("name"), name="alice")
    assert mapping["name"] == "ALICE"
    assert obj.name == "ALICE"

    mapping, obj = apply_to_docs(lambda: ops.lower("name"), name="ALICE")
    assert mapping["name"] == "alice"
    assert obj.name == "alice"

    mapping, obj = apply_to_docs(lambda: ops.replace("text", "world", "bear"), text="hello world")
    assert mapping["text"] == "hello bear"
    assert obj.text == "hello bear"

    mapping, obj = apply_to_docs(
        lambda: ops.format("greeting", name="Ada"),
        greeting="Hello {name}",
    )
    assert mapping["greeting"] == "Hello Ada"
    assert obj.greeting == "Hello Ada"


def test_setter_and_delete_apply_to_both_doc_types() -> None:
    mapping, obj = apply_to_docs(lambda: ops.setter("status", "done"), status="pending")
    assert mapping["status"] == "done"
    assert obj.status == "done"

    mapping, obj = apply_to_docs(lambda: ops.delete("status"), status="stale")
    assert "status" not in mapping
    assert not hasattr(obj, "status")


def test_default_sets_missing_and_respects_existing() -> None:
    transform = ops.default("fallback", "value")

    map_missing, obj_missing = make_docs()
    transform(map_missing)
    transform(obj_missing)
    assert map_missing["fallback"] == "value"
    assert obj_missing.fallback == "value"

    map_existing, obj_existing = make_docs(fallback="present")
    transform(map_existing)
    transform(obj_existing)
    assert map_existing["fallback"] == "present"
    assert obj_existing.fallback == "present"


def test_default_replaces_none_when_requested() -> None:
    transform = ops.default("maybe", "value", replace_none=True)
    map_doc, obj_doc = make_docs(maybe=None)
    transform(map_doc)
    transform(obj_doc)
    assert map_doc["maybe"] == "value"
    assert obj_doc.maybe == "value"


def test_push_creates_list_for_missing_field() -> None:
    mapping, obj = apply_to_docs(lambda: ops.push("items", "a"))
    assert mapping["items"] == ["a"]
    assert obj.items == ["a"]


def test_push_inserts_at_specific_index() -> None:
    mapping, obj = apply_to_docs(lambda: ops.push("items", "b", index=1), items=["a", "c"])
    assert mapping["items"] == ["a", "b", "c"]
    assert obj.items == ["a", "b", "c"]


def test_list_helpers_append_prepend_extend_pop() -> None:
    mapping, obj = apply_to_docs(lambda: ops.append("items", 2), items=[1])
    assert mapping["items"] == [1, 2]
    assert obj.items == [1, 2]

    mapping, obj = apply_to_docs(lambda: ops.prepend("items", 1), items=[2])
    assert mapping["items"] == [1, 2]
    assert obj.items == [1, 2]

    mapping, obj = apply_to_docs(lambda: ops.extend("items", [2, 3]), items=[1])
    assert mapping["items"] == [1, 2, 3]
    assert obj.items == [1, 2, 3]

    mapping, obj = apply_to_docs(lambda: ops.pop("items", index=1), items=[1, 2, 3])
    assert mapping["items"] == [1, 3]
    assert obj.items == [1, 3]


def test_if_else_executes_then_branch_for_positive_condition() -> None:
    mapping, obj = apply_to_docs(
        lambda: ops.if_else(
            "value",
            lambda v: v > 0,
            ops.add("value", 5),
            ops.subtract("value", 5),
        ),
        value=2,
    )
    assert mapping["value"] == 7
    assert obj.value == 7


def test_if_else_executes_otherwise_branch_for_negative_condition() -> None:
    mapping, obj = apply_to_docs(
        lambda: ops.if_else(
            "value",
            lambda v: v > 0,
            ops.add("value", 5),
            ops.subtract("value", 5),
        ),
        value=-2,
    )
    assert mapping["value"] == -7
    assert obj.value == -7
