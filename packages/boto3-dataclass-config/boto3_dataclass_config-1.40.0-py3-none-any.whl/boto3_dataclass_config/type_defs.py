# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_config import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccountAggregationSourceOutput:
    boto3_raw_data: "type_defs.AccountAggregationSourceOutputTypeDef" = (
        dataclasses.field()
    )

    AccountIds = field("AccountIds")
    AllAwsRegions = field("AllAwsRegions")
    AwsRegions = field("AwsRegions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AccountAggregationSourceOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountAggregationSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountAggregationSource:
    boto3_raw_data: "type_defs.AccountAggregationSourceTypeDef" = dataclasses.field()

    AccountIds = field("AccountIds")
    AllAwsRegions = field("AllAwsRegions")
    AwsRegions = field("AwsRegions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccountAggregationSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountAggregationSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregateConformancePackCompliance:
    boto3_raw_data: "type_defs.AggregateConformancePackComplianceTypeDef" = (
        dataclasses.field()
    )

    ComplianceType = field("ComplianceType")
    CompliantRuleCount = field("CompliantRuleCount")
    NonCompliantRuleCount = field("NonCompliantRuleCount")
    TotalRuleCount = field("TotalRuleCount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AggregateConformancePackComplianceTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregateConformancePackComplianceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregateConformancePackComplianceCount:
    boto3_raw_data: "type_defs.AggregateConformancePackComplianceCountTypeDef" = (
        dataclasses.field()
    )

    CompliantConformancePackCount = field("CompliantConformancePackCount")
    NonCompliantConformancePackCount = field("NonCompliantConformancePackCount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AggregateConformancePackComplianceCountTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregateConformancePackComplianceCountTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregateConformancePackComplianceFilters:
    boto3_raw_data: "type_defs.AggregateConformancePackComplianceFiltersTypeDef" = (
        dataclasses.field()
    )

    ConformancePackName = field("ConformancePackName")
    ComplianceType = field("ComplianceType")
    AccountId = field("AccountId")
    AwsRegion = field("AwsRegion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AggregateConformancePackComplianceFiltersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregateConformancePackComplianceFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregateConformancePackComplianceSummaryFilters:
    boto3_raw_data: (
        "type_defs.AggregateConformancePackComplianceSummaryFiltersTypeDef"
    ) = dataclasses.field()

    AccountId = field("AccountId")
    AwsRegion = field("AwsRegion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AggregateConformancePackComplianceSummaryFiltersTypeDef"
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
                "type_defs.AggregateConformancePackComplianceSummaryFiltersTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregateResourceIdentifier:
    boto3_raw_data: "type_defs.AggregateResourceIdentifierTypeDef" = dataclasses.field()

    SourceAccountId = field("SourceAccountId")
    SourceRegion = field("SourceRegion")
    ResourceId = field("ResourceId")
    ResourceType = field("ResourceType")
    ResourceName = field("ResourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AggregateResourceIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregateResourceIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregatedSourceStatus:
    boto3_raw_data: "type_defs.AggregatedSourceStatusTypeDef" = dataclasses.field()

    SourceId = field("SourceId")
    SourceType = field("SourceType")
    AwsRegion = field("AwsRegion")
    LastUpdateStatus = field("LastUpdateStatus")
    LastUpdateTime = field("LastUpdateTime")
    LastErrorCode = field("LastErrorCode")
    LastErrorMessage = field("LastErrorMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AggregatedSourceStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregatedSourceStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregationAuthorization:
    boto3_raw_data: "type_defs.AggregationAuthorizationTypeDef" = dataclasses.field()

    AggregationAuthorizationArn = field("AggregationAuthorizationArn")
    AuthorizedAccountId = field("AuthorizedAccountId")
    AuthorizedAwsRegion = field("AuthorizedAwsRegion")
    CreationTime = field("CreationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AggregationAuthorizationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregationAuthorizationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregatorFilterResourceTypeOutput:
    boto3_raw_data: "type_defs.AggregatorFilterResourceTypeOutputTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")
    Value = field("Value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AggregatorFilterResourceTypeOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregatorFilterResourceTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregatorFilterResourceType:
    boto3_raw_data: "type_defs.AggregatorFilterResourceTypeTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AggregatorFilterResourceTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregatorFilterResourceTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregatorFilterServicePrincipalOutput:
    boto3_raw_data: "type_defs.AggregatorFilterServicePrincipalOutputTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")
    Value = field("Value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AggregatorFilterServicePrincipalOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregatorFilterServicePrincipalOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregatorFilterServicePrincipal:
    boto3_raw_data: "type_defs.AggregatorFilterServicePrincipalTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")
    Value = field("Value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AggregatorFilterServicePrincipalTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregatorFilterServicePrincipalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateResourceTypesRequest:
    boto3_raw_data: "type_defs.AssociateResourceTypesRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationRecorderArn = field("ConfigurationRecorderArn")
    ResourceTypes = field("ResourceTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateResourceTypesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateResourceTypesRequestTypeDef"]
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
class BaseConfigurationItem:
    boto3_raw_data: "type_defs.BaseConfigurationItemTypeDef" = dataclasses.field()

    version = field("version")
    accountId = field("accountId")
    configurationItemCaptureTime = field("configurationItemCaptureTime")
    configurationItemStatus = field("configurationItemStatus")
    configurationStateId = field("configurationStateId")
    arn = field("arn")
    resourceType = field("resourceType")
    resourceId = field("resourceId")
    resourceName = field("resourceName")
    awsRegion = field("awsRegion")
    availabilityZone = field("availabilityZone")
    resourceCreationTime = field("resourceCreationTime")
    configuration = field("configuration")
    supplementaryConfiguration = field("supplementaryConfiguration")
    recordingFrequency = field("recordingFrequency")
    configurationItemDeliveryTime = field("configurationItemDeliveryTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BaseConfigurationItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BaseConfigurationItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceKey:
    boto3_raw_data: "type_defs.ResourceKeyTypeDef" = dataclasses.field()

    resourceType = field("resourceType")
    resourceId = field("resourceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceKeyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComplianceContributorCount:
    boto3_raw_data: "type_defs.ComplianceContributorCountTypeDef" = dataclasses.field()

    CappedCount = field("CappedCount")
    CapExceeded = field("CapExceeded")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComplianceContributorCountTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComplianceContributorCountTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigExportDeliveryInfo:
    boto3_raw_data: "type_defs.ConfigExportDeliveryInfoTypeDef" = dataclasses.field()

    lastStatus = field("lastStatus")
    lastErrorCode = field("lastErrorCode")
    lastErrorMessage = field("lastErrorMessage")
    lastAttemptTime = field("lastAttemptTime")
    lastSuccessfulTime = field("lastSuccessfulTime")
    nextDeliveryTime = field("nextDeliveryTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigExportDeliveryInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigExportDeliveryInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigRuleComplianceFilters:
    boto3_raw_data: "type_defs.ConfigRuleComplianceFiltersTypeDef" = dataclasses.field()

    ConfigRuleName = field("ConfigRuleName")
    ComplianceType = field("ComplianceType")
    AccountId = field("AccountId")
    AwsRegion = field("AwsRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigRuleComplianceFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigRuleComplianceFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigRuleComplianceSummaryFilters:
    boto3_raw_data: "type_defs.ConfigRuleComplianceSummaryFiltersTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    AwsRegion = field("AwsRegion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfigRuleComplianceSummaryFiltersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigRuleComplianceSummaryFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigRuleEvaluationStatus:
    boto3_raw_data: "type_defs.ConfigRuleEvaluationStatusTypeDef" = dataclasses.field()

    ConfigRuleName = field("ConfigRuleName")
    ConfigRuleArn = field("ConfigRuleArn")
    ConfigRuleId = field("ConfigRuleId")
    LastSuccessfulInvocationTime = field("LastSuccessfulInvocationTime")
    LastFailedInvocationTime = field("LastFailedInvocationTime")
    LastSuccessfulEvaluationTime = field("LastSuccessfulEvaluationTime")
    LastFailedEvaluationTime = field("LastFailedEvaluationTime")
    FirstActivatedTime = field("FirstActivatedTime")
    LastDeactivatedTime = field("LastDeactivatedTime")
    LastErrorCode = field("LastErrorCode")
    LastErrorMessage = field("LastErrorMessage")
    FirstEvaluationStarted = field("FirstEvaluationStarted")
    LastDebugLogDeliveryStatus = field("LastDebugLogDeliveryStatus")
    LastDebugLogDeliveryStatusReason = field("LastDebugLogDeliveryStatusReason")
    LastDebugLogDeliveryTime = field("LastDebugLogDeliveryTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigRuleEvaluationStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigRuleEvaluationStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationModeConfiguration:
    boto3_raw_data: "type_defs.EvaluationModeConfigurationTypeDef" = dataclasses.field()

    Mode = field("Mode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationModeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationModeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScopeOutput:
    boto3_raw_data: "type_defs.ScopeOutputTypeDef" = dataclasses.field()

    ComplianceResourceTypes = field("ComplianceResourceTypes")
    TagKey = field("TagKey")
    TagValue = field("TagValue")
    ComplianceResourceId = field("ComplianceResourceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScopeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScopeOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Scope:
    boto3_raw_data: "type_defs.ScopeTypeDef" = dataclasses.field()

    ComplianceResourceTypes = field("ComplianceResourceTypes")
    TagKey = field("TagKey")
    TagValue = field("TagValue")
    ComplianceResourceId = field("ComplianceResourceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScopeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScopeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigSnapshotDeliveryProperties:
    boto3_raw_data: "type_defs.ConfigSnapshotDeliveryPropertiesTypeDef" = (
        dataclasses.field()
    )

    deliveryFrequency = field("deliveryFrequency")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConfigSnapshotDeliveryPropertiesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigSnapshotDeliveryPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigStreamDeliveryInfo:
    boto3_raw_data: "type_defs.ConfigStreamDeliveryInfoTypeDef" = dataclasses.field()

    lastStatus = field("lastStatus")
    lastErrorCode = field("lastErrorCode")
    lastErrorMessage = field("lastErrorMessage")
    lastStatusChangeTime = field("lastStatusChangeTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigStreamDeliveryInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigStreamDeliveryInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationAggregationSourceOutput:
    boto3_raw_data: "type_defs.OrganizationAggregationSourceOutputTypeDef" = (
        dataclasses.field()
    )

    RoleArn = field("RoleArn")
    AwsRegions = field("AwsRegions")
    AllAwsRegions = field("AllAwsRegions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationAggregationSourceOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationAggregationSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Relationship:
    boto3_raw_data: "type_defs.RelationshipTypeDef" = dataclasses.field()

    resourceType = field("resourceType")
    resourceId = field("resourceId")
    resourceName = field("resourceName")
    relationshipName = field("relationshipName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RelationshipTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RelationshipTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationRecorderFilter:
    boto3_raw_data: "type_defs.ConfigurationRecorderFilterTypeDef" = dataclasses.field()

    filterName = field("filterName")
    filterValue = field("filterValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationRecorderFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationRecorderFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationRecorderStatus:
    boto3_raw_data: "type_defs.ConfigurationRecorderStatusTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    lastStartTime = field("lastStartTime")
    lastStopTime = field("lastStopTime")
    recording = field("recording")
    lastStatus = field("lastStatus")
    lastErrorCode = field("lastErrorCode")
    lastErrorMessage = field("lastErrorMessage")
    lastStatusChangeTime = field("lastStatusChangeTime")
    servicePrincipal = field("servicePrincipal")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationRecorderStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationRecorderStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationRecorderSummary:
    boto3_raw_data: "type_defs.ConfigurationRecorderSummaryTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    name = field("name")
    recordingScope = field("recordingScope")
    servicePrincipal = field("servicePrincipal")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationRecorderSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationRecorderSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConformancePackComplianceFilters:
    boto3_raw_data: "type_defs.ConformancePackComplianceFiltersTypeDef" = (
        dataclasses.field()
    )

    ConfigRuleNames = field("ConfigRuleNames")
    ComplianceType = field("ComplianceType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConformancePackComplianceFiltersTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConformancePackComplianceFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConformancePackComplianceScore:
    boto3_raw_data: "type_defs.ConformancePackComplianceScoreTypeDef" = (
        dataclasses.field()
    )

    Score = field("Score")
    ConformancePackName = field("ConformancePackName")
    LastUpdatedTime = field("LastUpdatedTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConformancePackComplianceScoreTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConformancePackComplianceScoreTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConformancePackComplianceScoresFilters:
    boto3_raw_data: "type_defs.ConformancePackComplianceScoresFiltersTypeDef" = (
        dataclasses.field()
    )

    ConformancePackNames = field("ConformancePackNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConformancePackComplianceScoresFiltersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConformancePackComplianceScoresFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConformancePackComplianceSummary:
    boto3_raw_data: "type_defs.ConformancePackComplianceSummaryTypeDef" = (
        dataclasses.field()
    )

    ConformancePackName = field("ConformancePackName")
    ConformancePackComplianceStatus = field("ConformancePackComplianceStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConformancePackComplianceSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConformancePackComplianceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConformancePackInputParameter:
    boto3_raw_data: "type_defs.ConformancePackInputParameterTypeDef" = (
        dataclasses.field()
    )

    ParameterName = field("ParameterName")
    ParameterValue = field("ParameterValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConformancePackInputParameterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConformancePackInputParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateSSMDocumentDetails:
    boto3_raw_data: "type_defs.TemplateSSMDocumentDetailsTypeDef" = dataclasses.field()

    DocumentName = field("DocumentName")
    DocumentVersion = field("DocumentVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TemplateSSMDocumentDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateSSMDocumentDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConformancePackEvaluationFilters:
    boto3_raw_data: "type_defs.ConformancePackEvaluationFiltersTypeDef" = (
        dataclasses.field()
    )

    ConfigRuleNames = field("ConfigRuleNames")
    ComplianceType = field("ComplianceType")
    ResourceType = field("ResourceType")
    ResourceIds = field("ResourceIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConformancePackEvaluationFiltersTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConformancePackEvaluationFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConformancePackRuleCompliance:
    boto3_raw_data: "type_defs.ConformancePackRuleComplianceTypeDef" = (
        dataclasses.field()
    )

    ConfigRuleName = field("ConfigRuleName")
    ComplianceType = field("ComplianceType")
    Controls = field("Controls")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConformancePackRuleComplianceTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConformancePackRuleComplianceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConformancePackStatusDetail:
    boto3_raw_data: "type_defs.ConformancePackStatusDetailTypeDef" = dataclasses.field()

    ConformancePackName = field("ConformancePackName")
    ConformancePackId = field("ConformancePackId")
    ConformancePackArn = field("ConformancePackArn")
    ConformancePackState = field("ConformancePackState")
    StackArn = field("StackArn")
    LastUpdateRequestedTime = field("LastUpdateRequestedTime")
    ConformancePackStatusReason = field("ConformancePackStatusReason")
    LastUpdateCompletedTime = field("LastUpdateCompletedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConformancePackStatusDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConformancePackStatusDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomPolicyDetails:
    boto3_raw_data: "type_defs.CustomPolicyDetailsTypeDef" = dataclasses.field()

    PolicyRuntime = field("PolicyRuntime")
    PolicyText = field("PolicyText")
    EnableDebugLogDelivery = field("EnableDebugLogDelivery")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomPolicyDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomPolicyDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAggregationAuthorizationRequest:
    boto3_raw_data: "type_defs.DeleteAggregationAuthorizationRequestTypeDef" = (
        dataclasses.field()
    )

    AuthorizedAccountId = field("AuthorizedAccountId")
    AuthorizedAwsRegion = field("AuthorizedAwsRegion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAggregationAuthorizationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAggregationAuthorizationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConfigRuleRequest:
    boto3_raw_data: "type_defs.DeleteConfigRuleRequestTypeDef" = dataclasses.field()

    ConfigRuleName = field("ConfigRuleName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConfigRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConfigRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConfigurationAggregatorRequest:
    boto3_raw_data: "type_defs.DeleteConfigurationAggregatorRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationAggregatorName = field("ConfigurationAggregatorName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteConfigurationAggregatorRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConfigurationAggregatorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConfigurationRecorderRequest:
    boto3_raw_data: "type_defs.DeleteConfigurationRecorderRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationRecorderName = field("ConfigurationRecorderName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteConfigurationRecorderRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConfigurationRecorderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConformancePackRequest:
    boto3_raw_data: "type_defs.DeleteConformancePackRequestTypeDef" = (
        dataclasses.field()
    )

    ConformancePackName = field("ConformancePackName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConformancePackRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConformancePackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDeliveryChannelRequest:
    boto3_raw_data: "type_defs.DeleteDeliveryChannelRequestTypeDef" = (
        dataclasses.field()
    )

    DeliveryChannelName = field("DeliveryChannelName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDeliveryChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDeliveryChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEvaluationResultsRequest:
    boto3_raw_data: "type_defs.DeleteEvaluationResultsRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigRuleName = field("ConfigRuleName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteEvaluationResultsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEvaluationResultsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOrganizationConfigRuleRequest:
    boto3_raw_data: "type_defs.DeleteOrganizationConfigRuleRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationConfigRuleName = field("OrganizationConfigRuleName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteOrganizationConfigRuleRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOrganizationConfigRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteOrganizationConformancePackRequest:
    boto3_raw_data: "type_defs.DeleteOrganizationConformancePackRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationConformancePackName = field("OrganizationConformancePackName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteOrganizationConformancePackRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteOrganizationConformancePackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePendingAggregationRequestRequest:
    boto3_raw_data: "type_defs.DeletePendingAggregationRequestRequestTypeDef" = (
        dataclasses.field()
    )

    RequesterAccountId = field("RequesterAccountId")
    RequesterAwsRegion = field("RequesterAwsRegion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeletePendingAggregationRequestRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePendingAggregationRequestRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRemediationConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteRemediationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigRuleName = field("ConfigRuleName")
    ResourceType = field("ResourceType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteRemediationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRemediationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemediationExceptionResourceKey:
    boto3_raw_data: "type_defs.RemediationExceptionResourceKeyTypeDef" = (
        dataclasses.field()
    )

    ResourceType = field("ResourceType")
    ResourceId = field("ResourceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemediationExceptionResourceKeyTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemediationExceptionResourceKeyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourceConfigRequest:
    boto3_raw_data: "type_defs.DeleteResourceConfigRequestTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    ResourceId = field("ResourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResourceConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourceConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRetentionConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteRetentionConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    RetentionConfigurationName = field("RetentionConfigurationName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteRetentionConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRetentionConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceLinkedConfigurationRecorderRequest:
    boto3_raw_data: (
        "type_defs.DeleteServiceLinkedConfigurationRecorderRequestTypeDef"
    ) = dataclasses.field()

    ServicePrincipal = field("ServicePrincipal")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteServiceLinkedConfigurationRecorderRequestTypeDef"
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
                "type_defs.DeleteServiceLinkedConfigurationRecorderRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStoredQueryRequest:
    boto3_raw_data: "type_defs.DeleteStoredQueryRequestTypeDef" = dataclasses.field()

    QueryName = field("QueryName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteStoredQueryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStoredQueryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeliverConfigSnapshotRequest:
    boto3_raw_data: "type_defs.DeliverConfigSnapshotRequestTypeDef" = (
        dataclasses.field()
    )

    deliveryChannelName = field("deliveryChannelName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeliverConfigSnapshotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeliverConfigSnapshotRequestTypeDef"]
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
class DescribeAggregationAuthorizationsRequest:
    boto3_raw_data: "type_defs.DescribeAggregationAuthorizationsRequestTypeDef" = (
        dataclasses.field()
    )

    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAggregationAuthorizationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAggregationAuthorizationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeComplianceByConfigRuleRequest:
    boto3_raw_data: "type_defs.DescribeComplianceByConfigRuleRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigRuleNames = field("ConfigRuleNames")
    ComplianceTypes = field("ComplianceTypes")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeComplianceByConfigRuleRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeComplianceByConfigRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeComplianceByResourceRequest:
    boto3_raw_data: "type_defs.DescribeComplianceByResourceRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceType = field("ResourceType")
    ResourceId = field("ResourceId")
    ComplianceTypes = field("ComplianceTypes")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeComplianceByResourceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeComplianceByResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigRuleEvaluationStatusRequest:
    boto3_raw_data: "type_defs.DescribeConfigRuleEvaluationStatusRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigRuleNames = field("ConfigRuleNames")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConfigRuleEvaluationStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigRuleEvaluationStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigRulesFilters:
    boto3_raw_data: "type_defs.DescribeConfigRulesFiltersTypeDef" = dataclasses.field()

    EvaluationMode = field("EvaluationMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeConfigRulesFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigRulesFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigurationAggregatorSourcesStatusRequest:
    boto3_raw_data: (
        "type_defs.DescribeConfigurationAggregatorSourcesStatusRequestTypeDef"
    ) = dataclasses.field()

    ConfigurationAggregatorName = field("ConfigurationAggregatorName")
    UpdateStatus = field("UpdateStatus")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConfigurationAggregatorSourcesStatusRequestTypeDef"
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
                "type_defs.DescribeConfigurationAggregatorSourcesStatusRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigurationAggregatorsRequest:
    boto3_raw_data: "type_defs.DescribeConfigurationAggregatorsRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationAggregatorNames = field("ConfigurationAggregatorNames")
    NextToken = field("NextToken")
    Limit = field("Limit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConfigurationAggregatorsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigurationAggregatorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigurationRecorderStatusRequest:
    boto3_raw_data: "type_defs.DescribeConfigurationRecorderStatusRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationRecorderNames = field("ConfigurationRecorderNames")
    ServicePrincipal = field("ServicePrincipal")
    Arn = field("Arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConfigurationRecorderStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigurationRecorderStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigurationRecordersRequest:
    boto3_raw_data: "type_defs.DescribeConfigurationRecordersRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationRecorderNames = field("ConfigurationRecorderNames")
    ServicePrincipal = field("ServicePrincipal")
    Arn = field("Arn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConfigurationRecordersRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigurationRecordersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConformancePackStatusRequest:
    boto3_raw_data: "type_defs.DescribeConformancePackStatusRequestTypeDef" = (
        dataclasses.field()
    )

    ConformancePackNames = field("ConformancePackNames")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConformancePackStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConformancePackStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConformancePacksRequest:
    boto3_raw_data: "type_defs.DescribeConformancePacksRequestTypeDef" = (
        dataclasses.field()
    )

    ConformancePackNames = field("ConformancePackNames")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeConformancePacksRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConformancePacksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDeliveryChannelStatusRequest:
    boto3_raw_data: "type_defs.DescribeDeliveryChannelStatusRequestTypeDef" = (
        dataclasses.field()
    )

    DeliveryChannelNames = field("DeliveryChannelNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDeliveryChannelStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDeliveryChannelStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDeliveryChannelsRequest:
    boto3_raw_data: "type_defs.DescribeDeliveryChannelsRequestTypeDef" = (
        dataclasses.field()
    )

    DeliveryChannelNames = field("DeliveryChannelNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDeliveryChannelsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDeliveryChannelsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationConfigRuleStatusesRequest:
    boto3_raw_data: "type_defs.DescribeOrganizationConfigRuleStatusesRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationConfigRuleNames = field("OrganizationConfigRuleNames")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrganizationConfigRuleStatusesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOrganizationConfigRuleStatusesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationConfigRuleStatus:
    boto3_raw_data: "type_defs.OrganizationConfigRuleStatusTypeDef" = (
        dataclasses.field()
    )

    OrganizationConfigRuleName = field("OrganizationConfigRuleName")
    OrganizationRuleStatus = field("OrganizationRuleStatus")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")
    LastUpdateTime = field("LastUpdateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrganizationConfigRuleStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationConfigRuleStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationConfigRulesRequest:
    boto3_raw_data: "type_defs.DescribeOrganizationConfigRulesRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationConfigRuleNames = field("OrganizationConfigRuleNames")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrganizationConfigRulesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOrganizationConfigRulesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationConformancePackStatusesRequest:
    boto3_raw_data: (
        "type_defs.DescribeOrganizationConformancePackStatusesRequestTypeDef"
    ) = dataclasses.field()

    OrganizationConformancePackNames = field("OrganizationConformancePackNames")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrganizationConformancePackStatusesRequestTypeDef"
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
                "type_defs.DescribeOrganizationConformancePackStatusesRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationConformancePackStatus:
    boto3_raw_data: "type_defs.OrganizationConformancePackStatusTypeDef" = (
        dataclasses.field()
    )

    OrganizationConformancePackName = field("OrganizationConformancePackName")
    Status = field("Status")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")
    LastUpdateTime = field("LastUpdateTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationConformancePackStatusTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationConformancePackStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationConformancePacksRequest:
    boto3_raw_data: "type_defs.DescribeOrganizationConformancePacksRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationConformancePackNames = field("OrganizationConformancePackNames")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrganizationConformancePacksRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOrganizationConformancePacksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePendingAggregationRequestsRequest:
    boto3_raw_data: "type_defs.DescribePendingAggregationRequestsRequestTypeDef" = (
        dataclasses.field()
    )

    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePendingAggregationRequestsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePendingAggregationRequestsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PendingAggregationRequest:
    boto3_raw_data: "type_defs.PendingAggregationRequestTypeDef" = dataclasses.field()

    RequesterAccountId = field("RequesterAccountId")
    RequesterAwsRegion = field("RequesterAwsRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PendingAggregationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PendingAggregationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRemediationConfigurationsRequest:
    boto3_raw_data: "type_defs.DescribeRemediationConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigRuleNames = field("ConfigRuleNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRemediationConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRemediationConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemediationException:
    boto3_raw_data: "type_defs.RemediationExceptionTypeDef" = dataclasses.field()

    ConfigRuleName = field("ConfigRuleName")
    ResourceType = field("ResourceType")
    ResourceId = field("ResourceId")
    Message = field("Message")
    ExpirationTime = field("ExpirationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemediationExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemediationExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRetentionConfigurationsRequest:
    boto3_raw_data: "type_defs.DescribeRetentionConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    RetentionConfigurationNames = field("RetentionConfigurationNames")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRetentionConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRetentionConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetentionConfiguration:
    boto3_raw_data: "type_defs.RetentionConfigurationTypeDef" = dataclasses.field()

    Name = field("Name")
    RetentionPeriodInDays = field("RetentionPeriodInDays")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetentionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetentionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateResourceTypesRequest:
    boto3_raw_data: "type_defs.DisassociateResourceTypesRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationRecorderArn = field("ConfigurationRecorderArn")
    ResourceTypes = field("ResourceTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateResourceTypesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateResourceTypesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationContext:
    boto3_raw_data: "type_defs.EvaluationContextTypeDef" = dataclasses.field()

    EvaluationContextIdentifier = field("EvaluationContextIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvaluationContextTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationContextTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationOutput:
    boto3_raw_data: "type_defs.EvaluationOutputTypeDef" = dataclasses.field()

    ComplianceResourceType = field("ComplianceResourceType")
    ComplianceResourceId = field("ComplianceResourceId")
    ComplianceType = field("ComplianceType")
    OrderingTimestamp = field("OrderingTimestamp")
    Annotation = field("Annotation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvaluationOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationResultQualifier:
    boto3_raw_data: "type_defs.EvaluationResultQualifierTypeDef" = dataclasses.field()

    ConfigRuleName = field("ConfigRuleName")
    ResourceType = field("ResourceType")
    ResourceId = field("ResourceId")
    EvaluationMode = field("EvaluationMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationResultQualifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationResultQualifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationStatus:
    boto3_raw_data: "type_defs.EvaluationStatusTypeDef" = dataclasses.field()

    Status = field("Status")
    FailureReason = field("FailureReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvaluationStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExclusionByResourceTypesOutput:
    boto3_raw_data: "type_defs.ExclusionByResourceTypesOutputTypeDef" = (
        dataclasses.field()
    )

    resourceTypes = field("resourceTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExclusionByResourceTypesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExclusionByResourceTypesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExclusionByResourceTypes:
    boto3_raw_data: "type_defs.ExclusionByResourceTypesTypeDef" = dataclasses.field()

    resourceTypes = field("resourceTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExclusionByResourceTypesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExclusionByResourceTypesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SsmControls:
    boto3_raw_data: "type_defs.SsmControlsTypeDef" = dataclasses.field()

    ConcurrentExecutionRatePercentage = field("ConcurrentExecutionRatePercentage")
    ErrorPercentage = field("ErrorPercentage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SsmControlsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SsmControlsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldInfo:
    boto3_raw_data: "type_defs.FieldInfoTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FieldInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAggregateComplianceDetailsByConfigRuleRequest:
    boto3_raw_data: (
        "type_defs.GetAggregateComplianceDetailsByConfigRuleRequestTypeDef"
    ) = dataclasses.field()

    ConfigurationAggregatorName = field("ConfigurationAggregatorName")
    ConfigRuleName = field("ConfigRuleName")
    AccountId = field("AccountId")
    AwsRegion = field("AwsRegion")
    ComplianceType = field("ComplianceType")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAggregateComplianceDetailsByConfigRuleRequestTypeDef"
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
                "type_defs.GetAggregateComplianceDetailsByConfigRuleRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceCountFilters:
    boto3_raw_data: "type_defs.ResourceCountFiltersTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    AccountId = field("AccountId")
    Region = field("Region")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceCountFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceCountFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupedResourceCount:
    boto3_raw_data: "type_defs.GroupedResourceCountTypeDef" = dataclasses.field()

    GroupName = field("GroupName")
    ResourceCount = field("ResourceCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GroupedResourceCountTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GroupedResourceCountTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComplianceDetailsByConfigRuleRequest:
    boto3_raw_data: "type_defs.GetComplianceDetailsByConfigRuleRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigRuleName = field("ConfigRuleName")
    ComplianceTypes = field("ComplianceTypes")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetComplianceDetailsByConfigRuleRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComplianceDetailsByConfigRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComplianceDetailsByResourceRequest:
    boto3_raw_data: "type_defs.GetComplianceDetailsByResourceRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceType = field("ResourceType")
    ResourceId = field("ResourceId")
    ComplianceTypes = field("ComplianceTypes")
    NextToken = field("NextToken")
    ResourceEvaluationId = field("ResourceEvaluationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetComplianceDetailsByResourceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComplianceDetailsByResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComplianceSummaryByResourceTypeRequest:
    boto3_raw_data: "type_defs.GetComplianceSummaryByResourceTypeRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceTypes = field("ResourceTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetComplianceSummaryByResourceTypeRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComplianceSummaryByResourceTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConformancePackComplianceSummaryRequest:
    boto3_raw_data: "type_defs.GetConformancePackComplianceSummaryRequestTypeDef" = (
        dataclasses.field()
    )

    ConformancePackNames = field("ConformancePackNames")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConformancePackComplianceSummaryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConformancePackComplianceSummaryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCustomRulePolicyRequest:
    boto3_raw_data: "type_defs.GetCustomRulePolicyRequestTypeDef" = dataclasses.field()

    ConfigRuleName = field("ConfigRuleName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCustomRulePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCustomRulePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDiscoveredResourceCountsRequest:
    boto3_raw_data: "type_defs.GetDiscoveredResourceCountsRequestTypeDef" = (
        dataclasses.field()
    )

    resourceTypes = field("resourceTypes")
    limit = field("limit")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDiscoveredResourceCountsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDiscoveredResourceCountsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceCount:
    boto3_raw_data: "type_defs.ResourceCountTypeDef" = dataclasses.field()

    resourceType = field("resourceType")
    count = field("count")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceCountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceCountTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatusDetailFilters:
    boto3_raw_data: "type_defs.StatusDetailFiltersTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    MemberAccountRuleStatus = field("MemberAccountRuleStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StatusDetailFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StatusDetailFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberAccountStatus:
    boto3_raw_data: "type_defs.MemberAccountStatusTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    ConfigRuleName = field("ConfigRuleName")
    MemberAccountRuleStatus = field("MemberAccountRuleStatus")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")
    LastUpdateTime = field("LastUpdateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MemberAccountStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemberAccountStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationResourceDetailedStatusFilters:
    boto3_raw_data: "type_defs.OrganizationResourceDetailedStatusFiltersTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationResourceDetailedStatusFiltersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationResourceDetailedStatusFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationConformancePackDetailedStatus:
    boto3_raw_data: "type_defs.OrganizationConformancePackDetailedStatusTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")
    ConformancePackName = field("ConformancePackName")
    Status = field("Status")
    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")
    LastUpdateTime = field("LastUpdateTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationConformancePackDetailedStatusTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationConformancePackDetailedStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOrganizationCustomRulePolicyRequest:
    boto3_raw_data: "type_defs.GetOrganizationCustomRulePolicyRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationConfigRuleName = field("OrganizationConfigRuleName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOrganizationCustomRulePolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOrganizationCustomRulePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceEvaluationSummaryRequest:
    boto3_raw_data: "type_defs.GetResourceEvaluationSummaryRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceEvaluationId = field("ResourceEvaluationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetResourceEvaluationSummaryRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceEvaluationSummaryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceDetails:
    boto3_raw_data: "type_defs.ResourceDetailsTypeDef" = dataclasses.field()

    ResourceId = field("ResourceId")
    ResourceType = field("ResourceType")
    ResourceConfiguration = field("ResourceConfiguration")
    ResourceConfigurationSchemaType = field("ResourceConfigurationSchemaType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStoredQueryRequest:
    boto3_raw_data: "type_defs.GetStoredQueryRequestTypeDef" = dataclasses.field()

    QueryName = field("QueryName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStoredQueryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStoredQueryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StoredQuery:
    boto3_raw_data: "type_defs.StoredQueryTypeDef" = dataclasses.field()

    QueryName = field("QueryName")
    QueryId = field("QueryId")
    QueryArn = field("QueryArn")
    Description = field("Description")
    Expression = field("Expression")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StoredQueryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StoredQueryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceFilters:
    boto3_raw_data: "type_defs.ResourceFiltersTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    ResourceId = field("ResourceId")
    ResourceName = field("ResourceName")
    Region = field("Region")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceFiltersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceFiltersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDiscoveredResourcesRequest:
    boto3_raw_data: "type_defs.ListDiscoveredResourcesRequestTypeDef" = (
        dataclasses.field()
    )

    resourceType = field("resourceType")
    resourceIds = field("resourceIds")
    resourceName = field("resourceName")
    limit = field("limit")
    includeDeletedResources = field("includeDeletedResources")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDiscoveredResourcesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDiscoveredResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceIdentifier:
    boto3_raw_data: "type_defs.ResourceIdentifierTypeDef" = dataclasses.field()

    resourceType = field("resourceType")
    resourceId = field("resourceId")
    resourceName = field("resourceName")
    resourceDeletionTime = field("resourceDeletionTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceEvaluation:
    boto3_raw_data: "type_defs.ResourceEvaluationTypeDef" = dataclasses.field()

    ResourceEvaluationId = field("ResourceEvaluationId")
    EvaluationMode = field("EvaluationMode")
    EvaluationStartTimestamp = field("EvaluationStartTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceEvaluationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceEvaluationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStoredQueriesRequest:
    boto3_raw_data: "type_defs.ListStoredQueriesRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStoredQueriesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStoredQueriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StoredQueryMetadata:
    boto3_raw_data: "type_defs.StoredQueryMetadataTypeDef" = dataclasses.field()

    QueryId = field("QueryId")
    QueryArn = field("QueryArn")
    QueryName = field("QueryName")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StoredQueryMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StoredQueryMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


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
class OrganizationAggregationSource:
    boto3_raw_data: "type_defs.OrganizationAggregationSourceTypeDef" = (
        dataclasses.field()
    )

    RoleArn = field("RoleArn")
    AwsRegions = field("AwsRegions")
    AllAwsRegions = field("AllAwsRegions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OrganizationAggregationSourceTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationAggregationSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationCustomPolicyRuleMetadataNoPolicy:
    boto3_raw_data: "type_defs.OrganizationCustomPolicyRuleMetadataNoPolicyTypeDef" = (
        dataclasses.field()
    )

    Description = field("Description")
    OrganizationConfigRuleTriggerTypes = field("OrganizationConfigRuleTriggerTypes")
    InputParameters = field("InputParameters")
    MaximumExecutionFrequency = field("MaximumExecutionFrequency")
    ResourceTypesScope = field("ResourceTypesScope")
    ResourceIdScope = field("ResourceIdScope")
    TagKeyScope = field("TagKeyScope")
    TagValueScope = field("TagValueScope")
    PolicyRuntime = field("PolicyRuntime")
    DebugLogDeliveryAccounts = field("DebugLogDeliveryAccounts")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationCustomPolicyRuleMetadataNoPolicyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationCustomPolicyRuleMetadataNoPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationCustomRuleMetadataOutput:
    boto3_raw_data: "type_defs.OrganizationCustomRuleMetadataOutputTypeDef" = (
        dataclasses.field()
    )

    LambdaFunctionArn = field("LambdaFunctionArn")
    OrganizationConfigRuleTriggerTypes = field("OrganizationConfigRuleTriggerTypes")
    Description = field("Description")
    InputParameters = field("InputParameters")
    MaximumExecutionFrequency = field("MaximumExecutionFrequency")
    ResourceTypesScope = field("ResourceTypesScope")
    ResourceIdScope = field("ResourceIdScope")
    TagKeyScope = field("TagKeyScope")
    TagValueScope = field("TagValueScope")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationCustomRuleMetadataOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationCustomRuleMetadataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationManagedRuleMetadataOutput:
    boto3_raw_data: "type_defs.OrganizationManagedRuleMetadataOutputTypeDef" = (
        dataclasses.field()
    )

    RuleIdentifier = field("RuleIdentifier")
    Description = field("Description")
    InputParameters = field("InputParameters")
    MaximumExecutionFrequency = field("MaximumExecutionFrequency")
    ResourceTypesScope = field("ResourceTypesScope")
    ResourceIdScope = field("ResourceIdScope")
    TagKeyScope = field("TagKeyScope")
    TagValueScope = field("TagValueScope")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationManagedRuleMetadataOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationManagedRuleMetadataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationCustomPolicyRuleMetadata:
    boto3_raw_data: "type_defs.OrganizationCustomPolicyRuleMetadataTypeDef" = (
        dataclasses.field()
    )

    PolicyRuntime = field("PolicyRuntime")
    PolicyText = field("PolicyText")
    Description = field("Description")
    OrganizationConfigRuleTriggerTypes = field("OrganizationConfigRuleTriggerTypes")
    InputParameters = field("InputParameters")
    MaximumExecutionFrequency = field("MaximumExecutionFrequency")
    ResourceTypesScope = field("ResourceTypesScope")
    ResourceIdScope = field("ResourceIdScope")
    TagKeyScope = field("TagKeyScope")
    TagValueScope = field("TagValueScope")
    DebugLogDeliveryAccounts = field("DebugLogDeliveryAccounts")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OrganizationCustomPolicyRuleMetadataTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationCustomPolicyRuleMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationCustomRuleMetadata:
    boto3_raw_data: "type_defs.OrganizationCustomRuleMetadataTypeDef" = (
        dataclasses.field()
    )

    LambdaFunctionArn = field("LambdaFunctionArn")
    OrganizationConfigRuleTriggerTypes = field("OrganizationConfigRuleTriggerTypes")
    Description = field("Description")
    InputParameters = field("InputParameters")
    MaximumExecutionFrequency = field("MaximumExecutionFrequency")
    ResourceTypesScope = field("ResourceTypesScope")
    ResourceIdScope = field("ResourceIdScope")
    TagKeyScope = field("TagKeyScope")
    TagValueScope = field("TagValueScope")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OrganizationCustomRuleMetadataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationCustomRuleMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationManagedRuleMetadata:
    boto3_raw_data: "type_defs.OrganizationManagedRuleMetadataTypeDef" = (
        dataclasses.field()
    )

    RuleIdentifier = field("RuleIdentifier")
    Description = field("Description")
    InputParameters = field("InputParameters")
    MaximumExecutionFrequency = field("MaximumExecutionFrequency")
    ResourceTypesScope = field("ResourceTypesScope")
    ResourceIdScope = field("ResourceIdScope")
    TagKeyScope = field("TagKeyScope")
    TagValueScope = field("TagValueScope")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.OrganizationManagedRuleMetadataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationManagedRuleMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourceConfigRequest:
    boto3_raw_data: "type_defs.PutResourceConfigRequestTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    SchemaVersionId = field("SchemaVersionId")
    ResourceId = field("ResourceId")
    Configuration = field("Configuration")
    ResourceName = field("ResourceName")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourceConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourceConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRetentionConfigurationRequest:
    boto3_raw_data: "type_defs.PutRetentionConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    RetentionPeriodInDays = field("RetentionPeriodInDays")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutRetentionConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRetentionConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordingStrategy:
    boto3_raw_data: "type_defs.RecordingStrategyTypeDef" = dataclasses.field()

    useOnly = field("useOnly")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecordingStrategyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecordingStrategyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordingModeOverrideOutput:
    boto3_raw_data: "type_defs.RecordingModeOverrideOutputTypeDef" = dataclasses.field()

    resourceTypes = field("resourceTypes")
    recordingFrequency = field("recordingFrequency")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecordingModeOverrideOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecordingModeOverrideOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordingModeOverride:
    boto3_raw_data: "type_defs.RecordingModeOverrideTypeDef" = dataclasses.field()

    resourceTypes = field("resourceTypes")
    recordingFrequency = field("recordingFrequency")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecordingModeOverrideTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecordingModeOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemediationExecutionStep:
    boto3_raw_data: "type_defs.RemediationExecutionStepTypeDef" = dataclasses.field()

    Name = field("Name")
    State = field("State")
    ErrorMessage = field("ErrorMessage")
    StartTime = field("StartTime")
    StopTime = field("StopTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemediationExecutionStepTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemediationExecutionStepTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceValue:
    boto3_raw_data: "type_defs.ResourceValueTypeDef" = dataclasses.field()

    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceValueTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StaticValueOutput:
    boto3_raw_data: "type_defs.StaticValueOutputTypeDef" = dataclasses.field()

    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StaticValueOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StaticValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelectAggregateResourceConfigRequest:
    boto3_raw_data: "type_defs.SelectAggregateResourceConfigRequestTypeDef" = (
        dataclasses.field()
    )

    Expression = field("Expression")
    ConfigurationAggregatorName = field("ConfigurationAggregatorName")
    Limit = field("Limit")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SelectAggregateResourceConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelectAggregateResourceConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelectResourceConfigRequest:
    boto3_raw_data: "type_defs.SelectResourceConfigRequestTypeDef" = dataclasses.field()

    Expression = field("Expression")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SelectResourceConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelectResourceConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceDetail:
    boto3_raw_data: "type_defs.SourceDetailTypeDef" = dataclasses.field()

    EventSource = field("EventSource")
    MessageType = field("MessageType")
    MaximumExecutionFrequency = field("MaximumExecutionFrequency")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartConfigRulesEvaluationRequest:
    boto3_raw_data: "type_defs.StartConfigRulesEvaluationRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigRuleNames = field("ConfigRuleNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartConfigRulesEvaluationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartConfigRulesEvaluationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartConfigurationRecorderRequest:
    boto3_raw_data: "type_defs.StartConfigurationRecorderRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationRecorderName = field("ConfigurationRecorderName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartConfigurationRecorderRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartConfigurationRecorderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StaticValue:
    boto3_raw_data: "type_defs.StaticValueTypeDef" = dataclasses.field()

    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StaticValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StaticValueTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopConfigurationRecorderRequest:
    boto3_raw_data: "type_defs.StopConfigurationRecorderRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationRecorderName = field("ConfigurationRecorderName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StopConfigurationRecorderRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopConfigurationRecorderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregateComplianceByConformancePack:
    boto3_raw_data: "type_defs.AggregateComplianceByConformancePackTypeDef" = (
        dataclasses.field()
    )

    ConformancePackName = field("ConformancePackName")

    @cached_property
    def Compliance(self):  # pragma: no cover
        return AggregateConformancePackCompliance.make_one(
            self.boto3_raw_data["Compliance"]
        )

    AccountId = field("AccountId")
    AwsRegion = field("AwsRegion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AggregateComplianceByConformancePackTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregateComplianceByConformancePackTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregateConformancePackComplianceSummary:
    boto3_raw_data: "type_defs.AggregateConformancePackComplianceSummaryTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ComplianceSummary(self):  # pragma: no cover
        return AggregateConformancePackComplianceCount.make_one(
            self.boto3_raw_data["ComplianceSummary"]
        )

    GroupName = field("GroupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AggregateConformancePackComplianceSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregateConformancePackComplianceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAggregateComplianceByConformancePacksRequest:
    boto3_raw_data: (
        "type_defs.DescribeAggregateComplianceByConformancePacksRequestTypeDef"
    ) = dataclasses.field()

    ConfigurationAggregatorName = field("ConfigurationAggregatorName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return AggregateConformancePackComplianceFilters.make_one(
            self.boto3_raw_data["Filters"]
        )

    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAggregateComplianceByConformancePacksRequestTypeDef"
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
                "type_defs.DescribeAggregateComplianceByConformancePacksRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAggregateConformancePackComplianceSummaryRequest:
    boto3_raw_data: (
        "type_defs.GetAggregateConformancePackComplianceSummaryRequestTypeDef"
    ) = dataclasses.field()

    ConfigurationAggregatorName = field("ConfigurationAggregatorName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return AggregateConformancePackComplianceSummaryFilters.make_one(
            self.boto3_raw_data["Filters"]
        )

    GroupByKey = field("GroupByKey")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAggregateConformancePackComplianceSummaryRequestTypeDef"
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
                "type_defs.GetAggregateConformancePackComplianceSummaryRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAggregateResourceConfigRequest:
    boto3_raw_data: "type_defs.BatchGetAggregateResourceConfigRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationAggregatorName = field("ConfigurationAggregatorName")

    @cached_property
    def ResourceIdentifiers(self):  # pragma: no cover
        return AggregateResourceIdentifier.make_many(
            self.boto3_raw_data["ResourceIdentifiers"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetAggregateResourceConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAggregateResourceConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAggregateResourceConfigRequest:
    boto3_raw_data: "type_defs.GetAggregateResourceConfigRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationAggregatorName = field("ConfigurationAggregatorName")

    @cached_property
    def ResourceIdentifier(self):  # pragma: no cover
        return AggregateResourceIdentifier.make_one(
            self.boto3_raw_data["ResourceIdentifier"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAggregateResourceConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAggregateResourceConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregatorFiltersOutput:
    boto3_raw_data: "type_defs.AggregatorFiltersOutputTypeDef" = dataclasses.field()

    @cached_property
    def ResourceType(self):  # pragma: no cover
        return AggregatorFilterResourceTypeOutput.make_one(
            self.boto3_raw_data["ResourceType"]
        )

    @cached_property
    def ServicePrincipal(self):  # pragma: no cover
        return AggregatorFilterServicePrincipalOutput.make_one(
            self.boto3_raw_data["ServicePrincipal"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AggregatorFiltersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregatorFiltersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregatorFilters:
    boto3_raw_data: "type_defs.AggregatorFiltersTypeDef" = dataclasses.field()

    @cached_property
    def ResourceType(self):  # pragma: no cover
        return AggregatorFilterResourceType.make_one(
            self.boto3_raw_data["ResourceType"]
        )

    @cached_property
    def ServicePrincipal(self):  # pragma: no cover
        return AggregatorFilterServicePrincipal.make_one(
            self.boto3_raw_data["ServicePrincipal"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AggregatorFiltersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregatorFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteServiceLinkedConfigurationRecorderResponse:
    boto3_raw_data: (
        "type_defs.DeleteServiceLinkedConfigurationRecorderResponseTypeDef"
    ) = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteServiceLinkedConfigurationRecorderResponseTypeDef"
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
                "type_defs.DeleteServiceLinkedConfigurationRecorderResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeliverConfigSnapshotResponse:
    boto3_raw_data: "type_defs.DeliverConfigSnapshotResponseTypeDef" = (
        dataclasses.field()
    )

    configSnapshotId = field("configSnapshotId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeliverConfigSnapshotResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeliverConfigSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAggregationAuthorizationsResponse:
    boto3_raw_data: "type_defs.DescribeAggregationAuthorizationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AggregationAuthorizations(self):  # pragma: no cover
        return AggregationAuthorization.make_many(
            self.boto3_raw_data["AggregationAuthorizations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAggregationAuthorizationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAggregationAuthorizationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigurationAggregatorSourcesStatusResponse:
    boto3_raw_data: (
        "type_defs.DescribeConfigurationAggregatorSourcesStatusResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def AggregatedSourceStatusList(self):  # pragma: no cover
        return AggregatedSourceStatus.make_many(
            self.boto3_raw_data["AggregatedSourceStatusList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConfigurationAggregatorSourcesStatusResponseTypeDef"
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
                "type_defs.DescribeConfigurationAggregatorSourcesStatusResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmptyResponseMetadata:
    boto3_raw_data: "type_defs.EmptyResponseMetadataTypeDef" = dataclasses.field()

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmptyResponseMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmptyResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCustomRulePolicyResponse:
    boto3_raw_data: "type_defs.GetCustomRulePolicyResponseTypeDef" = dataclasses.field()

    PolicyText = field("PolicyText")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCustomRulePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCustomRulePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOrganizationCustomRulePolicyResponse:
    boto3_raw_data: "type_defs.GetOrganizationCustomRulePolicyResponseTypeDef" = (
        dataclasses.field()
    )

    PolicyText = field("PolicyText")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOrganizationCustomRulePolicyResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOrganizationCustomRulePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAggregateDiscoveredResourcesResponse:
    boto3_raw_data: "type_defs.ListAggregateDiscoveredResourcesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResourceIdentifiers(self):  # pragma: no cover
        return AggregateResourceIdentifier.make_many(
            self.boto3_raw_data["ResourceIdentifiers"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAggregateDiscoveredResourcesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAggregateDiscoveredResourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAggregationAuthorizationResponse:
    boto3_raw_data: "type_defs.PutAggregationAuthorizationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AggregationAuthorization(self):  # pragma: no cover
        return AggregationAuthorization.make_one(
            self.boto3_raw_data["AggregationAuthorization"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutAggregationAuthorizationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAggregationAuthorizationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutConformancePackResponse:
    boto3_raw_data: "type_defs.PutConformancePackResponseTypeDef" = dataclasses.field()

    ConformancePackArn = field("ConformancePackArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutConformancePackResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutConformancePackResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutOrganizationConfigRuleResponse:
    boto3_raw_data: "type_defs.PutOrganizationConfigRuleResponseTypeDef" = (
        dataclasses.field()
    )

    OrganizationConfigRuleArn = field("OrganizationConfigRuleArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutOrganizationConfigRuleResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutOrganizationConfigRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutOrganizationConformancePackResponse:
    boto3_raw_data: "type_defs.PutOrganizationConformancePackResponseTypeDef" = (
        dataclasses.field()
    )

    OrganizationConformancePackArn = field("OrganizationConformancePackArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutOrganizationConformancePackResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutOrganizationConformancePackResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutServiceLinkedConfigurationRecorderResponse:
    boto3_raw_data: "type_defs.PutServiceLinkedConfigurationRecorderResponseTypeDef" = (
        dataclasses.field()
    )

    Arn = field("Arn")
    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutServiceLinkedConfigurationRecorderResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutServiceLinkedConfigurationRecorderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutStoredQueryResponse:
    boto3_raw_data: "type_defs.PutStoredQueryResponseTypeDef" = dataclasses.field()

    QueryArn = field("QueryArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutStoredQueryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutStoredQueryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartResourceEvaluationResponse:
    boto3_raw_data: "type_defs.StartResourceEvaluationResponseTypeDef" = (
        dataclasses.field()
    )

    ResourceEvaluationId = field("ResourceEvaluationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartResourceEvaluationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartResourceEvaluationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetAggregateResourceConfigResponse:
    boto3_raw_data: "type_defs.BatchGetAggregateResourceConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def BaseConfigurationItems(self):  # pragma: no cover
        return BaseConfigurationItem.make_many(
            self.boto3_raw_data["BaseConfigurationItems"]
        )

    @cached_property
    def UnprocessedResourceIdentifiers(self):  # pragma: no cover
        return AggregateResourceIdentifier.make_many(
            self.boto3_raw_data["UnprocessedResourceIdentifiers"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetAggregateResourceConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetAggregateResourceConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetResourceConfigRequest:
    boto3_raw_data: "type_defs.BatchGetResourceConfigRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def resourceKeys(self):  # pragma: no cover
        return ResourceKey.make_many(self.boto3_raw_data["resourceKeys"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetResourceConfigRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetResourceConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetResourceConfigResponse:
    boto3_raw_data: "type_defs.BatchGetResourceConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def baseConfigurationItems(self):  # pragma: no cover
        return BaseConfigurationItem.make_many(
            self.boto3_raw_data["baseConfigurationItems"]
        )

    @cached_property
    def unprocessedResourceKeys(self):  # pragma: no cover
        return ResourceKey.make_many(self.boto3_raw_data["unprocessedResourceKeys"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetResourceConfigResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetResourceConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRemediationExecutionStatusRequest:
    boto3_raw_data: "type_defs.DescribeRemediationExecutionStatusRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigRuleName = field("ConfigRuleName")

    @cached_property
    def ResourceKeys(self):  # pragma: no cover
        return ResourceKey.make_many(self.boto3_raw_data["ResourceKeys"])

    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRemediationExecutionStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRemediationExecutionStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRemediationExecutionRequest:
    boto3_raw_data: "type_defs.StartRemediationExecutionRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigRuleName = field("ConfigRuleName")

    @cached_property
    def ResourceKeys(self):  # pragma: no cover
        return ResourceKey.make_many(self.boto3_raw_data["ResourceKeys"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartRemediationExecutionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRemediationExecutionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartRemediationExecutionResponse:
    boto3_raw_data: "type_defs.StartRemediationExecutionResponseTypeDef" = (
        dataclasses.field()
    )

    FailureMessage = field("FailureMessage")

    @cached_property
    def FailedItems(self):  # pragma: no cover
        return ResourceKey.make_many(self.boto3_raw_data["FailedItems"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartRemediationExecutionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartRemediationExecutionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComplianceSummary:
    boto3_raw_data: "type_defs.ComplianceSummaryTypeDef" = dataclasses.field()

    @cached_property
    def CompliantResourceCount(self):  # pragma: no cover
        return ComplianceContributorCount.make_one(
            self.boto3_raw_data["CompliantResourceCount"]
        )

    @cached_property
    def NonCompliantResourceCount(self):  # pragma: no cover
        return ComplianceContributorCount.make_one(
            self.boto3_raw_data["NonCompliantResourceCount"]
        )

    ComplianceSummaryTimestamp = field("ComplianceSummaryTimestamp")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComplianceSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComplianceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Compliance:
    boto3_raw_data: "type_defs.ComplianceTypeDef" = dataclasses.field()

    ComplianceType = field("ComplianceType")

    @cached_property
    def ComplianceContributorCount(self):  # pragma: no cover
        return ComplianceContributorCount.make_one(
            self.boto3_raw_data["ComplianceContributorCount"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ComplianceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ComplianceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAggregateComplianceByConfigRulesRequest:
    boto3_raw_data: (
        "type_defs.DescribeAggregateComplianceByConfigRulesRequestTypeDef"
    ) = dataclasses.field()

    ConfigurationAggregatorName = field("ConfigurationAggregatorName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ConfigRuleComplianceFilters.make_one(self.boto3_raw_data["Filters"])

    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAggregateComplianceByConfigRulesRequestTypeDef"
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
                "type_defs.DescribeAggregateComplianceByConfigRulesRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAggregateConfigRuleComplianceSummaryRequest:
    boto3_raw_data: (
        "type_defs.GetAggregateConfigRuleComplianceSummaryRequestTypeDef"
    ) = dataclasses.field()

    ConfigurationAggregatorName = field("ConfigurationAggregatorName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ConfigRuleComplianceSummaryFilters.make_one(
            self.boto3_raw_data["Filters"]
        )

    GroupByKey = field("GroupByKey")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAggregateConfigRuleComplianceSummaryRequestTypeDef"
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
                "type_defs.GetAggregateConfigRuleComplianceSummaryRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigRuleEvaluationStatusResponse:
    boto3_raw_data: "type_defs.DescribeConfigRuleEvaluationStatusResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConfigRulesEvaluationStatus(self):  # pragma: no cover
        return ConfigRuleEvaluationStatus.make_many(
            self.boto3_raw_data["ConfigRulesEvaluationStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConfigRuleEvaluationStatusResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigRuleEvaluationStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeliveryChannel:
    boto3_raw_data: "type_defs.DeliveryChannelTypeDef" = dataclasses.field()

    name = field("name")
    s3BucketName = field("s3BucketName")
    s3KeyPrefix = field("s3KeyPrefix")
    s3KmsKeyArn = field("s3KmsKeyArn")
    snsTopicARN = field("snsTopicARN")

    @cached_property
    def configSnapshotDeliveryProperties(self):  # pragma: no cover
        return ConfigSnapshotDeliveryProperties.make_one(
            self.boto3_raw_data["configSnapshotDeliveryProperties"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeliveryChannelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeliveryChannelTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeliveryChannelStatus:
    boto3_raw_data: "type_defs.DeliveryChannelStatusTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def configSnapshotDeliveryInfo(self):  # pragma: no cover
        return ConfigExportDeliveryInfo.make_one(
            self.boto3_raw_data["configSnapshotDeliveryInfo"]
        )

    @cached_property
    def configHistoryDeliveryInfo(self):  # pragma: no cover
        return ConfigExportDeliveryInfo.make_one(
            self.boto3_raw_data["configHistoryDeliveryInfo"]
        )

    @cached_property
    def configStreamDeliveryInfo(self):  # pragma: no cover
        return ConfigStreamDeliveryInfo.make_one(
            self.boto3_raw_data["configStreamDeliveryInfo"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeliveryChannelStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeliveryChannelStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationItem:
    boto3_raw_data: "type_defs.ConfigurationItemTypeDef" = dataclasses.field()

    version = field("version")
    accountId = field("accountId")
    configurationItemCaptureTime = field("configurationItemCaptureTime")
    configurationItemStatus = field("configurationItemStatus")
    configurationStateId = field("configurationStateId")
    configurationItemMD5Hash = field("configurationItemMD5Hash")
    arn = field("arn")
    resourceType = field("resourceType")
    resourceId = field("resourceId")
    resourceName = field("resourceName")
    awsRegion = field("awsRegion")
    availabilityZone = field("availabilityZone")
    resourceCreationTime = field("resourceCreationTime")
    tags = field("tags")
    relatedEvents = field("relatedEvents")

    @cached_property
    def relationships(self):  # pragma: no cover
        return Relationship.make_many(self.boto3_raw_data["relationships"])

    configuration = field("configuration")
    supplementaryConfiguration = field("supplementaryConfiguration")
    recordingFrequency = field("recordingFrequency")
    configurationItemDeliveryTime = field("configurationItemDeliveryTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConfigurationItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfigurationRecordersRequest:
    boto3_raw_data: "type_defs.ListConfigurationRecordersRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return ConfigurationRecorderFilter.make_many(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfigurationRecordersRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfigurationRecordersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigurationRecorderStatusResponse:
    boto3_raw_data: "type_defs.DescribeConfigurationRecorderStatusResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConfigurationRecordersStatus(self):  # pragma: no cover
        return ConfigurationRecorderStatus.make_many(
            self.boto3_raw_data["ConfigurationRecordersStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConfigurationRecorderStatusResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigurationRecorderStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfigurationRecordersResponse:
    boto3_raw_data: "type_defs.ListConfigurationRecordersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConfigurationRecorderSummaries(self):  # pragma: no cover
        return ConfigurationRecorderSummary.make_many(
            self.boto3_raw_data["ConfigurationRecorderSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfigurationRecordersResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfigurationRecordersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConformancePackComplianceRequest:
    boto3_raw_data: "type_defs.DescribeConformancePackComplianceRequestTypeDef" = (
        dataclasses.field()
    )

    ConformancePackName = field("ConformancePackName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ConformancePackComplianceFilters.make_one(self.boto3_raw_data["Filters"])

    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConformancePackComplianceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConformancePackComplianceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConformancePackComplianceScoresResponse:
    boto3_raw_data: "type_defs.ListConformancePackComplianceScoresResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConformancePackComplianceScores(self):  # pragma: no cover
        return ConformancePackComplianceScore.make_many(
            self.boto3_raw_data["ConformancePackComplianceScores"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConformancePackComplianceScoresResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConformancePackComplianceScoresResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConformancePackComplianceScoresRequest:
    boto3_raw_data: "type_defs.ListConformancePackComplianceScoresRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return ConformancePackComplianceScoresFilters.make_one(
            self.boto3_raw_data["Filters"]
        )

    SortOrder = field("SortOrder")
    SortBy = field("SortBy")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConformancePackComplianceScoresRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConformancePackComplianceScoresRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConformancePackComplianceSummaryResponse:
    boto3_raw_data: "type_defs.GetConformancePackComplianceSummaryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConformancePackComplianceSummaryList(self):  # pragma: no cover
        return ConformancePackComplianceSummary.make_many(
            self.boto3_raw_data["ConformancePackComplianceSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConformancePackComplianceSummaryResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConformancePackComplianceSummaryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationConformancePack:
    boto3_raw_data: "type_defs.OrganizationConformancePackTypeDef" = dataclasses.field()

    OrganizationConformancePackName = field("OrganizationConformancePackName")
    OrganizationConformancePackArn = field("OrganizationConformancePackArn")
    LastUpdateTime = field("LastUpdateTime")
    DeliveryS3Bucket = field("DeliveryS3Bucket")
    DeliveryS3KeyPrefix = field("DeliveryS3KeyPrefix")

    @cached_property
    def ConformancePackInputParameters(self):  # pragma: no cover
        return ConformancePackInputParameter.make_many(
            self.boto3_raw_data["ConformancePackInputParameters"]
        )

    ExcludedAccounts = field("ExcludedAccounts")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrganizationConformancePackTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationConformancePackTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutOrganizationConformancePackRequest:
    boto3_raw_data: "type_defs.PutOrganizationConformancePackRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationConformancePackName = field("OrganizationConformancePackName")
    TemplateS3Uri = field("TemplateS3Uri")
    TemplateBody = field("TemplateBody")
    DeliveryS3Bucket = field("DeliveryS3Bucket")
    DeliveryS3KeyPrefix = field("DeliveryS3KeyPrefix")

    @cached_property
    def ConformancePackInputParameters(self):  # pragma: no cover
        return ConformancePackInputParameter.make_many(
            self.boto3_raw_data["ConformancePackInputParameters"]
        )

    ExcludedAccounts = field("ExcludedAccounts")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutOrganizationConformancePackRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutOrganizationConformancePackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConformancePackDetail:
    boto3_raw_data: "type_defs.ConformancePackDetailTypeDef" = dataclasses.field()

    ConformancePackName = field("ConformancePackName")
    ConformancePackArn = field("ConformancePackArn")
    ConformancePackId = field("ConformancePackId")
    DeliveryS3Bucket = field("DeliveryS3Bucket")
    DeliveryS3KeyPrefix = field("DeliveryS3KeyPrefix")

    @cached_property
    def ConformancePackInputParameters(self):  # pragma: no cover
        return ConformancePackInputParameter.make_many(
            self.boto3_raw_data["ConformancePackInputParameters"]
        )

    LastUpdateRequestedTime = field("LastUpdateRequestedTime")
    CreatedBy = field("CreatedBy")

    @cached_property
    def TemplateSSMDocumentDetails(self):  # pragma: no cover
        return TemplateSSMDocumentDetails.make_one(
            self.boto3_raw_data["TemplateSSMDocumentDetails"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConformancePackDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConformancePackDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutConformancePackRequest:
    boto3_raw_data: "type_defs.PutConformancePackRequestTypeDef" = dataclasses.field()

    ConformancePackName = field("ConformancePackName")
    TemplateS3Uri = field("TemplateS3Uri")
    TemplateBody = field("TemplateBody")
    DeliveryS3Bucket = field("DeliveryS3Bucket")
    DeliveryS3KeyPrefix = field("DeliveryS3KeyPrefix")

    @cached_property
    def ConformancePackInputParameters(self):  # pragma: no cover
        return ConformancePackInputParameter.make_many(
            self.boto3_raw_data["ConformancePackInputParameters"]
        )

    @cached_property
    def TemplateSSMDocumentDetails(self):  # pragma: no cover
        return TemplateSSMDocumentDetails.make_one(
            self.boto3_raw_data["TemplateSSMDocumentDetails"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutConformancePackRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutConformancePackRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConformancePackComplianceDetailsRequest:
    boto3_raw_data: "type_defs.GetConformancePackComplianceDetailsRequestTypeDef" = (
        dataclasses.field()
    )

    ConformancePackName = field("ConformancePackName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ConformancePackEvaluationFilters.make_one(self.boto3_raw_data["Filters"])

    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConformancePackComplianceDetailsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConformancePackComplianceDetailsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConformancePackComplianceResponse:
    boto3_raw_data: "type_defs.DescribeConformancePackComplianceResponseTypeDef" = (
        dataclasses.field()
    )

    ConformancePackName = field("ConformancePackName")

    @cached_property
    def ConformancePackRuleComplianceList(self):  # pragma: no cover
        return ConformancePackRuleCompliance.make_many(
            self.boto3_raw_data["ConformancePackRuleComplianceList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConformancePackComplianceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConformancePackComplianceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConformancePackStatusResponse:
    boto3_raw_data: "type_defs.DescribeConformancePackStatusResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConformancePackStatusDetails(self):  # pragma: no cover
        return ConformancePackStatusDetail.make_many(
            self.boto3_raw_data["ConformancePackStatusDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConformancePackStatusResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConformancePackStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRemediationExceptionsRequest:
    boto3_raw_data: "type_defs.DeleteRemediationExceptionsRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigRuleName = field("ConfigRuleName")

    @cached_property
    def ResourceKeys(self):  # pragma: no cover
        return RemediationExceptionResourceKey.make_many(
            self.boto3_raw_data["ResourceKeys"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteRemediationExceptionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRemediationExceptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRemediationExceptionsRequest:
    boto3_raw_data: "type_defs.DescribeRemediationExceptionsRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigRuleName = field("ConfigRuleName")

    @cached_property
    def ResourceKeys(self):  # pragma: no cover
        return RemediationExceptionResourceKey.make_many(
            self.boto3_raw_data["ResourceKeys"]
        )

    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRemediationExceptionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRemediationExceptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailedDeleteRemediationExceptionsBatch:
    boto3_raw_data: "type_defs.FailedDeleteRemediationExceptionsBatchTypeDef" = (
        dataclasses.field()
    )

    FailureMessage = field("FailureMessage")

    @cached_property
    def FailedItems(self):  # pragma: no cover
        return RemediationExceptionResourceKey.make_many(
            self.boto3_raw_data["FailedItems"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.FailedDeleteRemediationExceptionsBatchTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailedDeleteRemediationExceptionsBatchTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAggregateComplianceByConfigRulesRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeAggregateComplianceByConfigRulesRequestPaginateTypeDef"
    ) = dataclasses.field()

    ConfigurationAggregatorName = field("ConfigurationAggregatorName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ConfigRuleComplianceFilters.make_one(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAggregateComplianceByConfigRulesRequestPaginateTypeDef"
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
                "type_defs.DescribeAggregateComplianceByConfigRulesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAggregateComplianceByConformancePacksRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeAggregateComplianceByConformancePacksRequestPaginateTypeDef"
    ) = dataclasses.field()

    ConfigurationAggregatorName = field("ConfigurationAggregatorName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return AggregateConformancePackComplianceFilters.make_one(
            self.boto3_raw_data["Filters"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAggregateComplianceByConformancePacksRequestPaginateTypeDef"
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
                "type_defs.DescribeAggregateComplianceByConformancePacksRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAggregationAuthorizationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeAggregationAuthorizationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAggregationAuthorizationsRequestPaginateTypeDef"
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
                "type_defs.DescribeAggregationAuthorizationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeComplianceByConfigRuleRequestPaginate:
    boto3_raw_data: "type_defs.DescribeComplianceByConfigRuleRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ConfigRuleNames = field("ConfigRuleNames")
    ComplianceTypes = field("ComplianceTypes")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeComplianceByConfigRuleRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeComplianceByConfigRuleRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeComplianceByResourceRequestPaginate:
    boto3_raw_data: "type_defs.DescribeComplianceByResourceRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceType = field("ResourceType")
    ResourceId = field("ResourceId")
    ComplianceTypes = field("ComplianceTypes")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeComplianceByResourceRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeComplianceByResourceRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigRuleEvaluationStatusRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeConfigRuleEvaluationStatusRequestPaginateTypeDef"
    ) = dataclasses.field()

    ConfigRuleNames = field("ConfigRuleNames")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConfigRuleEvaluationStatusRequestPaginateTypeDef"
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
                "type_defs.DescribeConfigRuleEvaluationStatusRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigurationAggregatorSourcesStatusRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeConfigurationAggregatorSourcesStatusRequestPaginateTypeDef"
    ) = dataclasses.field()

    ConfigurationAggregatorName = field("ConfigurationAggregatorName")
    UpdateStatus = field("UpdateStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConfigurationAggregatorSourcesStatusRequestPaginateTypeDef"
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
                "type_defs.DescribeConfigurationAggregatorSourcesStatusRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigurationAggregatorsRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeConfigurationAggregatorsRequestPaginateTypeDef"
    ) = dataclasses.field()

    ConfigurationAggregatorNames = field("ConfigurationAggregatorNames")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConfigurationAggregatorsRequestPaginateTypeDef"
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
                "type_defs.DescribeConfigurationAggregatorsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConformancePackStatusRequestPaginate:
    boto3_raw_data: "type_defs.DescribeConformancePackStatusRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ConformancePackNames = field("ConformancePackNames")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConformancePackStatusRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConformancePackStatusRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConformancePacksRequestPaginate:
    boto3_raw_data: "type_defs.DescribeConformancePacksRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ConformancePackNames = field("ConformancePackNames")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConformancePacksRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConformancePacksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationConfigRuleStatusesRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeOrganizationConfigRuleStatusesRequestPaginateTypeDef"
    ) = dataclasses.field()

    OrganizationConfigRuleNames = field("OrganizationConfigRuleNames")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrganizationConfigRuleStatusesRequestPaginateTypeDef"
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
                "type_defs.DescribeOrganizationConfigRuleStatusesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationConfigRulesRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeOrganizationConfigRulesRequestPaginateTypeDef"
    ) = dataclasses.field()

    OrganizationConfigRuleNames = field("OrganizationConfigRuleNames")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrganizationConfigRulesRequestPaginateTypeDef"
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
                "type_defs.DescribeOrganizationConfigRulesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationConformancePackStatusesRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeOrganizationConformancePackStatusesRequestPaginateTypeDef"
    ) = dataclasses.field()

    OrganizationConformancePackNames = field("OrganizationConformancePackNames")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrganizationConformancePackStatusesRequestPaginateTypeDef"
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
                "type_defs.DescribeOrganizationConformancePackStatusesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationConformancePacksRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeOrganizationConformancePacksRequestPaginateTypeDef"
    ) = dataclasses.field()

    OrganizationConformancePackNames = field("OrganizationConformancePackNames")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrganizationConformancePacksRequestPaginateTypeDef"
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
                "type_defs.DescribeOrganizationConformancePacksRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePendingAggregationRequestsRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribePendingAggregationRequestsRequestPaginateTypeDef"
    ) = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePendingAggregationRequestsRequestPaginateTypeDef"
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
                "type_defs.DescribePendingAggregationRequestsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRemediationExecutionStatusRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeRemediationExecutionStatusRequestPaginateTypeDef"
    ) = dataclasses.field()

    ConfigRuleName = field("ConfigRuleName")

    @cached_property
    def ResourceKeys(self):  # pragma: no cover
        return ResourceKey.make_many(self.boto3_raw_data["ResourceKeys"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRemediationExecutionStatusRequestPaginateTypeDef"
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
                "type_defs.DescribeRemediationExecutionStatusRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRetentionConfigurationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeRetentionConfigurationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    RetentionConfigurationNames = field("RetentionConfigurationNames")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRetentionConfigurationsRequestPaginateTypeDef"
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
                "type_defs.DescribeRetentionConfigurationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAggregateComplianceDetailsByConfigRuleRequestPaginate:
    boto3_raw_data: (
        "type_defs.GetAggregateComplianceDetailsByConfigRuleRequestPaginateTypeDef"
    ) = dataclasses.field()

    ConfigurationAggregatorName = field("ConfigurationAggregatorName")
    ConfigRuleName = field("ConfigRuleName")
    AccountId = field("AccountId")
    AwsRegion = field("AwsRegion")
    ComplianceType = field("ComplianceType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAggregateComplianceDetailsByConfigRuleRequestPaginateTypeDef"
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
                "type_defs.GetAggregateComplianceDetailsByConfigRuleRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComplianceDetailsByConfigRuleRequestPaginate:
    boto3_raw_data: (
        "type_defs.GetComplianceDetailsByConfigRuleRequestPaginateTypeDef"
    ) = dataclasses.field()

    ConfigRuleName = field("ConfigRuleName")
    ComplianceTypes = field("ComplianceTypes")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetComplianceDetailsByConfigRuleRequestPaginateTypeDef"
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
                "type_defs.GetComplianceDetailsByConfigRuleRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComplianceDetailsByResourceRequestPaginate:
    boto3_raw_data: "type_defs.GetComplianceDetailsByResourceRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceType = field("ResourceType")
    ResourceId = field("ResourceId")
    ComplianceTypes = field("ComplianceTypes")
    ResourceEvaluationId = field("ResourceEvaluationId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetComplianceDetailsByResourceRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComplianceDetailsByResourceRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConformancePackComplianceSummaryRequestPaginate:
    boto3_raw_data: (
        "type_defs.GetConformancePackComplianceSummaryRequestPaginateTypeDef"
    ) = dataclasses.field()

    ConformancePackNames = field("ConformancePackNames")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConformancePackComplianceSummaryRequestPaginateTypeDef"
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
                "type_defs.GetConformancePackComplianceSummaryRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfigurationRecordersRequestPaginate:
    boto3_raw_data: "type_defs.ListConfigurationRecordersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return ConfigurationRecorderFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfigurationRecordersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfigurationRecordersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDiscoveredResourcesRequestPaginate:
    boto3_raw_data: "type_defs.ListDiscoveredResourcesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    resourceType = field("resourceType")
    resourceIds = field("resourceIds")
    resourceName = field("resourceName")
    includeDeletedResources = field("includeDeletedResources")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDiscoveredResourcesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDiscoveredResourcesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequestPaginate:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTagsForResourceRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelectAggregateResourceConfigRequestPaginate:
    boto3_raw_data: "type_defs.SelectAggregateResourceConfigRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Expression = field("Expression")
    ConfigurationAggregatorName = field("ConfigurationAggregatorName")
    MaxResults = field("MaxResults")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SelectAggregateResourceConfigRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelectAggregateResourceConfigRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelectResourceConfigRequestPaginate:
    boto3_raw_data: "type_defs.SelectResourceConfigRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Expression = field("Expression")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SelectResourceConfigRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelectResourceConfigRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigRulesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeConfigRulesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ConfigRuleNames = field("ConfigRuleNames")

    @cached_property
    def Filters(self):  # pragma: no cover
        return DescribeConfigRulesFilters.make_one(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConfigRulesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigRulesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigRulesRequest:
    boto3_raw_data: "type_defs.DescribeConfigRulesRequestTypeDef" = dataclasses.field()

    ConfigRuleNames = field("ConfigRuleNames")
    NextToken = field("NextToken")

    @cached_property
    def Filters(self):  # pragma: no cover
        return DescribeConfigRulesFilters.make_one(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeConfigRulesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigRulesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationConfigRuleStatusesResponse:
    boto3_raw_data: (
        "type_defs.DescribeOrganizationConfigRuleStatusesResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def OrganizationConfigRuleStatuses(self):  # pragma: no cover
        return OrganizationConfigRuleStatus.make_many(
            self.boto3_raw_data["OrganizationConfigRuleStatuses"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrganizationConfigRuleStatusesResponseTypeDef"
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
                "type_defs.DescribeOrganizationConfigRuleStatusesResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationConformancePackStatusesResponse:
    boto3_raw_data: (
        "type_defs.DescribeOrganizationConformancePackStatusesResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def OrganizationConformancePackStatuses(self):  # pragma: no cover
        return OrganizationConformancePackStatus.make_many(
            self.boto3_raw_data["OrganizationConformancePackStatuses"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrganizationConformancePackStatusesResponseTypeDef"
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
                "type_defs.DescribeOrganizationConformancePackStatusesResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePendingAggregationRequestsResponse:
    boto3_raw_data: "type_defs.DescribePendingAggregationRequestsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PendingAggregationRequests(self):  # pragma: no cover
        return PendingAggregationRequest.make_many(
            self.boto3_raw_data["PendingAggregationRequests"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePendingAggregationRequestsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePendingAggregationRequestsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRemediationExceptionsResponse:
    boto3_raw_data: "type_defs.DescribeRemediationExceptionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RemediationExceptions(self):  # pragma: no cover
        return RemediationException.make_many(
            self.boto3_raw_data["RemediationExceptions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRemediationExceptionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRemediationExceptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailedRemediationExceptionBatch:
    boto3_raw_data: "type_defs.FailedRemediationExceptionBatchTypeDef" = (
        dataclasses.field()
    )

    FailureMessage = field("FailureMessage")

    @cached_property
    def FailedItems(self):  # pragma: no cover
        return RemediationException.make_many(self.boto3_raw_data["FailedItems"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FailedRemediationExceptionBatchTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailedRemediationExceptionBatchTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRetentionConfigurationsResponse:
    boto3_raw_data: "type_defs.DescribeRetentionConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RetentionConfigurations(self):  # pragma: no cover
        return RetentionConfiguration.make_many(
            self.boto3_raw_data["RetentionConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRetentionConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRetentionConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRetentionConfigurationResponse:
    boto3_raw_data: "type_defs.PutRetentionConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RetentionConfiguration(self):  # pragma: no cover
        return RetentionConfiguration.make_one(
            self.boto3_raw_data["RetentionConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutRetentionConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRetentionConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEvaluationsResponse:
    boto3_raw_data: "type_defs.PutEvaluationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def FailedEvaluations(self):  # pragma: no cover
        return EvaluationOutput.make_many(self.boto3_raw_data["FailedEvaluations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutEvaluationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEvaluationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationResultIdentifier:
    boto3_raw_data: "type_defs.EvaluationResultIdentifierTypeDef" = dataclasses.field()

    @cached_property
    def EvaluationResultQualifier(self):  # pragma: no cover
        return EvaluationResultQualifier.make_one(
            self.boto3_raw_data["EvaluationResultQualifier"]
        )

    OrderingTimestamp = field("OrderingTimestamp")
    ResourceEvaluationId = field("ResourceEvaluationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvaluationResultIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationResultIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Evaluation:
    boto3_raw_data: "type_defs.EvaluationTypeDef" = dataclasses.field()

    ComplianceResourceType = field("ComplianceResourceType")
    ComplianceResourceId = field("ComplianceResourceId")
    ComplianceType = field("ComplianceType")
    OrderingTimestamp = field("OrderingTimestamp")
    Annotation = field("Annotation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvaluationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EvaluationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExternalEvaluation:
    boto3_raw_data: "type_defs.ExternalEvaluationTypeDef" = dataclasses.field()

    ComplianceResourceType = field("ComplianceResourceType")
    ComplianceResourceId = field("ComplianceResourceId")
    ComplianceType = field("ComplianceType")
    OrderingTimestamp = field("OrderingTimestamp")
    Annotation = field("Annotation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExternalEvaluationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExternalEvaluationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceConfigHistoryRequestPaginate:
    boto3_raw_data: "type_defs.GetResourceConfigHistoryRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    resourceType = field("resourceType")
    resourceId = field("resourceId")
    laterTime = field("laterTime")
    earlierTime = field("earlierTime")
    chronologicalOrder = field("chronologicalOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetResourceConfigHistoryRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceConfigHistoryRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceConfigHistoryRequest:
    boto3_raw_data: "type_defs.GetResourceConfigHistoryRequestTypeDef" = (
        dataclasses.field()
    )

    resourceType = field("resourceType")
    resourceId = field("resourceId")
    laterTime = field("laterTime")
    earlierTime = field("earlierTime")
    chronologicalOrder = field("chronologicalOrder")
    limit = field("limit")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetResourceConfigHistoryRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceConfigHistoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRemediationExceptionsRequest:
    boto3_raw_data: "type_defs.PutRemediationExceptionsRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigRuleName = field("ConfigRuleName")

    @cached_property
    def ResourceKeys(self):  # pragma: no cover
        return RemediationExceptionResourceKey.make_many(
            self.boto3_raw_data["ResourceKeys"]
        )

    Message = field("Message")
    ExpirationTime = field("ExpirationTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutRemediationExceptionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRemediationExceptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeWindow:
    boto3_raw_data: "type_defs.TimeWindowTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TimeWindowTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TimeWindowTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionControls:
    boto3_raw_data: "type_defs.ExecutionControlsTypeDef" = dataclasses.field()

    @cached_property
    def SsmControls(self):  # pragma: no cover
        return SsmControls.make_one(self.boto3_raw_data["SsmControls"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExecutionControlsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecutionControlsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryInfo:
    boto3_raw_data: "type_defs.QueryInfoTypeDef" = dataclasses.field()

    @cached_property
    def SelectFields(self):  # pragma: no cover
        return FieldInfo.make_many(self.boto3_raw_data["SelectFields"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAggregateDiscoveredResourceCountsRequest:
    boto3_raw_data: "type_defs.GetAggregateDiscoveredResourceCountsRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationAggregatorName = field("ConfigurationAggregatorName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ResourceCountFilters.make_one(self.boto3_raw_data["Filters"])

    GroupByKey = field("GroupByKey")
    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAggregateDiscoveredResourceCountsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAggregateDiscoveredResourceCountsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAggregateDiscoveredResourceCountsResponse:
    boto3_raw_data: "type_defs.GetAggregateDiscoveredResourceCountsResponseTypeDef" = (
        dataclasses.field()
    )

    TotalDiscoveredResources = field("TotalDiscoveredResources")
    GroupByKey = field("GroupByKey")

    @cached_property
    def GroupedResourceCounts(self):  # pragma: no cover
        return GroupedResourceCount.make_many(
            self.boto3_raw_data["GroupedResourceCounts"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAggregateDiscoveredResourceCountsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAggregateDiscoveredResourceCountsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDiscoveredResourceCountsResponse:
    boto3_raw_data: "type_defs.GetDiscoveredResourceCountsResponseTypeDef" = (
        dataclasses.field()
    )

    totalDiscoveredResources = field("totalDiscoveredResources")

    @cached_property
    def resourceCounts(self):  # pragma: no cover
        return ResourceCount.make_many(self.boto3_raw_data["resourceCounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDiscoveredResourceCountsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDiscoveredResourceCountsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOrganizationConfigRuleDetailedStatusRequestPaginate:
    boto3_raw_data: (
        "type_defs.GetOrganizationConfigRuleDetailedStatusRequestPaginateTypeDef"
    ) = dataclasses.field()

    OrganizationConfigRuleName = field("OrganizationConfigRuleName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return StatusDetailFilters.make_one(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOrganizationConfigRuleDetailedStatusRequestPaginateTypeDef"
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
                "type_defs.GetOrganizationConfigRuleDetailedStatusRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOrganizationConfigRuleDetailedStatusRequest:
    boto3_raw_data: (
        "type_defs.GetOrganizationConfigRuleDetailedStatusRequestTypeDef"
    ) = dataclasses.field()

    OrganizationConfigRuleName = field("OrganizationConfigRuleName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return StatusDetailFilters.make_one(self.boto3_raw_data["Filters"])

    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOrganizationConfigRuleDetailedStatusRequestTypeDef"
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
                "type_defs.GetOrganizationConfigRuleDetailedStatusRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOrganizationConfigRuleDetailedStatusResponse:
    boto3_raw_data: (
        "type_defs.GetOrganizationConfigRuleDetailedStatusResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def OrganizationConfigRuleDetailedStatus(self):  # pragma: no cover
        return MemberAccountStatus.make_many(
            self.boto3_raw_data["OrganizationConfigRuleDetailedStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOrganizationConfigRuleDetailedStatusResponseTypeDef"
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
                "type_defs.GetOrganizationConfigRuleDetailedStatusResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOrganizationConformancePackDetailedStatusRequestPaginate:
    boto3_raw_data: (
        "type_defs.GetOrganizationConformancePackDetailedStatusRequestPaginateTypeDef"
    ) = dataclasses.field()

    OrganizationConformancePackName = field("OrganizationConformancePackName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return OrganizationResourceDetailedStatusFilters.make_one(
            self.boto3_raw_data["Filters"]
        )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOrganizationConformancePackDetailedStatusRequestPaginateTypeDef"
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
                "type_defs.GetOrganizationConformancePackDetailedStatusRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOrganizationConformancePackDetailedStatusRequest:
    boto3_raw_data: (
        "type_defs.GetOrganizationConformancePackDetailedStatusRequestTypeDef"
    ) = dataclasses.field()

    OrganizationConformancePackName = field("OrganizationConformancePackName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return OrganizationResourceDetailedStatusFilters.make_one(
            self.boto3_raw_data["Filters"]
        )

    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOrganizationConformancePackDetailedStatusRequestTypeDef"
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
                "type_defs.GetOrganizationConformancePackDetailedStatusRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOrganizationConformancePackDetailedStatusResponse:
    boto3_raw_data: (
        "type_defs.GetOrganizationConformancePackDetailedStatusResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def OrganizationConformancePackDetailedStatuses(self):  # pragma: no cover
        return OrganizationConformancePackDetailedStatus.make_many(
            self.boto3_raw_data["OrganizationConformancePackDetailedStatuses"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOrganizationConformancePackDetailedStatusResponseTypeDef"
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
                "type_defs.GetOrganizationConformancePackDetailedStatusResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceEvaluationSummaryResponse:
    boto3_raw_data: "type_defs.GetResourceEvaluationSummaryResponseTypeDef" = (
        dataclasses.field()
    )

    ResourceEvaluationId = field("ResourceEvaluationId")
    EvaluationMode = field("EvaluationMode")

    @cached_property
    def EvaluationStatus(self):  # pragma: no cover
        return EvaluationStatus.make_one(self.boto3_raw_data["EvaluationStatus"])

    EvaluationStartTimestamp = field("EvaluationStartTimestamp")
    Compliance = field("Compliance")

    @cached_property
    def EvaluationContext(self):  # pragma: no cover
        return EvaluationContext.make_one(self.boto3_raw_data["EvaluationContext"])

    @cached_property
    def ResourceDetails(self):  # pragma: no cover
        return ResourceDetails.make_one(self.boto3_raw_data["ResourceDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetResourceEvaluationSummaryResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceEvaluationSummaryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartResourceEvaluationRequest:
    boto3_raw_data: "type_defs.StartResourceEvaluationRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResourceDetails(self):  # pragma: no cover
        return ResourceDetails.make_one(self.boto3_raw_data["ResourceDetails"])

    EvaluationMode = field("EvaluationMode")

    @cached_property
    def EvaluationContext(self):  # pragma: no cover
        return EvaluationContext.make_one(self.boto3_raw_data["EvaluationContext"])

    EvaluationTimeout = field("EvaluationTimeout")
    ClientToken = field("ClientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartResourceEvaluationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartResourceEvaluationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStoredQueryResponse:
    boto3_raw_data: "type_defs.GetStoredQueryResponseTypeDef" = dataclasses.field()

    @cached_property
    def StoredQuery(self):  # pragma: no cover
        return StoredQuery.make_one(self.boto3_raw_data["StoredQuery"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStoredQueryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStoredQueryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAggregateDiscoveredResourcesRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListAggregateDiscoveredResourcesRequestPaginateTypeDef"
    ) = dataclasses.field()

    ConfigurationAggregatorName = field("ConfigurationAggregatorName")
    ResourceType = field("ResourceType")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ResourceFilters.make_one(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAggregateDiscoveredResourcesRequestPaginateTypeDef"
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
                "type_defs.ListAggregateDiscoveredResourcesRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAggregateDiscoveredResourcesRequest:
    boto3_raw_data: "type_defs.ListAggregateDiscoveredResourcesRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationAggregatorName = field("ConfigurationAggregatorName")
    ResourceType = field("ResourceType")

    @cached_property
    def Filters(self):  # pragma: no cover
        return ResourceFilters.make_one(self.boto3_raw_data["Filters"])

    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAggregateDiscoveredResourcesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAggregateDiscoveredResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDiscoveredResourcesResponse:
    boto3_raw_data: "type_defs.ListDiscoveredResourcesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def resourceIdentifiers(self):  # pragma: no cover
        return ResourceIdentifier.make_many(self.boto3_raw_data["resourceIdentifiers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDiscoveredResourcesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDiscoveredResourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceEvaluationsResponse:
    boto3_raw_data: "type_defs.ListResourceEvaluationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResourceEvaluations(self):  # pragma: no cover
        return ResourceEvaluation.make_many(self.boto3_raw_data["ResourceEvaluations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResourceEvaluationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceEvaluationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStoredQueriesResponse:
    boto3_raw_data: "type_defs.ListStoredQueriesResponseTypeDef" = dataclasses.field()

    @cached_property
    def StoredQueryMetadata(self):  # pragma: no cover
        return StoredQueryMetadata.make_many(self.boto3_raw_data["StoredQueryMetadata"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStoredQueriesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStoredQueriesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAggregationAuthorizationRequest:
    boto3_raw_data: "type_defs.PutAggregationAuthorizationRequestTypeDef" = (
        dataclasses.field()
    )

    AuthorizedAccountId = field("AuthorizedAccountId")
    AuthorizedAwsRegion = field("AuthorizedAwsRegion")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutAggregationAuthorizationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAggregationAuthorizationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutServiceLinkedConfigurationRecorderRequest:
    boto3_raw_data: "type_defs.PutServiceLinkedConfigurationRecorderRequestTypeDef" = (
        dataclasses.field()
    )

    ServicePrincipal = field("ServicePrincipal")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutServiceLinkedConfigurationRecorderRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutServiceLinkedConfigurationRecorderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutStoredQueryRequest:
    boto3_raw_data: "type_defs.PutStoredQueryRequestTypeDef" = dataclasses.field()

    @cached_property
    def StoredQuery(self):  # pragma: no cover
        return StoredQuery.make_one(self.boto3_raw_data["StoredQuery"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutStoredQueryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutStoredQueryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OrganizationConfigRule:
    boto3_raw_data: "type_defs.OrganizationConfigRuleTypeDef" = dataclasses.field()

    OrganizationConfigRuleName = field("OrganizationConfigRuleName")
    OrganizationConfigRuleArn = field("OrganizationConfigRuleArn")

    @cached_property
    def OrganizationManagedRuleMetadata(self):  # pragma: no cover
        return OrganizationManagedRuleMetadataOutput.make_one(
            self.boto3_raw_data["OrganizationManagedRuleMetadata"]
        )

    @cached_property
    def OrganizationCustomRuleMetadata(self):  # pragma: no cover
        return OrganizationCustomRuleMetadataOutput.make_one(
            self.boto3_raw_data["OrganizationCustomRuleMetadata"]
        )

    ExcludedAccounts = field("ExcludedAccounts")
    LastUpdateTime = field("LastUpdateTime")

    @cached_property
    def OrganizationCustomPolicyRuleMetadata(self):  # pragma: no cover
        return OrganizationCustomPolicyRuleMetadataNoPolicy.make_one(
            self.boto3_raw_data["OrganizationCustomPolicyRuleMetadata"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OrganizationConfigRuleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OrganizationConfigRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordingGroupOutput:
    boto3_raw_data: "type_defs.RecordingGroupOutputTypeDef" = dataclasses.field()

    allSupported = field("allSupported")
    includeGlobalResourceTypes = field("includeGlobalResourceTypes")
    resourceTypes = field("resourceTypes")

    @cached_property
    def exclusionByResourceTypes(self):  # pragma: no cover
        return ExclusionByResourceTypesOutput.make_one(
            self.boto3_raw_data["exclusionByResourceTypes"]
        )

    @cached_property
    def recordingStrategy(self):  # pragma: no cover
        return RecordingStrategy.make_one(self.boto3_raw_data["recordingStrategy"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecordingGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecordingGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordingGroup:
    boto3_raw_data: "type_defs.RecordingGroupTypeDef" = dataclasses.field()

    allSupported = field("allSupported")
    includeGlobalResourceTypes = field("includeGlobalResourceTypes")
    resourceTypes = field("resourceTypes")

    @cached_property
    def exclusionByResourceTypes(self):  # pragma: no cover
        return ExclusionByResourceTypes.make_one(
            self.boto3_raw_data["exclusionByResourceTypes"]
        )

    @cached_property
    def recordingStrategy(self):  # pragma: no cover
        return RecordingStrategy.make_one(self.boto3_raw_data["recordingStrategy"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecordingGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecordingGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordingModeOutput:
    boto3_raw_data: "type_defs.RecordingModeOutputTypeDef" = dataclasses.field()

    recordingFrequency = field("recordingFrequency")

    @cached_property
    def recordingModeOverrides(self):  # pragma: no cover
        return RecordingModeOverrideOutput.make_many(
            self.boto3_raw_data["recordingModeOverrides"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecordingModeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecordingModeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordingMode:
    boto3_raw_data: "type_defs.RecordingModeTypeDef" = dataclasses.field()

    recordingFrequency = field("recordingFrequency")

    @cached_property
    def recordingModeOverrides(self):  # pragma: no cover
        return RecordingModeOverride.make_many(
            self.boto3_raw_data["recordingModeOverrides"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecordingModeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecordingModeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemediationExecutionStatus:
    boto3_raw_data: "type_defs.RemediationExecutionStatusTypeDef" = dataclasses.field()

    @cached_property
    def ResourceKey(self):  # pragma: no cover
        return ResourceKey.make_one(self.boto3_raw_data["ResourceKey"])

    State = field("State")

    @cached_property
    def StepDetails(self):  # pragma: no cover
        return RemediationExecutionStep.make_many(self.boto3_raw_data["StepDetails"])

    InvocationTime = field("InvocationTime")
    LastUpdatedTime = field("LastUpdatedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemediationExecutionStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemediationExecutionStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemediationParameterValueOutput:
    boto3_raw_data: "type_defs.RemediationParameterValueOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResourceValue(self):  # pragma: no cover
        return ResourceValue.make_one(self.boto3_raw_data["ResourceValue"])

    @cached_property
    def StaticValue(self):  # pragma: no cover
        return StaticValueOutput.make_one(self.boto3_raw_data["StaticValue"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemediationParameterValueOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemediationParameterValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceOutput:
    boto3_raw_data: "type_defs.SourceOutputTypeDef" = dataclasses.field()

    Owner = field("Owner")
    SourceIdentifier = field("SourceIdentifier")

    @cached_property
    def SourceDetails(self):  # pragma: no cover
        return SourceDetail.make_many(self.boto3_raw_data["SourceDetails"])

    @cached_property
    def CustomPolicyDetails(self):  # pragma: no cover
        return CustomPolicyDetails.make_one(self.boto3_raw_data["CustomPolicyDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Source:
    boto3_raw_data: "type_defs.SourceTypeDef" = dataclasses.field()

    Owner = field("Owner")
    SourceIdentifier = field("SourceIdentifier")

    @cached_property
    def SourceDetails(self):  # pragma: no cover
        return SourceDetail.make_many(self.boto3_raw_data["SourceDetails"])

    @cached_property
    def CustomPolicyDetails(self):  # pragma: no cover
        return CustomPolicyDetails.make_one(self.boto3_raw_data["CustomPolicyDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAggregateComplianceByConformancePacksResponse:
    boto3_raw_data: (
        "type_defs.DescribeAggregateComplianceByConformancePacksResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def AggregateComplianceByConformancePacks(self):  # pragma: no cover
        return AggregateComplianceByConformancePack.make_many(
            self.boto3_raw_data["AggregateComplianceByConformancePacks"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAggregateComplianceByConformancePacksResponseTypeDef"
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
                "type_defs.DescribeAggregateComplianceByConformancePacksResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAggregateConformancePackComplianceSummaryResponse:
    boto3_raw_data: (
        "type_defs.GetAggregateConformancePackComplianceSummaryResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def AggregateConformancePackComplianceSummaries(self):  # pragma: no cover
        return AggregateConformancePackComplianceSummary.make_many(
            self.boto3_raw_data["AggregateConformancePackComplianceSummaries"]
        )

    GroupByKey = field("GroupByKey")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAggregateConformancePackComplianceSummaryResponseTypeDef"
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
                "type_defs.GetAggregateConformancePackComplianceSummaryResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationAggregator:
    boto3_raw_data: "type_defs.ConfigurationAggregatorTypeDef" = dataclasses.field()

    ConfigurationAggregatorName = field("ConfigurationAggregatorName")
    ConfigurationAggregatorArn = field("ConfigurationAggregatorArn")

    @cached_property
    def AccountAggregationSources(self):  # pragma: no cover
        return AccountAggregationSourceOutput.make_many(
            self.boto3_raw_data["AccountAggregationSources"]
        )

    @cached_property
    def OrganizationAggregationSource(self):  # pragma: no cover
        return OrganizationAggregationSourceOutput.make_one(
            self.boto3_raw_data["OrganizationAggregationSource"]
        )

    CreationTime = field("CreationTime")
    LastUpdatedTime = field("LastUpdatedTime")
    CreatedBy = field("CreatedBy")

    @cached_property
    def AggregatorFilters(self):  # pragma: no cover
        return AggregatorFiltersOutput.make_one(
            self.boto3_raw_data["AggregatorFilters"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationAggregatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationAggregatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregateComplianceCount:
    boto3_raw_data: "type_defs.AggregateComplianceCountTypeDef" = dataclasses.field()

    GroupName = field("GroupName")

    @cached_property
    def ComplianceSummary(self):  # pragma: no cover
        return ComplianceSummary.make_one(self.boto3_raw_data["ComplianceSummary"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AggregateComplianceCountTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregateComplianceCountTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComplianceSummaryByResourceType:
    boto3_raw_data: "type_defs.ComplianceSummaryByResourceTypeTypeDef" = (
        dataclasses.field()
    )

    ResourceType = field("ResourceType")

    @cached_property
    def ComplianceSummary(self):  # pragma: no cover
        return ComplianceSummary.make_one(self.boto3_raw_data["ComplianceSummary"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ComplianceSummaryByResourceTypeTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComplianceSummaryByResourceTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComplianceSummaryByConfigRuleResponse:
    boto3_raw_data: "type_defs.GetComplianceSummaryByConfigRuleResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ComplianceSummary(self):  # pragma: no cover
        return ComplianceSummary.make_one(self.boto3_raw_data["ComplianceSummary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetComplianceSummaryByConfigRuleResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComplianceSummaryByConfigRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregateComplianceByConfigRule:
    boto3_raw_data: "type_defs.AggregateComplianceByConfigRuleTypeDef" = (
        dataclasses.field()
    )

    ConfigRuleName = field("ConfigRuleName")

    @cached_property
    def Compliance(self):  # pragma: no cover
        return Compliance.make_one(self.boto3_raw_data["Compliance"])

    AccountId = field("AccountId")
    AwsRegion = field("AwsRegion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AggregateComplianceByConfigRuleTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregateComplianceByConfigRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComplianceByConfigRule:
    boto3_raw_data: "type_defs.ComplianceByConfigRuleTypeDef" = dataclasses.field()

    ConfigRuleName = field("ConfigRuleName")

    @cached_property
    def Compliance(self):  # pragma: no cover
        return Compliance.make_one(self.boto3_raw_data["Compliance"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComplianceByConfigRuleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComplianceByConfigRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComplianceByResource:
    boto3_raw_data: "type_defs.ComplianceByResourceTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    ResourceId = field("ResourceId")

    @cached_property
    def Compliance(self):  # pragma: no cover
        return Compliance.make_one(self.boto3_raw_data["Compliance"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComplianceByResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComplianceByResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDeliveryChannelsResponse:
    boto3_raw_data: "type_defs.DescribeDeliveryChannelsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DeliveryChannels(self):  # pragma: no cover
        return DeliveryChannel.make_many(self.boto3_raw_data["DeliveryChannels"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDeliveryChannelsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDeliveryChannelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutDeliveryChannelRequest:
    boto3_raw_data: "type_defs.PutDeliveryChannelRequestTypeDef" = dataclasses.field()

    @cached_property
    def DeliveryChannel(self):  # pragma: no cover
        return DeliveryChannel.make_one(self.boto3_raw_data["DeliveryChannel"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutDeliveryChannelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDeliveryChannelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDeliveryChannelStatusResponse:
    boto3_raw_data: "type_defs.DescribeDeliveryChannelStatusResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DeliveryChannelsStatus(self):  # pragma: no cover
        return DeliveryChannelStatus.make_many(
            self.boto3_raw_data["DeliveryChannelsStatus"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDeliveryChannelStatusResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDeliveryChannelStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAggregateResourceConfigResponse:
    boto3_raw_data: "type_defs.GetAggregateResourceConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConfigurationItem(self):  # pragma: no cover
        return ConfigurationItem.make_one(self.boto3_raw_data["ConfigurationItem"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAggregateResourceConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAggregateResourceConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourceConfigHistoryResponse:
    boto3_raw_data: "type_defs.GetResourceConfigHistoryResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def configurationItems(self):  # pragma: no cover
        return ConfigurationItem.make_many(self.boto3_raw_data["configurationItems"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetResourceConfigHistoryResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourceConfigHistoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationConformancePacksResponse:
    boto3_raw_data: "type_defs.DescribeOrganizationConformancePacksResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OrganizationConformancePacks(self):  # pragma: no cover
        return OrganizationConformancePack.make_many(
            self.boto3_raw_data["OrganizationConformancePacks"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrganizationConformancePacksResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOrganizationConformancePacksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConformancePacksResponse:
    boto3_raw_data: "type_defs.DescribeConformancePacksResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConformancePackDetails(self):  # pragma: no cover
        return ConformancePackDetail.make_many(
            self.boto3_raw_data["ConformancePackDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeConformancePacksResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConformancePacksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRemediationExceptionsResponse:
    boto3_raw_data: "type_defs.DeleteRemediationExceptionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FailedBatches(self):  # pragma: no cover
        return FailedDeleteRemediationExceptionsBatch.make_many(
            self.boto3_raw_data["FailedBatches"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteRemediationExceptionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRemediationExceptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRemediationExceptionsResponse:
    boto3_raw_data: "type_defs.PutRemediationExceptionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FailedBatches(self):  # pragma: no cover
        return FailedRemediationExceptionBatch.make_many(
            self.boto3_raw_data["FailedBatches"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutRemediationExceptionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRemediationExceptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregateEvaluationResult:
    boto3_raw_data: "type_defs.AggregateEvaluationResultTypeDef" = dataclasses.field()

    @cached_property
    def EvaluationResultIdentifier(self):  # pragma: no cover
        return EvaluationResultIdentifier.make_one(
            self.boto3_raw_data["EvaluationResultIdentifier"]
        )

    ComplianceType = field("ComplianceType")
    ResultRecordedTime = field("ResultRecordedTime")
    ConfigRuleInvokedTime = field("ConfigRuleInvokedTime")
    Annotation = field("Annotation")
    AccountId = field("AccountId")
    AwsRegion = field("AwsRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AggregateEvaluationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregateEvaluationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConformancePackEvaluationResult:
    boto3_raw_data: "type_defs.ConformancePackEvaluationResultTypeDef" = (
        dataclasses.field()
    )

    ComplianceType = field("ComplianceType")

    @cached_property
    def EvaluationResultIdentifier(self):  # pragma: no cover
        return EvaluationResultIdentifier.make_one(
            self.boto3_raw_data["EvaluationResultIdentifier"]
        )

    ConfigRuleInvokedTime = field("ConfigRuleInvokedTime")
    ResultRecordedTime = field("ResultRecordedTime")
    Annotation = field("Annotation")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConformancePackEvaluationResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConformancePackEvaluationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvaluationResult:
    boto3_raw_data: "type_defs.EvaluationResultTypeDef" = dataclasses.field()

    @cached_property
    def EvaluationResultIdentifier(self):  # pragma: no cover
        return EvaluationResultIdentifier.make_one(
            self.boto3_raw_data["EvaluationResultIdentifier"]
        )

    ComplianceType = field("ComplianceType")
    ResultRecordedTime = field("ResultRecordedTime")
    ConfigRuleInvokedTime = field("ConfigRuleInvokedTime")
    Annotation = field("Annotation")
    ResultToken = field("ResultToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvaluationResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvaluationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutExternalEvaluationRequest:
    boto3_raw_data: "type_defs.PutExternalEvaluationRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigRuleName = field("ConfigRuleName")

    @cached_property
    def ExternalEvaluation(self):  # pragma: no cover
        return ExternalEvaluation.make_one(self.boto3_raw_data["ExternalEvaluation"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutExternalEvaluationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutExternalEvaluationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceEvaluationFilters:
    boto3_raw_data: "type_defs.ResourceEvaluationFiltersTypeDef" = dataclasses.field()

    EvaluationMode = field("EvaluationMode")

    @cached_property
    def TimeWindow(self):  # pragma: no cover
        return TimeWindow.make_one(self.boto3_raw_data["TimeWindow"])

    EvaluationContextIdentifier = field("EvaluationContextIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceEvaluationFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceEvaluationFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelectAggregateResourceConfigResponse:
    boto3_raw_data: "type_defs.SelectAggregateResourceConfigResponseTypeDef" = (
        dataclasses.field()
    )

    Results = field("Results")

    @cached_property
    def QueryInfo(self):  # pragma: no cover
        return QueryInfo.make_one(self.boto3_raw_data["QueryInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SelectAggregateResourceConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelectAggregateResourceConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelectResourceConfigResponse:
    boto3_raw_data: "type_defs.SelectResourceConfigResponseTypeDef" = (
        dataclasses.field()
    )

    Results = field("Results")

    @cached_property
    def QueryInfo(self):  # pragma: no cover
        return QueryInfo.make_one(self.boto3_raw_data["QueryInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SelectResourceConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelectResourceConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationConfigRulesResponse:
    boto3_raw_data: "type_defs.DescribeOrganizationConfigRulesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def OrganizationConfigRules(self):  # pragma: no cover
        return OrganizationConfigRule.make_many(
            self.boto3_raw_data["OrganizationConfigRules"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrganizationConfigRulesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOrganizationConfigRulesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutOrganizationConfigRuleRequest:
    boto3_raw_data: "type_defs.PutOrganizationConfigRuleRequestTypeDef" = (
        dataclasses.field()
    )

    OrganizationConfigRuleName = field("OrganizationConfigRuleName")
    OrganizationManagedRuleMetadata = field("OrganizationManagedRuleMetadata")
    OrganizationCustomRuleMetadata = field("OrganizationCustomRuleMetadata")
    ExcludedAccounts = field("ExcludedAccounts")

    @cached_property
    def OrganizationCustomPolicyRuleMetadata(self):  # pragma: no cover
        return OrganizationCustomPolicyRuleMetadata.make_one(
            self.boto3_raw_data["OrganizationCustomPolicyRuleMetadata"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutOrganizationConfigRuleRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutOrganizationConfigRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationRecorderOutput:
    boto3_raw_data: "type_defs.ConfigurationRecorderOutputTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    roleARN = field("roleARN")

    @cached_property
    def recordingGroup(self):  # pragma: no cover
        return RecordingGroupOutput.make_one(self.boto3_raw_data["recordingGroup"])

    @cached_property
    def recordingMode(self):  # pragma: no cover
        return RecordingModeOutput.make_one(self.boto3_raw_data["recordingMode"])

    recordingScope = field("recordingScope")
    servicePrincipal = field("servicePrincipal")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationRecorderOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationRecorderOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationRecorder:
    boto3_raw_data: "type_defs.ConfigurationRecorderTypeDef" = dataclasses.field()

    arn = field("arn")
    name = field("name")
    roleARN = field("roleARN")

    @cached_property
    def recordingGroup(self):  # pragma: no cover
        return RecordingGroup.make_one(self.boto3_raw_data["recordingGroup"])

    @cached_property
    def recordingMode(self):  # pragma: no cover
        return RecordingMode.make_one(self.boto3_raw_data["recordingMode"])

    recordingScope = field("recordingScope")
    servicePrincipal = field("servicePrincipal")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationRecorderTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationRecorderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRemediationExecutionStatusResponse:
    boto3_raw_data: "type_defs.DescribeRemediationExecutionStatusResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RemediationExecutionStatuses(self):  # pragma: no cover
        return RemediationExecutionStatus.make_many(
            self.boto3_raw_data["RemediationExecutionStatuses"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRemediationExecutionStatusResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRemediationExecutionStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemediationConfigurationOutput:
    boto3_raw_data: "type_defs.RemediationConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    ConfigRuleName = field("ConfigRuleName")
    TargetType = field("TargetType")
    TargetId = field("TargetId")
    TargetVersion = field("TargetVersion")
    Parameters = field("Parameters")
    ResourceType = field("ResourceType")
    Automatic = field("Automatic")

    @cached_property
    def ExecutionControls(self):  # pragma: no cover
        return ExecutionControls.make_one(self.boto3_raw_data["ExecutionControls"])

    MaximumAutomaticAttempts = field("MaximumAutomaticAttempts")
    RetryAttemptSeconds = field("RetryAttemptSeconds")
    Arn = field("Arn")
    CreatedByService = field("CreatedByService")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemediationConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemediationConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigRuleOutput:
    boto3_raw_data: "type_defs.ConfigRuleOutputTypeDef" = dataclasses.field()

    @cached_property
    def Source(self):  # pragma: no cover
        return SourceOutput.make_one(self.boto3_raw_data["Source"])

    ConfigRuleName = field("ConfigRuleName")
    ConfigRuleArn = field("ConfigRuleArn")
    ConfigRuleId = field("ConfigRuleId")
    Description = field("Description")

    @cached_property
    def Scope(self):  # pragma: no cover
        return ScopeOutput.make_one(self.boto3_raw_data["Scope"])

    InputParameters = field("InputParameters")
    MaximumExecutionFrequency = field("MaximumExecutionFrequency")
    ConfigRuleState = field("ConfigRuleState")
    CreatedBy = field("CreatedBy")

    @cached_property
    def EvaluationModes(self):  # pragma: no cover
        return EvaluationModeConfiguration.make_many(
            self.boto3_raw_data["EvaluationModes"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConfigRuleOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigRule:
    boto3_raw_data: "type_defs.ConfigRuleTypeDef" = dataclasses.field()

    @cached_property
    def Source(self):  # pragma: no cover
        return Source.make_one(self.boto3_raw_data["Source"])

    ConfigRuleName = field("ConfigRuleName")
    ConfigRuleArn = field("ConfigRuleArn")
    ConfigRuleId = field("ConfigRuleId")
    Description = field("Description")

    @cached_property
    def Scope(self):  # pragma: no cover
        return Scope.make_one(self.boto3_raw_data["Scope"])

    InputParameters = field("InputParameters")
    MaximumExecutionFrequency = field("MaximumExecutionFrequency")
    ConfigRuleState = field("ConfigRuleState")
    CreatedBy = field("CreatedBy")

    @cached_property
    def EvaluationModes(self):  # pragma: no cover
        return EvaluationModeConfiguration.make_many(
            self.boto3_raw_data["EvaluationModes"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConfigRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConfigRuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemediationParameterValue:
    boto3_raw_data: "type_defs.RemediationParameterValueTypeDef" = dataclasses.field()

    @cached_property
    def ResourceValue(self):  # pragma: no cover
        return ResourceValue.make_one(self.boto3_raw_data["ResourceValue"])

    StaticValue = field("StaticValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemediationParameterValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemediationParameterValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigurationAggregatorsResponse:
    boto3_raw_data: "type_defs.DescribeConfigurationAggregatorsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConfigurationAggregators(self):  # pragma: no cover
        return ConfigurationAggregator.make_many(
            self.boto3_raw_data["ConfigurationAggregators"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConfigurationAggregatorsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigurationAggregatorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutConfigurationAggregatorResponse:
    boto3_raw_data: "type_defs.PutConfigurationAggregatorResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConfigurationAggregator(self):  # pragma: no cover
        return ConfigurationAggregator.make_one(
            self.boto3_raw_data["ConfigurationAggregator"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutConfigurationAggregatorResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutConfigurationAggregatorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutConfigurationAggregatorRequest:
    boto3_raw_data: "type_defs.PutConfigurationAggregatorRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationAggregatorName = field("ConfigurationAggregatorName")
    AccountAggregationSources = field("AccountAggregationSources")
    OrganizationAggregationSource = field("OrganizationAggregationSource")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    AggregatorFilters = field("AggregatorFilters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutConfigurationAggregatorRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutConfigurationAggregatorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAggregateConfigRuleComplianceSummaryResponse:
    boto3_raw_data: (
        "type_defs.GetAggregateConfigRuleComplianceSummaryResponseTypeDef"
    ) = dataclasses.field()

    GroupByKey = field("GroupByKey")

    @cached_property
    def AggregateComplianceCounts(self):  # pragma: no cover
        return AggregateComplianceCount.make_many(
            self.boto3_raw_data["AggregateComplianceCounts"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAggregateConfigRuleComplianceSummaryResponseTypeDef"
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
                "type_defs.GetAggregateConfigRuleComplianceSummaryResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComplianceSummaryByResourceTypeResponse:
    boto3_raw_data: "type_defs.GetComplianceSummaryByResourceTypeResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ComplianceSummariesByResourceType(self):  # pragma: no cover
        return ComplianceSummaryByResourceType.make_many(
            self.boto3_raw_data["ComplianceSummariesByResourceType"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetComplianceSummaryByResourceTypeResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComplianceSummaryByResourceTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAggregateComplianceByConfigRulesResponse:
    boto3_raw_data: (
        "type_defs.DescribeAggregateComplianceByConfigRulesResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def AggregateComplianceByConfigRules(self):  # pragma: no cover
        return AggregateComplianceByConfigRule.make_many(
            self.boto3_raw_data["AggregateComplianceByConfigRules"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAggregateComplianceByConfigRulesResponseTypeDef"
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
                "type_defs.DescribeAggregateComplianceByConfigRulesResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeComplianceByConfigRuleResponse:
    boto3_raw_data: "type_defs.DescribeComplianceByConfigRuleResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ComplianceByConfigRules(self):  # pragma: no cover
        return ComplianceByConfigRule.make_many(
            self.boto3_raw_data["ComplianceByConfigRules"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeComplianceByConfigRuleResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeComplianceByConfigRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeComplianceByResourceResponse:
    boto3_raw_data: "type_defs.DescribeComplianceByResourceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ComplianceByResources(self):  # pragma: no cover
        return ComplianceByResource.make_many(
            self.boto3_raw_data["ComplianceByResources"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeComplianceByResourceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeComplianceByResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAggregateComplianceDetailsByConfigRuleResponse:
    boto3_raw_data: (
        "type_defs.GetAggregateComplianceDetailsByConfigRuleResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def AggregateEvaluationResults(self):  # pragma: no cover
        return AggregateEvaluationResult.make_many(
            self.boto3_raw_data["AggregateEvaluationResults"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetAggregateComplianceDetailsByConfigRuleResponseTypeDef"
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
                "type_defs.GetAggregateComplianceDetailsByConfigRuleResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConformancePackComplianceDetailsResponse:
    boto3_raw_data: "type_defs.GetConformancePackComplianceDetailsResponseTypeDef" = (
        dataclasses.field()
    )

    ConformancePackName = field("ConformancePackName")

    @cached_property
    def ConformancePackRuleEvaluationResults(self):  # pragma: no cover
        return ConformancePackEvaluationResult.make_many(
            self.boto3_raw_data["ConformancePackRuleEvaluationResults"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConformancePackComplianceDetailsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConformancePackComplianceDetailsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComplianceDetailsByConfigRuleResponse:
    boto3_raw_data: "type_defs.GetComplianceDetailsByConfigRuleResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EvaluationResults(self):  # pragma: no cover
        return EvaluationResult.make_many(self.boto3_raw_data["EvaluationResults"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetComplianceDetailsByConfigRuleResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComplianceDetailsByConfigRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetComplianceDetailsByResourceResponse:
    boto3_raw_data: "type_defs.GetComplianceDetailsByResourceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EvaluationResults(self):  # pragma: no cover
        return EvaluationResult.make_many(self.boto3_raw_data["EvaluationResults"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetComplianceDetailsByResourceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetComplianceDetailsByResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEvaluationsRequest:
    boto3_raw_data: "type_defs.PutEvaluationsRequestTypeDef" = dataclasses.field()

    ResultToken = field("ResultToken")
    Evaluations = field("Evaluations")
    TestMode = field("TestMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutEvaluationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEvaluationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceEvaluationsRequestPaginate:
    boto3_raw_data: "type_defs.ListResourceEvaluationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return ResourceEvaluationFilters.make_one(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceEvaluationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceEvaluationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceEvaluationsRequest:
    boto3_raw_data: "type_defs.ListResourceEvaluationsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return ResourceEvaluationFilters.make_one(self.boto3_raw_data["Filters"])

    Limit = field("Limit")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResourceEvaluationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceEvaluationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateResourceTypesResponse:
    boto3_raw_data: "type_defs.AssociateResourceTypesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConfigurationRecorder(self):  # pragma: no cover
        return ConfigurationRecorderOutput.make_one(
            self.boto3_raw_data["ConfigurationRecorder"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateResourceTypesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateResourceTypesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigurationRecordersResponse:
    boto3_raw_data: "type_defs.DescribeConfigurationRecordersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConfigurationRecorders(self):  # pragma: no cover
        return ConfigurationRecorderOutput.make_many(
            self.boto3_raw_data["ConfigurationRecorders"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConfigurationRecordersResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigurationRecordersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateResourceTypesResponse:
    boto3_raw_data: "type_defs.DisassociateResourceTypesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConfigurationRecorder(self):  # pragma: no cover
        return ConfigurationRecorderOutput.make_one(
            self.boto3_raw_data["ConfigurationRecorder"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateResourceTypesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateResourceTypesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRemediationConfigurationsResponse:
    boto3_raw_data: "type_defs.DescribeRemediationConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RemediationConfigurations(self):  # pragma: no cover
        return RemediationConfigurationOutput.make_many(
            self.boto3_raw_data["RemediationConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeRemediationConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRemediationConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailedRemediationBatch:
    boto3_raw_data: "type_defs.FailedRemediationBatchTypeDef" = dataclasses.field()

    FailureMessage = field("FailureMessage")

    @cached_property
    def FailedItems(self):  # pragma: no cover
        return RemediationConfigurationOutput.make_many(
            self.boto3_raw_data["FailedItems"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FailedRemediationBatchTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FailedRemediationBatchTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigRulesResponse:
    boto3_raw_data: "type_defs.DescribeConfigRulesResponseTypeDef" = dataclasses.field()

    @cached_property
    def ConfigRules(self):  # pragma: no cover
        return ConfigRuleOutput.make_many(self.boto3_raw_data["ConfigRules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeConfigRulesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigRulesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutConfigurationRecorderRequest:
    boto3_raw_data: "type_defs.PutConfigurationRecorderRequestTypeDef" = (
        dataclasses.field()
    )

    ConfigurationRecorder = field("ConfigurationRecorder")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutConfigurationRecorderRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutConfigurationRecorderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRemediationConfigurationsResponse:
    boto3_raw_data: "type_defs.PutRemediationConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def FailedBatches(self):  # pragma: no cover
        return FailedRemediationBatch.make_many(self.boto3_raw_data["FailedBatches"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutRemediationConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRemediationConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutConfigRuleRequest:
    boto3_raw_data: "type_defs.PutConfigRuleRequestTypeDef" = dataclasses.field()

    ConfigRule = field("ConfigRule")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutConfigRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutConfigRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemediationConfiguration:
    boto3_raw_data: "type_defs.RemediationConfigurationTypeDef" = dataclasses.field()

    ConfigRuleName = field("ConfigRuleName")
    TargetType = field("TargetType")
    TargetId = field("TargetId")
    TargetVersion = field("TargetVersion")
    Parameters = field("Parameters")
    ResourceType = field("ResourceType")
    Automatic = field("Automatic")

    @cached_property
    def ExecutionControls(self):  # pragma: no cover
        return ExecutionControls.make_one(self.boto3_raw_data["ExecutionControls"])

    MaximumAutomaticAttempts = field("MaximumAutomaticAttempts")
    RetryAttemptSeconds = field("RetryAttemptSeconds")
    Arn = field("Arn")
    CreatedByService = field("CreatedByService")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemediationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemediationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRemediationConfigurationsRequest:
    boto3_raw_data: "type_defs.PutRemediationConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    RemediationConfigurations = field("RemediationConfigurations")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutRemediationConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRemediationConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
