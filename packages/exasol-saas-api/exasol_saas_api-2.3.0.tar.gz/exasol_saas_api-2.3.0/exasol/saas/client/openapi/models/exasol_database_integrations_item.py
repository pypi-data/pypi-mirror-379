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
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import (
    UNSET,
    Unset,
)

T = TypeVar("T", bound="ExasolDatabaseIntegrationsItem")


@_attrs_define
class ExasolDatabaseIntegrationsItem:
    """
    Attributes:
        id (str):
        name (str):
        url (Union[Unset, str]):
    """

    id: str
    name: str
    url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        url = d.pop("url", UNSET)

        exasol_database_integrations_item = cls(
            id=id,
            name=name,
            url=url,
        )

        exasol_database_integrations_item.additional_properties = d
        return exasol_database_integrations_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
