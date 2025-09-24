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
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import (
    UNSET,
    Unset,
)

if TYPE_CHECKING:
    from ..models.auto_stop import AutoStop
    from ..models.cluster_settings_update import ClusterSettingsUpdate


T = TypeVar("T", bound="UpdateCluster")


@_attrs_define
class UpdateCluster:
    """
    Attributes:
        name (Union[Unset, str]):
        auto_stop (Union[Unset, AutoStop]):
        settings (Union[Unset, ClusterSettingsUpdate]):
    """

    name: Union[Unset, str] = UNSET
    auto_stop: Union[Unset, "AutoStop"] = UNSET
    settings: Union[Unset, "ClusterSettingsUpdate"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.auto_stop import AutoStop
        from ..models.cluster_settings_update import ClusterSettingsUpdate

        name = self.name

        auto_stop: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.auto_stop, Unset):
            auto_stop = self.auto_stop.to_dict()

        settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if auto_stop is not UNSET:
            field_dict["autoStop"] = auto_stop
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auto_stop import AutoStop
        from ..models.cluster_settings_update import ClusterSettingsUpdate

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _auto_stop = d.pop("autoStop", UNSET)
        auto_stop: Union[Unset, AutoStop]
        if isinstance(_auto_stop, Unset):
            auto_stop = UNSET
        else:
            auto_stop = AutoStop.from_dict(_auto_stop)

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, ClusterSettingsUpdate]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = ClusterSettingsUpdate.from_dict(_settings)

        update_cluster = cls(
            name=name,
            auto_stop=auto_stop,
            settings=settings,
        )

        return update_cluster
