from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from templafy.types import UNSET, Unset

T = TypeVar("T", bound="ConflictProblemDetails")


@_attrs_define
class ConflictProblemDetails:
    """Example:
        {'title': 'Conflict', 'detail': 'The request could not be completed due to a conflict with the current state of
            the resource.', 'status': 409, 'traceId': 'd61f7ce-cccb-4e5b-8727-3b68a61a0559'}

    Attributes:
        type_ (Union[None, Unset, str]):
        title (Union[None, Unset, str]):
        status (Union[None, Unset, int]):
        detail (Union[None, Unset, str]):
        instance (Union[None, Unset, str]):
        trace_id (Union[None, Unset, str]):
    """

    type_: None | Unset | str = UNSET
    title: None | Unset | str = UNSET
    status: None | Unset | int = UNSET
    detail: None | Unset | str = UNSET
    instance: None | Unset | str = UNSET
    trace_id: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        """Convert the object to a dictionary."""
        type_: None | Unset | str
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        title: None | Unset | str
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        status: None | Unset | int
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        detail: None | Unset | str
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail

        instance: None | Unset | str
        if isinstance(self.instance, Unset):
            instance = UNSET
        else:
            instance = self.instance

        trace_id: None | Unset | str
        if isinstance(self.trace_id, Unset):
            trace_id = UNSET
        else:
            trace_id = self.trace_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if title is not UNSET:
            field_dict["title"] = title
        if status is not UNSET:
            field_dict["status"] = status
        if detail is not UNSET:
            field_dict["detail"] = detail
        if instance is not UNSET:
            field_dict["instance"] = instance
        if trace_id is not UNSET:
            field_dict["traceId"] = trace_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        """Create an instance from a dictionary."""
        d = dict(src_dict)

        def _parse_type_(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_title(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_status(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | int", data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_detail(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        detail = _parse_detail(d.pop("detail", UNSET))

        def _parse_instance(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        instance = _parse_instance(d.pop("instance", UNSET))

        def _parse_trace_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast("None | Unset | str", data)

        trace_id = _parse_trace_id(d.pop("traceId", UNSET))

        conflict_problem_details = cls(
            type_=type_,
            title=title,
            status=status,
            detail=detail,
            instance=instance,
            trace_id=trace_id,
        )

        return conflict_problem_details
