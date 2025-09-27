# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_arc_zonal_shift import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AutoshiftInResource:
    boto3_raw_data: "type_defs.AutoshiftInResourceTypeDef" = dataclasses.field()

    appliedStatus = field("appliedStatus")
    awayFrom = field("awayFrom")
    startTime = field("startTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AutoshiftInResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoshiftInResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoshiftSummary:
    boto3_raw_data: "type_defs.AutoshiftSummaryTypeDef" = dataclasses.field()

    awayFrom = field("awayFrom")
    startTime = field("startTime")
    status = field("status")
    endTime = field("endTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutoshiftSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoshiftSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelPracticeRunRequest:
    boto3_raw_data: "type_defs.CancelPracticeRunRequestTypeDef" = dataclasses.field()

    zonalShiftId = field("zonalShiftId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelPracticeRunRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelPracticeRunRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseMetadata:
    boto3_raw_data: "type_defs.ResponseMetadataTypeDef" = dataclasses.field()

    RequestId = field("RequestId")
    HTTPStatusCode = field("HTTPStatusCode")
    HTTPHeaders = field("HTTPHeaders")
    RetryAttempts = field("RetryAttempts")
    HostId = field("HostId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResponseMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelZonalShiftRequest:
    boto3_raw_data: "type_defs.CancelZonalShiftRequestTypeDef" = dataclasses.field()

    zonalShiftId = field("zonalShiftId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelZonalShiftRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelZonalShiftRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ControlCondition:
    boto3_raw_data: "type_defs.ControlConditionTypeDef" = dataclasses.field()

    type = field("type")
    alarmIdentifier = field("alarmIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ControlConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ControlConditionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePracticeRunConfigurationRequest:
    boto3_raw_data: "type_defs.DeletePracticeRunConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    resourceIdentifier = field("resourceIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeletePracticeRunConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePracticeRunConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetManagedResourceRequest:
    boto3_raw_data: "type_defs.GetManagedResourceRequestTypeDef" = dataclasses.field()

    resourceIdentifier = field("resourceIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetManagedResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetManagedResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ZonalShiftInResource:
    boto3_raw_data: "type_defs.ZonalShiftInResourceTypeDef" = dataclasses.field()

    appliedStatus = field("appliedStatus")
    zonalShiftId = field("zonalShiftId")
    resourceIdentifier = field("resourceIdentifier")
    awayFrom = field("awayFrom")
    expiryTime = field("expiryTime")
    startTime = field("startTime")
    comment = field("comment")
    shiftType = field("shiftType")
    practiceRunOutcome = field("practiceRunOutcome")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ZonalShiftInResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ZonalShiftInResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PaginatorConfig:
    boto3_raw_data: "type_defs.PaginatorConfigTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    PageSize = field("PageSize")
    StartingToken = field("StartingToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PaginatorConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PaginatorConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAutoshiftsRequest:
    boto3_raw_data: "type_defs.ListAutoshiftsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    status = field("status")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAutoshiftsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAutoshiftsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedResourcesRequest:
    boto3_raw_data: "type_defs.ListManagedResourcesRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListManagedResourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListZonalShiftsRequest:
    boto3_raw_data: "type_defs.ListZonalShiftsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    status = field("status")
    maxResults = field("maxResults")
    resourceIdentifier = field("resourceIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListZonalShiftsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListZonalShiftsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ZonalShiftSummary:
    boto3_raw_data: "type_defs.ZonalShiftSummaryTypeDef" = dataclasses.field()

    zonalShiftId = field("zonalShiftId")
    resourceIdentifier = field("resourceIdentifier")
    awayFrom = field("awayFrom")
    expiryTime = field("expiryTime")
    startTime = field("startTime")
    status = field("status")
    comment = field("comment")
    shiftType = field("shiftType")
    practiceRunOutcome = field("practiceRunOutcome")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ZonalShiftSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ZonalShiftSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartPracticeRunRequest:
    boto3_raw_data: "type_defs.StartPracticeRunRequestTypeDef" = dataclasses.field()

    resourceIdentifier = field("resourceIdentifier")
    awayFrom = field("awayFrom")
    comment = field("comment")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartPracticeRunRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartPracticeRunRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartZonalShiftRequest:
    boto3_raw_data: "type_defs.StartZonalShiftRequestTypeDef" = dataclasses.field()

    resourceIdentifier = field("resourceIdentifier")
    awayFrom = field("awayFrom")
    expiresIn = field("expiresIn")
    comment = field("comment")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartZonalShiftRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartZonalShiftRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAutoshiftObserverNotificationStatusRequest:
    boto3_raw_data: (
        "type_defs.UpdateAutoshiftObserverNotificationStatusRequestTypeDef"
    ) = dataclasses.field()

    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAutoshiftObserverNotificationStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.UpdateAutoshiftObserverNotificationStatusRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateZonalAutoshiftConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateZonalAutoshiftConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    resourceIdentifier = field("resourceIdentifier")
    zonalAutoshiftStatus = field("zonalAutoshiftStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateZonalAutoshiftConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateZonalAutoshiftConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateZonalShiftRequest:
    boto3_raw_data: "type_defs.UpdateZonalShiftRequestTypeDef" = dataclasses.field()

    zonalShiftId = field("zonalShiftId")
    comment = field("comment")
    expiresIn = field("expiresIn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateZonalShiftRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateZonalShiftRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelPracticeRunResponse:
    boto3_raw_data: "type_defs.CancelPracticeRunResponseTypeDef" = dataclasses.field()

    zonalShiftId = field("zonalShiftId")
    resourceIdentifier = field("resourceIdentifier")
    awayFrom = field("awayFrom")
    expiryTime = field("expiryTime")
    startTime = field("startTime")
    status = field("status")
    comment = field("comment")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelPracticeRunResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelPracticeRunResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePracticeRunConfigurationResponse:
    boto3_raw_data: "type_defs.DeletePracticeRunConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    name = field("name")
    zonalAutoshiftStatus = field("zonalAutoshiftStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeletePracticeRunConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePracticeRunConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutoshiftObserverNotificationStatusResponse:
    boto3_raw_data: (
        "type_defs.GetAutoshiftObserverNotificationStatusResponseTypeDef"
    ) = dataclasses.field()

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAutoshiftObserverNotificationStatusResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.GetAutoshiftObserverNotificationStatusResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAutoshiftsResponse:
    boto3_raw_data: "type_defs.ListAutoshiftsResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return AutoshiftSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAutoshiftsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAutoshiftsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartPracticeRunResponse:
    boto3_raw_data: "type_defs.StartPracticeRunResponseTypeDef" = dataclasses.field()

    zonalShiftId = field("zonalShiftId")
    resourceIdentifier = field("resourceIdentifier")
    awayFrom = field("awayFrom")
    expiryTime = field("expiryTime")
    startTime = field("startTime")
    status = field("status")
    comment = field("comment")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartPracticeRunResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartPracticeRunResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAutoshiftObserverNotificationStatusResponse:
    boto3_raw_data: (
        "type_defs.UpdateAutoshiftObserverNotificationStatusResponseTypeDef"
    ) = dataclasses.field()

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAutoshiftObserverNotificationStatusResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.UpdateAutoshiftObserverNotificationStatusResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateZonalAutoshiftConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateZonalAutoshiftConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    resourceIdentifier = field("resourceIdentifier")
    zonalAutoshiftStatus = field("zonalAutoshiftStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateZonalAutoshiftConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateZonalAutoshiftConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ZonalShift:
    boto3_raw_data: "type_defs.ZonalShiftTypeDef" = dataclasses.field()

    zonalShiftId = field("zonalShiftId")
    resourceIdentifier = field("resourceIdentifier")
    awayFrom = field("awayFrom")
    expiryTime = field("expiryTime")
    startTime = field("startTime")
    status = field("status")
    comment = field("comment")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ZonalShiftTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ZonalShiftTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePracticeRunConfigurationRequest:
    boto3_raw_data: "type_defs.CreatePracticeRunConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    resourceIdentifier = field("resourceIdentifier")

    @cached_property
    def outcomeAlarms(self):  # pragma: no cover
        return ControlCondition.make_many(self.boto3_raw_data["outcomeAlarms"])

    blockedWindows = field("blockedWindows")
    blockedDates = field("blockedDates")

    @cached_property
    def blockingAlarms(self):  # pragma: no cover
        return ControlCondition.make_many(self.boto3_raw_data["blockingAlarms"])

    allowedWindows = field("allowedWindows")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePracticeRunConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePracticeRunConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PracticeRunConfiguration:
    boto3_raw_data: "type_defs.PracticeRunConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def outcomeAlarms(self):  # pragma: no cover
        return ControlCondition.make_many(self.boto3_raw_data["outcomeAlarms"])

    @cached_property
    def blockingAlarms(self):  # pragma: no cover
        return ControlCondition.make_many(self.boto3_raw_data["blockingAlarms"])

    blockedWindows = field("blockedWindows")
    allowedWindows = field("allowedWindows")
    blockedDates = field("blockedDates")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PracticeRunConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PracticeRunConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePracticeRunConfigurationRequest:
    boto3_raw_data: "type_defs.UpdatePracticeRunConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    resourceIdentifier = field("resourceIdentifier")
    blockedWindows = field("blockedWindows")
    blockedDates = field("blockedDates")

    @cached_property
    def blockingAlarms(self):  # pragma: no cover
        return ControlCondition.make_many(self.boto3_raw_data["blockingAlarms"])

    allowedWindows = field("allowedWindows")

    @cached_property
    def outcomeAlarms(self):  # pragma: no cover
        return ControlCondition.make_many(self.boto3_raw_data["outcomeAlarms"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePracticeRunConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePracticeRunConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedResourceSummary:
    boto3_raw_data: "type_defs.ManagedResourceSummaryTypeDef" = dataclasses.field()

    availabilityZones = field("availabilityZones")
    arn = field("arn")
    name = field("name")
    appliedWeights = field("appliedWeights")

    @cached_property
    def zonalShifts(self):  # pragma: no cover
        return ZonalShiftInResource.make_many(self.boto3_raw_data["zonalShifts"])

    @cached_property
    def autoshifts(self):  # pragma: no cover
        return AutoshiftInResource.make_many(self.boto3_raw_data["autoshifts"])

    zonalAutoshiftStatus = field("zonalAutoshiftStatus")
    practiceRunStatus = field("practiceRunStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedResourceSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedResourceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAutoshiftsRequestPaginate:
    boto3_raw_data: "type_defs.ListAutoshiftsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAutoshiftsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAutoshiftsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedResourcesRequestPaginate:
    boto3_raw_data: "type_defs.ListManagedResourcesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListManagedResourcesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedResourcesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListZonalShiftsRequestPaginate:
    boto3_raw_data: "type_defs.ListZonalShiftsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    status = field("status")
    resourceIdentifier = field("resourceIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListZonalShiftsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListZonalShiftsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListZonalShiftsResponse:
    boto3_raw_data: "type_defs.ListZonalShiftsResponseTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return ZonalShiftSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListZonalShiftsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListZonalShiftsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePracticeRunConfigurationResponse:
    boto3_raw_data: "type_defs.CreatePracticeRunConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    name = field("name")
    zonalAutoshiftStatus = field("zonalAutoshiftStatus")

    @cached_property
    def practiceRunConfiguration(self):  # pragma: no cover
        return PracticeRunConfiguration.make_one(
            self.boto3_raw_data["practiceRunConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePracticeRunConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePracticeRunConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetManagedResourceResponse:
    boto3_raw_data: "type_defs.GetManagedResourceResponseTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    appliedWeights = field("appliedWeights")

    @cached_property
    def zonalShifts(self):  # pragma: no cover
        return ZonalShiftInResource.make_many(self.boto3_raw_data["zonalShifts"])

    @cached_property
    def autoshifts(self):  # pragma: no cover
        return AutoshiftInResource.make_many(self.boto3_raw_data["autoshifts"])

    @cached_property
    def practiceRunConfiguration(self):  # pragma: no cover
        return PracticeRunConfiguration.make_one(
            self.boto3_raw_data["practiceRunConfiguration"]
        )

    zonalAutoshiftStatus = field("zonalAutoshiftStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetManagedResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetManagedResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePracticeRunConfigurationResponse:
    boto3_raw_data: "type_defs.UpdatePracticeRunConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    name = field("name")
    zonalAutoshiftStatus = field("zonalAutoshiftStatus")

    @cached_property
    def practiceRunConfiguration(self):  # pragma: no cover
        return PracticeRunConfiguration.make_one(
            self.boto3_raw_data["practiceRunConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePracticeRunConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePracticeRunConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedResourcesResponse:
    boto3_raw_data: "type_defs.ListManagedResourcesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return ManagedResourceSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListManagedResourcesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedResourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
