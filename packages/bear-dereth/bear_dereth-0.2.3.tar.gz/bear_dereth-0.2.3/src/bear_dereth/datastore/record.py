"""Settings record models for type-safe storage."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

from pydantic import Field

from bear_dereth.datastore.common import TypeList, ValueType
from bear_dereth.freezing import FrozenModel

if TYPE_CHECKING:
    from bear_dereth.datastore.models import Document


# TODO: We will need to replace this with Document and probably remove the type field.
class SettingsRecord[Value_T: ValueType](FrozenModel):
    """Pydantic model for a settings record with automatic type detection.

    This model ensures type safety when storing settings and automatically
    detects the type of the value for proper serialization.
    """

    key: str = Field(description="The setting key/name")
    value: Value_T = Field(description="The setting value")
    type: TypeList = Field(default="null", description="Auto-detected value type")

    def model_post_init(self, context: Any) -> None:
        """Post-initialization to set the type based on the value.

        Args:
            context: Pydantic validation context
        """
        match self.value:
            case None:
                self.type = "null"
            case bool():
                self.type = "boolean"
            case int():
                self.type = "number"
            case float():
                self.type = "float"
            case str():
                self.type = "string"
            case list():
                self.type = "list"
            case _:
                raise ValueError(f"Unsupported value type: {type(self.value)}")
        super().model_post_init(context)

    def __hash__(self) -> int:
        """Hash based on a frozen representation of the model."""
        return self.get_hash()

    def get_document(self) -> Document:
        """Get a Document representation of the record.

        Returns:
            Document instance containing the record data
        """
        return cast("Document", self.model_dump(frozen=False))  # type: ignore[return-value]


__all__ = ["SettingsRecord"]
