# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_customer_profiles import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AddProfileKeyRequest:
    boto3_raw_data: "type_defs.AddProfileKeyRequestTypeDef" = dataclasses.field()

    ProfileId = field("ProfileId")
    KeyName = field("KeyName")
    Values = field("Values")
    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddProfileKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddProfileKeyRequestTypeDef"]
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
class AdditionalSearchKey:
    boto3_raw_data: "type_defs.AdditionalSearchKeyTypeDef" = dataclasses.field()

    KeyName = field("KeyName")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdditionalSearchKeyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdditionalSearchKeyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileDimensionOutput:
    boto3_raw_data: "type_defs.ProfileDimensionOutputTypeDef" = dataclasses.field()

    DimensionType = field("DimensionType")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProfileDimensionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProfileDimensionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Address:
    boto3_raw_data: "type_defs.AddressTypeDef" = dataclasses.field()

    Address1 = field("Address1")
    Address2 = field("Address2")
    Address3 = field("Address3")
    Address4 = field("Address4")
    City = field("City")
    County = field("County")
    State = field("State")
    Province = field("Province")
    Country = field("Country")
    PostalCode = field("PostalCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddressTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddressTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppflowIntegrationWorkflowAttributes:
    boto3_raw_data: "type_defs.AppflowIntegrationWorkflowAttributesTypeDef" = (
        dataclasses.field()
    )

    SourceConnectorType = field("SourceConnectorType")
    ConnectorProfileName = field("ConnectorProfileName")
    RoleArn = field("RoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AppflowIntegrationWorkflowAttributesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppflowIntegrationWorkflowAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppflowIntegrationWorkflowMetrics:
    boto3_raw_data: "type_defs.AppflowIntegrationWorkflowMetricsTypeDef" = (
        dataclasses.field()
    )

    RecordsProcessed = field("RecordsProcessed")
    StepsCompleted = field("StepsCompleted")
    TotalSteps = field("TotalSteps")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AppflowIntegrationWorkflowMetricsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppflowIntegrationWorkflowMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppflowIntegrationWorkflowStep:
    boto3_raw_data: "type_defs.AppflowIntegrationWorkflowStepTypeDef" = (
        dataclasses.field()
    )

    FlowName = field("FlowName")
    Status = field("Status")
    ExecutionMessage = field("ExecutionMessage")
    RecordsProcessed = field("RecordsProcessed")
    BatchRecordsStartTime = field("BatchRecordsStartTime")
    BatchRecordsEndTime = field("BatchRecordsEndTime")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AppflowIntegrationWorkflowStepTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppflowIntegrationWorkflowStepTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeItem:
    boto3_raw_data: "type_defs.AttributeItemTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributeItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttributeItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeDimensionOutput:
    boto3_raw_data: "type_defs.AttributeDimensionOutputTypeDef" = dataclasses.field()

    DimensionType = field("DimensionType")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeDimensionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeDimensionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeDimension:
    boto3_raw_data: "type_defs.AttributeDimensionTypeDef" = dataclasses.field()

    DimensionType = field("DimensionType")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeDimensionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeDimensionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeTypesSelectorOutput:
    boto3_raw_data: "type_defs.AttributeTypesSelectorOutputTypeDef" = (
        dataclasses.field()
    )

    AttributeMatchingModel = field("AttributeMatchingModel")
    Address = field("Address")
    PhoneNumber = field("PhoneNumber")
    EmailAddress = field("EmailAddress")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeTypesSelectorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeTypesSelectorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeTypesSelector:
    boto3_raw_data: "type_defs.AttributeTypesSelectorTypeDef" = dataclasses.field()

    AttributeMatchingModel = field("AttributeMatchingModel")
    Address = field("Address")
    PhoneNumber = field("PhoneNumber")
    EmailAddress = field("EmailAddress")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeTypesSelectorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeTypesSelectorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeValueItem:
    boto3_raw_data: "type_defs.AttributeValueItemTypeDef" = dataclasses.field()

    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeValueItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeValueItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConflictResolution:
    boto3_raw_data: "type_defs.ConflictResolutionTypeDef" = dataclasses.field()

    ConflictResolvingModel = field("ConflictResolvingModel")
    SourceName = field("SourceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConflictResolutionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConflictResolutionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConsolidationOutput:
    boto3_raw_data: "type_defs.ConsolidationOutputTypeDef" = dataclasses.field()

    MatchingAttributesList = field("MatchingAttributesList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConsolidationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConsolidationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetCalculatedAttributeForProfileError:
    boto3_raw_data: "type_defs.BatchGetCalculatedAttributeForProfileErrorTypeDef" = (
        dataclasses.field()
    )

    Code = field("Code")
    Message = field("Message")
    ProfileId = field("ProfileId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetCalculatedAttributeForProfileErrorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetCalculatedAttributeForProfileErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CalculatedAttributeValue:
    boto3_raw_data: "type_defs.CalculatedAttributeValueTypeDef" = dataclasses.field()

    CalculatedAttributeName = field("CalculatedAttributeName")
    DisplayName = field("DisplayName")
    IsDataPartial = field("IsDataPartial")
    ProfileId = field("ProfileId")
    Value = field("Value")
    LastObjectTimestamp = field("LastObjectTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CalculatedAttributeValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CalculatedAttributeValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetProfileError:
    boto3_raw_data: "type_defs.BatchGetProfileErrorTypeDef" = dataclasses.field()

    Code = field("Code")
    Message = field("Message")
    ProfileId = field("ProfileId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetProfileErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetProfileErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetProfileRequest:
    boto3_raw_data: "type_defs.BatchGetProfileRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    ProfileIds = field("ProfileIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RangeOverride:
    boto3_raw_data: "type_defs.RangeOverrideTypeDef" = dataclasses.field()

    Start = field("Start")
    Unit = field("Unit")
    End = field("End")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RangeOverrideTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RangeOverrideTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Threshold:
    boto3_raw_data: "type_defs.ThresholdTypeDef" = dataclasses.field()

    Value = field("Value")
    Operator = field("Operator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ThresholdTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ThresholdTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectorOperator:
    boto3_raw_data: "type_defs.ConnectorOperatorTypeDef" = dataclasses.field()

    Marketo = field("Marketo")
    S3 = field("S3")
    Salesforce = field("Salesforce")
    ServiceNow = field("ServiceNow")
    Zendesk = field("Zendesk")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectorOperatorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectorOperatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Consolidation:
    boto3_raw_data: "type_defs.ConsolidationTypeDef" = dataclasses.field()

    MatchingAttributesList = field("MatchingAttributesList")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConsolidationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConsolidationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactPreference:
    boto3_raw_data: "type_defs.ContactPreferenceTypeDef" = dataclasses.field()

    KeyName = field("KeyName")
    KeyValue = field("KeyValue")
    ProfileId = field("ProfileId")
    ContactType = field("ContactType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContactPreferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContactPreferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Readiness:
    boto3_raw_data: "type_defs.ReadinessTypeDef" = dataclasses.field()

    ProgressPercentage = field("ProgressPercentage")
    Message = field("Message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReadinessTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ReadinessTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainLayoutRequest:
    boto3_raw_data: "type_defs.CreateDomainLayoutRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    LayoutDefinitionName = field("LayoutDefinitionName")
    Description = field("Description")
    DisplayName = field("DisplayName")
    LayoutType = field("LayoutType")
    Layout = field("Layout")
    IsDefault = field("IsDefault")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDomainLayoutRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainLayoutRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventStreamRequest:
    boto3_raw_data: "type_defs.CreateEventStreamRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    Uri = field("Uri")
    EventStreamName = field("EventStreamName")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEventStreamRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventStreamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSegmentSnapshotRequest:
    boto3_raw_data: "type_defs.CreateSegmentSnapshotRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    SegmentDefinitionName = field("SegmentDefinitionName")
    DataFormat = field("DataFormat")
    EncryptionKey = field("EncryptionKey")
    RoleArn = field("RoleArn")
    DestinationUri = field("DestinationUri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSegmentSnapshotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSegmentSnapshotRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectTypeField:
    boto3_raw_data: "type_defs.ObjectTypeFieldTypeDef" = dataclasses.field()

    Source = field("Source")
    Target = field("Target")
    ContentType = field("ContentType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ObjectTypeFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ObjectTypeFieldTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DateDimensionOutput:
    boto3_raw_data: "type_defs.DateDimensionOutputTypeDef" = dataclasses.field()

    DimensionType = field("DimensionType")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DateDimensionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DateDimensionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DateDimension:
    boto3_raw_data: "type_defs.DateDimensionTypeDef" = dataclasses.field()

    DimensionType = field("DimensionType")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DateDimensionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DateDimensionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCalculatedAttributeDefinitionRequest:
    boto3_raw_data: "type_defs.DeleteCalculatedAttributeDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    CalculatedAttributeName = field("CalculatedAttributeName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteCalculatedAttributeDefinitionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCalculatedAttributeDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainLayoutRequest:
    boto3_raw_data: "type_defs.DeleteDomainLayoutRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    LayoutDefinitionName = field("LayoutDefinitionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDomainLayoutRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainLayoutRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainRequest:
    boto3_raw_data: "type_defs.DeleteDomainRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventStreamRequest:
    boto3_raw_data: "type_defs.DeleteEventStreamRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    EventStreamName = field("EventStreamName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEventStreamRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventStreamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventTriggerRequest:
    boto3_raw_data: "type_defs.DeleteEventTriggerRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    EventTriggerName = field("EventTriggerName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEventTriggerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventTriggerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIntegrationRequest:
    boto3_raw_data: "type_defs.DeleteIntegrationRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    Uri = field("Uri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIntegrationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIntegrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProfileKeyRequest:
    boto3_raw_data: "type_defs.DeleteProfileKeyRequestTypeDef" = dataclasses.field()

    ProfileId = field("ProfileId")
    KeyName = field("KeyName")
    Values = field("Values")
    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProfileKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProfileKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProfileObjectRequest:
    boto3_raw_data: "type_defs.DeleteProfileObjectRequestTypeDef" = dataclasses.field()

    ProfileId = field("ProfileId")
    ProfileObjectUniqueKey = field("ProfileObjectUniqueKey")
    ObjectTypeName = field("ObjectTypeName")
    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProfileObjectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProfileObjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProfileObjectTypeRequest:
    boto3_raw_data: "type_defs.DeleteProfileObjectTypeRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    ObjectTypeName = field("ObjectTypeName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteProfileObjectTypeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProfileObjectTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProfileRequest:
    boto3_raw_data: "type_defs.DeleteProfileRequestTypeDef" = dataclasses.field()

    ProfileId = field("ProfileId")
    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSegmentDefinitionRequest:
    boto3_raw_data: "type_defs.DeleteSegmentDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    SegmentDefinitionName = field("SegmentDefinitionName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteSegmentDefinitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSegmentDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteWorkflowRequest:
    boto3_raw_data: "type_defs.DeleteWorkflowRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    WorkflowId = field("WorkflowId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteWorkflowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteWorkflowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationSummary:
    boto3_raw_data: "type_defs.DestinationSummaryTypeDef" = dataclasses.field()

    Uri = field("Uri")
    Status = field("Status")
    UnhealthySince = field("UnhealthySince")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DestinationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectProfileObjectTypeRequest:
    boto3_raw_data: "type_defs.DetectProfileObjectTypeRequestTypeDef" = (
        dataclasses.field()
    )

    Objects = field("Objects")
    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DetectProfileObjectTypeRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectProfileObjectTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectTypeKeyOutput:
    boto3_raw_data: "type_defs.ObjectTypeKeyOutputTypeDef" = dataclasses.field()

    StandardIdentifiers = field("StandardIdentifiers")
    FieldNames = field("FieldNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ObjectTypeKeyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectTypeKeyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainStats:
    boto3_raw_data: "type_defs.DomainStatsTypeDef" = dataclasses.field()

    ProfileCount = field("ProfileCount")
    MeteringProfileCount = field("MeteringProfileCount")
    ObjectCount = field("ObjectCount")
    TotalSize = field("TotalSize")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainStatsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainStatsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventStreamDestinationDetails:
    boto3_raw_data: "type_defs.EventStreamDestinationDetailsTypeDef" = (
        dataclasses.field()
    )

    Uri = field("Uri")
    Status = field("Status")
    UnhealthySince = field("UnhealthySince")
    Message = field("Message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EventStreamDestinationDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventStreamDestinationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectAttributeOutput:
    boto3_raw_data: "type_defs.ObjectAttributeOutputTypeDef" = dataclasses.field()

    ComparisonOperator = field("ComparisonOperator")
    Values = field("Values")
    Source = field("Source")
    FieldName = field("FieldName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ObjectAttributeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectAttributeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Period:
    boto3_raw_data: "type_defs.PeriodTypeDef" = dataclasses.field()

    Unit = field("Unit")
    Value = field("Value")
    MaxInvocationsPerProfile = field("MaxInvocationsPerProfile")
    Unlimited = field("Unlimited")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PeriodTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PeriodTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventTriggerSummaryItem:
    boto3_raw_data: "type_defs.EventTriggerSummaryItemTypeDef" = dataclasses.field()

    ObjectTypeName = field("ObjectTypeName")
    EventTriggerName = field("EventTriggerName")
    Description = field("Description")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventTriggerSummaryItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventTriggerSummaryItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ExportingConfig:
    boto3_raw_data: "type_defs.S3ExportingConfigTypeDef" = dataclasses.field()

    S3BucketName = field("S3BucketName")
    S3KeyName = field("S3KeyName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3ExportingConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ExportingConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3ExportingLocation:
    boto3_raw_data: "type_defs.S3ExportingLocationTypeDef" = dataclasses.field()

    S3BucketName = field("S3BucketName")
    S3KeyName = field("S3KeyName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3ExportingLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3ExportingLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtraLengthValueProfileDimensionOutput:
    boto3_raw_data: "type_defs.ExtraLengthValueProfileDimensionOutputTypeDef" = (
        dataclasses.field()
    )

    DimensionType = field("DimensionType")
    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExtraLengthValueProfileDimensionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExtraLengthValueProfileDimensionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtraLengthValueProfileDimension:
    boto3_raw_data: "type_defs.ExtraLengthValueProfileDimensionTypeDef" = (
        dataclasses.field()
    )

    DimensionType = field("DimensionType")
    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExtraLengthValueProfileDimensionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExtraLengthValueProfileDimensionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldSourceProfileIds:
    boto3_raw_data: "type_defs.FieldSourceProfileIdsTypeDef" = dataclasses.field()

    AccountNumber = field("AccountNumber")
    AdditionalInformation = field("AdditionalInformation")
    PartyType = field("PartyType")
    BusinessName = field("BusinessName")
    FirstName = field("FirstName")
    MiddleName = field("MiddleName")
    LastName = field("LastName")
    BirthDate = field("BirthDate")
    Gender = field("Gender")
    PhoneNumber = field("PhoneNumber")
    MobilePhoneNumber = field("MobilePhoneNumber")
    HomePhoneNumber = field("HomePhoneNumber")
    BusinessPhoneNumber = field("BusinessPhoneNumber")
    EmailAddress = field("EmailAddress")
    PersonalEmailAddress = field("PersonalEmailAddress")
    BusinessEmailAddress = field("BusinessEmailAddress")
    Address = field("Address")
    ShippingAddress = field("ShippingAddress")
    MailingAddress = field("MailingAddress")
    BillingAddress = field("BillingAddress")
    Attributes = field("Attributes")
    ProfileType = field("ProfileType")
    EngagementPreferences = field("EngagementPreferences")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FieldSourceProfileIdsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldSourceProfileIdsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterAttributeDimensionOutput:
    boto3_raw_data: "type_defs.FilterAttributeDimensionOutputTypeDef" = (
        dataclasses.field()
    )

    DimensionType = field("DimensionType")
    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FilterAttributeDimensionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FilterAttributeDimensionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterAttributeDimension:
    boto3_raw_data: "type_defs.FilterAttributeDimensionTypeDef" = dataclasses.field()

    DimensionType = field("DimensionType")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FilterAttributeDimensionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FilterAttributeDimensionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FoundByKeyValue:
    boto3_raw_data: "type_defs.FoundByKeyValueTypeDef" = dataclasses.field()

    KeyName = field("KeyName")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FoundByKeyValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FoundByKeyValueTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCalculatedAttributeDefinitionRequest:
    boto3_raw_data: "type_defs.GetCalculatedAttributeDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    CalculatedAttributeName = field("CalculatedAttributeName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCalculatedAttributeDefinitionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCalculatedAttributeDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCalculatedAttributeForProfileRequest:
    boto3_raw_data: "type_defs.GetCalculatedAttributeForProfileRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    ProfileId = field("ProfileId")
    CalculatedAttributeName = field("CalculatedAttributeName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCalculatedAttributeForProfileRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCalculatedAttributeForProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainLayoutRequest:
    boto3_raw_data: "type_defs.GetDomainLayoutRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    LayoutDefinitionName = field("LayoutDefinitionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDomainLayoutRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainLayoutRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainRequest:
    boto3_raw_data: "type_defs.GetDomainRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDomainRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventStreamRequest:
    boto3_raw_data: "type_defs.GetEventStreamRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    EventStreamName = field("EventStreamName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEventStreamRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventStreamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventTriggerRequest:
    boto3_raw_data: "type_defs.GetEventTriggerRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    EventTriggerName = field("EventTriggerName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEventTriggerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventTriggerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdentityResolutionJobRequest:
    boto3_raw_data: "type_defs.GetIdentityResolutionJobRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    JobId = field("JobId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetIdentityResolutionJobRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdentityResolutionJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobStats:
    boto3_raw_data: "type_defs.JobStatsTypeDef" = dataclasses.field()

    NumberOfProfilesReviewed = field("NumberOfProfilesReviewed")
    NumberOfMatchesFound = field("NumberOfMatchesFound")
    NumberOfMergesDone = field("NumberOfMergesDone")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobStatsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobStatsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIntegrationRequest:
    boto3_raw_data: "type_defs.GetIntegrationRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    Uri = field("Uri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIntegrationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIntegrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMatchesRequest:
    boto3_raw_data: "type_defs.GetMatchesRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetMatchesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMatchesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MatchItem:
    boto3_raw_data: "type_defs.MatchItemTypeDef" = dataclasses.field()

    MatchId = field("MatchId")
    ProfileIds = field("ProfileIds")
    ConfidenceScore = field("ConfidenceScore")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MatchItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MatchItemTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProfileObjectTypeRequest:
    boto3_raw_data: "type_defs.GetProfileObjectTypeRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    ObjectTypeName = field("ObjectTypeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetProfileObjectTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProfileObjectTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProfileObjectTypeTemplateRequest:
    boto3_raw_data: "type_defs.GetProfileObjectTypeTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    TemplateId = field("TemplateId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetProfileObjectTypeTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProfileObjectTypeTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSegmentDefinitionRequest:
    boto3_raw_data: "type_defs.GetSegmentDefinitionRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    SegmentDefinitionName = field("SegmentDefinitionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSegmentDefinitionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSegmentDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSegmentEstimateRequest:
    boto3_raw_data: "type_defs.GetSegmentEstimateRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    EstimateId = field("EstimateId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSegmentEstimateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSegmentEstimateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSegmentMembershipRequest:
    boto3_raw_data: "type_defs.GetSegmentMembershipRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    SegmentDefinitionName = field("SegmentDefinitionName")
    ProfileIds = field("ProfileIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSegmentMembershipRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSegmentMembershipRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileQueryFailures:
    boto3_raw_data: "type_defs.ProfileQueryFailuresTypeDef" = dataclasses.field()

    ProfileId = field("ProfileId")
    Message = field("Message")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProfileQueryFailuresTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProfileQueryFailuresTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSegmentSnapshotRequest:
    boto3_raw_data: "type_defs.GetSegmentSnapshotRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    SegmentDefinitionName = field("SegmentDefinitionName")
    SnapshotId = field("SnapshotId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSegmentSnapshotRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSegmentSnapshotRequestTypeDef"]
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
class GetSimilarProfilesRequest:
    boto3_raw_data: "type_defs.GetSimilarProfilesRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    MatchType = field("MatchType")
    SearchKey = field("SearchKey")
    SearchValue = field("SearchValue")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSimilarProfilesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSimilarProfilesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUploadJobPathRequest:
    boto3_raw_data: "type_defs.GetUploadJobPathRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    JobId = field("JobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUploadJobPathRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUploadJobPathRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUploadJobRequest:
    boto3_raw_data: "type_defs.GetUploadJobRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    JobId = field("JobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUploadJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUploadJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResultsSummary:
    boto3_raw_data: "type_defs.ResultsSummaryTypeDef" = dataclasses.field()

    UpdatedRecords = field("UpdatedRecords")
    CreatedRecords = field("CreatedRecords")
    FailedRecords = field("FailedRecords")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResultsSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResultsSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkflowRequest:
    boto3_raw_data: "type_defs.GetWorkflowRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    WorkflowId = field("WorkflowId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkflowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkflowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkflowStepsRequest:
    boto3_raw_data: "type_defs.GetWorkflowStepsRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    WorkflowId = field("WorkflowId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkflowStepsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkflowStepsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceSegment:
    boto3_raw_data: "type_defs.SourceSegmentTypeDef" = dataclasses.field()

    SegmentDefinitionName = field("SegmentDefinitionName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceSegmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceSegmentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IncrementalPullConfig:
    boto3_raw_data: "type_defs.IncrementalPullConfigTypeDef" = dataclasses.field()

    DatetimeTypeFieldName = field("DatetimeTypeFieldName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IncrementalPullConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IncrementalPullConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobSchedule:
    boto3_raw_data: "type_defs.JobScheduleTypeDef" = dataclasses.field()

    DayOfTheWeek = field("DayOfTheWeek")
    Time = field("Time")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobScheduleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobScheduleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LayoutItem:
    boto3_raw_data: "type_defs.LayoutItemTypeDef" = dataclasses.field()

    LayoutDefinitionName = field("LayoutDefinitionName")
    Description = field("Description")
    DisplayName = field("DisplayName")
    LayoutType = field("LayoutType")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    IsDefault = field("IsDefault")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LayoutItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LayoutItemTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountIntegrationsRequest:
    boto3_raw_data: "type_defs.ListAccountIntegrationsRequestTypeDef" = (
        dataclasses.field()
    )

    Uri = field("Uri")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    IncludeHidden = field("IncludeHidden")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAccountIntegrationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountIntegrationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIntegrationItem:
    boto3_raw_data: "type_defs.ListIntegrationItemTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    Uri = field("Uri")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    ObjectTypeName = field("ObjectTypeName")
    Tags = field("Tags")
    ObjectTypeNames = field("ObjectTypeNames")
    WorkflowId = field("WorkflowId")
    IsUnstructured = field("IsUnstructured")
    RoleArn = field("RoleArn")
    EventTriggerNames = field("EventTriggerNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIntegrationItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIntegrationItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCalculatedAttributeDefinitionItem:
    boto3_raw_data: "type_defs.ListCalculatedAttributeDefinitionItemTypeDef" = (
        dataclasses.field()
    )

    CalculatedAttributeName = field("CalculatedAttributeName")
    DisplayName = field("DisplayName")
    Description = field("Description")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    UseHistoricalData = field("UseHistoricalData")
    Status = field("Status")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCalculatedAttributeDefinitionItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCalculatedAttributeDefinitionItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCalculatedAttributeDefinitionsRequest:
    boto3_raw_data: "type_defs.ListCalculatedAttributeDefinitionsRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCalculatedAttributeDefinitionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCalculatedAttributeDefinitionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCalculatedAttributeForProfileItem:
    boto3_raw_data: "type_defs.ListCalculatedAttributeForProfileItemTypeDef" = (
        dataclasses.field()
    )

    CalculatedAttributeName = field("CalculatedAttributeName")
    DisplayName = field("DisplayName")
    IsDataPartial = field("IsDataPartial")
    Value = field("Value")
    LastObjectTimestamp = field("LastObjectTimestamp")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCalculatedAttributeForProfileItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCalculatedAttributeForProfileItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCalculatedAttributesForProfileRequest:
    boto3_raw_data: "type_defs.ListCalculatedAttributesForProfileRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    ProfileId = field("ProfileId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCalculatedAttributesForProfileRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCalculatedAttributesForProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainItem:
    boto3_raw_data: "type_defs.ListDomainItemTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListDomainItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListDomainItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainLayoutsRequest:
    boto3_raw_data: "type_defs.ListDomainLayoutsRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainLayoutsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainLayoutsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainsRequest:
    boto3_raw_data: "type_defs.ListDomainsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventStreamsRequest:
    boto3_raw_data: "type_defs.ListEventStreamsRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEventStreamsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventStreamsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventTriggersRequest:
    boto3_raw_data: "type_defs.ListEventTriggersRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEventTriggersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventTriggersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentityResolutionJobsRequest:
    boto3_raw_data: "type_defs.ListIdentityResolutionJobsRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListIdentityResolutionJobsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentityResolutionJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIntegrationsRequest:
    boto3_raw_data: "type_defs.ListIntegrationsRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    IncludeHidden = field("IncludeHidden")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIntegrationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIntegrationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectTypeAttributeItem:
    boto3_raw_data: "type_defs.ListObjectTypeAttributeItemTypeDef" = dataclasses.field()

    AttributeName = field("AttributeName")
    LastUpdatedAt = field("LastUpdatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListObjectTypeAttributeItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectTypeAttributeItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectTypeAttributesRequest:
    boto3_raw_data: "type_defs.ListObjectTypeAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    ObjectTypeName = field("ObjectTypeName")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListObjectTypeAttributesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectTypeAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfileObjectTypeItem:
    boto3_raw_data: "type_defs.ListProfileObjectTypeItemTypeDef" = dataclasses.field()

    ObjectTypeName = field("ObjectTypeName")
    Description = field("Description")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    MaxProfileObjectCount = field("MaxProfileObjectCount")
    MaxAvailableProfileObjectCount = field("MaxAvailableProfileObjectCount")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProfileObjectTypeItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfileObjectTypeItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfileObjectTypeTemplateItem:
    boto3_raw_data: "type_defs.ListProfileObjectTypeTemplateItemTypeDef" = (
        dataclasses.field()
    )

    TemplateId = field("TemplateId")
    SourceName = field("SourceName")
    SourceObject = field("SourceObject")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProfileObjectTypeTemplateItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfileObjectTypeTemplateItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfileObjectTypeTemplatesRequest:
    boto3_raw_data: "type_defs.ListProfileObjectTypeTemplatesRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProfileObjectTypeTemplatesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfileObjectTypeTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfileObjectTypesRequest:
    boto3_raw_data: "type_defs.ListProfileObjectTypesRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListProfileObjectTypesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfileObjectTypesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfileObjectsItem:
    boto3_raw_data: "type_defs.ListProfileObjectsItemTypeDef" = dataclasses.field()

    ObjectTypeName = field("ObjectTypeName")
    ProfileObjectUniqueKey = field("ProfileObjectUniqueKey")
    Object = field("Object")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProfileObjectsItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfileObjectsItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectFilter:
    boto3_raw_data: "type_defs.ObjectFilterTypeDef" = dataclasses.field()

    KeyName = field("KeyName")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ObjectFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ObjectFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRuleBasedMatchesRequest:
    boto3_raw_data: "type_defs.ListRuleBasedMatchesRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRuleBasedMatchesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRuleBasedMatchesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSegmentDefinitionsRequest:
    boto3_raw_data: "type_defs.ListSegmentDefinitionsRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSegmentDefinitionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSegmentDefinitionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentDefinitionItem:
    boto3_raw_data: "type_defs.SegmentDefinitionItemTypeDef" = dataclasses.field()

    SegmentDefinitionName = field("SegmentDefinitionName")
    DisplayName = field("DisplayName")
    Description = field("Description")
    SegmentDefinitionArn = field("SegmentDefinitionArn")
    CreatedAt = field("CreatedAt")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SegmentDefinitionItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SegmentDefinitionItemTypeDef"]
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
class ListUploadJobsRequest:
    boto3_raw_data: "type_defs.ListUploadJobsRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUploadJobsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUploadJobsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UploadJobItem:
    boto3_raw_data: "type_defs.UploadJobItemTypeDef" = dataclasses.field()

    JobId = field("JobId")
    DisplayName = field("DisplayName")
    Status = field("Status")
    StatusReason = field("StatusReason")
    CreatedAt = field("CreatedAt")
    CompletedAt = field("CompletedAt")
    DataExpiry = field("DataExpiry")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UploadJobItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UploadJobItemTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowsItem:
    boto3_raw_data: "type_defs.ListWorkflowsItemTypeDef" = dataclasses.field()

    WorkflowType = field("WorkflowType")
    WorkflowId = field("WorkflowId")
    Status = field("Status")
    StatusDescription = field("StatusDescription")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListWorkflowsItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowsItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MarketoSourceProperties:
    boto3_raw_data: "type_defs.MarketoSourcePropertiesTypeDef" = dataclasses.field()

    Object = field("Object")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MarketoSourcePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MarketoSourcePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MatchingRuleOutput:
    boto3_raw_data: "type_defs.MatchingRuleOutputTypeDef" = dataclasses.field()

    Rule = field("Rule")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MatchingRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MatchingRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MatchingRule:
    boto3_raw_data: "type_defs.MatchingRuleTypeDef" = dataclasses.field()

    Rule = field("Rule")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MatchingRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MatchingRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectAttribute:
    boto3_raw_data: "type_defs.ObjectAttributeTypeDef" = dataclasses.field()

    ComparisonOperator = field("ComparisonOperator")
    Values = field("Values")
    Source = field("Source")
    FieldName = field("FieldName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ObjectAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ObjectAttributeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectTypeKey:
    boto3_raw_data: "type_defs.ObjectTypeKeyTypeDef" = dataclasses.field()

    StandardIdentifiers = field("StandardIdentifiers")
    FieldNames = field("FieldNames")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ObjectTypeKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ObjectTypeKeyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileAttributeValuesRequest:
    boto3_raw_data: "type_defs.ProfileAttributeValuesRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    AttributeName = field("AttributeName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProfileAttributeValuesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProfileAttributeValuesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileTypeDimensionOutput:
    boto3_raw_data: "type_defs.ProfileTypeDimensionOutputTypeDef" = dataclasses.field()

    DimensionType = field("DimensionType")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProfileTypeDimensionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProfileTypeDimensionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileDimension:
    boto3_raw_data: "type_defs.ProfileDimensionTypeDef" = dataclasses.field()

    DimensionType = field("DimensionType")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProfileDimensionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProfileDimensionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileTypeDimension:
    boto3_raw_data: "type_defs.ProfileTypeDimensionTypeDef" = dataclasses.field()

    DimensionType = field("DimensionType")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProfileTypeDimensionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProfileTypeDimensionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutProfileObjectRequest:
    boto3_raw_data: "type_defs.PutProfileObjectRequestTypeDef" = dataclasses.field()

    ObjectTypeName = field("ObjectTypeName")
    Object = field("Object")
    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutProfileObjectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutProfileObjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValueRange:
    boto3_raw_data: "type_defs.ValueRangeTypeDef" = dataclasses.field()

    Start = field("Start")
    End = field("End")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ValueRangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ValueRangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3SourceProperties:
    boto3_raw_data: "type_defs.S3SourcePropertiesTypeDef" = dataclasses.field()

    BucketName = field("BucketName")
    BucketPrefix = field("BucketPrefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3SourcePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3SourcePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceSourceProperties:
    boto3_raw_data: "type_defs.SalesforceSourcePropertiesTypeDef" = dataclasses.field()

    Object = field("Object")
    EnableDynamicFieldUpdate = field("EnableDynamicFieldUpdate")
    IncludeDeletedRecords = field("IncludeDeletedRecords")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SalesforceSourcePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SalesforceSourcePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceNowSourceProperties:
    boto3_raw_data: "type_defs.ServiceNowSourcePropertiesTypeDef" = dataclasses.field()

    Object = field("Object")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceNowSourcePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceNowSourcePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ZendeskSourceProperties:
    boto3_raw_data: "type_defs.ZendeskSourcePropertiesTypeDef" = dataclasses.field()

    Object = field("Object")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ZendeskSourcePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ZendeskSourcePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartUploadJobRequest:
    boto3_raw_data: "type_defs.StartUploadJobRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    JobId = field("JobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartUploadJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartUploadJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopUploadJobRequest:
    boto3_raw_data: "type_defs.StopUploadJobRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    JobId = field("JobId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopUploadJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopUploadJobRequestTypeDef"]
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
class UpdateAddress:
    boto3_raw_data: "type_defs.UpdateAddressTypeDef" = dataclasses.field()

    Address1 = field("Address1")
    Address2 = field("Address2")
    Address3 = field("Address3")
    Address4 = field("Address4")
    City = field("City")
    County = field("County")
    State = field("State")
    Province = field("Province")
    Country = field("Country")
    PostalCode = field("PostalCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateAddressTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateAddressTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainLayoutRequest:
    boto3_raw_data: "type_defs.UpdateDomainLayoutRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    LayoutDefinitionName = field("LayoutDefinitionName")
    Description = field("Description")
    DisplayName = field("DisplayName")
    IsDefault = field("IsDefault")
    LayoutType = field("LayoutType")
    Layout = field("Layout")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDomainLayoutRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainLayoutRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddProfileKeyResponse:
    boto3_raw_data: "type_defs.AddProfileKeyResponseTypeDef" = dataclasses.field()

    KeyName = field("KeyName")
    Values = field("Values")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddProfileKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddProfileKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainLayoutResponse:
    boto3_raw_data: "type_defs.CreateDomainLayoutResponseTypeDef" = dataclasses.field()

    LayoutDefinitionName = field("LayoutDefinitionName")
    Description = field("Description")
    DisplayName = field("DisplayName")
    IsDefault = field("IsDefault")
    LayoutType = field("LayoutType")
    Layout = field("Layout")
    Version = field("Version")
    Tags = field("Tags")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDomainLayoutResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainLayoutResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventStreamResponse:
    boto3_raw_data: "type_defs.CreateEventStreamResponseTypeDef" = dataclasses.field()

    EventStreamArn = field("EventStreamArn")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEventStreamResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventStreamResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIntegrationWorkflowResponse:
    boto3_raw_data: "type_defs.CreateIntegrationWorkflowResponseTypeDef" = (
        dataclasses.field()
    )

    WorkflowId = field("WorkflowId")
    Message = field("Message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateIntegrationWorkflowResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIntegrationWorkflowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProfileResponse:
    boto3_raw_data: "type_defs.CreateProfileResponseTypeDef" = dataclasses.field()

    ProfileId = field("ProfileId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSegmentDefinitionResponse:
    boto3_raw_data: "type_defs.CreateSegmentDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    SegmentDefinitionName = field("SegmentDefinitionName")
    DisplayName = field("DisplayName")
    Description = field("Description")
    CreatedAt = field("CreatedAt")
    SegmentDefinitionArn = field("SegmentDefinitionArn")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSegmentDefinitionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSegmentDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSegmentEstimateResponse:
    boto3_raw_data: "type_defs.CreateSegmentEstimateResponseTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    EstimateId = field("EstimateId")
    StatusCode = field("StatusCode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSegmentEstimateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSegmentEstimateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSegmentSnapshotResponse:
    boto3_raw_data: "type_defs.CreateSegmentSnapshotResponseTypeDef" = (
        dataclasses.field()
    )

    SnapshotId = field("SnapshotId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSegmentSnapshotResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSegmentSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUploadJobResponse:
    boto3_raw_data: "type_defs.CreateUploadJobResponseTypeDef" = dataclasses.field()

    JobId = field("JobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUploadJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUploadJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainLayoutResponse:
    boto3_raw_data: "type_defs.DeleteDomainLayoutResponseTypeDef" = dataclasses.field()

    Message = field("Message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDomainLayoutResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainLayoutResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainResponse:
    boto3_raw_data: "type_defs.DeleteDomainResponseTypeDef" = dataclasses.field()

    Message = field("Message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDomainResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEventTriggerResponse:
    boto3_raw_data: "type_defs.DeleteEventTriggerResponseTypeDef" = dataclasses.field()

    Message = field("Message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEventTriggerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEventTriggerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIntegrationResponse:
    boto3_raw_data: "type_defs.DeleteIntegrationResponseTypeDef" = dataclasses.field()

    Message = field("Message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIntegrationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIntegrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProfileKeyResponse:
    boto3_raw_data: "type_defs.DeleteProfileKeyResponseTypeDef" = dataclasses.field()

    Message = field("Message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProfileKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProfileKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProfileObjectResponse:
    boto3_raw_data: "type_defs.DeleteProfileObjectResponseTypeDef" = dataclasses.field()

    Message = field("Message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProfileObjectResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProfileObjectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProfileObjectTypeResponse:
    boto3_raw_data: "type_defs.DeleteProfileObjectTypeResponseTypeDef" = (
        dataclasses.field()
    )

    Message = field("Message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteProfileObjectTypeResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProfileObjectTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProfileResponse:
    boto3_raw_data: "type_defs.DeleteProfileResponseTypeDef" = dataclasses.field()

    Message = field("Message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSegmentDefinitionResponse:
    boto3_raw_data: "type_defs.DeleteSegmentDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    Message = field("Message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteSegmentDefinitionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSegmentDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutoMergingPreviewResponse:
    boto3_raw_data: "type_defs.GetAutoMergingPreviewResponseTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    NumberOfMatchesInSample = field("NumberOfMatchesInSample")
    NumberOfProfilesInSample = field("NumberOfProfilesInSample")
    NumberOfProfilesWillBeMerged = field("NumberOfProfilesWillBeMerged")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAutoMergingPreviewResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAutoMergingPreviewResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCalculatedAttributeForProfileResponse:
    boto3_raw_data: "type_defs.GetCalculatedAttributeForProfileResponseTypeDef" = (
        dataclasses.field()
    )

    CalculatedAttributeName = field("CalculatedAttributeName")
    DisplayName = field("DisplayName")
    IsDataPartial = field("IsDataPartial")
    Value = field("Value")
    LastObjectTimestamp = field("LastObjectTimestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCalculatedAttributeForProfileResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCalculatedAttributeForProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainLayoutResponse:
    boto3_raw_data: "type_defs.GetDomainLayoutResponseTypeDef" = dataclasses.field()

    LayoutDefinitionName = field("LayoutDefinitionName")
    Description = field("Description")
    DisplayName = field("DisplayName")
    IsDefault = field("IsDefault")
    LayoutType = field("LayoutType")
    Layout = field("Layout")
    Version = field("Version")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDomainLayoutResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainLayoutResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIntegrationResponse:
    boto3_raw_data: "type_defs.GetIntegrationResponseTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    Uri = field("Uri")
    ObjectTypeName = field("ObjectTypeName")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    Tags = field("Tags")
    ObjectTypeNames = field("ObjectTypeNames")
    WorkflowId = field("WorkflowId")
    IsUnstructured = field("IsUnstructured")
    RoleArn = field("RoleArn")
    EventTriggerNames = field("EventTriggerNames")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIntegrationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIntegrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSegmentEstimateResponse:
    boto3_raw_data: "type_defs.GetSegmentEstimateResponseTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    EstimateId = field("EstimateId")
    Status = field("Status")
    Estimate = field("Estimate")
    Message = field("Message")
    StatusCode = field("StatusCode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSegmentEstimateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSegmentEstimateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSegmentSnapshotResponse:
    boto3_raw_data: "type_defs.GetSegmentSnapshotResponseTypeDef" = dataclasses.field()

    SnapshotId = field("SnapshotId")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    DataFormat = field("DataFormat")
    EncryptionKey = field("EncryptionKey")
    RoleArn = field("RoleArn")
    DestinationUri = field("DestinationUri")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSegmentSnapshotResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSegmentSnapshotResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSimilarProfilesResponse:
    boto3_raw_data: "type_defs.GetSimilarProfilesResponseTypeDef" = dataclasses.field()

    ProfileIds = field("ProfileIds")
    MatchId = field("MatchId")
    MatchType = field("MatchType")
    RuleLevel = field("RuleLevel")
    ConfidenceScore = field("ConfidenceScore")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSimilarProfilesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSimilarProfilesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUploadJobPathResponse:
    boto3_raw_data: "type_defs.GetUploadJobPathResponseTypeDef" = dataclasses.field()

    Url = field("Url")
    ClientToken = field("ClientToken")
    ValidUntil = field("ValidUntil")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUploadJobPathResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUploadJobPathResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRuleBasedMatchesResponse:
    boto3_raw_data: "type_defs.ListRuleBasedMatchesResponseTypeDef" = (
        dataclasses.field()
    )

    MatchIds = field("MatchIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRuleBasedMatchesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRuleBasedMatchesResponseTypeDef"]
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
class MergeProfilesResponse:
    boto3_raw_data: "type_defs.MergeProfilesResponseTypeDef" = dataclasses.field()

    Message = field("Message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MergeProfilesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MergeProfilesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutIntegrationResponse:
    boto3_raw_data: "type_defs.PutIntegrationResponseTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    Uri = field("Uri")
    ObjectTypeName = field("ObjectTypeName")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    Tags = field("Tags")
    ObjectTypeNames = field("ObjectTypeNames")
    WorkflowId = field("WorkflowId")
    IsUnstructured = field("IsUnstructured")
    RoleArn = field("RoleArn")
    EventTriggerNames = field("EventTriggerNames")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutIntegrationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutIntegrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutProfileObjectResponse:
    boto3_raw_data: "type_defs.PutProfileObjectResponseTypeDef" = dataclasses.field()

    ProfileObjectUniqueKey = field("ProfileObjectUniqueKey")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutProfileObjectResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutProfileObjectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainLayoutResponse:
    boto3_raw_data: "type_defs.UpdateDomainLayoutResponseTypeDef" = dataclasses.field()

    LayoutDefinitionName = field("LayoutDefinitionName")
    Description = field("Description")
    DisplayName = field("DisplayName")
    IsDefault = field("IsDefault")
    LayoutType = field("LayoutType")
    Layout = field("Layout")
    Version = field("Version")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDomainLayoutResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainLayoutResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProfileResponse:
    boto3_raw_data: "type_defs.UpdateProfileResponseTypeDef" = dataclasses.field()

    ProfileId = field("ProfileId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchProfilesRequest:
    boto3_raw_data: "type_defs.SearchProfilesRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    KeyName = field("KeyName")
    Values = field("Values")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def AdditionalSearchKeys(self):  # pragma: no cover
        return AdditionalSearchKey.make_many(
            self.boto3_raw_data["AdditionalSearchKeys"]
        )

    LogicalOperator = field("LogicalOperator")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchProfilesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchProfilesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddressDimensionOutput:
    boto3_raw_data: "type_defs.AddressDimensionOutputTypeDef" = dataclasses.field()

    @cached_property
    def City(self):  # pragma: no cover
        return ProfileDimensionOutput.make_one(self.boto3_raw_data["City"])

    @cached_property
    def Country(self):  # pragma: no cover
        return ProfileDimensionOutput.make_one(self.boto3_raw_data["Country"])

    @cached_property
    def County(self):  # pragma: no cover
        return ProfileDimensionOutput.make_one(self.boto3_raw_data["County"])

    @cached_property
    def PostalCode(self):  # pragma: no cover
        return ProfileDimensionOutput.make_one(self.boto3_raw_data["PostalCode"])

    @cached_property
    def Province(self):  # pragma: no cover
        return ProfileDimensionOutput.make_one(self.boto3_raw_data["Province"])

    @cached_property
    def State(self):  # pragma: no cover
        return ProfileDimensionOutput.make_one(self.boto3_raw_data["State"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddressDimensionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddressDimensionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowAttributes:
    boto3_raw_data: "type_defs.WorkflowAttributesTypeDef" = dataclasses.field()

    @cached_property
    def AppflowIntegration(self):  # pragma: no cover
        return AppflowIntegrationWorkflowAttributes.make_one(
            self.boto3_raw_data["AppflowIntegration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkflowAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowMetrics:
    boto3_raw_data: "type_defs.WorkflowMetricsTypeDef" = dataclasses.field()

    @cached_property
    def AppflowIntegration(self):  # pragma: no cover
        return AppflowIntegrationWorkflowMetrics.make_one(
            self.boto3_raw_data["AppflowIntegration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkflowMetricsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WorkflowMetricsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkflowStepItem:
    boto3_raw_data: "type_defs.WorkflowStepItemTypeDef" = dataclasses.field()

    @cached_property
    def AppflowIntegration(self):  # pragma: no cover
        return AppflowIntegrationWorkflowStep.make_one(
            self.boto3_raw_data["AppflowIntegration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WorkflowStepItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkflowStepItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeDetailsOutput:
    boto3_raw_data: "type_defs.AttributeDetailsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Attributes(self):  # pragma: no cover
        return AttributeItem.make_many(self.boto3_raw_data["Attributes"])

    Expression = field("Expression")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeDetailsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeDetailsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeDetails:
    boto3_raw_data: "type_defs.AttributeDetailsTypeDef" = dataclasses.field()

    @cached_property
    def Attributes(self):  # pragma: no cover
        return AttributeItem.make_many(self.boto3_raw_data["Attributes"])

    Expression = field("Expression")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributeDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileAttributeValuesResponse:
    boto3_raw_data: "type_defs.ProfileAttributeValuesResponseTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    AttributeName = field("AttributeName")

    @cached_property
    def Items(self):  # pragma: no cover
        return AttributeValueItem.make_many(self.boto3_raw_data["Items"])

    StatusCode = field("StatusCode")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProfileAttributeValuesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProfileAttributeValuesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoMergingOutput:
    boto3_raw_data: "type_defs.AutoMergingOutputTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @cached_property
    def Consolidation(self):  # pragma: no cover
        return ConsolidationOutput.make_one(self.boto3_raw_data["Consolidation"])

    @cached_property
    def ConflictResolution(self):  # pragma: no cover
        return ConflictResolution.make_one(self.boto3_raw_data["ConflictResolution"])

    MinAllowedConfidenceScoreForMerging = field("MinAllowedConfidenceScoreForMerging")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutoMergingOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoMergingOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Batch:
    boto3_raw_data: "type_defs.BatchTypeDef" = dataclasses.field()

    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BatchTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowsRequest:
    boto3_raw_data: "type_defs.ListWorkflowsRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    WorkflowType = field("WorkflowType")
    Status = field("Status")
    QueryStartDate = field("QueryStartDate")
    QueryEndDate = field("QueryEndDate")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkflowsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduledTriggerProperties:
    boto3_raw_data: "type_defs.ScheduledTriggerPropertiesTypeDef" = dataclasses.field()

    ScheduleExpression = field("ScheduleExpression")
    DataPullMode = field("DataPullMode")
    ScheduleStartTime = field("ScheduleStartTime")
    ScheduleEndTime = field("ScheduleEndTime")
    Timezone = field("Timezone")
    ScheduleOffset = field("ScheduleOffset")
    FirstExecutionFrom = field("FirstExecutionFrom")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduledTriggerPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduledTriggerPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConditionOverrides:
    boto3_raw_data: "type_defs.ConditionOverridesTypeDef" = dataclasses.field()

    @cached_property
    def Range(self):  # pragma: no cover
        return RangeOverride.make_one(self.boto3_raw_data["Range"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConditionOverridesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConditionOverridesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Task:
    boto3_raw_data: "type_defs.TaskTypeDef" = dataclasses.field()

    SourceFields = field("SourceFields")
    TaskType = field("TaskType")

    @cached_property
    def ConnectorOperator(self):  # pragma: no cover
        return ConnectorOperator.make_one(self.boto3_raw_data["ConnectorOperator"])

    DestinationField = field("DestinationField")
    TaskProperties = field("TaskProperties")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaskTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TaskTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EngagementPreferencesOutput:
    boto3_raw_data: "type_defs.EngagementPreferencesOutputTypeDef" = dataclasses.field()

    @cached_property
    def Phone(self):  # pragma: no cover
        return ContactPreference.make_many(self.boto3_raw_data["Phone"])

    @cached_property
    def Email(self):  # pragma: no cover
        return ContactPreference.make_many(self.boto3_raw_data["Email"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EngagementPreferencesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EngagementPreferencesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EngagementPreferences:
    boto3_raw_data: "type_defs.EngagementPreferencesTypeDef" = dataclasses.field()

    @cached_property
    def Phone(self):  # pragma: no cover
        return ContactPreference.make_many(self.boto3_raw_data["Phone"])

    @cached_property
    def Email(self):  # pragma: no cover
        return ContactPreference.make_many(self.boto3_raw_data["Email"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EngagementPreferencesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EngagementPreferencesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateUploadJobRequest:
    boto3_raw_data: "type_defs.CreateUploadJobRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    DisplayName = field("DisplayName")
    Fields = field("Fields")
    UniqueKey = field("UniqueKey")
    DataExpiry = field("DataExpiry")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateUploadJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateUploadJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventStreamSummary:
    boto3_raw_data: "type_defs.EventStreamSummaryTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    EventStreamName = field("EventStreamName")
    EventStreamArn = field("EventStreamArn")
    State = field("State")
    StoppedSince = field("StoppedSince")

    @cached_property
    def DestinationSummary(self):  # pragma: no cover
        return DestinationSummary.make_one(self.boto3_raw_data["DestinationSummary"])

    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventStreamSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventStreamSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectedProfileObjectType:
    boto3_raw_data: "type_defs.DetectedProfileObjectTypeTypeDef" = dataclasses.field()

    SourceLastUpdatedTimestampFormat = field("SourceLastUpdatedTimestampFormat")
    Fields = field("Fields")
    Keys = field("Keys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectedProfileObjectTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectedProfileObjectTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProfileObjectTypeResponse:
    boto3_raw_data: "type_defs.GetProfileObjectTypeResponseTypeDef" = (
        dataclasses.field()
    )

    ObjectTypeName = field("ObjectTypeName")
    Description = field("Description")
    TemplateId = field("TemplateId")
    ExpirationDays = field("ExpirationDays")
    EncryptionKey = field("EncryptionKey")
    AllowProfileCreation = field("AllowProfileCreation")
    SourceLastUpdatedTimestampFormat = field("SourceLastUpdatedTimestampFormat")
    MaxAvailableProfileObjectCount = field("MaxAvailableProfileObjectCount")
    MaxProfileObjectCount = field("MaxProfileObjectCount")
    Fields = field("Fields")
    Keys = field("Keys")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetProfileObjectTypeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProfileObjectTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProfileObjectTypeTemplateResponse:
    boto3_raw_data: "type_defs.GetProfileObjectTypeTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    TemplateId = field("TemplateId")
    SourceName = field("SourceName")
    SourceObject = field("SourceObject")
    AllowProfileCreation = field("AllowProfileCreation")
    SourceLastUpdatedTimestampFormat = field("SourceLastUpdatedTimestampFormat")
    Fields = field("Fields")
    Keys = field("Keys")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetProfileObjectTypeTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProfileObjectTypeTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutProfileObjectTypeResponse:
    boto3_raw_data: "type_defs.PutProfileObjectTypeResponseTypeDef" = (
        dataclasses.field()
    )

    ObjectTypeName = field("ObjectTypeName")
    Description = field("Description")
    TemplateId = field("TemplateId")
    ExpirationDays = field("ExpirationDays")
    EncryptionKey = field("EncryptionKey")
    AllowProfileCreation = field("AllowProfileCreation")
    SourceLastUpdatedTimestampFormat = field("SourceLastUpdatedTimestampFormat")
    MaxProfileObjectCount = field("MaxProfileObjectCount")
    MaxAvailableProfileObjectCount = field("MaxAvailableProfileObjectCount")
    Fields = field("Fields")
    Keys = field("Keys")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutProfileObjectTypeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutProfileObjectTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventStreamResponse:
    boto3_raw_data: "type_defs.GetEventStreamResponseTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    EventStreamArn = field("EventStreamArn")
    CreatedAt = field("CreatedAt")
    State = field("State")
    StoppedSince = field("StoppedSince")

    @cached_property
    def DestinationDetails(self):  # pragma: no cover
        return EventStreamDestinationDetails.make_one(
            self.boto3_raw_data["DestinationDetails"]
        )

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEventStreamResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventStreamResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventTriggerDimensionOutput:
    boto3_raw_data: "type_defs.EventTriggerDimensionOutputTypeDef" = dataclasses.field()

    @cached_property
    def ObjectAttributes(self):  # pragma: no cover
        return ObjectAttributeOutput.make_many(self.boto3_raw_data["ObjectAttributes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventTriggerDimensionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventTriggerDimensionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventTriggerLimitsOutput:
    boto3_raw_data: "type_defs.EventTriggerLimitsOutputTypeDef" = dataclasses.field()

    EventExpiration = field("EventExpiration")

    @cached_property
    def Periods(self):  # pragma: no cover
        return Period.make_many(self.boto3_raw_data["Periods"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventTriggerLimitsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventTriggerLimitsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventTriggerLimits:
    boto3_raw_data: "type_defs.EventTriggerLimitsTypeDef" = dataclasses.field()

    EventExpiration = field("EventExpiration")

    @cached_property
    def Periods(self):  # pragma: no cover
        return Period.make_many(self.boto3_raw_data["Periods"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventTriggerLimitsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventTriggerLimitsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventTriggersResponse:
    boto3_raw_data: "type_defs.ListEventTriggersResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return EventTriggerSummaryItem.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEventTriggersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventTriggersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportingConfig:
    boto3_raw_data: "type_defs.ExportingConfigTypeDef" = dataclasses.field()

    @cached_property
    def S3Exporting(self):  # pragma: no cover
        return S3ExportingConfig.make_one(self.boto3_raw_data["S3Exporting"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportingConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExportingConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportingLocation:
    boto3_raw_data: "type_defs.ExportingLocationTypeDef" = dataclasses.field()

    @cached_property
    def S3Exporting(self):  # pragma: no cover
        return S3ExportingLocation.make_one(self.boto3_raw_data["S3Exporting"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportingLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportingLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MergeProfilesRequest:
    boto3_raw_data: "type_defs.MergeProfilesRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    MainProfileId = field("MainProfileId")
    ProfileIdsToBeMerged = field("ProfileIdsToBeMerged")

    @cached_property
    def FieldSourceProfileIds(self):  # pragma: no cover
        return FieldSourceProfileIds.make_one(
            self.boto3_raw_data["FieldSourceProfileIds"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MergeProfilesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MergeProfilesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterDimensionOutput:
    boto3_raw_data: "type_defs.FilterDimensionOutputTypeDef" = dataclasses.field()

    Attributes = field("Attributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FilterDimensionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FilterDimensionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterDimension:
    boto3_raw_data: "type_defs.FilterDimensionTypeDef" = dataclasses.field()

    Attributes = field("Attributes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterDimensionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterDimensionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMatchesResponse:
    boto3_raw_data: "type_defs.GetMatchesResponseTypeDef" = dataclasses.field()

    MatchGenerationDate = field("MatchGenerationDate")
    PotentialMatches = field("PotentialMatches")

    @cached_property
    def Matches(self):  # pragma: no cover
        return MatchItem.make_many(self.boto3_raw_data["Matches"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMatchesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMatchesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSimilarProfilesRequestPaginate:
    boto3_raw_data: "type_defs.GetSimilarProfilesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    MatchType = field("MatchType")
    SearchKey = field("SearchKey")
    SearchValue = field("SearchValue")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetSimilarProfilesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSimilarProfilesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainLayoutsRequestPaginate:
    boto3_raw_data: "type_defs.ListDomainLayoutsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDomainLayoutsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainLayoutsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventStreamsRequestPaginate:
    boto3_raw_data: "type_defs.ListEventStreamsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEventStreamsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventStreamsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventTriggersRequestPaginate:
    boto3_raw_data: "type_defs.ListEventTriggersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEventTriggersRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventTriggersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectTypeAttributesRequestPaginate:
    boto3_raw_data: "type_defs.ListObjectTypeAttributesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    ObjectTypeName = field("ObjectTypeName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListObjectTypeAttributesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectTypeAttributesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRuleBasedMatchesRequestPaginate:
    boto3_raw_data: "type_defs.ListRuleBasedMatchesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRuleBasedMatchesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRuleBasedMatchesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSegmentDefinitionsRequestPaginate:
    boto3_raw_data: "type_defs.ListSegmentDefinitionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSegmentDefinitionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSegmentDefinitionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUploadJobsRequestPaginate:
    boto3_raw_data: "type_defs.ListUploadJobsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListUploadJobsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUploadJobsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetUploadJobResponse:
    boto3_raw_data: "type_defs.GetUploadJobResponseTypeDef" = dataclasses.field()

    JobId = field("JobId")
    DisplayName = field("DisplayName")
    Status = field("Status")
    StatusReason = field("StatusReason")
    CreatedAt = field("CreatedAt")
    CompletedAt = field("CompletedAt")
    Fields = field("Fields")
    UniqueKey = field("UniqueKey")

    @cached_property
    def ResultsSummary(self):  # pragma: no cover
        return ResultsSummary.make_one(self.boto3_raw_data["ResultsSummary"])

    DataExpiry = field("DataExpiry")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetUploadJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetUploadJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainLayoutsResponse:
    boto3_raw_data: "type_defs.ListDomainLayoutsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return LayoutItem.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainLayoutsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainLayoutsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccountIntegrationsResponse:
    boto3_raw_data: "type_defs.ListAccountIntegrationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Items(self):  # pragma: no cover
        return ListIntegrationItem.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAccountIntegrationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccountIntegrationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIntegrationsResponse:
    boto3_raw_data: "type_defs.ListIntegrationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return ListIntegrationItem.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIntegrationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIntegrationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCalculatedAttributeDefinitionsResponse:
    boto3_raw_data: "type_defs.ListCalculatedAttributeDefinitionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Items(self):  # pragma: no cover
        return ListCalculatedAttributeDefinitionItem.make_many(
            self.boto3_raw_data["Items"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCalculatedAttributeDefinitionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCalculatedAttributeDefinitionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCalculatedAttributesForProfileResponse:
    boto3_raw_data: "type_defs.ListCalculatedAttributesForProfileResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Items(self):  # pragma: no cover
        return ListCalculatedAttributeForProfileItem.make_many(
            self.boto3_raw_data["Items"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCalculatedAttributesForProfileResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCalculatedAttributesForProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainsResponse:
    boto3_raw_data: "type_defs.ListDomainsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return ListDomainItem.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectTypeAttributesResponse:
    boto3_raw_data: "type_defs.ListObjectTypeAttributesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Items(self):  # pragma: no cover
        return ListObjectTypeAttributeItem.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListObjectTypeAttributesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectTypeAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfileObjectTypesResponse:
    boto3_raw_data: "type_defs.ListProfileObjectTypesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Items(self):  # pragma: no cover
        return ListProfileObjectTypeItem.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListProfileObjectTypesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfileObjectTypesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfileObjectTypeTemplatesResponse:
    boto3_raw_data: "type_defs.ListProfileObjectTypeTemplatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Items(self):  # pragma: no cover
        return ListProfileObjectTypeTemplateItem.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProfileObjectTypeTemplatesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfileObjectTypeTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfileObjectsResponse:
    boto3_raw_data: "type_defs.ListProfileObjectsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return ListProfileObjectsItem.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProfileObjectsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfileObjectsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfileObjectsRequest:
    boto3_raw_data: "type_defs.ListProfileObjectsRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    ObjectTypeName = field("ObjectTypeName")
    ProfileId = field("ProfileId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def ObjectFilter(self):  # pragma: no cover
        return ObjectFilter.make_one(self.boto3_raw_data["ObjectFilter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProfileObjectsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfileObjectsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSegmentDefinitionsResponse:
    boto3_raw_data: "type_defs.ListSegmentDefinitionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Items(self):  # pragma: no cover
        return SegmentDefinitionItem.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListSegmentDefinitionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSegmentDefinitionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUploadJobsResponse:
    boto3_raw_data: "type_defs.ListUploadJobsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return UploadJobItem.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUploadJobsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUploadJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListWorkflowsResponse:
    boto3_raw_data: "type_defs.ListWorkflowsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return ListWorkflowsItem.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListWorkflowsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListWorkflowsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Range:
    boto3_raw_data: "type_defs.RangeTypeDef" = dataclasses.field()

    Value = field("Value")
    Unit = field("Unit")

    @cached_property
    def ValueRange(self):  # pragma: no cover
        return ValueRange.make_one(self.boto3_raw_data["ValueRange"])

    TimestampSource = field("TimestampSource")
    TimestampFormat = field("TimestampFormat")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceConnectorProperties:
    boto3_raw_data: "type_defs.SourceConnectorPropertiesTypeDef" = dataclasses.field()

    @cached_property
    def Marketo(self):  # pragma: no cover
        return MarketoSourceProperties.make_one(self.boto3_raw_data["Marketo"])

    @cached_property
    def S3(self):  # pragma: no cover
        return S3SourceProperties.make_one(self.boto3_raw_data["S3"])

    @cached_property
    def Salesforce(self):  # pragma: no cover
        return SalesforceSourceProperties.make_one(self.boto3_raw_data["Salesforce"])

    @cached_property
    def ServiceNow(self):  # pragma: no cover
        return ServiceNowSourceProperties.make_one(self.boto3_raw_data["ServiceNow"])

    @cached_property
    def Zendesk(self):  # pragma: no cover
        return ZendeskSourceProperties.make_one(self.boto3_raw_data["Zendesk"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceConnectorPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceConnectorPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileAttributesOutput:
    boto3_raw_data: "type_defs.ProfileAttributesOutputTypeDef" = dataclasses.field()

    @cached_property
    def AccountNumber(self):  # pragma: no cover
        return ProfileDimensionOutput.make_one(self.boto3_raw_data["AccountNumber"])

    @cached_property
    def AdditionalInformation(self):  # pragma: no cover
        return ExtraLengthValueProfileDimensionOutput.make_one(
            self.boto3_raw_data["AdditionalInformation"]
        )

    @cached_property
    def FirstName(self):  # pragma: no cover
        return ProfileDimensionOutput.make_one(self.boto3_raw_data["FirstName"])

    @cached_property
    def LastName(self):  # pragma: no cover
        return ProfileDimensionOutput.make_one(self.boto3_raw_data["LastName"])

    @cached_property
    def MiddleName(self):  # pragma: no cover
        return ProfileDimensionOutput.make_one(self.boto3_raw_data["MiddleName"])

    @cached_property
    def GenderString(self):  # pragma: no cover
        return ProfileDimensionOutput.make_one(self.boto3_raw_data["GenderString"])

    @cached_property
    def PartyTypeString(self):  # pragma: no cover
        return ProfileDimensionOutput.make_one(self.boto3_raw_data["PartyTypeString"])

    @cached_property
    def BirthDate(self):  # pragma: no cover
        return DateDimensionOutput.make_one(self.boto3_raw_data["BirthDate"])

    @cached_property
    def PhoneNumber(self):  # pragma: no cover
        return ProfileDimensionOutput.make_one(self.boto3_raw_data["PhoneNumber"])

    @cached_property
    def BusinessName(self):  # pragma: no cover
        return ProfileDimensionOutput.make_one(self.boto3_raw_data["BusinessName"])

    @cached_property
    def BusinessPhoneNumber(self):  # pragma: no cover
        return ProfileDimensionOutput.make_one(
            self.boto3_raw_data["BusinessPhoneNumber"]
        )

    @cached_property
    def HomePhoneNumber(self):  # pragma: no cover
        return ProfileDimensionOutput.make_one(self.boto3_raw_data["HomePhoneNumber"])

    @cached_property
    def MobilePhoneNumber(self):  # pragma: no cover
        return ProfileDimensionOutput.make_one(self.boto3_raw_data["MobilePhoneNumber"])

    @cached_property
    def EmailAddress(self):  # pragma: no cover
        return ProfileDimensionOutput.make_one(self.boto3_raw_data["EmailAddress"])

    @cached_property
    def PersonalEmailAddress(self):  # pragma: no cover
        return ProfileDimensionOutput.make_one(
            self.boto3_raw_data["PersonalEmailAddress"]
        )

    @cached_property
    def BusinessEmailAddress(self):  # pragma: no cover
        return ProfileDimensionOutput.make_one(
            self.boto3_raw_data["BusinessEmailAddress"]
        )

    @cached_property
    def Address(self):  # pragma: no cover
        return AddressDimensionOutput.make_one(self.boto3_raw_data["Address"])

    @cached_property
    def ShippingAddress(self):  # pragma: no cover
        return AddressDimensionOutput.make_one(self.boto3_raw_data["ShippingAddress"])

    @cached_property
    def MailingAddress(self):  # pragma: no cover
        return AddressDimensionOutput.make_one(self.boto3_raw_data["MailingAddress"])

    @cached_property
    def BillingAddress(self):  # pragma: no cover
        return AddressDimensionOutput.make_one(self.boto3_raw_data["BillingAddress"])

    Attributes = field("Attributes")

    @cached_property
    def ProfileType(self):  # pragma: no cover
        return ProfileTypeDimensionOutput.make_one(self.boto3_raw_data["ProfileType"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProfileAttributesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProfileAttributesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkflowResponse:
    boto3_raw_data: "type_defs.GetWorkflowResponseTypeDef" = dataclasses.field()

    WorkflowId = field("WorkflowId")
    WorkflowType = field("WorkflowType")
    Status = field("Status")
    ErrorDescription = field("ErrorDescription")
    StartDate = field("StartDate")
    LastUpdatedAt = field("LastUpdatedAt")

    @cached_property
    def Attributes(self):  # pragma: no cover
        return WorkflowAttributes.make_one(self.boto3_raw_data["Attributes"])

    @cached_property
    def Metrics(self):  # pragma: no cover
        return WorkflowMetrics.make_one(self.boto3_raw_data["Metrics"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkflowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkflowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetWorkflowStepsResponse:
    boto3_raw_data: "type_defs.GetWorkflowStepsResponseTypeDef" = dataclasses.field()

    WorkflowId = field("WorkflowId")
    WorkflowType = field("WorkflowType")

    @cached_property
    def Items(self):  # pragma: no cover
        return WorkflowStepItem.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetWorkflowStepsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetWorkflowStepsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TriggerProperties:
    boto3_raw_data: "type_defs.TriggerPropertiesTypeDef" = dataclasses.field()

    @cached_property
    def Scheduled(self):  # pragma: no cover
        return ScheduledTriggerProperties.make_one(self.boto3_raw_data["Scheduled"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TriggerPropertiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TriggerPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetCalculatedAttributeForProfileRequest:
    boto3_raw_data: "type_defs.BatchGetCalculatedAttributeForProfileRequestTypeDef" = (
        dataclasses.field()
    )

    CalculatedAttributeName = field("CalculatedAttributeName")
    DomainName = field("DomainName")
    ProfileIds = field("ProfileIds")

    @cached_property
    def ConditionOverrides(self):  # pragma: no cover
        return ConditionOverrides.make_one(self.boto3_raw_data["ConditionOverrides"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetCalculatedAttributeForProfileRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetCalculatedAttributeForProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetCalculatedAttributeForProfileResponse:
    boto3_raw_data: "type_defs.BatchGetCalculatedAttributeForProfileResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Errors(self):  # pragma: no cover
        return BatchGetCalculatedAttributeForProfileError.make_many(
            self.boto3_raw_data["Errors"]
        )

    @cached_property
    def CalculatedAttributeValues(self):  # pragma: no cover
        return CalculatedAttributeValue.make_many(
            self.boto3_raw_data["CalculatedAttributeValues"]
        )

    @cached_property
    def ConditionOverrides(self):  # pragma: no cover
        return ConditionOverrides.make_one(self.boto3_raw_data["ConditionOverrides"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetCalculatedAttributeForProfileResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetCalculatedAttributeForProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CalculatedAttributeDimensionOutput:
    boto3_raw_data: "type_defs.CalculatedAttributeDimensionOutputTypeDef" = (
        dataclasses.field()
    )

    DimensionType = field("DimensionType")
    Values = field("Values")

    @cached_property
    def ConditionOverrides(self):  # pragma: no cover
        return ConditionOverrides.make_one(self.boto3_raw_data["ConditionOverrides"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CalculatedAttributeDimensionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CalculatedAttributeDimensionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CalculatedAttributeDimension:
    boto3_raw_data: "type_defs.CalculatedAttributeDimensionTypeDef" = (
        dataclasses.field()
    )

    DimensionType = field("DimensionType")
    Values = field("Values")

    @cached_property
    def ConditionOverrides(self):  # pragma: no cover
        return ConditionOverrides.make_one(self.boto3_raw_data["ConditionOverrides"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CalculatedAttributeDimensionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CalculatedAttributeDimensionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoMerging:
    boto3_raw_data: "type_defs.AutoMergingTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    Consolidation = field("Consolidation")

    @cached_property
    def ConflictResolution(self):  # pragma: no cover
        return ConflictResolution.make_one(self.boto3_raw_data["ConflictResolution"])

    MinAllowedConfidenceScoreForMerging = field("MinAllowedConfidenceScoreForMerging")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutoMergingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AutoMergingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAutoMergingPreviewRequest:
    boto3_raw_data: "type_defs.GetAutoMergingPreviewRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    Consolidation = field("Consolidation")

    @cached_property
    def ConflictResolution(self):  # pragma: no cover
        return ConflictResolution.make_one(self.boto3_raw_data["ConflictResolution"])

    MinAllowedConfidenceScoreForMerging = field("MinAllowedConfidenceScoreForMerging")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAutoMergingPreviewRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAutoMergingPreviewRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Profile:
    boto3_raw_data: "type_defs.ProfileTypeDef" = dataclasses.field()

    ProfileId = field("ProfileId")
    AccountNumber = field("AccountNumber")
    AdditionalInformation = field("AdditionalInformation")
    PartyType = field("PartyType")
    BusinessName = field("BusinessName")
    FirstName = field("FirstName")
    MiddleName = field("MiddleName")
    LastName = field("LastName")
    BirthDate = field("BirthDate")
    Gender = field("Gender")
    PhoneNumber = field("PhoneNumber")
    MobilePhoneNumber = field("MobilePhoneNumber")
    HomePhoneNumber = field("HomePhoneNumber")
    BusinessPhoneNumber = field("BusinessPhoneNumber")
    EmailAddress = field("EmailAddress")
    PersonalEmailAddress = field("PersonalEmailAddress")
    BusinessEmailAddress = field("BusinessEmailAddress")

    @cached_property
    def Address(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["Address"])

    @cached_property
    def ShippingAddress(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["ShippingAddress"])

    @cached_property
    def MailingAddress(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["MailingAddress"])

    @cached_property
    def BillingAddress(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["BillingAddress"])

    Attributes = field("Attributes")

    @cached_property
    def FoundByItems(self):  # pragma: no cover
        return FoundByKeyValue.make_many(self.boto3_raw_data["FoundByItems"])

    PartyTypeString = field("PartyTypeString")
    GenderString = field("GenderString")
    ProfileType = field("ProfileType")

    @cached_property
    def EngagementPreferences(self):  # pragma: no cover
        return EngagementPreferencesOutput.make_one(
            self.boto3_raw_data["EngagementPreferences"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProfileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProfileTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEventStreamsResponse:
    boto3_raw_data: "type_defs.ListEventStreamsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return EventStreamSummary.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEventStreamsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEventStreamsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectProfileObjectTypeResponse:
    boto3_raw_data: "type_defs.DetectProfileObjectTypeResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DetectedProfileObjectTypes(self):  # pragma: no cover
        return DetectedProfileObjectType.make_many(
            self.boto3_raw_data["DetectedProfileObjectTypes"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DetectProfileObjectTypeResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectProfileObjectTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventTriggerConditionOutput:
    boto3_raw_data: "type_defs.EventTriggerConditionOutputTypeDef" = dataclasses.field()

    @cached_property
    def EventTriggerDimensions(self):  # pragma: no cover
        return EventTriggerDimensionOutput.make_many(
            self.boto3_raw_data["EventTriggerDimensions"]
        )

    LogicalOperator = field("LogicalOperator")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventTriggerConditionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventTriggerConditionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MatchingResponse:
    boto3_raw_data: "type_defs.MatchingResponseTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @cached_property
    def JobSchedule(self):  # pragma: no cover
        return JobSchedule.make_one(self.boto3_raw_data["JobSchedule"])

    @cached_property
    def AutoMerging(self):  # pragma: no cover
        return AutoMergingOutput.make_one(self.boto3_raw_data["AutoMerging"])

    @cached_property
    def ExportingConfig(self):  # pragma: no cover
        return ExportingConfig.make_one(self.boto3_raw_data["ExportingConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MatchingResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MatchingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleBasedMatchingResponse:
    boto3_raw_data: "type_defs.RuleBasedMatchingResponseTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @cached_property
    def MatchingRules(self):  # pragma: no cover
        return MatchingRuleOutput.make_many(self.boto3_raw_data["MatchingRules"])

    Status = field("Status")
    MaxAllowedRuleLevelForMerging = field("MaxAllowedRuleLevelForMerging")
    MaxAllowedRuleLevelForMatching = field("MaxAllowedRuleLevelForMatching")

    @cached_property
    def AttributeTypesSelector(self):  # pragma: no cover
        return AttributeTypesSelectorOutput.make_one(
            self.boto3_raw_data["AttributeTypesSelector"]
        )

    @cached_property
    def ConflictResolution(self):  # pragma: no cover
        return ConflictResolution.make_one(self.boto3_raw_data["ConflictResolution"])

    @cached_property
    def ExportingConfig(self):  # pragma: no cover
        return ExportingConfig.make_one(self.boto3_raw_data["ExportingConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleBasedMatchingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleBasedMatchingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdentityResolutionJobResponse:
    boto3_raw_data: "type_defs.GetIdentityResolutionJobResponseTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    JobId = field("JobId")
    Status = field("Status")
    Message = field("Message")
    JobStartTime = field("JobStartTime")
    JobEndTime = field("JobEndTime")
    LastUpdatedAt = field("LastUpdatedAt")
    JobExpirationTime = field("JobExpirationTime")

    @cached_property
    def AutoMerging(self):  # pragma: no cover
        return AutoMergingOutput.make_one(self.boto3_raw_data["AutoMerging"])

    @cached_property
    def ExportingLocation(self):  # pragma: no cover
        return ExportingLocation.make_one(self.boto3_raw_data["ExportingLocation"])

    @cached_property
    def JobStats(self):  # pragma: no cover
        return JobStats.make_one(self.boto3_raw_data["JobStats"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetIdentityResolutionJobResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdentityResolutionJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityResolutionJob:
    boto3_raw_data: "type_defs.IdentityResolutionJobTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    JobId = field("JobId")
    Status = field("Status")
    JobStartTime = field("JobStartTime")
    JobEndTime = field("JobEndTime")

    @cached_property
    def JobStats(self):  # pragma: no cover
        return JobStats.make_one(self.boto3_raw_data["JobStats"])

    @cached_property
    def ExportingLocation(self):  # pragma: no cover
        return ExportingLocation.make_one(self.boto3_raw_data["ExportingLocation"])

    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentityResolutionJobTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityResolutionJobTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterGroupOutput:
    boto3_raw_data: "type_defs.FilterGroupOutputTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return FilterDimensionOutput.make_many(self.boto3_raw_data["Dimensions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterGroupOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FilterGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterGroup:
    boto3_raw_data: "type_defs.FilterGroupTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return FilterDimension.make_many(self.boto3_raw_data["Dimensions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterGroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleBasedMatchingRequest:
    boto3_raw_data: "type_defs.RuleBasedMatchingRequestTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    MatchingRules = field("MatchingRules")
    MaxAllowedRuleLevelForMerging = field("MaxAllowedRuleLevelForMerging")
    MaxAllowedRuleLevelForMatching = field("MaxAllowedRuleLevelForMatching")
    AttributeTypesSelector = field("AttributeTypesSelector")

    @cached_property
    def ConflictResolution(self):  # pragma: no cover
        return ConflictResolution.make_one(self.boto3_raw_data["ConflictResolution"])

    @cached_property
    def ExportingConfig(self):  # pragma: no cover
        return ExportingConfig.make_one(self.boto3_raw_data["ExportingConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleBasedMatchingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleBasedMatchingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventTriggerDimension:
    boto3_raw_data: "type_defs.EventTriggerDimensionTypeDef" = dataclasses.field()

    ObjectAttributes = field("ObjectAttributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventTriggerDimensionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventTriggerDimensionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutProfileObjectTypeRequest:
    boto3_raw_data: "type_defs.PutProfileObjectTypeRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    ObjectTypeName = field("ObjectTypeName")
    Description = field("Description")
    TemplateId = field("TemplateId")
    ExpirationDays = field("ExpirationDays")
    EncryptionKey = field("EncryptionKey")
    AllowProfileCreation = field("AllowProfileCreation")
    SourceLastUpdatedTimestampFormat = field("SourceLastUpdatedTimestampFormat")
    MaxProfileObjectCount = field("MaxProfileObjectCount")
    Fields = field("Fields")
    Keys = field("Keys")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutProfileObjectTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutProfileObjectTypeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddressDimension:
    boto3_raw_data: "type_defs.AddressDimensionTypeDef" = dataclasses.field()

    City = field("City")
    Country = field("Country")
    County = field("County")
    PostalCode = field("PostalCode")
    Province = field("Province")
    State = field("State")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddressDimensionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddressDimensionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Conditions:
    boto3_raw_data: "type_defs.ConditionsTypeDef" = dataclasses.field()

    @cached_property
    def Range(self):  # pragma: no cover
        return Range.make_one(self.boto3_raw_data["Range"])

    ObjectCount = field("ObjectCount")

    @cached_property
    def Threshold(self):  # pragma: no cover
        return Threshold.make_one(self.boto3_raw_data["Threshold"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConditionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConditionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceFlowConfig:
    boto3_raw_data: "type_defs.SourceFlowConfigTypeDef" = dataclasses.field()

    ConnectorType = field("ConnectorType")

    @cached_property
    def SourceConnectorProperties(self):  # pragma: no cover
        return SourceConnectorProperties.make_one(
            self.boto3_raw_data["SourceConnectorProperties"]
        )

    ConnectorProfileName = field("ConnectorProfileName")

    @cached_property
    def IncrementalPullConfig(self):  # pragma: no cover
        return IncrementalPullConfig.make_one(
            self.boto3_raw_data["IncrementalPullConfig"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceFlowConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceFlowConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TriggerConfig:
    boto3_raw_data: "type_defs.TriggerConfigTypeDef" = dataclasses.field()

    TriggerType = field("TriggerType")

    @cached_property
    def TriggerProperties(self):  # pragma: no cover
        return TriggerProperties.make_one(self.boto3_raw_data["TriggerProperties"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TriggerConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TriggerConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DimensionOutput:
    boto3_raw_data: "type_defs.DimensionOutputTypeDef" = dataclasses.field()

    @cached_property
    def ProfileAttributes(self):  # pragma: no cover
        return ProfileAttributesOutput.make_one(
            self.boto3_raw_data["ProfileAttributes"]
        )

    CalculatedAttributes = field("CalculatedAttributes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DimensionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DimensionOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetProfileResponse:
    boto3_raw_data: "type_defs.BatchGetProfileResponseTypeDef" = dataclasses.field()

    @cached_property
    def Errors(self):  # pragma: no cover
        return BatchGetProfileError.make_many(self.boto3_raw_data["Errors"])

    @cached_property
    def Profiles(self):  # pragma: no cover
        return Profile.make_many(self.boto3_raw_data["Profiles"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileQueryResult:
    boto3_raw_data: "type_defs.ProfileQueryResultTypeDef" = dataclasses.field()

    ProfileId = field("ProfileId")
    QueryResult = field("QueryResult")

    @cached_property
    def Profile(self):  # pragma: no cover
        return Profile.make_one(self.boto3_raw_data["Profile"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProfileQueryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProfileQueryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchProfilesResponse:
    boto3_raw_data: "type_defs.SearchProfilesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return Profile.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchProfilesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchProfilesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProfileRequest:
    boto3_raw_data: "type_defs.CreateProfileRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    AccountNumber = field("AccountNumber")
    AdditionalInformation = field("AdditionalInformation")
    PartyType = field("PartyType")
    BusinessName = field("BusinessName")
    FirstName = field("FirstName")
    MiddleName = field("MiddleName")
    LastName = field("LastName")
    BirthDate = field("BirthDate")
    Gender = field("Gender")
    PhoneNumber = field("PhoneNumber")
    MobilePhoneNumber = field("MobilePhoneNumber")
    HomePhoneNumber = field("HomePhoneNumber")
    BusinessPhoneNumber = field("BusinessPhoneNumber")
    EmailAddress = field("EmailAddress")
    PersonalEmailAddress = field("PersonalEmailAddress")
    BusinessEmailAddress = field("BusinessEmailAddress")

    @cached_property
    def Address(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["Address"])

    @cached_property
    def ShippingAddress(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["ShippingAddress"])

    @cached_property
    def MailingAddress(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["MailingAddress"])

    @cached_property
    def BillingAddress(self):  # pragma: no cover
        return Address.make_one(self.boto3_raw_data["BillingAddress"])

    Attributes = field("Attributes")
    PartyTypeString = field("PartyTypeString")
    GenderString = field("GenderString")
    ProfileType = field("ProfileType")
    EngagementPreferences = field("EngagementPreferences")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProfileRequest:
    boto3_raw_data: "type_defs.UpdateProfileRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    ProfileId = field("ProfileId")
    AdditionalInformation = field("AdditionalInformation")
    AccountNumber = field("AccountNumber")
    PartyType = field("PartyType")
    BusinessName = field("BusinessName")
    FirstName = field("FirstName")
    MiddleName = field("MiddleName")
    LastName = field("LastName")
    BirthDate = field("BirthDate")
    Gender = field("Gender")
    PhoneNumber = field("PhoneNumber")
    MobilePhoneNumber = field("MobilePhoneNumber")
    HomePhoneNumber = field("HomePhoneNumber")
    BusinessPhoneNumber = field("BusinessPhoneNumber")
    EmailAddress = field("EmailAddress")
    PersonalEmailAddress = field("PersonalEmailAddress")
    BusinessEmailAddress = field("BusinessEmailAddress")

    @cached_property
    def Address(self):  # pragma: no cover
        return UpdateAddress.make_one(self.boto3_raw_data["Address"])

    @cached_property
    def ShippingAddress(self):  # pragma: no cover
        return UpdateAddress.make_one(self.boto3_raw_data["ShippingAddress"])

    @cached_property
    def MailingAddress(self):  # pragma: no cover
        return UpdateAddress.make_one(self.boto3_raw_data["MailingAddress"])

    @cached_property
    def BillingAddress(self):  # pragma: no cover
        return UpdateAddress.make_one(self.boto3_raw_data["BillingAddress"])

    Attributes = field("Attributes")
    PartyTypeString = field("PartyTypeString")
    GenderString = field("GenderString")
    ProfileType = field("ProfileType")
    EngagementPreferences = field("EngagementPreferences")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventTriggerResponse:
    boto3_raw_data: "type_defs.CreateEventTriggerResponseTypeDef" = dataclasses.field()

    EventTriggerName = field("EventTriggerName")
    ObjectTypeName = field("ObjectTypeName")
    Description = field("Description")

    @cached_property
    def EventTriggerConditions(self):  # pragma: no cover
        return EventTriggerConditionOutput.make_many(
            self.boto3_raw_data["EventTriggerConditions"]
        )

    SegmentFilter = field("SegmentFilter")

    @cached_property
    def EventTriggerLimits(self):  # pragma: no cover
        return EventTriggerLimitsOutput.make_one(
            self.boto3_raw_data["EventTriggerLimits"]
        )

    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEventTriggerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventTriggerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEventTriggerResponse:
    boto3_raw_data: "type_defs.GetEventTriggerResponseTypeDef" = dataclasses.field()

    EventTriggerName = field("EventTriggerName")
    ObjectTypeName = field("ObjectTypeName")
    Description = field("Description")

    @cached_property
    def EventTriggerConditions(self):  # pragma: no cover
        return EventTriggerConditionOutput.make_many(
            self.boto3_raw_data["EventTriggerConditions"]
        )

    SegmentFilter = field("SegmentFilter")

    @cached_property
    def EventTriggerLimits(self):  # pragma: no cover
        return EventTriggerLimitsOutput.make_one(
            self.boto3_raw_data["EventTriggerLimits"]
        )

    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEventTriggerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEventTriggerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEventTriggerResponse:
    boto3_raw_data: "type_defs.UpdateEventTriggerResponseTypeDef" = dataclasses.field()

    EventTriggerName = field("EventTriggerName")
    ObjectTypeName = field("ObjectTypeName")
    Description = field("Description")

    @cached_property
    def EventTriggerConditions(self):  # pragma: no cover
        return EventTriggerConditionOutput.make_many(
            self.boto3_raw_data["EventTriggerConditions"]
        )

    SegmentFilter = field("SegmentFilter")

    @cached_property
    def EventTriggerLimits(self):  # pragma: no cover
        return EventTriggerLimitsOutput.make_one(
            self.boto3_raw_data["EventTriggerLimits"]
        )

    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEventTriggerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEventTriggerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainResponse:
    boto3_raw_data: "type_defs.CreateDomainResponseTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    DefaultExpirationDays = field("DefaultExpirationDays")
    DefaultEncryptionKey = field("DefaultEncryptionKey")
    DeadLetterQueueUrl = field("DeadLetterQueueUrl")

    @cached_property
    def Matching(self):  # pragma: no cover
        return MatchingResponse.make_one(self.boto3_raw_data["Matching"])

    @cached_property
    def RuleBasedMatching(self):  # pragma: no cover
        return RuleBasedMatchingResponse.make_one(
            self.boto3_raw_data["RuleBasedMatching"]
        )

    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDomainResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainResponse:
    boto3_raw_data: "type_defs.GetDomainResponseTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    DefaultExpirationDays = field("DefaultExpirationDays")
    DefaultEncryptionKey = field("DefaultEncryptionKey")
    DeadLetterQueueUrl = field("DeadLetterQueueUrl")

    @cached_property
    def Stats(self):  # pragma: no cover
        return DomainStats.make_one(self.boto3_raw_data["Stats"])

    @cached_property
    def Matching(self):  # pragma: no cover
        return MatchingResponse.make_one(self.boto3_raw_data["Matching"])

    @cached_property
    def RuleBasedMatching(self):  # pragma: no cover
        return RuleBasedMatchingResponse.make_one(
            self.boto3_raw_data["RuleBasedMatching"]
        )

    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDomainResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainResponse:
    boto3_raw_data: "type_defs.UpdateDomainResponseTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    DefaultExpirationDays = field("DefaultExpirationDays")
    DefaultEncryptionKey = field("DefaultEncryptionKey")
    DeadLetterQueueUrl = field("DeadLetterQueueUrl")

    @cached_property
    def Matching(self):  # pragma: no cover
        return MatchingResponse.make_one(self.boto3_raw_data["Matching"])

    @cached_property
    def RuleBasedMatching(self):  # pragma: no cover
        return RuleBasedMatchingResponse.make_one(
            self.boto3_raw_data["RuleBasedMatching"]
        )

    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDomainResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentityResolutionJobsResponse:
    boto3_raw_data: "type_defs.ListIdentityResolutionJobsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def IdentityResolutionJobsList(self):  # pragma: no cover
        return IdentityResolutionJob.make_many(
            self.boto3_raw_data["IdentityResolutionJobsList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListIdentityResolutionJobsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentityResolutionJobsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterOutput:
    boto3_raw_data: "type_defs.FilterOutputTypeDef" = dataclasses.field()

    Include = field("Include")

    @cached_property
    def Groups(self):  # pragma: no cover
        return FilterGroupOutput.make_many(self.boto3_raw_data["Groups"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Filter:
    boto3_raw_data: "type_defs.FilterTypeDef" = dataclasses.field()

    Include = field("Include")

    @cached_property
    def Groups(self):  # pragma: no cover
        return FilterGroup.make_many(self.boto3_raw_data["Groups"])

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
class UpdateCalculatedAttributeDefinitionRequest:
    boto3_raw_data: "type_defs.UpdateCalculatedAttributeDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    CalculatedAttributeName = field("CalculatedAttributeName")
    DisplayName = field("DisplayName")
    Description = field("Description")

    @cached_property
    def Conditions(self):  # pragma: no cover
        return Conditions.make_one(self.boto3_raw_data["Conditions"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCalculatedAttributeDefinitionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCalculatedAttributeDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCalculatedAttributeDefinitionResponse:
    boto3_raw_data: "type_defs.UpdateCalculatedAttributeDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    CalculatedAttributeName = field("CalculatedAttributeName")
    DisplayName = field("DisplayName")
    Description = field("Description")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    Statistic = field("Statistic")

    @cached_property
    def Conditions(self):  # pragma: no cover
        return Conditions.make_one(self.boto3_raw_data["Conditions"])

    @cached_property
    def AttributeDetails(self):  # pragma: no cover
        return AttributeDetailsOutput.make_one(self.boto3_raw_data["AttributeDetails"])

    UseHistoricalData = field("UseHistoricalData")
    Status = field("Status")

    @cached_property
    def Readiness(self):  # pragma: no cover
        return Readiness.make_one(self.boto3_raw_data["Readiness"])

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateCalculatedAttributeDefinitionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCalculatedAttributeDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlowDefinition:
    boto3_raw_data: "type_defs.FlowDefinitionTypeDef" = dataclasses.field()

    FlowName = field("FlowName")
    KmsArn = field("KmsArn")

    @cached_property
    def SourceFlowConfig(self):  # pragma: no cover
        return SourceFlowConfig.make_one(self.boto3_raw_data["SourceFlowConfig"])

    @cached_property
    def Tasks(self):  # pragma: no cover
        return Task.make_many(self.boto3_raw_data["Tasks"])

    @cached_property
    def TriggerConfig(self):  # pragma: no cover
        return TriggerConfig.make_one(self.boto3_raw_data["TriggerConfig"])

    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FlowDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FlowDefinitionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GroupOutput:
    boto3_raw_data: "type_defs.GroupOutputTypeDef" = dataclasses.field()

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return DimensionOutput.make_many(self.boto3_raw_data["Dimensions"])

    @cached_property
    def SourceSegments(self):  # pragma: no cover
        return SourceSegment.make_many(self.boto3_raw_data["SourceSegments"])

    SourceType = field("SourceType")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MatchingRequest:
    boto3_raw_data: "type_defs.MatchingRequestTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @cached_property
    def JobSchedule(self):  # pragma: no cover
        return JobSchedule.make_one(self.boto3_raw_data["JobSchedule"])

    AutoMerging = field("AutoMerging")

    @cached_property
    def ExportingConfig(self):  # pragma: no cover
        return ExportingConfig.make_one(self.boto3_raw_data["ExportingConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MatchingRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MatchingRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSegmentMembershipResponse:
    boto3_raw_data: "type_defs.GetSegmentMembershipResponseTypeDef" = (
        dataclasses.field()
    )

    SegmentDefinitionName = field("SegmentDefinitionName")

    @cached_property
    def Profiles(self):  # pragma: no cover
        return ProfileQueryResult.make_many(self.boto3_raw_data["Profiles"])

    @cached_property
    def Failures(self):  # pragma: no cover
        return ProfileQueryFailures.make_many(self.boto3_raw_data["Failures"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSegmentMembershipResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSegmentMembershipResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCalculatedAttributeDefinitionResponse:
    boto3_raw_data: "type_defs.CreateCalculatedAttributeDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    CalculatedAttributeName = field("CalculatedAttributeName")
    DisplayName = field("DisplayName")
    Description = field("Description")

    @cached_property
    def AttributeDetails(self):  # pragma: no cover
        return AttributeDetailsOutput.make_one(self.boto3_raw_data["AttributeDetails"])

    @cached_property
    def Conditions(self):  # pragma: no cover
        return Conditions.make_one(self.boto3_raw_data["Conditions"])

    @cached_property
    def Filter(self):  # pragma: no cover
        return FilterOutput.make_one(self.boto3_raw_data["Filter"])

    Statistic = field("Statistic")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    UseHistoricalData = field("UseHistoricalData")
    Status = field("Status")

    @cached_property
    def Readiness(self):  # pragma: no cover
        return Readiness.make_one(self.boto3_raw_data["Readiness"])

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCalculatedAttributeDefinitionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCalculatedAttributeDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCalculatedAttributeDefinitionResponse:
    boto3_raw_data: "type_defs.GetCalculatedAttributeDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    CalculatedAttributeName = field("CalculatedAttributeName")
    DisplayName = field("DisplayName")
    Description = field("Description")
    CreatedAt = field("CreatedAt")
    LastUpdatedAt = field("LastUpdatedAt")
    Statistic = field("Statistic")

    @cached_property
    def Filter(self):  # pragma: no cover
        return FilterOutput.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def Conditions(self):  # pragma: no cover
        return Conditions.make_one(self.boto3_raw_data["Conditions"])

    @cached_property
    def AttributeDetails(self):  # pragma: no cover
        return AttributeDetailsOutput.make_one(self.boto3_raw_data["AttributeDetails"])

    UseHistoricalData = field("UseHistoricalData")
    Status = field("Status")

    @cached_property
    def Readiness(self):  # pragma: no cover
        return Readiness.make_one(self.boto3_raw_data["Readiness"])

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCalculatedAttributeDefinitionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCalculatedAttributeDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventTriggerCondition:
    boto3_raw_data: "type_defs.EventTriggerConditionTypeDef" = dataclasses.field()

    EventTriggerDimensions = field("EventTriggerDimensions")
    LogicalOperator = field("LogicalOperator")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventTriggerConditionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventTriggerConditionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileAttributes:
    boto3_raw_data: "type_defs.ProfileAttributesTypeDef" = dataclasses.field()

    AccountNumber = field("AccountNumber")
    AdditionalInformation = field("AdditionalInformation")
    FirstName = field("FirstName")
    LastName = field("LastName")
    MiddleName = field("MiddleName")
    GenderString = field("GenderString")
    PartyTypeString = field("PartyTypeString")
    BirthDate = field("BirthDate")
    PhoneNumber = field("PhoneNumber")
    BusinessName = field("BusinessName")
    BusinessPhoneNumber = field("BusinessPhoneNumber")
    HomePhoneNumber = field("HomePhoneNumber")
    MobilePhoneNumber = field("MobilePhoneNumber")
    EmailAddress = field("EmailAddress")
    PersonalEmailAddress = field("PersonalEmailAddress")
    BusinessEmailAddress = field("BusinessEmailAddress")
    Address = field("Address")
    ShippingAddress = field("ShippingAddress")
    MailingAddress = field("MailingAddress")
    BillingAddress = field("BillingAddress")
    Attributes = field("Attributes")
    ProfileType = field("ProfileType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProfileAttributesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProfileAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppflowIntegration:
    boto3_raw_data: "type_defs.AppflowIntegrationTypeDef" = dataclasses.field()

    @cached_property
    def FlowDefinition(self):  # pragma: no cover
        return FlowDefinition.make_one(self.boto3_raw_data["FlowDefinition"])

    @cached_property
    def Batches(self):  # pragma: no cover
        return Batch.make_many(self.boto3_raw_data["Batches"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AppflowIntegrationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppflowIntegrationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutIntegrationRequest:
    boto3_raw_data: "type_defs.PutIntegrationRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    Uri = field("Uri")
    ObjectTypeName = field("ObjectTypeName")
    Tags = field("Tags")

    @cached_property
    def FlowDefinition(self):  # pragma: no cover
        return FlowDefinition.make_one(self.boto3_raw_data["FlowDefinition"])

    ObjectTypeNames = field("ObjectTypeNames")
    RoleArn = field("RoleArn")
    EventTriggerNames = field("EventTriggerNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutIntegrationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutIntegrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentGroupOutput:
    boto3_raw_data: "type_defs.SegmentGroupOutputTypeDef" = dataclasses.field()

    @cached_property
    def Groups(self):  # pragma: no cover
        return GroupOutput.make_many(self.boto3_raw_data["Groups"])

    Include = field("Include")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SegmentGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SegmentGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainRequest:
    boto3_raw_data: "type_defs.CreateDomainRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    DefaultExpirationDays = field("DefaultExpirationDays")
    DefaultEncryptionKey = field("DefaultEncryptionKey")
    DeadLetterQueueUrl = field("DeadLetterQueueUrl")

    @cached_property
    def Matching(self):  # pragma: no cover
        return MatchingRequest.make_one(self.boto3_raw_data["Matching"])

    @cached_property
    def RuleBasedMatching(self):  # pragma: no cover
        return RuleBasedMatchingRequest.make_one(
            self.boto3_raw_data["RuleBasedMatching"]
        )

    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainRequest:
    boto3_raw_data: "type_defs.UpdateDomainRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    DefaultExpirationDays = field("DefaultExpirationDays")
    DefaultEncryptionKey = field("DefaultEncryptionKey")
    DeadLetterQueueUrl = field("DeadLetterQueueUrl")

    @cached_property
    def Matching(self):  # pragma: no cover
        return MatchingRequest.make_one(self.boto3_raw_data["Matching"])

    @cached_property
    def RuleBasedMatching(self):  # pragma: no cover
        return RuleBasedMatchingRequest.make_one(
            self.boto3_raw_data["RuleBasedMatching"]
        )

    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCalculatedAttributeDefinitionRequest:
    boto3_raw_data: "type_defs.CreateCalculatedAttributeDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    CalculatedAttributeName = field("CalculatedAttributeName")
    AttributeDetails = field("AttributeDetails")
    Statistic = field("Statistic")
    DisplayName = field("DisplayName")
    Description = field("Description")

    @cached_property
    def Conditions(self):  # pragma: no cover
        return Conditions.make_one(self.boto3_raw_data["Conditions"])

    Filter = field("Filter")
    UseHistoricalData = field("UseHistoricalData")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCalculatedAttributeDefinitionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCalculatedAttributeDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntegrationConfig:
    boto3_raw_data: "type_defs.IntegrationConfigTypeDef" = dataclasses.field()

    @cached_property
    def AppflowIntegration(self):  # pragma: no cover
        return AppflowIntegration.make_one(self.boto3_raw_data["AppflowIntegration"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IntegrationConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntegrationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSegmentDefinitionResponse:
    boto3_raw_data: "type_defs.GetSegmentDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    SegmentDefinitionName = field("SegmentDefinitionName")
    DisplayName = field("DisplayName")
    Description = field("Description")

    @cached_property
    def SegmentGroups(self):  # pragma: no cover
        return SegmentGroupOutput.make_one(self.boto3_raw_data["SegmentGroups"])

    SegmentDefinitionArn = field("SegmentDefinitionArn")
    CreatedAt = field("CreatedAt")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSegmentDefinitionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSegmentDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEventTriggerRequest:
    boto3_raw_data: "type_defs.CreateEventTriggerRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    EventTriggerName = field("EventTriggerName")
    ObjectTypeName = field("ObjectTypeName")
    EventTriggerConditions = field("EventTriggerConditions")
    Description = field("Description")
    SegmentFilter = field("SegmentFilter")
    EventTriggerLimits = field("EventTriggerLimits")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEventTriggerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEventTriggerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEventTriggerRequest:
    boto3_raw_data: "type_defs.UpdateEventTriggerRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    EventTriggerName = field("EventTriggerName")
    ObjectTypeName = field("ObjectTypeName")
    Description = field("Description")
    EventTriggerConditions = field("EventTriggerConditions")
    SegmentFilter = field("SegmentFilter")
    EventTriggerLimits = field("EventTriggerLimits")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEventTriggerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEventTriggerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Dimension:
    boto3_raw_data: "type_defs.DimensionTypeDef" = dataclasses.field()

    ProfileAttributes = field("ProfileAttributes")
    CalculatedAttributes = field("CalculatedAttributes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DimensionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DimensionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIntegrationWorkflowRequest:
    boto3_raw_data: "type_defs.CreateIntegrationWorkflowRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    WorkflowType = field("WorkflowType")

    @cached_property
    def IntegrationConfig(self):  # pragma: no cover
        return IntegrationConfig.make_one(self.boto3_raw_data["IntegrationConfig"])

    ObjectTypeName = field("ObjectTypeName")
    RoleArn = field("RoleArn")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateIntegrationWorkflowRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIntegrationWorkflowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Group:
    boto3_raw_data: "type_defs.GroupTypeDef" = dataclasses.field()

    Dimensions = field("Dimensions")

    @cached_property
    def SourceSegments(self):  # pragma: no cover
        return SourceSegment.make_many(self.boto3_raw_data["SourceSegments"])

    SourceType = field("SourceType")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentGroup:
    boto3_raw_data: "type_defs.SegmentGroupTypeDef" = dataclasses.field()

    @cached_property
    def Groups(self):  # pragma: no cover
        return Group.make_many(self.boto3_raw_data["Groups"])

    Include = field("Include")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SegmentGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SegmentGroupTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SegmentGroupStructure:
    boto3_raw_data: "type_defs.SegmentGroupStructureTypeDef" = dataclasses.field()

    Groups = field("Groups")
    Include = field("Include")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SegmentGroupStructureTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SegmentGroupStructureTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSegmentEstimateRequest:
    boto3_raw_data: "type_defs.CreateSegmentEstimateRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")

    @cached_property
    def SegmentQuery(self):  # pragma: no cover
        return SegmentGroupStructure.make_one(self.boto3_raw_data["SegmentQuery"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSegmentEstimateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSegmentEstimateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSegmentDefinitionRequest:
    boto3_raw_data: "type_defs.CreateSegmentDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    SegmentDefinitionName = field("SegmentDefinitionName")
    DisplayName = field("DisplayName")
    SegmentGroups = field("SegmentGroups")
    Description = field("Description")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateSegmentDefinitionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSegmentDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
