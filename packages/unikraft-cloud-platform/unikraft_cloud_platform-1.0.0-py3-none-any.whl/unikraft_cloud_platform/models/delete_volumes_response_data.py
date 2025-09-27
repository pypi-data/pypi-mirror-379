from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delete_volumes_response_deleted_volume import DeleteVolumesResponseDeletedVolume


T = TypeVar("T", bound="DeleteVolumesResponseData")


@_attrs_define
class DeleteVolumesResponseData:
    volumes: Union[Unset, list["DeleteVolumesResponseDeletedVolume"]] = UNSET
    """ The volume(s) which were deleted by the request. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        volumes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.volumes, Unset):
            volumes = []
            for volumes_item_data in self.volumes:
                volumes_item = volumes_item_data.to_dict()
                volumes.append(volumes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if volumes is not UNSET:
            field_dict["volumes"] = volumes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delete_volumes_response_deleted_volume import DeleteVolumesResponseDeletedVolume

        d = dict(src_dict)
        volumes = []
        _volumes = d.pop("volumes", UNSET)
        for volumes_item_data in _volumes or []:
            volumes_item = DeleteVolumesResponseDeletedVolume.from_dict(volumes_item_data)

            volumes.append(volumes_item)

        delete_volumes_response_data = cls(
            volumes=volumes,
        )

        delete_volumes_response_data.additional_properties = d
        return delete_volumes_response_data

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
