from collections.abc import (
    Generator,
    Mapping,
)
from typing import (
    TYPE_CHECKING,
    Any,
    BinaryIO,
    Optional,
    TextIO,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="DownloadFile")


@_attrs_define
class DownloadFile:
    """
    Attributes:
        url (str):
    """

    url: str

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        download_file = cls(
            url=url,
        )

        return download_file
