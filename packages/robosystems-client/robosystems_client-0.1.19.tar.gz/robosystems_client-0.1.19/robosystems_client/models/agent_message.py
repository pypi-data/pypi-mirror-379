import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentMessage")


@_attrs_define
class AgentMessage:
  """Message in conversation history.

  Attributes:
      role (str): Message role (user/assistant)
      content (str): Message content
      timestamp (Union[None, Unset, datetime.datetime]): Message timestamp
  """

  role: str
  content: str
  timestamp: Union[None, Unset, datetime.datetime] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    role = self.role

    content = self.content

    timestamp: Union[None, Unset, str]
    if isinstance(self.timestamp, Unset):
      timestamp = UNSET
    elif isinstance(self.timestamp, datetime.datetime):
      timestamp = self.timestamp.isoformat()
    else:
      timestamp = self.timestamp

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "role": role,
        "content": content,
      }
    )
    if timestamp is not UNSET:
      field_dict["timestamp"] = timestamp

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    role = d.pop("role")

    content = d.pop("content")

    def _parse_timestamp(data: object) -> Union[None, Unset, datetime.datetime]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        timestamp_type_0 = isoparse(data)

        return timestamp_type_0
      except:  # noqa: E722
        pass
      return cast(Union[None, Unset, datetime.datetime], data)

    timestamp = _parse_timestamp(d.pop("timestamp", UNSET))

    agent_message = cls(
      role=role,
      content=content,
      timestamp=timestamp,
    )

    agent_message.additional_properties = d
    return agent_message

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
