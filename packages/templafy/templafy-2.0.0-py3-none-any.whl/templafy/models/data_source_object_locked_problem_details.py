from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from templafy.models.lock_reason import LockReason
from templafy.types import UNSET, Unset

if TYPE_CHECKING:
    from templafy.models.dependency import Dependency
from templafy.models.dependency import Dependency

T = TypeVar("T", bound="DataSourceObjectLockedProblemDetails")


@_attrs_define
class DataSourceObjectLockedProblemDetails:
    """The reason the resource is locked with an optional array of dependencies. Dependencies array is populated only when
    lockedReason is hardDependency and contains a maximum of 50 items per sourceEntityType

    Example:
            {'title': 'Locked', 'detail': 'The data source item cannot be deleted because it has been used by another
                resource.', 'status': 423, 'traceId': 'd61f7ce-cccb-4e5b-8727-3b68a61a0559', 'lockReason': 'hardDependency',
                'dependencies': [{'sourceEntityType': 'dataSourceItem', 'sourceEntityId': '1031936131644784655', 'description':
                "There is a dependency from 'DataSourceItem'."}]}

    Attributes:
            lock_reason (Union[Unset, LockReason]): The reason the resource is locked. It is either because the resource is
                depended upon by another resource or the resource has restricted access and cannot be modified.
            dependencies (Union[None, Unset, list['Dependency']]):
            type_ (Union[None, Unset, str]):
            title (Union[None, Unset, str]):
            status (Union[None, Unset, int]):
            detail (Union[None, Unset, str]):
            instance (Union[None, Unset, str]):
            trace_id (Union[None, Unset, str]):
    """

    lock_reason: Unset | LockReason = UNSET
    dependencies: None | Unset | list["Dependency"] = UNSET
    type_: None | Unset | str = UNSET
    title: None | Unset | str = UNSET
    status: None | Unset | int = UNSET
    detail: None | Unset | str = UNSET
    instance: None | Unset | str = UNSET
    trace_id: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        lock_reason: Unset | str = UNSET
        if not isinstance(self.lock_reason, Unset):
            lock_reason = self.lock_reason.value

        dependencies: None | Unset | list[dict[str, Any]]
        if isinstance(self.dependencies, Unset):
            dependencies = UNSET
        elif isinstance(self.dependencies, list):
            dependencies = []
            for dependencies_type_0_item_data in self.dependencies:
                dependencies_type_0_item = dependencies_type_0_item_data.to_dict()
                dependencies.append(dependencies_type_0_item)

        else:
            dependencies = self.dependencies

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
        if lock_reason is not UNSET:
            field_dict["lockReason"] = lock_reason
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
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
        # Top-level imports are used to avoid inline imports (PLC0415)
        d = dict(src_dict)
        _lock_reason = d.pop("lockReason", UNSET)
        lock_reason: Unset | LockReason
        if isinstance(_lock_reason, Unset):
            lock_reason = UNSET
        else:
            lock_reason = LockReason(_lock_reason)

        def _parse_dependencies(data: object) -> None | Unset | list["Dependency"]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError
                dependencies_type_0 = []
                _dependencies_type_0 = data
                for dependencies_type_0_item_data in _dependencies_type_0:
                    dependencies_type_0_item = Dependency.from_dict(
                        dependencies_type_0_item_data
                    )

                    dependencies_type_0.append(dependencies_type_0_item)

                return dependencies_type_0
            except:  # noqa: E722
                pass
            return cast("None | Unset | list[Dependency]", data)

        dependencies = _parse_dependencies(d.pop("dependencies", UNSET))

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

        data_source_object_locked_problem_details = cls(
            lock_reason=lock_reason,
            dependencies=dependencies,
            type_=type_,
            title=title,
            status=status,
            detail=detail,
            instance=instance,
            trace_id=trace_id,
        )

        return data_source_object_locked_problem_details
