from __future__ import annotations

from collections.abc import Callable
from http.cookiejar import CookieJar
from typing import Any, TypedDict, TypeVar

try:
    from typing import Literal, NotRequired
except ImportError:
    from typing import Literal, NotRequired


class ProfileTypeT(TypedDict):
    unique_name: str
    id: int
    info: str | None
    find_strict: bool
    name: str
    is_google: bool
    two_step_enabled: bool
    has_password: bool
    phoneconfirmed: NotRequired[bool]
    email: str
    phonenumber: NotRequired[str | None]
    active: bool
    deleted: bool
    info_parsed: NotRequired[list[TextParsedT] | None]
    info_chat: NotRequired[int | None]
    is_bot: bool
    name_trans: NotRequired[str]
    organizations: list[int]
    time_created: str
    time_updated: str
    timezone_offset_minutes: NotRequired[int | None]


# noinspection PyUnresolvedReferences
class TextParsedT(TypedDict):
    type: str
    value: str
    name: NotRequired[str]
    id: NotRequired[int]


# noinspection PyUnresolvedReferences
class PostMetaUserT(TypedDict):
    id: int
    name: str
    unique_name: str
    is_bot: NotRequired[bool]


class BotProfileT(TypedDict):
    id: int
    active: bool
    deleted: bool
    email: str | None
    find_strict: bool
    has_password: bool
    info: str | None
    info_parsed: list
    info_chat: int
    is_bot: bool
    is_google: bool
    name: str
    name_trans: str
    unique_name: str
    organizations: list
    phoneconfirmed: bool
    phonenumber: str | None
    time_created: str
    time_updated: str
    two_step_enabled: bool


class PostMetaFileT(TypedDict):
    name: str
    guid: str
    size: int
    mime_type: str
    origin: tuple[int, int]


class MetaReplyT(TypedDict):
    text: str
    user_id: int
    user_name: str
    in_thread_no: int


class PostMetaThreadT(TypedDict):
    title: str


class PostMetaT(TypedDict):
    user: PostMetaUserT
    thread: PostMetaThreadT
    file: PostMetaFileT
    reply: MetaReplyT
    attachments: list[str]


class PostMention(TypedDict):
    id: int
    name: str
    value: str


class BaseEvent(TypedDict):
    type: Literal[
        'GROUP_LEAVED',
        'GROUP_DELETED',
        'ORG_MEMBERS',
        'GROUP_CREATED',
        'GROUP_UPDATED',
        'ENTER_TO_THREAD',
        'CALL',
        'POST_PINNED',
        'NEW_THREAD',
        'EDIT_THREAD',
        'ENTER_TO_THREAD',
        'CHAT_TITLE',
    ]
    data: dict[str, Any]


class ChatTagT(TypedDict):
    tag: str
    chat_ids: list[int]


class ChatTagsResponseT(TypedDict):
    sync_time: str
    chats_tags: list[ChatTagT]


class TeamT(TypedDict):
    id: int
    slug: str
    title: str
    description: str
    email_domain: NotRequired[str | None]
    time_created: str
    time_updated: str
    two_step_required: bool
    default_chat_id: int
    is_member: bool
    is_admin: bool
    state: str
    inviter_id: NotRequired[int | None]
    guests: list[int]
    users: list[int]
    admins: list[int]
    groups: list[int]
    description_parsed: NotRequired[list[TextParsedT] | None]


class TeamsResponseT(TypedDict):
    orgs: list[TeamT]
    unavailable: NotRequired[list[int]]


class GroupSyncResponseT(TypedDict):
    """Response from group synchronization endpoint."""

    new: list[int]
    groups: list[int]
    removed: list[int]


class GroupAccessT(TypedDict):
    """Group access information response."""

    access: str  # Returns "OK" when user has access


class GroupOperationResponseT(TypedDict):
    """Response from group operations like leave, add/remove members."""

    group_id: int


FormatterT = dict[str, Callable[[dict[str, Any], str], Any]]
CookieJarT = TypeVar('CookieJarT', bound=CookieJar)
QuoteRangeT = dict[str, str | int]
HeaderLikeT = dict[str, str]
SecondStepFnT = Callable[[CookieJar, dict[str, str], str], tuple[bool, dict[str, str]]]
