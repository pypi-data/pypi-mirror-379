# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_appflow import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AggregationConfig:
    boto3_raw_data: "type_defs.AggregationConfigTypeDef" = dataclasses.field()

    aggregationType = field("aggregationType")
    targetFileSize = field("targetFileSize")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AggregationConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmplitudeConnectorProfileCredentials:
    boto3_raw_data: "type_defs.AmplitudeConnectorProfileCredentialsTypeDef" = (
        dataclasses.field()
    )

    apiKey = field("apiKey")
    secretKey = field("secretKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AmplitudeConnectorProfileCredentialsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmplitudeConnectorProfileCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AmplitudeSourceProperties:
    boto3_raw_data: "type_defs.AmplitudeSourcePropertiesTypeDef" = dataclasses.field()

    object = field("object")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AmplitudeSourcePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AmplitudeSourcePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiKeyCredentials:
    boto3_raw_data: "type_defs.ApiKeyCredentialsTypeDef" = dataclasses.field()

    apiKey = field("apiKey")
    apiSecretKey = field("apiSecretKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApiKeyCredentialsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApiKeyCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthParameter:
    boto3_raw_data: "type_defs.AuthParameterTypeDef" = dataclasses.field()

    key = field("key")
    isRequired = field("isRequired")
    label = field("label")
    description = field("description")
    isSensitiveField = field("isSensitiveField")
    connectorSuppliedValues = field("connectorSuppliedValues")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AuthParameterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AuthParameterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BasicAuthCredentials:
    boto3_raw_data: "type_defs.BasicAuthCredentialsTypeDef" = dataclasses.field()

    username = field("username")
    password = field("password")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BasicAuthCredentialsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BasicAuthCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelFlowExecutionsRequest:
    boto3_raw_data: "type_defs.CancelFlowExecutionsRequestTypeDef" = dataclasses.field()

    flowName = field("flowName")
    executionIds = field("executionIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelFlowExecutionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelFlowExecutionsRequestTypeDef"]
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
class ConnectorRuntimeSetting:
    boto3_raw_data: "type_defs.ConnectorRuntimeSettingTypeDef" = dataclasses.field()

    key = field("key")
    dataType = field("dataType")
    isRequired = field("isRequired")
    label = field("label")
    description = field("description")
    scope = field("scope")
    connectorSuppliedValueOptions = field("connectorSuppliedValueOptions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectorRuntimeSettingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectorRuntimeSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataTransferApi:
    boto3_raw_data: "type_defs.DataTransferApiTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataTransferApiTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataTransferApiTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectorDetail:
    boto3_raw_data: "type_defs.ConnectorDetailTypeDef" = dataclasses.field()

    connectorDescription = field("connectorDescription")
    connectorName = field("connectorName")
    connectorOwner = field("connectorOwner")
    connectorVersion = field("connectorVersion")
    applicationType = field("applicationType")
    connectorType = field("connectorType")
    connectorLabel = field("connectorLabel")
    registeredAt = field("registeredAt")
    registeredBy = field("registeredBy")
    connectorProvisioningType = field("connectorProvisioningType")
    connectorModes = field("connectorModes")
    supportedDataTransferTypes = field("supportedDataTransferTypes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectorDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConnectorDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationFieldProperties:
    boto3_raw_data: "type_defs.DestinationFieldPropertiesTypeDef" = dataclasses.field()

    isCreatable = field("isCreatable")
    isNullable = field("isNullable")
    isUpsertable = field("isUpsertable")
    isUpdatable = field("isUpdatable")
    isDefaultedOnCreate = field("isDefaultedOnCreate")
    supportedWriteOperations = field("supportedWriteOperations")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DestinationFieldPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationFieldPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceFieldProperties:
    boto3_raw_data: "type_defs.SourceFieldPropertiesTypeDef" = dataclasses.field()

    isRetrievable = field("isRetrievable")
    isQueryable = field("isQueryable")
    isTimestampFieldForIncrementalQueries = field(
        "isTimestampFieldForIncrementalQueries"
    )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceFieldPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceFieldPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectorEntity:
    boto3_raw_data: "type_defs.ConnectorEntityTypeDef" = dataclasses.field()

    name = field("name")
    label = field("label")
    hasNestedEntities = field("hasNestedEntities")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectorEntityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConnectorEntityTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GoogleAnalyticsMetadata:
    boto3_raw_data: "type_defs.GoogleAnalyticsMetadataTypeDef" = dataclasses.field()

    oAuthScopes = field("oAuthScopes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GoogleAnalyticsMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GoogleAnalyticsMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HoneycodeMetadata:
    boto3_raw_data: "type_defs.HoneycodeMetadataTypeDef" = dataclasses.field()

    oAuthScopes = field("oAuthScopes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HoneycodeMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HoneycodeMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceMetadata:
    boto3_raw_data: "type_defs.SalesforceMetadataTypeDef" = dataclasses.field()

    oAuthScopes = field("oAuthScopes")
    dataTransferApis = field("dataTransferApis")
    oauth2GrantTypesSupported = field("oauth2GrantTypesSupported")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SalesforceMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SalesforceMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlackMetadata:
    boto3_raw_data: "type_defs.SlackMetadataTypeDef" = dataclasses.field()

    oAuthScopes = field("oAuthScopes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SlackMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SlackMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnowflakeMetadata:
    boto3_raw_data: "type_defs.SnowflakeMetadataTypeDef" = dataclasses.field()

    supportedRegions = field("supportedRegions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SnowflakeMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnowflakeMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ZendeskMetadata:
    boto3_raw_data: "type_defs.ZendeskMetadataTypeDef" = dataclasses.field()

    oAuthScopes = field("oAuthScopes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ZendeskMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ZendeskMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectorOAuthRequest:
    boto3_raw_data: "type_defs.ConnectorOAuthRequestTypeDef" = dataclasses.field()

    authCode = field("authCode")
    redirectUri = field("redirectUri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectorOAuthRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectorOAuthRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectorOperator:
    boto3_raw_data: "type_defs.ConnectorOperatorTypeDef" = dataclasses.field()

    Amplitude = field("Amplitude")
    Datadog = field("Datadog")
    Dynatrace = field("Dynatrace")
    GoogleAnalytics = field("GoogleAnalytics")
    InforNexus = field("InforNexus")
    Marketo = field("Marketo")
    S3 = field("S3")
    Salesforce = field("Salesforce")
    ServiceNow = field("ServiceNow")
    Singular = field("Singular")
    Slack = field("Slack")
    Trendmicro = field("Trendmicro")
    Veeva = field("Veeva")
    Zendesk = field("Zendesk")
    SAPOData = field("SAPOData")
    CustomConnector = field("CustomConnector")
    Pardot = field("Pardot")

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
class DatadogConnectorProfileCredentials:
    boto3_raw_data: "type_defs.DatadogConnectorProfileCredentialsTypeDef" = (
        dataclasses.field()
    )

    apiKey = field("apiKey")
    applicationKey = field("applicationKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DatadogConnectorProfileCredentialsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatadogConnectorProfileCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DynatraceConnectorProfileCredentials:
    boto3_raw_data: "type_defs.DynatraceConnectorProfileCredentialsTypeDef" = (
        dataclasses.field()
    )

    apiToken = field("apiToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DynatraceConnectorProfileCredentialsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DynatraceConnectorProfileCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InforNexusConnectorProfileCredentials:
    boto3_raw_data: "type_defs.InforNexusConnectorProfileCredentialsTypeDef" = (
        dataclasses.field()
    )

    accessKeyId = field("accessKeyId")
    userId = field("userId")
    secretAccessKey = field("secretAccessKey")
    datakey = field("datakey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InforNexusConnectorProfileCredentialsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InforNexusConnectorProfileCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftConnectorProfileCredentials:
    boto3_raw_data: "type_defs.RedshiftConnectorProfileCredentialsTypeDef" = (
        dataclasses.field()
    )

    username = field("username")
    password = field("password")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RedshiftConnectorProfileCredentialsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftConnectorProfileCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SingularConnectorProfileCredentials:
    boto3_raw_data: "type_defs.SingularConnectorProfileCredentialsTypeDef" = (
        dataclasses.field()
    )

    apiKey = field("apiKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SingularConnectorProfileCredentialsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SingularConnectorProfileCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnowflakeConnectorProfileCredentials:
    boto3_raw_data: "type_defs.SnowflakeConnectorProfileCredentialsTypeDef" = (
        dataclasses.field()
    )

    username = field("username")
    password = field("password")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SnowflakeConnectorProfileCredentialsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnowflakeConnectorProfileCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrendmicroConnectorProfileCredentials:
    boto3_raw_data: "type_defs.TrendmicroConnectorProfileCredentialsTypeDef" = (
        dataclasses.field()
    )

    apiSecretKey = field("apiSecretKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TrendmicroConnectorProfileCredentialsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrendmicroConnectorProfileCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VeevaConnectorProfileCredentials:
    boto3_raw_data: "type_defs.VeevaConnectorProfileCredentialsTypeDef" = (
        dataclasses.field()
    )

    username = field("username")
    password = field("password")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VeevaConnectorProfileCredentialsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VeevaConnectorProfileCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatadogConnectorProfileProperties:
    boto3_raw_data: "type_defs.DatadogConnectorProfilePropertiesTypeDef" = (
        dataclasses.field()
    )

    instanceUrl = field("instanceUrl")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DatadogConnectorProfilePropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatadogConnectorProfilePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DynatraceConnectorProfileProperties:
    boto3_raw_data: "type_defs.DynatraceConnectorProfilePropertiesTypeDef" = (
        dataclasses.field()
    )

    instanceUrl = field("instanceUrl")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DynatraceConnectorProfilePropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DynatraceConnectorProfilePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InforNexusConnectorProfileProperties:
    boto3_raw_data: "type_defs.InforNexusConnectorProfilePropertiesTypeDef" = (
        dataclasses.field()
    )

    instanceUrl = field("instanceUrl")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.InforNexusConnectorProfilePropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InforNexusConnectorProfilePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MarketoConnectorProfileProperties:
    boto3_raw_data: "type_defs.MarketoConnectorProfilePropertiesTypeDef" = (
        dataclasses.field()
    )

    instanceUrl = field("instanceUrl")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MarketoConnectorProfilePropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MarketoConnectorProfilePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PardotConnectorProfileProperties:
    boto3_raw_data: "type_defs.PardotConnectorProfilePropertiesTypeDef" = (
        dataclasses.field()
    )

    instanceUrl = field("instanceUrl")
    isSandboxEnvironment = field("isSandboxEnvironment")
    businessUnitId = field("businessUnitId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PardotConnectorProfilePropertiesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PardotConnectorProfilePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftConnectorProfileProperties:
    boto3_raw_data: "type_defs.RedshiftConnectorProfilePropertiesTypeDef" = (
        dataclasses.field()
    )

    bucketName = field("bucketName")
    roleArn = field("roleArn")
    databaseUrl = field("databaseUrl")
    bucketPrefix = field("bucketPrefix")
    dataApiRoleArn = field("dataApiRoleArn")
    isRedshiftServerless = field("isRedshiftServerless")
    clusterIdentifier = field("clusterIdentifier")
    workgroupName = field("workgroupName")
    databaseName = field("databaseName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RedshiftConnectorProfilePropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftConnectorProfilePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceConnectorProfileProperties:
    boto3_raw_data: "type_defs.SalesforceConnectorProfilePropertiesTypeDef" = (
        dataclasses.field()
    )

    instanceUrl = field("instanceUrl")
    isSandboxEnvironment = field("isSandboxEnvironment")
    usePrivateLinkForMetadataAndAuthorization = field(
        "usePrivateLinkForMetadataAndAuthorization"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SalesforceConnectorProfilePropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SalesforceConnectorProfilePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceNowConnectorProfileProperties:
    boto3_raw_data: "type_defs.ServiceNowConnectorProfilePropertiesTypeDef" = (
        dataclasses.field()
    )

    instanceUrl = field("instanceUrl")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceNowConnectorProfilePropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceNowConnectorProfilePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlackConnectorProfileProperties:
    boto3_raw_data: "type_defs.SlackConnectorProfilePropertiesTypeDef" = (
        dataclasses.field()
    )

    instanceUrl = field("instanceUrl")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SlackConnectorProfilePropertiesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlackConnectorProfilePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnowflakeConnectorProfileProperties:
    boto3_raw_data: "type_defs.SnowflakeConnectorProfilePropertiesTypeDef" = (
        dataclasses.field()
    )

    warehouse = field("warehouse")
    stage = field("stage")
    bucketName = field("bucketName")
    bucketPrefix = field("bucketPrefix")
    privateLinkServiceName = field("privateLinkServiceName")
    accountName = field("accountName")
    region = field("region")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SnowflakeConnectorProfilePropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnowflakeConnectorProfilePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VeevaConnectorProfileProperties:
    boto3_raw_data: "type_defs.VeevaConnectorProfilePropertiesTypeDef" = (
        dataclasses.field()
    )

    instanceUrl = field("instanceUrl")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.VeevaConnectorProfilePropertiesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VeevaConnectorProfilePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ZendeskConnectorProfileProperties:
    boto3_raw_data: "type_defs.ZendeskConnectorProfilePropertiesTypeDef" = (
        dataclasses.field()
    )

    instanceUrl = field("instanceUrl")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ZendeskConnectorProfilePropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ZendeskConnectorProfilePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivateConnectionProvisioningState:
    boto3_raw_data: "type_defs.PrivateConnectionProvisioningStateTypeDef" = (
        dataclasses.field()
    )

    status = field("status")
    failureMessage = field("failureMessage")
    failureCause = field("failureCause")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PrivateConnectionProvisioningStateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivateConnectionProvisioningStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LambdaConnectorProvisioningConfig:
    boto3_raw_data: "type_defs.LambdaConnectorProvisioningConfigTypeDef" = (
        dataclasses.field()
    )

    lambdaArn = field("lambdaArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LambdaConnectorProvisioningConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LambdaConnectorProvisioningConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomAuthCredentials:
    boto3_raw_data: "type_defs.CustomAuthCredentialsTypeDef" = dataclasses.field()

    customAuthenticationType = field("customAuthenticationType")
    credentialsMap = field("credentialsMap")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomAuthCredentialsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomAuthCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorHandlingConfig:
    boto3_raw_data: "type_defs.ErrorHandlingConfigTypeDef" = dataclasses.field()

    failOnFirstDestinationError = field("failOnFirstDestinationError")
    bucketPrefix = field("bucketPrefix")
    bucketName = field("bucketName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ErrorHandlingConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ErrorHandlingConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OAuth2PropertiesOutput:
    boto3_raw_data: "type_defs.OAuth2PropertiesOutputTypeDef" = dataclasses.field()

    tokenUrl = field("tokenUrl")
    oAuth2GrantType = field("oAuth2GrantType")
    tokenUrlCustomProperties = field("tokenUrlCustomProperties")

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
class CustomerProfilesDestinationProperties:
    boto3_raw_data: "type_defs.CustomerProfilesDestinationPropertiesTypeDef" = (
        dataclasses.field()
    )

    domainName = field("domainName")
    objectTypeName = field("objectTypeName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomerProfilesDestinationPropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomerProfilesDestinationPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatadogSourceProperties:
    boto3_raw_data: "type_defs.DatadogSourcePropertiesTypeDef" = dataclasses.field()

    object = field("object")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatadogSourcePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatadogSourcePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConnectorProfileRequest:
    boto3_raw_data: "type_defs.DeleteConnectorProfileRequestTypeDef" = (
        dataclasses.field()
    )

    connectorProfileName = field("connectorProfileName")
    forceDelete = field("forceDelete")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteConnectorProfileRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConnectorProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFlowRequest:
    boto3_raw_data: "type_defs.DeleteFlowRequestTypeDef" = dataclasses.field()

    flowName = field("flowName")
    forceDelete = field("forceDelete")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteFlowRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectorEntityRequest:
    boto3_raw_data: "type_defs.DescribeConnectorEntityRequestTypeDef" = (
        dataclasses.field()
    )

    connectorEntityName = field("connectorEntityName")
    connectorType = field("connectorType")
    connectorProfileName = field("connectorProfileName")
    apiVersion = field("apiVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeConnectorEntityRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectorEntityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectorProfilesRequest:
    boto3_raw_data: "type_defs.DescribeConnectorProfilesRequestTypeDef" = (
        dataclasses.field()
    )

    connectorProfileNames = field("connectorProfileNames")
    connectorType = field("connectorType")
    connectorLabel = field("connectorLabel")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeConnectorProfilesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectorProfilesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectorRequest:
    boto3_raw_data: "type_defs.DescribeConnectorRequestTypeDef" = dataclasses.field()

    connectorType = field("connectorType")
    connectorLabel = field("connectorLabel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeConnectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectorsRequest:
    boto3_raw_data: "type_defs.DescribeConnectorsRequestTypeDef" = dataclasses.field()

    connectorTypes = field("connectorTypes")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeConnectorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFlowExecutionRecordsRequest:
    boto3_raw_data: "type_defs.DescribeFlowExecutionRecordsRequestTypeDef" = (
        dataclasses.field()
    )

    flowName = field("flowName")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFlowExecutionRecordsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFlowExecutionRecordsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFlowRequest:
    boto3_raw_data: "type_defs.DescribeFlowRequestTypeDef" = dataclasses.field()

    flowName = field("flowName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFlowRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionDetails:
    boto3_raw_data: "type_defs.ExecutionDetailsTypeDef" = dataclasses.field()

    mostRecentExecutionMessage = field("mostRecentExecutionMessage")
    mostRecentExecutionTime = field("mostRecentExecutionTime")
    mostRecentExecutionStatus = field("mostRecentExecutionStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExecutionDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecutionDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DynatraceSourceProperties:
    boto3_raw_data: "type_defs.DynatraceSourcePropertiesTypeDef" = dataclasses.field()

    object = field("object")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DynatraceSourcePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DynatraceSourcePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorInfo:
    boto3_raw_data: "type_defs.ErrorInfoTypeDef" = dataclasses.field()

    putFailuresCount = field("putFailuresCount")
    executionMessage = field("executionMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Range:
    boto3_raw_data: "type_defs.RangeTypeDef" = dataclasses.field()

    maximum = field("maximum")
    minimum = field("minimum")

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
class GlueDataCatalogConfig:
    boto3_raw_data: "type_defs.GlueDataCatalogConfigTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    databaseName = field("databaseName")
    tablePrefix = field("tablePrefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlueDataCatalogConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlueDataCatalogConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GoogleAnalyticsSourceProperties:
    boto3_raw_data: "type_defs.GoogleAnalyticsSourcePropertiesTypeDef" = (
        dataclasses.field()
    )

    object = field("object")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GoogleAnalyticsSourcePropertiesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GoogleAnalyticsSourcePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IncrementalPullConfig:
    boto3_raw_data: "type_defs.IncrementalPullConfigTypeDef" = dataclasses.field()

    datetimeTypeFieldName = field("datetimeTypeFieldName")

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
class InforNexusSourceProperties:
    boto3_raw_data: "type_defs.InforNexusSourcePropertiesTypeDef" = dataclasses.field()

    object = field("object")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InforNexusSourcePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InforNexusSourcePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectorEntitiesRequest:
    boto3_raw_data: "type_defs.ListConnectorEntitiesRequestTypeDef" = (
        dataclasses.field()
    )

    connectorProfileName = field("connectorProfileName")
    connectorType = field("connectorType")
    entitiesPath = field("entitiesPath")
    apiVersion = field("apiVersion")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConnectorEntitiesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectorEntitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectorsRequest:
    boto3_raw_data: "type_defs.ListConnectorsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConnectorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowsRequest:
    boto3_raw_data: "type_defs.ListFlowsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListFlowsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowsRequestTypeDef"]
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
class MarketoSourceProperties:
    boto3_raw_data: "type_defs.MarketoSourcePropertiesTypeDef" = dataclasses.field()

    object = field("object")

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
class RegistrationOutput:
    boto3_raw_data: "type_defs.RegistrationOutputTypeDef" = dataclasses.field()

    message = field("message")
    result = field("result")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegistrationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegistrationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OAuth2CustomParameter:
    boto3_raw_data: "type_defs.OAuth2CustomParameterTypeDef" = dataclasses.field()

    key = field("key")
    isRequired = field("isRequired")
    label = field("label")
    description = field("description")
    isSensitiveField = field("isSensitiveField")
    connectorSuppliedValues = field("connectorSuppliedValues")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OAuth2CustomParameterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OAuth2CustomParameterTypeDef"]
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

    tokenUrl = field("tokenUrl")
    oAuth2GrantType = field("oAuth2GrantType")
    tokenUrlCustomProperties = field("tokenUrlCustomProperties")

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
class OAuthPropertiesOutput:
    boto3_raw_data: "type_defs.OAuthPropertiesOutputTypeDef" = dataclasses.field()

    tokenUrl = field("tokenUrl")
    authCodeUrl = field("authCodeUrl")
    oAuthScopes = field("oAuthScopes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OAuthPropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OAuthPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OAuthProperties:
    boto3_raw_data: "type_defs.OAuthPropertiesTypeDef" = dataclasses.field()

    tokenUrl = field("tokenUrl")
    authCodeUrl = field("authCodeUrl")
    oAuthScopes = field("oAuthScopes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OAuthPropertiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OAuthPropertiesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PardotSourceProperties:
    boto3_raw_data: "type_defs.PardotSourcePropertiesTypeDef" = dataclasses.field()

    object = field("object")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PardotSourcePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PardotSourcePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrefixConfigOutput:
    boto3_raw_data: "type_defs.PrefixConfigOutputTypeDef" = dataclasses.field()

    prefixType = field("prefixType")
    prefixFormat = field("prefixFormat")
    pathPrefixHierarchy = field("pathPrefixHierarchy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrefixConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrefixConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrefixConfig:
    boto3_raw_data: "type_defs.PrefixConfigTypeDef" = dataclasses.field()

    prefixType = field("prefixType")
    prefixFormat = field("prefixFormat")
    pathPrefixHierarchy = field("pathPrefixHierarchy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PrefixConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PrefixConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetConnectorMetadataCacheRequest:
    boto3_raw_data: "type_defs.ResetConnectorMetadataCacheRequestTypeDef" = (
        dataclasses.field()
    )

    connectorProfileName = field("connectorProfileName")
    connectorType = field("connectorType")
    connectorEntityName = field("connectorEntityName")
    entitiesPath = field("entitiesPath")
    apiVersion = field("apiVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ResetConnectorMetadataCacheRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetConnectorMetadataCacheRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3InputFormatConfig:
    boto3_raw_data: "type_defs.S3InputFormatConfigTypeDef" = dataclasses.field()

    s3InputFileType = field("s3InputFileType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3InputFormatConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3InputFormatConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuccessResponseHandlingConfig:
    boto3_raw_data: "type_defs.SuccessResponseHandlingConfigTypeDef" = (
        dataclasses.field()
    )

    bucketPrefix = field("bucketPrefix")
    bucketName = field("bucketName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SuccessResponseHandlingConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuccessResponseHandlingConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SAPODataPaginationConfig:
    boto3_raw_data: "type_defs.SAPODataPaginationConfigTypeDef" = dataclasses.field()

    maxPageSize = field("maxPageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SAPODataPaginationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SAPODataPaginationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SAPODataParallelismConfig:
    boto3_raw_data: "type_defs.SAPODataParallelismConfigTypeDef" = dataclasses.field()

    maxParallelism = field("maxParallelism")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SAPODataParallelismConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SAPODataParallelismConfigTypeDef"]
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

    object = field("object")
    enableDynamicFieldUpdate = field("enableDynamicFieldUpdate")
    includeDeletedRecords = field("includeDeletedRecords")
    dataTransferApi = field("dataTransferApi")

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
class ScheduledTriggerPropertiesOutput:
    boto3_raw_data: "type_defs.ScheduledTriggerPropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    scheduleExpression = field("scheduleExpression")
    dataPullMode = field("dataPullMode")
    scheduleStartTime = field("scheduleStartTime")
    scheduleEndTime = field("scheduleEndTime")
    timezone = field("timezone")
    scheduleOffset = field("scheduleOffset")
    firstExecutionFrom = field("firstExecutionFrom")
    flowErrorDeactivationThreshold = field("flowErrorDeactivationThreshold")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ScheduledTriggerPropertiesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduledTriggerPropertiesOutputTypeDef"]
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

    object = field("object")

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
class SingularSourceProperties:
    boto3_raw_data: "type_defs.SingularSourcePropertiesTypeDef" = dataclasses.field()

    object = field("object")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SingularSourcePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SingularSourcePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlackSourceProperties:
    boto3_raw_data: "type_defs.SlackSourcePropertiesTypeDef" = dataclasses.field()

    object = field("object")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SlackSourcePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlackSourcePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrendmicroSourceProperties:
    boto3_raw_data: "type_defs.TrendmicroSourcePropertiesTypeDef" = dataclasses.field()

    object = field("object")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrendmicroSourcePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrendmicroSourcePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VeevaSourceProperties:
    boto3_raw_data: "type_defs.VeevaSourcePropertiesTypeDef" = dataclasses.field()

    object = field("object")
    documentType = field("documentType")
    includeSourceFiles = field("includeSourceFiles")
    includeRenditions = field("includeRenditions")
    includeAllVersions = field("includeAllVersions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VeevaSourcePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VeevaSourcePropertiesTypeDef"]
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

    object = field("object")

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
class StartFlowRequest:
    boto3_raw_data: "type_defs.StartFlowRequestTypeDef" = dataclasses.field()

    flowName = field("flowName")
    clientToken = field("clientToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartFlowRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopFlowRequest:
    boto3_raw_data: "type_defs.StopFlowRequestTypeDef" = dataclasses.field()

    flowName = field("flowName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopFlowRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StopFlowRequestTypeDef"]],
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
class UnregisterConnectorRequest:
    boto3_raw_data: "type_defs.UnregisterConnectorRequestTypeDef" = dataclasses.field()

    connectorLabel = field("connectorLabel")
    forceDelete = field("forceDelete")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnregisterConnectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnregisterConnectorRequestTypeDef"]
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
class CustomAuthConfig:
    boto3_raw_data: "type_defs.CustomAuthConfigTypeDef" = dataclasses.field()

    customAuthenticationType = field("customAuthenticationType")

    @cached_property
    def authParameters(self):  # pragma: no cover
        return AuthParameter.make_many(self.boto3_raw_data["authParameters"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomAuthConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomAuthConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelFlowExecutionsResponse:
    boto3_raw_data: "type_defs.CancelFlowExecutionsResponseTypeDef" = (
        dataclasses.field()
    )

    invalidExecutions = field("invalidExecutions")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelFlowExecutionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelFlowExecutionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectorProfileResponse:
    boto3_raw_data: "type_defs.CreateConnectorProfileResponseTypeDef" = (
        dataclasses.field()
    )

    connectorProfileArn = field("connectorProfileArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateConnectorProfileResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectorProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFlowResponse:
    boto3_raw_data: "type_defs.CreateFlowResponseTypeDef" = dataclasses.field()

    flowArn = field("flowArn")
    flowStatus = field("flowStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFlowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFlowResponseTypeDef"]
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
class RegisterConnectorResponse:
    boto3_raw_data: "type_defs.RegisterConnectorResponseTypeDef" = dataclasses.field()

    connectorArn = field("connectorArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterConnectorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterConnectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartFlowResponse:
    boto3_raw_data: "type_defs.StartFlowResponseTypeDef" = dataclasses.field()

    flowArn = field("flowArn")
    flowStatus = field("flowStatus")
    executionId = field("executionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartFlowResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartFlowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopFlowResponse:
    boto3_raw_data: "type_defs.StopFlowResponseTypeDef" = dataclasses.field()

    flowArn = field("flowArn")
    flowStatus = field("flowStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopFlowResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopFlowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectorProfileResponse:
    boto3_raw_data: "type_defs.UpdateConnectorProfileResponseTypeDef" = (
        dataclasses.field()
    )

    connectorProfileArn = field("connectorProfileArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateConnectorProfileResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectorProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectorRegistrationResponse:
    boto3_raw_data: "type_defs.UpdateConnectorRegistrationResponseTypeDef" = (
        dataclasses.field()
    )

    connectorArn = field("connectorArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConnectorRegistrationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectorRegistrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFlowResponse:
    boto3_raw_data: "type_defs.UpdateFlowResponseTypeDef" = dataclasses.field()

    flowStatus = field("flowStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFlowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFlowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomConnectorSourcePropertiesOutput:
    boto3_raw_data: "type_defs.CustomConnectorSourcePropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    entityName = field("entityName")
    customProperties = field("customProperties")

    @cached_property
    def dataTransferApi(self):  # pragma: no cover
        return DataTransferApi.make_one(self.boto3_raw_data["dataTransferApi"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomConnectorSourcePropertiesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomConnectorSourcePropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomConnectorSourceProperties:
    boto3_raw_data: "type_defs.CustomConnectorSourcePropertiesTypeDef" = (
        dataclasses.field()
    )

    entityName = field("entityName")
    customProperties = field("customProperties")

    @cached_property
    def dataTransferApi(self):  # pragma: no cover
        return DataTransferApi.make_one(self.boto3_raw_data["dataTransferApi"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CustomConnectorSourcePropertiesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomConnectorSourcePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectorsResponse:
    boto3_raw_data: "type_defs.ListConnectorsResponseTypeDef" = dataclasses.field()

    @cached_property
    def connectors(self):  # pragma: no cover
        return ConnectorDetail.make_many(self.boto3_raw_data["connectors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConnectorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConnectorEntitiesResponse:
    boto3_raw_data: "type_defs.ListConnectorEntitiesResponseTypeDef" = (
        dataclasses.field()
    )

    connectorEntityMap = field("connectorEntityMap")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListConnectorEntitiesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConnectorEntitiesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectorMetadata:
    boto3_raw_data: "type_defs.ConnectorMetadataTypeDef" = dataclasses.field()

    Amplitude = field("Amplitude")
    Datadog = field("Datadog")
    Dynatrace = field("Dynatrace")

    @cached_property
    def GoogleAnalytics(self):  # pragma: no cover
        return GoogleAnalyticsMetadata.make_one(self.boto3_raw_data["GoogleAnalytics"])

    InforNexus = field("InforNexus")
    Marketo = field("Marketo")
    Redshift = field("Redshift")
    S3 = field("S3")

    @cached_property
    def Salesforce(self):  # pragma: no cover
        return SalesforceMetadata.make_one(self.boto3_raw_data["Salesforce"])

    ServiceNow = field("ServiceNow")
    Singular = field("Singular")

    @cached_property
    def Slack(self):  # pragma: no cover
        return SlackMetadata.make_one(self.boto3_raw_data["Slack"])

    @cached_property
    def Snowflake(self):  # pragma: no cover
        return SnowflakeMetadata.make_one(self.boto3_raw_data["Snowflake"])

    Trendmicro = field("Trendmicro")
    Veeva = field("Veeva")

    @cached_property
    def Zendesk(self):  # pragma: no cover
        return ZendeskMetadata.make_one(self.boto3_raw_data["Zendesk"])

    EventBridge = field("EventBridge")
    Upsolver = field("Upsolver")
    CustomerProfiles = field("CustomerProfiles")

    @cached_property
    def Honeycode(self):  # pragma: no cover
        return HoneycodeMetadata.make_one(self.boto3_raw_data["Honeycode"])

    SAPOData = field("SAPOData")
    Pardot = field("Pardot")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectorMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectorMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GoogleAnalyticsConnectorProfileCredentials:
    boto3_raw_data: "type_defs.GoogleAnalyticsConnectorProfileCredentialsTypeDef" = (
        dataclasses.field()
    )

    clientId = field("clientId")
    clientSecret = field("clientSecret")
    accessToken = field("accessToken")
    refreshToken = field("refreshToken")

    @cached_property
    def oAuthRequest(self):  # pragma: no cover
        return ConnectorOAuthRequest.make_one(self.boto3_raw_data["oAuthRequest"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GoogleAnalyticsConnectorProfileCredentialsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GoogleAnalyticsConnectorProfileCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HoneycodeConnectorProfileCredentials:
    boto3_raw_data: "type_defs.HoneycodeConnectorProfileCredentialsTypeDef" = (
        dataclasses.field()
    )

    accessToken = field("accessToken")
    refreshToken = field("refreshToken")

    @cached_property
    def oAuthRequest(self):  # pragma: no cover
        return ConnectorOAuthRequest.make_one(self.boto3_raw_data["oAuthRequest"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.HoneycodeConnectorProfileCredentialsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HoneycodeConnectorProfileCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MarketoConnectorProfileCredentials:
    boto3_raw_data: "type_defs.MarketoConnectorProfileCredentialsTypeDef" = (
        dataclasses.field()
    )

    clientId = field("clientId")
    clientSecret = field("clientSecret")
    accessToken = field("accessToken")

    @cached_property
    def oAuthRequest(self):  # pragma: no cover
        return ConnectorOAuthRequest.make_one(self.boto3_raw_data["oAuthRequest"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MarketoConnectorProfileCredentialsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MarketoConnectorProfileCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OAuth2Credentials:
    boto3_raw_data: "type_defs.OAuth2CredentialsTypeDef" = dataclasses.field()

    clientId = field("clientId")
    clientSecret = field("clientSecret")
    accessToken = field("accessToken")
    refreshToken = field("refreshToken")

    @cached_property
    def oAuthRequest(self):  # pragma: no cover
        return ConnectorOAuthRequest.make_one(self.boto3_raw_data["oAuthRequest"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OAuth2CredentialsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OAuth2CredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OAuthCredentials:
    boto3_raw_data: "type_defs.OAuthCredentialsTypeDef" = dataclasses.field()

    clientId = field("clientId")
    clientSecret = field("clientSecret")
    accessToken = field("accessToken")
    refreshToken = field("refreshToken")

    @cached_property
    def oAuthRequest(self):  # pragma: no cover
        return ConnectorOAuthRequest.make_one(self.boto3_raw_data["oAuthRequest"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OAuthCredentialsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OAuthCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PardotConnectorProfileCredentials:
    boto3_raw_data: "type_defs.PardotConnectorProfileCredentialsTypeDef" = (
        dataclasses.field()
    )

    accessToken = field("accessToken")
    refreshToken = field("refreshToken")

    @cached_property
    def oAuthRequest(self):  # pragma: no cover
        return ConnectorOAuthRequest.make_one(self.boto3_raw_data["oAuthRequest"])

    clientCredentialsArn = field("clientCredentialsArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PardotConnectorProfileCredentialsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PardotConnectorProfileCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceConnectorProfileCredentials:
    boto3_raw_data: "type_defs.SalesforceConnectorProfileCredentialsTypeDef" = (
        dataclasses.field()
    )

    accessToken = field("accessToken")
    refreshToken = field("refreshToken")

    @cached_property
    def oAuthRequest(self):  # pragma: no cover
        return ConnectorOAuthRequest.make_one(self.boto3_raw_data["oAuthRequest"])

    clientCredentialsArn = field("clientCredentialsArn")
    oAuth2GrantType = field("oAuth2GrantType")
    jwtToken = field("jwtToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SalesforceConnectorProfileCredentialsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SalesforceConnectorProfileCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlackConnectorProfileCredentials:
    boto3_raw_data: "type_defs.SlackConnectorProfileCredentialsTypeDef" = (
        dataclasses.field()
    )

    clientId = field("clientId")
    clientSecret = field("clientSecret")
    accessToken = field("accessToken")

    @cached_property
    def oAuthRequest(self):  # pragma: no cover
        return ConnectorOAuthRequest.make_one(self.boto3_raw_data["oAuthRequest"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SlackConnectorProfileCredentialsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlackConnectorProfileCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ZendeskConnectorProfileCredentials:
    boto3_raw_data: "type_defs.ZendeskConnectorProfileCredentialsTypeDef" = (
        dataclasses.field()
    )

    clientId = field("clientId")
    clientSecret = field("clientSecret")
    accessToken = field("accessToken")

    @cached_property
    def oAuthRequest(self):  # pragma: no cover
        return ConnectorOAuthRequest.make_one(self.boto3_raw_data["oAuthRequest"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ZendeskConnectorProfileCredentialsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ZendeskConnectorProfileCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TaskOutput:
    boto3_raw_data: "type_defs.TaskOutputTypeDef" = dataclasses.field()

    sourceFields = field("sourceFields")
    taskType = field("taskType")

    @cached_property
    def connectorOperator(self):  # pragma: no cover
        return ConnectorOperator.make_one(self.boto3_raw_data["connectorOperator"])

    destinationField = field("destinationField")
    taskProperties = field("taskProperties")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaskOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TaskOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Task:
    boto3_raw_data: "type_defs.TaskTypeDef" = dataclasses.field()

    sourceFields = field("sourceFields")
    taskType = field("taskType")

    @cached_property
    def connectorOperator(self):  # pragma: no cover
        return ConnectorOperator.make_one(self.boto3_raw_data["connectorOperator"])

    destinationField = field("destinationField")
    taskProperties = field("taskProperties")

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
class ConnectorProvisioningConfig:
    boto3_raw_data: "type_defs.ConnectorProvisioningConfigTypeDef" = dataclasses.field()

    @cached_property
    def lambda_(self):  # pragma: no cover
        return LambdaConnectorProvisioningConfig.make_one(self.boto3_raw_data["lambda"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectorProvisioningConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectorProvisioningConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomConnectorDestinationPropertiesOutput:
    boto3_raw_data: "type_defs.CustomConnectorDestinationPropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    entityName = field("entityName")

    @cached_property
    def errorHandlingConfig(self):  # pragma: no cover
        return ErrorHandlingConfig.make_one(self.boto3_raw_data["errorHandlingConfig"])

    writeOperationType = field("writeOperationType")
    idFieldNames = field("idFieldNames")
    customProperties = field("customProperties")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomConnectorDestinationPropertiesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomConnectorDestinationPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomConnectorDestinationProperties:
    boto3_raw_data: "type_defs.CustomConnectorDestinationPropertiesTypeDef" = (
        dataclasses.field()
    )

    entityName = field("entityName")

    @cached_property
    def errorHandlingConfig(self):  # pragma: no cover
        return ErrorHandlingConfig.make_one(self.boto3_raw_data["errorHandlingConfig"])

    writeOperationType = field("writeOperationType")
    idFieldNames = field("idFieldNames")
    customProperties = field("customProperties")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomConnectorDestinationPropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomConnectorDestinationPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventBridgeDestinationProperties:
    boto3_raw_data: "type_defs.EventBridgeDestinationPropertiesTypeDef" = (
        dataclasses.field()
    )

    object = field("object")

    @cached_property
    def errorHandlingConfig(self):  # pragma: no cover
        return ErrorHandlingConfig.make_one(self.boto3_raw_data["errorHandlingConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EventBridgeDestinationPropertiesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventBridgeDestinationPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HoneycodeDestinationProperties:
    boto3_raw_data: "type_defs.HoneycodeDestinationPropertiesTypeDef" = (
        dataclasses.field()
    )

    object = field("object")

    @cached_property
    def errorHandlingConfig(self):  # pragma: no cover
        return ErrorHandlingConfig.make_one(self.boto3_raw_data["errorHandlingConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.HoneycodeDestinationPropertiesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HoneycodeDestinationPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MarketoDestinationProperties:
    boto3_raw_data: "type_defs.MarketoDestinationPropertiesTypeDef" = (
        dataclasses.field()
    )

    object = field("object")

    @cached_property
    def errorHandlingConfig(self):  # pragma: no cover
        return ErrorHandlingConfig.make_one(self.boto3_raw_data["errorHandlingConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MarketoDestinationPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MarketoDestinationPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedshiftDestinationProperties:
    boto3_raw_data: "type_defs.RedshiftDestinationPropertiesTypeDef" = (
        dataclasses.field()
    )

    object = field("object")
    intermediateBucketName = field("intermediateBucketName")
    bucketPrefix = field("bucketPrefix")

    @cached_property
    def errorHandlingConfig(self):  # pragma: no cover
        return ErrorHandlingConfig.make_one(self.boto3_raw_data["errorHandlingConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RedshiftDestinationPropertiesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedshiftDestinationPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceDestinationPropertiesOutput:
    boto3_raw_data: "type_defs.SalesforceDestinationPropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    object = field("object")
    idFieldNames = field("idFieldNames")

    @cached_property
    def errorHandlingConfig(self):  # pragma: no cover
        return ErrorHandlingConfig.make_one(self.boto3_raw_data["errorHandlingConfig"])

    writeOperationType = field("writeOperationType")
    dataTransferApi = field("dataTransferApi")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SalesforceDestinationPropertiesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SalesforceDestinationPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SalesforceDestinationProperties:
    boto3_raw_data: "type_defs.SalesforceDestinationPropertiesTypeDef" = (
        dataclasses.field()
    )

    object = field("object")
    idFieldNames = field("idFieldNames")

    @cached_property
    def errorHandlingConfig(self):  # pragma: no cover
        return ErrorHandlingConfig.make_one(self.boto3_raw_data["errorHandlingConfig"])

    writeOperationType = field("writeOperationType")
    dataTransferApi = field("dataTransferApi")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SalesforceDestinationPropertiesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SalesforceDestinationPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnowflakeDestinationProperties:
    boto3_raw_data: "type_defs.SnowflakeDestinationPropertiesTypeDef" = (
        dataclasses.field()
    )

    object = field("object")
    intermediateBucketName = field("intermediateBucketName")
    bucketPrefix = field("bucketPrefix")

    @cached_property
    def errorHandlingConfig(self):  # pragma: no cover
        return ErrorHandlingConfig.make_one(self.boto3_raw_data["errorHandlingConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SnowflakeDestinationPropertiesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnowflakeDestinationPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ZendeskDestinationPropertiesOutput:
    boto3_raw_data: "type_defs.ZendeskDestinationPropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    object = field("object")
    idFieldNames = field("idFieldNames")

    @cached_property
    def errorHandlingConfig(self):  # pragma: no cover
        return ErrorHandlingConfig.make_one(self.boto3_raw_data["errorHandlingConfig"])

    writeOperationType = field("writeOperationType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ZendeskDestinationPropertiesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ZendeskDestinationPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ZendeskDestinationProperties:
    boto3_raw_data: "type_defs.ZendeskDestinationPropertiesTypeDef" = (
        dataclasses.field()
    )

    object = field("object")
    idFieldNames = field("idFieldNames")

    @cached_property
    def errorHandlingConfig(self):  # pragma: no cover
        return ErrorHandlingConfig.make_one(self.boto3_raw_data["errorHandlingConfig"])

    writeOperationType = field("writeOperationType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ZendeskDestinationPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ZendeskDestinationPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomConnectorProfilePropertiesOutput:
    boto3_raw_data: "type_defs.CustomConnectorProfilePropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    profileProperties = field("profileProperties")

    @cached_property
    def oAuth2Properties(self):  # pragma: no cover
        return OAuth2PropertiesOutput.make_one(self.boto3_raw_data["oAuth2Properties"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomConnectorProfilePropertiesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomConnectorProfilePropertiesOutputTypeDef"]
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

    flowArn = field("flowArn")
    description = field("description")
    flowName = field("flowName")
    flowStatus = field("flowStatus")
    sourceConnectorType = field("sourceConnectorType")
    sourceConnectorLabel = field("sourceConnectorLabel")
    destinationConnectorType = field("destinationConnectorType")
    destinationConnectorLabel = field("destinationConnectorLabel")
    triggerType = field("triggerType")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    createdBy = field("createdBy")
    lastUpdatedBy = field("lastUpdatedBy")
    tags = field("tags")

    @cached_property
    def lastRunExecutionDetails(self):  # pragma: no cover
        return ExecutionDetails.make_one(self.boto3_raw_data["lastRunExecutionDetails"])

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
class ExecutionResult:
    boto3_raw_data: "type_defs.ExecutionResultTypeDef" = dataclasses.field()

    @cached_property
    def errorInfo(self):  # pragma: no cover
        return ErrorInfo.make_one(self.boto3_raw_data["errorInfo"])

    bytesProcessed = field("bytesProcessed")
    bytesWritten = field("bytesWritten")
    recordsProcessed = field("recordsProcessed")
    numParallelProcesses = field("numParallelProcesses")
    maxPageSize = field("maxPageSize")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExecutionResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExecutionResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldTypeDetails:
    boto3_raw_data: "type_defs.FieldTypeDetailsTypeDef" = dataclasses.field()

    fieldType = field("fieldType")
    filterOperators = field("filterOperators")
    supportedValues = field("supportedValues")
    valueRegexPattern = field("valueRegexPattern")
    supportedDateFormat = field("supportedDateFormat")

    @cached_property
    def fieldValueRange(self):  # pragma: no cover
        return Range.make_one(self.boto3_raw_data["fieldValueRange"])

    @cached_property
    def fieldLengthRange(self):  # pragma: no cover
        return Range.make_one(self.boto3_raw_data["fieldLengthRange"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldTypeDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldTypeDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataCatalogConfig:
    boto3_raw_data: "type_defs.MetadataCatalogConfigTypeDef" = dataclasses.field()

    @cached_property
    def glueDataCatalog(self):  # pragma: no cover
        return GlueDataCatalogConfig.make_one(self.boto3_raw_data["glueDataCatalog"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetadataCatalogConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataCatalogConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetadataCatalogDetail:
    boto3_raw_data: "type_defs.MetadataCatalogDetailTypeDef" = dataclasses.field()

    catalogType = field("catalogType")
    tableName = field("tableName")

    @cached_property
    def tableRegistrationOutput(self):  # pragma: no cover
        return RegistrationOutput.make_one(
            self.boto3_raw_data["tableRegistrationOutput"]
        )

    @cached_property
    def partitionRegistrationOutput(self):  # pragma: no cover
        return RegistrationOutput.make_one(
            self.boto3_raw_data["partitionRegistrationOutput"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetadataCatalogDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetadataCatalogDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OAuth2Defaults:
    boto3_raw_data: "type_defs.OAuth2DefaultsTypeDef" = dataclasses.field()

    oauthScopes = field("oauthScopes")
    tokenUrls = field("tokenUrls")
    authCodeUrls = field("authCodeUrls")
    oauth2GrantTypesSupported = field("oauth2GrantTypesSupported")

    @cached_property
    def oauth2CustomProperties(self):  # pragma: no cover
        return OAuth2CustomParameter.make_many(
            self.boto3_raw_data["oauth2CustomProperties"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OAuth2DefaultsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OAuth2DefaultsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SAPODataConnectorProfilePropertiesOutput:
    boto3_raw_data: "type_defs.SAPODataConnectorProfilePropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    applicationHostUrl = field("applicationHostUrl")
    applicationServicePath = field("applicationServicePath")
    portNumber = field("portNumber")
    clientNumber = field("clientNumber")
    logonLanguage = field("logonLanguage")
    privateLinkServiceName = field("privateLinkServiceName")

    @cached_property
    def oAuthProperties(self):  # pragma: no cover
        return OAuthPropertiesOutput.make_one(self.boto3_raw_data["oAuthProperties"])

    disableSSO = field("disableSSO")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SAPODataConnectorProfilePropertiesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SAPODataConnectorProfilePropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3OutputFormatConfigOutput:
    boto3_raw_data: "type_defs.S3OutputFormatConfigOutputTypeDef" = dataclasses.field()

    fileType = field("fileType")

    @cached_property
    def prefixConfig(self):  # pragma: no cover
        return PrefixConfigOutput.make_one(self.boto3_raw_data["prefixConfig"])

    @cached_property
    def aggregationConfig(self):  # pragma: no cover
        return AggregationConfig.make_one(self.boto3_raw_data["aggregationConfig"])

    preserveSourceDataTyping = field("preserveSourceDataTyping")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3OutputFormatConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3OutputFormatConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpsolverS3OutputFormatConfigOutput:
    boto3_raw_data: "type_defs.UpsolverS3OutputFormatConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def prefixConfig(self):  # pragma: no cover
        return PrefixConfigOutput.make_one(self.boto3_raw_data["prefixConfig"])

    fileType = field("fileType")

    @cached_property
    def aggregationConfig(self):  # pragma: no cover
        return AggregationConfig.make_one(self.boto3_raw_data["aggregationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpsolverS3OutputFormatConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpsolverS3OutputFormatConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3SourceProperties:
    boto3_raw_data: "type_defs.S3SourcePropertiesTypeDef" = dataclasses.field()

    bucketName = field("bucketName")
    bucketPrefix = field("bucketPrefix")

    @cached_property
    def s3InputFormatConfig(self):  # pragma: no cover
        return S3InputFormatConfig.make_one(self.boto3_raw_data["s3InputFormatConfig"])

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
class SAPODataDestinationPropertiesOutput:
    boto3_raw_data: "type_defs.SAPODataDestinationPropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    objectPath = field("objectPath")

    @cached_property
    def successResponseHandlingConfig(self):  # pragma: no cover
        return SuccessResponseHandlingConfig.make_one(
            self.boto3_raw_data["successResponseHandlingConfig"]
        )

    idFieldNames = field("idFieldNames")

    @cached_property
    def errorHandlingConfig(self):  # pragma: no cover
        return ErrorHandlingConfig.make_one(self.boto3_raw_data["errorHandlingConfig"])

    writeOperationType = field("writeOperationType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SAPODataDestinationPropertiesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SAPODataDestinationPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SAPODataDestinationProperties:
    boto3_raw_data: "type_defs.SAPODataDestinationPropertiesTypeDef" = (
        dataclasses.field()
    )

    objectPath = field("objectPath")

    @cached_property
    def successResponseHandlingConfig(self):  # pragma: no cover
        return SuccessResponseHandlingConfig.make_one(
            self.boto3_raw_data["successResponseHandlingConfig"]
        )

    idFieldNames = field("idFieldNames")

    @cached_property
    def errorHandlingConfig(self):  # pragma: no cover
        return ErrorHandlingConfig.make_one(self.boto3_raw_data["errorHandlingConfig"])

    writeOperationType = field("writeOperationType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SAPODataDestinationPropertiesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SAPODataDestinationPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SAPODataSourceProperties:
    boto3_raw_data: "type_defs.SAPODataSourcePropertiesTypeDef" = dataclasses.field()

    objectPath = field("objectPath")

    @cached_property
    def parallelismConfig(self):  # pragma: no cover
        return SAPODataParallelismConfig.make_one(
            self.boto3_raw_data["parallelismConfig"]
        )

    @cached_property
    def paginationConfig(self):  # pragma: no cover
        return SAPODataPaginationConfig.make_one(
            self.boto3_raw_data["paginationConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SAPODataSourcePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SAPODataSourcePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TriggerPropertiesOutput:
    boto3_raw_data: "type_defs.TriggerPropertiesOutputTypeDef" = dataclasses.field()

    @cached_property
    def Scheduled(self):  # pragma: no cover
        return ScheduledTriggerPropertiesOutput.make_one(
            self.boto3_raw_data["Scheduled"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TriggerPropertiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TriggerPropertiesOutputTypeDef"]
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

    scheduleExpression = field("scheduleExpression")
    dataPullMode = field("dataPullMode")
    scheduleStartTime = field("scheduleStartTime")
    scheduleEndTime = field("scheduleEndTime")
    timezone = field("timezone")
    scheduleOffset = field("scheduleOffset")
    firstExecutionFrom = field("firstExecutionFrom")
    flowErrorDeactivationThreshold = field("flowErrorDeactivationThreshold")

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
class CustomConnectorProfileCredentials:
    boto3_raw_data: "type_defs.CustomConnectorProfileCredentialsTypeDef" = (
        dataclasses.field()
    )

    authenticationType = field("authenticationType")

    @cached_property
    def basic(self):  # pragma: no cover
        return BasicAuthCredentials.make_one(self.boto3_raw_data["basic"])

    @cached_property
    def oauth2(self):  # pragma: no cover
        return OAuth2Credentials.make_one(self.boto3_raw_data["oauth2"])

    @cached_property
    def apiKey(self):  # pragma: no cover
        return ApiKeyCredentials.make_one(self.boto3_raw_data["apiKey"])

    @cached_property
    def custom(self):  # pragma: no cover
        return CustomAuthCredentials.make_one(self.boto3_raw_data["custom"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CustomConnectorProfileCredentialsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomConnectorProfileCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceNowConnectorProfileCredentials:
    boto3_raw_data: "type_defs.ServiceNowConnectorProfileCredentialsTypeDef" = (
        dataclasses.field()
    )

    username = field("username")
    password = field("password")

    @cached_property
    def oAuth2Credentials(self):  # pragma: no cover
        return OAuth2Credentials.make_one(self.boto3_raw_data["oAuth2Credentials"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceNowConnectorProfileCredentialsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceNowConnectorProfileCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SAPODataConnectorProfileCredentials:
    boto3_raw_data: "type_defs.SAPODataConnectorProfileCredentialsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def basicAuthCredentials(self):  # pragma: no cover
        return BasicAuthCredentials.make_one(
            self.boto3_raw_data["basicAuthCredentials"]
        )

    @cached_property
    def oAuthCredentials(self):  # pragma: no cover
        return OAuthCredentials.make_one(self.boto3_raw_data["oAuthCredentials"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SAPODataConnectorProfileCredentialsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SAPODataConnectorProfileCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterConnectorRequest:
    boto3_raw_data: "type_defs.RegisterConnectorRequestTypeDef" = dataclasses.field()

    connectorLabel = field("connectorLabel")
    description = field("description")
    connectorProvisioningType = field("connectorProvisioningType")

    @cached_property
    def connectorProvisioningConfig(self):  # pragma: no cover
        return ConnectorProvisioningConfig.make_one(
            self.boto3_raw_data["connectorProvisioningConfig"]
        )

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterConnectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterConnectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectorRegistrationRequest:
    boto3_raw_data: "type_defs.UpdateConnectorRegistrationRequestTypeDef" = (
        dataclasses.field()
    )

    connectorLabel = field("connectorLabel")
    description = field("description")

    @cached_property
    def connectorProvisioningConfig(self):  # pragma: no cover
        return ConnectorProvisioningConfig.make_one(
            self.boto3_raw_data["connectorProvisioningConfig"]
        )

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConnectorRegistrationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectorRegistrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFlowsResponse:
    boto3_raw_data: "type_defs.ListFlowsResponseTypeDef" = dataclasses.field()

    @cached_property
    def flows(self):  # pragma: no cover
        return FlowDefinition.make_many(self.boto3_raw_data["flows"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListFlowsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFlowsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SupportedFieldTypeDetails:
    boto3_raw_data: "type_defs.SupportedFieldTypeDetailsTypeDef" = dataclasses.field()

    @cached_property
    def v1(self):  # pragma: no cover
        return FieldTypeDetails.make_one(self.boto3_raw_data["v1"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SupportedFieldTypeDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SupportedFieldTypeDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecutionRecord:
    boto3_raw_data: "type_defs.ExecutionRecordTypeDef" = dataclasses.field()

    executionId = field("executionId")
    executionStatus = field("executionStatus")

    @cached_property
    def executionResult(self):  # pragma: no cover
        return ExecutionResult.make_one(self.boto3_raw_data["executionResult"])

    startedAt = field("startedAt")
    lastUpdatedAt = field("lastUpdatedAt")
    dataPullStartTime = field("dataPullStartTime")
    dataPullEndTime = field("dataPullEndTime")

    @cached_property
    def metadataCatalogDetails(self):  # pragma: no cover
        return MetadataCatalogDetail.make_many(
            self.boto3_raw_data["metadataCatalogDetails"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExecutionRecordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExecutionRecordTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthenticationConfig:
    boto3_raw_data: "type_defs.AuthenticationConfigTypeDef" = dataclasses.field()

    isBasicAuthSupported = field("isBasicAuthSupported")
    isApiKeyAuthSupported = field("isApiKeyAuthSupported")
    isOAuth2Supported = field("isOAuth2Supported")
    isCustomAuthSupported = field("isCustomAuthSupported")

    @cached_property
    def oAuth2Defaults(self):  # pragma: no cover
        return OAuth2Defaults.make_one(self.boto3_raw_data["oAuth2Defaults"])

    @cached_property
    def customAuthConfigs(self):  # pragma: no cover
        return CustomAuthConfig.make_many(self.boto3_raw_data["customAuthConfigs"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthenticationConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthenticationConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomConnectorProfileProperties:
    boto3_raw_data: "type_defs.CustomConnectorProfilePropertiesTypeDef" = (
        dataclasses.field()
    )

    profileProperties = field("profileProperties")
    oAuth2Properties = field("oAuth2Properties")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CustomConnectorProfilePropertiesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomConnectorProfilePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectorProfilePropertiesOutput:
    boto3_raw_data: "type_defs.ConnectorProfilePropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    Amplitude = field("Amplitude")

    @cached_property
    def Datadog(self):  # pragma: no cover
        return DatadogConnectorProfileProperties.make_one(
            self.boto3_raw_data["Datadog"]
        )

    @cached_property
    def Dynatrace(self):  # pragma: no cover
        return DynatraceConnectorProfileProperties.make_one(
            self.boto3_raw_data["Dynatrace"]
        )

    GoogleAnalytics = field("GoogleAnalytics")
    Honeycode = field("Honeycode")

    @cached_property
    def InforNexus(self):  # pragma: no cover
        return InforNexusConnectorProfileProperties.make_one(
            self.boto3_raw_data["InforNexus"]
        )

    @cached_property
    def Marketo(self):  # pragma: no cover
        return MarketoConnectorProfileProperties.make_one(
            self.boto3_raw_data["Marketo"]
        )

    @cached_property
    def Redshift(self):  # pragma: no cover
        return RedshiftConnectorProfileProperties.make_one(
            self.boto3_raw_data["Redshift"]
        )

    @cached_property
    def Salesforce(self):  # pragma: no cover
        return SalesforceConnectorProfileProperties.make_one(
            self.boto3_raw_data["Salesforce"]
        )

    @cached_property
    def ServiceNow(self):  # pragma: no cover
        return ServiceNowConnectorProfileProperties.make_one(
            self.boto3_raw_data["ServiceNow"]
        )

    Singular = field("Singular")

    @cached_property
    def Slack(self):  # pragma: no cover
        return SlackConnectorProfileProperties.make_one(self.boto3_raw_data["Slack"])

    @cached_property
    def Snowflake(self):  # pragma: no cover
        return SnowflakeConnectorProfileProperties.make_one(
            self.boto3_raw_data["Snowflake"]
        )

    Trendmicro = field("Trendmicro")

    @cached_property
    def Veeva(self):  # pragma: no cover
        return VeevaConnectorProfileProperties.make_one(self.boto3_raw_data["Veeva"])

    @cached_property
    def Zendesk(self):  # pragma: no cover
        return ZendeskConnectorProfileProperties.make_one(
            self.boto3_raw_data["Zendesk"]
        )

    @cached_property
    def SAPOData(self):  # pragma: no cover
        return SAPODataConnectorProfilePropertiesOutput.make_one(
            self.boto3_raw_data["SAPOData"]
        )

    @cached_property
    def CustomConnector(self):  # pragma: no cover
        return CustomConnectorProfilePropertiesOutput.make_one(
            self.boto3_raw_data["CustomConnector"]
        )

    @cached_property
    def Pardot(self):  # pragma: no cover
        return PardotConnectorProfileProperties.make_one(self.boto3_raw_data["Pardot"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConnectorProfilePropertiesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectorProfilePropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SAPODataConnectorProfileProperties:
    boto3_raw_data: "type_defs.SAPODataConnectorProfilePropertiesTypeDef" = (
        dataclasses.field()
    )

    applicationHostUrl = field("applicationHostUrl")
    applicationServicePath = field("applicationServicePath")
    portNumber = field("portNumber")
    clientNumber = field("clientNumber")
    logonLanguage = field("logonLanguage")
    privateLinkServiceName = field("privateLinkServiceName")
    oAuthProperties = field("oAuthProperties")
    disableSSO = field("disableSSO")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SAPODataConnectorProfilePropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SAPODataConnectorProfilePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DestinationPropertiesOutput:
    boto3_raw_data: "type_defs.S3DestinationPropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    bucketName = field("bucketName")
    bucketPrefix = field("bucketPrefix")

    @cached_property
    def s3OutputFormatConfig(self):  # pragma: no cover
        return S3OutputFormatConfigOutput.make_one(
            self.boto3_raw_data["s3OutputFormatConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.S3DestinationPropertiesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3DestinationPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpsolverDestinationPropertiesOutput:
    boto3_raw_data: "type_defs.UpsolverDestinationPropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    bucketName = field("bucketName")

    @cached_property
    def s3OutputFormatConfig(self):  # pragma: no cover
        return UpsolverS3OutputFormatConfigOutput.make_one(
            self.boto3_raw_data["s3OutputFormatConfig"]
        )

    bucketPrefix = field("bucketPrefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpsolverDestinationPropertiesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpsolverDestinationPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3OutputFormatConfig:
    boto3_raw_data: "type_defs.S3OutputFormatConfigTypeDef" = dataclasses.field()

    fileType = field("fileType")
    prefixConfig = field("prefixConfig")

    @cached_property
    def aggregationConfig(self):  # pragma: no cover
        return AggregationConfig.make_one(self.boto3_raw_data["aggregationConfig"])

    preserveSourceDataTyping = field("preserveSourceDataTyping")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3OutputFormatConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3OutputFormatConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpsolverS3OutputFormatConfig:
    boto3_raw_data: "type_defs.UpsolverS3OutputFormatConfigTypeDef" = (
        dataclasses.field()
    )

    prefixConfig = field("prefixConfig")
    fileType = field("fileType")

    @cached_property
    def aggregationConfig(self):  # pragma: no cover
        return AggregationConfig.make_one(self.boto3_raw_data["aggregationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpsolverS3OutputFormatConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpsolverS3OutputFormatConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceConnectorPropertiesOutput:
    boto3_raw_data: "type_defs.SourceConnectorPropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Amplitude(self):  # pragma: no cover
        return AmplitudeSourceProperties.make_one(self.boto3_raw_data["Amplitude"])

    @cached_property
    def Datadog(self):  # pragma: no cover
        return DatadogSourceProperties.make_one(self.boto3_raw_data["Datadog"])

    @cached_property
    def Dynatrace(self):  # pragma: no cover
        return DynatraceSourceProperties.make_one(self.boto3_raw_data["Dynatrace"])

    @cached_property
    def GoogleAnalytics(self):  # pragma: no cover
        return GoogleAnalyticsSourceProperties.make_one(
            self.boto3_raw_data["GoogleAnalytics"]
        )

    @cached_property
    def InforNexus(self):  # pragma: no cover
        return InforNexusSourceProperties.make_one(self.boto3_raw_data["InforNexus"])

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
    def Singular(self):  # pragma: no cover
        return SingularSourceProperties.make_one(self.boto3_raw_data["Singular"])

    @cached_property
    def Slack(self):  # pragma: no cover
        return SlackSourceProperties.make_one(self.boto3_raw_data["Slack"])

    @cached_property
    def Trendmicro(self):  # pragma: no cover
        return TrendmicroSourceProperties.make_one(self.boto3_raw_data["Trendmicro"])

    @cached_property
    def Veeva(self):  # pragma: no cover
        return VeevaSourceProperties.make_one(self.boto3_raw_data["Veeva"])

    @cached_property
    def Zendesk(self):  # pragma: no cover
        return ZendeskSourceProperties.make_one(self.boto3_raw_data["Zendesk"])

    @cached_property
    def SAPOData(self):  # pragma: no cover
        return SAPODataSourceProperties.make_one(self.boto3_raw_data["SAPOData"])

    @cached_property
    def CustomConnector(self):  # pragma: no cover
        return CustomConnectorSourcePropertiesOutput.make_one(
            self.boto3_raw_data["CustomConnector"]
        )

    @cached_property
    def Pardot(self):  # pragma: no cover
        return PardotSourceProperties.make_one(self.boto3_raw_data["Pardot"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SourceConnectorPropertiesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceConnectorPropertiesOutputTypeDef"]
        ],
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
    def Amplitude(self):  # pragma: no cover
        return AmplitudeSourceProperties.make_one(self.boto3_raw_data["Amplitude"])

    @cached_property
    def Datadog(self):  # pragma: no cover
        return DatadogSourceProperties.make_one(self.boto3_raw_data["Datadog"])

    @cached_property
    def Dynatrace(self):  # pragma: no cover
        return DynatraceSourceProperties.make_one(self.boto3_raw_data["Dynatrace"])

    @cached_property
    def GoogleAnalytics(self):  # pragma: no cover
        return GoogleAnalyticsSourceProperties.make_one(
            self.boto3_raw_data["GoogleAnalytics"]
        )

    @cached_property
    def InforNexus(self):  # pragma: no cover
        return InforNexusSourceProperties.make_one(self.boto3_raw_data["InforNexus"])

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
    def Singular(self):  # pragma: no cover
        return SingularSourceProperties.make_one(self.boto3_raw_data["Singular"])

    @cached_property
    def Slack(self):  # pragma: no cover
        return SlackSourceProperties.make_one(self.boto3_raw_data["Slack"])

    @cached_property
    def Trendmicro(self):  # pragma: no cover
        return TrendmicroSourceProperties.make_one(self.boto3_raw_data["Trendmicro"])

    @cached_property
    def Veeva(self):  # pragma: no cover
        return VeevaSourceProperties.make_one(self.boto3_raw_data["Veeva"])

    @cached_property
    def Zendesk(self):  # pragma: no cover
        return ZendeskSourceProperties.make_one(self.boto3_raw_data["Zendesk"])

    @cached_property
    def SAPOData(self):  # pragma: no cover
        return SAPODataSourceProperties.make_one(self.boto3_raw_data["SAPOData"])

    @cached_property
    def CustomConnector(self):  # pragma: no cover
        return CustomConnectorSourceProperties.make_one(
            self.boto3_raw_data["CustomConnector"]
        )

    @cached_property
    def Pardot(self):  # pragma: no cover
        return PardotSourceProperties.make_one(self.boto3_raw_data["Pardot"])

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
class TriggerConfigOutput:
    boto3_raw_data: "type_defs.TriggerConfigOutputTypeDef" = dataclasses.field()

    triggerType = field("triggerType")

    @cached_property
    def triggerProperties(self):  # pragma: no cover
        return TriggerPropertiesOutput.make_one(
            self.boto3_raw_data["triggerProperties"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TriggerConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TriggerConfigOutputTypeDef"]
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
class ConnectorProfileCredentials:
    boto3_raw_data: "type_defs.ConnectorProfileCredentialsTypeDef" = dataclasses.field()

    @cached_property
    def Amplitude(self):  # pragma: no cover
        return AmplitudeConnectorProfileCredentials.make_one(
            self.boto3_raw_data["Amplitude"]
        )

    @cached_property
    def Datadog(self):  # pragma: no cover
        return DatadogConnectorProfileCredentials.make_one(
            self.boto3_raw_data["Datadog"]
        )

    @cached_property
    def Dynatrace(self):  # pragma: no cover
        return DynatraceConnectorProfileCredentials.make_one(
            self.boto3_raw_data["Dynatrace"]
        )

    @cached_property
    def GoogleAnalytics(self):  # pragma: no cover
        return GoogleAnalyticsConnectorProfileCredentials.make_one(
            self.boto3_raw_data["GoogleAnalytics"]
        )

    @cached_property
    def Honeycode(self):  # pragma: no cover
        return HoneycodeConnectorProfileCredentials.make_one(
            self.boto3_raw_data["Honeycode"]
        )

    @cached_property
    def InforNexus(self):  # pragma: no cover
        return InforNexusConnectorProfileCredentials.make_one(
            self.boto3_raw_data["InforNexus"]
        )

    @cached_property
    def Marketo(self):  # pragma: no cover
        return MarketoConnectorProfileCredentials.make_one(
            self.boto3_raw_data["Marketo"]
        )

    @cached_property
    def Redshift(self):  # pragma: no cover
        return RedshiftConnectorProfileCredentials.make_one(
            self.boto3_raw_data["Redshift"]
        )

    @cached_property
    def Salesforce(self):  # pragma: no cover
        return SalesforceConnectorProfileCredentials.make_one(
            self.boto3_raw_data["Salesforce"]
        )

    @cached_property
    def ServiceNow(self):  # pragma: no cover
        return ServiceNowConnectorProfileCredentials.make_one(
            self.boto3_raw_data["ServiceNow"]
        )

    @cached_property
    def Singular(self):  # pragma: no cover
        return SingularConnectorProfileCredentials.make_one(
            self.boto3_raw_data["Singular"]
        )

    @cached_property
    def Slack(self):  # pragma: no cover
        return SlackConnectorProfileCredentials.make_one(self.boto3_raw_data["Slack"])

    @cached_property
    def Snowflake(self):  # pragma: no cover
        return SnowflakeConnectorProfileCredentials.make_one(
            self.boto3_raw_data["Snowflake"]
        )

    @cached_property
    def Trendmicro(self):  # pragma: no cover
        return TrendmicroConnectorProfileCredentials.make_one(
            self.boto3_raw_data["Trendmicro"]
        )

    @cached_property
    def Veeva(self):  # pragma: no cover
        return VeevaConnectorProfileCredentials.make_one(self.boto3_raw_data["Veeva"])

    @cached_property
    def Zendesk(self):  # pragma: no cover
        return ZendeskConnectorProfileCredentials.make_one(
            self.boto3_raw_data["Zendesk"]
        )

    @cached_property
    def SAPOData(self):  # pragma: no cover
        return SAPODataConnectorProfileCredentials.make_one(
            self.boto3_raw_data["SAPOData"]
        )

    @cached_property
    def CustomConnector(self):  # pragma: no cover
        return CustomConnectorProfileCredentials.make_one(
            self.boto3_raw_data["CustomConnector"]
        )

    @cached_property
    def Pardot(self):  # pragma: no cover
        return PardotConnectorProfileCredentials.make_one(self.boto3_raw_data["Pardot"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectorProfileCredentialsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectorProfileCredentialsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectorEntityField:
    boto3_raw_data: "type_defs.ConnectorEntityFieldTypeDef" = dataclasses.field()

    identifier = field("identifier")
    parentIdentifier = field("parentIdentifier")
    label = field("label")
    isPrimaryKey = field("isPrimaryKey")
    defaultValue = field("defaultValue")
    isDeprecated = field("isDeprecated")

    @cached_property
    def supportedFieldTypeDetails(self):  # pragma: no cover
        return SupportedFieldTypeDetails.make_one(
            self.boto3_raw_data["supportedFieldTypeDetails"]
        )

    description = field("description")

    @cached_property
    def sourceProperties(self):  # pragma: no cover
        return SourceFieldProperties.make_one(self.boto3_raw_data["sourceProperties"])

    @cached_property
    def destinationProperties(self):  # pragma: no cover
        return DestinationFieldProperties.make_one(
            self.boto3_raw_data["destinationProperties"]
        )

    customProperties = field("customProperties")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectorEntityFieldTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectorEntityFieldTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFlowExecutionRecordsResponse:
    boto3_raw_data: "type_defs.DescribeFlowExecutionRecordsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def flowExecutions(self):  # pragma: no cover
        return ExecutionRecord.make_many(self.boto3_raw_data["flowExecutions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFlowExecutionRecordsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFlowExecutionRecordsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectorConfiguration:
    boto3_raw_data: "type_defs.ConnectorConfigurationTypeDef" = dataclasses.field()

    canUseAsSource = field("canUseAsSource")
    canUseAsDestination = field("canUseAsDestination")
    supportedDestinationConnectors = field("supportedDestinationConnectors")
    supportedSchedulingFrequencies = field("supportedSchedulingFrequencies")
    isPrivateLinkEnabled = field("isPrivateLinkEnabled")
    isPrivateLinkEndpointUrlRequired = field("isPrivateLinkEndpointUrlRequired")
    supportedTriggerTypes = field("supportedTriggerTypes")

    @cached_property
    def connectorMetadata(self):  # pragma: no cover
        return ConnectorMetadata.make_one(self.boto3_raw_data["connectorMetadata"])

    connectorType = field("connectorType")
    connectorLabel = field("connectorLabel")
    connectorDescription = field("connectorDescription")
    connectorOwner = field("connectorOwner")
    connectorName = field("connectorName")
    connectorVersion = field("connectorVersion")
    connectorArn = field("connectorArn")
    connectorModes = field("connectorModes")

    @cached_property
    def authenticationConfig(self):  # pragma: no cover
        return AuthenticationConfig.make_one(
            self.boto3_raw_data["authenticationConfig"]
        )

    @cached_property
    def connectorRuntimeSettings(self):  # pragma: no cover
        return ConnectorRuntimeSetting.make_many(
            self.boto3_raw_data["connectorRuntimeSettings"]
        )

    supportedApiVersions = field("supportedApiVersions")
    supportedOperators = field("supportedOperators")
    supportedWriteOperations = field("supportedWriteOperations")
    connectorProvisioningType = field("connectorProvisioningType")

    @cached_property
    def connectorProvisioningConfig(self):  # pragma: no cover
        return ConnectorProvisioningConfig.make_one(
            self.boto3_raw_data["connectorProvisioningConfig"]
        )

    logoURL = field("logoURL")
    registeredAt = field("registeredAt")
    registeredBy = field("registeredBy")
    supportedDataTransferTypes = field("supportedDataTransferTypes")

    @cached_property
    def supportedDataTransferApis(self):  # pragma: no cover
        return DataTransferApi.make_many(
            self.boto3_raw_data["supportedDataTransferApis"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectorConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectorConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectorProfile:
    boto3_raw_data: "type_defs.ConnectorProfileTypeDef" = dataclasses.field()

    connectorProfileArn = field("connectorProfileArn")
    connectorProfileName = field("connectorProfileName")
    connectorType = field("connectorType")
    connectorLabel = field("connectorLabel")
    connectionMode = field("connectionMode")
    credentialsArn = field("credentialsArn")

    @cached_property
    def connectorProfileProperties(self):  # pragma: no cover
        return ConnectorProfilePropertiesOutput.make_one(
            self.boto3_raw_data["connectorProfileProperties"]
        )

    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")

    @cached_property
    def privateConnectionProvisioningState(self):  # pragma: no cover
        return PrivateConnectionProvisioningState.make_one(
            self.boto3_raw_data["privateConnectionProvisioningState"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectorProfileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectorProfileTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationConnectorPropertiesOutput:
    boto3_raw_data: "type_defs.DestinationConnectorPropertiesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Redshift(self):  # pragma: no cover
        return RedshiftDestinationProperties.make_one(self.boto3_raw_data["Redshift"])

    @cached_property
    def S3(self):  # pragma: no cover
        return S3DestinationPropertiesOutput.make_one(self.boto3_raw_data["S3"])

    @cached_property
    def Salesforce(self):  # pragma: no cover
        return SalesforceDestinationPropertiesOutput.make_one(
            self.boto3_raw_data["Salesforce"]
        )

    @cached_property
    def Snowflake(self):  # pragma: no cover
        return SnowflakeDestinationProperties.make_one(self.boto3_raw_data["Snowflake"])

    @cached_property
    def EventBridge(self):  # pragma: no cover
        return EventBridgeDestinationProperties.make_one(
            self.boto3_raw_data["EventBridge"]
        )

    LookoutMetrics = field("LookoutMetrics")

    @cached_property
    def Upsolver(self):  # pragma: no cover
        return UpsolverDestinationPropertiesOutput.make_one(
            self.boto3_raw_data["Upsolver"]
        )

    @cached_property
    def Honeycode(self):  # pragma: no cover
        return HoneycodeDestinationProperties.make_one(self.boto3_raw_data["Honeycode"])

    @cached_property
    def CustomerProfiles(self):  # pragma: no cover
        return CustomerProfilesDestinationProperties.make_one(
            self.boto3_raw_data["CustomerProfiles"]
        )

    @cached_property
    def Zendesk(self):  # pragma: no cover
        return ZendeskDestinationPropertiesOutput.make_one(
            self.boto3_raw_data["Zendesk"]
        )

    @cached_property
    def Marketo(self):  # pragma: no cover
        return MarketoDestinationProperties.make_one(self.boto3_raw_data["Marketo"])

    @cached_property
    def CustomConnector(self):  # pragma: no cover
        return CustomConnectorDestinationPropertiesOutput.make_one(
            self.boto3_raw_data["CustomConnector"]
        )

    @cached_property
    def SAPOData(self):  # pragma: no cover
        return SAPODataDestinationPropertiesOutput.make_one(
            self.boto3_raw_data["SAPOData"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DestinationConnectorPropertiesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationConnectorPropertiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceFlowConfigOutput:
    boto3_raw_data: "type_defs.SourceFlowConfigOutputTypeDef" = dataclasses.field()

    connectorType = field("connectorType")

    @cached_property
    def sourceConnectorProperties(self):  # pragma: no cover
        return SourceConnectorPropertiesOutput.make_one(
            self.boto3_raw_data["sourceConnectorProperties"]
        )

    apiVersion = field("apiVersion")
    connectorProfileName = field("connectorProfileName")

    @cached_property
    def incrementalPullConfig(self):  # pragma: no cover
        return IncrementalPullConfig.make_one(
            self.boto3_raw_data["incrementalPullConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceFlowConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceFlowConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceFlowConfig:
    boto3_raw_data: "type_defs.SourceFlowConfigTypeDef" = dataclasses.field()

    connectorType = field("connectorType")

    @cached_property
    def sourceConnectorProperties(self):  # pragma: no cover
        return SourceConnectorProperties.make_one(
            self.boto3_raw_data["sourceConnectorProperties"]
        )

    apiVersion = field("apiVersion")
    connectorProfileName = field("connectorProfileName")

    @cached_property
    def incrementalPullConfig(self):  # pragma: no cover
        return IncrementalPullConfig.make_one(
            self.boto3_raw_data["incrementalPullConfig"]
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

    triggerType = field("triggerType")

    @cached_property
    def triggerProperties(self):  # pragma: no cover
        return TriggerProperties.make_one(self.boto3_raw_data["triggerProperties"])

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
class DescribeConnectorEntityResponse:
    boto3_raw_data: "type_defs.DescribeConnectorEntityResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def connectorEntityFields(self):  # pragma: no cover
        return ConnectorEntityField.make_many(
            self.boto3_raw_data["connectorEntityFields"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeConnectorEntityResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectorEntityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectorResponse:
    boto3_raw_data: "type_defs.DescribeConnectorResponseTypeDef" = dataclasses.field()

    @cached_property
    def connectorConfiguration(self):  # pragma: no cover
        return ConnectorConfiguration.make_one(
            self.boto3_raw_data["connectorConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeConnectorResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectorsResponse:
    boto3_raw_data: "type_defs.DescribeConnectorsResponseTypeDef" = dataclasses.field()

    connectorConfigurations = field("connectorConfigurations")

    @cached_property
    def connectors(self):  # pragma: no cover
        return ConnectorDetail.make_many(self.boto3_raw_data["connectors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeConnectorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConnectorProfilesResponse:
    boto3_raw_data: "type_defs.DescribeConnectorProfilesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def connectorProfileDetails(self):  # pragma: no cover
        return ConnectorProfile.make_many(
            self.boto3_raw_data["connectorProfileDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConnectorProfilesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConnectorProfilesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectorProfileProperties:
    boto3_raw_data: "type_defs.ConnectorProfilePropertiesTypeDef" = dataclasses.field()

    Amplitude = field("Amplitude")

    @cached_property
    def Datadog(self):  # pragma: no cover
        return DatadogConnectorProfileProperties.make_one(
            self.boto3_raw_data["Datadog"]
        )

    @cached_property
    def Dynatrace(self):  # pragma: no cover
        return DynatraceConnectorProfileProperties.make_one(
            self.boto3_raw_data["Dynatrace"]
        )

    GoogleAnalytics = field("GoogleAnalytics")
    Honeycode = field("Honeycode")

    @cached_property
    def InforNexus(self):  # pragma: no cover
        return InforNexusConnectorProfileProperties.make_one(
            self.boto3_raw_data["InforNexus"]
        )

    @cached_property
    def Marketo(self):  # pragma: no cover
        return MarketoConnectorProfileProperties.make_one(
            self.boto3_raw_data["Marketo"]
        )

    @cached_property
    def Redshift(self):  # pragma: no cover
        return RedshiftConnectorProfileProperties.make_one(
            self.boto3_raw_data["Redshift"]
        )

    @cached_property
    def Salesforce(self):  # pragma: no cover
        return SalesforceConnectorProfileProperties.make_one(
            self.boto3_raw_data["Salesforce"]
        )

    @cached_property
    def ServiceNow(self):  # pragma: no cover
        return ServiceNowConnectorProfileProperties.make_one(
            self.boto3_raw_data["ServiceNow"]
        )

    Singular = field("Singular")

    @cached_property
    def Slack(self):  # pragma: no cover
        return SlackConnectorProfileProperties.make_one(self.boto3_raw_data["Slack"])

    @cached_property
    def Snowflake(self):  # pragma: no cover
        return SnowflakeConnectorProfileProperties.make_one(
            self.boto3_raw_data["Snowflake"]
        )

    Trendmicro = field("Trendmicro")

    @cached_property
    def Veeva(self):  # pragma: no cover
        return VeevaConnectorProfileProperties.make_one(self.boto3_raw_data["Veeva"])

    @cached_property
    def Zendesk(self):  # pragma: no cover
        return ZendeskConnectorProfileProperties.make_one(
            self.boto3_raw_data["Zendesk"]
        )

    SAPOData = field("SAPOData")
    CustomConnector = field("CustomConnector")

    @cached_property
    def Pardot(self):  # pragma: no cover
        return PardotConnectorProfileProperties.make_one(self.boto3_raw_data["Pardot"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectorProfilePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectorProfilePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationFlowConfigOutput:
    boto3_raw_data: "type_defs.DestinationFlowConfigOutputTypeDef" = dataclasses.field()

    connectorType = field("connectorType")

    @cached_property
    def destinationConnectorProperties(self):  # pragma: no cover
        return DestinationConnectorPropertiesOutput.make_one(
            self.boto3_raw_data["destinationConnectorProperties"]
        )

    apiVersion = field("apiVersion")
    connectorProfileName = field("connectorProfileName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DestinationFlowConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationFlowConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DestinationProperties:
    boto3_raw_data: "type_defs.S3DestinationPropertiesTypeDef" = dataclasses.field()

    bucketName = field("bucketName")
    bucketPrefix = field("bucketPrefix")
    s3OutputFormatConfig = field("s3OutputFormatConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3DestinationPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3DestinationPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpsolverDestinationProperties:
    boto3_raw_data: "type_defs.UpsolverDestinationPropertiesTypeDef" = (
        dataclasses.field()
    )

    bucketName = field("bucketName")
    s3OutputFormatConfig = field("s3OutputFormatConfig")
    bucketPrefix = field("bucketPrefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpsolverDestinationPropertiesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpsolverDestinationPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFlowResponse:
    boto3_raw_data: "type_defs.DescribeFlowResponseTypeDef" = dataclasses.field()

    flowArn = field("flowArn")
    description = field("description")
    flowName = field("flowName")
    kmsArn = field("kmsArn")
    flowStatus = field("flowStatus")
    flowStatusMessage = field("flowStatusMessage")

    @cached_property
    def sourceFlowConfig(self):  # pragma: no cover
        return SourceFlowConfigOutput.make_one(self.boto3_raw_data["sourceFlowConfig"])

    @cached_property
    def destinationFlowConfigList(self):  # pragma: no cover
        return DestinationFlowConfigOutput.make_many(
            self.boto3_raw_data["destinationFlowConfigList"]
        )

    @cached_property
    def lastRunExecutionDetails(self):  # pragma: no cover
        return ExecutionDetails.make_one(self.boto3_raw_data["lastRunExecutionDetails"])

    @cached_property
    def triggerConfig(self):  # pragma: no cover
        return TriggerConfigOutput.make_one(self.boto3_raw_data["triggerConfig"])

    @cached_property
    def tasks(self):  # pragma: no cover
        return TaskOutput.make_many(self.boto3_raw_data["tasks"])

    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    createdBy = field("createdBy")
    lastUpdatedBy = field("lastUpdatedBy")
    tags = field("tags")

    @cached_property
    def metadataCatalogConfig(self):  # pragma: no cover
        return MetadataCatalogConfig.make_one(
            self.boto3_raw_data["metadataCatalogConfig"]
        )

    @cached_property
    def lastRunMetadataCatalogDetails(self):  # pragma: no cover
        return MetadataCatalogDetail.make_many(
            self.boto3_raw_data["lastRunMetadataCatalogDetails"]
        )

    schemaVersion = field("schemaVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFlowResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFlowResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectorProfileConfig:
    boto3_raw_data: "type_defs.ConnectorProfileConfigTypeDef" = dataclasses.field()

    connectorProfileProperties = field("connectorProfileProperties")

    @cached_property
    def connectorProfileCredentials(self):  # pragma: no cover
        return ConnectorProfileCredentials.make_one(
            self.boto3_raw_data["connectorProfileCredentials"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectorProfileConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectorProfileConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationConnectorProperties:
    boto3_raw_data: "type_defs.DestinationConnectorPropertiesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Redshift(self):  # pragma: no cover
        return RedshiftDestinationProperties.make_one(self.boto3_raw_data["Redshift"])

    S3 = field("S3")
    Salesforce = field("Salesforce")

    @cached_property
    def Snowflake(self):  # pragma: no cover
        return SnowflakeDestinationProperties.make_one(self.boto3_raw_data["Snowflake"])

    @cached_property
    def EventBridge(self):  # pragma: no cover
        return EventBridgeDestinationProperties.make_one(
            self.boto3_raw_data["EventBridge"]
        )

    LookoutMetrics = field("LookoutMetrics")
    Upsolver = field("Upsolver")

    @cached_property
    def Honeycode(self):  # pragma: no cover
        return HoneycodeDestinationProperties.make_one(self.boto3_raw_data["Honeycode"])

    @cached_property
    def CustomerProfiles(self):  # pragma: no cover
        return CustomerProfilesDestinationProperties.make_one(
            self.boto3_raw_data["CustomerProfiles"]
        )

    Zendesk = field("Zendesk")

    @cached_property
    def Marketo(self):  # pragma: no cover
        return MarketoDestinationProperties.make_one(self.boto3_raw_data["Marketo"])

    CustomConnector = field("CustomConnector")
    SAPOData = field("SAPOData")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DestinationConnectorPropertiesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationConnectorPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConnectorProfileRequest:
    boto3_raw_data: "type_defs.CreateConnectorProfileRequestTypeDef" = (
        dataclasses.field()
    )

    connectorProfileName = field("connectorProfileName")
    connectorType = field("connectorType")
    connectionMode = field("connectionMode")

    @cached_property
    def connectorProfileConfig(self):  # pragma: no cover
        return ConnectorProfileConfig.make_one(
            self.boto3_raw_data["connectorProfileConfig"]
        )

    kmsArn = field("kmsArn")
    connectorLabel = field("connectorLabel")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateConnectorProfileRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConnectorProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConnectorProfileRequest:
    boto3_raw_data: "type_defs.UpdateConnectorProfileRequestTypeDef" = (
        dataclasses.field()
    )

    connectorProfileName = field("connectorProfileName")
    connectionMode = field("connectionMode")

    @cached_property
    def connectorProfileConfig(self):  # pragma: no cover
        return ConnectorProfileConfig.make_one(
            self.boto3_raw_data["connectorProfileConfig"]
        )

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateConnectorProfileRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConnectorProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DestinationFlowConfig:
    boto3_raw_data: "type_defs.DestinationFlowConfigTypeDef" = dataclasses.field()

    connectorType = field("connectorType")
    destinationConnectorProperties = field("destinationConnectorProperties")
    apiVersion = field("apiVersion")
    connectorProfileName = field("connectorProfileName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DestinationFlowConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DestinationFlowConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFlowRequest:
    boto3_raw_data: "type_defs.CreateFlowRequestTypeDef" = dataclasses.field()

    flowName = field("flowName")
    triggerConfig = field("triggerConfig")
    sourceFlowConfig = field("sourceFlowConfig")
    destinationFlowConfigList = field("destinationFlowConfigList")
    tasks = field("tasks")
    description = field("description")
    kmsArn = field("kmsArn")
    tags = field("tags")

    @cached_property
    def metadataCatalogConfig(self):  # pragma: no cover
        return MetadataCatalogConfig.make_one(
            self.boto3_raw_data["metadataCatalogConfig"]
        )

    clientToken = field("clientToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateFlowRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFlowRequest:
    boto3_raw_data: "type_defs.UpdateFlowRequestTypeDef" = dataclasses.field()

    flowName = field("flowName")
    triggerConfig = field("triggerConfig")
    sourceFlowConfig = field("sourceFlowConfig")
    destinationFlowConfigList = field("destinationFlowConfigList")
    tasks = field("tasks")
    description = field("description")

    @cached_property
    def metadataCatalogConfig(self):  # pragma: no cover
        return MetadataCatalogConfig.make_one(
            self.boto3_raw_data["metadataCatalogConfig"]
        )

    clientToken = field("clientToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateFlowRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFlowRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
