# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_datazone import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AcceptChoice:
    boto3_raw_data: "type_defs.AcceptChoiceTypeDef" = dataclasses.field()

    predictionTarget = field("predictionTarget")
    editedValue = field("editedValue")
    predictionChoice = field("predictionChoice")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AcceptChoiceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AcceptChoiceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptRule:
    boto3_raw_data: "type_defs.AcceptRuleTypeDef" = dataclasses.field()

    rule = field("rule")
    threshold = field("threshold")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AcceptRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AcceptRuleTypeDef"]]
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
class AcceptedAssetScope:
    boto3_raw_data: "type_defs.AcceptedAssetScopeTypeDef" = dataclasses.field()

    assetId = field("assetId")
    filterIds = field("filterIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AcceptedAssetScopeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptedAssetScopeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormOutput:
    boto3_raw_data: "type_defs.FormOutputTypeDef" = dataclasses.field()

    formName = field("formName")
    content = field("content")
    typeName = field("typeName")
    typeRevision = field("typeRevision")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FormOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FormOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountInfoOutput:
    boto3_raw_data: "type_defs.AccountInfoOutputTypeDef" = dataclasses.field()

    awsAccountId = field("awsAccountId")
    supportedRegions = field("supportedRegions")
    awsAccountName = field("awsAccountName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountInfoOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountInfoOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountInfo:
    boto3_raw_data: "type_defs.AccountInfoTypeDef" = dataclasses.field()

    awsAccountId = field("awsAccountId")
    supportedRegions = field("supportedRegions")
    awsAccountName = field("awsAccountName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountPoolSummary:
    boto3_raw_data: "type_defs.AccountPoolSummaryTypeDef" = dataclasses.field()

    createdBy = field("createdBy")
    domainId = field("domainId")
    domainUnitId = field("domainUnitId")
    id = field("id")
    name = field("name")
    resolutionStrategy = field("resolutionStrategy")
    updatedBy = field("updatedBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccountPoolSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountPoolSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomAccountPoolHandler:
    boto3_raw_data: "type_defs.CustomAccountPoolHandlerTypeDef" = dataclasses.field()

    lambdaFunctionArn = field("lambdaFunctionArn")
    lambdaExecutionRoleArn = field("lambdaExecutionRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomAccountPoolHandlerTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomAccountPoolHandlerTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsConsoleLinkParameters:
    boto3_raw_data: "type_defs.AwsConsoleLinkParametersTypeDef" = dataclasses.field()

    uri = field("uri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AwsConsoleLinkParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AwsConsoleLinkParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddToProjectMemberPoolPolicyGrantDetail:
    boto3_raw_data: "type_defs.AddToProjectMemberPoolPolicyGrantDetailTypeDef" = (
        dataclasses.field()
    )

    includeChildDomainUnits = field("includeChildDomainUnits")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AddToProjectMemberPoolPolicyGrantDetailTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddToProjectMemberPoolPolicyGrantDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregationListItem:
    boto3_raw_data: "type_defs.AggregationListItemTypeDef" = dataclasses.field()

    attribute = field("attribute")
    displayValue = field("displayValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AggregationListItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregationListItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregationOutputItem:
    boto3_raw_data: "type_defs.AggregationOutputItemTypeDef" = dataclasses.field()

    count = field("count")
    displayValue = field("displayValue")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AggregationOutputItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregationOutputItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ColumnFilterConfigurationOutput:
    boto3_raw_data: "type_defs.ColumnFilterConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    includedColumnNames = field("includedColumnNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ColumnFilterConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ColumnFilterConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ColumnFilterConfiguration:
    boto3_raw_data: "type_defs.ColumnFilterConfigurationTypeDef" = dataclasses.field()

    includedColumnNames = field("includedColumnNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ColumnFilterConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ColumnFilterConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetFilterSummary:
    boto3_raw_data: "type_defs.AssetFilterSummaryTypeDef" = dataclasses.field()

    assetId = field("assetId")
    domainId = field("domainId")
    id = field("id")
    name = field("name")
    createdAt = field("createdAt")
    description = field("description")
    effectiveColumnNames = field("effectiveColumnNames")
    effectiveRowFilter = field("effectiveRowFilter")
    errorMessage = field("errorMessage")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetFilterSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetFilterSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetInDataProductListingItem:
    boto3_raw_data: "type_defs.AssetInDataProductListingItemTypeDef" = (
        dataclasses.field()
    )

    entityId = field("entityId")
    entityRevision = field("entityRevision")
    entityType = field("entityType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssetInDataProductListingItemTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetInDataProductListingItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeSeriesDataPointSummaryFormOutput:
    boto3_raw_data: "type_defs.TimeSeriesDataPointSummaryFormOutputTypeDef" = (
        dataclasses.field()
    )

    formName = field("formName")
    timestamp = field("timestamp")
    typeIdentifier = field("typeIdentifier")
    contentSummary = field("contentSummary")
    id = field("id")
    typeRevision = field("typeRevision")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TimeSeriesDataPointSummaryFormOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeSeriesDataPointSummaryFormOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetListingDetails:
    boto3_raw_data: "type_defs.AssetListingDetailsTypeDef" = dataclasses.field()

    listingId = field("listingId")
    listingStatus = field("listingStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetListingDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetListingDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetailedGlossaryTerm:
    boto3_raw_data: "type_defs.DetailedGlossaryTermTypeDef" = dataclasses.field()

    name = field("name")
    shortDescription = field("shortDescription")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetailedGlossaryTermTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetailedGlossaryTermTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetRevision:
    boto3_raw_data: "type_defs.AssetRevisionTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    domainId = field("domainId")
    id = field("id")
    revision = field("revision")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetRevisionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssetRevisionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetScope:
    boto3_raw_data: "type_defs.AssetScopeTypeDef" = dataclasses.field()

    assetId = field("assetId")
    filterIds = field("filterIds")
    status = field("status")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetScopeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssetScopeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetTargetNameMap:
    boto3_raw_data: "type_defs.AssetTargetNameMapTypeDef" = dataclasses.field()

    assetId = field("assetId")
    targetName = field("targetName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetTargetNameMapTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetTargetNameMapTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormEntryOutput:
    boto3_raw_data: "type_defs.FormEntryOutputTypeDef" = dataclasses.field()

    typeName = field("typeName")
    typeRevision = field("typeRevision")
    required = field("required")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FormEntryOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FormEntryOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetTypesForRuleOutput:
    boto3_raw_data: "type_defs.AssetTypesForRuleOutputTypeDef" = dataclasses.field()

    selectionMode = field("selectionMode")
    specificAssetTypes = field("specificAssetTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetTypesForRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetTypesForRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetTypesForRule:
    boto3_raw_data: "type_defs.AssetTypesForRuleTypeDef" = dataclasses.field()

    selectionMode = field("selectionMode")
    specificAssetTypes = field("specificAssetTypes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetTypesForRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetTypesForRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateEnvironmentRoleInput:
    boto3_raw_data: "type_defs.AssociateEnvironmentRoleInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    environmentIdentifier = field("environmentIdentifier")
    environmentRoleArn = field("environmentRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateEnvironmentRoleInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateEnvironmentRoleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateGovernedTermsInput:
    boto3_raw_data: "type_defs.AssociateGovernedTermsInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    entityIdentifier = field("entityIdentifier")
    entityType = field("entityType")
    governedGlossaryTerms = field("governedGlossaryTerms")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateGovernedTermsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateGovernedTermsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AthenaPropertiesInput:
    boto3_raw_data: "type_defs.AthenaPropertiesInputTypeDef" = dataclasses.field()

    workgroupName = field("workgroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AthenaPropertiesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AthenaPropertiesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AthenaPropertiesOutput:
    boto3_raw_data: "type_defs.AthenaPropertiesOutputTypeDef" = dataclasses.field()

    workgroupName = field("workgroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AthenaPropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AthenaPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AthenaPropertiesPatch:
    boto3_raw_data: "type_defs.AthenaPropertiesPatchTypeDef" = dataclasses.field()

    workgroupName = field("workgroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AthenaPropertiesPatchTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AthenaPropertiesPatchTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BasicAuthenticationCredentials:
    boto3_raw_data: "type_defs.BasicAuthenticationCredentialsTypeDef" = (
        dataclasses.field()
    )

    password = field("password")
    userName = field("userName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BasicAuthenticationCredentialsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BasicAuthenticationCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizationCodeProperties:
    boto3_raw_data: "type_defs.AuthorizationCodePropertiesTypeDef" = dataclasses.field()

    authorizationCode = field("authorizationCode")
    redirectUri = field("redirectUri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthorizationCodePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizationCodePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsAccount:
    boto3_raw_data: "type_defs.AwsAccountTypeDef" = dataclasses.field()

    awsAccountId = field("awsAccountId")
    awsAccountIdPath = field("awsAccountIdPath")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AwsAccountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AwsAccountTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AwsLocation:
    boto3_raw_data: "type_defs.AwsLocationTypeDef" = dataclasses.field()

    accessRole = field("accessRole")
    awsAccountId = field("awsAccountId")
    awsRegion = field("awsRegion")
    iamConnectionId = field("iamConnectionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AwsLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AwsLocationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BusinessNameGenerationConfiguration:
    boto3_raw_data: "type_defs.BusinessNameGenerationConfigurationTypeDef" = (
        dataclasses.field()
    )

    enabled = field("enabled")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BusinessNameGenerationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BusinessNameGenerationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelMetadataGenerationRunInput:
    boto3_raw_data: "type_defs.CancelMetadataGenerationRunInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CancelMetadataGenerationRunInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelMetadataGenerationRunInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelSubscriptionInput:
    boto3_raw_data: "type_defs.CancelSubscriptionInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelSubscriptionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelSubscriptionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudFormationProperties:
    boto3_raw_data: "type_defs.CloudFormationPropertiesTypeDef" = dataclasses.field()

    templateUrl = field("templateUrl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudFormationPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudFormationPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurableActionParameter:
    boto3_raw_data: "type_defs.ConfigurableActionParameterTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurableActionParameterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurableActionParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionCredentials:
    boto3_raw_data: "type_defs.ConnectionCredentialsTypeDef" = dataclasses.field()

    accessKeyId = field("accessKeyId")
    expiration = field("expiration")
    secretAccessKey = field("secretAccessKey")
    sessionToken = field("sessionToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectionCredentialsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HyperPodPropertiesInput:
    boto3_raw_data: "type_defs.HyperPodPropertiesInputTypeDef" = dataclasses.field()

    clusterName = field("clusterName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HyperPodPropertiesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HyperPodPropertiesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IamPropertiesInput:
    boto3_raw_data: "type_defs.IamPropertiesInputTypeDef" = dataclasses.field()

    glueLineageSyncEnabled = field("glueLineageSyncEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IamPropertiesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IamPropertiesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3PropertiesInput:
    boto3_raw_data: "type_defs.S3PropertiesInputTypeDef" = dataclasses.field()

    s3Uri = field("s3Uri")
    s3AccessGrantLocationId = field("s3AccessGrantLocationId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3PropertiesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3PropertiesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SparkEmrPropertiesInput:
    boto3_raw_data: "type_defs.SparkEmrPropertiesInputTypeDef" = dataclasses.field()

    computeArn = field("computeArn")
    instanceProfileArn = field("instanceProfileArn")
    javaVirtualEnv = field("javaVirtualEnv")
    logUri = field("logUri")
    pythonVirtualEnv = field("pythonVirtualEnv")
    runtimeRole = field("runtimeRole")
    trustedCertificatesS3Uri = field("trustedCertificatesS3Uri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SparkEmrPropertiesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SparkEmrPropertiesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GluePropertiesOutput:
    boto3_raw_data: "type_defs.GluePropertiesOutputTypeDef" = dataclasses.field()

    errorMessage = field("errorMessage")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GluePropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GluePropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HyperPodPropertiesOutput:
    boto3_raw_data: "type_defs.HyperPodPropertiesOutputTypeDef" = dataclasses.field()

    clusterName = field("clusterName")
    clusterArn = field("clusterArn")
    orchestrator = field("orchestrator")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HyperPodPropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HyperPodPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IamPropertiesOutput:
    boto3_raw_data: "type_defs.IamPropertiesOutputTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    glueLineageSyncEnabled = field("glueLineageSyncEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IamPropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IamPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3PropertiesOutput:
    boto3_raw_data: "type_defs.S3PropertiesOutputTypeDef" = dataclasses.field()

    s3Uri = field("s3Uri")
    errorMessage = field("errorMessage")
    s3AccessGrantLocationId = field("s3AccessGrantLocationId")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3PropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3PropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IamPropertiesPatch:
    boto3_raw_data: "type_defs.IamPropertiesPatchTypeDef" = dataclasses.field()

    glueLineageSyncEnabled = field("glueLineageSyncEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IamPropertiesPatchTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IamPropertiesPatchTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3PropertiesPatch:
    boto3_raw_data: "type_defs.S3PropertiesPatchTypeDef" = dataclasses.field()

    s3Uri = field("s3Uri")
    s3AccessGrantLocationId = field("s3AccessGrantLocationId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3PropertiesPatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3PropertiesPatchTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SparkEmrPropertiesPatch:
    boto3_raw_data: "type_defs.SparkEmrPropertiesPatchTypeDef" = dataclasses.field()

    computeArn = field("computeArn")
    instanceProfileArn = field("instanceProfileArn")
    javaVirtualEnv = field("javaVirtualEnv")
    logUri = field("logUri")
    pythonVirtualEnv = field("pythonVirtualEnv")
    runtimeRole = field("runtimeRole")
    trustedCertificatesS3Uri = field("trustedCertificatesS3Uri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SparkEmrPropertiesPatchTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SparkEmrPropertiesPatchTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormInput:
    boto3_raw_data: "type_defs.FormInputTypeDef" = dataclasses.field()

    formName = field("formName")
    content = field("content")
    typeIdentifier = field("typeIdentifier")
    typeRevision = field("typeRevision")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FormInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FormInputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormEntryInput:
    boto3_raw_data: "type_defs.FormEntryInputTypeDef" = dataclasses.field()

    typeIdentifier = field("typeIdentifier")
    typeRevision = field("typeRevision")
    required = field("required")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FormEntryInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FormEntryInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssetTypePolicyGrantDetail:
    boto3_raw_data: "type_defs.CreateAssetTypePolicyGrantDetailTypeDef" = (
        dataclasses.field()
    )

    includeChildDomainUnits = field("includeChildDomainUnits")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAssetTypePolicyGrantDetailTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssetTypePolicyGrantDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProductItemOutput:
    boto3_raw_data: "type_defs.DataProductItemOutputTypeDef" = dataclasses.field()

    identifier = field("identifier")
    itemType = field("itemType")
    glossaryTerms = field("glossaryTerms")
    revision = field("revision")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataProductItemOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataProductItemOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecommendationConfiguration:
    boto3_raw_data: "type_defs.RecommendationConfigurationTypeDef" = dataclasses.field()

    enableBusinessNameGeneration = field("enableBusinessNameGeneration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecommendationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecommendationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduleConfiguration:
    boto3_raw_data: "type_defs.ScheduleConfigurationTypeDef" = dataclasses.field()

    schedule = field("schedule")
    timezone = field("timezone")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduleConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduleConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceErrorMessage:
    boto3_raw_data: "type_defs.DataSourceErrorMessageTypeDef" = dataclasses.field()

    errorType = field("errorType")
    errorDetail = field("errorDetail")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataSourceErrorMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceErrorMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SingleSignOn:
    boto3_raw_data: "type_defs.SingleSignOnTypeDef" = dataclasses.field()

    idcInstanceArn = field("idcInstanceArn")
    type = field("type")
    userAssignment = field("userAssignment")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SingleSignOnTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SingleSignOnTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainUnitInput:
    boto3_raw_data: "type_defs.CreateDomainUnitInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    name = field("name")
    parentDomainUnitIdentifier = field("parentDomainUnitIdentifier")
    clientToken = field("clientToken")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDomainUnitInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainUnitInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainUnitPolicyGrantDetail:
    boto3_raw_data: "type_defs.CreateDomainUnitPolicyGrantDetailTypeDef" = (
        dataclasses.field()
    )

    includeChildDomainUnits = field("includeChildDomainUnits")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateDomainUnitPolicyGrantDetailTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainUnitPolicyGrantDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomParameter:
    boto3_raw_data: "type_defs.CustomParameterTypeDef" = dataclasses.field()

    fieldType = field("fieldType")
    keyName = field("keyName")
    defaultValue = field("defaultValue")
    description = field("description")
    isEditable = field("isEditable")
    isOptional = field("isOptional")
    isUpdateSupported = field("isUpdateSupported")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomParameterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomParameterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentProperties:
    boto3_raw_data: "type_defs.DeploymentPropertiesTypeDef" = dataclasses.field()

    endTimeoutMinutes = field("endTimeoutMinutes")
    startTimeoutMinutes = field("startTimeoutMinutes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeploymentPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentParameter:
    boto3_raw_data: "type_defs.EnvironmentParameterTypeDef" = dataclasses.field()

    name = field("name")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentParameterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentParameterTypeDef"]
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

    type = field("type")
    value = field("value")
    name = field("name")
    provider = field("provider")

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
class CreateEnvironmentProfilePolicyGrantDetail:
    boto3_raw_data: "type_defs.CreateEnvironmentProfilePolicyGrantDetailTypeDef" = (
        dataclasses.field()
    )

    domainUnitId = field("domainUnitId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateEnvironmentProfilePolicyGrantDetailTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentProfilePolicyGrantDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Model:
    boto3_raw_data: "type_defs.ModelTypeDef" = dataclasses.field()

    smithy = field("smithy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ModelTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ModelTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFormTypePolicyGrantDetail:
    boto3_raw_data: "type_defs.CreateFormTypePolicyGrantDetailTypeDef" = (
        dataclasses.field()
    )

    includeChildDomainUnits = field("includeChildDomainUnits")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateFormTypePolicyGrantDetailTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFormTypePolicyGrantDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGlossaryInput:
    boto3_raw_data: "type_defs.CreateGlossaryInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    name = field("name")
    owningProjectIdentifier = field("owningProjectIdentifier")
    clientToken = field("clientToken")
    description = field("description")
    status = field("status")
    usageRestrictions = field("usageRestrictions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGlossaryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGlossaryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGlossaryPolicyGrantDetail:
    boto3_raw_data: "type_defs.CreateGlossaryPolicyGrantDetailTypeDef" = (
        dataclasses.field()
    )

    includeChildDomainUnits = field("includeChildDomainUnits")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateGlossaryPolicyGrantDetailTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGlossaryPolicyGrantDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TermRelationsOutput:
    boto3_raw_data: "type_defs.TermRelationsOutputTypeDef" = dataclasses.field()

    classifies = field("classifies")
    isA = field("isA")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TermRelationsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TermRelationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGroupProfileInput:
    boto3_raw_data: "type_defs.CreateGroupProfileInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    groupIdentifier = field("groupIdentifier")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGroupProfileInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGroupProfileInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateListingChangeSetInput:
    boto3_raw_data: "type_defs.CreateListingChangeSetInputTypeDef" = dataclasses.field()

    action = field("action")
    domainIdentifier = field("domainIdentifier")
    entityIdentifier = field("entityIdentifier")
    entityType = field("entityType")
    clientToken = field("clientToken")
    entityRevision = field("entityRevision")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateListingChangeSetInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateListingChangeSetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProjectFromProjectProfilePolicyGrantDetailOutput:
    boto3_raw_data: (
        "type_defs.CreateProjectFromProjectProfilePolicyGrantDetailOutputTypeDef"
    ) = dataclasses.field()

    includeChildDomainUnits = field("includeChildDomainUnits")
    projectProfiles = field("projectProfiles")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateProjectFromProjectProfilePolicyGrantDetailOutputTypeDef"
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
                "type_defs.CreateProjectFromProjectProfilePolicyGrantDetailOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProjectFromProjectProfilePolicyGrantDetail:
    boto3_raw_data: (
        "type_defs.CreateProjectFromProjectProfilePolicyGrantDetailTypeDef"
    ) = dataclasses.field()

    includeChildDomainUnits = field("includeChildDomainUnits")
    projectProfiles = field("projectProfiles")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateProjectFromProjectProfilePolicyGrantDetailTypeDef"
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
                "type_defs.CreateProjectFromProjectProfilePolicyGrantDetailTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Member:
    boto3_raw_data: "type_defs.MemberTypeDef" = dataclasses.field()

    groupIdentifier = field("groupIdentifier")
    userIdentifier = field("userIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MemberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MemberTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectDeletionError:
    boto3_raw_data: "type_defs.ProjectDeletionErrorTypeDef" = dataclasses.field()

    code = field("code")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProjectDeletionErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProjectDeletionErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProjectPolicyGrantDetail:
    boto3_raw_data: "type_defs.CreateProjectPolicyGrantDetailTypeDef" = (
        dataclasses.field()
    )

    includeChildDomainUnits = field("includeChildDomainUnits")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateProjectPolicyGrantDetailTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProjectPolicyGrantDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscribedListingInput:
    boto3_raw_data: "type_defs.SubscribedListingInputTypeDef" = dataclasses.field()

    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubscribedListingInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscribedListingInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscriptionTargetForm:
    boto3_raw_data: "type_defs.SubscriptionTargetFormTypeDef" = dataclasses.field()

    content = field("content")
    formName = field("formName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubscriptionTargetFormTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscriptionTargetFormTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserProfileInput:
    boto3_raw_data: "type_defs.CreateUserProfileInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    userIdentifier = field("userIdentifier")
    clientToken = field("clientToken")
    userType = field("userType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUserProfileInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserProfileInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProductItem:
    boto3_raw_data: "type_defs.DataProductItemTypeDef" = dataclasses.field()

    identifier = field("identifier")
    itemType = field("itemType")
    glossaryTerms = field("glossaryTerms")
    revision = field("revision")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataProductItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataProductItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProductRevision:
    boto3_raw_data: "type_defs.DataProductRevisionTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    domainId = field("domainId")
    id = field("id")
    revision = field("revision")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataProductRevisionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataProductRevisionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SageMakerRunConfigurationInput:
    boto3_raw_data: "type_defs.SageMakerRunConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    trackingAssets = field("trackingAssets")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SageMakerRunConfigurationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SageMakerRunConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SageMakerRunConfigurationOutput:
    boto3_raw_data: "type_defs.SageMakerRunConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    trackingAssets = field("trackingAssets")
    accountId = field("accountId")
    region = field("region")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SageMakerRunConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SageMakerRunConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LineageInfo:
    boto3_raw_data: "type_defs.LineageInfoTypeDef" = dataclasses.field()

    errorMessage = field("errorMessage")
    eventId = field("eventId")
    eventStatus = field("eventStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LineageInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LineageInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceRunLineageSummary:
    boto3_raw_data: "type_defs.DataSourceRunLineageSummaryTypeDef" = dataclasses.field()

    importStatus = field("importStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataSourceRunLineageSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceRunLineageSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RunStatisticsForAssets:
    boto3_raw_data: "type_defs.RunStatisticsForAssetsTypeDef" = dataclasses.field()

    added = field("added")
    failed = field("failed")
    skipped = field("skipped")
    unchanged = field("unchanged")
    updated = field("updated")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RunStatisticsForAssetsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RunStatisticsForAssetsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccountPoolInput:
    boto3_raw_data: "type_defs.DeleteAccountPoolInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAccountPoolInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccountPoolInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAssetFilterInput:
    boto3_raw_data: "type_defs.DeleteAssetFilterInputTypeDef" = dataclasses.field()

    assetIdentifier = field("assetIdentifier")
    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAssetFilterInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAssetFilterInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAssetInput:
    boto3_raw_data: "type_defs.DeleteAssetInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteAssetInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAssetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAssetTypeInput:
    boto3_raw_data: "type_defs.DeleteAssetTypeInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAssetTypeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAssetTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConnectionInput:
    boto3_raw_data: "type_defs.DeleteConnectionInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConnectionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConnectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataProductInput:
    boto3_raw_data: "type_defs.DeleteDataProductInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDataProductInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataProductInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataSourceInput:
    boto3_raw_data: "type_defs.DeleteDataSourceInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    clientToken = field("clientToken")
    retainPermissionsOnRevokeFailure = field("retainPermissionsOnRevokeFailure")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDataSourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataSourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainInput:
    boto3_raw_data: "type_defs.DeleteDomainInputTypeDef" = dataclasses.field()

    identifier = field("identifier")
    clientToken = field("clientToken")
    skipDeletionCheck = field("skipDeletionCheck")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteDomainInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainUnitInput:
    boto3_raw_data: "type_defs.DeleteDomainUnitInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDomainUnitInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainUnitInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEnvironmentActionInput:
    boto3_raw_data: "type_defs.DeleteEnvironmentActionInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    environmentIdentifier = field("environmentIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEnvironmentActionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEnvironmentActionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEnvironmentBlueprintConfigurationInput:
    boto3_raw_data: "type_defs.DeleteEnvironmentBlueprintConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    environmentBlueprintIdentifier = field("environmentBlueprintIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteEnvironmentBlueprintConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEnvironmentBlueprintConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEnvironmentBlueprintInput:
    boto3_raw_data: "type_defs.DeleteEnvironmentBlueprintInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteEnvironmentBlueprintInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEnvironmentBlueprintInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEnvironmentInput:
    boto3_raw_data: "type_defs.DeleteEnvironmentInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEnvironmentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEnvironmentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEnvironmentProfileInput:
    boto3_raw_data: "type_defs.DeleteEnvironmentProfileInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteEnvironmentProfileInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEnvironmentProfileInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFormTypeInput:
    boto3_raw_data: "type_defs.DeleteFormTypeInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    formTypeIdentifier = field("formTypeIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFormTypeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFormTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGlossaryInput:
    boto3_raw_data: "type_defs.DeleteGlossaryInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGlossaryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGlossaryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGlossaryTermInput:
    boto3_raw_data: "type_defs.DeleteGlossaryTermInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGlossaryTermInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGlossaryTermInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteListingInput:
    boto3_raw_data: "type_defs.DeleteListingInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteListingInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteListingInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProjectInput:
    boto3_raw_data: "type_defs.DeleteProjectInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    skipDeletionCheck = field("skipDeletionCheck")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProjectInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProjectInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProjectProfileInput:
    boto3_raw_data: "type_defs.DeleteProjectProfileInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProjectProfileInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProjectProfileInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRuleInput:
    boto3_raw_data: "type_defs.DeleteRuleInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteRuleInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeleteRuleInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSubscriptionGrantInput:
    boto3_raw_data: "type_defs.DeleteSubscriptionGrantInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSubscriptionGrantInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSubscriptionGrantInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSubscriptionRequestInput:
    boto3_raw_data: "type_defs.DeleteSubscriptionRequestInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteSubscriptionRequestInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSubscriptionRequestInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSubscriptionTargetInput:
    boto3_raw_data: "type_defs.DeleteSubscriptionTargetInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    environmentIdentifier = field("environmentIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteSubscriptionTargetInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSubscriptionTargetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTimeSeriesDataPointsInput:
    boto3_raw_data: "type_defs.DeleteTimeSeriesDataPointsInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    entityIdentifier = field("entityIdentifier")
    entityType = field("entityType")
    formName = field("formName")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteTimeSeriesDataPointsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTimeSeriesDataPointsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentError:
    boto3_raw_data: "type_defs.EnvironmentErrorTypeDef" = dataclasses.field()

    message = field("message")
    code = field("code")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnvironmentErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateEnvironmentRoleInput:
    boto3_raw_data: "type_defs.DisassociateEnvironmentRoleInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    environmentIdentifier = field("environmentIdentifier")
    environmentRoleArn = field("environmentRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateEnvironmentRoleInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateEnvironmentRoleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateGovernedTermsInput:
    boto3_raw_data: "type_defs.DisassociateGovernedTermsInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    entityIdentifier = field("entityIdentifier")
    entityType = field("entityType")
    governedGlossaryTerms = field("governedGlossaryTerms")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateGovernedTermsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateGovernedTermsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainSummary:
    boto3_raw_data: "type_defs.DomainSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    id = field("id")
    managedAccountId = field("managedAccountId")
    name = field("name")
    status = field("status")
    description = field("description")
    domainVersion = field("domainVersion")
    lastUpdatedAt = field("lastUpdatedAt")
    portalUrl = field("portalUrl")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainUnitFilterForProject:
    boto3_raw_data: "type_defs.DomainUnitFilterForProjectTypeDef" = dataclasses.field()

    domainUnit = field("domainUnit")
    includeChildDomainUnits = field("includeChildDomainUnits")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainUnitFilterForProjectTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainUnitFilterForProjectTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainUnitGrantFilterOutput:
    boto3_raw_data: "type_defs.DomainUnitGrantFilterOutputTypeDef" = dataclasses.field()

    allDomainUnitsGrantFilter = field("allDomainUnitsGrantFilter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainUnitGrantFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainUnitGrantFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainUnitGrantFilter:
    boto3_raw_data: "type_defs.DomainUnitGrantFilterTypeDef" = dataclasses.field()

    allDomainUnitsGrantFilter = field("allDomainUnitsGrantFilter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainUnitGrantFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainUnitGrantFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainUnitGroupProperties:
    boto3_raw_data: "type_defs.DomainUnitGroupPropertiesTypeDef" = dataclasses.field()

    groupId = field("groupId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainUnitGroupPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainUnitGroupPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainUnitUserProperties:
    boto3_raw_data: "type_defs.DomainUnitUserPropertiesTypeDef" = dataclasses.field()

    userId = field("userId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainUnitUserPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainUnitUserPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainUnitSummary:
    boto3_raw_data: "type_defs.DomainUnitSummaryTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainUnitSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainUnitSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainUnitTarget:
    boto3_raw_data: "type_defs.DomainUnitTargetTypeDef" = dataclasses.field()

    domainUnitId = field("domainUnitId")
    includeChildDomainUnits = field("includeChildDomainUnits")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainUnitTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainUnitTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Region:
    boto3_raw_data: "type_defs.RegionTypeDef" = dataclasses.field()

    regionName = field("regionName")
    regionNamePath = field("regionNamePath")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RegionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RegionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentConfigurationParameter:
    boto3_raw_data: "type_defs.EnvironmentConfigurationParameterTypeDef" = (
        dataclasses.field()
    )

    isEditable = field("isEditable")
    name = field("name")
    value = field("value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnvironmentConfigurationParameterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentConfigurationParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentResolvedAccount:
    boto3_raw_data: "type_defs.EnvironmentResolvedAccountTypeDef" = dataclasses.field()

    awsAccountId = field("awsAccountId")
    regionName = field("regionName")
    sourceAccountPoolId = field("sourceAccountPoolId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentResolvedAccountTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentResolvedAccountTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentProfileSummary:
    boto3_raw_data: "type_defs.EnvironmentProfileSummaryTypeDef" = dataclasses.field()

    createdBy = field("createdBy")
    domainId = field("domainId")
    environmentBlueprintId = field("environmentBlueprintId")
    id = field("id")
    name = field("name")
    awsAccountId = field("awsAccountId")
    awsAccountRegion = field("awsAccountRegion")
    createdAt = field("createdAt")
    description = field("description")
    projectId = field("projectId")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentProfileSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentProfileSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentSummary:
    boto3_raw_data: "type_defs.EnvironmentSummaryTypeDef" = dataclasses.field()

    createdBy = field("createdBy")
    domainId = field("domainId")
    name = field("name")
    projectId = field("projectId")
    provider = field("provider")
    awsAccountId = field("awsAccountId")
    awsAccountRegion = field("awsAccountRegion")
    createdAt = field("createdAt")
    description = field("description")
    environmentConfigurationId = field("environmentConfigurationId")
    environmentProfileId = field("environmentProfileId")
    id = field("id")
    status = field("status")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EqualToExpression:
    boto3_raw_data: "type_defs.EqualToExpressionTypeDef" = dataclasses.field()

    columnName = field("columnName")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EqualToExpressionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EqualToExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FailureCause:
    boto3_raw_data: "type_defs.FailureCauseTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FailureCauseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FailureCauseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Filter:
    boto3_raw_data: "type_defs.FilterTypeDef" = dataclasses.field()

    attribute = field("attribute")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterExpression:
    boto3_raw_data: "type_defs.FilterExpressionTypeDef" = dataclasses.field()

    expression = field("expression")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterExpressionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FilterExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Import:
    boto3_raw_data: "type_defs.ImportTypeDef" = dataclasses.field()

    name = field("name")
    revision = field("revision")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ImportTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccountPoolInput:
    boto3_raw_data: "type_defs.GetAccountPoolInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccountPoolInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountPoolInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssetFilterInput:
    boto3_raw_data: "type_defs.GetAssetFilterInputTypeDef" = dataclasses.field()

    assetIdentifier = field("assetIdentifier")
    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAssetFilterInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssetFilterInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssetInput:
    boto3_raw_data: "type_defs.GetAssetInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    revision = field("revision")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAssetInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetAssetInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssetTypeInput:
    boto3_raw_data: "type_defs.GetAssetTypeInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    revision = field("revision")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAssetTypeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssetTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectionInput:
    boto3_raw_data: "type_defs.GetConnectionInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    withSecret = field("withSecret")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConnectionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataProductInput:
    boto3_raw_data: "type_defs.GetDataProductInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    revision = field("revision")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataProductInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataProductInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataSourceInput:
    boto3_raw_data: "type_defs.GetDataSourceInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataSourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataSourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataSourceRunInput:
    boto3_raw_data: "type_defs.GetDataSourceRunInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataSourceRunInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataSourceRunInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainInput:
    boto3_raw_data: "type_defs.GetDomainInputTypeDef" = dataclasses.field()

    identifier = field("identifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDomainInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetDomainInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainUnitInput:
    boto3_raw_data: "type_defs.GetDomainUnitInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDomainUnitInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainUnitInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentActionInput:
    boto3_raw_data: "type_defs.GetEnvironmentActionInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    environmentIdentifier = field("environmentIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEnvironmentActionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentActionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentBlueprintConfigurationInput:
    boto3_raw_data: "type_defs.GetEnvironmentBlueprintConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    environmentBlueprintIdentifier = field("environmentBlueprintIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEnvironmentBlueprintConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentBlueprintConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentBlueprintInput:
    boto3_raw_data: "type_defs.GetEnvironmentBlueprintInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEnvironmentBlueprintInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentBlueprintInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentCredentialsInput:
    boto3_raw_data: "type_defs.GetEnvironmentCredentialsInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    environmentIdentifier = field("environmentIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetEnvironmentCredentialsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentCredentialsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentInput:
    boto3_raw_data: "type_defs.GetEnvironmentInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEnvironmentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentProfileInput:
    boto3_raw_data: "type_defs.GetEnvironmentProfileInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEnvironmentProfileInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentProfileInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFormTypeInput:
    boto3_raw_data: "type_defs.GetFormTypeInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    formTypeIdentifier = field("formTypeIdentifier")
    revision = field("revision")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFormTypeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFormTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGlossaryInput:
    boto3_raw_data: "type_defs.GetGlossaryInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetGlossaryInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGlossaryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGlossaryTermInput:
    boto3_raw_data: "type_defs.GetGlossaryTermInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGlossaryTermInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGlossaryTermInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupProfileInput:
    boto3_raw_data: "type_defs.GetGroupProfileInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    groupIdentifier = field("groupIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGroupProfileInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGroupProfileInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIamPortalLoginUrlInput:
    boto3_raw_data: "type_defs.GetIamPortalLoginUrlInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIamPortalLoginUrlInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIamPortalLoginUrlInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJobRunInput:
    boto3_raw_data: "type_defs.GetJobRunInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetJobRunInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetJobRunInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobRunError:
    boto3_raw_data: "type_defs.JobRunErrorTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobRunErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobRunErrorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLineageEventInput:
    boto3_raw_data: "type_defs.GetLineageEventInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLineageEventInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLineageEventInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LineageNodeReference:
    boto3_raw_data: "type_defs.LineageNodeReferenceTypeDef" = dataclasses.field()

    eventTimestamp = field("eventTimestamp")
    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LineageNodeReferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LineageNodeReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetListingInput:
    boto3_raw_data: "type_defs.GetListingInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    listingRevision = field("listingRevision")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetListingInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetListingInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMetadataGenerationRunInput:
    boto3_raw_data: "type_defs.GetMetadataGenerationRunInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMetadataGenerationRunInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMetadataGenerationRunInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataGenerationRunTarget:
    boto3_raw_data: "type_defs.MetadataGenerationRunTargetTypeDef" = dataclasses.field()

    identifier = field("identifier")
    type = field("type")
    revision = field("revision")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetadataGenerationRunTargetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataGenerationRunTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProjectInput:
    boto3_raw_data: "type_defs.GetProjectInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetProjectInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetProjectInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProjectProfileInput:
    boto3_raw_data: "type_defs.GetProjectProfileInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetProjectProfileInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProjectProfileInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRuleInput:
    boto3_raw_data: "type_defs.GetRuleInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    revision = field("revision")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRuleInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetRuleInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSubscriptionGrantInput:
    boto3_raw_data: "type_defs.GetSubscriptionGrantInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSubscriptionGrantInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSubscriptionGrantInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSubscriptionInput:
    boto3_raw_data: "type_defs.GetSubscriptionInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSubscriptionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSubscriptionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSubscriptionRequestDetailsInput:
    boto3_raw_data: "type_defs.GetSubscriptionRequestDetailsInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSubscriptionRequestDetailsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSubscriptionRequestDetailsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSubscriptionTargetInput:
    boto3_raw_data: "type_defs.GetSubscriptionTargetInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    environmentIdentifier = field("environmentIdentifier")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSubscriptionTargetInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSubscriptionTargetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTimeSeriesDataPointInput:
    boto3_raw_data: "type_defs.GetTimeSeriesDataPointInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    entityIdentifier = field("entityIdentifier")
    entityType = field("entityType")
    formName = field("formName")
    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTimeSeriesDataPointInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTimeSeriesDataPointInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeSeriesDataPointFormOutput:
    boto3_raw_data: "type_defs.TimeSeriesDataPointFormOutputTypeDef" = (
        dataclasses.field()
    )

    formName = field("formName")
    timestamp = field("timestamp")
    typeIdentifier = field("typeIdentifier")
    content = field("content")
    id = field("id")
    typeRevision = field("typeRevision")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TimeSeriesDataPointFormOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeSeriesDataPointFormOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserProfileInput:
    boto3_raw_data: "type_defs.GetUserProfileInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    userIdentifier = field("userIdentifier")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUserProfileInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUserProfileInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhysicalConnectionRequirementsOutput:
    boto3_raw_data: "type_defs.PhysicalConnectionRequirementsOutputTypeDef" = (
        dataclasses.field()
    )

    availabilityZone = field("availabilityZone")
    securityGroupIdList = field("securityGroupIdList")
    subnetId = field("subnetId")
    subnetIdList = field("subnetIdList")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PhysicalConnectionRequirementsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PhysicalConnectionRequirementsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlueOAuth2Credentials:
    boto3_raw_data: "type_defs.GlueOAuth2CredentialsTypeDef" = dataclasses.field()

    accessToken = field("accessToken")
    jwtToken = field("jwtToken")
    refreshToken = field("refreshToken")
    userManagedClientApplicationClientSecret = field(
        "userManagedClientApplicationClientSecret"
    )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlueOAuth2CredentialsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlueOAuth2CredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelfGrantStatusDetail:
    boto3_raw_data: "type_defs.SelfGrantStatusDetailTypeDef" = dataclasses.field()

    databaseName = field("databaseName")
    status = field("status")
    failureCause = field("failureCause")
    schemaName = field("schemaName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SelfGrantStatusDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelfGrantStatusDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListingRevisionInput:
    boto3_raw_data: "type_defs.ListingRevisionInputTypeDef" = dataclasses.field()

    identifier = field("identifier")
    revision = field("revision")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListingRevisionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListingRevisionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListingRevision:
    boto3_raw_data: "type_defs.ListingRevisionTypeDef" = dataclasses.field()

    id = field("id")
    revision = field("revision")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListingRevisionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListingRevisionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GreaterThanExpression:
    boto3_raw_data: "type_defs.GreaterThanExpressionTypeDef" = dataclasses.field()

    columnName = field("columnName")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GreaterThanExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GreaterThanExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GreaterThanOrEqualToExpression:
    boto3_raw_data: "type_defs.GreaterThanOrEqualToExpressionTypeDef" = (
        dataclasses.field()
    )

    columnName = field("columnName")
    value = field("value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GreaterThanOrEqualToExpressionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GreaterThanOrEqualToExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupDetails:
    boto3_raw_data: "type_defs.GroupDetailsTypeDef" = dataclasses.field()

    groupId = field("groupId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupPolicyGrantPrincipal:
    boto3_raw_data: "type_defs.GroupPolicyGrantPrincipalTypeDef" = dataclasses.field()

    groupIdentifier = field("groupIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GroupPolicyGrantPrincipalTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GroupPolicyGrantPrincipalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupProfileSummary:
    boto3_raw_data: "type_defs.GroupProfileSummaryTypeDef" = dataclasses.field()

    domainId = field("domainId")
    groupName = field("groupName")
    id = field("id")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GroupProfileSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GroupProfileSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IamUserProfileDetails:
    boto3_raw_data: "type_defs.IamUserProfileDetailsTypeDef" = dataclasses.field()

    arn = field("arn")
    principalId = field("principalId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IamUserProfileDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IamUserProfileDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InExpressionOutput:
    boto3_raw_data: "type_defs.InExpressionOutputTypeDef" = dataclasses.field()

    columnName = field("columnName")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InExpressionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InExpressionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InExpression:
    boto3_raw_data: "type_defs.InExpressionTypeDef" = dataclasses.field()

    columnName = field("columnName")
    values = field("values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InExpressionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InExpressionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsNotNullExpression:
    boto3_raw_data: "type_defs.IsNotNullExpressionTypeDef" = dataclasses.field()

    columnName = field("columnName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IsNotNullExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsNotNullExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IsNullExpression:
    boto3_raw_data: "type_defs.IsNullExpressionTypeDef" = dataclasses.field()

    columnName = field("columnName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IsNullExpressionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IsNullExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LakeFormationConfigurationOutput:
    boto3_raw_data: "type_defs.LakeFormationConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    locationRegistrationExcludeS3Locations = field(
        "locationRegistrationExcludeS3Locations"
    )
    locationRegistrationRole = field("locationRegistrationRole")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.LakeFormationConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LakeFormationConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LakeFormationConfiguration:
    boto3_raw_data: "type_defs.LakeFormationConfigurationTypeDef" = dataclasses.field()

    locationRegistrationExcludeS3Locations = field(
        "locationRegistrationExcludeS3Locations"
    )
    locationRegistrationRole = field("locationRegistrationRole")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LakeFormationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LakeFormationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LessThanExpression:
    boto3_raw_data: "type_defs.LessThanExpressionTypeDef" = dataclasses.field()

    columnName = field("columnName")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LessThanExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LessThanExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LessThanOrEqualToExpression:
    boto3_raw_data: "type_defs.LessThanOrEqualToExpressionTypeDef" = dataclasses.field()

    columnName = field("columnName")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LessThanOrEqualToExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LessThanOrEqualToExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LikeExpression:
    boto3_raw_data: "type_defs.LikeExpressionTypeDef" = dataclasses.field()

    columnName = field("columnName")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LikeExpressionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LikeExpressionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LineageNodeSummary:
    boto3_raw_data: "type_defs.LineageNodeSummaryTypeDef" = dataclasses.field()

    domainId = field("domainId")
    id = field("id")
    typeName = field("typeName")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    eventTimestamp = field("eventTimestamp")
    name = field("name")
    sourceIdentifier = field("sourceIdentifier")
    typeRevision = field("typeRevision")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LineageNodeSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LineageNodeSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LineageSqlQueryRunDetails:
    boto3_raw_data: "type_defs.LineageSqlQueryRunDetailsTypeDef" = dataclasses.field()

    errorMessages = field("errorMessages")
    numQueriesFailed = field("numQueriesFailed")
    queryEndTime = field("queryEndTime")
    queryStartTime = field("queryStartTime")
    totalQueriesProcessed = field("totalQueriesProcessed")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LineageSqlQueryRunDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LineageSqlQueryRunDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LineageSyncSchedule:
    boto3_raw_data: "type_defs.LineageSyncScheduleTypeDef" = dataclasses.field()

    schedule = field("schedule")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LineageSyncScheduleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LineageSyncScheduleTypeDef"]
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
class ListAccountPoolsInput:
    boto3_raw_data: "type_defs.ListAccountPoolsInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    maxResults = field("maxResults")
    name = field("name")
    nextToken = field("nextToken")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccountPoolsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountPoolsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountsInAccountPoolInput:
    boto3_raw_data: "type_defs.ListAccountsInAccountPoolInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAccountsInAccountPoolInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountsInAccountPoolInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetFiltersInput:
    boto3_raw_data: "type_defs.ListAssetFiltersInputTypeDef" = dataclasses.field()

    assetIdentifier = field("assetIdentifier")
    domainIdentifier = field("domainIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssetFiltersInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetFiltersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetRevisionsInput:
    boto3_raw_data: "type_defs.ListAssetRevisionsInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssetRevisionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetRevisionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectionsInput:
    boto3_raw_data: "type_defs.ListConnectionsInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    projectIdentifier = field("projectIdentifier")
    environmentIdentifier = field("environmentIdentifier")
    maxResults = field("maxResults")
    name = field("name")
    nextToken = field("nextToken")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConnectionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataProductRevisionsInput:
    boto3_raw_data: "type_defs.ListDataProductRevisionsInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDataProductRevisionsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataProductRevisionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSourceRunActivitiesInput:
    boto3_raw_data: "type_defs.ListDataSourceRunActivitiesInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDataSourceRunActivitiesInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSourceRunActivitiesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSourceRunsInput:
    boto3_raw_data: "type_defs.ListDataSourceRunsInputTypeDef" = dataclasses.field()

    dataSourceIdentifier = field("dataSourceIdentifier")
    domainIdentifier = field("domainIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataSourceRunsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSourceRunsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSourcesInput:
    boto3_raw_data: "type_defs.ListDataSourcesInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    projectIdentifier = field("projectIdentifier")
    connectionIdentifier = field("connectionIdentifier")
    environmentIdentifier = field("environmentIdentifier")
    maxResults = field("maxResults")
    name = field("name")
    nextToken = field("nextToken")
    status = field("status")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataSourcesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSourcesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainUnitsForParentInput:
    boto3_raw_data: "type_defs.ListDomainUnitsForParentInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    parentDomainUnitIdentifier = field("parentDomainUnitIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDomainUnitsForParentInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainUnitsForParentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainsInput:
    boto3_raw_data: "type_defs.ListDomainsInputTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListDomainsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntityOwnersInput:
    boto3_raw_data: "type_defs.ListEntityOwnersInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    entityIdentifier = field("entityIdentifier")
    entityType = field("entityType")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEntityOwnersInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntityOwnersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentActionsInput:
    boto3_raw_data: "type_defs.ListEnvironmentActionsInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    environmentIdentifier = field("environmentIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEnvironmentActionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentActionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentBlueprintConfigurationsInput:
    boto3_raw_data: "type_defs.ListEnvironmentBlueprintConfigurationsInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEnvironmentBlueprintConfigurationsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentBlueprintConfigurationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentBlueprintsInput:
    boto3_raw_data: "type_defs.ListEnvironmentBlueprintsInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    managed = field("managed")
    maxResults = field("maxResults")
    name = field("name")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEnvironmentBlueprintsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentBlueprintsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentProfilesInput:
    boto3_raw_data: "type_defs.ListEnvironmentProfilesInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    awsAccountId = field("awsAccountId")
    awsAccountRegion = field("awsAccountRegion")
    environmentBlueprintIdentifier = field("environmentBlueprintIdentifier")
    maxResults = field("maxResults")
    name = field("name")
    nextToken = field("nextToken")
    projectIdentifier = field("projectIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEnvironmentProfilesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentProfilesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentsInput:
    boto3_raw_data: "type_defs.ListEnvironmentsInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    projectIdentifier = field("projectIdentifier")
    awsAccountId = field("awsAccountId")
    awsAccountRegion = field("awsAccountRegion")
    environmentBlueprintIdentifier = field("environmentBlueprintIdentifier")
    environmentProfileIdentifier = field("environmentProfileIdentifier")
    maxResults = field("maxResults")
    name = field("name")
    nextToken = field("nextToken")
    provider = field("provider")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEnvironmentsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobRunsInput:
    boto3_raw_data: "type_defs.ListJobRunsInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    jobIdentifier = field("jobIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    sortOrder = field("sortOrder")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListJobRunsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobRunsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMetadataGenerationRunsInput:
    boto3_raw_data: "type_defs.ListMetadataGenerationRunsInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    status = field("status")
    type = field("type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMetadataGenerationRunsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMetadataGenerationRunsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyGrantsInput:
    boto3_raw_data: "type_defs.ListPolicyGrantsInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    entityIdentifier = field("entityIdentifier")
    entityType = field("entityType")
    policyType = field("policyType")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPolicyGrantsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyGrantsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProjectMembershipsInput:
    boto3_raw_data: "type_defs.ListProjectMembershipsInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    projectIdentifier = field("projectIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProjectMembershipsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProjectMembershipsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProjectProfilesInput:
    boto3_raw_data: "type_defs.ListProjectProfilesInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    maxResults = field("maxResults")
    name = field("name")
    nextToken = field("nextToken")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProjectProfilesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProjectProfilesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectProfileSummary:
    boto3_raw_data: "type_defs.ProjectProfileSummaryTypeDef" = dataclasses.field()

    createdBy = field("createdBy")
    domainId = field("domainId")
    id = field("id")
    name = field("name")
    createdAt = field("createdAt")
    description = field("description")
    domainUnitId = field("domainUnitId")
    lastUpdatedAt = field("lastUpdatedAt")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProjectProfileSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProjectProfileSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProjectsInput:
    boto3_raw_data: "type_defs.ListProjectsInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    groupIdentifier = field("groupIdentifier")
    maxResults = field("maxResults")
    name = field("name")
    nextToken = field("nextToken")
    userIdentifier = field("userIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListProjectsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProjectsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRulesInput:
    boto3_raw_data: "type_defs.ListRulesInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    targetIdentifier = field("targetIdentifier")
    targetType = field("targetType")
    action = field("action")
    assetTypes = field("assetTypes")
    dataProduct = field("dataProduct")
    includeCascaded = field("includeCascaded")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    projectIds = field("projectIds")
    ruleType = field("ruleType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListRulesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListRulesInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubscriptionGrantsInput:
    boto3_raw_data: "type_defs.ListSubscriptionGrantsInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    environmentId = field("environmentId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    owningProjectId = field("owningProjectId")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")
    subscribedListingId = field("subscribedListingId")
    subscriptionId = field("subscriptionId")
    subscriptionTargetId = field("subscriptionTargetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSubscriptionGrantsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubscriptionGrantsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubscriptionRequestsInput:
    boto3_raw_data: "type_defs.ListSubscriptionRequestsInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    approverProjectId = field("approverProjectId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    owningProjectId = field("owningProjectId")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")
    status = field("status")
    subscribedListingId = field("subscribedListingId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSubscriptionRequestsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubscriptionRequestsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubscriptionTargetsInput:
    boto3_raw_data: "type_defs.ListSubscriptionTargetsInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    environmentIdentifier = field("environmentIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSubscriptionTargetsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubscriptionTargetsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubscriptionsInput:
    boto3_raw_data: "type_defs.ListSubscriptionsInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    approverProjectId = field("approverProjectId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    owningProjectId = field("owningProjectId")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")
    status = field("status")
    subscribedListingId = field("subscribedListingId")
    subscriptionRequestIdentifier = field("subscriptionRequestIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSubscriptionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubscriptionsInputTypeDef"]
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

    resourceArn = field("resourceArn")

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
class MatchOffset:
    boto3_raw_data: "type_defs.MatchOffsetTypeDef" = dataclasses.field()

    endOffset = field("endOffset")
    startOffset = field("startOffset")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MatchOffsetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MatchOffsetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserDetails:
    boto3_raw_data: "type_defs.UserDetailsTypeDef" = dataclasses.field()

    userId = field("userId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserDetailsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataFormReference:
    boto3_raw_data: "type_defs.MetadataFormReferenceTypeDef" = dataclasses.field()

    typeIdentifier = field("typeIdentifier")
    typeRevision = field("typeRevision")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetadataFormReferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataFormReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataFormSummary:
    boto3_raw_data: "type_defs.MetadataFormSummaryTypeDef" = dataclasses.field()

    typeName = field("typeName")
    typeRevision = field("typeRevision")
    formName = field("formName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetadataFormSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataFormSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NameIdentifier:
    boto3_raw_data: "type_defs.NameIdentifierTypeDef" = dataclasses.field()

    name = field("name")
    namespace = field("namespace")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NameIdentifierTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NameIdentifierTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotEqualToExpression:
    boto3_raw_data: "type_defs.NotEqualToExpressionTypeDef" = dataclasses.field()

    columnName = field("columnName")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotEqualToExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotEqualToExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotInExpressionOutput:
    boto3_raw_data: "type_defs.NotInExpressionOutputTypeDef" = dataclasses.field()

    columnName = field("columnName")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotInExpressionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotInExpressionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotInExpression:
    boto3_raw_data: "type_defs.NotInExpressionTypeDef" = dataclasses.field()

    columnName = field("columnName")
    values = field("values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NotInExpressionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NotInExpressionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotLikeExpression:
    boto3_raw_data: "type_defs.NotLikeExpressionTypeDef" = dataclasses.field()

    columnName = field("columnName")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NotLikeExpressionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotLikeExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationResource:
    boto3_raw_data: "type_defs.NotificationResourceTypeDef" = dataclasses.field()

    id = field("id")
    type = field("type")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationResourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationResourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OAuth2ClientApplication:
    boto3_raw_data: "type_defs.OAuth2ClientApplicationTypeDef" = dataclasses.field()

    aWSManagedClientApplicationReference = field("aWSManagedClientApplicationReference")
    userManagedClientApplicationClientId = field("userManagedClientApplicationClientId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OAuth2ClientApplicationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OAuth2ClientApplicationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OverrideDomainUnitOwnersPolicyGrantDetail:
    boto3_raw_data: "type_defs.OverrideDomainUnitOwnersPolicyGrantDetailTypeDef" = (
        dataclasses.field()
    )

    includeChildDomainUnits = field("includeChildDomainUnits")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OverrideDomainUnitOwnersPolicyGrantDetailTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OverrideDomainUnitOwnersPolicyGrantDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OverrideProjectOwnersPolicyGrantDetail:
    boto3_raw_data: "type_defs.OverrideProjectOwnersPolicyGrantDetailTypeDef" = (
        dataclasses.field()
    )

    includeChildDomainUnits = field("includeChildDomainUnits")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OverrideProjectOwnersPolicyGrantDetailTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OverrideProjectOwnersPolicyGrantDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OwnerGroupPropertiesOutput:
    boto3_raw_data: "type_defs.OwnerGroupPropertiesOutputTypeDef" = dataclasses.field()

    groupId = field("groupId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OwnerGroupPropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OwnerGroupPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OwnerGroupProperties:
    boto3_raw_data: "type_defs.OwnerGroupPropertiesTypeDef" = dataclasses.field()

    groupIdentifier = field("groupIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OwnerGroupPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OwnerGroupPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OwnerUserPropertiesOutput:
    boto3_raw_data: "type_defs.OwnerUserPropertiesOutputTypeDef" = dataclasses.field()

    userId = field("userId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OwnerUserPropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OwnerUserPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OwnerUserProperties:
    boto3_raw_data: "type_defs.OwnerUserPropertiesTypeDef" = dataclasses.field()

    userIdentifier = field("userIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OwnerUserPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OwnerUserPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhysicalConnectionRequirements:
    boto3_raw_data: "type_defs.PhysicalConnectionRequirementsTypeDef" = (
        dataclasses.field()
    )

    availabilityZone = field("availabilityZone")
    securityGroupIdList = field("securityGroupIdList")
    subnetId = field("subnetId")
    subnetIdList = field("subnetIdList")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PhysicalConnectionRequirementsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PhysicalConnectionRequirementsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UseAssetTypePolicyGrantDetail:
    boto3_raw_data: "type_defs.UseAssetTypePolicyGrantDetailTypeDef" = (
        dataclasses.field()
    )

    domainUnitId = field("domainUnitId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UseAssetTypePolicyGrantDetailTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UseAssetTypePolicyGrantDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserPolicyGrantPrincipalOutput:
    boto3_raw_data: "type_defs.UserPolicyGrantPrincipalOutputTypeDef" = (
        dataclasses.field()
    )

    allUsersGrantFilter = field("allUsersGrantFilter")
    userIdentifier = field("userIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UserPolicyGrantPrincipalOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserPolicyGrantPrincipalOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserPolicyGrantPrincipal:
    boto3_raw_data: "type_defs.UserPolicyGrantPrincipalTypeDef" = dataclasses.field()

    allUsersGrantFilter = field("allUsersGrantFilter")
    userIdentifier = field("userIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserPolicyGrantPrincipalTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserPolicyGrantPrincipalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectsForRuleOutput:
    boto3_raw_data: "type_defs.ProjectsForRuleOutputTypeDef" = dataclasses.field()

    selectionMode = field("selectionMode")
    specificProjects = field("specificProjects")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProjectsForRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProjectsForRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectsForRule:
    boto3_raw_data: "type_defs.ProjectsForRuleTypeDef" = dataclasses.field()

    selectionMode = field("selectionMode")
    specificProjects = field("specificProjects")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProjectsForRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProjectsForRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftClusterStorage:
    boto3_raw_data: "type_defs.RedshiftClusterStorageTypeDef" = dataclasses.field()

    clusterName = field("clusterName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedshiftClusterStorageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftClusterStorageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftCredentialConfiguration:
    boto3_raw_data: "type_defs.RedshiftCredentialConfigurationTypeDef" = (
        dataclasses.field()
    )

    secretManagerArn = field("secretManagerArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RedshiftCredentialConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftCredentialConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UsernamePassword:
    boto3_raw_data: "type_defs.UsernamePasswordTypeDef" = dataclasses.field()

    password = field("password")
    username = field("username")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UsernamePasswordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UsernamePasswordTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftStorageProperties:
    boto3_raw_data: "type_defs.RedshiftStoragePropertiesTypeDef" = dataclasses.field()

    clusterName = field("clusterName")
    workgroupName = field("workgroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedshiftStoragePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftStoragePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftServerlessStorage:
    boto3_raw_data: "type_defs.RedshiftServerlessStorageTypeDef" = dataclasses.field()

    workgroupName = field("workgroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedshiftServerlessStorageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftServerlessStorageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectChoice:
    boto3_raw_data: "type_defs.RejectChoiceTypeDef" = dataclasses.field()

    predictionTarget = field("predictionTarget")
    predictionChoices = field("predictionChoices")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RejectChoiceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RejectChoiceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectRule:
    boto3_raw_data: "type_defs.RejectRuleTypeDef" = dataclasses.field()

    rule = field("rule")
    threshold = field("threshold")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RejectRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RejectRuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectSubscriptionRequestInput:
    boto3_raw_data: "type_defs.RejectSubscriptionRequestInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    decisionComment = field("decisionComment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RejectSubscriptionRequestInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectSubscriptionRequestInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokeSubscriptionInput:
    boto3_raw_data: "type_defs.RevokeSubscriptionInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    retainPermissions = field("retainPermissions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RevokeSubscriptionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokeSubscriptionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchGroupProfilesInput:
    boto3_raw_data: "type_defs.SearchGroupProfilesInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    groupType = field("groupType")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    searchText = field("searchText")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchGroupProfilesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchGroupProfilesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchInItem:
    boto3_raw_data: "type_defs.SearchInItemTypeDef" = dataclasses.field()

    attribute = field("attribute")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchInItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SearchInItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchSort:
    boto3_raw_data: "type_defs.SearchSortTypeDef" = dataclasses.field()

    attribute = field("attribute")
    order = field("order")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchSortTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SearchSortTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchUserProfilesInput:
    boto3_raw_data: "type_defs.SearchUserProfilesInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    userType = field("userType")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    searchText = field("searchText")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchUserProfilesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchUserProfilesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SparkGlueArgs:
    boto3_raw_data: "type_defs.SparkGlueArgsTypeDef" = dataclasses.field()

    connection = field("connection")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SparkGlueArgsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SparkGlueArgsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SsoUserProfileDetails:
    boto3_raw_data: "type_defs.SsoUserProfileDetailsTypeDef" = dataclasses.field()

    firstName = field("firstName")
    lastName = field("lastName")
    username = field("username")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SsoUserProfileDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SsoUserProfileDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDataSourceRunInput:
    boto3_raw_data: "type_defs.StartDataSourceRunInputTypeDef" = dataclasses.field()

    dataSourceIdentifier = field("dataSourceIdentifier")
    domainIdentifier = field("domainIdentifier")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartDataSourceRunInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDataSourceRunInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscribedProjectInput:
    boto3_raw_data: "type_defs.SubscribedProjectInputTypeDef" = dataclasses.field()

    identifier = field("identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubscribedProjectInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscribedProjectInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscribedProject:
    boto3_raw_data: "type_defs.SubscribedProjectTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubscribedProjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscribedProjectTypeDef"]
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

    resourceArn = field("resourceArn")
    tags = field("tags")

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
class TermRelations:
    boto3_raw_data: "type_defs.TermRelationsTypeDef" = dataclasses.field()

    classifies = field("classifies")
    isA = field("isA")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TermRelationsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TermRelationsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

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
class UpdateDomainUnitInput:
    boto3_raw_data: "type_defs.UpdateDomainUnitInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    description = field("description")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDomainUnitInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainUnitInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGlossaryInput:
    boto3_raw_data: "type_defs.UpdateGlossaryInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    clientToken = field("clientToken")
    description = field("description")
    name = field("name")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGlossaryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGlossaryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGroupProfileInput:
    boto3_raw_data: "type_defs.UpdateGroupProfileInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    groupIdentifier = field("groupIdentifier")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGroupProfileInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGroupProfileInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSubscriptionRequestInput:
    boto3_raw_data: "type_defs.UpdateSubscriptionRequestInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    requestReason = field("requestReason")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateSubscriptionRequestInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSubscriptionRequestInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserProfileInput:
    boto3_raw_data: "type_defs.UpdateUserProfileInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    status = field("status")
    userIdentifier = field("userIdentifier")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateUserProfileInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserProfileInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptPredictionsInput:
    boto3_raw_data: "type_defs.AcceptPredictionsInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @cached_property
    def acceptChoices(self):  # pragma: no cover
        return AcceptChoice.make_many(self.boto3_raw_data["acceptChoices"])

    @cached_property
    def acceptRule(self):  # pragma: no cover
        return AcceptRule.make_one(self.boto3_raw_data["acceptRule"])

    clientToken = field("clientToken")
    revision = field("revision")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AcceptPredictionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptPredictionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptPredictionsOutput:
    boto3_raw_data: "type_defs.AcceptPredictionsOutputTypeDef" = dataclasses.field()

    assetId = field("assetId")
    domainId = field("domainId")
    revision = field("revision")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AcceptPredictionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptPredictionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddPolicyGrantOutput:
    boto3_raw_data: "type_defs.AddPolicyGrantOutputTypeDef" = dataclasses.field()

    grantId = field("grantId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddPolicyGrantOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddPolicyGrantOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFormTypeOutput:
    boto3_raw_data: "type_defs.CreateFormTypeOutputTypeDef" = dataclasses.field()

    description = field("description")
    domainId = field("domainId")
    name = field("name")
    originDomainId = field("originDomainId")
    originProjectId = field("originProjectId")
    owningProjectId = field("owningProjectId")
    revision = field("revision")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFormTypeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFormTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGlossaryOutput:
    boto3_raw_data: "type_defs.CreateGlossaryOutputTypeDef" = dataclasses.field()

    description = field("description")
    domainId = field("domainId")
    id = field("id")
    name = field("name")
    owningProjectId = field("owningProjectId")
    status = field("status")
    usageRestrictions = field("usageRestrictions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGlossaryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGlossaryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGroupProfileOutput:
    boto3_raw_data: "type_defs.CreateGroupProfileOutputTypeDef" = dataclasses.field()

    domainId = field("domainId")
    groupName = field("groupName")
    id = field("id")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGroupProfileOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGroupProfileOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateListingChangeSetOutput:
    boto3_raw_data: "type_defs.CreateListingChangeSetOutputTypeDef" = (
        dataclasses.field()
    )

    listingId = field("listingId")
    listingRevision = field("listingRevision")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateListingChangeSetOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateListingChangeSetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConnectionOutput:
    boto3_raw_data: "type_defs.DeleteConnectionOutputTypeDef" = dataclasses.field()

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConnectionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConnectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainOutput:
    boto3_raw_data: "type_defs.DeleteDomainOutputTypeDef" = dataclasses.field()

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDomainOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainOutputTypeDef"]
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
class GetEnvironmentCredentialsOutput:
    boto3_raw_data: "type_defs.GetEnvironmentCredentialsOutputTypeDef" = (
        dataclasses.field()
    )

    accessKeyId = field("accessKeyId")
    expiration = field("expiration")
    secretAccessKey = field("secretAccessKey")
    sessionToken = field("sessionToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetEnvironmentCredentialsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentCredentialsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGlossaryOutput:
    boto3_raw_data: "type_defs.GetGlossaryOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")
    id = field("id")
    name = field("name")
    owningProjectId = field("owningProjectId")
    status = field("status")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")
    usageRestrictions = field("usageRestrictions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetGlossaryOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGlossaryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGroupProfileOutput:
    boto3_raw_data: "type_defs.GetGroupProfileOutputTypeDef" = dataclasses.field()

    domainId = field("domainId")
    groupName = field("groupName")
    id = field("id")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGroupProfileOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGroupProfileOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIamPortalLoginUrlOutput:
    boto3_raw_data: "type_defs.GetIamPortalLoginUrlOutputTypeDef" = dataclasses.field()

    authCodeUrl = field("authCodeUrl")
    userProfileId = field("userProfileId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIamPortalLoginUrlOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIamPortalLoginUrlOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLineageEventOutput:
    boto3_raw_data: "type_defs.GetLineageEventOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    domainId = field("domainId")
    event = field("event")
    eventTime = field("eventTime")
    id = field("id")
    processingStatus = field("processingStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLineageEventOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLineageEventOutputTypeDef"]
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

    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

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
class PostLineageEventOutput:
    boto3_raw_data: "type_defs.PostLineageEventOutputTypeDef" = dataclasses.field()

    domainId = field("domainId")
    id = field("id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PostLineageEventOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostLineageEventOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectPredictionsOutput:
    boto3_raw_data: "type_defs.RejectPredictionsOutputTypeDef" = dataclasses.field()

    assetId = field("assetId")
    assetRevision = field("assetRevision")
    domainId = field("domainId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RejectPredictionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectPredictionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMetadataGenerationRunOutput:
    boto3_raw_data: "type_defs.StartMetadataGenerationRunOutputTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    domainId = field("domainId")
    id = field("id")
    owningProjectId = field("owningProjectId")
    status = field("status")
    type = field("type")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartMetadataGenerationRunOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMetadataGenerationRunOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGlossaryOutput:
    boto3_raw_data: "type_defs.UpdateGlossaryOutputTypeDef" = dataclasses.field()

    description = field("description")
    domainId = field("domainId")
    id = field("id")
    name = field("name")
    owningProjectId = field("owningProjectId")
    status = field("status")
    usageRestrictions = field("usageRestrictions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGlossaryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGlossaryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGroupProfileOutput:
    boto3_raw_data: "type_defs.UpdateGroupProfileOutputTypeDef" = dataclasses.field()

    domainId = field("domainId")
    groupName = field("groupName")
    id = field("id")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGroupProfileOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGroupProfileOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptSubscriptionRequestInput:
    boto3_raw_data: "type_defs.AcceptSubscriptionRequestInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @cached_property
    def assetScopes(self):  # pragma: no cover
        return AcceptedAssetScope.make_many(self.boto3_raw_data["assetScopes"])

    decisionComment = field("decisionComment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AcceptSubscriptionRequestInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptSubscriptionRequestInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountsInAccountPoolOutput:
    boto3_raw_data: "type_defs.ListAccountsInAccountPoolOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return AccountInfoOutput.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAccountsInAccountPoolOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountsInAccountPoolOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountPoolsOutput:
    boto3_raw_data: "type_defs.ListAccountPoolsOutputTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return AccountPoolSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccountPoolsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountPoolsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountSourceOutput:
    boto3_raw_data: "type_defs.AccountSourceOutputTypeDef" = dataclasses.field()

    @cached_property
    def accounts(self):  # pragma: no cover
        return AccountInfoOutput.make_many(self.boto3_raw_data["accounts"])

    @cached_property
    def customAccountPoolHandler(self):  # pragma: no cover
        return CustomAccountPoolHandler.make_one(
            self.boto3_raw_data["customAccountPoolHandler"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccountSourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountSource:
    boto3_raw_data: "type_defs.AccountSourceTypeDef" = dataclasses.field()

    @cached_property
    def accounts(self):  # pragma: no cover
        return AccountInfo.make_many(self.boto3_raw_data["accounts"])

    @cached_property
    def customAccountPoolHandler(self):  # pragma: no cover
        return CustomAccountPoolHandler.make_one(
            self.boto3_raw_data["customAccountPoolHandler"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionParameters:
    boto3_raw_data: "type_defs.ActionParametersTypeDef" = dataclasses.field()

    @cached_property
    def awsConsoleLink(self):  # pragma: no cover
        return AwsConsoleLinkParameters.make_one(self.boto3_raw_data["awsConsoleLink"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionParametersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregationOutput:
    boto3_raw_data: "type_defs.AggregationOutputTypeDef" = dataclasses.field()

    attribute = field("attribute")
    displayValue = field("displayValue")

    @cached_property
    def items(self):  # pragma: no cover
        return AggregationOutputItem.make_many(self.boto3_raw_data["items"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AggregationOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetFiltersOutput:
    boto3_raw_data: "type_defs.ListAssetFiltersOutputTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return AssetFilterSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssetFiltersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetFiltersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTimeSeriesDataPointsOutput:
    boto3_raw_data: "type_defs.ListTimeSeriesDataPointsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return TimeSeriesDataPointSummaryFormOutput.make_many(
            self.boto3_raw_data["items"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTimeSeriesDataPointsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTimeSeriesDataPointsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssetOutput:
    boto3_raw_data: "type_defs.GetAssetOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")
    externalIdentifier = field("externalIdentifier")
    firstRevisionCreatedAt = field("firstRevisionCreatedAt")
    firstRevisionCreatedBy = field("firstRevisionCreatedBy")

    @cached_property
    def formsOutput(self):  # pragma: no cover
        return FormOutput.make_many(self.boto3_raw_data["formsOutput"])

    glossaryTerms = field("glossaryTerms")
    governedGlossaryTerms = field("governedGlossaryTerms")
    id = field("id")

    @cached_property
    def latestTimeSeriesDataPointFormsOutput(self):  # pragma: no cover
        return TimeSeriesDataPointSummaryFormOutput.make_many(
            self.boto3_raw_data["latestTimeSeriesDataPointFormsOutput"]
        )

    @cached_property
    def listing(self):  # pragma: no cover
        return AssetListingDetails.make_one(self.boto3_raw_data["listing"])

    name = field("name")
    owningProjectId = field("owningProjectId")

    @cached_property
    def readOnlyFormsOutput(self):  # pragma: no cover
        return FormOutput.make_many(self.boto3_raw_data["readOnlyFormsOutput"])

    revision = field("revision")
    typeIdentifier = field("typeIdentifier")
    typeRevision = field("typeRevision")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetAssetOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetAssetOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetListing:
    boto3_raw_data: "type_defs.AssetListingTypeDef" = dataclasses.field()

    assetId = field("assetId")
    assetRevision = field("assetRevision")
    assetType = field("assetType")
    createdAt = field("createdAt")
    forms = field("forms")

    @cached_property
    def glossaryTerms(self):  # pragma: no cover
        return DetailedGlossaryTerm.make_many(self.boto3_raw_data["glossaryTerms"])

    @cached_property
    def governedGlossaryTerms(self):  # pragma: no cover
        return DetailedGlossaryTerm.make_many(
            self.boto3_raw_data["governedGlossaryTerms"]
        )

    @cached_property
    def latestTimeSeriesDataPointForms(self):  # pragma: no cover
        return TimeSeriesDataPointSummaryFormOutput.make_many(
            self.boto3_raw_data["latestTimeSeriesDataPointForms"]
        )

    owningProjectId = field("owningProjectId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetListingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssetListingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListingSummaryItem:
    boto3_raw_data: "type_defs.ListingSummaryItemTypeDef" = dataclasses.field()

    @cached_property
    def glossaryTerms(self):  # pragma: no cover
        return DetailedGlossaryTerm.make_many(self.boto3_raw_data["glossaryTerms"])

    listingId = field("listingId")
    listingRevision = field("listingRevision")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListingSummaryItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListingSummaryItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListingSummary:
    boto3_raw_data: "type_defs.ListingSummaryTypeDef" = dataclasses.field()

    @cached_property
    def glossaryTerms(self):  # pragma: no cover
        return DetailedGlossaryTerm.make_many(self.boto3_raw_data["glossaryTerms"])

    listingId = field("listingId")
    listingRevision = field("listingRevision")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListingSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListingSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscribedProductListing:
    boto3_raw_data: "type_defs.SubscribedProductListingTypeDef" = dataclasses.field()

    @cached_property
    def assetListings(self):  # pragma: no cover
        return AssetInDataProductListingItem.make_many(
            self.boto3_raw_data["assetListings"]
        )

    description = field("description")
    entityId = field("entityId")
    entityRevision = field("entityRevision")

    @cached_property
    def glossaryTerms(self):  # pragma: no cover
        return DetailedGlossaryTerm.make_many(self.boto3_raw_data["glossaryTerms"])

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubscribedProductListingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscribedProductListingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetRevisionsOutput:
    boto3_raw_data: "type_defs.ListAssetRevisionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return AssetRevision.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssetRevisionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetRevisionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscribedAssetListing:
    boto3_raw_data: "type_defs.SubscribedAssetListingTypeDef" = dataclasses.field()

    @cached_property
    def assetScope(self):  # pragma: no cover
        return AssetScope.make_one(self.boto3_raw_data["assetScope"])

    entityId = field("entityId")
    entityRevision = field("entityRevision")
    entityType = field("entityType")
    forms = field("forms")

    @cached_property
    def glossaryTerms(self):  # pragma: no cover
        return DetailedGlossaryTerm.make_many(self.boto3_raw_data["glossaryTerms"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubscribedAssetListingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscribedAssetListingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetTypeItem:
    boto3_raw_data: "type_defs.AssetTypeItemTypeDef" = dataclasses.field()

    domainId = field("domainId")
    formsOutput = field("formsOutput")
    name = field("name")
    owningProjectId = field("owningProjectId")
    revision = field("revision")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    originDomainId = field("originDomainId")
    originProjectId = field("originProjectId")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetTypeItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssetTypeItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssetTypeOutput:
    boto3_raw_data: "type_defs.CreateAssetTypeOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")
    formsOutput = field("formsOutput")
    name = field("name")
    originDomainId = field("originDomainId")
    originProjectId = field("originProjectId")
    owningProjectId = field("owningProjectId")
    revision = field("revision")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAssetTypeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssetTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssetTypeOutput:
    boto3_raw_data: "type_defs.GetAssetTypeOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")
    formsOutput = field("formsOutput")
    name = field("name")
    originDomainId = field("originDomainId")
    originProjectId = field("originProjectId")
    owningProjectId = field("owningProjectId")
    revision = field("revision")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAssetTypeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssetTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LineageNodeTypeItem:
    boto3_raw_data: "type_defs.LineageNodeTypeItemTypeDef" = dataclasses.field()

    domainId = field("domainId")
    formsOutput = field("formsOutput")
    revision = field("revision")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    name = field("name")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LineageNodeTypeItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LineageNodeTypeItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthenticationConfigurationPatch:
    boto3_raw_data: "type_defs.AuthenticationConfigurationPatchTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def basicAuthenticationCredentials(self):  # pragma: no cover
        return BasicAuthenticationCredentials.make_one(
            self.boto3_raw_data["basicAuthenticationCredentials"]
        )

    secretArn = field("secretArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AuthenticationConfigurationPatchTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthenticationConfigurationPatchTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PostLineageEventInput:
    boto3_raw_data: "type_defs.PostLineageEventInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    event = field("event")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PostLineageEventInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostLineageEventInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PredictionConfiguration:
    boto3_raw_data: "type_defs.PredictionConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def businessNameGeneration(self):  # pragma: no cover
        return BusinessNameGenerationConfiguration.make_one(
            self.boto3_raw_data["businessNameGeneration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PredictionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PredictionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisioningProperties:
    boto3_raw_data: "type_defs.ProvisioningPropertiesTypeDef" = dataclasses.field()

    @cached_property
    def cloudFormation(self):  # pragma: no cover
        return CloudFormationProperties.make_one(self.boto3_raw_data["cloudFormation"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisioningPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisioningPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurableEnvironmentAction:
    boto3_raw_data: "type_defs.ConfigurableEnvironmentActionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def parameters(self):  # pragma: no cover
        return ConfigurableActionParameter.make_many(self.boto3_raw_data["parameters"])

    type = field("type")
    auth = field("auth")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConfigurableEnvironmentActionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurableEnvironmentActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssetTypeInput:
    boto3_raw_data: "type_defs.CreateAssetTypeInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    formsInput = field("formsInput")
    name = field("name")
    owningProjectIdentifier = field("owningProjectIdentifier")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAssetTypeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssetTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataProductOutput:
    boto3_raw_data: "type_defs.CreateDataProductOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")
    firstRevisionCreatedAt = field("firstRevisionCreatedAt")
    firstRevisionCreatedBy = field("firstRevisionCreatedBy")

    @cached_property
    def formsOutput(self):  # pragma: no cover
        return FormOutput.make_many(self.boto3_raw_data["formsOutput"])

    glossaryTerms = field("glossaryTerms")
    id = field("id")

    @cached_property
    def items(self):  # pragma: no cover
        return DataProductItemOutput.make_many(self.boto3_raw_data["items"])

    name = field("name")
    owningProjectId = field("owningProjectId")
    revision = field("revision")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataProductOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataProductOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataProductRevisionOutput:
    boto3_raw_data: "type_defs.CreateDataProductRevisionOutputTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")
    firstRevisionCreatedAt = field("firstRevisionCreatedAt")
    firstRevisionCreatedBy = field("firstRevisionCreatedBy")

    @cached_property
    def formsOutput(self):  # pragma: no cover
        return FormOutput.make_many(self.boto3_raw_data["formsOutput"])

    glossaryTerms = field("glossaryTerms")
    id = field("id")

    @cached_property
    def items(self):  # pragma: no cover
        return DataProductItemOutput.make_many(self.boto3_raw_data["items"])

    name = field("name")
    owningProjectId = field("owningProjectId")
    revision = field("revision")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDataProductRevisionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataProductRevisionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataProductOutput:
    boto3_raw_data: "type_defs.GetDataProductOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")
    firstRevisionCreatedAt = field("firstRevisionCreatedAt")
    firstRevisionCreatedBy = field("firstRevisionCreatedBy")

    @cached_property
    def formsOutput(self):  # pragma: no cover
        return FormOutput.make_many(self.boto3_raw_data["formsOutput"])

    glossaryTerms = field("glossaryTerms")
    id = field("id")

    @cached_property
    def items(self):  # pragma: no cover
        return DataProductItemOutput.make_many(self.boto3_raw_data["items"])

    name = field("name")
    owningProjectId = field("owningProjectId")
    revision = field("revision")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataProductOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataProductOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceSummary:
    boto3_raw_data: "type_defs.DataSourceSummaryTypeDef" = dataclasses.field()

    dataSourceId = field("dataSourceId")
    domainId = field("domainId")
    name = field("name")
    status = field("status")
    type = field("type")
    connectionId = field("connectionId")
    createdAt = field("createdAt")
    description = field("description")
    enableSetting = field("enableSetting")
    environmentId = field("environmentId")
    lastRunAssetCount = field("lastRunAssetCount")
    lastRunAt = field("lastRunAt")

    @cached_property
    def lastRunErrorMessage(self):  # pragma: no cover
        return DataSourceErrorMessage.make_one(
            self.boto3_raw_data["lastRunErrorMessage"]
        )

    lastRunStatus = field("lastRunStatus")

    @cached_property
    def schedule(self):  # pragma: no cover
        return ScheduleConfiguration.make_one(self.boto3_raw_data["schedule"])

    updatedAt = field("updatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSourceSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainInput:
    boto3_raw_data: "type_defs.CreateDomainInputTypeDef" = dataclasses.field()

    domainExecutionRole = field("domainExecutionRole")
    name = field("name")
    clientToken = field("clientToken")
    description = field("description")
    domainVersion = field("domainVersion")
    kmsKeyIdentifier = field("kmsKeyIdentifier")
    serviceRole = field("serviceRole")

    @cached_property
    def singleSignOn(self):  # pragma: no cover
        return SingleSignOn.make_one(self.boto3_raw_data["singleSignOn"])

    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateDomainInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainOutput:
    boto3_raw_data: "type_defs.CreateDomainOutputTypeDef" = dataclasses.field()

    arn = field("arn")
    description = field("description")
    domainExecutionRole = field("domainExecutionRole")
    domainVersion = field("domainVersion")
    id = field("id")
    kmsKeyIdentifier = field("kmsKeyIdentifier")
    name = field("name")
    portalUrl = field("portalUrl")
    rootDomainUnitId = field("rootDomainUnitId")
    serviceRole = field("serviceRole")

    @cached_property
    def singleSignOn(self):  # pragma: no cover
        return SingleSignOn.make_one(self.boto3_raw_data["singleSignOn"])

    status = field("status")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDomainOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainOutput:
    boto3_raw_data: "type_defs.GetDomainOutputTypeDef" = dataclasses.field()

    arn = field("arn")
    createdAt = field("createdAt")
    description = field("description")
    domainExecutionRole = field("domainExecutionRole")
    domainVersion = field("domainVersion")
    id = field("id")
    kmsKeyIdentifier = field("kmsKeyIdentifier")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    portalUrl = field("portalUrl")
    rootDomainUnitId = field("rootDomainUnitId")
    serviceRole = field("serviceRole")

    @cached_property
    def singleSignOn(self):  # pragma: no cover
        return SingleSignOn.make_one(self.boto3_raw_data["singleSignOn"])

    status = field("status")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDomainOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetDomainOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainInput:
    boto3_raw_data: "type_defs.UpdateDomainInputTypeDef" = dataclasses.field()

    identifier = field("identifier")
    clientToken = field("clientToken")
    description = field("description")
    domainExecutionRole = field("domainExecutionRole")
    name = field("name")
    serviceRole = field("serviceRole")

    @cached_property
    def singleSignOn(self):  # pragma: no cover
        return SingleSignOn.make_one(self.boto3_raw_data["singleSignOn"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateDomainInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainOutput:
    boto3_raw_data: "type_defs.UpdateDomainOutputTypeDef" = dataclasses.field()

    description = field("description")
    domainExecutionRole = field("domainExecutionRole")
    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    rootDomainUnitId = field("rootDomainUnitId")
    serviceRole = field("serviceRole")

    @cached_property
    def singleSignOn(self):  # pragma: no cover
        return SingleSignOn.make_one(self.boto3_raw_data["singleSignOn"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDomainOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentProfileOutput:
    boto3_raw_data: "type_defs.CreateEnvironmentProfileOutputTypeDef" = (
        dataclasses.field()
    )

    awsAccountId = field("awsAccountId")
    awsAccountRegion = field("awsAccountRegion")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")
    environmentBlueprintId = field("environmentBlueprintId")
    id = field("id")
    name = field("name")
    projectId = field("projectId")
    updatedAt = field("updatedAt")

    @cached_property
    def userParameters(self):  # pragma: no cover
        return CustomParameter.make_many(self.boto3_raw_data["userParameters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateEnvironmentProfileOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentProfileOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentProfileOutput:
    boto3_raw_data: "type_defs.GetEnvironmentProfileOutputTypeDef" = dataclasses.field()

    awsAccountId = field("awsAccountId")
    awsAccountRegion = field("awsAccountRegion")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")
    environmentBlueprintId = field("environmentBlueprintId")
    id = field("id")
    name = field("name")
    projectId = field("projectId")
    updatedAt = field("updatedAt")

    @cached_property
    def userParameters(self):  # pragma: no cover
        return CustomParameter.make_many(self.boto3_raw_data["userParameters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEnvironmentProfileOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentProfileOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEnvironmentProfileOutput:
    boto3_raw_data: "type_defs.UpdateEnvironmentProfileOutputTypeDef" = (
        dataclasses.field()
    )

    awsAccountId = field("awsAccountId")
    awsAccountRegion = field("awsAccountRegion")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")
    environmentBlueprintId = field("environmentBlueprintId")
    id = field("id")
    name = field("name")
    projectId = field("projectId")
    updatedAt = field("updatedAt")

    @cached_property
    def userParameters(self):  # pragma: no cover
        return CustomParameter.make_many(self.boto3_raw_data["userParameters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateEnvironmentProfileOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnvironmentProfileOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentInput:
    boto3_raw_data: "type_defs.CreateEnvironmentInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    name = field("name")
    projectIdentifier = field("projectIdentifier")
    deploymentOrder = field("deploymentOrder")
    description = field("description")
    environmentAccountIdentifier = field("environmentAccountIdentifier")
    environmentAccountRegion = field("environmentAccountRegion")
    environmentBlueprintIdentifier = field("environmentBlueprintIdentifier")
    environmentConfigurationId = field("environmentConfigurationId")
    environmentProfileIdentifier = field("environmentProfileIdentifier")
    glossaryTerms = field("glossaryTerms")

    @cached_property
    def userParameters(self):  # pragma: no cover
        return EnvironmentParameter.make_many(self.boto3_raw_data["userParameters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEnvironmentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentProfileInput:
    boto3_raw_data: "type_defs.CreateEnvironmentProfileInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    environmentBlueprintIdentifier = field("environmentBlueprintIdentifier")
    name = field("name")
    projectIdentifier = field("projectIdentifier")
    awsAccountId = field("awsAccountId")
    awsAccountRegion = field("awsAccountRegion")
    description = field("description")

    @cached_property
    def userParameters(self):  # pragma: no cover
        return EnvironmentParameter.make_many(self.boto3_raw_data["userParameters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateEnvironmentProfileInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentProfileInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEnvironmentInput:
    boto3_raw_data: "type_defs.UpdateEnvironmentInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    blueprintVersion = field("blueprintVersion")
    description = field("description")
    glossaryTerms = field("glossaryTerms")
    name = field("name")

    @cached_property
    def userParameters(self):  # pragma: no cover
        return EnvironmentParameter.make_many(self.boto3_raw_data["userParameters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEnvironmentInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnvironmentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEnvironmentProfileInput:
    boto3_raw_data: "type_defs.UpdateEnvironmentProfileInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    awsAccountId = field("awsAccountId")
    awsAccountRegion = field("awsAccountRegion")
    description = field("description")
    name = field("name")

    @cached_property
    def userParameters(self):  # pragma: no cover
        return EnvironmentParameter.make_many(self.boto3_raw_data["userParameters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateEnvironmentProfileInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnvironmentProfileInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFormTypeInput:
    boto3_raw_data: "type_defs.CreateFormTypeInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")

    @cached_property
    def model(self):  # pragma: no cover
        return Model.make_one(self.boto3_raw_data["model"])

    name = field("name")
    owningProjectIdentifier = field("owningProjectIdentifier")
    description = field("description")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFormTypeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFormTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGlossaryTermOutput:
    boto3_raw_data: "type_defs.CreateGlossaryTermOutputTypeDef" = dataclasses.field()

    domainId = field("domainId")
    glossaryId = field("glossaryId")
    id = field("id")
    longDescription = field("longDescription")
    name = field("name")
    shortDescription = field("shortDescription")
    status = field("status")

    @cached_property
    def termRelations(self):  # pragma: no cover
        return TermRelationsOutput.make_one(self.boto3_raw_data["termRelations"])

    usageRestrictions = field("usageRestrictions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGlossaryTermOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGlossaryTermOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGlossaryTermOutput:
    boto3_raw_data: "type_defs.GetGlossaryTermOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    domainId = field("domainId")
    glossaryId = field("glossaryId")
    id = field("id")
    longDescription = field("longDescription")
    name = field("name")
    shortDescription = field("shortDescription")
    status = field("status")

    @cached_property
    def termRelations(self):  # pragma: no cover
        return TermRelationsOutput.make_one(self.boto3_raw_data["termRelations"])

    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")
    usageRestrictions = field("usageRestrictions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGlossaryTermOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGlossaryTermOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGlossaryTermOutput:
    boto3_raw_data: "type_defs.UpdateGlossaryTermOutputTypeDef" = dataclasses.field()

    domainId = field("domainId")
    glossaryId = field("glossaryId")
    id = field("id")
    longDescription = field("longDescription")
    name = field("name")
    shortDescription = field("shortDescription")
    status = field("status")

    @cached_property
    def termRelations(self):  # pragma: no cover
        return TermRelationsOutput.make_one(self.boto3_raw_data["termRelations"])

    usageRestrictions = field("usageRestrictions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGlossaryTermOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGlossaryTermOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProjectMembershipInput:
    boto3_raw_data: "type_defs.CreateProjectMembershipInputTypeDef" = (
        dataclasses.field()
    )

    designation = field("designation")
    domainIdentifier = field("domainIdentifier")

    @cached_property
    def member(self):  # pragma: no cover
        return Member.make_one(self.boto3_raw_data["member"])

    projectIdentifier = field("projectIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProjectMembershipInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProjectMembershipInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProjectMembershipInput:
    boto3_raw_data: "type_defs.DeleteProjectMembershipInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")

    @cached_property
    def member(self):  # pragma: no cover
        return Member.make_one(self.boto3_raw_data["member"])

    projectIdentifier = field("projectIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProjectMembershipInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProjectMembershipInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectSummary:
    boto3_raw_data: "type_defs.ProjectSummaryTypeDef" = dataclasses.field()

    createdBy = field("createdBy")
    domainId = field("domainId")
    id = field("id")
    name = field("name")
    createdAt = field("createdAt")
    description = field("description")
    domainUnitId = field("domainUnitId")

    @cached_property
    def failureReasons(self):  # pragma: no cover
        return ProjectDeletionError.make_many(self.boto3_raw_data["failureReasons"])

    projectStatus = field("projectStatus")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProjectSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProjectSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSubscriptionTargetInput:
    boto3_raw_data: "type_defs.CreateSubscriptionTargetInputTypeDef" = (
        dataclasses.field()
    )

    applicableAssetTypes = field("applicableAssetTypes")
    authorizedPrincipals = field("authorizedPrincipals")
    domainIdentifier = field("domainIdentifier")
    environmentIdentifier = field("environmentIdentifier")
    manageAccessRole = field("manageAccessRole")
    name = field("name")

    @cached_property
    def subscriptionTargetConfig(self):  # pragma: no cover
        return SubscriptionTargetForm.make_many(
            self.boto3_raw_data["subscriptionTargetConfig"]
        )

    type = field("type")
    clientToken = field("clientToken")
    provider = field("provider")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSubscriptionTargetInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSubscriptionTargetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSubscriptionTargetOutput:
    boto3_raw_data: "type_defs.CreateSubscriptionTargetOutputTypeDef" = (
        dataclasses.field()
    )

    applicableAssetTypes = field("applicableAssetTypes")
    authorizedPrincipals = field("authorizedPrincipals")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    domainId = field("domainId")
    environmentId = field("environmentId")
    id = field("id")
    manageAccessRole = field("manageAccessRole")
    name = field("name")
    projectId = field("projectId")
    provider = field("provider")

    @cached_property
    def subscriptionTargetConfig(self):  # pragma: no cover
        return SubscriptionTargetForm.make_many(
            self.boto3_raw_data["subscriptionTargetConfig"]
        )

    type = field("type")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSubscriptionTargetOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSubscriptionTargetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSubscriptionTargetOutput:
    boto3_raw_data: "type_defs.GetSubscriptionTargetOutputTypeDef" = dataclasses.field()

    applicableAssetTypes = field("applicableAssetTypes")
    authorizedPrincipals = field("authorizedPrincipals")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    domainId = field("domainId")
    environmentId = field("environmentId")
    id = field("id")
    manageAccessRole = field("manageAccessRole")
    name = field("name")
    projectId = field("projectId")
    provider = field("provider")

    @cached_property
    def subscriptionTargetConfig(self):  # pragma: no cover
        return SubscriptionTargetForm.make_many(
            self.boto3_raw_data["subscriptionTargetConfig"]
        )

    type = field("type")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSubscriptionTargetOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSubscriptionTargetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscriptionTargetSummary:
    boto3_raw_data: "type_defs.SubscriptionTargetSummaryTypeDef" = dataclasses.field()

    applicableAssetTypes = field("applicableAssetTypes")
    authorizedPrincipals = field("authorizedPrincipals")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    domainId = field("domainId")
    environmentId = field("environmentId")
    id = field("id")
    name = field("name")
    projectId = field("projectId")
    provider = field("provider")

    @cached_property
    def subscriptionTargetConfig(self):  # pragma: no cover
        return SubscriptionTargetForm.make_many(
            self.boto3_raw_data["subscriptionTargetConfig"]
        )

    type = field("type")
    manageAccessRole = field("manageAccessRole")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubscriptionTargetSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscriptionTargetSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSubscriptionTargetInput:
    boto3_raw_data: "type_defs.UpdateSubscriptionTargetInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    environmentIdentifier = field("environmentIdentifier")
    identifier = field("identifier")
    applicableAssetTypes = field("applicableAssetTypes")
    authorizedPrincipals = field("authorizedPrincipals")
    manageAccessRole = field("manageAccessRole")
    name = field("name")
    provider = field("provider")

    @cached_property
    def subscriptionTargetConfig(self):  # pragma: no cover
        return SubscriptionTargetForm.make_many(
            self.boto3_raw_data["subscriptionTargetConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateSubscriptionTargetInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSubscriptionTargetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSubscriptionTargetOutput:
    boto3_raw_data: "type_defs.UpdateSubscriptionTargetOutputTypeDef" = (
        dataclasses.field()
    )

    applicableAssetTypes = field("applicableAssetTypes")
    authorizedPrincipals = field("authorizedPrincipals")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    domainId = field("domainId")
    environmentId = field("environmentId")
    id = field("id")
    manageAccessRole = field("manageAccessRole")
    name = field("name")
    projectId = field("projectId")
    provider = field("provider")

    @cached_property
    def subscriptionTargetConfig(self):  # pragma: no cover
        return SubscriptionTargetForm.make_many(
            self.boto3_raw_data["subscriptionTargetConfig"]
        )

    type = field("type")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateSubscriptionTargetOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSubscriptionTargetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataProductRevisionsOutput:
    boto3_raw_data: "type_defs.ListDataProductRevisionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return DataProductRevision.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDataProductRevisionsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataProductRevisionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceRunActivity:
    boto3_raw_data: "type_defs.DataSourceRunActivityTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    dataAssetStatus = field("dataAssetStatus")
    dataSourceRunId = field("dataSourceRunId")
    database = field("database")
    projectId = field("projectId")
    technicalName = field("technicalName")
    updatedAt = field("updatedAt")
    dataAssetId = field("dataAssetId")

    @cached_property
    def errorMessage(self):  # pragma: no cover
        return DataSourceErrorMessage.make_one(self.boto3_raw_data["errorMessage"])

    @cached_property
    def lineageSummary(self):  # pragma: no cover
        return LineageInfo.make_one(self.boto3_raw_data["lineageSummary"])

    technicalDescription = field("technicalDescription")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataSourceRunActivityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceRunActivityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceRunSummary:
    boto3_raw_data: "type_defs.DataSourceRunSummaryTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    dataSourceId = field("dataSourceId")
    id = field("id")
    projectId = field("projectId")
    status = field("status")
    type = field("type")
    updatedAt = field("updatedAt")

    @cached_property
    def errorMessage(self):  # pragma: no cover
        return DataSourceErrorMessage.make_one(self.boto3_raw_data["errorMessage"])

    @cached_property
    def lineageSummary(self):  # pragma: no cover
        return DataSourceRunLineageSummary.make_one(
            self.boto3_raw_data["lineageSummary"]
        )

    @cached_property
    def runStatisticsForAssets(self):  # pragma: no cover
        return RunStatisticsForAssets.make_one(
            self.boto3_raw_data["runStatisticsForAssets"]
        )

    startedAt = field("startedAt")
    stoppedAt = field("stoppedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataSourceRunSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceRunSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataSourceRunOutput:
    boto3_raw_data: "type_defs.GetDataSourceRunOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    dataSourceConfigurationSnapshot = field("dataSourceConfigurationSnapshot")
    dataSourceId = field("dataSourceId")
    domainId = field("domainId")

    @cached_property
    def errorMessage(self):  # pragma: no cover
        return DataSourceErrorMessage.make_one(self.boto3_raw_data["errorMessage"])

    id = field("id")

    @cached_property
    def lineageSummary(self):  # pragma: no cover
        return DataSourceRunLineageSummary.make_one(
            self.boto3_raw_data["lineageSummary"]
        )

    projectId = field("projectId")

    @cached_property
    def runStatisticsForAssets(self):  # pragma: no cover
        return RunStatisticsForAssets.make_one(
            self.boto3_raw_data["runStatisticsForAssets"]
        )

    startedAt = field("startedAt")
    status = field("status")
    stoppedAt = field("stoppedAt")
    type = field("type")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataSourceRunOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataSourceRunOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartDataSourceRunOutput:
    boto3_raw_data: "type_defs.StartDataSourceRunOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    dataSourceConfigurationSnapshot = field("dataSourceConfigurationSnapshot")
    dataSourceId = field("dataSourceId")
    domainId = field("domainId")

    @cached_property
    def errorMessage(self):  # pragma: no cover
        return DataSourceErrorMessage.make_one(self.boto3_raw_data["errorMessage"])

    id = field("id")
    projectId = field("projectId")

    @cached_property
    def runStatisticsForAssets(self):  # pragma: no cover
        return RunStatisticsForAssets.make_one(
            self.boto3_raw_data["runStatisticsForAssets"]
        )

    startedAt = field("startedAt")
    status = field("status")
    stoppedAt = field("stoppedAt")
    type = field("type")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartDataSourceRunOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDataSourceRunOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Deployment:
    boto3_raw_data: "type_defs.DeploymentTypeDef" = dataclasses.field()

    deploymentId = field("deploymentId")
    deploymentStatus = field("deploymentStatus")
    deploymentType = field("deploymentType")

    @cached_property
    def failureReason(self):  # pragma: no cover
        return EnvironmentError.make_one(self.boto3_raw_data["failureReason"])

    isDeploymentComplete = field("isDeploymentComplete")
    messages = field("messages")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeploymentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeploymentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentDeploymentDetailsOutput:
    boto3_raw_data: "type_defs.EnvironmentDeploymentDetailsOutputTypeDef" = (
        dataclasses.field()
    )

    environmentFailureReasons = field("environmentFailureReasons")
    overallDeploymentStatus = field("overallDeploymentStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnvironmentDeploymentDetailsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentDeploymentDetailsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentDeploymentDetails:
    boto3_raw_data: "type_defs.EnvironmentDeploymentDetailsTypeDef" = (
        dataclasses.field()
    )

    environmentFailureReasons = field("environmentFailureReasons")
    overallDeploymentStatus = field("overallDeploymentStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentDeploymentDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentDeploymentDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainsOutput:
    boto3_raw_data: "type_defs.ListDomainsOutputTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return DomainSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListDomainsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectGrantFilter:
    boto3_raw_data: "type_defs.ProjectGrantFilterTypeDef" = dataclasses.field()

    @cached_property
    def domainUnitFilter(self):  # pragma: no cover
        return DomainUnitFilterForProject.make_one(
            self.boto3_raw_data["domainUnitFilter"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProjectGrantFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProjectGrantFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainUnitPolicyGrantPrincipalOutput:
    boto3_raw_data: "type_defs.DomainUnitPolicyGrantPrincipalOutputTypeDef" = (
        dataclasses.field()
    )

    domainUnitDesignation = field("domainUnitDesignation")

    @cached_property
    def domainUnitGrantFilter(self):  # pragma: no cover
        return DomainUnitGrantFilterOutput.make_one(
            self.boto3_raw_data["domainUnitGrantFilter"]
        )

    domainUnitIdentifier = field("domainUnitIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DomainUnitPolicyGrantPrincipalOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainUnitPolicyGrantPrincipalOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainUnitPolicyGrantPrincipal:
    boto3_raw_data: "type_defs.DomainUnitPolicyGrantPrincipalTypeDef" = (
        dataclasses.field()
    )

    domainUnitDesignation = field("domainUnitDesignation")

    @cached_property
    def domainUnitGrantFilter(self):  # pragma: no cover
        return DomainUnitGrantFilter.make_one(
            self.boto3_raw_data["domainUnitGrantFilter"]
        )

    domainUnitIdentifier = field("domainUnitIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DomainUnitPolicyGrantPrincipalTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainUnitPolicyGrantPrincipalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainUnitOwnerProperties:
    boto3_raw_data: "type_defs.DomainUnitOwnerPropertiesTypeDef" = dataclasses.field()

    @cached_property
    def group(self):  # pragma: no cover
        return DomainUnitGroupProperties.make_one(self.boto3_raw_data["group"])

    @cached_property
    def user(self):  # pragma: no cover
        return DomainUnitUserProperties.make_one(self.boto3_raw_data["user"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainUnitOwnerPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainUnitOwnerPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainUnitsForParentOutput:
    boto3_raw_data: "type_defs.ListDomainUnitsForParentOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return DomainUnitSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDomainUnitsForParentOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainUnitsForParentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleTarget:
    boto3_raw_data: "type_defs.RuleTargetTypeDef" = dataclasses.field()

    @cached_property
    def domainUnitTarget(self):  # pragma: no cover
        return DomainUnitTarget.make_one(self.boto3_raw_data["domainUnitTarget"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleTargetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentConfigurationParametersDetailsOutput:
    boto3_raw_data: (
        "type_defs.EnvironmentConfigurationParametersDetailsOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def parameterOverrides(self):  # pragma: no cover
        return EnvironmentConfigurationParameter.make_many(
            self.boto3_raw_data["parameterOverrides"]
        )

    @cached_property
    def resolvedParameters(self):  # pragma: no cover
        return EnvironmentConfigurationParameter.make_many(
            self.boto3_raw_data["resolvedParameters"]
        )

    ssmPath = field("ssmPath")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnvironmentConfigurationParametersDetailsOutputTypeDef"
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
                "type_defs.EnvironmentConfigurationParametersDetailsOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentConfigurationParametersDetails:
    boto3_raw_data: "type_defs.EnvironmentConfigurationParametersDetailsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def parameterOverrides(self):  # pragma: no cover
        return EnvironmentConfigurationParameter.make_many(
            self.boto3_raw_data["parameterOverrides"]
        )

    @cached_property
    def resolvedParameters(self):  # pragma: no cover
        return EnvironmentConfigurationParameter.make_many(
            self.boto3_raw_data["resolvedParameters"]
        )

    ssmPath = field("ssmPath")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnvironmentConfigurationParametersDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentConfigurationParametersDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentConfigurationUserParameterOutput:
    boto3_raw_data: "type_defs.EnvironmentConfigurationUserParameterOutputTypeDef" = (
        dataclasses.field()
    )

    environmentConfigurationName = field("environmentConfigurationName")
    environmentId = field("environmentId")

    @cached_property
    def environmentParameters(self):  # pragma: no cover
        return EnvironmentParameter.make_many(
            self.boto3_raw_data["environmentParameters"]
        )

    @cached_property
    def environmentResolvedAccount(self):  # pragma: no cover
        return EnvironmentResolvedAccount.make_one(
            self.boto3_raw_data["environmentResolvedAccount"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnvironmentConfigurationUserParameterOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentConfigurationUserParameterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentConfigurationUserParameter:
    boto3_raw_data: "type_defs.EnvironmentConfigurationUserParameterTypeDef" = (
        dataclasses.field()
    )

    environmentConfigurationName = field("environmentConfigurationName")
    environmentId = field("environmentId")

    @cached_property
    def environmentParameters(self):  # pragma: no cover
        return EnvironmentParameter.make_many(
            self.boto3_raw_data["environmentParameters"]
        )

    @cached_property
    def environmentResolvedAccount(self):  # pragma: no cover
        return EnvironmentResolvedAccount.make_one(
            self.boto3_raw_data["environmentResolvedAccount"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnvironmentConfigurationUserParameterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentConfigurationUserParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentProfilesOutput:
    boto3_raw_data: "type_defs.ListEnvironmentProfilesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return EnvironmentProfileSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEnvironmentProfilesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentProfilesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentsOutput:
    boto3_raw_data: "type_defs.ListEnvironmentsOutputTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return EnvironmentSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEnvironmentsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscribedAsset:
    boto3_raw_data: "type_defs.SubscribedAssetTypeDef" = dataclasses.field()

    assetId = field("assetId")
    assetRevision = field("assetRevision")
    status = field("status")

    @cached_property
    def assetScope(self):  # pragma: no cover
        return AssetScope.make_one(self.boto3_raw_data["assetScope"])

    @cached_property
    def failureCause(self):  # pragma: no cover
        return FailureCause.make_one(self.boto3_raw_data["failureCause"])

    failureTimestamp = field("failureTimestamp")
    grantedTimestamp = field("grantedTimestamp")
    targetName = field("targetName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubscribedAssetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SubscribedAssetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSubscriptionGrantStatusInput:
    boto3_raw_data: "type_defs.UpdateSubscriptionGrantStatusInputTypeDef" = (
        dataclasses.field()
    )

    assetIdentifier = field("assetIdentifier")
    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    status = field("status")

    @cached_property
    def failureCause(self):  # pragma: no cover
        return FailureCause.make_one(self.boto3_raw_data["failureCause"])

    targetName = field("targetName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSubscriptionGrantStatusInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSubscriptionGrantStatusInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterClausePaginator:
    boto3_raw_data: "type_defs.FilterClausePaginatorTypeDef" = dataclasses.field()

    and_ = field("and")

    @cached_property
    def filter(self):  # pragma: no cover
        return Filter.make_one(self.boto3_raw_data["filter"])

    or_ = field("or")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FilterClausePaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FilterClausePaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterClause:
    boto3_raw_data: "type_defs.FilterClauseTypeDef" = dataclasses.field()

    and_ = field("and")

    @cached_property
    def filter(self):  # pragma: no cover
        return Filter.make_one(self.boto3_raw_data["filter"])

    or_ = field("or")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterClauseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterClauseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelationalFilterConfigurationOutput:
    boto3_raw_data: "type_defs.RelationalFilterConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    databaseName = field("databaseName")

    @cached_property
    def filterExpressions(self):  # pragma: no cover
        return FilterExpression.make_many(self.boto3_raw_data["filterExpressions"])

    schemaName = field("schemaName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RelationalFilterConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelationalFilterConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelationalFilterConfiguration:
    boto3_raw_data: "type_defs.RelationalFilterConfigurationTypeDef" = (
        dataclasses.field()
    )

    databaseName = field("databaseName")

    @cached_property
    def filterExpressions(self):  # pragma: no cover
        return FilterExpression.make_many(self.boto3_raw_data["filterExpressions"])

    schemaName = field("schemaName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RelationalFilterConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelationalFilterConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormTypeData:
    boto3_raw_data: "type_defs.FormTypeDataTypeDef" = dataclasses.field()

    domainId = field("domainId")
    name = field("name")
    revision = field("revision")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")

    @cached_property
    def imports(self):  # pragma: no cover
        return Import.make_many(self.boto3_raw_data["imports"])

    @cached_property
    def model(self):  # pragma: no cover
        return Model.make_one(self.boto3_raw_data["model"])

    originDomainId = field("originDomainId")
    originProjectId = field("originProjectId")
    owningProjectId = field("owningProjectId")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FormTypeDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FormTypeDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFormTypeOutput:
    boto3_raw_data: "type_defs.GetFormTypeOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")

    @cached_property
    def imports(self):  # pragma: no cover
        return Import.make_many(self.boto3_raw_data["imports"])

    @cached_property
    def model(self):  # pragma: no cover
        return Model.make_one(self.boto3_raw_data["model"])

    name = field("name")
    originDomainId = field("originDomainId")
    originProjectId = field("originProjectId")
    owningProjectId = field("owningProjectId")
    revision = field("revision")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFormTypeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFormTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobRunSummary:
    boto3_raw_data: "type_defs.JobRunSummaryTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    domainId = field("domainId")
    endTime = field("endTime")

    @cached_property
    def error(self):  # pragma: no cover
        return JobRunError.make_one(self.boto3_raw_data["error"])

    jobId = field("jobId")
    jobType = field("jobType")
    runId = field("runId")
    runMode = field("runMode")
    startTime = field("startTime")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobRunSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobRunSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLineageNodeInput:
    boto3_raw_data: "type_defs.GetLineageNodeInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    eventTimestamp = field("eventTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLineageNodeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLineageNodeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLineageEventsInput:
    boto3_raw_data: "type_defs.ListLineageEventsInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    processingStatus = field("processingStatus")
    sortOrder = field("sortOrder")
    timestampAfter = field("timestampAfter")
    timestampBefore = field("timestampBefore")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLineageEventsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLineageEventsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLineageNodeHistoryInput:
    boto3_raw_data: "type_defs.ListLineageNodeHistoryInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    direction = field("direction")
    eventTimestampGTE = field("eventTimestampGTE")
    eventTimestampLTE = field("eventTimestampLTE")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    sortOrder = field("sortOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLineageNodeHistoryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLineageNodeHistoryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNotificationsInput:
    boto3_raw_data: "type_defs.ListNotificationsInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    type = field("type")
    afterTimestamp = field("afterTimestamp")
    beforeTimestamp = field("beforeTimestamp")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    subjects = field("subjects")
    taskStatus = field("taskStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNotificationsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotificationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTimeSeriesDataPointsInput:
    boto3_raw_data: "type_defs.ListTimeSeriesDataPointsInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    entityIdentifier = field("entityIdentifier")
    entityType = field("entityType")
    formName = field("formName")
    endedAt = field("endedAt")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    startedAt = field("startedAt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTimeSeriesDataPointsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTimeSeriesDataPointsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimeSeriesDataPointFormInput:
    boto3_raw_data: "type_defs.TimeSeriesDataPointFormInputTypeDef" = (
        dataclasses.field()
    )

    formName = field("formName")
    timestamp = field("timestamp")
    typeIdentifier = field("typeIdentifier")
    content = field("content")
    typeRevision = field("typeRevision")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimeSeriesDataPointFormInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimeSeriesDataPointFormInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLineageNodeOutput:
    boto3_raw_data: "type_defs.GetLineageNodeOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")

    @cached_property
    def downstreamNodes(self):  # pragma: no cover
        return LineageNodeReference.make_many(self.boto3_raw_data["downstreamNodes"])

    eventTimestamp = field("eventTimestamp")

    @cached_property
    def formsOutput(self):  # pragma: no cover
        return FormOutput.make_many(self.boto3_raw_data["formsOutput"])

    id = field("id")
    name = field("name")
    sourceIdentifier = field("sourceIdentifier")
    typeName = field("typeName")
    typeRevision = field("typeRevision")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def upstreamNodes(self):  # pragma: no cover
        return LineageNodeReference.make_many(self.boto3_raw_data["upstreamNodes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLineageNodeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLineageNodeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMetadataGenerationRunOutput:
    boto3_raw_data: "type_defs.GetMetadataGenerationRunOutputTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    domainId = field("domainId")
    id = field("id")
    owningProjectId = field("owningProjectId")
    status = field("status")

    @cached_property
    def target(self):  # pragma: no cover
        return MetadataGenerationRunTarget.make_one(self.boto3_raw_data["target"])

    type = field("type")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetMetadataGenerationRunOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMetadataGenerationRunOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataGenerationRunItem:
    boto3_raw_data: "type_defs.MetadataGenerationRunItemTypeDef" = dataclasses.field()

    domainId = field("domainId")
    id = field("id")
    owningProjectId = field("owningProjectId")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    status = field("status")

    @cached_property
    def target(self):  # pragma: no cover
        return MetadataGenerationRunTarget.make_one(self.boto3_raw_data["target"])

    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetadataGenerationRunItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataGenerationRunItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMetadataGenerationRunInput:
    boto3_raw_data: "type_defs.StartMetadataGenerationRunInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    owningProjectIdentifier = field("owningProjectIdentifier")

    @cached_property
    def target(self):  # pragma: no cover
        return MetadataGenerationRunTarget.make_one(self.boto3_raw_data["target"])

    type = field("type")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StartMetadataGenerationRunInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMetadataGenerationRunInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTimeSeriesDataPointOutput:
    boto3_raw_data: "type_defs.GetTimeSeriesDataPointOutputTypeDef" = (
        dataclasses.field()
    )

    domainId = field("domainId")
    entityId = field("entityId")
    entityType = field("entityType")

    @cached_property
    def form(self):  # pragma: no cover
        return TimeSeriesDataPointFormOutput.make_one(self.boto3_raw_data["form"])

    formName = field("formName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTimeSeriesDataPointOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTimeSeriesDataPointOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PostTimeSeriesDataPointsOutput:
    boto3_raw_data: "type_defs.PostTimeSeriesDataPointsOutputTypeDef" = (
        dataclasses.field()
    )

    domainId = field("domainId")
    entityId = field("entityId")
    entityType = field("entityType")

    @cached_property
    def forms(self):  # pragma: no cover
        return TimeSeriesDataPointFormOutput.make_many(self.boto3_raw_data["forms"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PostTimeSeriesDataPointsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostTimeSeriesDataPointsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlueSelfGrantStatusOutput:
    boto3_raw_data: "type_defs.GlueSelfGrantStatusOutputTypeDef" = dataclasses.field()

    @cached_property
    def selfGrantStatusDetails(self):  # pragma: no cover
        return SelfGrantStatusDetail.make_many(
            self.boto3_raw_data["selfGrantStatusDetails"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlueSelfGrantStatusOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlueSelfGrantStatusOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftSelfGrantStatusOutput:
    boto3_raw_data: "type_defs.RedshiftSelfGrantStatusOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def selfGrantStatusDetails(self):  # pragma: no cover
        return SelfGrantStatusDetail.make_many(
            self.boto3_raw_data["selfGrantStatusDetails"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RedshiftSelfGrantStatusOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftSelfGrantStatusOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrantedEntityInput:
    boto3_raw_data: "type_defs.GrantedEntityInputTypeDef" = dataclasses.field()

    @cached_property
    def listing(self):  # pragma: no cover
        return ListingRevisionInput.make_one(self.boto3_raw_data["listing"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GrantedEntityInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GrantedEntityInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrantedEntity:
    boto3_raw_data: "type_defs.GrantedEntityTypeDef" = dataclasses.field()

    @cached_property
    def listing(self):  # pragma: no cover
        return ListingRevision.make_one(self.boto3_raw_data["listing"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GrantedEntityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GrantedEntityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchGroupProfilesOutput:
    boto3_raw_data: "type_defs.SearchGroupProfilesOutputTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return GroupProfileSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchGroupProfilesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchGroupProfilesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisioningConfigurationOutput:
    boto3_raw_data: "type_defs.ProvisioningConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def lakeFormationConfiguration(self):  # pragma: no cover
        return LakeFormationConfigurationOutput.make_one(
            self.boto3_raw_data["lakeFormationConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProvisioningConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisioningConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLineageNodeHistoryOutput:
    boto3_raw_data: "type_defs.ListLineageNodeHistoryOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def nodes(self):  # pragma: no cover
        return LineageNodeSummary.make_many(self.boto3_raw_data["nodes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLineageNodeHistoryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLineageNodeHistoryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LineageRunDetails:
    boto3_raw_data: "type_defs.LineageRunDetailsTypeDef" = dataclasses.field()

    @cached_property
    def sqlQueryRunDetails(self):  # pragma: no cover
        return LineageSqlQueryRunDetails.make_one(
            self.boto3_raw_data["sqlQueryRunDetails"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LineageRunDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LineageRunDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftLineageSyncConfigurationInput:
    boto3_raw_data: "type_defs.RedshiftLineageSyncConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    enabled = field("enabled")

    @cached_property
    def schedule(self):  # pragma: no cover
        return LineageSyncSchedule.make_one(self.boto3_raw_data["schedule"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RedshiftLineageSyncConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftLineageSyncConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftLineageSyncConfigurationOutput:
    boto3_raw_data: "type_defs.RedshiftLineageSyncConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    enabled = field("enabled")
    lineageJobId = field("lineageJobId")

    @cached_property
    def schedule(self):  # pragma: no cover
        return LineageSyncSchedule.make_one(self.boto3_raw_data["schedule"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RedshiftLineageSyncConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftLineageSyncConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountPoolsInputPaginate:
    boto3_raw_data: "type_defs.ListAccountPoolsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    name = field("name")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAccountPoolsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountPoolsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountsInAccountPoolInputPaginate:
    boto3_raw_data: "type_defs.ListAccountsInAccountPoolInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccountsInAccountPoolInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountsInAccountPoolInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetFiltersInputPaginate:
    boto3_raw_data: "type_defs.ListAssetFiltersInputPaginateTypeDef" = (
        dataclasses.field()
    )

    assetIdentifier = field("assetIdentifier")
    domainIdentifier = field("domainIdentifier")
    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssetFiltersInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetFiltersInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssetRevisionsInputPaginate:
    boto3_raw_data: "type_defs.ListAssetRevisionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssetRevisionsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssetRevisionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectionsInputPaginate:
    boto3_raw_data: "type_defs.ListConnectionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    projectIdentifier = field("projectIdentifier")
    environmentIdentifier = field("environmentIdentifier")
    name = field("name")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")
    type = field("type")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConnectionsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataProductRevisionsInputPaginate:
    boto3_raw_data: "type_defs.ListDataProductRevisionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataProductRevisionsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataProductRevisionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSourceRunActivitiesInputPaginate:
    boto3_raw_data: "type_defs.ListDataSourceRunActivitiesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataSourceRunActivitiesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSourceRunActivitiesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSourceRunsInputPaginate:
    boto3_raw_data: "type_defs.ListDataSourceRunsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    dataSourceIdentifier = field("dataSourceIdentifier")
    domainIdentifier = field("domainIdentifier")
    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDataSourceRunsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSourceRunsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSourcesInputPaginate:
    boto3_raw_data: "type_defs.ListDataSourcesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    projectIdentifier = field("projectIdentifier")
    connectionIdentifier = field("connectionIdentifier")
    environmentIdentifier = field("environmentIdentifier")
    name = field("name")
    status = field("status")
    type = field("type")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataSourcesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSourcesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainUnitsForParentInputPaginate:
    boto3_raw_data: "type_defs.ListDomainUnitsForParentInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    parentDomainUnitIdentifier = field("parentDomainUnitIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDomainUnitsForParentInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainUnitsForParentInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainsInputPaginate:
    boto3_raw_data: "type_defs.ListDomainsInputPaginateTypeDef" = dataclasses.field()

    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntityOwnersInputPaginate:
    boto3_raw_data: "type_defs.ListEntityOwnersInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    entityIdentifier = field("entityIdentifier")
    entityType = field("entityType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEntityOwnersInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntityOwnersInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentActionsInputPaginate:
    boto3_raw_data: "type_defs.ListEnvironmentActionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    environmentIdentifier = field("environmentIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEnvironmentActionsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentActionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentBlueprintConfigurationsInputPaginate:
    boto3_raw_data: (
        "type_defs.ListEnvironmentBlueprintConfigurationsInputPaginateTypeDef"
    ) = dataclasses.field()

    domainIdentifier = field("domainIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEnvironmentBlueprintConfigurationsInputPaginateTypeDef"
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
                "type_defs.ListEnvironmentBlueprintConfigurationsInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentBlueprintsInputPaginate:
    boto3_raw_data: "type_defs.ListEnvironmentBlueprintsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    managed = field("managed")
    name = field("name")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEnvironmentBlueprintsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentBlueprintsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentProfilesInputPaginate:
    boto3_raw_data: "type_defs.ListEnvironmentProfilesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    awsAccountId = field("awsAccountId")
    awsAccountRegion = field("awsAccountRegion")
    environmentBlueprintIdentifier = field("environmentBlueprintIdentifier")
    name = field("name")
    projectIdentifier = field("projectIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEnvironmentProfilesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentProfilesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentsInputPaginate:
    boto3_raw_data: "type_defs.ListEnvironmentsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    projectIdentifier = field("projectIdentifier")
    awsAccountId = field("awsAccountId")
    awsAccountRegion = field("awsAccountRegion")
    environmentBlueprintIdentifier = field("environmentBlueprintIdentifier")
    environmentProfileIdentifier = field("environmentProfileIdentifier")
    name = field("name")
    provider = field("provider")
    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEnvironmentsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobRunsInputPaginate:
    boto3_raw_data: "type_defs.ListJobRunsInputPaginateTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    jobIdentifier = field("jobIdentifier")
    sortOrder = field("sortOrder")
    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobRunsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobRunsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLineageEventsInputPaginate:
    boto3_raw_data: "type_defs.ListLineageEventsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    processingStatus = field("processingStatus")
    sortOrder = field("sortOrder")
    timestampAfter = field("timestampAfter")
    timestampBefore = field("timestampBefore")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListLineageEventsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLineageEventsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLineageNodeHistoryInputPaginate:
    boto3_raw_data: "type_defs.ListLineageNodeHistoryInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    direction = field("direction")
    eventTimestampGTE = field("eventTimestampGTE")
    eventTimestampLTE = field("eventTimestampLTE")
    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLineageNodeHistoryInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLineageNodeHistoryInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMetadataGenerationRunsInputPaginate:
    boto3_raw_data: "type_defs.ListMetadataGenerationRunsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    status = field("status")
    type = field("type")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListMetadataGenerationRunsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMetadataGenerationRunsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNotificationsInputPaginate:
    boto3_raw_data: "type_defs.ListNotificationsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    type = field("type")
    afterTimestamp = field("afterTimestamp")
    beforeTimestamp = field("beforeTimestamp")
    subjects = field("subjects")
    taskStatus = field("taskStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListNotificationsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotificationsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyGrantsInputPaginate:
    boto3_raw_data: "type_defs.ListPolicyGrantsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    entityIdentifier = field("entityIdentifier")
    entityType = field("entityType")
    policyType = field("policyType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPolicyGrantsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyGrantsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProjectMembershipsInputPaginate:
    boto3_raw_data: "type_defs.ListProjectMembershipsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    projectIdentifier = field("projectIdentifier")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProjectMembershipsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProjectMembershipsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProjectProfilesInputPaginate:
    boto3_raw_data: "type_defs.ListProjectProfilesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    name = field("name")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListProjectProfilesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProjectProfilesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProjectsInputPaginate:
    boto3_raw_data: "type_defs.ListProjectsInputPaginateTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    groupIdentifier = field("groupIdentifier")
    name = field("name")
    userIdentifier = field("userIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProjectsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProjectsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRulesInputPaginate:
    boto3_raw_data: "type_defs.ListRulesInputPaginateTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    targetIdentifier = field("targetIdentifier")
    targetType = field("targetType")
    action = field("action")
    assetTypes = field("assetTypes")
    dataProduct = field("dataProduct")
    includeCascaded = field("includeCascaded")
    projectIds = field("projectIds")
    ruleType = field("ruleType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRulesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRulesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubscriptionGrantsInputPaginate:
    boto3_raw_data: "type_defs.ListSubscriptionGrantsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    environmentId = field("environmentId")
    owningProjectId = field("owningProjectId")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")
    subscribedListingId = field("subscribedListingId")
    subscriptionId = field("subscriptionId")
    subscriptionTargetId = field("subscriptionTargetId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSubscriptionGrantsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubscriptionGrantsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubscriptionRequestsInputPaginate:
    boto3_raw_data: "type_defs.ListSubscriptionRequestsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    approverProjectId = field("approverProjectId")
    owningProjectId = field("owningProjectId")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")
    status = field("status")
    subscribedListingId = field("subscribedListingId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSubscriptionRequestsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubscriptionRequestsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubscriptionTargetsInputPaginate:
    boto3_raw_data: "type_defs.ListSubscriptionTargetsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    environmentIdentifier = field("environmentIdentifier")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSubscriptionTargetsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubscriptionTargetsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubscriptionsInputPaginate:
    boto3_raw_data: "type_defs.ListSubscriptionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    approverProjectId = field("approverProjectId")
    owningProjectId = field("owningProjectId")
    sortBy = field("sortBy")
    sortOrder = field("sortOrder")
    status = field("status")
    subscribedListingId = field("subscribedListingId")
    subscriptionRequestIdentifier = field("subscriptionRequestIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSubscriptionsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubscriptionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTimeSeriesDataPointsInputPaginate:
    boto3_raw_data: "type_defs.ListTimeSeriesDataPointsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    entityIdentifier = field("entityIdentifier")
    entityType = field("entityType")
    formName = field("formName")
    endedAt = field("endedAt")
    startedAt = field("startedAt")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTimeSeriesDataPointsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTimeSeriesDataPointsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchGroupProfilesInputPaginate:
    boto3_raw_data: "type_defs.SearchGroupProfilesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    groupType = field("groupType")
    searchText = field("searchText")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchGroupProfilesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchGroupProfilesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchUserProfilesInputPaginate:
    boto3_raw_data: "type_defs.SearchUserProfilesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    userType = field("userType")
    searchText = field("searchText")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchUserProfilesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchUserProfilesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProjectProfilesOutput:
    boto3_raw_data: "type_defs.ListProjectProfilesOutputTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return ProjectProfileSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProjectProfilesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProjectProfilesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextMatchItem:
    boto3_raw_data: "type_defs.TextMatchItemTypeDef" = dataclasses.field()

    attribute = field("attribute")

    @cached_property
    def matchOffsets(self):  # pragma: no cover
        return MatchOffset.make_many(self.boto3_raw_data["matchOffsets"])

    text = field("text")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TextMatchItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TextMatchItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberDetails:
    boto3_raw_data: "type_defs.MemberDetailsTypeDef" = dataclasses.field()

    @cached_property
    def group(self):  # pragma: no cover
        return GroupDetails.make_one(self.boto3_raw_data["group"])

    @cached_property
    def user(self):  # pragma: no cover
        return UserDetails.make_one(self.boto3_raw_data["user"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MemberDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MemberDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataFormEnforcementDetailOutput:
    boto3_raw_data: "type_defs.MetadataFormEnforcementDetailOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def requiredMetadataForms(self):  # pragma: no cover
        return MetadataFormReference.make_many(
            self.boto3_raw_data["requiredMetadataForms"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MetadataFormEnforcementDetailOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataFormEnforcementDetailOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataFormEnforcementDetail:
    boto3_raw_data: "type_defs.MetadataFormEnforcementDetailTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def requiredMetadataForms(self):  # pragma: no cover
        return MetadataFormReference.make_many(
            self.boto3_raw_data["requiredMetadataForms"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MetadataFormEnforcementDetailTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataFormEnforcementDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenLineageRunEventSummary:
    boto3_raw_data: "type_defs.OpenLineageRunEventSummaryTypeDef" = dataclasses.field()

    eventType = field("eventType")

    @cached_property
    def inputs(self):  # pragma: no cover
        return NameIdentifier.make_many(self.boto3_raw_data["inputs"])

    @cached_property
    def job(self):  # pragma: no cover
        return NameIdentifier.make_one(self.boto3_raw_data["job"])

    @cached_property
    def outputs(self):  # pragma: no cover
        return NameIdentifier.make_many(self.boto3_raw_data["outputs"])

    runId = field("runId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpenLineageRunEventSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenLineageRunEventSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RowFilterExpressionOutput:
    boto3_raw_data: "type_defs.RowFilterExpressionOutputTypeDef" = dataclasses.field()

    @cached_property
    def equalTo(self):  # pragma: no cover
        return EqualToExpression.make_one(self.boto3_raw_data["equalTo"])

    @cached_property
    def greaterThan(self):  # pragma: no cover
        return GreaterThanExpression.make_one(self.boto3_raw_data["greaterThan"])

    @cached_property
    def greaterThanOrEqualTo(self):  # pragma: no cover
        return GreaterThanOrEqualToExpression.make_one(
            self.boto3_raw_data["greaterThanOrEqualTo"]
        )

    @cached_property
    def in_(self):  # pragma: no cover
        return InExpressionOutput.make_one(self.boto3_raw_data["in"])

    @cached_property
    def isNotNull(self):  # pragma: no cover
        return IsNotNullExpression.make_one(self.boto3_raw_data["isNotNull"])

    @cached_property
    def isNull(self):  # pragma: no cover
        return IsNullExpression.make_one(self.boto3_raw_data["isNull"])

    @cached_property
    def lessThan(self):  # pragma: no cover
        return LessThanExpression.make_one(self.boto3_raw_data["lessThan"])

    @cached_property
    def lessThanOrEqualTo(self):  # pragma: no cover
        return LessThanOrEqualToExpression.make_one(
            self.boto3_raw_data["lessThanOrEqualTo"]
        )

    @cached_property
    def like(self):  # pragma: no cover
        return LikeExpression.make_one(self.boto3_raw_data["like"])

    @cached_property
    def notEqualTo(self):  # pragma: no cover
        return NotEqualToExpression.make_one(self.boto3_raw_data["notEqualTo"])

    @cached_property
    def notIn(self):  # pragma: no cover
        return NotInExpressionOutput.make_one(self.boto3_raw_data["notIn"])

    @cached_property
    def notLike(self):  # pragma: no cover
        return NotLikeExpression.make_one(self.boto3_raw_data["notLike"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RowFilterExpressionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RowFilterExpressionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RowFilterExpression:
    boto3_raw_data: "type_defs.RowFilterExpressionTypeDef" = dataclasses.field()

    @cached_property
    def equalTo(self):  # pragma: no cover
        return EqualToExpression.make_one(self.boto3_raw_data["equalTo"])

    @cached_property
    def greaterThan(self):  # pragma: no cover
        return GreaterThanExpression.make_one(self.boto3_raw_data["greaterThan"])

    @cached_property
    def greaterThanOrEqualTo(self):  # pragma: no cover
        return GreaterThanOrEqualToExpression.make_one(
            self.boto3_raw_data["greaterThanOrEqualTo"]
        )

    @cached_property
    def in_(self):  # pragma: no cover
        return InExpression.make_one(self.boto3_raw_data["in"])

    @cached_property
    def isNotNull(self):  # pragma: no cover
        return IsNotNullExpression.make_one(self.boto3_raw_data["isNotNull"])

    @cached_property
    def isNull(self):  # pragma: no cover
        return IsNullExpression.make_one(self.boto3_raw_data["isNull"])

    @cached_property
    def lessThan(self):  # pragma: no cover
        return LessThanExpression.make_one(self.boto3_raw_data["lessThan"])

    @cached_property
    def lessThanOrEqualTo(self):  # pragma: no cover
        return LessThanOrEqualToExpression.make_one(
            self.boto3_raw_data["lessThanOrEqualTo"]
        )

    @cached_property
    def like(self):  # pragma: no cover
        return LikeExpression.make_one(self.boto3_raw_data["like"])

    @cached_property
    def notEqualTo(self):  # pragma: no cover
        return NotEqualToExpression.make_one(self.boto3_raw_data["notEqualTo"])

    @cached_property
    def notIn(self):  # pragma: no cover
        return NotInExpression.make_one(self.boto3_raw_data["notIn"])

    @cached_property
    def notLike(self):  # pragma: no cover
        return NotLikeExpression.make_one(self.boto3_raw_data["notLike"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RowFilterExpressionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RowFilterExpressionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Topic:
    boto3_raw_data: "type_defs.TopicTypeDef" = dataclasses.field()

    @cached_property
    def resource(self):  # pragma: no cover
        return NotificationResource.make_one(self.boto3_raw_data["resource"])

    role = field("role")
    subject = field("subject")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TopicTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TopicTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OAuth2PropertiesOutput:
    boto3_raw_data: "type_defs.OAuth2PropertiesOutputTypeDef" = dataclasses.field()

    @cached_property
    def authorizationCodeProperties(self):  # pragma: no cover
        return AuthorizationCodeProperties.make_one(
            self.boto3_raw_data["authorizationCodeProperties"]
        )

    @cached_property
    def oAuth2ClientApplication(self):  # pragma: no cover
        return OAuth2ClientApplication.make_one(
            self.boto3_raw_data["oAuth2ClientApplication"]
        )

    @cached_property
    def oAuth2Credentials(self):  # pragma: no cover
        return GlueOAuth2Credentials.make_one(self.boto3_raw_data["oAuth2Credentials"])

    oAuth2GrantType = field("oAuth2GrantType")
    tokenUrl = field("tokenUrl")
    tokenUrlParametersMap = field("tokenUrlParametersMap")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OAuth2PropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OAuth2PropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OAuth2Properties:
    boto3_raw_data: "type_defs.OAuth2PropertiesTypeDef" = dataclasses.field()

    @cached_property
    def authorizationCodeProperties(self):  # pragma: no cover
        return AuthorizationCodeProperties.make_one(
            self.boto3_raw_data["authorizationCodeProperties"]
        )

    @cached_property
    def oAuth2ClientApplication(self):  # pragma: no cover
        return OAuth2ClientApplication.make_one(
            self.boto3_raw_data["oAuth2ClientApplication"]
        )

    @cached_property
    def oAuth2Credentials(self):  # pragma: no cover
        return GlueOAuth2Credentials.make_one(self.boto3_raw_data["oAuth2Credentials"])

    oAuth2GrantType = field("oAuth2GrantType")
    tokenUrl = field("tokenUrl")
    tokenUrlParametersMap = field("tokenUrlParametersMap")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OAuth2PropertiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OAuth2PropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OwnerPropertiesOutput:
    boto3_raw_data: "type_defs.OwnerPropertiesOutputTypeDef" = dataclasses.field()

    @cached_property
    def group(self):  # pragma: no cover
        return OwnerGroupPropertiesOutput.make_one(self.boto3_raw_data["group"])

    @cached_property
    def user(self):  # pragma: no cover
        return OwnerUserPropertiesOutput.make_one(self.boto3_raw_data["user"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OwnerPropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OwnerPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OwnerProperties:
    boto3_raw_data: "type_defs.OwnerPropertiesTypeDef" = dataclasses.field()

    @cached_property
    def group(self):  # pragma: no cover
        return OwnerGroupProperties.make_one(self.boto3_raw_data["group"])

    @cached_property
    def user(self):  # pragma: no cover
        return OwnerUserProperties.make_one(self.boto3_raw_data["user"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OwnerPropertiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OwnerPropertiesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyGrantDetailOutput:
    boto3_raw_data: "type_defs.PolicyGrantDetailOutputTypeDef" = dataclasses.field()

    @cached_property
    def addToProjectMemberPool(self):  # pragma: no cover
        return AddToProjectMemberPoolPolicyGrantDetail.make_one(
            self.boto3_raw_data["addToProjectMemberPool"]
        )

    @cached_property
    def createAssetType(self):  # pragma: no cover
        return CreateAssetTypePolicyGrantDetail.make_one(
            self.boto3_raw_data["createAssetType"]
        )

    @cached_property
    def createDomainUnit(self):  # pragma: no cover
        return CreateDomainUnitPolicyGrantDetail.make_one(
            self.boto3_raw_data["createDomainUnit"]
        )

    createEnvironment = field("createEnvironment")
    createEnvironmentFromBlueprint = field("createEnvironmentFromBlueprint")

    @cached_property
    def createEnvironmentProfile(self):  # pragma: no cover
        return CreateEnvironmentProfilePolicyGrantDetail.make_one(
            self.boto3_raw_data["createEnvironmentProfile"]
        )

    @cached_property
    def createFormType(self):  # pragma: no cover
        return CreateFormTypePolicyGrantDetail.make_one(
            self.boto3_raw_data["createFormType"]
        )

    @cached_property
    def createGlossary(self):  # pragma: no cover
        return CreateGlossaryPolicyGrantDetail.make_one(
            self.boto3_raw_data["createGlossary"]
        )

    @cached_property
    def createProject(self):  # pragma: no cover
        return CreateProjectPolicyGrantDetail.make_one(
            self.boto3_raw_data["createProject"]
        )

    @cached_property
    def createProjectFromProjectProfile(self):  # pragma: no cover
        return CreateProjectFromProjectProfilePolicyGrantDetailOutput.make_one(
            self.boto3_raw_data["createProjectFromProjectProfile"]
        )

    delegateCreateEnvironmentProfile = field("delegateCreateEnvironmentProfile")

    @cached_property
    def overrideDomainUnitOwners(self):  # pragma: no cover
        return OverrideDomainUnitOwnersPolicyGrantDetail.make_one(
            self.boto3_raw_data["overrideDomainUnitOwners"]
        )

    @cached_property
    def overrideProjectOwners(self):  # pragma: no cover
        return OverrideProjectOwnersPolicyGrantDetail.make_one(
            self.boto3_raw_data["overrideProjectOwners"]
        )

    @cached_property
    def useAssetType(self):  # pragma: no cover
        return UseAssetTypePolicyGrantDetail.make_one(
            self.boto3_raw_data["useAssetType"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolicyGrantDetailOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyGrantDetailOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyGrantDetail:
    boto3_raw_data: "type_defs.PolicyGrantDetailTypeDef" = dataclasses.field()

    @cached_property
    def addToProjectMemberPool(self):  # pragma: no cover
        return AddToProjectMemberPoolPolicyGrantDetail.make_one(
            self.boto3_raw_data["addToProjectMemberPool"]
        )

    @cached_property
    def createAssetType(self):  # pragma: no cover
        return CreateAssetTypePolicyGrantDetail.make_one(
            self.boto3_raw_data["createAssetType"]
        )

    @cached_property
    def createDomainUnit(self):  # pragma: no cover
        return CreateDomainUnitPolicyGrantDetail.make_one(
            self.boto3_raw_data["createDomainUnit"]
        )

    createEnvironment = field("createEnvironment")
    createEnvironmentFromBlueprint = field("createEnvironmentFromBlueprint")

    @cached_property
    def createEnvironmentProfile(self):  # pragma: no cover
        return CreateEnvironmentProfilePolicyGrantDetail.make_one(
            self.boto3_raw_data["createEnvironmentProfile"]
        )

    @cached_property
    def createFormType(self):  # pragma: no cover
        return CreateFormTypePolicyGrantDetail.make_one(
            self.boto3_raw_data["createFormType"]
        )

    @cached_property
    def createGlossary(self):  # pragma: no cover
        return CreateGlossaryPolicyGrantDetail.make_one(
            self.boto3_raw_data["createGlossary"]
        )

    @cached_property
    def createProject(self):  # pragma: no cover
        return CreateProjectPolicyGrantDetail.make_one(
            self.boto3_raw_data["createProject"]
        )

    @cached_property
    def createProjectFromProjectProfile(self):  # pragma: no cover
        return CreateProjectFromProjectProfilePolicyGrantDetail.make_one(
            self.boto3_raw_data["createProjectFromProjectProfile"]
        )

    delegateCreateEnvironmentProfile = field("delegateCreateEnvironmentProfile")

    @cached_property
    def overrideDomainUnitOwners(self):  # pragma: no cover
        return OverrideDomainUnitOwnersPolicyGrantDetail.make_one(
            self.boto3_raw_data["overrideDomainUnitOwners"]
        )

    @cached_property
    def overrideProjectOwners(self):  # pragma: no cover
        return OverrideProjectOwnersPolicyGrantDetail.make_one(
            self.boto3_raw_data["overrideProjectOwners"]
        )

    @cached_property
    def useAssetType(self):  # pragma: no cover
        return UseAssetTypePolicyGrantDetail.make_one(
            self.boto3_raw_data["useAssetType"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyGrantDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyGrantDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleScopeOutput:
    boto3_raw_data: "type_defs.RuleScopeOutputTypeDef" = dataclasses.field()

    @cached_property
    def assetType(self):  # pragma: no cover
        return AssetTypesForRuleOutput.make_one(self.boto3_raw_data["assetType"])

    dataProduct = field("dataProduct")

    @cached_property
    def project(self):  # pragma: no cover
        return ProjectsForRuleOutput.make_one(self.boto3_raw_data["project"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleScopeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleScopeOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleScope:
    boto3_raw_data: "type_defs.RuleScopeTypeDef" = dataclasses.field()

    @cached_property
    def assetType(self):  # pragma: no cover
        return AssetTypesForRule.make_one(self.boto3_raw_data["assetType"])

    dataProduct = field("dataProduct")

    @cached_property
    def project(self):  # pragma: no cover
        return ProjectsForRule.make_one(self.boto3_raw_data["project"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleScopeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleScopeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftCredentials:
    boto3_raw_data: "type_defs.RedshiftCredentialsTypeDef" = dataclasses.field()

    secretArn = field("secretArn")

    @cached_property
    def usernamePassword(self):  # pragma: no cover
        return UsernamePassword.make_one(self.boto3_raw_data["usernamePassword"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedshiftCredentialsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SparkEmrPropertiesOutput:
    boto3_raw_data: "type_defs.SparkEmrPropertiesOutputTypeDef" = dataclasses.field()

    computeArn = field("computeArn")

    @cached_property
    def credentials(self):  # pragma: no cover
        return UsernamePassword.make_one(self.boto3_raw_data["credentials"])

    credentialsExpiration = field("credentialsExpiration")
    governanceType = field("governanceType")
    instanceProfileArn = field("instanceProfileArn")
    javaVirtualEnv = field("javaVirtualEnv")
    livyEndpoint = field("livyEndpoint")
    logUri = field("logUri")
    pythonVirtualEnv = field("pythonVirtualEnv")
    runtimeRole = field("runtimeRole")
    trustedCertificatesS3Uri = field("trustedCertificatesS3Uri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SparkEmrPropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SparkEmrPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftStorage:
    boto3_raw_data: "type_defs.RedshiftStorageTypeDef" = dataclasses.field()

    @cached_property
    def redshiftClusterSource(self):  # pragma: no cover
        return RedshiftClusterStorage.make_one(
            self.boto3_raw_data["redshiftClusterSource"]
        )

    @cached_property
    def redshiftServerlessSource(self):  # pragma: no cover
        return RedshiftServerlessStorage.make_one(
            self.boto3_raw_data["redshiftServerlessSource"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RedshiftStorageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RedshiftStorageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectPredictionsInput:
    boto3_raw_data: "type_defs.RejectPredictionsInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    clientToken = field("clientToken")

    @cached_property
    def rejectChoices(self):  # pragma: no cover
        return RejectChoice.make_many(self.boto3_raw_data["rejectChoices"])

    @cached_property
    def rejectRule(self):  # pragma: no cover
        return RejectRule.make_one(self.boto3_raw_data["rejectRule"])

    revision = field("revision")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RejectPredictionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectPredictionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SparkGluePropertiesInput:
    boto3_raw_data: "type_defs.SparkGluePropertiesInputTypeDef" = dataclasses.field()

    @cached_property
    def additionalArgs(self):  # pragma: no cover
        return SparkGlueArgs.make_one(self.boto3_raw_data["additionalArgs"])

    glueConnectionName = field("glueConnectionName")
    glueVersion = field("glueVersion")
    idleTimeout = field("idleTimeout")
    javaVirtualEnv = field("javaVirtualEnv")
    numberOfWorkers = field("numberOfWorkers")
    pythonVirtualEnv = field("pythonVirtualEnv")
    workerType = field("workerType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SparkGluePropertiesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SparkGluePropertiesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SparkGluePropertiesOutput:
    boto3_raw_data: "type_defs.SparkGluePropertiesOutputTypeDef" = dataclasses.field()

    @cached_property
    def additionalArgs(self):  # pragma: no cover
        return SparkGlueArgs.make_one(self.boto3_raw_data["additionalArgs"])

    glueConnectionName = field("glueConnectionName")
    glueVersion = field("glueVersion")
    idleTimeout = field("idleTimeout")
    javaVirtualEnv = field("javaVirtualEnv")
    numberOfWorkers = field("numberOfWorkers")
    pythonVirtualEnv = field("pythonVirtualEnv")
    workerType = field("workerType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SparkGluePropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SparkGluePropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserProfileDetails:
    boto3_raw_data: "type_defs.UserProfileDetailsTypeDef" = dataclasses.field()

    @cached_property
    def iam(self):  # pragma: no cover
        return IamUserProfileDetails.make_one(self.boto3_raw_data["iam"])

    @cached_property
    def sso(self):  # pragma: no cover
        return SsoUserProfileDetails.make_one(self.boto3_raw_data["sso"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserProfileDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserProfileDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscribedPrincipalInput:
    boto3_raw_data: "type_defs.SubscribedPrincipalInputTypeDef" = dataclasses.field()

    @cached_property
    def project(self):  # pragma: no cover
        return SubscribedProjectInput.make_one(self.boto3_raw_data["project"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubscribedPrincipalInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscribedPrincipalInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscribedPrincipal:
    boto3_raw_data: "type_defs.SubscribedPrincipalTypeDef" = dataclasses.field()

    @cached_property
    def project(self):  # pragma: no cover
        return SubscribedProject.make_one(self.boto3_raw_data["project"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubscribedPrincipalTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscribedPrincipalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccountPoolOutput:
    boto3_raw_data: "type_defs.CreateAccountPoolOutputTypeDef" = dataclasses.field()

    @cached_property
    def accountSource(self):  # pragma: no cover
        return AccountSourceOutput.make_one(self.boto3_raw_data["accountSource"])

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")
    domainUnitId = field("domainUnitId")
    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    resolutionStrategy = field("resolutionStrategy")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccountPoolOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccountPoolOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccountPoolOutput:
    boto3_raw_data: "type_defs.GetAccountPoolOutputTypeDef" = dataclasses.field()

    @cached_property
    def accountSource(self):  # pragma: no cover
        return AccountSourceOutput.make_one(self.boto3_raw_data["accountSource"])

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")
    domainUnitId = field("domainUnitId")
    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    resolutionStrategy = field("resolutionStrategy")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccountPoolOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountPoolOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccountPoolOutput:
    boto3_raw_data: "type_defs.UpdateAccountPoolOutputTypeDef" = dataclasses.field()

    @cached_property
    def accountSource(self):  # pragma: no cover
        return AccountSourceOutput.make_one(self.boto3_raw_data["accountSource"])

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")
    domainUnitId = field("domainUnitId")
    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    resolutionStrategy = field("resolutionStrategy")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAccountPoolOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccountPoolOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentActionInput:
    boto3_raw_data: "type_defs.CreateEnvironmentActionInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    environmentIdentifier = field("environmentIdentifier")
    name = field("name")

    @cached_property
    def parameters(self):  # pragma: no cover
        return ActionParameters.make_one(self.boto3_raw_data["parameters"])

    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEnvironmentActionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentActionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentActionOutput:
    boto3_raw_data: "type_defs.CreateEnvironmentActionOutputTypeDef" = (
        dataclasses.field()
    )

    description = field("description")
    domainId = field("domainId")
    environmentId = field("environmentId")
    id = field("id")
    name = field("name")

    @cached_property
    def parameters(self):  # pragma: no cover
        return ActionParameters.make_one(self.boto3_raw_data["parameters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateEnvironmentActionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentActionSummary:
    boto3_raw_data: "type_defs.EnvironmentActionSummaryTypeDef" = dataclasses.field()

    domainId = field("domainId")
    environmentId = field("environmentId")
    id = field("id")
    name = field("name")

    @cached_property
    def parameters(self):  # pragma: no cover
        return ActionParameters.make_one(self.boto3_raw_data["parameters"])

    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentActionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentActionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentActionOutput:
    boto3_raw_data: "type_defs.GetEnvironmentActionOutputTypeDef" = dataclasses.field()

    description = field("description")
    domainId = field("domainId")
    environmentId = field("environmentId")
    id = field("id")
    name = field("name")

    @cached_property
    def parameters(self):  # pragma: no cover
        return ActionParameters.make_one(self.boto3_raw_data["parameters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEnvironmentActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEnvironmentActionInput:
    boto3_raw_data: "type_defs.UpdateEnvironmentActionInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    environmentIdentifier = field("environmentIdentifier")
    identifier = field("identifier")
    description = field("description")
    name = field("name")

    @cached_property
    def parameters(self):  # pragma: no cover
        return ActionParameters.make_one(self.boto3_raw_data["parameters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEnvironmentActionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnvironmentActionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEnvironmentActionOutput:
    boto3_raw_data: "type_defs.UpdateEnvironmentActionOutputTypeDef" = (
        dataclasses.field()
    )

    description = field("description")
    domainId = field("domainId")
    environmentId = field("environmentId")
    id = field("id")
    name = field("name")

    @cached_property
    def parameters(self):  # pragma: no cover
        return ActionParameters.make_one(self.boto3_raw_data["parameters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateEnvironmentActionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnvironmentActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProductListing:
    boto3_raw_data: "type_defs.DataProductListingTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    dataProductId = field("dataProductId")
    dataProductRevision = field("dataProductRevision")
    forms = field("forms")

    @cached_property
    def glossaryTerms(self):  # pragma: no cover
        return DetailedGlossaryTerm.make_many(self.boto3_raw_data["glossaryTerms"])

    @cached_property
    def items(self):  # pragma: no cover
        return ListingSummary.make_many(self.boto3_raw_data["items"])

    owningProjectId = field("owningProjectId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataProductListingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataProductListingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscribedListingItem:
    boto3_raw_data: "type_defs.SubscribedListingItemTypeDef" = dataclasses.field()

    @cached_property
    def assetListing(self):  # pragma: no cover
        return SubscribedAssetListing.make_one(self.boto3_raw_data["assetListing"])

    @cached_property
    def productListing(self):  # pragma: no cover
        return SubscribedProductListing.make_one(self.boto3_raw_data["productListing"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubscribedListingItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscribedListingItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlueConnectionPatch:
    boto3_raw_data: "type_defs.GlueConnectionPatchTypeDef" = dataclasses.field()

    @cached_property
    def authenticationConfiguration(self):  # pragma: no cover
        return AuthenticationConfigurationPatch.make_one(
            self.boto3_raw_data["authenticationConfiguration"]
        )

    connectionProperties = field("connectionProperties")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlueConnectionPatchTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlueConnectionPatchTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssetInput:
    boto3_raw_data: "type_defs.CreateAssetInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    name = field("name")
    owningProjectIdentifier = field("owningProjectIdentifier")
    typeIdentifier = field("typeIdentifier")
    clientToken = field("clientToken")
    description = field("description")
    externalIdentifier = field("externalIdentifier")

    @cached_property
    def formsInput(self):  # pragma: no cover
        return FormInput.make_many(self.boto3_raw_data["formsInput"])

    glossaryTerms = field("glossaryTerms")

    @cached_property
    def predictionConfiguration(self):  # pragma: no cover
        return PredictionConfiguration.make_one(
            self.boto3_raw_data["predictionConfiguration"]
        )

    typeRevision = field("typeRevision")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateAssetInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssetOutput:
    boto3_raw_data: "type_defs.CreateAssetOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")
    externalIdentifier = field("externalIdentifier")
    firstRevisionCreatedAt = field("firstRevisionCreatedAt")
    firstRevisionCreatedBy = field("firstRevisionCreatedBy")

    @cached_property
    def formsOutput(self):  # pragma: no cover
        return FormOutput.make_many(self.boto3_raw_data["formsOutput"])

    glossaryTerms = field("glossaryTerms")
    governedGlossaryTerms = field("governedGlossaryTerms")
    id = field("id")

    @cached_property
    def latestTimeSeriesDataPointFormsOutput(self):  # pragma: no cover
        return TimeSeriesDataPointSummaryFormOutput.make_many(
            self.boto3_raw_data["latestTimeSeriesDataPointFormsOutput"]
        )

    @cached_property
    def listing(self):  # pragma: no cover
        return AssetListingDetails.make_one(self.boto3_raw_data["listing"])

    name = field("name")
    owningProjectId = field("owningProjectId")

    @cached_property
    def predictionConfiguration(self):  # pragma: no cover
        return PredictionConfiguration.make_one(
            self.boto3_raw_data["predictionConfiguration"]
        )

    @cached_property
    def readOnlyFormsOutput(self):  # pragma: no cover
        return FormOutput.make_many(self.boto3_raw_data["readOnlyFormsOutput"])

    revision = field("revision")
    typeIdentifier = field("typeIdentifier")
    typeRevision = field("typeRevision")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateAssetOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssetRevisionInput:
    boto3_raw_data: "type_defs.CreateAssetRevisionInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    name = field("name")
    clientToken = field("clientToken")
    description = field("description")

    @cached_property
    def formsInput(self):  # pragma: no cover
        return FormInput.make_many(self.boto3_raw_data["formsInput"])

    glossaryTerms = field("glossaryTerms")

    @cached_property
    def predictionConfiguration(self):  # pragma: no cover
        return PredictionConfiguration.make_one(
            self.boto3_raw_data["predictionConfiguration"]
        )

    typeRevision = field("typeRevision")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAssetRevisionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssetRevisionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssetRevisionOutput:
    boto3_raw_data: "type_defs.CreateAssetRevisionOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")
    externalIdentifier = field("externalIdentifier")
    firstRevisionCreatedAt = field("firstRevisionCreatedAt")
    firstRevisionCreatedBy = field("firstRevisionCreatedBy")

    @cached_property
    def formsOutput(self):  # pragma: no cover
        return FormOutput.make_many(self.boto3_raw_data["formsOutput"])

    glossaryTerms = field("glossaryTerms")
    governedGlossaryTerms = field("governedGlossaryTerms")
    id = field("id")

    @cached_property
    def latestTimeSeriesDataPointFormsOutput(self):  # pragma: no cover
        return TimeSeriesDataPointSummaryFormOutput.make_many(
            self.boto3_raw_data["latestTimeSeriesDataPointFormsOutput"]
        )

    @cached_property
    def listing(self):  # pragma: no cover
        return AssetListingDetails.make_one(self.boto3_raw_data["listing"])

    name = field("name")
    owningProjectId = field("owningProjectId")

    @cached_property
    def predictionConfiguration(self):  # pragma: no cover
        return PredictionConfiguration.make_one(
            self.boto3_raw_data["predictionConfiguration"]
        )

    @cached_property
    def readOnlyFormsOutput(self):  # pragma: no cover
        return FormOutput.make_many(self.boto3_raw_data["readOnlyFormsOutput"])

    revision = field("revision")
    typeIdentifier = field("typeIdentifier")
    typeRevision = field("typeRevision")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAssetRevisionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssetRevisionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentBlueprintInput:
    boto3_raw_data: "type_defs.CreateEnvironmentBlueprintInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    name = field("name")

    @cached_property
    def provisioningProperties(self):  # pragma: no cover
        return ProvisioningProperties.make_one(
            self.boto3_raw_data["provisioningProperties"]
        )

    description = field("description")

    @cached_property
    def userParameters(self):  # pragma: no cover
        return CustomParameter.make_many(self.boto3_raw_data["userParameters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateEnvironmentBlueprintInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentBlueprintInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentBlueprintOutput:
    boto3_raw_data: "type_defs.CreateEnvironmentBlueprintOutputTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")

    @cached_property
    def deploymentProperties(self):  # pragma: no cover
        return DeploymentProperties.make_one(
            self.boto3_raw_data["deploymentProperties"]
        )

    description = field("description")
    glossaryTerms = field("glossaryTerms")
    id = field("id")
    name = field("name")
    provider = field("provider")

    @cached_property
    def provisioningProperties(self):  # pragma: no cover
        return ProvisioningProperties.make_one(
            self.boto3_raw_data["provisioningProperties"]
        )

    updatedAt = field("updatedAt")

    @cached_property
    def userParameters(self):  # pragma: no cover
        return CustomParameter.make_many(self.boto3_raw_data["userParameters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateEnvironmentBlueprintOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentBlueprintOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentBlueprintSummary:
    boto3_raw_data: "type_defs.EnvironmentBlueprintSummaryTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    provider = field("provider")

    @cached_property
    def provisioningProperties(self):  # pragma: no cover
        return ProvisioningProperties.make_one(
            self.boto3_raw_data["provisioningProperties"]
        )

    createdAt = field("createdAt")
    description = field("description")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentBlueprintSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentBlueprintSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentBlueprintOutput:
    boto3_raw_data: "type_defs.GetEnvironmentBlueprintOutputTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")

    @cached_property
    def deploymentProperties(self):  # pragma: no cover
        return DeploymentProperties.make_one(
            self.boto3_raw_data["deploymentProperties"]
        )

    description = field("description")
    glossaryTerms = field("glossaryTerms")
    id = field("id")
    name = field("name")
    provider = field("provider")

    @cached_property
    def provisioningProperties(self):  # pragma: no cover
        return ProvisioningProperties.make_one(
            self.boto3_raw_data["provisioningProperties"]
        )

    updatedAt = field("updatedAt")

    @cached_property
    def userParameters(self):  # pragma: no cover
        return CustomParameter.make_many(self.boto3_raw_data["userParameters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetEnvironmentBlueprintOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentBlueprintOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEnvironmentBlueprintInput:
    boto3_raw_data: "type_defs.UpdateEnvironmentBlueprintInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    description = field("description")

    @cached_property
    def provisioningProperties(self):  # pragma: no cover
        return ProvisioningProperties.make_one(
            self.boto3_raw_data["provisioningProperties"]
        )

    @cached_property
    def userParameters(self):  # pragma: no cover
        return CustomParameter.make_many(self.boto3_raw_data["userParameters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateEnvironmentBlueprintInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnvironmentBlueprintInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEnvironmentBlueprintOutput:
    boto3_raw_data: "type_defs.UpdateEnvironmentBlueprintOutputTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")

    @cached_property
    def deploymentProperties(self):  # pragma: no cover
        return DeploymentProperties.make_one(
            self.boto3_raw_data["deploymentProperties"]
        )

    description = field("description")
    glossaryTerms = field("glossaryTerms")
    id = field("id")
    name = field("name")
    provider = field("provider")

    @cached_property
    def provisioningProperties(self):  # pragma: no cover
        return ProvisioningProperties.make_one(
            self.boto3_raw_data["provisioningProperties"]
        )

    updatedAt = field("updatedAt")

    @cached_property
    def userParameters(self):  # pragma: no cover
        return CustomParameter.make_many(self.boto3_raw_data["userParameters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateEnvironmentBlueprintOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnvironmentBlueprintOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSourcesOutput:
    boto3_raw_data: "type_defs.ListDataSourcesOutputTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return DataSourceSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataSourcesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSourcesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProjectsOutput:
    boto3_raw_data: "type_defs.ListProjectsOutputTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return ProjectSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProjectsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProjectsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubscriptionTargetsOutput:
    boto3_raw_data: "type_defs.ListSubscriptionTargetsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return SubscriptionTargetSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSubscriptionTargetsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubscriptionTargetsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataProductInput:
    boto3_raw_data: "type_defs.CreateDataProductInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    name = field("name")
    owningProjectIdentifier = field("owningProjectIdentifier")
    clientToken = field("clientToken")
    description = field("description")

    @cached_property
    def formsInput(self):  # pragma: no cover
        return FormInput.make_many(self.boto3_raw_data["formsInput"])

    glossaryTerms = field("glossaryTerms")
    items = field("items")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataProductInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataProductInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataProductRevisionInput:
    boto3_raw_data: "type_defs.CreateDataProductRevisionInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    name = field("name")
    clientToken = field("clientToken")
    description = field("description")

    @cached_property
    def formsInput(self):  # pragma: no cover
        return FormInput.make_many(self.boto3_raw_data["formsInput"])

    glossaryTerms = field("glossaryTerms")
    items = field("items")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDataProductRevisionInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataProductRevisionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSourceRunActivitiesOutput:
    boto3_raw_data: "type_defs.ListDataSourceRunActivitiesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return DataSourceRunActivity.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDataSourceRunActivitiesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSourceRunActivitiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDataSourceRunsOutput:
    boto3_raw_data: "type_defs.ListDataSourceRunsOutputTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return DataSourceRunSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDataSourceRunsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDataSourceRunsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentOutput:
    boto3_raw_data: "type_defs.CreateEnvironmentOutputTypeDef" = dataclasses.field()

    awsAccountId = field("awsAccountId")
    awsAccountRegion = field("awsAccountRegion")
    createdAt = field("createdAt")
    createdBy = field("createdBy")

    @cached_property
    def deploymentProperties(self):  # pragma: no cover
        return DeploymentProperties.make_one(
            self.boto3_raw_data["deploymentProperties"]
        )

    description = field("description")
    domainId = field("domainId")

    @cached_property
    def environmentActions(self):  # pragma: no cover
        return ConfigurableEnvironmentAction.make_many(
            self.boto3_raw_data["environmentActions"]
        )

    environmentBlueprintId = field("environmentBlueprintId")
    environmentConfigurationId = field("environmentConfigurationId")
    environmentProfileId = field("environmentProfileId")
    glossaryTerms = field("glossaryTerms")
    id = field("id")

    @cached_property
    def lastDeployment(self):  # pragma: no cover
        return Deployment.make_one(self.boto3_raw_data["lastDeployment"])

    name = field("name")
    projectId = field("projectId")
    provider = field("provider")

    @cached_property
    def provisionedResources(self):  # pragma: no cover
        return Resource.make_many(self.boto3_raw_data["provisionedResources"])

    @cached_property
    def provisioningProperties(self):  # pragma: no cover
        return ProvisioningProperties.make_one(
            self.boto3_raw_data["provisioningProperties"]
        )

    status = field("status")
    updatedAt = field("updatedAt")

    @cached_property
    def userParameters(self):  # pragma: no cover
        return CustomParameter.make_many(self.boto3_raw_data["userParameters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEnvironmentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentOutput:
    boto3_raw_data: "type_defs.GetEnvironmentOutputTypeDef" = dataclasses.field()

    awsAccountId = field("awsAccountId")
    awsAccountRegion = field("awsAccountRegion")
    createdAt = field("createdAt")
    createdBy = field("createdBy")

    @cached_property
    def deploymentProperties(self):  # pragma: no cover
        return DeploymentProperties.make_one(
            self.boto3_raw_data["deploymentProperties"]
        )

    description = field("description")
    domainId = field("domainId")

    @cached_property
    def environmentActions(self):  # pragma: no cover
        return ConfigurableEnvironmentAction.make_many(
            self.boto3_raw_data["environmentActions"]
        )

    environmentBlueprintId = field("environmentBlueprintId")
    environmentConfigurationId = field("environmentConfigurationId")
    environmentProfileId = field("environmentProfileId")
    glossaryTerms = field("glossaryTerms")
    id = field("id")

    @cached_property
    def lastDeployment(self):  # pragma: no cover
        return Deployment.make_one(self.boto3_raw_data["lastDeployment"])

    name = field("name")
    projectId = field("projectId")
    provider = field("provider")

    @cached_property
    def provisionedResources(self):  # pragma: no cover
        return Resource.make_many(self.boto3_raw_data["provisionedResources"])

    @cached_property
    def provisioningProperties(self):  # pragma: no cover
        return ProvisioningProperties.make_one(
            self.boto3_raw_data["provisioningProperties"]
        )

    status = field("status")
    updatedAt = field("updatedAt")

    @cached_property
    def userParameters(self):  # pragma: no cover
        return CustomParameter.make_many(self.boto3_raw_data["userParameters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEnvironmentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEnvironmentOutput:
    boto3_raw_data: "type_defs.UpdateEnvironmentOutputTypeDef" = dataclasses.field()

    awsAccountId = field("awsAccountId")
    awsAccountRegion = field("awsAccountRegion")
    createdAt = field("createdAt")
    createdBy = field("createdBy")

    @cached_property
    def deploymentProperties(self):  # pragma: no cover
        return DeploymentProperties.make_one(
            self.boto3_raw_data["deploymentProperties"]
        )

    description = field("description")
    domainId = field("domainId")

    @cached_property
    def environmentActions(self):  # pragma: no cover
        return ConfigurableEnvironmentAction.make_many(
            self.boto3_raw_data["environmentActions"]
        )

    environmentBlueprintId = field("environmentBlueprintId")
    environmentConfigurationId = field("environmentConfigurationId")
    environmentProfileId = field("environmentProfileId")
    glossaryTerms = field("glossaryTerms")
    id = field("id")

    @cached_property
    def lastDeployment(self):  # pragma: no cover
        return Deployment.make_one(self.boto3_raw_data["lastDeployment"])

    name = field("name")
    projectId = field("projectId")
    provider = field("provider")

    @cached_property
    def provisionedResources(self):  # pragma: no cover
        return Resource.make_many(self.boto3_raw_data["provisionedResources"])

    @cached_property
    def provisioningProperties(self):  # pragma: no cover
        return ProvisioningProperties.make_one(
            self.boto3_raw_data["provisioningProperties"]
        )

    status = field("status")
    updatedAt = field("updatedAt")

    @cached_property
    def userParameters(self):  # pragma: no cover
        return CustomParameter.make_many(self.boto3_raw_data["userParameters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEnvironmentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnvironmentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectPolicyGrantPrincipal:
    boto3_raw_data: "type_defs.ProjectPolicyGrantPrincipalTypeDef" = dataclasses.field()

    projectDesignation = field("projectDesignation")

    @cached_property
    def projectGrantFilter(self):  # pragma: no cover
        return ProjectGrantFilter.make_one(self.boto3_raw_data["projectGrantFilter"])

    projectIdentifier = field("projectIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProjectPolicyGrantPrincipalTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProjectPolicyGrantPrincipalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainUnitOutput:
    boto3_raw_data: "type_defs.CreateDomainUnitOutputTypeDef" = dataclasses.field()

    ancestorDomainUnitIds = field("ancestorDomainUnitIds")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")
    id = field("id")
    name = field("name")

    @cached_property
    def owners(self):  # pragma: no cover
        return DomainUnitOwnerProperties.make_many(self.boto3_raw_data["owners"])

    parentDomainUnitId = field("parentDomainUnitId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDomainUnitOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainUnitOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainUnitOutput:
    boto3_raw_data: "type_defs.GetDomainUnitOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")
    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    lastUpdatedBy = field("lastUpdatedBy")
    name = field("name")

    @cached_property
    def owners(self):  # pragma: no cover
        return DomainUnitOwnerProperties.make_many(self.boto3_raw_data["owners"])

    parentDomainUnitId = field("parentDomainUnitId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDomainUnitOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainUnitOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainUnitOutput:
    boto3_raw_data: "type_defs.UpdateDomainUnitOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")
    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    lastUpdatedBy = field("lastUpdatedBy")
    name = field("name")

    @cached_property
    def owners(self):  # pragma: no cover
        return DomainUnitOwnerProperties.make_many(self.boto3_raw_data["owners"])

    parentDomainUnitId = field("parentDomainUnitId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDomainUnitOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainUnitOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentConfigurationOutput:
    boto3_raw_data: "type_defs.EnvironmentConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    environmentBlueprintId = field("environmentBlueprintId")
    name = field("name")
    accountPools = field("accountPools")

    @cached_property
    def awsAccount(self):  # pragma: no cover
        return AwsAccount.make_one(self.boto3_raw_data["awsAccount"])

    @cached_property
    def awsRegion(self):  # pragma: no cover
        return Region.make_one(self.boto3_raw_data["awsRegion"])

    @cached_property
    def configurationParameters(self):  # pragma: no cover
        return EnvironmentConfigurationParametersDetailsOutput.make_one(
            self.boto3_raw_data["configurationParameters"]
        )

    deploymentMode = field("deploymentMode")
    deploymentOrder = field("deploymentOrder")
    description = field("description")
    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EnvironmentConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProjectOutput:
    boto3_raw_data: "type_defs.CreateProjectOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")
    domainUnitId = field("domainUnitId")

    @cached_property
    def environmentDeploymentDetails(self):  # pragma: no cover
        return EnvironmentDeploymentDetailsOutput.make_one(
            self.boto3_raw_data["environmentDeploymentDetails"]
        )

    @cached_property
    def failureReasons(self):  # pragma: no cover
        return ProjectDeletionError.make_many(self.boto3_raw_data["failureReasons"])

    glossaryTerms = field("glossaryTerms")
    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    projectProfileId = field("projectProfileId")
    projectStatus = field("projectStatus")

    @cached_property
    def userParameters(self):  # pragma: no cover
        return EnvironmentConfigurationUserParameterOutput.make_many(
            self.boto3_raw_data["userParameters"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProjectOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProjectOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProjectOutput:
    boto3_raw_data: "type_defs.GetProjectOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")
    domainUnitId = field("domainUnitId")

    @cached_property
    def environmentDeploymentDetails(self):  # pragma: no cover
        return EnvironmentDeploymentDetailsOutput.make_one(
            self.boto3_raw_data["environmentDeploymentDetails"]
        )

    @cached_property
    def failureReasons(self):  # pragma: no cover
        return ProjectDeletionError.make_many(self.boto3_raw_data["failureReasons"])

    glossaryTerms = field("glossaryTerms")
    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    projectProfileId = field("projectProfileId")
    projectStatus = field("projectStatus")

    @cached_property
    def userParameters(self):  # pragma: no cover
        return EnvironmentConfigurationUserParameterOutput.make_many(
            self.boto3_raw_data["userParameters"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetProjectOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProjectOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProjectOutput:
    boto3_raw_data: "type_defs.UpdateProjectOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")
    domainUnitId = field("domainUnitId")

    @cached_property
    def environmentDeploymentDetails(self):  # pragma: no cover
        return EnvironmentDeploymentDetailsOutput.make_one(
            self.boto3_raw_data["environmentDeploymentDetails"]
        )

    @cached_property
    def failureReasons(self):  # pragma: no cover
        return ProjectDeletionError.make_many(self.boto3_raw_data["failureReasons"])

    glossaryTerms = field("glossaryTerms")
    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    projectProfileId = field("projectProfileId")
    projectStatus = field("projectStatus")

    @cached_property
    def userParameters(self):  # pragma: no cover
        return EnvironmentConfigurationUserParameterOutput.make_many(
            self.boto3_raw_data["userParameters"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProjectOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProjectOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchInputPaginate:
    boto3_raw_data: "type_defs.SearchInputPaginateTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    searchScope = field("searchScope")
    additionalAttributes = field("additionalAttributes")

    @cached_property
    def filters(self):  # pragma: no cover
        return FilterClausePaginator.make_one(self.boto3_raw_data["filters"])

    owningProjectIdentifier = field("owningProjectIdentifier")

    @cached_property
    def searchIn(self):  # pragma: no cover
        return SearchInItem.make_many(self.boto3_raw_data["searchIn"])

    searchText = field("searchText")

    @cached_property
    def sort(self):  # pragma: no cover
        return SearchSort.make_one(self.boto3_raw_data["sort"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchListingsInputPaginate:
    boto3_raw_data: "type_defs.SearchListingsInputPaginateTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    additionalAttributes = field("additionalAttributes")

    @cached_property
    def aggregations(self):  # pragma: no cover
        return AggregationListItem.make_many(self.boto3_raw_data["aggregations"])

    @cached_property
    def filters(self):  # pragma: no cover
        return FilterClausePaginator.make_one(self.boto3_raw_data["filters"])

    @cached_property
    def searchIn(self):  # pragma: no cover
        return SearchInItem.make_many(self.boto3_raw_data["searchIn"])

    searchText = field("searchText")

    @cached_property
    def sort(self):  # pragma: no cover
        return SearchSort.make_one(self.boto3_raw_data["sort"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchListingsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchListingsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchTypesInputPaginate:
    boto3_raw_data: "type_defs.SearchTypesInputPaginateTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    managed = field("managed")
    searchScope = field("searchScope")

    @cached_property
    def filters(self):  # pragma: no cover
        return FilterClausePaginator.make_one(self.boto3_raw_data["filters"])

    @cached_property
    def searchIn(self):  # pragma: no cover
        return SearchInItem.make_many(self.boto3_raw_data["searchIn"])

    searchText = field("searchText")

    @cached_property
    def sort(self):  # pragma: no cover
        return SearchSort.make_one(self.boto3_raw_data["sort"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchTypesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchTypesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchInput:
    boto3_raw_data: "type_defs.SearchInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    searchScope = field("searchScope")
    additionalAttributes = field("additionalAttributes")

    @cached_property
    def filters(self):  # pragma: no cover
        return FilterClause.make_one(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    owningProjectIdentifier = field("owningProjectIdentifier")

    @cached_property
    def searchIn(self):  # pragma: no cover
        return SearchInItem.make_many(self.boto3_raw_data["searchIn"])

    searchText = field("searchText")

    @cached_property
    def sort(self):  # pragma: no cover
        return SearchSort.make_one(self.boto3_raw_data["sort"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SearchInputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchListingsInput:
    boto3_raw_data: "type_defs.SearchListingsInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    additionalAttributes = field("additionalAttributes")

    @cached_property
    def aggregations(self):  # pragma: no cover
        return AggregationListItem.make_many(self.boto3_raw_data["aggregations"])

    @cached_property
    def filters(self):  # pragma: no cover
        return FilterClause.make_one(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def searchIn(self):  # pragma: no cover
        return SearchInItem.make_many(self.boto3_raw_data["searchIn"])

    searchText = field("searchText")

    @cached_property
    def sort(self):  # pragma: no cover
        return SearchSort.make_one(self.boto3_raw_data["sort"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchListingsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchListingsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchTypesInput:
    boto3_raw_data: "type_defs.SearchTypesInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    managed = field("managed")
    searchScope = field("searchScope")

    @cached_property
    def filters(self):  # pragma: no cover
        return FilterClause.make_one(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @cached_property
    def searchIn(self):  # pragma: no cover
        return SearchInItem.make_many(self.boto3_raw_data["searchIn"])

    searchText = field("searchText")

    @cached_property
    def sort(self):  # pragma: no cover
        return SearchSort.make_one(self.boto3_raw_data["sort"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchTypesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchTypesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlueRunConfigurationOutput:
    boto3_raw_data: "type_defs.GlueRunConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def relationalFilterConfigurations(self):  # pragma: no cover
        return RelationalFilterConfigurationOutput.make_many(
            self.boto3_raw_data["relationalFilterConfigurations"]
        )

    accountId = field("accountId")
    autoImportDataQualityResult = field("autoImportDataQualityResult")
    catalogName = field("catalogName")
    dataAccessRole = field("dataAccessRole")
    region = field("region")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlueRunConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlueRunConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchTypesResultItem:
    boto3_raw_data: "type_defs.SearchTypesResultItemTypeDef" = dataclasses.field()

    @cached_property
    def assetTypeItem(self):  # pragma: no cover
        return AssetTypeItem.make_one(self.boto3_raw_data["assetTypeItem"])

    @cached_property
    def formTypeItem(self):  # pragma: no cover
        return FormTypeData.make_one(self.boto3_raw_data["formTypeItem"])

    @cached_property
    def lineageNodeTypeItem(self):  # pragma: no cover
        return LineageNodeTypeItem.make_one(self.boto3_raw_data["lineageNodeTypeItem"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchTypesResultItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchTypesResultItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobRunsOutput:
    boto3_raw_data: "type_defs.ListJobRunsOutputTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return JobRunSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListJobRunsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobRunsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PostTimeSeriesDataPointsInput:
    boto3_raw_data: "type_defs.PostTimeSeriesDataPointsInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    entityIdentifier = field("entityIdentifier")
    entityType = field("entityType")

    @cached_property
    def forms(self):  # pragma: no cover
        return TimeSeriesDataPointFormInput.make_many(self.boto3_raw_data["forms"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PostTimeSeriesDataPointsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PostTimeSeriesDataPointsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMetadataGenerationRunsOutput:
    boto3_raw_data: "type_defs.ListMetadataGenerationRunsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return MetadataGenerationRunItem.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListMetadataGenerationRunsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMetadataGenerationRunsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SelfGrantStatusOutput:
    boto3_raw_data: "type_defs.SelfGrantStatusOutputTypeDef" = dataclasses.field()

    @cached_property
    def glueSelfGrantStatus(self):  # pragma: no cover
        return GlueSelfGrantStatusOutput.make_one(
            self.boto3_raw_data["glueSelfGrantStatus"]
        )

    @cached_property
    def redshiftSelfGrantStatus(self):  # pragma: no cover
        return RedshiftSelfGrantStatusOutput.make_one(
            self.boto3_raw_data["redshiftSelfGrantStatus"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SelfGrantStatusOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SelfGrantStatusOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSubscriptionGrantInput:
    boto3_raw_data: "type_defs.CreateSubscriptionGrantInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    environmentIdentifier = field("environmentIdentifier")

    @cached_property
    def grantedEntity(self):  # pragma: no cover
        return GrantedEntityInput.make_one(self.boto3_raw_data["grantedEntity"])

    @cached_property
    def assetTargetNames(self):  # pragma: no cover
        return AssetTargetNameMap.make_many(self.boto3_raw_data["assetTargetNames"])

    clientToken = field("clientToken")
    subscriptionTargetIdentifier = field("subscriptionTargetIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSubscriptionGrantInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSubscriptionGrantInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSubscriptionGrantOutput:
    boto3_raw_data: "type_defs.CreateSubscriptionGrantOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assets(self):  # pragma: no cover
        return SubscribedAsset.make_many(self.boto3_raw_data["assets"])

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    domainId = field("domainId")

    @cached_property
    def grantedEntity(self):  # pragma: no cover
        return GrantedEntity.make_one(self.boto3_raw_data["grantedEntity"])

    id = field("id")
    status = field("status")
    subscriptionId = field("subscriptionId")
    subscriptionTargetId = field("subscriptionTargetId")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSubscriptionGrantOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSubscriptionGrantOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSubscriptionGrantOutput:
    boto3_raw_data: "type_defs.DeleteSubscriptionGrantOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assets(self):  # pragma: no cover
        return SubscribedAsset.make_many(self.boto3_raw_data["assets"])

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    domainId = field("domainId")

    @cached_property
    def grantedEntity(self):  # pragma: no cover
        return GrantedEntity.make_one(self.boto3_raw_data["grantedEntity"])

    id = field("id")
    status = field("status")
    subscriptionId = field("subscriptionId")
    subscriptionTargetId = field("subscriptionTargetId")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteSubscriptionGrantOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSubscriptionGrantOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSubscriptionGrantOutput:
    boto3_raw_data: "type_defs.GetSubscriptionGrantOutputTypeDef" = dataclasses.field()

    @cached_property
    def assets(self):  # pragma: no cover
        return SubscribedAsset.make_many(self.boto3_raw_data["assets"])

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    domainId = field("domainId")

    @cached_property
    def grantedEntity(self):  # pragma: no cover
        return GrantedEntity.make_one(self.boto3_raw_data["grantedEntity"])

    id = field("id")
    status = field("status")
    subscriptionId = field("subscriptionId")
    subscriptionTargetId = field("subscriptionTargetId")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSubscriptionGrantOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSubscriptionGrantOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscriptionGrantSummary:
    boto3_raw_data: "type_defs.SubscriptionGrantSummaryTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    domainId = field("domainId")

    @cached_property
    def grantedEntity(self):  # pragma: no cover
        return GrantedEntity.make_one(self.boto3_raw_data["grantedEntity"])

    id = field("id")
    status = field("status")
    subscriptionTargetId = field("subscriptionTargetId")
    updatedAt = field("updatedAt")

    @cached_property
    def assets(self):  # pragma: no cover
        return SubscribedAsset.make_many(self.boto3_raw_data["assets"])

    subscriptionId = field("subscriptionId")
    updatedBy = field("updatedBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubscriptionGrantSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscriptionGrantSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSubscriptionGrantStatusOutput:
    boto3_raw_data: "type_defs.UpdateSubscriptionGrantStatusOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assets(self):  # pragma: no cover
        return SubscribedAsset.make_many(self.boto3_raw_data["assets"])

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    domainId = field("domainId")

    @cached_property
    def grantedEntity(self):  # pragma: no cover
        return GrantedEntity.make_one(self.boto3_raw_data["grantedEntity"])

    id = field("id")
    status = field("status")
    subscriptionId = field("subscriptionId")
    subscriptionTargetId = field("subscriptionTargetId")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateSubscriptionGrantStatusOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSubscriptionGrantStatusOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentBlueprintConfigurationItem:
    boto3_raw_data: "type_defs.EnvironmentBlueprintConfigurationItemTypeDef" = (
        dataclasses.field()
    )

    domainId = field("domainId")
    environmentBlueprintId = field("environmentBlueprintId")
    createdAt = field("createdAt")
    enabledRegions = field("enabledRegions")
    environmentRolePermissionBoundary = field("environmentRolePermissionBoundary")
    manageAccessRoleArn = field("manageAccessRoleArn")

    @cached_property
    def provisioningConfigurations(self):  # pragma: no cover
        return ProvisioningConfigurationOutput.make_many(
            self.boto3_raw_data["provisioningConfigurations"]
        )

    provisioningRoleArn = field("provisioningRoleArn")
    regionalParameters = field("regionalParameters")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnvironmentBlueprintConfigurationItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentBlueprintConfigurationItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentBlueprintConfigurationOutput:
    boto3_raw_data: "type_defs.GetEnvironmentBlueprintConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")
    domainId = field("domainId")
    enabledRegions = field("enabledRegions")
    environmentBlueprintId = field("environmentBlueprintId")
    environmentRolePermissionBoundary = field("environmentRolePermissionBoundary")
    manageAccessRoleArn = field("manageAccessRoleArn")

    @cached_property
    def provisioningConfigurations(self):  # pragma: no cover
        return ProvisioningConfigurationOutput.make_many(
            self.boto3_raw_data["provisioningConfigurations"]
        )

    provisioningRoleArn = field("provisioningRoleArn")
    regionalParameters = field("regionalParameters")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEnvironmentBlueprintConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentBlueprintConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEnvironmentBlueprintConfigurationOutput:
    boto3_raw_data: "type_defs.PutEnvironmentBlueprintConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")
    domainId = field("domainId")
    enabledRegions = field("enabledRegions")
    environmentBlueprintId = field("environmentBlueprintId")
    environmentRolePermissionBoundary = field("environmentRolePermissionBoundary")
    manageAccessRoleArn = field("manageAccessRoleArn")

    @cached_property
    def provisioningConfigurations(self):  # pragma: no cover
        return ProvisioningConfigurationOutput.make_many(
            self.boto3_raw_data["provisioningConfigurations"]
        )

    provisioningRoleArn = field("provisioningRoleArn")
    regionalParameters = field("regionalParameters")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutEnvironmentBlueprintConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEnvironmentBlueprintConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProvisioningConfiguration:
    boto3_raw_data: "type_defs.ProvisioningConfigurationTypeDef" = dataclasses.field()

    lakeFormationConfiguration = field("lakeFormationConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProvisioningConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProvisioningConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobRunDetails:
    boto3_raw_data: "type_defs.JobRunDetailsTypeDef" = dataclasses.field()

    @cached_property
    def lineageRunDetails(self):  # pragma: no cover
        return LineageRunDetails.make_one(self.boto3_raw_data["lineageRunDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobRunDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobRunDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MatchRationaleItem:
    boto3_raw_data: "type_defs.MatchRationaleItemTypeDef" = dataclasses.field()

    @cached_property
    def textMatches(self):  # pragma: no cover
        return TextMatchItem.make_many(self.boto3_raw_data["textMatches"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MatchRationaleItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MatchRationaleItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProjectMember:
    boto3_raw_data: "type_defs.ProjectMemberTypeDef" = dataclasses.field()

    designation = field("designation")

    @cached_property
    def memberDetails(self):  # pragma: no cover
        return MemberDetails.make_one(self.boto3_raw_data["memberDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProjectMemberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProjectMemberTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleDetailOutput:
    boto3_raw_data: "type_defs.RuleDetailOutputTypeDef" = dataclasses.field()

    @cached_property
    def metadataFormEnforcementDetail(self):  # pragma: no cover
        return MetadataFormEnforcementDetailOutput.make_one(
            self.boto3_raw_data["metadataFormEnforcementDetail"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleDetailOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleDetailOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleDetail:
    boto3_raw_data: "type_defs.RuleDetailTypeDef" = dataclasses.field()

    @cached_property
    def metadataFormEnforcementDetail(self):  # pragma: no cover
        return MetadataFormEnforcementDetail.make_one(
            self.boto3_raw_data["metadataFormEnforcementDetail"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleDetailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventSummary:
    boto3_raw_data: "type_defs.EventSummaryTypeDef" = dataclasses.field()

    @cached_property
    def openLineageRunEventSummary(self):  # pragma: no cover
        return OpenLineageRunEventSummary.make_one(
            self.boto3_raw_data["openLineageRunEventSummary"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EventSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RowFilterOutput:
    boto3_raw_data: "type_defs.RowFilterOutputTypeDef" = dataclasses.field()

    and_ = field("and")

    @cached_property
    def expression(self):  # pragma: no cover
        return RowFilterExpressionOutput.make_one(self.boto3_raw_data["expression"])

    or_ = field("or")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RowFilterOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RowFilterOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RowFilter:
    boto3_raw_data: "type_defs.RowFilterTypeDef" = dataclasses.field()

    and_ = field("and")

    @cached_property
    def expression(self):  # pragma: no cover
        return RowFilterExpression.make_one(self.boto3_raw_data["expression"])

    or_ = field("or")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RowFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RowFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NotificationOutput:
    boto3_raw_data: "type_defs.NotificationOutputTypeDef" = dataclasses.field()

    actionLink = field("actionLink")
    creationTimestamp = field("creationTimestamp")
    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    lastUpdatedTimestamp = field("lastUpdatedTimestamp")
    message = field("message")
    title = field("title")

    @cached_property
    def topic(self):  # pragma: no cover
        return Topic.make_one(self.boto3_raw_data["topic"])

    type = field("type")
    metadata = field("metadata")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NotificationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NotificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthenticationConfiguration:
    boto3_raw_data: "type_defs.AuthenticationConfigurationTypeDef" = dataclasses.field()

    authenticationType = field("authenticationType")

    @cached_property
    def oAuth2Properties(self):  # pragma: no cover
        return OAuth2PropertiesOutput.make_one(self.boto3_raw_data["oAuth2Properties"])

    secretArn = field("secretArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthenticationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthenticationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEntityOwnersOutput:
    boto3_raw_data: "type_defs.ListEntityOwnersOutputTypeDef" = dataclasses.field()

    @cached_property
    def owners(self):  # pragma: no cover
        return OwnerPropertiesOutput.make_many(self.boto3_raw_data["owners"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEntityOwnersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEntityOwnersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddEntityOwnerInput:
    boto3_raw_data: "type_defs.AddEntityOwnerInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    entityIdentifier = field("entityIdentifier")
    entityType = field("entityType")

    @cached_property
    def owner(self):  # pragma: no cover
        return OwnerProperties.make_one(self.boto3_raw_data["owner"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddEntityOwnerInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddEntityOwnerInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveEntityOwnerInput:
    boto3_raw_data: "type_defs.RemoveEntityOwnerInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    entityIdentifier = field("entityIdentifier")
    entityType = field("entityType")

    @cached_property
    def owner(self):  # pragma: no cover
        return OwnerProperties.make_one(self.boto3_raw_data["owner"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveEntityOwnerInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveEntityOwnerInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleSummary:
    boto3_raw_data: "type_defs.RuleSummaryTypeDef" = dataclasses.field()

    action = field("action")
    identifier = field("identifier")
    lastUpdatedBy = field("lastUpdatedBy")
    name = field("name")
    revision = field("revision")
    ruleType = field("ruleType")

    @cached_property
    def scope(self):  # pragma: no cover
        return RuleScopeOutput.make_one(self.boto3_raw_data["scope"])

    @cached_property
    def target(self):  # pragma: no cover
        return RuleTarget.make_one(self.boto3_raw_data["target"])

    targetType = field("targetType")
    updatedAt = field("updatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftPropertiesInput:
    boto3_raw_data: "type_defs.RedshiftPropertiesInputTypeDef" = dataclasses.field()

    @cached_property
    def credentials(self):  # pragma: no cover
        return RedshiftCredentials.make_one(self.boto3_raw_data["credentials"])

    databaseName = field("databaseName")
    host = field("host")

    @cached_property
    def lineageSync(self):  # pragma: no cover
        return RedshiftLineageSyncConfigurationInput.make_one(
            self.boto3_raw_data["lineageSync"]
        )

    port = field("port")

    @cached_property
    def storage(self):  # pragma: no cover
        return RedshiftStorageProperties.make_one(self.boto3_raw_data["storage"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedshiftPropertiesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftPropertiesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftPropertiesOutput:
    boto3_raw_data: "type_defs.RedshiftPropertiesOutputTypeDef" = dataclasses.field()

    @cached_property
    def credentials(self):  # pragma: no cover
        return RedshiftCredentials.make_one(self.boto3_raw_data["credentials"])

    databaseName = field("databaseName")
    isProvisionedSecret = field("isProvisionedSecret")
    jdbcIamUrl = field("jdbcIamUrl")
    jdbcUrl = field("jdbcUrl")

    @cached_property
    def lineageSync(self):  # pragma: no cover
        return RedshiftLineageSyncConfigurationOutput.make_one(
            self.boto3_raw_data["lineageSync"]
        )

    redshiftTempDir = field("redshiftTempDir")
    status = field("status")

    @cached_property
    def storage(self):  # pragma: no cover
        return RedshiftStorageProperties.make_one(self.boto3_raw_data["storage"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedshiftPropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftPropertiesPatch:
    boto3_raw_data: "type_defs.RedshiftPropertiesPatchTypeDef" = dataclasses.field()

    @cached_property
    def credentials(self):  # pragma: no cover
        return RedshiftCredentials.make_one(self.boto3_raw_data["credentials"])

    databaseName = field("databaseName")
    host = field("host")

    @cached_property
    def lineageSync(self):  # pragma: no cover
        return RedshiftLineageSyncConfigurationInput.make_one(
            self.boto3_raw_data["lineageSync"]
        )

    port = field("port")

    @cached_property
    def storage(self):  # pragma: no cover
        return RedshiftStorageProperties.make_one(self.boto3_raw_data["storage"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedshiftPropertiesPatchTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftPropertiesPatchTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftRunConfigurationOutput:
    boto3_raw_data: "type_defs.RedshiftRunConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def redshiftStorage(self):  # pragma: no cover
        return RedshiftStorage.make_one(self.boto3_raw_data["redshiftStorage"])

    @cached_property
    def relationalFilterConfigurations(self):  # pragma: no cover
        return RelationalFilterConfigurationOutput.make_many(
            self.boto3_raw_data["relationalFilterConfigurations"]
        )

    accountId = field("accountId")
    dataAccessRole = field("dataAccessRole")

    @cached_property
    def redshiftCredentialConfiguration(self):  # pragma: no cover
        return RedshiftCredentialConfiguration.make_one(
            self.boto3_raw_data["redshiftCredentialConfiguration"]
        )

    region = field("region")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RedshiftRunConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftRunConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUserProfileOutput:
    boto3_raw_data: "type_defs.CreateUserProfileOutputTypeDef" = dataclasses.field()

    @cached_property
    def details(self):  # pragma: no cover
        return UserProfileDetails.make_one(self.boto3_raw_data["details"])

    domainId = field("domainId")
    id = field("id")
    status = field("status")
    type = field("type")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUserProfileOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUserProfileOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUserProfileOutput:
    boto3_raw_data: "type_defs.GetUserProfileOutputTypeDef" = dataclasses.field()

    @cached_property
    def details(self):  # pragma: no cover
        return UserProfileDetails.make_one(self.boto3_raw_data["details"])

    domainId = field("domainId")
    id = field("id")
    status = field("status")
    type = field("type")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUserProfileOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUserProfileOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateUserProfileOutput:
    boto3_raw_data: "type_defs.UpdateUserProfileOutputTypeDef" = dataclasses.field()

    @cached_property
    def details(self):  # pragma: no cover
        return UserProfileDetails.make_one(self.boto3_raw_data["details"])

    domainId = field("domainId")
    id = field("id")
    status = field("status")
    type = field("type")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateUserProfileOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateUserProfileOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserProfileSummary:
    boto3_raw_data: "type_defs.UserProfileSummaryTypeDef" = dataclasses.field()

    @cached_property
    def details(self):  # pragma: no cover
        return UserProfileDetails.make_one(self.boto3_raw_data["details"])

    domainId = field("domainId")
    id = field("id")
    status = field("status")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UserProfileSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UserProfileSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSubscriptionRequestInput:
    boto3_raw_data: "type_defs.CreateSubscriptionRequestInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    requestReason = field("requestReason")

    @cached_property
    def subscribedListings(self):  # pragma: no cover
        return SubscribedListingInput.make_many(
            self.boto3_raw_data["subscribedListings"]
        )

    @cached_property
    def subscribedPrincipals(self):  # pragma: no cover
        return SubscribedPrincipalInput.make_many(
            self.boto3_raw_data["subscribedPrincipals"]
        )

    clientToken = field("clientToken")

    @cached_property
    def metadataForms(self):  # pragma: no cover
        return FormInput.make_many(self.boto3_raw_data["metadataForms"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSubscriptionRequestInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSubscriptionRequestInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGlossaryTermInput:
    boto3_raw_data: "type_defs.CreateGlossaryTermInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    glossaryIdentifier = field("glossaryIdentifier")
    name = field("name")
    clientToken = field("clientToken")
    longDescription = field("longDescription")
    shortDescription = field("shortDescription")
    status = field("status")
    termRelations = field("termRelations")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGlossaryTermInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGlossaryTermInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGlossaryTermInput:
    boto3_raw_data: "type_defs.UpdateGlossaryTermInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    glossaryIdentifier = field("glossaryIdentifier")
    longDescription = field("longDescription")
    name = field("name")
    shortDescription = field("shortDescription")
    status = field("status")
    termRelations = field("termRelations")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGlossaryTermInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGlossaryTermInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccountPoolInput:
    boto3_raw_data: "type_defs.CreateAccountPoolInputTypeDef" = dataclasses.field()

    accountSource = field("accountSource")
    domainIdentifier = field("domainIdentifier")
    name = field("name")
    resolutionStrategy = field("resolutionStrategy")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccountPoolInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccountPoolInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccountPoolInput:
    boto3_raw_data: "type_defs.UpdateAccountPoolInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    accountSource = field("accountSource")
    description = field("description")
    name = field("name")
    resolutionStrategy = field("resolutionStrategy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAccountPoolInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccountPoolInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentActionsOutput:
    boto3_raw_data: "type_defs.ListEnvironmentActionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return EnvironmentActionSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEnvironmentActionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentActionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListingItem:
    boto3_raw_data: "type_defs.ListingItemTypeDef" = dataclasses.field()

    @cached_property
    def assetListing(self):  # pragma: no cover
        return AssetListing.make_one(self.boto3_raw_data["assetListing"])

    @cached_property
    def dataProductListing(self):  # pragma: no cover
        return DataProductListing.make_one(self.boto3_raw_data["dataProductListing"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListingItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListingItemTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscribedListing:
    boto3_raw_data: "type_defs.SubscribedListingTypeDef" = dataclasses.field()

    description = field("description")
    id = field("id")

    @cached_property
    def item(self):  # pragma: no cover
        return SubscribedListingItem.make_one(self.boto3_raw_data["item"])

    name = field("name")
    ownerProjectId = field("ownerProjectId")
    ownerProjectName = field("ownerProjectName")
    revision = field("revision")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubscribedListingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscribedListingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GluePropertiesPatch:
    boto3_raw_data: "type_defs.GluePropertiesPatchTypeDef" = dataclasses.field()

    @cached_property
    def glueConnectionInput(self):  # pragma: no cover
        return GlueConnectionPatch.make_one(self.boto3_raw_data["glueConnectionInput"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GluePropertiesPatchTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GluePropertiesPatchTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentBlueprintsOutput:
    boto3_raw_data: "type_defs.ListEnvironmentBlueprintsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return EnvironmentBlueprintSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEnvironmentBlueprintsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentBlueprintsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyGrantPrincipalOutput:
    boto3_raw_data: "type_defs.PolicyGrantPrincipalOutputTypeDef" = dataclasses.field()

    @cached_property
    def domainUnit(self):  # pragma: no cover
        return DomainUnitPolicyGrantPrincipalOutput.make_one(
            self.boto3_raw_data["domainUnit"]
        )

    @cached_property
    def group(self):  # pragma: no cover
        return GroupPolicyGrantPrincipal.make_one(self.boto3_raw_data["group"])

    @cached_property
    def project(self):  # pragma: no cover
        return ProjectPolicyGrantPrincipal.make_one(self.boto3_raw_data["project"])

    @cached_property
    def user(self):  # pragma: no cover
        return UserPolicyGrantPrincipalOutput.make_one(self.boto3_raw_data["user"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolicyGrantPrincipalOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyGrantPrincipalOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyGrantPrincipal:
    boto3_raw_data: "type_defs.PolicyGrantPrincipalTypeDef" = dataclasses.field()

    @cached_property
    def domainUnit(self):  # pragma: no cover
        return DomainUnitPolicyGrantPrincipal.make_one(
            self.boto3_raw_data["domainUnit"]
        )

    @cached_property
    def group(self):  # pragma: no cover
        return GroupPolicyGrantPrincipal.make_one(self.boto3_raw_data["group"])

    @cached_property
    def project(self):  # pragma: no cover
        return ProjectPolicyGrantPrincipal.make_one(self.boto3_raw_data["project"])

    @cached_property
    def user(self):  # pragma: no cover
        return UserPolicyGrantPrincipal.make_one(self.boto3_raw_data["user"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolicyGrantPrincipalTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyGrantPrincipalTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProjectProfileOutput:
    boto3_raw_data: "type_defs.CreateProjectProfileOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")
    domainUnitId = field("domainUnitId")

    @cached_property
    def environmentConfigurations(self):  # pragma: no cover
        return EnvironmentConfigurationOutput.make_many(
            self.boto3_raw_data["environmentConfigurations"]
        )

    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProjectProfileOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProjectProfileOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProjectProfileOutput:
    boto3_raw_data: "type_defs.GetProjectProfileOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")
    domainUnitId = field("domainUnitId")

    @cached_property
    def environmentConfigurations(self):  # pragma: no cover
        return EnvironmentConfigurationOutput.make_many(
            self.boto3_raw_data["environmentConfigurations"]
        )

    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetProjectProfileOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProjectProfileOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProjectProfileOutput:
    boto3_raw_data: "type_defs.UpdateProjectProfileOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")
    domainUnitId = field("domainUnitId")

    @cached_property
    def environmentConfigurations(self):  # pragma: no cover
        return EnvironmentConfigurationOutput.make_many(
            self.boto3_raw_data["environmentConfigurations"]
        )

    id = field("id")
    lastUpdatedAt = field("lastUpdatedAt")
    name = field("name")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProjectProfileOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProjectProfileOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentConfiguration:
    boto3_raw_data: "type_defs.EnvironmentConfigurationTypeDef" = dataclasses.field()

    environmentBlueprintId = field("environmentBlueprintId")
    name = field("name")
    accountPools = field("accountPools")

    @cached_property
    def awsAccount(self):  # pragma: no cover
        return AwsAccount.make_one(self.boto3_raw_data["awsAccount"])

    @cached_property
    def awsRegion(self):  # pragma: no cover
        return Region.make_one(self.boto3_raw_data["awsRegion"])

    configurationParameters = field("configurationParameters")
    deploymentMode = field("deploymentMode")
    deploymentOrder = field("deploymentOrder")
    description = field("description")
    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProjectInput:
    boto3_raw_data: "type_defs.CreateProjectInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    name = field("name")
    description = field("description")
    domainUnitId = field("domainUnitId")
    glossaryTerms = field("glossaryTerms")
    projectProfileId = field("projectProfileId")
    userParameters = field("userParameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProjectInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProjectInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProjectInput:
    boto3_raw_data: "type_defs.UpdateProjectInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    description = field("description")
    domainUnitId = field("domainUnitId")
    environmentDeploymentDetails = field("environmentDeploymentDetails")
    glossaryTerms = field("glossaryTerms")
    name = field("name")
    projectProfileVersion = field("projectProfileVersion")
    userParameters = field("userParameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProjectInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProjectInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlueRunConfigurationInput:
    boto3_raw_data: "type_defs.GlueRunConfigurationInputTypeDef" = dataclasses.field()

    relationalFilterConfigurations = field("relationalFilterConfigurations")
    autoImportDataQualityResult = field("autoImportDataQualityResult")
    catalogName = field("catalogName")
    dataAccessRole = field("dataAccessRole")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlueRunConfigurationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlueRunConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftRunConfigurationInput:
    boto3_raw_data: "type_defs.RedshiftRunConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    relationalFilterConfigurations = field("relationalFilterConfigurations")
    dataAccessRole = field("dataAccessRole")

    @cached_property
    def redshiftCredentialConfiguration(self):  # pragma: no cover
        return RedshiftCredentialConfiguration.make_one(
            self.boto3_raw_data["redshiftCredentialConfiguration"]
        )

    @cached_property
    def redshiftStorage(self):  # pragma: no cover
        return RedshiftStorage.make_one(self.boto3_raw_data["redshiftStorage"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RedshiftRunConfigurationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftRunConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchTypesOutput:
    boto3_raw_data: "type_defs.SearchTypesOutputTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return SearchTypesResultItem.make_many(self.boto3_raw_data["items"])

    totalMatchCount = field("totalMatchCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchTypesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchTypesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubscriptionGrantsOutput:
    boto3_raw_data: "type_defs.ListSubscriptionGrantsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return SubscriptionGrantSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSubscriptionGrantsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubscriptionGrantsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentBlueprintConfigurationsOutput:
    boto3_raw_data: "type_defs.ListEnvironmentBlueprintConfigurationsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return EnvironmentBlueprintConfigurationItem.make_many(
            self.boto3_raw_data["items"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEnvironmentBlueprintConfigurationsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentBlueprintConfigurationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetJobRunOutput:
    boto3_raw_data: "type_defs.GetJobRunOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")

    @cached_property
    def details(self):  # pragma: no cover
        return JobRunDetails.make_one(self.boto3_raw_data["details"])

    domainId = field("domainId")
    endTime = field("endTime")

    @cached_property
    def error(self):  # pragma: no cover
        return JobRunError.make_one(self.boto3_raw_data["error"])

    id = field("id")
    jobId = field("jobId")
    jobType = field("jobType")
    runMode = field("runMode")
    startTime = field("startTime")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetJobRunOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetJobRunOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetItemAdditionalAttributes:
    boto3_raw_data: "type_defs.AssetItemAdditionalAttributesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def formsOutput(self):  # pragma: no cover
        return FormOutput.make_many(self.boto3_raw_data["formsOutput"])

    @cached_property
    def latestTimeSeriesDataPointFormsOutput(self):  # pragma: no cover
        return TimeSeriesDataPointSummaryFormOutput.make_many(
            self.boto3_raw_data["latestTimeSeriesDataPointFormsOutput"]
        )

    @cached_property
    def matchRationale(self):  # pragma: no cover
        return MatchRationaleItem.make_many(self.boto3_raw_data["matchRationale"])

    @cached_property
    def readOnlyFormsOutput(self):  # pragma: no cover
        return FormOutput.make_many(self.boto3_raw_data["readOnlyFormsOutput"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssetItemAdditionalAttributesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetItemAdditionalAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetListingItemAdditionalAttributes:
    boto3_raw_data: "type_defs.AssetListingItemAdditionalAttributesTypeDef" = (
        dataclasses.field()
    )

    forms = field("forms")

    @cached_property
    def latestTimeSeriesDataPointForms(self):  # pragma: no cover
        return TimeSeriesDataPointSummaryFormOutput.make_many(
            self.boto3_raw_data["latestTimeSeriesDataPointForms"]
        )

    @cached_property
    def matchRationale(self):  # pragma: no cover
        return MatchRationaleItem.make_many(self.boto3_raw_data["matchRationale"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssetListingItemAdditionalAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetListingItemAdditionalAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProductItemAdditionalAttributes:
    boto3_raw_data: "type_defs.DataProductItemAdditionalAttributesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def matchRationale(self):  # pragma: no cover
        return MatchRationaleItem.make_many(self.boto3_raw_data["matchRationale"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataProductItemAdditionalAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataProductItemAdditionalAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProductListingItemAdditionalAttributes:
    boto3_raw_data: "type_defs.DataProductListingItemAdditionalAttributesTypeDef" = (
        dataclasses.field()
    )

    forms = field("forms")

    @cached_property
    def matchRationale(self):  # pragma: no cover
        return MatchRationaleItem.make_many(self.boto3_raw_data["matchRationale"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DataProductListingItemAdditionalAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataProductListingItemAdditionalAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlossaryItemAdditionalAttributes:
    boto3_raw_data: "type_defs.GlossaryItemAdditionalAttributesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def matchRationale(self):  # pragma: no cover
        return MatchRationaleItem.make_many(self.boto3_raw_data["matchRationale"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GlossaryItemAdditionalAttributesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlossaryItemAdditionalAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlossaryTermItemAdditionalAttributes:
    boto3_raw_data: "type_defs.GlossaryTermItemAdditionalAttributesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def matchRationale(self):  # pragma: no cover
        return MatchRationaleItem.make_many(self.boto3_raw_data["matchRationale"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GlossaryTermItemAdditionalAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlossaryTermItemAdditionalAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProjectMembershipsOutput:
    boto3_raw_data: "type_defs.ListProjectMembershipsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def members(self):  # pragma: no cover
        return ProjectMember.make_many(self.boto3_raw_data["members"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProjectMembershipsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProjectMembershipsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRuleOutput:
    boto3_raw_data: "type_defs.CreateRuleOutputTypeDef" = dataclasses.field()

    action = field("action")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")

    @cached_property
    def detail(self):  # pragma: no cover
        return RuleDetailOutput.make_one(self.boto3_raw_data["detail"])

    identifier = field("identifier")
    name = field("name")
    ruleType = field("ruleType")

    @cached_property
    def scope(self):  # pragma: no cover
        return RuleScopeOutput.make_one(self.boto3_raw_data["scope"])

    @cached_property
    def target(self):  # pragma: no cover
        return RuleTarget.make_one(self.boto3_raw_data["target"])

    targetType = field("targetType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateRuleOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRuleOutput:
    boto3_raw_data: "type_defs.GetRuleOutputTypeDef" = dataclasses.field()

    action = field("action")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")

    @cached_property
    def detail(self):  # pragma: no cover
        return RuleDetailOutput.make_one(self.boto3_raw_data["detail"])

    identifier = field("identifier")
    lastUpdatedBy = field("lastUpdatedBy")
    name = field("name")
    revision = field("revision")
    ruleType = field("ruleType")

    @cached_property
    def scope(self):  # pragma: no cover
        return RuleScopeOutput.make_one(self.boto3_raw_data["scope"])

    @cached_property
    def target(self):  # pragma: no cover
        return RuleTarget.make_one(self.boto3_raw_data["target"])

    targetType = field("targetType")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRuleOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetRuleOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRuleOutput:
    boto3_raw_data: "type_defs.UpdateRuleOutputTypeDef" = dataclasses.field()

    action = field("action")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")

    @cached_property
    def detail(self):  # pragma: no cover
        return RuleDetailOutput.make_one(self.boto3_raw_data["detail"])

    identifier = field("identifier")
    lastUpdatedBy = field("lastUpdatedBy")
    name = field("name")
    revision = field("revision")
    ruleType = field("ruleType")

    @cached_property
    def scope(self):  # pragma: no cover
        return RuleScopeOutput.make_one(self.boto3_raw_data["scope"])

    @cached_property
    def target(self):  # pragma: no cover
        return RuleTarget.make_one(self.boto3_raw_data["target"])

    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateRuleOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LineageEventSummary:
    boto3_raw_data: "type_defs.LineageEventSummaryTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    domainId = field("domainId")

    @cached_property
    def eventSummary(self):  # pragma: no cover
        return EventSummary.make_one(self.boto3_raw_data["eventSummary"])

    eventTime = field("eventTime")
    id = field("id")
    processingStatus = field("processingStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LineageEventSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LineageEventSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RowFilterConfigurationOutput:
    boto3_raw_data: "type_defs.RowFilterConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def rowFilter(self):  # pragma: no cover
        return RowFilterOutput.make_one(self.boto3_raw_data["rowFilter"])

    sensitive = field("sensitive")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RowFilterConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RowFilterConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RowFilterConfiguration:
    boto3_raw_data: "type_defs.RowFilterConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def rowFilter(self):  # pragma: no cover
        return RowFilter.make_one(self.boto3_raw_data["rowFilter"])

    sensitive = field("sensitive")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RowFilterConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RowFilterConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNotificationsOutput:
    boto3_raw_data: "type_defs.ListNotificationsOutputTypeDef" = dataclasses.field()

    @cached_property
    def notifications(self):  # pragma: no cover
        return NotificationOutput.make_many(self.boto3_raw_data["notifications"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNotificationsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotificationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlueConnection:
    boto3_raw_data: "type_defs.GlueConnectionTypeDef" = dataclasses.field()

    athenaProperties = field("athenaProperties")

    @cached_property
    def authenticationConfiguration(self):  # pragma: no cover
        return AuthenticationConfiguration.make_one(
            self.boto3_raw_data["authenticationConfiguration"]
        )

    compatibleComputeEnvironments = field("compatibleComputeEnvironments")
    connectionProperties = field("connectionProperties")
    connectionSchemaVersion = field("connectionSchemaVersion")
    connectionType = field("connectionType")
    creationTime = field("creationTime")
    description = field("description")
    lastConnectionValidationTime = field("lastConnectionValidationTime")
    lastUpdatedBy = field("lastUpdatedBy")
    lastUpdatedTime = field("lastUpdatedTime")
    matchCriteria = field("matchCriteria")
    name = field("name")

    @cached_property
    def physicalConnectionRequirements(self):  # pragma: no cover
        return PhysicalConnectionRequirementsOutput.make_one(
            self.boto3_raw_data["physicalConnectionRequirements"]
        )

    pythonProperties = field("pythonProperties")
    sparkProperties = field("sparkProperties")
    status = field("status")
    statusReason = field("statusReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GlueConnectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GlueConnectionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthenticationConfigurationInput:
    boto3_raw_data: "type_defs.AuthenticationConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    authenticationType = field("authenticationType")

    @cached_property
    def basicAuthenticationCredentials(self):  # pragma: no cover
        return BasicAuthenticationCredentials.make_one(
            self.boto3_raw_data["basicAuthenticationCredentials"]
        )

    customAuthenticationCredentials = field("customAuthenticationCredentials")
    kmsKeyArn = field("kmsKeyArn")
    oAuth2Properties = field("oAuth2Properties")
    secretArn = field("secretArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AuthenticationConfigurationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthenticationConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRulesOutput:
    boto3_raw_data: "type_defs.ListRulesOutputTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return RuleSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListRulesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListRulesOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionPropertiesOutput:
    boto3_raw_data: "type_defs.ConnectionPropertiesOutputTypeDef" = dataclasses.field()

    @cached_property
    def athenaProperties(self):  # pragma: no cover
        return AthenaPropertiesOutput.make_one(self.boto3_raw_data["athenaProperties"])

    @cached_property
    def glueProperties(self):  # pragma: no cover
        return GluePropertiesOutput.make_one(self.boto3_raw_data["glueProperties"])

    @cached_property
    def hyperPodProperties(self):  # pragma: no cover
        return HyperPodPropertiesOutput.make_one(
            self.boto3_raw_data["hyperPodProperties"]
        )

    @cached_property
    def iamProperties(self):  # pragma: no cover
        return IamPropertiesOutput.make_one(self.boto3_raw_data["iamProperties"])

    @cached_property
    def redshiftProperties(self):  # pragma: no cover
        return RedshiftPropertiesOutput.make_one(
            self.boto3_raw_data["redshiftProperties"]
        )

    @cached_property
    def s3Properties(self):  # pragma: no cover
        return S3PropertiesOutput.make_one(self.boto3_raw_data["s3Properties"])

    @cached_property
    def sparkEmrProperties(self):  # pragma: no cover
        return SparkEmrPropertiesOutput.make_one(
            self.boto3_raw_data["sparkEmrProperties"]
        )

    @cached_property
    def sparkGlueProperties(self):  # pragma: no cover
        return SparkGluePropertiesOutput.make_one(
            self.boto3_raw_data["sparkGlueProperties"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectionPropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceConfigurationOutput:
    boto3_raw_data: "type_defs.DataSourceConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def glueRunConfiguration(self):  # pragma: no cover
        return GlueRunConfigurationOutput.make_one(
            self.boto3_raw_data["glueRunConfiguration"]
        )

    @cached_property
    def redshiftRunConfiguration(self):  # pragma: no cover
        return RedshiftRunConfigurationOutput.make_one(
            self.boto3_raw_data["redshiftRunConfiguration"]
        )

    @cached_property
    def sageMakerRunConfiguration(self):  # pragma: no cover
        return SageMakerRunConfigurationOutput.make_one(
            self.boto3_raw_data["sageMakerRunConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DataSourceConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchUserProfilesOutput:
    boto3_raw_data: "type_defs.SearchUserProfilesOutputTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return UserProfileSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchUserProfilesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchUserProfilesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetListingOutput:
    boto3_raw_data: "type_defs.GetListingOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    domainId = field("domainId")
    id = field("id")

    @cached_property
    def item(self):  # pragma: no cover
        return ListingItem.make_one(self.boto3_raw_data["item"])

    listingRevision = field("listingRevision")
    name = field("name")
    status = field("status")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetListingOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetListingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AcceptSubscriptionRequestOutput:
    boto3_raw_data: "type_defs.AcceptSubscriptionRequestOutputTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    decisionComment = field("decisionComment")
    domainId = field("domainId")
    existingSubscriptionId = field("existingSubscriptionId")
    id = field("id")

    @cached_property
    def metadataForms(self):  # pragma: no cover
        return FormOutput.make_many(self.boto3_raw_data["metadataForms"])

    requestReason = field("requestReason")
    reviewerId = field("reviewerId")
    status = field("status")

    @cached_property
    def subscribedListings(self):  # pragma: no cover
        return SubscribedListing.make_many(self.boto3_raw_data["subscribedListings"])

    @cached_property
    def subscribedPrincipals(self):  # pragma: no cover
        return SubscribedPrincipal.make_many(
            self.boto3_raw_data["subscribedPrincipals"]
        )

    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AcceptSubscriptionRequestOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptSubscriptionRequestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelSubscriptionOutput:
    boto3_raw_data: "type_defs.CancelSubscriptionOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    domainId = field("domainId")
    id = field("id")
    retainPermissions = field("retainPermissions")
    status = field("status")

    @cached_property
    def subscribedListing(self):  # pragma: no cover
        return SubscribedListing.make_one(self.boto3_raw_data["subscribedListing"])

    @cached_property
    def subscribedPrincipal(self):  # pragma: no cover
        return SubscribedPrincipal.make_one(self.boto3_raw_data["subscribedPrincipal"])

    subscriptionRequestId = field("subscriptionRequestId")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelSubscriptionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelSubscriptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSubscriptionRequestOutput:
    boto3_raw_data: "type_defs.CreateSubscriptionRequestOutputTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    decisionComment = field("decisionComment")
    domainId = field("domainId")
    existingSubscriptionId = field("existingSubscriptionId")
    id = field("id")

    @cached_property
    def metadataForms(self):  # pragma: no cover
        return FormOutput.make_many(self.boto3_raw_data["metadataForms"])

    requestReason = field("requestReason")
    reviewerId = field("reviewerId")
    status = field("status")

    @cached_property
    def subscribedListings(self):  # pragma: no cover
        return SubscribedListing.make_many(self.boto3_raw_data["subscribedListings"])

    @cached_property
    def subscribedPrincipals(self):  # pragma: no cover
        return SubscribedPrincipal.make_many(
            self.boto3_raw_data["subscribedPrincipals"]
        )

    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSubscriptionRequestOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSubscriptionRequestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSubscriptionOutput:
    boto3_raw_data: "type_defs.GetSubscriptionOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    domainId = field("domainId")
    id = field("id")
    retainPermissions = field("retainPermissions")
    status = field("status")

    @cached_property
    def subscribedListing(self):  # pragma: no cover
        return SubscribedListing.make_one(self.boto3_raw_data["subscribedListing"])

    @cached_property
    def subscribedPrincipal(self):  # pragma: no cover
        return SubscribedPrincipal.make_one(self.boto3_raw_data["subscribedPrincipal"])

    subscriptionRequestId = field("subscriptionRequestId")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSubscriptionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSubscriptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSubscriptionRequestDetailsOutput:
    boto3_raw_data: "type_defs.GetSubscriptionRequestDetailsOutputTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    decisionComment = field("decisionComment")
    domainId = field("domainId")
    existingSubscriptionId = field("existingSubscriptionId")
    id = field("id")

    @cached_property
    def metadataForms(self):  # pragma: no cover
        return FormOutput.make_many(self.boto3_raw_data["metadataForms"])

    requestReason = field("requestReason")
    reviewerId = field("reviewerId")
    status = field("status")

    @cached_property
    def subscribedListings(self):  # pragma: no cover
        return SubscribedListing.make_many(self.boto3_raw_data["subscribedListings"])

    @cached_property
    def subscribedPrincipals(self):  # pragma: no cover
        return SubscribedPrincipal.make_many(
            self.boto3_raw_data["subscribedPrincipals"]
        )

    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSubscriptionRequestDetailsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSubscriptionRequestDetailsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectSubscriptionRequestOutput:
    boto3_raw_data: "type_defs.RejectSubscriptionRequestOutputTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    decisionComment = field("decisionComment")
    domainId = field("domainId")
    existingSubscriptionId = field("existingSubscriptionId")
    id = field("id")

    @cached_property
    def metadataForms(self):  # pragma: no cover
        return FormOutput.make_many(self.boto3_raw_data["metadataForms"])

    requestReason = field("requestReason")
    reviewerId = field("reviewerId")
    status = field("status")

    @cached_property
    def subscribedListings(self):  # pragma: no cover
        return SubscribedListing.make_many(self.boto3_raw_data["subscribedListings"])

    @cached_property
    def subscribedPrincipals(self):  # pragma: no cover
        return SubscribedPrincipal.make_many(
            self.boto3_raw_data["subscribedPrincipals"]
        )

    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RejectSubscriptionRequestOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectSubscriptionRequestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokeSubscriptionOutput:
    boto3_raw_data: "type_defs.RevokeSubscriptionOutputTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    domainId = field("domainId")
    id = field("id")
    retainPermissions = field("retainPermissions")
    status = field("status")

    @cached_property
    def subscribedListing(self):  # pragma: no cover
        return SubscribedListing.make_one(self.boto3_raw_data["subscribedListing"])

    @cached_property
    def subscribedPrincipal(self):  # pragma: no cover
        return SubscribedPrincipal.make_one(self.boto3_raw_data["subscribedPrincipal"])

    subscriptionRequestId = field("subscriptionRequestId")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RevokeSubscriptionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokeSubscriptionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscriptionRequestSummary:
    boto3_raw_data: "type_defs.SubscriptionRequestSummaryTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    domainId = field("domainId")
    id = field("id")
    requestReason = field("requestReason")
    status = field("status")

    @cached_property
    def subscribedListings(self):  # pragma: no cover
        return SubscribedListing.make_many(self.boto3_raw_data["subscribedListings"])

    @cached_property
    def subscribedPrincipals(self):  # pragma: no cover
        return SubscribedPrincipal.make_many(
            self.boto3_raw_data["subscribedPrincipals"]
        )

    updatedAt = field("updatedAt")
    decisionComment = field("decisionComment")
    existingSubscriptionId = field("existingSubscriptionId")

    @cached_property
    def metadataFormsSummary(self):  # pragma: no cover
        return MetadataFormSummary.make_many(
            self.boto3_raw_data["metadataFormsSummary"]
        )

    reviewerId = field("reviewerId")
    updatedBy = field("updatedBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubscriptionRequestSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscriptionRequestSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscriptionSummary:
    boto3_raw_data: "type_defs.SubscriptionSummaryTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    domainId = field("domainId")
    id = field("id")
    status = field("status")

    @cached_property
    def subscribedListing(self):  # pragma: no cover
        return SubscribedListing.make_one(self.boto3_raw_data["subscribedListing"])

    @cached_property
    def subscribedPrincipal(self):  # pragma: no cover
        return SubscribedPrincipal.make_one(self.boto3_raw_data["subscribedPrincipal"])

    updatedAt = field("updatedAt")
    retainPermissions = field("retainPermissions")
    subscriptionRequestId = field("subscriptionRequestId")
    updatedBy = field("updatedBy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubscriptionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscriptionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSubscriptionRequestOutput:
    boto3_raw_data: "type_defs.UpdateSubscriptionRequestOutputTypeDef" = (
        dataclasses.field()
    )

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    decisionComment = field("decisionComment")
    domainId = field("domainId")
    existingSubscriptionId = field("existingSubscriptionId")
    id = field("id")

    @cached_property
    def metadataForms(self):  # pragma: no cover
        return FormOutput.make_many(self.boto3_raw_data["metadataForms"])

    requestReason = field("requestReason")
    reviewerId = field("reviewerId")
    status = field("status")

    @cached_property
    def subscribedListings(self):  # pragma: no cover
        return SubscribedListing.make_many(self.boto3_raw_data["subscribedListings"])

    @cached_property
    def subscribedPrincipals(self):  # pragma: no cover
        return SubscribedPrincipal.make_many(
            self.boto3_raw_data["subscribedPrincipals"]
        )

    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateSubscriptionRequestOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSubscriptionRequestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionPropertiesPatch:
    boto3_raw_data: "type_defs.ConnectionPropertiesPatchTypeDef" = dataclasses.field()

    @cached_property
    def athenaProperties(self):  # pragma: no cover
        return AthenaPropertiesPatch.make_one(self.boto3_raw_data["athenaProperties"])

    @cached_property
    def glueProperties(self):  # pragma: no cover
        return GluePropertiesPatch.make_one(self.boto3_raw_data["glueProperties"])

    @cached_property
    def iamProperties(self):  # pragma: no cover
        return IamPropertiesPatch.make_one(self.boto3_raw_data["iamProperties"])

    @cached_property
    def redshiftProperties(self):  # pragma: no cover
        return RedshiftPropertiesPatch.make_one(
            self.boto3_raw_data["redshiftProperties"]
        )

    @cached_property
    def s3Properties(self):  # pragma: no cover
        return S3PropertiesPatch.make_one(self.boto3_raw_data["s3Properties"])

    @cached_property
    def sparkEmrProperties(self):  # pragma: no cover
        return SparkEmrPropertiesPatch.make_one(
            self.boto3_raw_data["sparkEmrProperties"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectionPropertiesPatchTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionPropertiesPatchTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyGrantMember:
    boto3_raw_data: "type_defs.PolicyGrantMemberTypeDef" = dataclasses.field()

    createdAt = field("createdAt")
    createdBy = field("createdBy")

    @cached_property
    def detail(self):  # pragma: no cover
        return PolicyGrantDetailOutput.make_one(self.boto3_raw_data["detail"])

    grantId = field("grantId")

    @cached_property
    def principal(self):  # pragma: no cover
        return PolicyGrantPrincipalOutput.make_one(self.boto3_raw_data["principal"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyGrantMemberTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyGrantMemberTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSourceConfigurationInput:
    boto3_raw_data: "type_defs.DataSourceConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def glueRunConfiguration(self):  # pragma: no cover
        return GlueRunConfigurationInput.make_one(
            self.boto3_raw_data["glueRunConfiguration"]
        )

    @cached_property
    def redshiftRunConfiguration(self):  # pragma: no cover
        return RedshiftRunConfigurationInput.make_one(
            self.boto3_raw_data["redshiftRunConfiguration"]
        )

    @cached_property
    def sageMakerRunConfiguration(self):  # pragma: no cover
        return SageMakerRunConfigurationInput.make_one(
            self.boto3_raw_data["sageMakerRunConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataSourceConfigurationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataSourceConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutEnvironmentBlueprintConfigurationInput:
    boto3_raw_data: "type_defs.PutEnvironmentBlueprintConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    domainIdentifier = field("domainIdentifier")
    enabledRegions = field("enabledRegions")
    environmentBlueprintIdentifier = field("environmentBlueprintIdentifier")
    environmentRolePermissionBoundary = field("environmentRolePermissionBoundary")
    globalParameters = field("globalParameters")
    manageAccessRoleArn = field("manageAccessRoleArn")
    provisioningConfigurations = field("provisioningConfigurations")
    provisioningRoleArn = field("provisioningRoleArn")
    regionalParameters = field("regionalParameters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutEnvironmentBlueprintConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutEnvironmentBlueprintConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetItem:
    boto3_raw_data: "type_defs.AssetItemTypeDef" = dataclasses.field()

    domainId = field("domainId")
    identifier = field("identifier")
    name = field("name")
    owningProjectId = field("owningProjectId")
    typeIdentifier = field("typeIdentifier")
    typeRevision = field("typeRevision")

    @cached_property
    def additionalAttributes(self):  # pragma: no cover
        return AssetItemAdditionalAttributes.make_one(
            self.boto3_raw_data["additionalAttributes"]
        )

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    externalIdentifier = field("externalIdentifier")
    firstRevisionCreatedAt = field("firstRevisionCreatedAt")
    firstRevisionCreatedBy = field("firstRevisionCreatedBy")
    glossaryTerms = field("glossaryTerms")
    governedGlossaryTerms = field("governedGlossaryTerms")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssetItemTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetListingItem:
    boto3_raw_data: "type_defs.AssetListingItemTypeDef" = dataclasses.field()

    @cached_property
    def additionalAttributes(self):  # pragma: no cover
        return AssetListingItemAdditionalAttributes.make_one(
            self.boto3_raw_data["additionalAttributes"]
        )

    createdAt = field("createdAt")
    description = field("description")
    entityId = field("entityId")
    entityRevision = field("entityRevision")
    entityType = field("entityType")

    @cached_property
    def glossaryTerms(self):  # pragma: no cover
        return DetailedGlossaryTerm.make_many(self.boto3_raw_data["glossaryTerms"])

    @cached_property
    def governedGlossaryTerms(self):  # pragma: no cover
        return DetailedGlossaryTerm.make_many(
            self.boto3_raw_data["governedGlossaryTerms"]
        )

    listingCreatedBy = field("listingCreatedBy")
    listingId = field("listingId")
    listingRevision = field("listingRevision")
    listingUpdatedBy = field("listingUpdatedBy")
    name = field("name")
    owningProjectId = field("owningProjectId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssetListingItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetListingItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProductResultItem:
    boto3_raw_data: "type_defs.DataProductResultItemTypeDef" = dataclasses.field()

    domainId = field("domainId")
    id = field("id")
    name = field("name")
    owningProjectId = field("owningProjectId")

    @cached_property
    def additionalAttributes(self):  # pragma: no cover
        return DataProductItemAdditionalAttributes.make_one(
            self.boto3_raw_data["additionalAttributes"]
        )

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    firstRevisionCreatedAt = field("firstRevisionCreatedAt")
    firstRevisionCreatedBy = field("firstRevisionCreatedBy")
    glossaryTerms = field("glossaryTerms")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataProductResultItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataProductResultItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataProductListingItem:
    boto3_raw_data: "type_defs.DataProductListingItemTypeDef" = dataclasses.field()

    @cached_property
    def additionalAttributes(self):  # pragma: no cover
        return DataProductListingItemAdditionalAttributes.make_one(
            self.boto3_raw_data["additionalAttributes"]
        )

    createdAt = field("createdAt")
    description = field("description")
    entityId = field("entityId")
    entityRevision = field("entityRevision")

    @cached_property
    def glossaryTerms(self):  # pragma: no cover
        return DetailedGlossaryTerm.make_many(self.boto3_raw_data["glossaryTerms"])

    @cached_property
    def items(self):  # pragma: no cover
        return ListingSummaryItem.make_many(self.boto3_raw_data["items"])

    listingCreatedBy = field("listingCreatedBy")
    listingId = field("listingId")
    listingRevision = field("listingRevision")
    listingUpdatedBy = field("listingUpdatedBy")
    name = field("name")
    owningProjectId = field("owningProjectId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataProductListingItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataProductListingItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlossaryItem:
    boto3_raw_data: "type_defs.GlossaryItemTypeDef" = dataclasses.field()

    domainId = field("domainId")
    id = field("id")
    name = field("name")
    owningProjectId = field("owningProjectId")
    status = field("status")

    @cached_property
    def additionalAttributes(self):  # pragma: no cover
        return GlossaryItemAdditionalAttributes.make_one(
            self.boto3_raw_data["additionalAttributes"]
        )

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    description = field("description")
    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")
    usageRestrictions = field("usageRestrictions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GlossaryItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GlossaryItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlossaryTermItem:
    boto3_raw_data: "type_defs.GlossaryTermItemTypeDef" = dataclasses.field()

    domainId = field("domainId")
    glossaryId = field("glossaryId")
    id = field("id")
    name = field("name")
    status = field("status")

    @cached_property
    def additionalAttributes(self):  # pragma: no cover
        return GlossaryTermItemAdditionalAttributes.make_one(
            self.boto3_raw_data["additionalAttributes"]
        )

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    longDescription = field("longDescription")
    shortDescription = field("shortDescription")

    @cached_property
    def termRelations(self):  # pragma: no cover
        return TermRelationsOutput.make_one(self.boto3_raw_data["termRelations"])

    updatedAt = field("updatedAt")
    updatedBy = field("updatedBy")
    usageRestrictions = field("usageRestrictions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GlossaryTermItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlossaryTermItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRuleInput:
    boto3_raw_data: "type_defs.CreateRuleInputTypeDef" = dataclasses.field()

    action = field("action")
    detail = field("detail")
    domainIdentifier = field("domainIdentifier")
    name = field("name")
    scope = field("scope")

    @cached_property
    def target(self):  # pragma: no cover
        return RuleTarget.make_one(self.boto3_raw_data["target"])

    clientToken = field("clientToken")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateRuleInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CreateRuleInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRuleInput:
    boto3_raw_data: "type_defs.UpdateRuleInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    description = field("description")
    detail = field("detail")
    includeChildDomainUnits = field("includeChildDomainUnits")
    name = field("name")
    scope = field("scope")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateRuleInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateRuleInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLineageEventsOutput:
    boto3_raw_data: "type_defs.ListLineageEventsOutputTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return LineageEventSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLineageEventsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLineageEventsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetFilterConfigurationOutput:
    boto3_raw_data: "type_defs.AssetFilterConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def columnConfiguration(self):  # pragma: no cover
        return ColumnFilterConfigurationOutput.make_one(
            self.boto3_raw_data["columnConfiguration"]
        )

    @cached_property
    def rowConfiguration(self):  # pragma: no cover
        return RowFilterConfigurationOutput.make_one(
            self.boto3_raw_data["rowConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssetFilterConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetFilterConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssetFilterConfiguration:
    boto3_raw_data: "type_defs.AssetFilterConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def columnConfiguration(self):  # pragma: no cover
        return ColumnFilterConfiguration.make_one(
            self.boto3_raw_data["columnConfiguration"]
        )

    @cached_property
    def rowConfiguration(self):  # pragma: no cover
        return RowFilterConfiguration.make_one(self.boto3_raw_data["rowConfiguration"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssetFilterConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssetFilterConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhysicalEndpoint:
    boto3_raw_data: "type_defs.PhysicalEndpointTypeDef" = dataclasses.field()

    @cached_property
    def awsLocation(self):  # pragma: no cover
        return AwsLocation.make_one(self.boto3_raw_data["awsLocation"])

    @cached_property
    def glueConnection(self):  # pragma: no cover
        return GlueConnection.make_one(self.boto3_raw_data["glueConnection"])

    glueConnectionName = field("glueConnectionName")
    host = field("host")
    port = field("port")
    protocol = field("protocol")
    stage = field("stage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PhysicalEndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PhysicalEndpointTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlueConnectionInput:
    boto3_raw_data: "type_defs.GlueConnectionInputTypeDef" = dataclasses.field()

    athenaProperties = field("athenaProperties")

    @cached_property
    def authenticationConfiguration(self):  # pragma: no cover
        return AuthenticationConfigurationInput.make_one(
            self.boto3_raw_data["authenticationConfiguration"]
        )

    connectionProperties = field("connectionProperties")
    connectionType = field("connectionType")
    description = field("description")
    matchCriteria = field("matchCriteria")
    name = field("name")
    physicalConnectionRequirements = field("physicalConnectionRequirements")
    pythonProperties = field("pythonProperties")
    sparkProperties = field("sparkProperties")
    validateCredentials = field("validateCredentials")
    validateForComputeEnvironments = field("validateForComputeEnvironments")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlueConnectionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlueConnectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataSourceOutput:
    boto3_raw_data: "type_defs.CreateDataSourceOutputTypeDef" = dataclasses.field()

    @cached_property
    def assetFormsOutput(self):  # pragma: no cover
        return FormOutput.make_many(self.boto3_raw_data["assetFormsOutput"])

    @cached_property
    def configuration(self):  # pragma: no cover
        return DataSourceConfigurationOutput.make_one(
            self.boto3_raw_data["configuration"]
        )

    connectionId = field("connectionId")
    createdAt = field("createdAt")
    description = field("description")
    domainId = field("domainId")
    enableSetting = field("enableSetting")
    environmentId = field("environmentId")

    @cached_property
    def errorMessage(self):  # pragma: no cover
        return DataSourceErrorMessage.make_one(self.boto3_raw_data["errorMessage"])

    id = field("id")
    lastRunAt = field("lastRunAt")

    @cached_property
    def lastRunErrorMessage(self):  # pragma: no cover
        return DataSourceErrorMessage.make_one(
            self.boto3_raw_data["lastRunErrorMessage"]
        )

    lastRunStatus = field("lastRunStatus")
    name = field("name")
    projectId = field("projectId")
    publishOnImport = field("publishOnImport")

    @cached_property
    def recommendation(self):  # pragma: no cover
        return RecommendationConfiguration.make_one(
            self.boto3_raw_data["recommendation"]
        )

    @cached_property
    def schedule(self):  # pragma: no cover
        return ScheduleConfiguration.make_one(self.boto3_raw_data["schedule"])

    status = field("status")
    type = field("type")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataSourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataSourceOutput:
    boto3_raw_data: "type_defs.DeleteDataSourceOutputTypeDef" = dataclasses.field()

    @cached_property
    def assetFormsOutput(self):  # pragma: no cover
        return FormOutput.make_many(self.boto3_raw_data["assetFormsOutput"])

    @cached_property
    def configuration(self):  # pragma: no cover
        return DataSourceConfigurationOutput.make_one(
            self.boto3_raw_data["configuration"]
        )

    connectionId = field("connectionId")
    createdAt = field("createdAt")
    description = field("description")
    domainId = field("domainId")
    enableSetting = field("enableSetting")
    environmentId = field("environmentId")

    @cached_property
    def errorMessage(self):  # pragma: no cover
        return DataSourceErrorMessage.make_one(self.boto3_raw_data["errorMessage"])

    id = field("id")
    lastRunAt = field("lastRunAt")

    @cached_property
    def lastRunErrorMessage(self):  # pragma: no cover
        return DataSourceErrorMessage.make_one(
            self.boto3_raw_data["lastRunErrorMessage"]
        )

    lastRunStatus = field("lastRunStatus")
    name = field("name")
    projectId = field("projectId")
    publishOnImport = field("publishOnImport")
    retainPermissionsOnRevokeFailure = field("retainPermissionsOnRevokeFailure")

    @cached_property
    def schedule(self):  # pragma: no cover
        return ScheduleConfiguration.make_one(self.boto3_raw_data["schedule"])

    @cached_property
    def selfGrantStatus(self):  # pragma: no cover
        return SelfGrantStatusOutput.make_one(self.boto3_raw_data["selfGrantStatus"])

    status = field("status")
    type = field("type")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDataSourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataSourceOutput:
    boto3_raw_data: "type_defs.GetDataSourceOutputTypeDef" = dataclasses.field()

    @cached_property
    def assetFormsOutput(self):  # pragma: no cover
        return FormOutput.make_many(self.boto3_raw_data["assetFormsOutput"])

    @cached_property
    def configuration(self):  # pragma: no cover
        return DataSourceConfigurationOutput.make_one(
            self.boto3_raw_data["configuration"]
        )

    connectionId = field("connectionId")
    createdAt = field("createdAt")
    description = field("description")
    domainId = field("domainId")
    enableSetting = field("enableSetting")
    environmentId = field("environmentId")

    @cached_property
    def errorMessage(self):  # pragma: no cover
        return DataSourceErrorMessage.make_one(self.boto3_raw_data["errorMessage"])

    id = field("id")
    lastRunAssetCount = field("lastRunAssetCount")
    lastRunAt = field("lastRunAt")

    @cached_property
    def lastRunErrorMessage(self):  # pragma: no cover
        return DataSourceErrorMessage.make_one(
            self.boto3_raw_data["lastRunErrorMessage"]
        )

    lastRunStatus = field("lastRunStatus")
    name = field("name")
    projectId = field("projectId")
    publishOnImport = field("publishOnImport")

    @cached_property
    def recommendation(self):  # pragma: no cover
        return RecommendationConfiguration.make_one(
            self.boto3_raw_data["recommendation"]
        )

    @cached_property
    def schedule(self):  # pragma: no cover
        return ScheduleConfiguration.make_one(self.boto3_raw_data["schedule"])

    @cached_property
    def selfGrantStatus(self):  # pragma: no cover
        return SelfGrantStatusOutput.make_one(self.boto3_raw_data["selfGrantStatus"])

    status = field("status")
    type = field("type")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDataSourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataSourceOutput:
    boto3_raw_data: "type_defs.UpdateDataSourceOutputTypeDef" = dataclasses.field()

    @cached_property
    def assetFormsOutput(self):  # pragma: no cover
        return FormOutput.make_many(self.boto3_raw_data["assetFormsOutput"])

    @cached_property
    def configuration(self):  # pragma: no cover
        return DataSourceConfigurationOutput.make_one(
            self.boto3_raw_data["configuration"]
        )

    connectionId = field("connectionId")
    createdAt = field("createdAt")
    description = field("description")
    domainId = field("domainId")
    enableSetting = field("enableSetting")
    environmentId = field("environmentId")

    @cached_property
    def errorMessage(self):  # pragma: no cover
        return DataSourceErrorMessage.make_one(self.boto3_raw_data["errorMessage"])

    id = field("id")
    lastRunAt = field("lastRunAt")

    @cached_property
    def lastRunErrorMessage(self):  # pragma: no cover
        return DataSourceErrorMessage.make_one(
            self.boto3_raw_data["lastRunErrorMessage"]
        )

    lastRunStatus = field("lastRunStatus")
    name = field("name")
    projectId = field("projectId")
    publishOnImport = field("publishOnImport")

    @cached_property
    def recommendation(self):  # pragma: no cover
        return RecommendationConfiguration.make_one(
            self.boto3_raw_data["recommendation"]
        )

    retainPermissionsOnRevokeFailure = field("retainPermissionsOnRevokeFailure")

    @cached_property
    def schedule(self):  # pragma: no cover
        return ScheduleConfiguration.make_one(self.boto3_raw_data["schedule"])

    @cached_property
    def selfGrantStatus(self):  # pragma: no cover
        return SelfGrantStatusOutput.make_one(self.boto3_raw_data["selfGrantStatus"])

    status = field("status")
    type = field("type")
    updatedAt = field("updatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDataSourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubscriptionRequestsOutput:
    boto3_raw_data: "type_defs.ListSubscriptionRequestsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def items(self):  # pragma: no cover
        return SubscriptionRequestSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSubscriptionRequestsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubscriptionRequestsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSubscriptionsOutput:
    boto3_raw_data: "type_defs.ListSubscriptionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return SubscriptionSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSubscriptionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSubscriptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectionInput:
    boto3_raw_data: "type_defs.UpdateConnectionInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @cached_property
    def awsLocation(self):  # pragma: no cover
        return AwsLocation.make_one(self.boto3_raw_data["awsLocation"])

    description = field("description")

    @cached_property
    def props(self):  # pragma: no cover
        return ConnectionPropertiesPatch.make_one(self.boto3_raw_data["props"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConnectionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyGrantsOutput:
    boto3_raw_data: "type_defs.ListPolicyGrantsOutputTypeDef" = dataclasses.field()

    @cached_property
    def grantList(self):  # pragma: no cover
        return PolicyGrantMember.make_many(self.boto3_raw_data["grantList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPolicyGrantsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyGrantsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddPolicyGrantInput:
    boto3_raw_data: "type_defs.AddPolicyGrantInputTypeDef" = dataclasses.field()

    detail = field("detail")
    domainIdentifier = field("domainIdentifier")
    entityIdentifier = field("entityIdentifier")
    entityType = field("entityType")
    policyType = field("policyType")
    principal = field("principal")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddPolicyGrantInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddPolicyGrantInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemovePolicyGrantInput:
    boto3_raw_data: "type_defs.RemovePolicyGrantInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    entityIdentifier = field("entityIdentifier")
    entityType = field("entityType")
    policyType = field("policyType")
    principal = field("principal")
    clientToken = field("clientToken")
    grantIdentifier = field("grantIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemovePolicyGrantInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemovePolicyGrantInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProjectProfileInput:
    boto3_raw_data: "type_defs.CreateProjectProfileInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    name = field("name")
    description = field("description")
    domainUnitIdentifier = field("domainUnitIdentifier")
    environmentConfigurations = field("environmentConfigurations")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProjectProfileInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProjectProfileInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProjectProfileInput:
    boto3_raw_data: "type_defs.UpdateProjectProfileInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    description = field("description")
    domainUnitIdentifier = field("domainUnitIdentifier")
    environmentConfigurations = field("environmentConfigurations")
    name = field("name")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProjectProfileInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProjectProfileInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDataSourceInput:
    boto3_raw_data: "type_defs.CreateDataSourceInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    name = field("name")
    projectIdentifier = field("projectIdentifier")
    type = field("type")

    @cached_property
    def assetFormsInput(self):  # pragma: no cover
        return FormInput.make_many(self.boto3_raw_data["assetFormsInput"])

    clientToken = field("clientToken")

    @cached_property
    def configuration(self):  # pragma: no cover
        return DataSourceConfigurationInput.make_one(
            self.boto3_raw_data["configuration"]
        )

    connectionIdentifier = field("connectionIdentifier")
    description = field("description")
    enableSetting = field("enableSetting")
    environmentIdentifier = field("environmentIdentifier")
    publishOnImport = field("publishOnImport")

    @cached_property
    def recommendation(self):  # pragma: no cover
        return RecommendationConfiguration.make_one(
            self.boto3_raw_data["recommendation"]
        )

    @cached_property
    def schedule(self):  # pragma: no cover
        return ScheduleConfiguration.make_one(self.boto3_raw_data["schedule"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDataSourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDataSourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDataSourceInput:
    boto3_raw_data: "type_defs.UpdateDataSourceInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")

    @cached_property
    def assetFormsInput(self):  # pragma: no cover
        return FormInput.make_many(self.boto3_raw_data["assetFormsInput"])

    @cached_property
    def configuration(self):  # pragma: no cover
        return DataSourceConfigurationInput.make_one(
            self.boto3_raw_data["configuration"]
        )

    description = field("description")
    enableSetting = field("enableSetting")
    name = field("name")
    publishOnImport = field("publishOnImport")

    @cached_property
    def recommendation(self):  # pragma: no cover
        return RecommendationConfiguration.make_one(
            self.boto3_raw_data["recommendation"]
        )

    retainPermissionsOnRevokeFailure = field("retainPermissionsOnRevokeFailure")

    @cached_property
    def schedule(self):  # pragma: no cover
        return ScheduleConfiguration.make_one(self.boto3_raw_data["schedule"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDataSourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDataSourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchResultItem:
    boto3_raw_data: "type_defs.SearchResultItemTypeDef" = dataclasses.field()

    @cached_property
    def assetListing(self):  # pragma: no cover
        return AssetListingItem.make_one(self.boto3_raw_data["assetListing"])

    @cached_property
    def dataProductListing(self):  # pragma: no cover
        return DataProductListingItem.make_one(
            self.boto3_raw_data["dataProductListing"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchResultItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchResultItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchInventoryResultItem:
    boto3_raw_data: "type_defs.SearchInventoryResultItemTypeDef" = dataclasses.field()

    @cached_property
    def assetItem(self):  # pragma: no cover
        return AssetItem.make_one(self.boto3_raw_data["assetItem"])

    @cached_property
    def dataProductItem(self):  # pragma: no cover
        return DataProductResultItem.make_one(self.boto3_raw_data["dataProductItem"])

    @cached_property
    def glossaryItem(self):  # pragma: no cover
        return GlossaryItem.make_one(self.boto3_raw_data["glossaryItem"])

    @cached_property
    def glossaryTermItem(self):  # pragma: no cover
        return GlossaryTermItem.make_one(self.boto3_raw_data["glossaryTermItem"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchInventoryResultItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchInventoryResultItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssetFilterOutput:
    boto3_raw_data: "type_defs.CreateAssetFilterOutputTypeDef" = dataclasses.field()

    assetId = field("assetId")

    @cached_property
    def configuration(self):  # pragma: no cover
        return AssetFilterConfigurationOutput.make_one(
            self.boto3_raw_data["configuration"]
        )

    createdAt = field("createdAt")
    description = field("description")
    domainId = field("domainId")
    effectiveColumnNames = field("effectiveColumnNames")
    effectiveRowFilter = field("effectiveRowFilter")
    errorMessage = field("errorMessage")
    id = field("id")
    name = field("name")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAssetFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssetFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssetFilterOutput:
    boto3_raw_data: "type_defs.GetAssetFilterOutputTypeDef" = dataclasses.field()

    assetId = field("assetId")

    @cached_property
    def configuration(self):  # pragma: no cover
        return AssetFilterConfigurationOutput.make_one(
            self.boto3_raw_data["configuration"]
        )

    createdAt = field("createdAt")
    description = field("description")
    domainId = field("domainId")
    effectiveColumnNames = field("effectiveColumnNames")
    effectiveRowFilter = field("effectiveRowFilter")
    errorMessage = field("errorMessage")
    id = field("id")
    name = field("name")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAssetFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssetFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssetFilterOutput:
    boto3_raw_data: "type_defs.UpdateAssetFilterOutputTypeDef" = dataclasses.field()

    assetId = field("assetId")

    @cached_property
    def configuration(self):  # pragma: no cover
        return AssetFilterConfigurationOutput.make_one(
            self.boto3_raw_data["configuration"]
        )

    createdAt = field("createdAt")
    description = field("description")
    domainId = field("domainId")
    effectiveColumnNames = field("effectiveColumnNames")
    effectiveRowFilter = field("effectiveRowFilter")
    errorMessage = field("errorMessage")
    id = field("id")
    name = field("name")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAssetFilterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssetFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionSummary:
    boto3_raw_data: "type_defs.ConnectionSummaryTypeDef" = dataclasses.field()

    connectionId = field("connectionId")
    domainId = field("domainId")
    domainUnitId = field("domainUnitId")
    name = field("name")

    @cached_property
    def physicalEndpoints(self):  # pragma: no cover
        return PhysicalEndpoint.make_many(self.boto3_raw_data["physicalEndpoints"])

    type = field("type")
    environmentId = field("environmentId")
    projectId = field("projectId")

    @cached_property
    def props(self):  # pragma: no cover
        return ConnectionPropertiesOutput.make_one(self.boto3_raw_data["props"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectionSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectionOutput:
    boto3_raw_data: "type_defs.CreateConnectionOutputTypeDef" = dataclasses.field()

    connectionId = field("connectionId")
    description = field("description")
    domainId = field("domainId")
    domainUnitId = field("domainUnitId")
    environmentId = field("environmentId")
    name = field("name")

    @cached_property
    def physicalEndpoints(self):  # pragma: no cover
        return PhysicalEndpoint.make_many(self.boto3_raw_data["physicalEndpoints"])

    projectId = field("projectId")

    @cached_property
    def props(self):  # pragma: no cover
        return ConnectionPropertiesOutput.make_one(self.boto3_raw_data["props"])

    type = field("type")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConnectionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConnectionOutput:
    boto3_raw_data: "type_defs.GetConnectionOutputTypeDef" = dataclasses.field()

    @cached_property
    def connectionCredentials(self):  # pragma: no cover
        return ConnectionCredentials.make_one(
            self.boto3_raw_data["connectionCredentials"]
        )

    connectionId = field("connectionId")
    description = field("description")
    domainId = field("domainId")
    domainUnitId = field("domainUnitId")
    environmentId = field("environmentId")
    environmentUserRole = field("environmentUserRole")
    name = field("name")

    @cached_property
    def physicalEndpoints(self):  # pragma: no cover
        return PhysicalEndpoint.make_many(self.boto3_raw_data["physicalEndpoints"])

    projectId = field("projectId")

    @cached_property
    def props(self):  # pragma: no cover
        return ConnectionPropertiesOutput.make_one(self.boto3_raw_data["props"])

    type = field("type")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConnectionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConnectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectionOutput:
    boto3_raw_data: "type_defs.UpdateConnectionOutputTypeDef" = dataclasses.field()

    connectionId = field("connectionId")
    description = field("description")
    domainId = field("domainId")
    domainUnitId = field("domainUnitId")
    environmentId = field("environmentId")
    name = field("name")

    @cached_property
    def physicalEndpoints(self):  # pragma: no cover
        return PhysicalEndpoint.make_many(self.boto3_raw_data["physicalEndpoints"])

    projectId = field("projectId")

    @cached_property
    def props(self):  # pragma: no cover
        return ConnectionPropertiesOutput.make_one(self.boto3_raw_data["props"])

    type = field("type")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConnectionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GluePropertiesInput:
    boto3_raw_data: "type_defs.GluePropertiesInputTypeDef" = dataclasses.field()

    @cached_property
    def glueConnectionInput(self):  # pragma: no cover
        return GlueConnectionInput.make_one(self.boto3_raw_data["glueConnectionInput"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GluePropertiesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GluePropertiesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchListingsOutput:
    boto3_raw_data: "type_defs.SearchListingsOutputTypeDef" = dataclasses.field()

    @cached_property
    def aggregates(self):  # pragma: no cover
        return AggregationOutput.make_many(self.boto3_raw_data["aggregates"])

    @cached_property
    def items(self):  # pragma: no cover
        return SearchResultItem.make_many(self.boto3_raw_data["items"])

    totalMatchCount = field("totalMatchCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchListingsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchListingsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchOutput:
    boto3_raw_data: "type_defs.SearchOutputTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return SearchInventoryResultItem.make_many(self.boto3_raw_data["items"])

    totalMatchCount = field("totalMatchCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SearchOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssetFilterInput:
    boto3_raw_data: "type_defs.CreateAssetFilterInputTypeDef" = dataclasses.field()

    assetIdentifier = field("assetIdentifier")
    configuration = field("configuration")
    domainIdentifier = field("domainIdentifier")
    name = field("name")
    clientToken = field("clientToken")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAssetFilterInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssetFilterInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssetFilterInput:
    boto3_raw_data: "type_defs.UpdateAssetFilterInputTypeDef" = dataclasses.field()

    assetIdentifier = field("assetIdentifier")
    domainIdentifier = field("domainIdentifier")
    identifier = field("identifier")
    configuration = field("configuration")
    description = field("description")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAssetFilterInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssetFilterInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectionsOutput:
    boto3_raw_data: "type_defs.ListConnectionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def items(self):  # pragma: no cover
        return ConnectionSummary.make_many(self.boto3_raw_data["items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConnectionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionPropertiesInput:
    boto3_raw_data: "type_defs.ConnectionPropertiesInputTypeDef" = dataclasses.field()

    @cached_property
    def athenaProperties(self):  # pragma: no cover
        return AthenaPropertiesInput.make_one(self.boto3_raw_data["athenaProperties"])

    @cached_property
    def glueProperties(self):  # pragma: no cover
        return GluePropertiesInput.make_one(self.boto3_raw_data["glueProperties"])

    @cached_property
    def hyperPodProperties(self):  # pragma: no cover
        return HyperPodPropertiesInput.make_one(
            self.boto3_raw_data["hyperPodProperties"]
        )

    @cached_property
    def iamProperties(self):  # pragma: no cover
        return IamPropertiesInput.make_one(self.boto3_raw_data["iamProperties"])

    @cached_property
    def redshiftProperties(self):  # pragma: no cover
        return RedshiftPropertiesInput.make_one(
            self.boto3_raw_data["redshiftProperties"]
        )

    @cached_property
    def s3Properties(self):  # pragma: no cover
        return S3PropertiesInput.make_one(self.boto3_raw_data["s3Properties"])

    @cached_property
    def sparkEmrProperties(self):  # pragma: no cover
        return SparkEmrPropertiesInput.make_one(
            self.boto3_raw_data["sparkEmrProperties"]
        )

    @cached_property
    def sparkGlueProperties(self):  # pragma: no cover
        return SparkGluePropertiesInput.make_one(
            self.boto3_raw_data["sparkGlueProperties"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectionPropertiesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionPropertiesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectionInput:
    boto3_raw_data: "type_defs.CreateConnectionInputTypeDef" = dataclasses.field()

    domainIdentifier = field("domainIdentifier")
    environmentIdentifier = field("environmentIdentifier")
    name = field("name")

    @cached_property
    def awsLocation(self):  # pragma: no cover
        return AwsLocation.make_one(self.boto3_raw_data["awsLocation"])

    clientToken = field("clientToken")
    description = field("description")

    @cached_property
    def props(self):  # pragma: no cover
        return ConnectionPropertiesInput.make_one(self.boto3_raw_data["props"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConnectionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
