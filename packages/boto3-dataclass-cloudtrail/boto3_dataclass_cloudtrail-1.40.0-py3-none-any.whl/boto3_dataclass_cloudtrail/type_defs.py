# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cloudtrail import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdvancedFieldSelectorOutput:
    boto3_raw_data: "type_defs.AdvancedFieldSelectorOutputTypeDef" = dataclasses.field()

    Field = field("Field")
    Equals = field("Equals")
    StartsWith = field("StartsWith")
    EndsWith = field("EndsWith")
    NotEquals = field("NotEquals")
    NotStartsWith = field("NotStartsWith")
    NotEndsWith = field("NotEndsWith")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdvancedFieldSelectorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdvancedFieldSelectorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdvancedFieldSelector:
    boto3_raw_data: "type_defs.AdvancedFieldSelectorTypeDef" = dataclasses.field()

    Field = field("Field")
    Equals = field("Equals")
    StartsWith = field("StartsWith")
    EndsWith = field("EndsWith")
    NotEquals = field("NotEquals")
    NotStartsWith = field("NotStartsWith")
    NotEndsWith = field("NotEndsWith")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdvancedFieldSelectorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdvancedFieldSelectorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelQueryRequest:
    boto3_raw_data: "type_defs.CancelQueryRequestTypeDef" = dataclasses.field()

    QueryId = field("QueryId")
    EventDataStore = field("EventDataStore")
    EventDataStoreOwnerAccountId = field("EventDataStoreOwnerAccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelQueryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelQueryRequestTypeDef"]
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
class Channel:
    boto3_raw_data: "type_defs.ChannelTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChannelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChannelTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContextKeySelectorOutput:
    boto3_raw_data: "type_defs.ContextKeySelectorOutputTypeDef" = dataclasses.field()

    Type = field("Type")
    Equals = field("Equals")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContextKeySelectorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContextKeySelectorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContextKeySelector:
    boto3_raw_data: "type_defs.ContextKeySelectorTypeDef" = dataclasses.field()

    Type = field("Type")
    Equals = field("Equals")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContextKeySelectorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContextKeySelectorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Destination:
    boto3_raw_data: "type_defs.DestinationTypeDef" = dataclasses.field()

    Type = field("Type")
    Location = field("Location")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DestinationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestWidget:
    boto3_raw_data: "type_defs.RequestWidgetTypeDef" = dataclasses.field()

    QueryStatement = field("QueryStatement")
    ViewProperties = field("ViewProperties")
    QueryParameters = field("QueryParameters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RequestWidgetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RequestWidgetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Widget:
    boto3_raw_data: "type_defs.WidgetTypeDef" = dataclasses.field()

    QueryAlias = field("QueryAlias")
    QueryStatement = field("QueryStatement")
    QueryParameters = field("QueryParameters")
    ViewProperties = field("ViewProperties")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WidgetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WidgetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DashboardDetail:
    boto3_raw_data: "type_defs.DashboardDetailTypeDef" = dataclasses.field()

    DashboardArn = field("DashboardArn")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DashboardDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DashboardDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataResourceOutput:
    boto3_raw_data: "type_defs.DataResourceOutputTypeDef" = dataclasses.field()

    Type = field("Type")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataResource:
    boto3_raw_data: "type_defs.DataResourceTypeDef" = dataclasses.field()

    Type = field("Type")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataResourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteChannelRequest:
    boto3_raw_data: "type_defs.DeleteChannelRequestTypeDef" = dataclasses.field()

    Channel = field("Channel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDashboardRequest:
    boto3_raw_data: "type_defs.DeleteDashboardRequestTypeDef" = dataclasses.field()

    DashboardId = field("DashboardId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDashboardRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDashboardRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventDataStoreRequest:
    boto3_raw_data: "type_defs.DeleteEventDataStoreRequestTypeDef" = dataclasses.field()

    EventDataStore = field("EventDataStore")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEventDataStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventDataStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourcePolicyRequest:
    boto3_raw_data: "type_defs.DeleteResourcePolicyRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTrailRequest:
    boto3_raw_data: "type_defs.DeleteTrailRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTrailRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTrailRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterOrganizationDelegatedAdminRequest:
    boto3_raw_data: "type_defs.DeregisterOrganizationDelegatedAdminRequestTypeDef" = (
        dataclasses.field()
    )

    DelegatedAdminAccountId = field("DelegatedAdminAccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeregisterOrganizationDelegatedAdminRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterOrganizationDelegatedAdminRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeQueryRequest:
    boto3_raw_data: "type_defs.DescribeQueryRequestTypeDef" = dataclasses.field()

    EventDataStore = field("EventDataStore")
    QueryId = field("QueryId")
    QueryAlias = field("QueryAlias")
    RefreshId = field("RefreshId")
    EventDataStoreOwnerAccountId = field("EventDataStoreOwnerAccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeQueryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeQueryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryStatisticsForDescribeQuery:
    boto3_raw_data: "type_defs.QueryStatisticsForDescribeQueryTypeDef" = (
        dataclasses.field()
    )

    EventsMatched = field("EventsMatched")
    EventsScanned = field("EventsScanned")
    BytesScanned = field("BytesScanned")
    ExecutionTimeInMillis = field("ExecutionTimeInMillis")
    CreationTime = field("CreationTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.QueryStatisticsForDescribeQueryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryStatisticsForDescribeQueryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrailsRequest:
    boto3_raw_data: "type_defs.DescribeTrailsRequestTypeDef" = dataclasses.field()

    trailNameList = field("trailNameList")
    includeShadowTrails = field("includeShadowTrails")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTrailsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrailsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Trail:
    boto3_raw_data: "type_defs.TrailTypeDef" = dataclasses.field()

    Name = field("Name")
    S3BucketName = field("S3BucketName")
    S3KeyPrefix = field("S3KeyPrefix")
    SnsTopicName = field("SnsTopicName")
    SnsTopicARN = field("SnsTopicARN")
    IncludeGlobalServiceEvents = field("IncludeGlobalServiceEvents")
    IsMultiRegionTrail = field("IsMultiRegionTrail")
    HomeRegion = field("HomeRegion")
    TrailARN = field("TrailARN")
    LogFileValidationEnabled = field("LogFileValidationEnabled")
    CloudWatchLogsLogGroupArn = field("CloudWatchLogsLogGroupArn")
    CloudWatchLogsRoleArn = field("CloudWatchLogsRoleArn")
    KmsKeyId = field("KmsKeyId")
    HasCustomEventSelectors = field("HasCustomEventSelectors")
    HasInsightSelectors = field("HasInsightSelectors")
    IsOrganizationTrail = field("IsOrganizationTrail")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TrailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableFederationRequest:
    boto3_raw_data: "type_defs.DisableFederationRequestTypeDef" = dataclasses.field()

    EventDataStore = field("EventDataStore")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableFederationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableFederationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableFederationRequest:
    boto3_raw_data: "type_defs.EnableFederationRequestTypeDef" = dataclasses.field()

    EventDataStore = field("EventDataStore")
    FederationRoleArn = field("FederationRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnableFederationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableFederationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Resource:
    boto3_raw_data: "type_defs.ResourceTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    ResourceName = field("ResourceName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateQueryRequest:
    boto3_raw_data: "type_defs.GenerateQueryRequestTypeDef" = dataclasses.field()

    EventDataStores = field("EventDataStores")
    Prompt = field("Prompt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerateQueryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateQueryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChannelRequest:
    boto3_raw_data: "type_defs.GetChannelRequestTypeDef" = dataclasses.field()

    Channel = field("Channel")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetChannelRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IngestionStatus:
    boto3_raw_data: "type_defs.IngestionStatusTypeDef" = dataclasses.field()

    LatestIngestionSuccessTime = field("LatestIngestionSuccessTime")
    LatestIngestionSuccessEventID = field("LatestIngestionSuccessEventID")
    LatestIngestionErrorCode = field("LatestIngestionErrorCode")
    LatestIngestionAttemptTime = field("LatestIngestionAttemptTime")
    LatestIngestionAttemptEventID = field("LatestIngestionAttemptEventID")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IngestionStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IngestionStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDashboardRequest:
    boto3_raw_data: "type_defs.GetDashboardRequestTypeDef" = dataclasses.field()

    DashboardId = field("DashboardId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDashboardRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDashboardRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventConfigurationRequest:
    boto3_raw_data: "type_defs.GetEventConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    EventDataStore = field("EventDataStore")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEventConfigurationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventDataStoreRequest:
    boto3_raw_data: "type_defs.GetEventDataStoreRequestTypeDef" = dataclasses.field()

    EventDataStore = field("EventDataStore")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEventDataStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventDataStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PartitionKey:
    boto3_raw_data: "type_defs.PartitionKeyTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PartitionKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PartitionKeyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventSelectorsRequest:
    boto3_raw_data: "type_defs.GetEventSelectorsRequestTypeDef" = dataclasses.field()

    TrailName = field("TrailName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEventSelectorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventSelectorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImportRequest:
    boto3_raw_data: "type_defs.GetImportRequestTypeDef" = dataclasses.field()

    ImportId = field("ImportId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetImportRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportStatistics:
    boto3_raw_data: "type_defs.ImportStatisticsTypeDef" = dataclasses.field()

    PrefixesFound = field("PrefixesFound")
    PrefixesCompleted = field("PrefixesCompleted")
    FilesCompleted = field("FilesCompleted")
    EventsCompleted = field("EventsCompleted")
    FailedEntries = field("FailedEntries")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportStatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInsightSelectorsRequest:
    boto3_raw_data: "type_defs.GetInsightSelectorsRequestTypeDef" = dataclasses.field()

    TrailName = field("TrailName")
    EventDataStore = field("EventDataStore")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInsightSelectorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInsightSelectorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InsightSelector:
    boto3_raw_data: "type_defs.InsightSelectorTypeDef" = dataclasses.field()

    InsightType = field("InsightType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InsightSelectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InsightSelectorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryResultsRequest:
    boto3_raw_data: "type_defs.GetQueryResultsRequestTypeDef" = dataclasses.field()

    QueryId = field("QueryId")
    EventDataStore = field("EventDataStore")
    NextToken = field("NextToken")
    MaxQueryResults = field("MaxQueryResults")
    EventDataStoreOwnerAccountId = field("EventDataStoreOwnerAccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQueryResultsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueryResultsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryStatistics:
    boto3_raw_data: "type_defs.QueryStatisticsTypeDef" = dataclasses.field()

    ResultsCount = field("ResultsCount")
    TotalResultsCount = field("TotalResultsCount")
    BytesScanned = field("BytesScanned")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryStatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryStatisticsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePolicyRequest:
    boto3_raw_data: "type_defs.GetResourcePolicyRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrailRequest:
    boto3_raw_data: "type_defs.GetTrailRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTrailRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetTrailRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrailStatusRequest:
    boto3_raw_data: "type_defs.GetTrailStatusRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTrailStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrailStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportFailureListItem:
    boto3_raw_data: "type_defs.ImportFailureListItemTypeDef" = dataclasses.field()

    Location = field("Location")
    Status = field("Status")
    ErrorType = field("ErrorType")
    ErrorMessage = field("ErrorMessage")
    LastUpdatedTime = field("LastUpdatedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportFailureListItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportFailureListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ImportSource:
    boto3_raw_data: "type_defs.S3ImportSourceTypeDef" = dataclasses.field()

    S3LocationUri = field("S3LocationUri")
    S3BucketRegion = field("S3BucketRegion")
    S3BucketAccessRoleArn = field("S3BucketAccessRoleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ImportSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3ImportSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportsListItem:
    boto3_raw_data: "type_defs.ImportsListItemTypeDef" = dataclasses.field()

    ImportId = field("ImportId")
    ImportStatus = field("ImportStatus")
    Destinations = field("Destinations")
    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportsListItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImportsListItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelsRequest:
    boto3_raw_data: "type_defs.ListChannelsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDashboardsRequest:
    boto3_raw_data: "type_defs.ListDashboardsRequestTypeDef" = dataclasses.field()

    NamePrefix = field("NamePrefix")
    Type = field("Type")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDashboardsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDashboardsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventDataStoresRequest:
    boto3_raw_data: "type_defs.ListEventDataStoresRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEventDataStoresRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventDataStoresRequestTypeDef"]
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
class ListImportFailuresRequest:
    boto3_raw_data: "type_defs.ListImportFailuresRequestTypeDef" = dataclasses.field()

    ImportId = field("ImportId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImportFailuresRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportFailuresRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportsRequest:
    boto3_raw_data: "type_defs.ListImportsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    Destination = field("Destination")
    ImportStatus = field("ImportStatus")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImportsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublicKey:
    boto3_raw_data: "type_defs.PublicKeyTypeDef" = dataclasses.field()

    Value = field("Value")
    ValidityStartTime = field("ValidityStartTime")
    ValidityEndTime = field("ValidityEndTime")
    Fingerprint = field("Fingerprint")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PublicKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PublicKeyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Query:
    boto3_raw_data: "type_defs.QueryTypeDef" = dataclasses.field()

    QueryId = field("QueryId")
    QueryStatus = field("QueryStatus")
    CreationTime = field("CreationTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsRequest:
    boto3_raw_data: "type_defs.ListTagsRequestTypeDef" = dataclasses.field()

    ResourceIdList = field("ResourceIdList")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTagsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListTagsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrailsRequest:
    boto3_raw_data: "type_defs.ListTrailsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTrailsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrailsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrailInfo:
    boto3_raw_data: "type_defs.TrailInfoTypeDef" = dataclasses.field()

    TrailARN = field("TrailARN")
    Name = field("Name")
    HomeRegion = field("HomeRegion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrailInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TrailInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LookupAttribute:
    boto3_raw_data: "type_defs.LookupAttributeTypeDef" = dataclasses.field()

    AttributeKey = field("AttributeKey")
    AttributeValue = field("AttributeValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LookupAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LookupAttributeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourcePolicyRequest:
    boto3_raw_data: "type_defs.PutResourcePolicyRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    ResourcePolicy = field("ResourcePolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RefreshScheduleFrequency:
    boto3_raw_data: "type_defs.RefreshScheduleFrequencyTypeDef" = dataclasses.field()

    Unit = field("Unit")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RefreshScheduleFrequencyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RefreshScheduleFrequencyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterOrganizationDelegatedAdminRequest:
    boto3_raw_data: "type_defs.RegisterOrganizationDelegatedAdminRequestTypeDef" = (
        dataclasses.field()
    )

    MemberAccountId = field("MemberAccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegisterOrganizationDelegatedAdminRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterOrganizationDelegatedAdminRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreEventDataStoreRequest:
    boto3_raw_data: "type_defs.RestoreEventDataStoreRequestTypeDef" = (
        dataclasses.field()
    )

    EventDataStore = field("EventDataStore")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RestoreEventDataStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreEventDataStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchSampleQueriesRequest:
    boto3_raw_data: "type_defs.SearchSampleQueriesRequestTypeDef" = dataclasses.field()

    SearchPhrase = field("SearchPhrase")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchSampleQueriesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchSampleQueriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchSampleQueriesSearchResult:
    boto3_raw_data: "type_defs.SearchSampleQueriesSearchResultTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Description = field("Description")
    SQL = field("SQL")
    Relevance = field("Relevance")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchSampleQueriesSearchResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchSampleQueriesSearchResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDashboardRefreshRequest:
    boto3_raw_data: "type_defs.StartDashboardRefreshRequestTypeDef" = (
        dataclasses.field()
    )

    DashboardId = field("DashboardId")
    QueryParameterValues = field("QueryParameterValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartDashboardRefreshRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDashboardRefreshRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartEventDataStoreIngestionRequest:
    boto3_raw_data: "type_defs.StartEventDataStoreIngestionRequestTypeDef" = (
        dataclasses.field()
    )

    EventDataStore = field("EventDataStore")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartEventDataStoreIngestionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartEventDataStoreIngestionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartLoggingRequest:
    boto3_raw_data: "type_defs.StartLoggingRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartLoggingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartLoggingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartQueryRequest:
    boto3_raw_data: "type_defs.StartQueryRequestTypeDef" = dataclasses.field()

    QueryStatement = field("QueryStatement")
    DeliveryS3Uri = field("DeliveryS3Uri")
    QueryAlias = field("QueryAlias")
    QueryParameters = field("QueryParameters")
    EventDataStoreOwnerAccountId = field("EventDataStoreOwnerAccountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartQueryRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartQueryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopEventDataStoreIngestionRequest:
    boto3_raw_data: "type_defs.StopEventDataStoreIngestionRequestTypeDef" = (
        dataclasses.field()
    )

    EventDataStore = field("EventDataStore")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StopEventDataStoreIngestionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopEventDataStoreIngestionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopImportRequest:
    boto3_raw_data: "type_defs.StopImportRequestTypeDef" = dataclasses.field()

    ImportId = field("ImportId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopImportRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopImportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopLoggingRequest:
    boto3_raw_data: "type_defs.StopLoggingRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopLoggingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopLoggingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTrailRequest:
    boto3_raw_data: "type_defs.UpdateTrailRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    S3BucketName = field("S3BucketName")
    S3KeyPrefix = field("S3KeyPrefix")
    SnsTopicName = field("SnsTopicName")
    IncludeGlobalServiceEvents = field("IncludeGlobalServiceEvents")
    IsMultiRegionTrail = field("IsMultiRegionTrail")
    EnableLogFileValidation = field("EnableLogFileValidation")
    CloudWatchLogsLogGroupArn = field("CloudWatchLogsLogGroupArn")
    CloudWatchLogsRoleArn = field("CloudWatchLogsRoleArn")
    KmsKeyId = field("KmsKeyId")
    IsOrganizationTrail = field("IsOrganizationTrail")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTrailRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTrailRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddTagsRequest:
    boto3_raw_data: "type_defs.AddTagsRequestTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")

    @cached_property
    def TagsList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagsList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddTagsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddTagsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrailRequest:
    boto3_raw_data: "type_defs.CreateTrailRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    S3BucketName = field("S3BucketName")
    S3KeyPrefix = field("S3KeyPrefix")
    SnsTopicName = field("SnsTopicName")
    IncludeGlobalServiceEvents = field("IncludeGlobalServiceEvents")
    IsMultiRegionTrail = field("IsMultiRegionTrail")
    EnableLogFileValidation = field("EnableLogFileValidation")
    CloudWatchLogsLogGroupArn = field("CloudWatchLogsLogGroupArn")
    CloudWatchLogsRoleArn = field("CloudWatchLogsRoleArn")
    KmsKeyId = field("KmsKeyId")
    IsOrganizationTrail = field("IsOrganizationTrail")

    @cached_property
    def TagsList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagsList"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTrailRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrailRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveTagsRequest:
    boto3_raw_data: "type_defs.RemoveTagsRequestTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")

    @cached_property
    def TagsList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagsList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RemoveTagsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceTag:
    boto3_raw_data: "type_defs.ResourceTagTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")

    @cached_property
    def TagsList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagsList"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceTagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceTagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdvancedEventSelectorOutput:
    boto3_raw_data: "type_defs.AdvancedEventSelectorOutputTypeDef" = dataclasses.field()

    @cached_property
    def FieldSelectors(self):  # pragma: no cover
        return AdvancedFieldSelectorOutput.make_many(
            self.boto3_raw_data["FieldSelectors"]
        )

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdvancedEventSelectorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdvancedEventSelectorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelQueryResponse:
    boto3_raw_data: "type_defs.CancelQueryResponseTypeDef" = dataclasses.field()

    QueryId = field("QueryId")
    QueryStatus = field("QueryStatus")
    EventDataStoreOwnerAccountId = field("EventDataStoreOwnerAccountId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelQueryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelQueryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrailResponse:
    boto3_raw_data: "type_defs.CreateTrailResponseTypeDef" = dataclasses.field()

    Name = field("Name")
    S3BucketName = field("S3BucketName")
    S3KeyPrefix = field("S3KeyPrefix")
    SnsTopicName = field("SnsTopicName")
    SnsTopicARN = field("SnsTopicARN")
    IncludeGlobalServiceEvents = field("IncludeGlobalServiceEvents")
    IsMultiRegionTrail = field("IsMultiRegionTrail")
    TrailARN = field("TrailARN")
    LogFileValidationEnabled = field("LogFileValidationEnabled")
    CloudWatchLogsLogGroupArn = field("CloudWatchLogsLogGroupArn")
    CloudWatchLogsRoleArn = field("CloudWatchLogsRoleArn")
    KmsKeyId = field("KmsKeyId")
    IsOrganizationTrail = field("IsOrganizationTrail")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTrailResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrailResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableFederationResponse:
    boto3_raw_data: "type_defs.DisableFederationResponseTypeDef" = dataclasses.field()

    EventDataStoreArn = field("EventDataStoreArn")
    FederationStatus = field("FederationStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableFederationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableFederationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableFederationResponse:
    boto3_raw_data: "type_defs.EnableFederationResponseTypeDef" = dataclasses.field()

    EventDataStoreArn = field("EventDataStoreArn")
    FederationStatus = field("FederationStatus")
    FederationRoleArn = field("FederationRoleArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnableFederationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableFederationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateQueryResponse:
    boto3_raw_data: "type_defs.GenerateQueryResponseTypeDef" = dataclasses.field()

    QueryStatement = field("QueryStatement")
    QueryAlias = field("QueryAlias")
    EventDataStoreOwnerAccountId = field("EventDataStoreOwnerAccountId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerateQueryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateQueryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePolicyResponse:
    boto3_raw_data: "type_defs.GetResourcePolicyResponseTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    ResourcePolicy = field("ResourcePolicy")
    DelegatedAdminResourcePolicy = field("DelegatedAdminResourcePolicy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrailStatusResponse:
    boto3_raw_data: "type_defs.GetTrailStatusResponseTypeDef" = dataclasses.field()

    IsLogging = field("IsLogging")
    LatestDeliveryError = field("LatestDeliveryError")
    LatestNotificationError = field("LatestNotificationError")
    LatestDeliveryTime = field("LatestDeliveryTime")
    LatestNotificationTime = field("LatestNotificationTime")
    StartLoggingTime = field("StartLoggingTime")
    StopLoggingTime = field("StopLoggingTime")
    LatestCloudWatchLogsDeliveryError = field("LatestCloudWatchLogsDeliveryError")
    LatestCloudWatchLogsDeliveryTime = field("LatestCloudWatchLogsDeliveryTime")
    LatestDigestDeliveryTime = field("LatestDigestDeliveryTime")
    LatestDigestDeliveryError = field("LatestDigestDeliveryError")
    LatestDeliveryAttemptTime = field("LatestDeliveryAttemptTime")
    LatestNotificationAttemptTime = field("LatestNotificationAttemptTime")
    LatestNotificationAttemptSucceeded = field("LatestNotificationAttemptSucceeded")
    LatestDeliveryAttemptSucceeded = field("LatestDeliveryAttemptSucceeded")
    TimeLoggingStarted = field("TimeLoggingStarted")
    TimeLoggingStopped = field("TimeLoggingStopped")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTrailStatusResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrailStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInsightsMetricDataResponse:
    boto3_raw_data: "type_defs.ListInsightsMetricDataResponseTypeDef" = (
        dataclasses.field()
    )

    EventSource = field("EventSource")
    EventName = field("EventName")
    InsightType = field("InsightType")
    ErrorCode = field("ErrorCode")
    Timestamps = field("Timestamps")
    Values = field("Values")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInsightsMetricDataResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInsightsMetricDataResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourcePolicyResponse:
    boto3_raw_data: "type_defs.PutResourcePolicyResponseTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    ResourcePolicy = field("ResourcePolicy")
    DelegatedAdminResourcePolicy = field("DelegatedAdminResourcePolicy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourcePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourcePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDashboardRefreshResponse:
    boto3_raw_data: "type_defs.StartDashboardRefreshResponseTypeDef" = (
        dataclasses.field()
    )

    RefreshId = field("RefreshId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartDashboardRefreshResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDashboardRefreshResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartQueryResponse:
    boto3_raw_data: "type_defs.StartQueryResponseTypeDef" = dataclasses.field()

    QueryId = field("QueryId")
    EventDataStoreOwnerAccountId = field("EventDataStoreOwnerAccountId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartQueryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartQueryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTrailResponse:
    boto3_raw_data: "type_defs.UpdateTrailResponseTypeDef" = dataclasses.field()

    Name = field("Name")
    S3BucketName = field("S3BucketName")
    S3KeyPrefix = field("S3KeyPrefix")
    SnsTopicName = field("SnsTopicName")
    SnsTopicARN = field("SnsTopicARN")
    IncludeGlobalServiceEvents = field("IncludeGlobalServiceEvents")
    IsMultiRegionTrail = field("IsMultiRegionTrail")
    TrailARN = field("TrailARN")
    LogFileValidationEnabled = field("LogFileValidationEnabled")
    CloudWatchLogsLogGroupArn = field("CloudWatchLogsLogGroupArn")
    CloudWatchLogsRoleArn = field("CloudWatchLogsRoleArn")
    KmsKeyId = field("KmsKeyId")
    IsOrganizationTrail = field("IsOrganizationTrail")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTrailResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTrailResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChannelsResponse:
    boto3_raw_data: "type_defs.ListChannelsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Channels(self):  # pragma: no cover
        return Channel.make_many(self.boto3_raw_data["Channels"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChannelsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChannelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventConfigurationResponse:
    boto3_raw_data: "type_defs.GetEventConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    EventDataStoreArn = field("EventDataStoreArn")
    MaxEventSize = field("MaxEventSize")

    @cached_property
    def ContextKeySelectors(self):  # pragma: no cover
        return ContextKeySelectorOutput.make_many(
            self.boto3_raw_data["ContextKeySelectors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetEventConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEventConfigurationResponse:
    boto3_raw_data: "type_defs.PutEventConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    EventDataStoreArn = field("EventDataStoreArn")
    MaxEventSize = field("MaxEventSize")

    @cached_property
    def ContextKeySelectors(self):  # pragma: no cover
        return ContextKeySelectorOutput.make_many(
            self.boto3_raw_data["ContextKeySelectors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutEventConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEventConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChannelRequest:
    boto3_raw_data: "type_defs.CreateChannelRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Source = field("Source")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return Destination.make_many(self.boto3_raw_data["Destinations"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChannelResponse:
    boto3_raw_data: "type_defs.CreateChannelResponseTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")
    Name = field("Name")
    Source = field("Source")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return Destination.make_many(self.boto3_raw_data["Destinations"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateChannelRequest:
    boto3_raw_data: "type_defs.UpdateChannelRequestTypeDef" = dataclasses.field()

    Channel = field("Channel")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return Destination.make_many(self.boto3_raw_data["Destinations"])

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateChannelResponse:
    boto3_raw_data: "type_defs.UpdateChannelResponseTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")
    Name = field("Name")
    Source = field("Source")

    @cached_property
    def Destinations(self):  # pragma: no cover
        return Destination.make_many(self.boto3_raw_data["Destinations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDashboardsResponse:
    boto3_raw_data: "type_defs.ListDashboardsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Dashboards(self):  # pragma: no cover
        return DashboardDetail.make_many(self.boto3_raw_data["Dashboards"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDashboardsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDashboardsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventSelectorOutput:
    boto3_raw_data: "type_defs.EventSelectorOutputTypeDef" = dataclasses.field()

    ReadWriteType = field("ReadWriteType")
    IncludeManagementEvents = field("IncludeManagementEvents")

    @cached_property
    def DataResources(self):  # pragma: no cover
        return DataResourceOutput.make_many(self.boto3_raw_data["DataResources"])

    ExcludeManagementEventSources = field("ExcludeManagementEventSources")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventSelectorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventSelectorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeQueryResponse:
    boto3_raw_data: "type_defs.DescribeQueryResponseTypeDef" = dataclasses.field()

    QueryId = field("QueryId")
    QueryString = field("QueryString")
    QueryStatus = field("QueryStatus")

    @cached_property
    def QueryStatistics(self):  # pragma: no cover
        return QueryStatisticsForDescribeQuery.make_one(
            self.boto3_raw_data["QueryStatistics"]
        )

    ErrorMessage = field("ErrorMessage")
    DeliveryS3Uri = field("DeliveryS3Uri")
    DeliveryStatus = field("DeliveryStatus")
    Prompt = field("Prompt")
    EventDataStoreOwnerAccountId = field("EventDataStoreOwnerAccountId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeQueryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeQueryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrailsResponse:
    boto3_raw_data: "type_defs.DescribeTrailsResponseTypeDef" = dataclasses.field()

    @cached_property
    def trailList(self):  # pragma: no cover
        return Trail.make_many(self.boto3_raw_data["trailList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTrailsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrailsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrailResponse:
    boto3_raw_data: "type_defs.GetTrailResponseTypeDef" = dataclasses.field()

    @cached_property
    def Trail(self):  # pragma: no cover
        return Trail.make_one(self.boto3_raw_data["Trail"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTrailResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrailResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Event:
    boto3_raw_data: "type_defs.EventTypeDef" = dataclasses.field()

    EventId = field("EventId")
    EventName = field("EventName")
    ReadOnly = field("ReadOnly")
    AccessKeyId = field("AccessKeyId")
    EventTime = field("EventTime")
    EventSource = field("EventSource")
    Username = field("Username")

    @cached_property
    def Resources(self):  # pragma: no cover
        return Resource.make_many(self.boto3_raw_data["Resources"])

    CloudTrailEvent = field("CloudTrailEvent")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInsightSelectorsResponse:
    boto3_raw_data: "type_defs.GetInsightSelectorsResponseTypeDef" = dataclasses.field()

    TrailARN = field("TrailARN")

    @cached_property
    def InsightSelectors(self):  # pragma: no cover
        return InsightSelector.make_many(self.boto3_raw_data["InsightSelectors"])

    EventDataStoreArn = field("EventDataStoreArn")
    InsightsDestination = field("InsightsDestination")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInsightSelectorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInsightSelectorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutInsightSelectorsRequest:
    boto3_raw_data: "type_defs.PutInsightSelectorsRequestTypeDef" = dataclasses.field()

    @cached_property
    def InsightSelectors(self):  # pragma: no cover
        return InsightSelector.make_many(self.boto3_raw_data["InsightSelectors"])

    TrailName = field("TrailName")
    EventDataStore = field("EventDataStore")
    InsightsDestination = field("InsightsDestination")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutInsightSelectorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutInsightSelectorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutInsightSelectorsResponse:
    boto3_raw_data: "type_defs.PutInsightSelectorsResponseTypeDef" = dataclasses.field()

    TrailARN = field("TrailARN")

    @cached_property
    def InsightSelectors(self):  # pragma: no cover
        return InsightSelector.make_many(self.boto3_raw_data["InsightSelectors"])

    EventDataStoreArn = field("EventDataStoreArn")
    InsightsDestination = field("InsightsDestination")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutInsightSelectorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutInsightSelectorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryResultsResponse:
    boto3_raw_data: "type_defs.GetQueryResultsResponseTypeDef" = dataclasses.field()

    QueryStatus = field("QueryStatus")

    @cached_property
    def QueryStatistics(self):  # pragma: no cover
        return QueryStatistics.make_one(self.boto3_raw_data["QueryStatistics"])

    QueryResultRows = field("QueryResultRows")
    ErrorMessage = field("ErrorMessage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQueryResultsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueryResultsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportFailuresResponse:
    boto3_raw_data: "type_defs.ListImportFailuresResponseTypeDef" = dataclasses.field()

    @cached_property
    def Failures(self):  # pragma: no cover
        return ImportFailureListItem.make_many(self.boto3_raw_data["Failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImportFailuresResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportFailuresResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportSource:
    boto3_raw_data: "type_defs.ImportSourceTypeDef" = dataclasses.field()

    @cached_property
    def S3(self):  # pragma: no cover
        return S3ImportSource.make_one(self.boto3_raw_data["S3"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImportSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportsResponse:
    boto3_raw_data: "type_defs.ListImportsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Imports(self):  # pragma: no cover
        return ImportsListItem.make_many(self.boto3_raw_data["Imports"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImportsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportFailuresRequestPaginate:
    boto3_raw_data: "type_defs.ListImportFailuresRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ImportId = field("ImportId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListImportFailuresRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportFailuresRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportsRequestPaginate:
    boto3_raw_data: "type_defs.ListImportsRequestPaginateTypeDef" = dataclasses.field()

    Destination = field("Destination")
    ImportStatus = field("ImportStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImportsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsRequestPaginate:
    boto3_raw_data: "type_defs.ListTagsRequestPaginateTypeDef" = dataclasses.field()

    ResourceIdList = field("ResourceIdList")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrailsRequestPaginate:
    boto3_raw_data: "type_defs.ListTrailsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTrailsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrailsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInsightsMetricDataRequest:
    boto3_raw_data: "type_defs.ListInsightsMetricDataRequestTypeDef" = (
        dataclasses.field()
    )

    EventSource = field("EventSource")
    EventName = field("EventName")
    InsightType = field("InsightType")
    ErrorCode = field("ErrorCode")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    Period = field("Period")
    DataType = field("DataType")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListInsightsMetricDataRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInsightsMetricDataRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPublicKeysRequestPaginate:
    boto3_raw_data: "type_defs.ListPublicKeysRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPublicKeysRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPublicKeysRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPublicKeysRequest:
    boto3_raw_data: "type_defs.ListPublicKeysRequestTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPublicKeysRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPublicKeysRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueriesRequest:
    boto3_raw_data: "type_defs.ListQueriesRequestTypeDef" = dataclasses.field()

    EventDataStore = field("EventDataStore")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    QueryStatus = field("QueryStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListQueriesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPublicKeysResponse:
    boto3_raw_data: "type_defs.ListPublicKeysResponseTypeDef" = dataclasses.field()

    @cached_property
    def PublicKeyList(self):  # pragma: no cover
        return PublicKey.make_many(self.boto3_raw_data["PublicKeyList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPublicKeysResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPublicKeysResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueriesResponse:
    boto3_raw_data: "type_defs.ListQueriesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Queries(self):  # pragma: no cover
        return Query.make_many(self.boto3_raw_data["Queries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListQueriesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueriesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrailsResponse:
    boto3_raw_data: "type_defs.ListTrailsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Trails(self):  # pragma: no cover
        return TrailInfo.make_many(self.boto3_raw_data["Trails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTrailsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrailsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LookupEventsRequestPaginate:
    boto3_raw_data: "type_defs.LookupEventsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def LookupAttributes(self):  # pragma: no cover
        return LookupAttribute.make_many(self.boto3_raw_data["LookupAttributes"])

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    EventCategory = field("EventCategory")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LookupEventsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LookupEventsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LookupEventsRequest:
    boto3_raw_data: "type_defs.LookupEventsRequestTypeDef" = dataclasses.field()

    @cached_property
    def LookupAttributes(self):  # pragma: no cover
        return LookupAttribute.make_many(self.boto3_raw_data["LookupAttributes"])

    StartTime = field("StartTime")
    EndTime = field("EndTime")
    EventCategory = field("EventCategory")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LookupEventsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LookupEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RefreshSchedule:
    boto3_raw_data: "type_defs.RefreshScheduleTypeDef" = dataclasses.field()

    @cached_property
    def Frequency(self):  # pragma: no cover
        return RefreshScheduleFrequency.make_one(self.boto3_raw_data["Frequency"])

    Status = field("Status")
    TimeOfDay = field("TimeOfDay")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RefreshScheduleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RefreshScheduleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchSampleQueriesResponse:
    boto3_raw_data: "type_defs.SearchSampleQueriesResponseTypeDef" = dataclasses.field()

    @cached_property
    def SearchResults(self):  # pragma: no cover
        return SearchSampleQueriesSearchResult.make_many(
            self.boto3_raw_data["SearchResults"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchSampleQueriesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchSampleQueriesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsResponse:
    boto3_raw_data: "type_defs.ListTagsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ResourceTagList(self):  # pragma: no cover
        return ResourceTag.make_many(self.boto3_raw_data["ResourceTagList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTagsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventDataStoreResponse:
    boto3_raw_data: "type_defs.CreateEventDataStoreResponseTypeDef" = (
        dataclasses.field()
    )

    EventDataStoreArn = field("EventDataStoreArn")
    Name = field("Name")
    Status = field("Status")

    @cached_property
    def AdvancedEventSelectors(self):  # pragma: no cover
        return AdvancedEventSelectorOutput.make_many(
            self.boto3_raw_data["AdvancedEventSelectors"]
        )

    MultiRegionEnabled = field("MultiRegionEnabled")
    OrganizationEnabled = field("OrganizationEnabled")
    RetentionPeriod = field("RetentionPeriod")
    TerminationProtectionEnabled = field("TerminationProtectionEnabled")

    @cached_property
    def TagsList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagsList"])

    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")
    KmsKeyId = field("KmsKeyId")
    BillingMode = field("BillingMode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEventDataStoreResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventDataStoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventDataStore:
    boto3_raw_data: "type_defs.EventDataStoreTypeDef" = dataclasses.field()

    EventDataStoreArn = field("EventDataStoreArn")
    Name = field("Name")
    TerminationProtectionEnabled = field("TerminationProtectionEnabled")
    Status = field("Status")

    @cached_property
    def AdvancedEventSelectors(self):  # pragma: no cover
        return AdvancedEventSelectorOutput.make_many(
            self.boto3_raw_data["AdvancedEventSelectors"]
        )

    MultiRegionEnabled = field("MultiRegionEnabled")
    OrganizationEnabled = field("OrganizationEnabled")
    RetentionPeriod = field("RetentionPeriod")
    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventDataStoreTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventDataStoreTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventDataStoreResponse:
    boto3_raw_data: "type_defs.GetEventDataStoreResponseTypeDef" = dataclasses.field()

    EventDataStoreArn = field("EventDataStoreArn")
    Name = field("Name")
    Status = field("Status")

    @cached_property
    def AdvancedEventSelectors(self):  # pragma: no cover
        return AdvancedEventSelectorOutput.make_many(
            self.boto3_raw_data["AdvancedEventSelectors"]
        )

    MultiRegionEnabled = field("MultiRegionEnabled")
    OrganizationEnabled = field("OrganizationEnabled")
    RetentionPeriod = field("RetentionPeriod")
    TerminationProtectionEnabled = field("TerminationProtectionEnabled")
    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")
    KmsKeyId = field("KmsKeyId")
    BillingMode = field("BillingMode")
    FederationStatus = field("FederationStatus")
    FederationRoleArn = field("FederationRoleArn")

    @cached_property
    def PartitionKeys(self):  # pragma: no cover
        return PartitionKey.make_many(self.boto3_raw_data["PartitionKeys"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEventDataStoreResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventDataStoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestoreEventDataStoreResponse:
    boto3_raw_data: "type_defs.RestoreEventDataStoreResponseTypeDef" = (
        dataclasses.field()
    )

    EventDataStoreArn = field("EventDataStoreArn")
    Name = field("Name")
    Status = field("Status")

    @cached_property
    def AdvancedEventSelectors(self):  # pragma: no cover
        return AdvancedEventSelectorOutput.make_many(
            self.boto3_raw_data["AdvancedEventSelectors"]
        )

    MultiRegionEnabled = field("MultiRegionEnabled")
    OrganizationEnabled = field("OrganizationEnabled")
    RetentionPeriod = field("RetentionPeriod")
    TerminationProtectionEnabled = field("TerminationProtectionEnabled")
    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")
    KmsKeyId = field("KmsKeyId")
    BillingMode = field("BillingMode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RestoreEventDataStoreResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestoreEventDataStoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceConfig:
    boto3_raw_data: "type_defs.SourceConfigTypeDef" = dataclasses.field()

    ApplyToAllRegions = field("ApplyToAllRegions")

    @cached_property
    def AdvancedEventSelectors(self):  # pragma: no cover
        return AdvancedEventSelectorOutput.make_many(
            self.boto3_raw_data["AdvancedEventSelectors"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEventDataStoreResponse:
    boto3_raw_data: "type_defs.UpdateEventDataStoreResponseTypeDef" = (
        dataclasses.field()
    )

    EventDataStoreArn = field("EventDataStoreArn")
    Name = field("Name")
    Status = field("Status")

    @cached_property
    def AdvancedEventSelectors(self):  # pragma: no cover
        return AdvancedEventSelectorOutput.make_many(
            self.boto3_raw_data["AdvancedEventSelectors"]
        )

    MultiRegionEnabled = field("MultiRegionEnabled")
    OrganizationEnabled = field("OrganizationEnabled")
    RetentionPeriod = field("RetentionPeriod")
    TerminationProtectionEnabled = field("TerminationProtectionEnabled")
    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")
    KmsKeyId = field("KmsKeyId")
    BillingMode = field("BillingMode")
    FederationStatus = field("FederationStatus")
    FederationRoleArn = field("FederationRoleArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEventDataStoreResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEventDataStoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdvancedEventSelector:
    boto3_raw_data: "type_defs.AdvancedEventSelectorTypeDef" = dataclasses.field()

    FieldSelectors = field("FieldSelectors")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdvancedEventSelectorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdvancedEventSelectorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEventConfigurationRequest:
    boto3_raw_data: "type_defs.PutEventConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    MaxEventSize = field("MaxEventSize")
    ContextKeySelectors = field("ContextKeySelectors")
    EventDataStore = field("EventDataStore")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutEventConfigurationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEventConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventSelectorsResponse:
    boto3_raw_data: "type_defs.GetEventSelectorsResponseTypeDef" = dataclasses.field()

    TrailARN = field("TrailARN")

    @cached_property
    def EventSelectors(self):  # pragma: no cover
        return EventSelectorOutput.make_many(self.boto3_raw_data["EventSelectors"])

    @cached_property
    def AdvancedEventSelectors(self):  # pragma: no cover
        return AdvancedEventSelectorOutput.make_many(
            self.boto3_raw_data["AdvancedEventSelectors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEventSelectorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventSelectorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEventSelectorsResponse:
    boto3_raw_data: "type_defs.PutEventSelectorsResponseTypeDef" = dataclasses.field()

    TrailARN = field("TrailARN")

    @cached_property
    def EventSelectors(self):  # pragma: no cover
        return EventSelectorOutput.make_many(self.boto3_raw_data["EventSelectors"])

    @cached_property
    def AdvancedEventSelectors(self):  # pragma: no cover
        return AdvancedEventSelectorOutput.make_many(
            self.boto3_raw_data["AdvancedEventSelectors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutEventSelectorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEventSelectorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventSelector:
    boto3_raw_data: "type_defs.EventSelectorTypeDef" = dataclasses.field()

    ReadWriteType = field("ReadWriteType")
    IncludeManagementEvents = field("IncludeManagementEvents")
    DataResources = field("DataResources")
    ExcludeManagementEventSources = field("ExcludeManagementEventSources")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventSelectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventSelectorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LookupEventsResponse:
    boto3_raw_data: "type_defs.LookupEventsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Events(self):  # pragma: no cover
        return Event.make_many(self.boto3_raw_data["Events"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LookupEventsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LookupEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetImportResponse:
    boto3_raw_data: "type_defs.GetImportResponseTypeDef" = dataclasses.field()

    ImportId = field("ImportId")
    Destinations = field("Destinations")

    @cached_property
    def ImportSource(self):  # pragma: no cover
        return ImportSource.make_one(self.boto3_raw_data["ImportSource"])

    StartEventTime = field("StartEventTime")
    EndEventTime = field("EndEventTime")
    ImportStatus = field("ImportStatus")
    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")

    @cached_property
    def ImportStatistics(self):  # pragma: no cover
        return ImportStatistics.make_one(self.boto3_raw_data["ImportStatistics"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetImportResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetImportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartImportRequest:
    boto3_raw_data: "type_defs.StartImportRequestTypeDef" = dataclasses.field()

    Destinations = field("Destinations")

    @cached_property
    def ImportSource(self):  # pragma: no cover
        return ImportSource.make_one(self.boto3_raw_data["ImportSource"])

    StartEventTime = field("StartEventTime")
    EndEventTime = field("EndEventTime")
    ImportId = field("ImportId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartImportRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartImportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartImportResponse:
    boto3_raw_data: "type_defs.StartImportResponseTypeDef" = dataclasses.field()

    ImportId = field("ImportId")
    Destinations = field("Destinations")

    @cached_property
    def ImportSource(self):  # pragma: no cover
        return ImportSource.make_one(self.boto3_raw_data["ImportSource"])

    StartEventTime = field("StartEventTime")
    EndEventTime = field("EndEventTime")
    ImportStatus = field("ImportStatus")
    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartImportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartImportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopImportResponse:
    boto3_raw_data: "type_defs.StopImportResponseTypeDef" = dataclasses.field()

    ImportId = field("ImportId")

    @cached_property
    def ImportSource(self):  # pragma: no cover
        return ImportSource.make_one(self.boto3_raw_data["ImportSource"])

    Destinations = field("Destinations")
    ImportStatus = field("ImportStatus")
    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")
    StartEventTime = field("StartEventTime")
    EndEventTime = field("EndEventTime")

    @cached_property
    def ImportStatistics(self):  # pragma: no cover
        return ImportStatistics.make_one(self.boto3_raw_data["ImportStatistics"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopImportResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopImportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDashboardRequest:
    boto3_raw_data: "type_defs.CreateDashboardRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def RefreshSchedule(self):  # pragma: no cover
        return RefreshSchedule.make_one(self.boto3_raw_data["RefreshSchedule"])

    @cached_property
    def TagsList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagsList"])

    TerminationProtectionEnabled = field("TerminationProtectionEnabled")

    @cached_property
    def Widgets(self):  # pragma: no cover
        return RequestWidget.make_many(self.boto3_raw_data["Widgets"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDashboardRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDashboardRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDashboardResponse:
    boto3_raw_data: "type_defs.CreateDashboardResponseTypeDef" = dataclasses.field()

    DashboardArn = field("DashboardArn")
    Name = field("Name")
    Type = field("Type")

    @cached_property
    def Widgets(self):  # pragma: no cover
        return Widget.make_many(self.boto3_raw_data["Widgets"])

    @cached_property
    def TagsList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagsList"])

    @cached_property
    def RefreshSchedule(self):  # pragma: no cover
        return RefreshSchedule.make_one(self.boto3_raw_data["RefreshSchedule"])

    TerminationProtectionEnabled = field("TerminationProtectionEnabled")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDashboardResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDashboardResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDashboardResponse:
    boto3_raw_data: "type_defs.GetDashboardResponseTypeDef" = dataclasses.field()

    DashboardArn = field("DashboardArn")
    Type = field("Type")
    Status = field("Status")

    @cached_property
    def Widgets(self):  # pragma: no cover
        return Widget.make_many(self.boto3_raw_data["Widgets"])

    @cached_property
    def RefreshSchedule(self):  # pragma: no cover
        return RefreshSchedule.make_one(self.boto3_raw_data["RefreshSchedule"])

    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")
    LastRefreshId = field("LastRefreshId")
    LastRefreshFailureReason = field("LastRefreshFailureReason")
    TerminationProtectionEnabled = field("TerminationProtectionEnabled")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDashboardResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDashboardResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDashboardRequest:
    boto3_raw_data: "type_defs.UpdateDashboardRequestTypeDef" = dataclasses.field()

    DashboardId = field("DashboardId")

    @cached_property
    def Widgets(self):  # pragma: no cover
        return RequestWidget.make_many(self.boto3_raw_data["Widgets"])

    @cached_property
    def RefreshSchedule(self):  # pragma: no cover
        return RefreshSchedule.make_one(self.boto3_raw_data["RefreshSchedule"])

    TerminationProtectionEnabled = field("TerminationProtectionEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDashboardRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDashboardRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDashboardResponse:
    boto3_raw_data: "type_defs.UpdateDashboardResponseTypeDef" = dataclasses.field()

    DashboardArn = field("DashboardArn")
    Name = field("Name")
    Type = field("Type")

    @cached_property
    def Widgets(self):  # pragma: no cover
        return Widget.make_many(self.boto3_raw_data["Widgets"])

    @cached_property
    def RefreshSchedule(self):  # pragma: no cover
        return RefreshSchedule.make_one(self.boto3_raw_data["RefreshSchedule"])

    TerminationProtectionEnabled = field("TerminationProtectionEnabled")
    CreatedTimestamp = field("CreatedTimestamp")
    UpdatedTimestamp = field("UpdatedTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDashboardResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDashboardResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventDataStoresResponse:
    boto3_raw_data: "type_defs.ListEventDataStoresResponseTypeDef" = dataclasses.field()

    @cached_property
    def EventDataStores(self):  # pragma: no cover
        return EventDataStore.make_many(self.boto3_raw_data["EventDataStores"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEventDataStoresResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventDataStoresResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChannelResponse:
    boto3_raw_data: "type_defs.GetChannelResponseTypeDef" = dataclasses.field()

    ChannelArn = field("ChannelArn")
    Name = field("Name")
    Source = field("Source")

    @cached_property
    def SourceConfig(self):  # pragma: no cover
        return SourceConfig.make_one(self.boto3_raw_data["SourceConfig"])

    @cached_property
    def Destinations(self):  # pragma: no cover
        return Destination.make_many(self.boto3_raw_data["Destinations"])

    @cached_property
    def IngestionStatus(self):  # pragma: no cover
        return IngestionStatus.make_one(self.boto3_raw_data["IngestionStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetChannelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChannelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventDataStoreRequest:
    boto3_raw_data: "type_defs.CreateEventDataStoreRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    AdvancedEventSelectors = field("AdvancedEventSelectors")
    MultiRegionEnabled = field("MultiRegionEnabled")
    OrganizationEnabled = field("OrganizationEnabled")
    RetentionPeriod = field("RetentionPeriod")
    TerminationProtectionEnabled = field("TerminationProtectionEnabled")

    @cached_property
    def TagsList(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagsList"])

    KmsKeyId = field("KmsKeyId")
    StartIngestion = field("StartIngestion")
    BillingMode = field("BillingMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEventDataStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventDataStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEventDataStoreRequest:
    boto3_raw_data: "type_defs.UpdateEventDataStoreRequestTypeDef" = dataclasses.field()

    EventDataStore = field("EventDataStore")
    Name = field("Name")
    AdvancedEventSelectors = field("AdvancedEventSelectors")
    MultiRegionEnabled = field("MultiRegionEnabled")
    OrganizationEnabled = field("OrganizationEnabled")
    RetentionPeriod = field("RetentionPeriod")
    TerminationProtectionEnabled = field("TerminationProtectionEnabled")
    KmsKeyId = field("KmsKeyId")
    BillingMode = field("BillingMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEventDataStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEventDataStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEventSelectorsRequest:
    boto3_raw_data: "type_defs.PutEventSelectorsRequestTypeDef" = dataclasses.field()

    TrailName = field("TrailName")
    EventSelectors = field("EventSelectors")
    AdvancedEventSelectors = field("AdvancedEventSelectors")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutEventSelectorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEventSelectorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
