"""Core User model without lazy loading."""

from __future__ import annotations

from typing import Any

from .base import CoreBaseModel, CoreClientObject

__all__ = ('CoreUser', 'UserInfoParsedItem')


# Types for User
class UserInfoParsedItem(dict[str, Any]):
    """Parsed user info item."""

    type: str
    value: str


class CoreUser(CoreBaseModel, CoreClientObject):
    """Core User model with common functionality."""

    # User attributes (based on API documentation)
    id: int
    name: str
    name_trans: str | None
    info: str | None
    unique_name: str
    deleted: bool
    active: bool
    time_updated: str
    time_created: str
    is_bot: bool
    alias: str | None
    timezone_offset_minutes: int | None
    owner_id: int | None
    organizations: list[int]  # Confirmed: this is list[int] in real API, not bool|null as in docs
    info_parsed: list[UserInfoParsedItem] | None

    def __init__(self, client: Any, user_id: int, **kwargs: Any) -> None:
        self.id = user_id
        self._attr_formatters: dict[str, Any] = {}  # User has no special formatters

        # Call parent constructors
        CoreBaseModel.__init__(self, id=user_id, **kwargs)
        CoreClientObject.__init__(self, client)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CoreUser):
            return id(other) == id(self)
        return self.id == other.id

    def __str__(self) -> str:
        return self._data.get('name', '')
