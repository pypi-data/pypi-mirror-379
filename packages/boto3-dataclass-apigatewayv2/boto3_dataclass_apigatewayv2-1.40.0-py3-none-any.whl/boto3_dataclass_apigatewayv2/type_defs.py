# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_apigatewayv2 import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccessLogSettings:
    boto3_raw_data: "type_defs.AccessLogSettingsTypeDef" = dataclasses.field()

    DestinationArn = field("DestinationArn")
    Format = field("Format")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessLogSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessLogSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApiMapping:
    boto3_raw_data: "type_defs.ApiMappingTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    Stage = field("Stage")
    ApiMappingId = field("ApiMappingId")
    ApiMappingKey = field("ApiMappingKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApiMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApiMappingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CorsOutput:
    boto3_raw_data: "type_defs.CorsOutputTypeDef" = dataclasses.field()

    AllowCredentials = field("AllowCredentials")
    AllowHeaders = field("AllowHeaders")
    AllowMethods = field("AllowMethods")
    AllowOrigins = field("AllowOrigins")
    ExposeHeaders = field("ExposeHeaders")
    MaxAge = field("MaxAge")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CorsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CorsOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JWTConfigurationOutput:
    boto3_raw_data: "type_defs.JWTConfigurationOutputTypeDef" = dataclasses.field()

    Audience = field("Audience")
    Issuer = field("Issuer")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JWTConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JWTConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Cors:
    boto3_raw_data: "type_defs.CorsTypeDef" = dataclasses.field()

    AllowCredentials = field("AllowCredentials")
    AllowHeaders = field("AllowHeaders")
    AllowMethods = field("AllowMethods")
    AllowOrigins = field("AllowOrigins")
    ExposeHeaders = field("ExposeHeaders")
    MaxAge = field("MaxAge")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CorsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CorsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApiMappingRequest:
    boto3_raw_data: "type_defs.CreateApiMappingRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    DomainName = field("DomainName")
    Stage = field("Stage")
    ApiMappingKey = field("ApiMappingKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApiMappingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApiMappingRequestTypeDef"]
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
class CreateDeploymentRequest:
    boto3_raw_data: "type_defs.CreateDeploymentRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    Description = field("Description")
    StageName = field("StageName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeploymentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MutualTlsAuthenticationInput:
    boto3_raw_data: "type_defs.MutualTlsAuthenticationInputTypeDef" = (
        dataclasses.field()
    )

    TruststoreUri = field("TruststoreUri")
    TruststoreVersion = field("TruststoreVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MutualTlsAuthenticationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MutualTlsAuthenticationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainNameConfigurationOutput:
    boto3_raw_data: "type_defs.DomainNameConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    ApiGatewayDomainName = field("ApiGatewayDomainName")
    CertificateArn = field("CertificateArn")
    CertificateName = field("CertificateName")
    CertificateUploadDate = field("CertificateUploadDate")
    DomainNameStatus = field("DomainNameStatus")
    DomainNameStatusMessage = field("DomainNameStatusMessage")
    EndpointType = field("EndpointType")
    HostedZoneId = field("HostedZoneId")
    IpAddressType = field("IpAddressType")
    SecurityPolicy = field("SecurityPolicy")
    OwnershipVerificationCertificateArn = field("OwnershipVerificationCertificateArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DomainNameConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainNameConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MutualTlsAuthentication:
    boto3_raw_data: "type_defs.MutualTlsAuthenticationTypeDef" = dataclasses.field()

    TruststoreUri = field("TruststoreUri")
    TruststoreVersion = field("TruststoreVersion")
    TruststoreWarnings = field("TruststoreWarnings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MutualTlsAuthenticationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MutualTlsAuthenticationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TlsConfigInput:
    boto3_raw_data: "type_defs.TlsConfigInputTypeDef" = dataclasses.field()

    ServerNameToVerify = field("ServerNameToVerify")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TlsConfigInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TlsConfigInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIntegrationResponseRequest:
    boto3_raw_data: "type_defs.CreateIntegrationResponseRequestTypeDef" = (
        dataclasses.field()
    )

    ApiId = field("ApiId")
    IntegrationId = field("IntegrationId")
    IntegrationResponseKey = field("IntegrationResponseKey")
    ContentHandlingStrategy = field("ContentHandlingStrategy")
    ResponseParameters = field("ResponseParameters")
    ResponseTemplates = field("ResponseTemplates")
    TemplateSelectionExpression = field("TemplateSelectionExpression")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateIntegrationResponseRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIntegrationResponseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TlsConfig:
    boto3_raw_data: "type_defs.TlsConfigTypeDef" = dataclasses.field()

    ServerNameToVerify = field("ServerNameToVerify")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TlsConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TlsConfigTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateModelRequest:
    boto3_raw_data: "type_defs.CreateModelRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    Name = field("Name")
    Schema = field("Schema")
    ContentType = field("ContentType")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterConstraints:
    boto3_raw_data: "type_defs.ParameterConstraintsTypeDef" = dataclasses.field()

    Required = field("Required")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParameterConstraintsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParameterConstraintsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteSettings:
    boto3_raw_data: "type_defs.RouteSettingsTypeDef" = dataclasses.field()

    DataTraceEnabled = field("DataTraceEnabled")
    DetailedMetricsEnabled = field("DetailedMetricsEnabled")
    LoggingLevel = field("LoggingLevel")
    ThrottlingBurstLimit = field("ThrottlingBurstLimit")
    ThrottlingRateLimit = field("ThrottlingRateLimit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVpcLinkRequest:
    boto3_raw_data: "type_defs.CreateVpcLinkRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    SubnetIds = field("SubnetIds")
    SecurityGroupIds = field("SecurityGroupIds")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVpcLinkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVpcLinkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccessLogSettingsRequest:
    boto3_raw_data: "type_defs.DeleteAccessLogSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    ApiId = field("ApiId")
    StageName = field("StageName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteAccessLogSettingsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccessLogSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApiMappingRequest:
    boto3_raw_data: "type_defs.DeleteApiMappingRequestTypeDef" = dataclasses.field()

    ApiMappingId = field("ApiMappingId")
    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteApiMappingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApiMappingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApiRequest:
    boto3_raw_data: "type_defs.DeleteApiRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteApiRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAuthorizerRequest:
    boto3_raw_data: "type_defs.DeleteAuthorizerRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    AuthorizerId = field("AuthorizerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAuthorizerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAuthorizerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCorsConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteCorsConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ApiId = field("ApiId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteCorsConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCorsConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDeploymentRequest:
    boto3_raw_data: "type_defs.DeleteDeploymentRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    DeploymentId = field("DeploymentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDeploymentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainNameRequest:
    boto3_raw_data: "type_defs.DeleteDomainNameRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDomainNameRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainNameRequestTypeDef"]
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

    ApiId = field("ApiId")
    IntegrationId = field("IntegrationId")

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
class DeleteIntegrationResponseRequest:
    boto3_raw_data: "type_defs.DeleteIntegrationResponseRequestTypeDef" = (
        dataclasses.field()
    )

    ApiId = field("ApiId")
    IntegrationId = field("IntegrationId")
    IntegrationResponseId = field("IntegrationResponseId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteIntegrationResponseRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIntegrationResponseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteModelRequest:
    boto3_raw_data: "type_defs.DeleteModelRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    ModelId = field("ModelId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRouteRequestParameterRequest:
    boto3_raw_data: "type_defs.DeleteRouteRequestParameterRequestTypeDef" = (
        dataclasses.field()
    )

    ApiId = field("ApiId")
    RequestParameterKey = field("RequestParameterKey")
    RouteId = field("RouteId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteRouteRequestParameterRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRouteRequestParameterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRouteRequest:
    boto3_raw_data: "type_defs.DeleteRouteRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    RouteId = field("RouteId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRouteRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRouteRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRouteResponseRequest:
    boto3_raw_data: "type_defs.DeleteRouteResponseRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    RouteId = field("RouteId")
    RouteResponseId = field("RouteResponseId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRouteResponseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRouteResponseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRouteSettingsRequest:
    boto3_raw_data: "type_defs.DeleteRouteSettingsRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    RouteKey = field("RouteKey")
    StageName = field("StageName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRouteSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRouteSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRoutingRuleRequest:
    boto3_raw_data: "type_defs.DeleteRoutingRuleRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    RoutingRuleId = field("RoutingRuleId")
    DomainNameId = field("DomainNameId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRoutingRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRoutingRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStageRequest:
    boto3_raw_data: "type_defs.DeleteStageRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    StageName = field("StageName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteStageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVpcLinkRequest:
    boto3_raw_data: "type_defs.DeleteVpcLinkRequestTypeDef" = dataclasses.field()

    VpcLinkId = field("VpcLinkId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVpcLinkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVpcLinkRequestTypeDef"]
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

    AutoDeployed = field("AutoDeployed")
    CreatedDate = field("CreatedDate")
    DeploymentId = field("DeploymentId")
    DeploymentStatus = field("DeploymentStatus")
    DeploymentStatusMessage = field("DeploymentStatusMessage")
    Description = field("Description")

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
class ExportApiRequest:
    boto3_raw_data: "type_defs.ExportApiRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    OutputType = field("OutputType")
    Specification = field("Specification")
    ExportVersion = field("ExportVersion")
    IncludeExtensions = field("IncludeExtensions")
    StageName = field("StageName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportApiRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportApiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApiMappingRequest:
    boto3_raw_data: "type_defs.GetApiMappingRequestTypeDef" = dataclasses.field()

    ApiMappingId = field("ApiMappingId")
    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApiMappingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApiMappingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApiMappingsRequest:
    boto3_raw_data: "type_defs.GetApiMappingsRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApiMappingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApiMappingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApiRequest:
    boto3_raw_data: "type_defs.GetApiRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetApiRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetApiRequestTypeDef"]],
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
class GetApisRequest:
    boto3_raw_data: "type_defs.GetApisRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetApisRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetApisRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAuthorizerRequest:
    boto3_raw_data: "type_defs.GetAuthorizerRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    AuthorizerId = field("AuthorizerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAuthorizerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAuthorizerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAuthorizersRequest:
    boto3_raw_data: "type_defs.GetAuthorizersRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAuthorizersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAuthorizersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentRequest:
    boto3_raw_data: "type_defs.GetDeploymentRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    DeploymentId = field("DeploymentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentsRequest:
    boto3_raw_data: "type_defs.GetDeploymentsRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainNameRequest:
    boto3_raw_data: "type_defs.GetDomainNameRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDomainNameRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainNameRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainNamesRequest:
    boto3_raw_data: "type_defs.GetDomainNamesRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDomainNamesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainNamesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIntegrationRequest:
    boto3_raw_data: "type_defs.GetIntegrationRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    IntegrationId = field("IntegrationId")

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
class GetIntegrationResponseRequest:
    boto3_raw_data: "type_defs.GetIntegrationResponseRequestTypeDef" = (
        dataclasses.field()
    )

    ApiId = field("ApiId")
    IntegrationId = field("IntegrationId")
    IntegrationResponseId = field("IntegrationResponseId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetIntegrationResponseRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIntegrationResponseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIntegrationResponsesRequest:
    boto3_raw_data: "type_defs.GetIntegrationResponsesRequestTypeDef" = (
        dataclasses.field()
    )

    ApiId = field("ApiId")
    IntegrationId = field("IntegrationId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetIntegrationResponsesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIntegrationResponsesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntegrationResponse:
    boto3_raw_data: "type_defs.IntegrationResponseTypeDef" = dataclasses.field()

    IntegrationResponseKey = field("IntegrationResponseKey")
    ContentHandlingStrategy = field("ContentHandlingStrategy")
    IntegrationResponseId = field("IntegrationResponseId")
    ResponseParameters = field("ResponseParameters")
    ResponseTemplates = field("ResponseTemplates")
    TemplateSelectionExpression = field("TemplateSelectionExpression")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IntegrationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntegrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIntegrationsRequest:
    boto3_raw_data: "type_defs.GetIntegrationsRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIntegrationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIntegrationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelRequest:
    boto3_raw_data: "type_defs.GetModelRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    ModelId = field("ModelId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetModelRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetModelRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelTemplateRequest:
    boto3_raw_data: "type_defs.GetModelTemplateRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    ModelId = field("ModelId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetModelTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetModelTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelsRequest:
    boto3_raw_data: "type_defs.GetModelsRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetModelsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetModelsRequestTypeDef"]
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

    Name = field("Name")
    ContentType = field("ContentType")
    Description = field("Description")
    ModelId = field("ModelId")
    Schema = field("Schema")

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
class GetRouteRequest:
    boto3_raw_data: "type_defs.GetRouteRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    RouteId = field("RouteId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRouteRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetRouteRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRouteResponseRequest:
    boto3_raw_data: "type_defs.GetRouteResponseRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    RouteId = field("RouteId")
    RouteResponseId = field("RouteResponseId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRouteResponseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRouteResponseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRouteResponsesRequest:
    boto3_raw_data: "type_defs.GetRouteResponsesRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    RouteId = field("RouteId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRouteResponsesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRouteResponsesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRoutesRequest:
    boto3_raw_data: "type_defs.GetRoutesRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRoutesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRoutesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRoutingRuleRequest:
    boto3_raw_data: "type_defs.GetRoutingRuleRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    RoutingRuleId = field("RoutingRuleId")
    DomainNameId = field("DomainNameId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRoutingRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRoutingRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStageRequest:
    boto3_raw_data: "type_defs.GetStageRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    StageName = field("StageName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetStageRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetStageRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStagesRequest:
    boto3_raw_data: "type_defs.GetStagesRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetStagesRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTagsRequest:
    boto3_raw_data: "type_defs.GetTagsRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTagsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetTagsRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVpcLinkRequest:
    boto3_raw_data: "type_defs.GetVpcLinkRequestTypeDef" = dataclasses.field()

    VpcLinkId = field("VpcLinkId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetVpcLinkRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVpcLinkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVpcLinksRequest:
    boto3_raw_data: "type_defs.GetVpcLinksRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVpcLinksRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVpcLinksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcLink:
    boto3_raw_data: "type_defs.VpcLinkTypeDef" = dataclasses.field()

    Name = field("Name")
    SecurityGroupIds = field("SecurityGroupIds")
    SubnetIds = field("SubnetIds")
    VpcLinkId = field("VpcLinkId")
    CreatedDate = field("CreatedDate")
    Tags = field("Tags")
    VpcLinkStatus = field("VpcLinkStatus")
    VpcLinkStatusMessage = field("VpcLinkStatusMessage")
    VpcLinkVersion = field("VpcLinkVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcLinkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VpcLinkTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportApiRequest:
    boto3_raw_data: "type_defs.ImportApiRequestTypeDef" = dataclasses.field()

    Body = field("Body")
    Basepath = field("Basepath")
    FailOnWarnings = field("FailOnWarnings")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportApiRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportApiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JWTConfiguration:
    boto3_raw_data: "type_defs.JWTConfigurationTypeDef" = dataclasses.field()

    Audience = field("Audience")
    Issuer = field("Issuer")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JWTConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JWTConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRoutingRulesRequest:
    boto3_raw_data: "type_defs.ListRoutingRulesRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    DomainNameId = field("DomainNameId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRoutingRulesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRoutingRulesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReimportApiRequest:
    boto3_raw_data: "type_defs.ReimportApiRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    Body = field("Body")
    Basepath = field("Basepath")
    FailOnWarnings = field("FailOnWarnings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReimportApiRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReimportApiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResetAuthorizersCacheRequest:
    boto3_raw_data: "type_defs.ResetAuthorizersCacheRequestTypeDef" = (
        dataclasses.field()
    )

    ApiId = field("ApiId")
    StageName = field("StageName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResetAuthorizersCacheRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResetAuthorizersCacheRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingRuleActionInvokeApi:
    boto3_raw_data: "type_defs.RoutingRuleActionInvokeApiTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    Stage = field("Stage")
    StripBasePath = field("StripBasePath")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutingRuleActionInvokeApiTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutingRuleActionInvokeApiTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingRuleMatchBasePathsOutput:
    boto3_raw_data: "type_defs.RoutingRuleMatchBasePathsOutputTypeDef" = (
        dataclasses.field()
    )

    AnyOf = field("AnyOf")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RoutingRuleMatchBasePathsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutingRuleMatchBasePathsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingRuleMatchBasePaths:
    boto3_raw_data: "type_defs.RoutingRuleMatchBasePathsTypeDef" = dataclasses.field()

    AnyOf = field("AnyOf")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutingRuleMatchBasePathsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutingRuleMatchBasePathsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingRuleMatchHeaderValue:
    boto3_raw_data: "type_defs.RoutingRuleMatchHeaderValueTypeDef" = dataclasses.field()

    Header = field("Header")
    ValueGlob = field("ValueGlob")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutingRuleMatchHeaderValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutingRuleMatchHeaderValueTypeDef"]
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
    Tags = field("Tags")

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
class UpdateApiMappingRequest:
    boto3_raw_data: "type_defs.UpdateApiMappingRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    ApiMappingId = field("ApiMappingId")
    DomainName = field("DomainName")
    ApiMappingKey = field("ApiMappingKey")
    Stage = field("Stage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApiMappingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApiMappingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDeploymentRequest:
    boto3_raw_data: "type_defs.UpdateDeploymentRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    DeploymentId = field("DeploymentId")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDeploymentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIntegrationResponseRequest:
    boto3_raw_data: "type_defs.UpdateIntegrationResponseRequestTypeDef" = (
        dataclasses.field()
    )

    ApiId = field("ApiId")
    IntegrationId = field("IntegrationId")
    IntegrationResponseId = field("IntegrationResponseId")
    ContentHandlingStrategy = field("ContentHandlingStrategy")
    IntegrationResponseKey = field("IntegrationResponseKey")
    ResponseParameters = field("ResponseParameters")
    ResponseTemplates = field("ResponseTemplates")
    TemplateSelectionExpression = field("TemplateSelectionExpression")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateIntegrationResponseRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIntegrationResponseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateModelRequest:
    boto3_raw_data: "type_defs.UpdateModelRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    ModelId = field("ModelId")
    ContentType = field("ContentType")
    Description = field("Description")
    Name = field("Name")
    Schema = field("Schema")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateModelRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateModelRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVpcLinkRequest:
    boto3_raw_data: "type_defs.UpdateVpcLinkRequestTypeDef" = dataclasses.field()

    VpcLinkId = field("VpcLinkId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVpcLinkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVpcLinkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Api:
    boto3_raw_data: "type_defs.ApiTypeDef" = dataclasses.field()

    Name = field("Name")
    ProtocolType = field("ProtocolType")
    RouteSelectionExpression = field("RouteSelectionExpression")
    ApiEndpoint = field("ApiEndpoint")
    ApiGatewayManaged = field("ApiGatewayManaged")
    ApiId = field("ApiId")
    ApiKeySelectionExpression = field("ApiKeySelectionExpression")

    @cached_property
    def CorsConfiguration(self):  # pragma: no cover
        return CorsOutput.make_one(self.boto3_raw_data["CorsConfiguration"])

    CreatedDate = field("CreatedDate")
    Description = field("Description")
    DisableSchemaValidation = field("DisableSchemaValidation")
    DisableExecuteApiEndpoint = field("DisableExecuteApiEndpoint")
    ImportInfo = field("ImportInfo")
    IpAddressType = field("IpAddressType")
    Tags = field("Tags")
    Version = field("Version")
    Warnings = field("Warnings")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApiTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApiTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Authorizer:
    boto3_raw_data: "type_defs.AuthorizerTypeDef" = dataclasses.field()

    Name = field("Name")
    AuthorizerCredentialsArn = field("AuthorizerCredentialsArn")
    AuthorizerId = field("AuthorizerId")
    AuthorizerPayloadFormatVersion = field("AuthorizerPayloadFormatVersion")
    AuthorizerResultTtlInSeconds = field("AuthorizerResultTtlInSeconds")
    AuthorizerType = field("AuthorizerType")
    AuthorizerUri = field("AuthorizerUri")
    EnableSimpleResponses = field("EnableSimpleResponses")
    IdentitySource = field("IdentitySource")
    IdentityValidationExpression = field("IdentityValidationExpression")

    @cached_property
    def JwtConfiguration(self):  # pragma: no cover
        return JWTConfigurationOutput.make_one(self.boto3_raw_data["JwtConfiguration"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AuthorizerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AuthorizerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApiMappingResponse:
    boto3_raw_data: "type_defs.CreateApiMappingResponseTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    ApiMappingId = field("ApiMappingId")
    ApiMappingKey = field("ApiMappingKey")
    Stage = field("Stage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApiMappingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApiMappingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApiResponse:
    boto3_raw_data: "type_defs.CreateApiResponseTypeDef" = dataclasses.field()

    ApiEndpoint = field("ApiEndpoint")
    ApiGatewayManaged = field("ApiGatewayManaged")
    ApiId = field("ApiId")
    ApiKeySelectionExpression = field("ApiKeySelectionExpression")

    @cached_property
    def CorsConfiguration(self):  # pragma: no cover
        return CorsOutput.make_one(self.boto3_raw_data["CorsConfiguration"])

    CreatedDate = field("CreatedDate")
    Description = field("Description")
    DisableSchemaValidation = field("DisableSchemaValidation")
    DisableExecuteApiEndpoint = field("DisableExecuteApiEndpoint")
    ImportInfo = field("ImportInfo")
    IpAddressType = field("IpAddressType")
    Name = field("Name")
    ProtocolType = field("ProtocolType")
    RouteSelectionExpression = field("RouteSelectionExpression")
    Tags = field("Tags")
    Version = field("Version")
    Warnings = field("Warnings")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateApiResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApiResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAuthorizerResponse:
    boto3_raw_data: "type_defs.CreateAuthorizerResponseTypeDef" = dataclasses.field()

    AuthorizerCredentialsArn = field("AuthorizerCredentialsArn")
    AuthorizerId = field("AuthorizerId")
    AuthorizerPayloadFormatVersion = field("AuthorizerPayloadFormatVersion")
    AuthorizerResultTtlInSeconds = field("AuthorizerResultTtlInSeconds")
    AuthorizerType = field("AuthorizerType")
    AuthorizerUri = field("AuthorizerUri")
    EnableSimpleResponses = field("EnableSimpleResponses")
    IdentitySource = field("IdentitySource")
    IdentityValidationExpression = field("IdentityValidationExpression")

    @cached_property
    def JwtConfiguration(self):  # pragma: no cover
        return JWTConfigurationOutput.make_one(self.boto3_raw_data["JwtConfiguration"])

    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAuthorizerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAuthorizerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeploymentResponse:
    boto3_raw_data: "type_defs.CreateDeploymentResponseTypeDef" = dataclasses.field()

    AutoDeployed = field("AutoDeployed")
    CreatedDate = field("CreatedDate")
    DeploymentId = field("DeploymentId")
    DeploymentStatus = field("DeploymentStatus")
    DeploymentStatusMessage = field("DeploymentStatusMessage")
    Description = field("Description")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeploymentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeploymentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIntegrationResponseResponse:
    boto3_raw_data: "type_defs.CreateIntegrationResponseResponseTypeDef" = (
        dataclasses.field()
    )

    ContentHandlingStrategy = field("ContentHandlingStrategy")
    IntegrationResponseId = field("IntegrationResponseId")
    IntegrationResponseKey = field("IntegrationResponseKey")
    ResponseParameters = field("ResponseParameters")
    ResponseTemplates = field("ResponseTemplates")
    TemplateSelectionExpression = field("TemplateSelectionExpression")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateIntegrationResponseResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIntegrationResponseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateModelResponse:
    boto3_raw_data: "type_defs.CreateModelResponseTypeDef" = dataclasses.field()

    ContentType = field("ContentType")
    Description = field("Description")
    ModelId = field("ModelId")
    Name = field("Name")
    Schema = field("Schema")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateModelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVpcLinkResponse:
    boto3_raw_data: "type_defs.CreateVpcLinkResponseTypeDef" = dataclasses.field()

    CreatedDate = field("CreatedDate")
    Name = field("Name")
    SecurityGroupIds = field("SecurityGroupIds")
    SubnetIds = field("SubnetIds")
    Tags = field("Tags")
    VpcLinkId = field("VpcLinkId")
    VpcLinkStatus = field("VpcLinkStatus")
    VpcLinkStatusMessage = field("VpcLinkStatusMessage")
    VpcLinkVersion = field("VpcLinkVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVpcLinkResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVpcLinkResponseTypeDef"]
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
class ExportApiResponse:
    boto3_raw_data: "type_defs.ExportApiResponseTypeDef" = dataclasses.field()

    body = field("body")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportApiResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportApiResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApiMappingResponse:
    boto3_raw_data: "type_defs.GetApiMappingResponseTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    ApiMappingId = field("ApiMappingId")
    ApiMappingKey = field("ApiMappingKey")
    Stage = field("Stage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApiMappingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApiMappingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApiMappingsResponse:
    boto3_raw_data: "type_defs.GetApiMappingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return ApiMapping.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApiMappingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApiMappingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApiResponse:
    boto3_raw_data: "type_defs.GetApiResponseTypeDef" = dataclasses.field()

    ApiEndpoint = field("ApiEndpoint")
    ApiGatewayManaged = field("ApiGatewayManaged")
    ApiId = field("ApiId")
    ApiKeySelectionExpression = field("ApiKeySelectionExpression")

    @cached_property
    def CorsConfiguration(self):  # pragma: no cover
        return CorsOutput.make_one(self.boto3_raw_data["CorsConfiguration"])

    CreatedDate = field("CreatedDate")
    Description = field("Description")
    DisableSchemaValidation = field("DisableSchemaValidation")
    DisableExecuteApiEndpoint = field("DisableExecuteApiEndpoint")
    ImportInfo = field("ImportInfo")
    IpAddressType = field("IpAddressType")
    Name = field("Name")
    ProtocolType = field("ProtocolType")
    RouteSelectionExpression = field("RouteSelectionExpression")
    Tags = field("Tags")
    Version = field("Version")
    Warnings = field("Warnings")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetApiResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetApiResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAuthorizerResponse:
    boto3_raw_data: "type_defs.GetAuthorizerResponseTypeDef" = dataclasses.field()

    AuthorizerCredentialsArn = field("AuthorizerCredentialsArn")
    AuthorizerId = field("AuthorizerId")
    AuthorizerPayloadFormatVersion = field("AuthorizerPayloadFormatVersion")
    AuthorizerResultTtlInSeconds = field("AuthorizerResultTtlInSeconds")
    AuthorizerType = field("AuthorizerType")
    AuthorizerUri = field("AuthorizerUri")
    EnableSimpleResponses = field("EnableSimpleResponses")
    IdentitySource = field("IdentitySource")
    IdentityValidationExpression = field("IdentityValidationExpression")

    @cached_property
    def JwtConfiguration(self):  # pragma: no cover
        return JWTConfigurationOutput.make_one(self.boto3_raw_data["JwtConfiguration"])

    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAuthorizerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAuthorizerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentResponse:
    boto3_raw_data: "type_defs.GetDeploymentResponseTypeDef" = dataclasses.field()

    AutoDeployed = field("AutoDeployed")
    CreatedDate = field("CreatedDate")
    DeploymentId = field("DeploymentId")
    DeploymentStatus = field("DeploymentStatus")
    DeploymentStatusMessage = field("DeploymentStatusMessage")
    Description = field("Description")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIntegrationResponseResponse:
    boto3_raw_data: "type_defs.GetIntegrationResponseResponseTypeDef" = (
        dataclasses.field()
    )

    ContentHandlingStrategy = field("ContentHandlingStrategy")
    IntegrationResponseId = field("IntegrationResponseId")
    IntegrationResponseKey = field("IntegrationResponseKey")
    ResponseParameters = field("ResponseParameters")
    ResponseTemplates = field("ResponseTemplates")
    TemplateSelectionExpression = field("TemplateSelectionExpression")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetIntegrationResponseResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIntegrationResponseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelResponse:
    boto3_raw_data: "type_defs.GetModelResponseTypeDef" = dataclasses.field()

    ContentType = field("ContentType")
    Description = field("Description")
    ModelId = field("ModelId")
    Name = field("Name")
    Schema = field("Schema")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetModelResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelTemplateResponse:
    boto3_raw_data: "type_defs.GetModelTemplateResponseTypeDef" = dataclasses.field()

    Value = field("Value")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetModelTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetModelTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTagsResponse:
    boto3_raw_data: "type_defs.GetTagsResponseTypeDef" = dataclasses.field()

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTagsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetTagsResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVpcLinkResponse:
    boto3_raw_data: "type_defs.GetVpcLinkResponseTypeDef" = dataclasses.field()

    CreatedDate = field("CreatedDate")
    Name = field("Name")
    SecurityGroupIds = field("SecurityGroupIds")
    SubnetIds = field("SubnetIds")
    Tags = field("Tags")
    VpcLinkId = field("VpcLinkId")
    VpcLinkStatus = field("VpcLinkStatus")
    VpcLinkStatusMessage = field("VpcLinkStatusMessage")
    VpcLinkVersion = field("VpcLinkVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVpcLinkResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVpcLinkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportApiResponse:
    boto3_raw_data: "type_defs.ImportApiResponseTypeDef" = dataclasses.field()

    ApiEndpoint = field("ApiEndpoint")
    ApiGatewayManaged = field("ApiGatewayManaged")
    ApiId = field("ApiId")
    ApiKeySelectionExpression = field("ApiKeySelectionExpression")

    @cached_property
    def CorsConfiguration(self):  # pragma: no cover
        return CorsOutput.make_one(self.boto3_raw_data["CorsConfiguration"])

    CreatedDate = field("CreatedDate")
    Description = field("Description")
    DisableSchemaValidation = field("DisableSchemaValidation")
    DisableExecuteApiEndpoint = field("DisableExecuteApiEndpoint")
    ImportInfo = field("ImportInfo")
    IpAddressType = field("IpAddressType")
    Name = field("Name")
    ProtocolType = field("ProtocolType")
    RouteSelectionExpression = field("RouteSelectionExpression")
    Tags = field("Tags")
    Version = field("Version")
    Warnings = field("Warnings")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ImportApiResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportApiResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReimportApiResponse:
    boto3_raw_data: "type_defs.ReimportApiResponseTypeDef" = dataclasses.field()

    ApiEndpoint = field("ApiEndpoint")
    ApiGatewayManaged = field("ApiGatewayManaged")
    ApiId = field("ApiId")
    ApiKeySelectionExpression = field("ApiKeySelectionExpression")

    @cached_property
    def CorsConfiguration(self):  # pragma: no cover
        return CorsOutput.make_one(self.boto3_raw_data["CorsConfiguration"])

    CreatedDate = field("CreatedDate")
    Description = field("Description")
    DisableSchemaValidation = field("DisableSchemaValidation")
    DisableExecuteApiEndpoint = field("DisableExecuteApiEndpoint")
    ImportInfo = field("ImportInfo")
    IpAddressType = field("IpAddressType")
    Name = field("Name")
    ProtocolType = field("ProtocolType")
    RouteSelectionExpression = field("RouteSelectionExpression")
    Tags = field("Tags")
    Version = field("Version")
    Warnings = field("Warnings")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReimportApiResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReimportApiResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApiMappingResponse:
    boto3_raw_data: "type_defs.UpdateApiMappingResponseTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    ApiMappingId = field("ApiMappingId")
    ApiMappingKey = field("ApiMappingKey")
    Stage = field("Stage")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApiMappingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApiMappingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApiResponse:
    boto3_raw_data: "type_defs.UpdateApiResponseTypeDef" = dataclasses.field()

    ApiEndpoint = field("ApiEndpoint")
    ApiGatewayManaged = field("ApiGatewayManaged")
    ApiId = field("ApiId")
    ApiKeySelectionExpression = field("ApiKeySelectionExpression")

    @cached_property
    def CorsConfiguration(self):  # pragma: no cover
        return CorsOutput.make_one(self.boto3_raw_data["CorsConfiguration"])

    CreatedDate = field("CreatedDate")
    Description = field("Description")
    DisableSchemaValidation = field("DisableSchemaValidation")
    DisableExecuteApiEndpoint = field("DisableExecuteApiEndpoint")
    ImportInfo = field("ImportInfo")
    IpAddressType = field("IpAddressType")
    Name = field("Name")
    ProtocolType = field("ProtocolType")
    RouteSelectionExpression = field("RouteSelectionExpression")
    Tags = field("Tags")
    Version = field("Version")
    Warnings = field("Warnings")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateApiResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApiResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAuthorizerResponse:
    boto3_raw_data: "type_defs.UpdateAuthorizerResponseTypeDef" = dataclasses.field()

    AuthorizerCredentialsArn = field("AuthorizerCredentialsArn")
    AuthorizerId = field("AuthorizerId")
    AuthorizerPayloadFormatVersion = field("AuthorizerPayloadFormatVersion")
    AuthorizerResultTtlInSeconds = field("AuthorizerResultTtlInSeconds")
    AuthorizerType = field("AuthorizerType")
    AuthorizerUri = field("AuthorizerUri")
    EnableSimpleResponses = field("EnableSimpleResponses")
    IdentitySource = field("IdentitySource")
    IdentityValidationExpression = field("IdentityValidationExpression")

    @cached_property
    def JwtConfiguration(self):  # pragma: no cover
        return JWTConfigurationOutput.make_one(self.boto3_raw_data["JwtConfiguration"])

    Name = field("Name")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAuthorizerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAuthorizerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDeploymentResponse:
    boto3_raw_data: "type_defs.UpdateDeploymentResponseTypeDef" = dataclasses.field()

    AutoDeployed = field("AutoDeployed")
    CreatedDate = field("CreatedDate")
    DeploymentId = field("DeploymentId")
    DeploymentStatus = field("DeploymentStatus")
    DeploymentStatusMessage = field("DeploymentStatusMessage")
    Description = field("Description")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDeploymentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDeploymentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIntegrationResponseResponse:
    boto3_raw_data: "type_defs.UpdateIntegrationResponseResponseTypeDef" = (
        dataclasses.field()
    )

    ContentHandlingStrategy = field("ContentHandlingStrategy")
    IntegrationResponseId = field("IntegrationResponseId")
    IntegrationResponseKey = field("IntegrationResponseKey")
    ResponseParameters = field("ResponseParameters")
    ResponseTemplates = field("ResponseTemplates")
    TemplateSelectionExpression = field("TemplateSelectionExpression")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateIntegrationResponseResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIntegrationResponseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateModelResponse:
    boto3_raw_data: "type_defs.UpdateModelResponseTypeDef" = dataclasses.field()

    ContentType = field("ContentType")
    Description = field("Description")
    ModelId = field("ModelId")
    Name = field("Name")
    Schema = field("Schema")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateModelResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateModelResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVpcLinkResponse:
    boto3_raw_data: "type_defs.UpdateVpcLinkResponseTypeDef" = dataclasses.field()

    CreatedDate = field("CreatedDate")
    Name = field("Name")
    SecurityGroupIds = field("SecurityGroupIds")
    SubnetIds = field("SubnetIds")
    Tags = field("Tags")
    VpcLinkId = field("VpcLinkId")
    VpcLinkStatus = field("VpcLinkStatus")
    VpcLinkStatusMessage = field("VpcLinkStatusMessage")
    VpcLinkVersion = field("VpcLinkVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVpcLinkResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVpcLinkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainNameResponse:
    boto3_raw_data: "type_defs.CreateDomainNameResponseTypeDef" = dataclasses.field()

    ApiMappingSelectionExpression = field("ApiMappingSelectionExpression")
    DomainName = field("DomainName")
    DomainNameArn = field("DomainNameArn")

    @cached_property
    def DomainNameConfigurations(self):  # pragma: no cover
        return DomainNameConfigurationOutput.make_many(
            self.boto3_raw_data["DomainNameConfigurations"]
        )

    @cached_property
    def MutualTlsAuthentication(self):  # pragma: no cover
        return MutualTlsAuthentication.make_one(
            self.boto3_raw_data["MutualTlsAuthentication"]
        )

    RoutingMode = field("RoutingMode")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDomainNameResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainNameResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainName:
    boto3_raw_data: "type_defs.DomainNameTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    ApiMappingSelectionExpression = field("ApiMappingSelectionExpression")
    DomainNameArn = field("DomainNameArn")

    @cached_property
    def DomainNameConfigurations(self):  # pragma: no cover
        return DomainNameConfigurationOutput.make_many(
            self.boto3_raw_data["DomainNameConfigurations"]
        )

    @cached_property
    def MutualTlsAuthentication(self):  # pragma: no cover
        return MutualTlsAuthentication.make_one(
            self.boto3_raw_data["MutualTlsAuthentication"]
        )

    RoutingMode = field("RoutingMode")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainNameTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainNameTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainNameResponse:
    boto3_raw_data: "type_defs.GetDomainNameResponseTypeDef" = dataclasses.field()

    ApiMappingSelectionExpression = field("ApiMappingSelectionExpression")
    DomainName = field("DomainName")
    DomainNameArn = field("DomainNameArn")

    @cached_property
    def DomainNameConfigurations(self):  # pragma: no cover
        return DomainNameConfigurationOutput.make_many(
            self.boto3_raw_data["DomainNameConfigurations"]
        )

    @cached_property
    def MutualTlsAuthentication(self):  # pragma: no cover
        return MutualTlsAuthentication.make_one(
            self.boto3_raw_data["MutualTlsAuthentication"]
        )

    RoutingMode = field("RoutingMode")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDomainNameResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainNameResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainNameResponse:
    boto3_raw_data: "type_defs.UpdateDomainNameResponseTypeDef" = dataclasses.field()

    ApiMappingSelectionExpression = field("ApiMappingSelectionExpression")
    DomainName = field("DomainName")
    DomainNameArn = field("DomainNameArn")

    @cached_property
    def DomainNameConfigurations(self):  # pragma: no cover
        return DomainNameConfigurationOutput.make_many(
            self.boto3_raw_data["DomainNameConfigurations"]
        )

    @cached_property
    def MutualTlsAuthentication(self):  # pragma: no cover
        return MutualTlsAuthentication.make_one(
            self.boto3_raw_data["MutualTlsAuthentication"]
        )

    RoutingMode = field("RoutingMode")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDomainNameResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainNameResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIntegrationRequest:
    boto3_raw_data: "type_defs.CreateIntegrationRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    IntegrationType = field("IntegrationType")
    ConnectionId = field("ConnectionId")
    ConnectionType = field("ConnectionType")
    ContentHandlingStrategy = field("ContentHandlingStrategy")
    CredentialsArn = field("CredentialsArn")
    Description = field("Description")
    IntegrationMethod = field("IntegrationMethod")
    IntegrationSubtype = field("IntegrationSubtype")
    IntegrationUri = field("IntegrationUri")
    PassthroughBehavior = field("PassthroughBehavior")
    PayloadFormatVersion = field("PayloadFormatVersion")
    RequestParameters = field("RequestParameters")
    RequestTemplates = field("RequestTemplates")
    ResponseParameters = field("ResponseParameters")
    TemplateSelectionExpression = field("TemplateSelectionExpression")
    TimeoutInMillis = field("TimeoutInMillis")

    @cached_property
    def TlsConfig(self):  # pragma: no cover
        return TlsConfigInput.make_one(self.boto3_raw_data["TlsConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIntegrationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIntegrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIntegrationRequest:
    boto3_raw_data: "type_defs.UpdateIntegrationRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    IntegrationId = field("IntegrationId")
    ConnectionId = field("ConnectionId")
    ConnectionType = field("ConnectionType")
    ContentHandlingStrategy = field("ContentHandlingStrategy")
    CredentialsArn = field("CredentialsArn")
    Description = field("Description")
    IntegrationMethod = field("IntegrationMethod")
    IntegrationSubtype = field("IntegrationSubtype")
    IntegrationType = field("IntegrationType")
    IntegrationUri = field("IntegrationUri")
    PassthroughBehavior = field("PassthroughBehavior")
    PayloadFormatVersion = field("PayloadFormatVersion")
    RequestParameters = field("RequestParameters")
    RequestTemplates = field("RequestTemplates")
    ResponseParameters = field("ResponseParameters")
    TemplateSelectionExpression = field("TemplateSelectionExpression")
    TimeoutInMillis = field("TimeoutInMillis")

    @cached_property
    def TlsConfig(self):  # pragma: no cover
        return TlsConfigInput.make_one(self.boto3_raw_data["TlsConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateIntegrationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIntegrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIntegrationResult:
    boto3_raw_data: "type_defs.CreateIntegrationResultTypeDef" = dataclasses.field()

    ApiGatewayManaged = field("ApiGatewayManaged")
    ConnectionId = field("ConnectionId")
    ConnectionType = field("ConnectionType")
    ContentHandlingStrategy = field("ContentHandlingStrategy")
    CredentialsArn = field("CredentialsArn")
    Description = field("Description")
    IntegrationId = field("IntegrationId")
    IntegrationMethod = field("IntegrationMethod")
    IntegrationResponseSelectionExpression = field(
        "IntegrationResponseSelectionExpression"
    )
    IntegrationSubtype = field("IntegrationSubtype")
    IntegrationType = field("IntegrationType")
    IntegrationUri = field("IntegrationUri")
    PassthroughBehavior = field("PassthroughBehavior")
    PayloadFormatVersion = field("PayloadFormatVersion")
    RequestParameters = field("RequestParameters")
    RequestTemplates = field("RequestTemplates")
    ResponseParameters = field("ResponseParameters")
    TemplateSelectionExpression = field("TemplateSelectionExpression")
    TimeoutInMillis = field("TimeoutInMillis")

    @cached_property
    def TlsConfig(self):  # pragma: no cover
        return TlsConfig.make_one(self.boto3_raw_data["TlsConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIntegrationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIntegrationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIntegrationResult:
    boto3_raw_data: "type_defs.GetIntegrationResultTypeDef" = dataclasses.field()

    ApiGatewayManaged = field("ApiGatewayManaged")
    ConnectionId = field("ConnectionId")
    ConnectionType = field("ConnectionType")
    ContentHandlingStrategy = field("ContentHandlingStrategy")
    CredentialsArn = field("CredentialsArn")
    Description = field("Description")
    IntegrationId = field("IntegrationId")
    IntegrationMethod = field("IntegrationMethod")
    IntegrationResponseSelectionExpression = field(
        "IntegrationResponseSelectionExpression"
    )
    IntegrationSubtype = field("IntegrationSubtype")
    IntegrationType = field("IntegrationType")
    IntegrationUri = field("IntegrationUri")
    PassthroughBehavior = field("PassthroughBehavior")
    PayloadFormatVersion = field("PayloadFormatVersion")
    RequestParameters = field("RequestParameters")
    RequestTemplates = field("RequestTemplates")
    ResponseParameters = field("ResponseParameters")
    TemplateSelectionExpression = field("TemplateSelectionExpression")
    TimeoutInMillis = field("TimeoutInMillis")

    @cached_property
    def TlsConfig(self):  # pragma: no cover
        return TlsConfig.make_one(self.boto3_raw_data["TlsConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIntegrationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIntegrationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Integration:
    boto3_raw_data: "type_defs.IntegrationTypeDef" = dataclasses.field()

    ApiGatewayManaged = field("ApiGatewayManaged")
    ConnectionId = field("ConnectionId")
    ConnectionType = field("ConnectionType")
    ContentHandlingStrategy = field("ContentHandlingStrategy")
    CredentialsArn = field("CredentialsArn")
    Description = field("Description")
    IntegrationId = field("IntegrationId")
    IntegrationMethod = field("IntegrationMethod")
    IntegrationResponseSelectionExpression = field(
        "IntegrationResponseSelectionExpression"
    )
    IntegrationSubtype = field("IntegrationSubtype")
    IntegrationType = field("IntegrationType")
    IntegrationUri = field("IntegrationUri")
    PassthroughBehavior = field("PassthroughBehavior")
    PayloadFormatVersion = field("PayloadFormatVersion")
    RequestParameters = field("RequestParameters")
    RequestTemplates = field("RequestTemplates")
    ResponseParameters = field("ResponseParameters")
    TemplateSelectionExpression = field("TemplateSelectionExpression")
    TimeoutInMillis = field("TimeoutInMillis")

    @cached_property
    def TlsConfig(self):  # pragma: no cover
        return TlsConfig.make_one(self.boto3_raw_data["TlsConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IntegrationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IntegrationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIntegrationResult:
    boto3_raw_data: "type_defs.UpdateIntegrationResultTypeDef" = dataclasses.field()

    ApiGatewayManaged = field("ApiGatewayManaged")
    ConnectionId = field("ConnectionId")
    ConnectionType = field("ConnectionType")
    ContentHandlingStrategy = field("ContentHandlingStrategy")
    CredentialsArn = field("CredentialsArn")
    Description = field("Description")
    IntegrationId = field("IntegrationId")
    IntegrationMethod = field("IntegrationMethod")
    IntegrationResponseSelectionExpression = field(
        "IntegrationResponseSelectionExpression"
    )
    IntegrationSubtype = field("IntegrationSubtype")
    IntegrationType = field("IntegrationType")
    IntegrationUri = field("IntegrationUri")
    PassthroughBehavior = field("PassthroughBehavior")
    PayloadFormatVersion = field("PayloadFormatVersion")
    RequestParameters = field("RequestParameters")
    RequestTemplates = field("RequestTemplates")
    ResponseParameters = field("ResponseParameters")
    TemplateSelectionExpression = field("TemplateSelectionExpression")
    TimeoutInMillis = field("TimeoutInMillis")

    @cached_property
    def TlsConfig(self):  # pragma: no cover
        return TlsConfig.make_one(self.boto3_raw_data["TlsConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateIntegrationResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIntegrationResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRouteRequest:
    boto3_raw_data: "type_defs.CreateRouteRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    RouteKey = field("RouteKey")
    ApiKeyRequired = field("ApiKeyRequired")
    AuthorizationScopes = field("AuthorizationScopes")
    AuthorizationType = field("AuthorizationType")
    AuthorizerId = field("AuthorizerId")
    ModelSelectionExpression = field("ModelSelectionExpression")
    OperationName = field("OperationName")
    RequestModels = field("RequestModels")
    RequestParameters = field("RequestParameters")
    RouteResponseSelectionExpression = field("RouteResponseSelectionExpression")
    Target = field("Target")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRouteRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRouteRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRouteResponseRequest:
    boto3_raw_data: "type_defs.CreateRouteResponseRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    RouteId = field("RouteId")
    RouteResponseKey = field("RouteResponseKey")
    ModelSelectionExpression = field("ModelSelectionExpression")
    ResponseModels = field("ResponseModels")
    ResponseParameters = field("ResponseParameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRouteResponseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRouteResponseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRouteResponseResponse:
    boto3_raw_data: "type_defs.CreateRouteResponseResponseTypeDef" = dataclasses.field()

    ModelSelectionExpression = field("ModelSelectionExpression")
    ResponseModels = field("ResponseModels")
    ResponseParameters = field("ResponseParameters")
    RouteResponseId = field("RouteResponseId")
    RouteResponseKey = field("RouteResponseKey")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRouteResponseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRouteResponseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRouteResult:
    boto3_raw_data: "type_defs.CreateRouteResultTypeDef" = dataclasses.field()

    ApiGatewayManaged = field("ApiGatewayManaged")
    ApiKeyRequired = field("ApiKeyRequired")
    AuthorizationScopes = field("AuthorizationScopes")
    AuthorizationType = field("AuthorizationType")
    AuthorizerId = field("AuthorizerId")
    ModelSelectionExpression = field("ModelSelectionExpression")
    OperationName = field("OperationName")
    RequestModels = field("RequestModels")
    RequestParameters = field("RequestParameters")
    RouteId = field("RouteId")
    RouteKey = field("RouteKey")
    RouteResponseSelectionExpression = field("RouteResponseSelectionExpression")
    Target = field("Target")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateRouteResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRouteResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRouteResponseResponse:
    boto3_raw_data: "type_defs.GetRouteResponseResponseTypeDef" = dataclasses.field()

    ModelSelectionExpression = field("ModelSelectionExpression")
    ResponseModels = field("ResponseModels")
    ResponseParameters = field("ResponseParameters")
    RouteResponseId = field("RouteResponseId")
    RouteResponseKey = field("RouteResponseKey")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRouteResponseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRouteResponseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRouteResult:
    boto3_raw_data: "type_defs.GetRouteResultTypeDef" = dataclasses.field()

    ApiGatewayManaged = field("ApiGatewayManaged")
    ApiKeyRequired = field("ApiKeyRequired")
    AuthorizationScopes = field("AuthorizationScopes")
    AuthorizationType = field("AuthorizationType")
    AuthorizerId = field("AuthorizerId")
    ModelSelectionExpression = field("ModelSelectionExpression")
    OperationName = field("OperationName")
    RequestModels = field("RequestModels")
    RequestParameters = field("RequestParameters")
    RouteId = field("RouteId")
    RouteKey = field("RouteKey")
    RouteResponseSelectionExpression = field("RouteResponseSelectionExpression")
    Target = field("Target")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRouteResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetRouteResultTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RouteResponse:
    boto3_raw_data: "type_defs.RouteResponseTypeDef" = dataclasses.field()

    RouteResponseKey = field("RouteResponseKey")
    ModelSelectionExpression = field("ModelSelectionExpression")
    ResponseModels = field("ResponseModels")
    ResponseParameters = field("ResponseParameters")
    RouteResponseId = field("RouteResponseId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Route:
    boto3_raw_data: "type_defs.RouteTypeDef" = dataclasses.field()

    RouteKey = field("RouteKey")
    ApiGatewayManaged = field("ApiGatewayManaged")
    ApiKeyRequired = field("ApiKeyRequired")
    AuthorizationScopes = field("AuthorizationScopes")
    AuthorizationType = field("AuthorizationType")
    AuthorizerId = field("AuthorizerId")
    ModelSelectionExpression = field("ModelSelectionExpression")
    OperationName = field("OperationName")
    RequestModels = field("RequestModels")
    RequestParameters = field("RequestParameters")
    RouteId = field("RouteId")
    RouteResponseSelectionExpression = field("RouteResponseSelectionExpression")
    Target = field("Target")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RouteTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RouteTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRouteRequest:
    boto3_raw_data: "type_defs.UpdateRouteRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    RouteId = field("RouteId")
    ApiKeyRequired = field("ApiKeyRequired")
    AuthorizationScopes = field("AuthorizationScopes")
    AuthorizationType = field("AuthorizationType")
    AuthorizerId = field("AuthorizerId")
    ModelSelectionExpression = field("ModelSelectionExpression")
    OperationName = field("OperationName")
    RequestModels = field("RequestModels")
    RequestParameters = field("RequestParameters")
    RouteKey = field("RouteKey")
    RouteResponseSelectionExpression = field("RouteResponseSelectionExpression")
    Target = field("Target")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRouteRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRouteRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRouteResponseRequest:
    boto3_raw_data: "type_defs.UpdateRouteResponseRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    RouteId = field("RouteId")
    RouteResponseId = field("RouteResponseId")
    ModelSelectionExpression = field("ModelSelectionExpression")
    ResponseModels = field("ResponseModels")
    ResponseParameters = field("ResponseParameters")
    RouteResponseKey = field("RouteResponseKey")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRouteResponseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRouteResponseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRouteResponseResponse:
    boto3_raw_data: "type_defs.UpdateRouteResponseResponseTypeDef" = dataclasses.field()

    ModelSelectionExpression = field("ModelSelectionExpression")
    ResponseModels = field("ResponseModels")
    ResponseParameters = field("ResponseParameters")
    RouteResponseId = field("RouteResponseId")
    RouteResponseKey = field("RouteResponseKey")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateRouteResponseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRouteResponseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateRouteResult:
    boto3_raw_data: "type_defs.UpdateRouteResultTypeDef" = dataclasses.field()

    ApiGatewayManaged = field("ApiGatewayManaged")
    ApiKeyRequired = field("ApiKeyRequired")
    AuthorizationScopes = field("AuthorizationScopes")
    AuthorizationType = field("AuthorizationType")
    AuthorizerId = field("AuthorizerId")
    ModelSelectionExpression = field("ModelSelectionExpression")
    OperationName = field("OperationName")
    RequestModels = field("RequestModels")
    RequestParameters = field("RequestParameters")
    RouteId = field("RouteId")
    RouteKey = field("RouteKey")
    RouteResponseSelectionExpression = field("RouteResponseSelectionExpression")
    Target = field("Target")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateRouteResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateRouteResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStageRequest:
    boto3_raw_data: "type_defs.CreateStageRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    StageName = field("StageName")

    @cached_property
    def AccessLogSettings(self):  # pragma: no cover
        return AccessLogSettings.make_one(self.boto3_raw_data["AccessLogSettings"])

    AutoDeploy = field("AutoDeploy")
    ClientCertificateId = field("ClientCertificateId")

    @cached_property
    def DefaultRouteSettings(self):  # pragma: no cover
        return RouteSettings.make_one(self.boto3_raw_data["DefaultRouteSettings"])

    DeploymentId = field("DeploymentId")
    Description = field("Description")
    RouteSettings = field("RouteSettings")
    StageVariables = field("StageVariables")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStageResponse:
    boto3_raw_data: "type_defs.CreateStageResponseTypeDef" = dataclasses.field()

    @cached_property
    def AccessLogSettings(self):  # pragma: no cover
        return AccessLogSettings.make_one(self.boto3_raw_data["AccessLogSettings"])

    ApiGatewayManaged = field("ApiGatewayManaged")
    AutoDeploy = field("AutoDeploy")
    ClientCertificateId = field("ClientCertificateId")
    CreatedDate = field("CreatedDate")

    @cached_property
    def DefaultRouteSettings(self):  # pragma: no cover
        return RouteSettings.make_one(self.boto3_raw_data["DefaultRouteSettings"])

    DeploymentId = field("DeploymentId")
    Description = field("Description")
    LastDeploymentStatusMessage = field("LastDeploymentStatusMessage")
    LastUpdatedDate = field("LastUpdatedDate")
    RouteSettings = field("RouteSettings")
    StageName = field("StageName")
    StageVariables = field("StageVariables")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStageResponse:
    boto3_raw_data: "type_defs.GetStageResponseTypeDef" = dataclasses.field()

    @cached_property
    def AccessLogSettings(self):  # pragma: no cover
        return AccessLogSettings.make_one(self.boto3_raw_data["AccessLogSettings"])

    ApiGatewayManaged = field("ApiGatewayManaged")
    AutoDeploy = field("AutoDeploy")
    ClientCertificateId = field("ClientCertificateId")
    CreatedDate = field("CreatedDate")

    @cached_property
    def DefaultRouteSettings(self):  # pragma: no cover
        return RouteSettings.make_one(self.boto3_raw_data["DefaultRouteSettings"])

    DeploymentId = field("DeploymentId")
    Description = field("Description")
    LastDeploymentStatusMessage = field("LastDeploymentStatusMessage")
    LastUpdatedDate = field("LastUpdatedDate")
    RouteSettings = field("RouteSettings")
    StageName = field("StageName")
    StageVariables = field("StageVariables")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetStageResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Stage:
    boto3_raw_data: "type_defs.StageTypeDef" = dataclasses.field()

    StageName = field("StageName")

    @cached_property
    def AccessLogSettings(self):  # pragma: no cover
        return AccessLogSettings.make_one(self.boto3_raw_data["AccessLogSettings"])

    ApiGatewayManaged = field("ApiGatewayManaged")
    AutoDeploy = field("AutoDeploy")
    ClientCertificateId = field("ClientCertificateId")
    CreatedDate = field("CreatedDate")

    @cached_property
    def DefaultRouteSettings(self):  # pragma: no cover
        return RouteSettings.make_one(self.boto3_raw_data["DefaultRouteSettings"])

    DeploymentId = field("DeploymentId")
    Description = field("Description")
    LastDeploymentStatusMessage = field("LastDeploymentStatusMessage")
    LastUpdatedDate = field("LastUpdatedDate")
    RouteSettings = field("RouteSettings")
    StageVariables = field("StageVariables")
    Tags = field("Tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StageTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStageRequest:
    boto3_raw_data: "type_defs.UpdateStageRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    StageName = field("StageName")

    @cached_property
    def AccessLogSettings(self):  # pragma: no cover
        return AccessLogSettings.make_one(self.boto3_raw_data["AccessLogSettings"])

    AutoDeploy = field("AutoDeploy")
    ClientCertificateId = field("ClientCertificateId")

    @cached_property
    def DefaultRouteSettings(self):  # pragma: no cover
        return RouteSettings.make_one(self.boto3_raw_data["DefaultRouteSettings"])

    DeploymentId = field("DeploymentId")
    Description = field("Description")
    RouteSettings = field("RouteSettings")
    StageVariables = field("StageVariables")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateStageRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStageRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStageResponse:
    boto3_raw_data: "type_defs.UpdateStageResponseTypeDef" = dataclasses.field()

    @cached_property
    def AccessLogSettings(self):  # pragma: no cover
        return AccessLogSettings.make_one(self.boto3_raw_data["AccessLogSettings"])

    ApiGatewayManaged = field("ApiGatewayManaged")
    AutoDeploy = field("AutoDeploy")
    ClientCertificateId = field("ClientCertificateId")
    CreatedDate = field("CreatedDate")

    @cached_property
    def DefaultRouteSettings(self):  # pragma: no cover
        return RouteSettings.make_one(self.boto3_raw_data["DefaultRouteSettings"])

    DeploymentId = field("DeploymentId")
    Description = field("Description")
    LastDeploymentStatusMessage = field("LastDeploymentStatusMessage")
    LastUpdatedDate = field("LastUpdatedDate")
    RouteSettings = field("RouteSettings")
    StageName = field("StageName")
    StageVariables = field("StageVariables")
    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateStageResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStageResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentsResponse:
    boto3_raw_data: "type_defs.GetDeploymentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return Deployment.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainNameConfiguration:
    boto3_raw_data: "type_defs.DomainNameConfigurationTypeDef" = dataclasses.field()

    ApiGatewayDomainName = field("ApiGatewayDomainName")
    CertificateArn = field("CertificateArn")
    CertificateName = field("CertificateName")
    CertificateUploadDate = field("CertificateUploadDate")
    DomainNameStatus = field("DomainNameStatus")
    DomainNameStatusMessage = field("DomainNameStatusMessage")
    EndpointType = field("EndpointType")
    HostedZoneId = field("HostedZoneId")
    IpAddressType = field("IpAddressType")
    SecurityPolicy = field("SecurityPolicy")
    OwnershipVerificationCertificateArn = field("OwnershipVerificationCertificateArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainNameConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainNameConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApisRequestPaginate:
    boto3_raw_data: "type_defs.GetApisRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApisRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApisRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAuthorizersRequestPaginate:
    boto3_raw_data: "type_defs.GetAuthorizersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ApiId = field("ApiId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAuthorizersRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAuthorizersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentsRequestPaginate:
    boto3_raw_data: "type_defs.GetDeploymentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ApiId = field("ApiId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDeploymentsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainNamesRequestPaginate:
    boto3_raw_data: "type_defs.GetDomainNamesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDomainNamesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainNamesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIntegrationResponsesRequestPaginate:
    boto3_raw_data: "type_defs.GetIntegrationResponsesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ApiId = field("ApiId")
    IntegrationId = field("IntegrationId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetIntegrationResponsesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIntegrationResponsesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIntegrationsRequestPaginate:
    boto3_raw_data: "type_defs.GetIntegrationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ApiId = field("ApiId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetIntegrationsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIntegrationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelsRequestPaginate:
    boto3_raw_data: "type_defs.GetModelsRequestPaginateTypeDef" = dataclasses.field()

    ApiId = field("ApiId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetModelsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetModelsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRouteResponsesRequestPaginate:
    boto3_raw_data: "type_defs.GetRouteResponsesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ApiId = field("ApiId")
    RouteId = field("RouteId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetRouteResponsesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRouteResponsesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRoutesRequestPaginate:
    boto3_raw_data: "type_defs.GetRoutesRequestPaginateTypeDef" = dataclasses.field()

    ApiId = field("ApiId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRoutesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRoutesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStagesRequestPaginate:
    boto3_raw_data: "type_defs.GetStagesRequestPaginateTypeDef" = dataclasses.field()

    ApiId = field("ApiId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStagesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStagesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRoutingRulesRequestPaginate:
    boto3_raw_data: "type_defs.ListRoutingRulesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    DomainNameId = field("DomainNameId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListRoutingRulesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRoutingRulesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIntegrationResponsesResponse:
    boto3_raw_data: "type_defs.GetIntegrationResponsesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Items(self):  # pragma: no cover
        return IntegrationResponse.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetIntegrationResponsesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIntegrationResponsesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetModelsResponse:
    boto3_raw_data: "type_defs.GetModelsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return Model.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetModelsResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetModelsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetVpcLinksResponse:
    boto3_raw_data: "type_defs.GetVpcLinksResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return VpcLink.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetVpcLinksResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetVpcLinksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingRuleAction:
    boto3_raw_data: "type_defs.RoutingRuleActionTypeDef" = dataclasses.field()

    @cached_property
    def InvokeApi(self):  # pragma: no cover
        return RoutingRuleActionInvokeApi.make_one(self.boto3_raw_data["InvokeApi"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RoutingRuleActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutingRuleActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingRuleMatchHeadersOutput:
    boto3_raw_data: "type_defs.RoutingRuleMatchHeadersOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AnyOf(self):  # pragma: no cover
        return RoutingRuleMatchHeaderValue.make_many(self.boto3_raw_data["AnyOf"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RoutingRuleMatchHeadersOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutingRuleMatchHeadersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingRuleMatchHeaders:
    boto3_raw_data: "type_defs.RoutingRuleMatchHeadersTypeDef" = dataclasses.field()

    @cached_property
    def AnyOf(self):  # pragma: no cover
        return RoutingRuleMatchHeaderValue.make_many(self.boto3_raw_data["AnyOf"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutingRuleMatchHeadersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutingRuleMatchHeadersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApisResponse:
    boto3_raw_data: "type_defs.GetApisResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return Api.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetApisResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetApisResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAuthorizersResponse:
    boto3_raw_data: "type_defs.GetAuthorizersResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return Authorizer.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAuthorizersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAuthorizersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApiRequest:
    boto3_raw_data: "type_defs.CreateApiRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    ProtocolType = field("ProtocolType")
    ApiKeySelectionExpression = field("ApiKeySelectionExpression")
    CorsConfiguration = field("CorsConfiguration")
    CredentialsArn = field("CredentialsArn")
    Description = field("Description")
    DisableSchemaValidation = field("DisableSchemaValidation")
    DisableExecuteApiEndpoint = field("DisableExecuteApiEndpoint")
    IpAddressType = field("IpAddressType")
    RouteKey = field("RouteKey")
    RouteSelectionExpression = field("RouteSelectionExpression")
    Tags = field("Tags")
    Target = field("Target")
    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateApiRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApiRequest:
    boto3_raw_data: "type_defs.UpdateApiRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    ApiKeySelectionExpression = field("ApiKeySelectionExpression")
    CorsConfiguration = field("CorsConfiguration")
    CredentialsArn = field("CredentialsArn")
    Description = field("Description")
    DisableSchemaValidation = field("DisableSchemaValidation")
    DisableExecuteApiEndpoint = field("DisableExecuteApiEndpoint")
    IpAddressType = field("IpAddressType")
    Name = field("Name")
    RouteKey = field("RouteKey")
    RouteSelectionExpression = field("RouteSelectionExpression")
    Target = field("Target")
    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateApiRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApiRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainNamesResponse:
    boto3_raw_data: "type_defs.GetDomainNamesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return DomainName.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDomainNamesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainNamesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIntegrationsResponse:
    boto3_raw_data: "type_defs.GetIntegrationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return Integration.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIntegrationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIntegrationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRouteResponsesResponse:
    boto3_raw_data: "type_defs.GetRouteResponsesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return RouteResponse.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRouteResponsesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRouteResponsesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRoutesResponse:
    boto3_raw_data: "type_defs.GetRoutesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return Route.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetRoutesResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRoutesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStagesResponse:
    boto3_raw_data: "type_defs.GetStagesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return Stage.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetStagesResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStagesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAuthorizerRequest:
    boto3_raw_data: "type_defs.CreateAuthorizerRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    AuthorizerType = field("AuthorizerType")
    IdentitySource = field("IdentitySource")
    Name = field("Name")
    AuthorizerCredentialsArn = field("AuthorizerCredentialsArn")
    AuthorizerPayloadFormatVersion = field("AuthorizerPayloadFormatVersion")
    AuthorizerResultTtlInSeconds = field("AuthorizerResultTtlInSeconds")
    AuthorizerUri = field("AuthorizerUri")
    EnableSimpleResponses = field("EnableSimpleResponses")
    IdentityValidationExpression = field("IdentityValidationExpression")
    JwtConfiguration = field("JwtConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAuthorizerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAuthorizerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAuthorizerRequest:
    boto3_raw_data: "type_defs.UpdateAuthorizerRequestTypeDef" = dataclasses.field()

    ApiId = field("ApiId")
    AuthorizerId = field("AuthorizerId")
    AuthorizerCredentialsArn = field("AuthorizerCredentialsArn")
    AuthorizerPayloadFormatVersion = field("AuthorizerPayloadFormatVersion")
    AuthorizerResultTtlInSeconds = field("AuthorizerResultTtlInSeconds")
    AuthorizerType = field("AuthorizerType")
    AuthorizerUri = field("AuthorizerUri")
    EnableSimpleResponses = field("EnableSimpleResponses")
    IdentitySource = field("IdentitySource")
    IdentityValidationExpression = field("IdentityValidationExpression")
    JwtConfiguration = field("JwtConfiguration")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAuthorizerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAuthorizerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingRuleConditionOutput:
    boto3_raw_data: "type_defs.RoutingRuleConditionOutputTypeDef" = dataclasses.field()

    @cached_property
    def MatchBasePaths(self):  # pragma: no cover
        return RoutingRuleMatchBasePathsOutput.make_one(
            self.boto3_raw_data["MatchBasePaths"]
        )

    @cached_property
    def MatchHeaders(self):  # pragma: no cover
        return RoutingRuleMatchHeadersOutput.make_one(
            self.boto3_raw_data["MatchHeaders"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutingRuleConditionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutingRuleConditionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainNameRequest:
    boto3_raw_data: "type_defs.CreateDomainNameRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    DomainNameConfigurations = field("DomainNameConfigurations")

    @cached_property
    def MutualTlsAuthentication(self):  # pragma: no cover
        return MutualTlsAuthenticationInput.make_one(
            self.boto3_raw_data["MutualTlsAuthentication"]
        )

    RoutingMode = field("RoutingMode")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDomainNameRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainNameRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainNameRequest:
    boto3_raw_data: "type_defs.UpdateDomainNameRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    DomainNameConfigurations = field("DomainNameConfigurations")

    @cached_property
    def MutualTlsAuthentication(self):  # pragma: no cover
        return MutualTlsAuthenticationInput.make_one(
            self.boto3_raw_data["MutualTlsAuthentication"]
        )

    RoutingMode = field("RoutingMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateDomainNameRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainNameRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRoutingRuleResponse:
    boto3_raw_data: "type_defs.CreateRoutingRuleResponseTypeDef" = dataclasses.field()

    @cached_property
    def Actions(self):  # pragma: no cover
        return RoutingRuleAction.make_many(self.boto3_raw_data["Actions"])

    @cached_property
    def Conditions(self):  # pragma: no cover
        return RoutingRuleConditionOutput.make_many(self.boto3_raw_data["Conditions"])

    Priority = field("Priority")
    RoutingRuleArn = field("RoutingRuleArn")
    RoutingRuleId = field("RoutingRuleId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRoutingRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRoutingRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetRoutingRuleResponse:
    boto3_raw_data: "type_defs.GetRoutingRuleResponseTypeDef" = dataclasses.field()

    @cached_property
    def Actions(self):  # pragma: no cover
        return RoutingRuleAction.make_many(self.boto3_raw_data["Actions"])

    @cached_property
    def Conditions(self):  # pragma: no cover
        return RoutingRuleConditionOutput.make_many(self.boto3_raw_data["Conditions"])

    Priority = field("Priority")
    RoutingRuleArn = field("RoutingRuleArn")
    RoutingRuleId = field("RoutingRuleId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetRoutingRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetRoutingRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRoutingRuleResponse:
    boto3_raw_data: "type_defs.PutRoutingRuleResponseTypeDef" = dataclasses.field()

    @cached_property
    def Actions(self):  # pragma: no cover
        return RoutingRuleAction.make_many(self.boto3_raw_data["Actions"])

    @cached_property
    def Conditions(self):  # pragma: no cover
        return RoutingRuleConditionOutput.make_many(self.boto3_raw_data["Conditions"])

    Priority = field("Priority")
    RoutingRuleArn = field("RoutingRuleArn")
    RoutingRuleId = field("RoutingRuleId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutRoutingRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRoutingRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingRule:
    boto3_raw_data: "type_defs.RoutingRuleTypeDef" = dataclasses.field()

    @cached_property
    def Actions(self):  # pragma: no cover
        return RoutingRuleAction.make_many(self.boto3_raw_data["Actions"])

    @cached_property
    def Conditions(self):  # pragma: no cover
        return RoutingRuleConditionOutput.make_many(self.boto3_raw_data["Conditions"])

    Priority = field("Priority")
    RoutingRuleArn = field("RoutingRuleArn")
    RoutingRuleId = field("RoutingRuleId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RoutingRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RoutingRuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RoutingRuleCondition:
    boto3_raw_data: "type_defs.RoutingRuleConditionTypeDef" = dataclasses.field()

    MatchBasePaths = field("MatchBasePaths")
    MatchHeaders = field("MatchHeaders")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RoutingRuleConditionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RoutingRuleConditionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRoutingRulesResponse:
    boto3_raw_data: "type_defs.ListRoutingRulesResponseTypeDef" = dataclasses.field()

    @cached_property
    def RoutingRules(self):  # pragma: no cover
        return RoutingRule.make_many(self.boto3_raw_data["RoutingRules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRoutingRulesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRoutingRulesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRoutingRuleRequest:
    boto3_raw_data: "type_defs.CreateRoutingRuleRequestTypeDef" = dataclasses.field()

    @cached_property
    def Actions(self):  # pragma: no cover
        return RoutingRuleAction.make_many(self.boto3_raw_data["Actions"])

    Conditions = field("Conditions")
    DomainName = field("DomainName")
    Priority = field("Priority")
    DomainNameId = field("DomainNameId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRoutingRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRoutingRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRoutingRuleRequest:
    boto3_raw_data: "type_defs.PutRoutingRuleRequestTypeDef" = dataclasses.field()

    @cached_property
    def Actions(self):  # pragma: no cover
        return RoutingRuleAction.make_many(self.boto3_raw_data["Actions"])

    Conditions = field("Conditions")
    DomainName = field("DomainName")
    Priority = field("Priority")
    RoutingRuleId = field("RoutingRuleId")
    DomainNameId = field("DomainNameId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutRoutingRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRoutingRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
