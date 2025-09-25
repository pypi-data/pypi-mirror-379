from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAPIKeyRequest")


@_attrs_define
class CreateAPIKeyRequest:
  """Request model for creating a new API key.

  Attributes:
      name (str): Name for the API key
      description (Union[None, Unset, str]): Optional description
      expires_at (Union[None, Unset, str]): Optional expiration date in ISO format (e.g. 2024-12-31T23:59:59Z)
  """

  name: str
  description: Union[None, Unset, str] = UNSET
  expires_at: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    description: Union[None, Unset, str]
    if isinstance(self.description, Unset):
      description = UNSET
    else:
      description = self.description

    expires_at: Union[None, Unset, str]
    if isinstance(self.expires_at, Unset):
      expires_at = UNSET
    else:
      expires_at = self.expires_at

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
      }
    )
    if description is not UNSET:
      field_dict["description"] = description
    if expires_at is not UNSET:
      field_dict["expires_at"] = expires_at

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    name = d.pop("name")

    def _parse_description(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    description = _parse_description(d.pop("description", UNSET))

    def _parse_expires_at(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

    create_api_key_request = cls(
      name=name,
      description=description,
      expires_at=expires_at,
    )

    create_api_key_request.additional_properties = d
    return create_api_key_request

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
