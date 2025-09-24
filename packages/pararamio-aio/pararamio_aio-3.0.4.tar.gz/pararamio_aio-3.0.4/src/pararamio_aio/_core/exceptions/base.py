from __future__ import annotations

__all__ = (
    'PararamModelNotLoadedError',
    'PararamMultipleFoundError',
    'PararamNoNextPostError',
    'PararamNoPrevPostError',
    'PararamNotFoundError',
    'PararamioAuthenticationError',
    'PararamioCaptchaAuthenticationError',
    'PararamioException',
    'PararamioHTTPRequestError',
    'PararamioLimitExceededError',
    'PararamioMethodNotAllowedError',
    'PararamioPasswordAuthenticationError',
    'PararamioRequestError',
    'PararamioSecondFactorAuthenticationError',
    'PararamioServerResponseError',
    'PararamioValidationError',
    'PararamioXSRFRequestError',
)

import json
from json import JSONDecodeError
from typing import IO
from urllib.error import HTTPError


class PararamioException(Exception):  # noqa: N818
    pass


class PararamioValidationError(PararamioException):
    pass


class PararamModelNotLoadedError(PararamioException):
    """Exception raised when trying to access an attribute that hasn't been loaded yet."""


class PararamNotFoundError(PararamioException):
    """Exception raised when expected item is not found."""

    def __init__(self, message: str = 'Expected item not found'):
        super().__init__(message)


class PararamMultipleFoundError(PararamioException):
    """Exception raised when multiple items found when expecting exactly one."""

    def __init__(self, message: str = 'Multiple items found when expecting one'):
        super().__init__(message)


class PararamioHTTPRequestError(HTTPError, PararamioException):  # pylint: disable=too-many-ancestors
    _response: bytes | None
    fp: IO[bytes]

    def __init__(self, url: str, code: int, msg: str, hdrs: list[tuple[str, str]], fp: IO[bytes]):
        self._response = None
        self.msg = msg
        super().__init__(url, code, msg, hdrs, fp)  # type: ignore

    @property
    def response(self):
        if not self._response and self.fp is not None:
            self._response = self.fp.read()
        return self._response

    @property
    def message(self) -> str | None:
        if self.code in [403, 400]:
            try:
                resp = json.loads(self.response)
                return resp.get('error', None) or resp.get('message', None)
            except JSONDecodeError:
                pass
        return None

    def __str__(self):
        msg = self.message
        if msg:
            return msg
        return str(super(HTTPError, self))


class PararamioRequestError(PararamioException):
    pass


class PararamioServerResponseError(PararamioRequestError):
    response: dict

    def __init__(self, msg: str, response: dict):
        self.msg = msg
        self.response = response

    def __str__(self):
        return f'{self.__class__.__name__}, {self.msg or " has been raised"}'


class PararamioLimitExceededError(PararamioRequestError):
    pass


class PararamioMethodNotAllowedError(PararamioException):
    pass


class PararamioAuthenticationError(PararamioException):
    """Base authentication exception."""

    def __init__(self, message: str, error_code: str | None = None, **kwargs):
        super().__init__(message)
        self.error_code = error_code
        self.retry_after: int | None = kwargs.get('retry_after')


class PararamioXSRFRequestError(PararamioAuthenticationError):
    pass


class PararamioPasswordAuthenticationError(PararamioAuthenticationError):
    pass


class PararamioSecondFactorAuthenticationError(PararamioAuthenticationError):
    pass


class PararamioCaptchaAuthenticationError(PararamioAuthenticationError):
    pass


class PararamNoNextPostError(PararamioException, StopIteration):
    pass


class PararamNoPrevPostError(PararamioException, StopIteration):
    pass
