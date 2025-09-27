# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_elbv2 import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AuthenticateCognitoActionConfigOutput:
    boto3_raw_data: "type_defs.AuthenticateCognitoActionConfigOutputTypeDef" = (
        dataclasses.field()
    )

    UserPoolArn = field("UserPoolArn")
    UserPoolClientId = field("UserPoolClientId")
    UserPoolDomain = field("UserPoolDomain")
    SessionCookieName = field("SessionCookieName")
    Scope = field("Scope")
    SessionTimeout = field("SessionTimeout")
    AuthenticationRequestExtraParams = field("AuthenticationRequestExtraParams")
    OnUnauthenticatedRequest = field("OnUnauthenticatedRequest")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AuthenticateCognitoActionConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthenticateCognitoActionConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthenticateOidcActionConfigOutput:
    boto3_raw_data: "type_defs.AuthenticateOidcActionConfigOutputTypeDef" = (
        dataclasses.field()
    )

    Issuer = field("Issuer")
    AuthorizationEndpoint = field("AuthorizationEndpoint")
    TokenEndpoint = field("TokenEndpoint")
    UserInfoEndpoint = field("UserInfoEndpoint")
    ClientId = field("ClientId")
    ClientSecret = field("ClientSecret")
    SessionCookieName = field("SessionCookieName")
    Scope = field("Scope")
    SessionTimeout = field("SessionTimeout")
    AuthenticationRequestExtraParams = field("AuthenticationRequestExtraParams")
    OnUnauthenticatedRequest = field("OnUnauthenticatedRequest")
    UseExistingClientSecret = field("UseExistingClientSecret")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AuthenticateOidcActionConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthenticateOidcActionConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FixedResponseActionConfig:
    boto3_raw_data: "type_defs.FixedResponseActionConfigTypeDef" = dataclasses.field()

    StatusCode = field("StatusCode")
    MessageBody = field("MessageBody")
    ContentType = field("ContentType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FixedResponseActionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FixedResponseActionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RedirectActionConfig:
    boto3_raw_data: "type_defs.RedirectActionConfigTypeDef" = dataclasses.field()

    StatusCode = field("StatusCode")
    Protocol = field("Protocol")
    Port = field("Port")
    Host = field("Host")
    Path = field("Path")
    Query = field("Query")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RedirectActionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RedirectActionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Certificate:
    boto3_raw_data: "type_defs.CertificateTypeDef" = dataclasses.field()

    CertificateArn = field("CertificateArn")
    IsDefault = field("IsDefault")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CertificateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CertificateTypeDef"]]
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
class RevocationContent:
    boto3_raw_data: "type_defs.RevocationContentTypeDef" = dataclasses.field()

    S3Bucket = field("S3Bucket")
    S3Key = field("S3Key")
    S3ObjectVersion = field("S3ObjectVersion")
    RevocationType = field("RevocationType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RevocationContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevocationContentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrustStoreRevocation:
    boto3_raw_data: "type_defs.TrustStoreRevocationTypeDef" = dataclasses.field()

    TrustStoreArn = field("TrustStoreArn")
    RevocationId = field("RevocationId")
    RevocationType = field("RevocationType")
    NumberOfRevokedEntries = field("NumberOfRevokedEntries")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrustStoreRevocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrustStoreRevocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdministrativeOverride:
    boto3_raw_data: "type_defs.AdministrativeOverrideTypeDef" = dataclasses.field()

    State = field("State")
    Reason = field("Reason")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdministrativeOverrideTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdministrativeOverrideTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalyDetection:
    boto3_raw_data: "type_defs.AnomalyDetectionTypeDef" = dataclasses.field()

    Result = field("Result")
    MitigationInEffect = field("MitigationInEffect")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnomalyDetectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnomalyDetectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthenticateCognitoActionConfig:
    boto3_raw_data: "type_defs.AuthenticateCognitoActionConfigTypeDef" = (
        dataclasses.field()
    )

    UserPoolArn = field("UserPoolArn")
    UserPoolClientId = field("UserPoolClientId")
    UserPoolDomain = field("UserPoolDomain")
    SessionCookieName = field("SessionCookieName")
    Scope = field("Scope")
    SessionTimeout = field("SessionTimeout")
    AuthenticationRequestExtraParams = field("AuthenticationRequestExtraParams")
    OnUnauthenticatedRequest = field("OnUnauthenticatedRequest")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AuthenticateCognitoActionConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthenticateCognitoActionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthenticateOidcActionConfig:
    boto3_raw_data: "type_defs.AuthenticateOidcActionConfigTypeDef" = (
        dataclasses.field()
    )

    Issuer = field("Issuer")
    AuthorizationEndpoint = field("AuthorizationEndpoint")
    TokenEndpoint = field("TokenEndpoint")
    UserInfoEndpoint = field("UserInfoEndpoint")
    ClientId = field("ClientId")
    ClientSecret = field("ClientSecret")
    SessionCookieName = field("SessionCookieName")
    Scope = field("Scope")
    SessionTimeout = field("SessionTimeout")
    AuthenticationRequestExtraParams = field("AuthenticationRequestExtraParams")
    OnUnauthenticatedRequest = field("OnUnauthenticatedRequest")
    UseExistingClientSecret = field("UseExistingClientSecret")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthenticateOidcActionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthenticateOidcActionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoadBalancerAddress:
    boto3_raw_data: "type_defs.LoadBalancerAddressTypeDef" = dataclasses.field()

    IpAddress = field("IpAddress")
    AllocationId = field("AllocationId")
    PrivateIPv4Address = field("PrivateIPv4Address")
    IPv6Address = field("IPv6Address")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoadBalancerAddressTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoadBalancerAddressTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacityReservationStatus:
    boto3_raw_data: "type_defs.CapacityReservationStatusTypeDef" = dataclasses.field()

    Code = field("Code")
    Reason = field("Reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CapacityReservationStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapacityReservationStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Cipher:
    boto3_raw_data: "type_defs.CipherTypeDef" = dataclasses.field()

    Name = field("Name")
    Priority = field("Priority")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CipherTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CipherTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MutualAuthenticationAttributes:
    boto3_raw_data: "type_defs.MutualAuthenticationAttributesTypeDef" = (
        dataclasses.field()
    )

    Mode = field("Mode")
    TrustStoreArn = field("TrustStoreArn")
    IgnoreClientCertificateExpiry = field("IgnoreClientCertificateExpiry")
    TrustStoreAssociationStatus = field("TrustStoreAssociationStatus")
    AdvertiseTrustStoreCaNames = field("AdvertiseTrustStoreCaNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MutualAuthenticationAttributesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MutualAuthenticationAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IpamPools:
    boto3_raw_data: "type_defs.IpamPoolsTypeDef" = dataclasses.field()

    Ipv4IpamPoolId = field("Ipv4IpamPoolId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IpamPoolsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IpamPoolsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubnetMapping:
    boto3_raw_data: "type_defs.SubnetMappingTypeDef" = dataclasses.field()

    SubnetId = field("SubnetId")
    AllocationId = field("AllocationId")
    PrivateIPv4Address = field("PrivateIPv4Address")
    IPv6Address = field("IPv6Address")
    SourceNatIpv6Prefix = field("SourceNatIpv6Prefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubnetMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SubnetMappingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Matcher:
    boto3_raw_data: "type_defs.MatcherTypeDef" = dataclasses.field()

    HttpCode = field("HttpCode")
    GrpcCode = field("GrpcCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MatcherTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MatcherTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrustStore:
    boto3_raw_data: "type_defs.TrustStoreTypeDef" = dataclasses.field()

    Name = field("Name")
    TrustStoreArn = field("TrustStoreArn")
    Status = field("Status")
    NumberOfCaCertificates = field("NumberOfCaCertificates")
    TotalRevokedEntries = field("TotalRevokedEntries")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrustStoreTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TrustStoreTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteListenerInput:
    boto3_raw_data: "type_defs.DeleteListenerInputTypeDef" = dataclasses.field()

    ListenerArn = field("ListenerArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteListenerInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteListenerInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLoadBalancerInput:
    boto3_raw_data: "type_defs.DeleteLoadBalancerInputTypeDef" = dataclasses.field()

    LoadBalancerArn = field("LoadBalancerArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLoadBalancerInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLoadBalancerInputTypeDef"]
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

    RuleArn = field("RuleArn")

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
class DeleteSharedTrustStoreAssociationInput:
    boto3_raw_data: "type_defs.DeleteSharedTrustStoreAssociationInputTypeDef" = (
        dataclasses.field()
    )

    TrustStoreArn = field("TrustStoreArn")
    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteSharedTrustStoreAssociationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSharedTrustStoreAssociationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTargetGroupInput:
    boto3_raw_data: "type_defs.DeleteTargetGroupInputTypeDef" = dataclasses.field()

    TargetGroupArn = field("TargetGroupArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTargetGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTargetGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTrustStoreInput:
    boto3_raw_data: "type_defs.DeleteTrustStoreInputTypeDef" = dataclasses.field()

    TrustStoreArn = field("TrustStoreArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTrustStoreInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTrustStoreInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetDescription:
    boto3_raw_data: "type_defs.TargetDescriptionTypeDef" = dataclasses.field()

    Id = field("Id")
    Port = field("Port")
    AvailabilityZone = field("AvailabilityZone")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetDescriptionTypeDef"]
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
class DescribeAccountLimitsInput:
    boto3_raw_data: "type_defs.DescribeAccountLimitsInputTypeDef" = dataclasses.field()

    Marker = field("Marker")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAccountLimitsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountLimitsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Limit:
    boto3_raw_data: "type_defs.LimitTypeDef" = dataclasses.field()

    Name = field("Name")
    Max = field("Max")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LimitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LimitTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCapacityReservationInput:
    boto3_raw_data: "type_defs.DescribeCapacityReservationInputTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerArn = field("LoadBalancerArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeCapacityReservationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCapacityReservationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MinimumLoadBalancerCapacity:
    boto3_raw_data: "type_defs.MinimumLoadBalancerCapacityTypeDef" = dataclasses.field()

    CapacityUnits = field("CapacityUnits")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MinimumLoadBalancerCapacityTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MinimumLoadBalancerCapacityTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeListenerAttributesInput:
    boto3_raw_data: "type_defs.DescribeListenerAttributesInputTypeDef" = (
        dataclasses.field()
    )

    ListenerArn = field("ListenerArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeListenerAttributesInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeListenerAttributesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListenerAttribute:
    boto3_raw_data: "type_defs.ListenerAttributeTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListenerAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListenerAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeListenerCertificatesInput:
    boto3_raw_data: "type_defs.DescribeListenerCertificatesInputTypeDef" = (
        dataclasses.field()
    )

    ListenerArn = field("ListenerArn")
    Marker = field("Marker")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeListenerCertificatesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeListenerCertificatesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeListenersInput:
    boto3_raw_data: "type_defs.DescribeListenersInputTypeDef" = dataclasses.field()

    LoadBalancerArn = field("LoadBalancerArn")
    ListenerArns = field("ListenerArns")
    Marker = field("Marker")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeListenersInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeListenersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoadBalancerAttributesInput:
    boto3_raw_data: "type_defs.DescribeLoadBalancerAttributesInputTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerArn = field("LoadBalancerArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLoadBalancerAttributesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoadBalancerAttributesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoadBalancerAttribute:
    boto3_raw_data: "type_defs.LoadBalancerAttributeTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoadBalancerAttributeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoadBalancerAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoadBalancersInput:
    boto3_raw_data: "type_defs.DescribeLoadBalancersInputTypeDef" = dataclasses.field()

    LoadBalancerArns = field("LoadBalancerArns")
    Names = field("Names")
    Marker = field("Marker")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLoadBalancersInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoadBalancersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaiterConfig:
    boto3_raw_data: "type_defs.WaiterConfigTypeDef" = dataclasses.field()

    Delay = field("Delay")
    MaxAttempts = field("MaxAttempts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WaiterConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WaiterConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRulesInput:
    boto3_raw_data: "type_defs.DescribeRulesInputTypeDef" = dataclasses.field()

    ListenerArn = field("ListenerArn")
    RuleArns = field("RuleArns")
    Marker = field("Marker")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRulesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRulesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSSLPoliciesInput:
    boto3_raw_data: "type_defs.DescribeSSLPoliciesInputTypeDef" = dataclasses.field()

    Names = field("Names")
    Marker = field("Marker")
    PageSize = field("PageSize")
    LoadBalancerType = field("LoadBalancerType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSSLPoliciesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSSLPoliciesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTagsInput:
    boto3_raw_data: "type_defs.DescribeTagsInputTypeDef" = dataclasses.field()

    ResourceArns = field("ResourceArns")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DescribeTagsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTagsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTargetGroupAttributesInput:
    boto3_raw_data: "type_defs.DescribeTargetGroupAttributesInputTypeDef" = (
        dataclasses.field()
    )

    TargetGroupArn = field("TargetGroupArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTargetGroupAttributesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTargetGroupAttributesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetGroupAttribute:
    boto3_raw_data: "type_defs.TargetGroupAttributeTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetGroupAttributeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetGroupAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTargetGroupsInput:
    boto3_raw_data: "type_defs.DescribeTargetGroupsInputTypeDef" = dataclasses.field()

    LoadBalancerArn = field("LoadBalancerArn")
    TargetGroupArns = field("TargetGroupArns")
    Names = field("Names")
    Marker = field("Marker")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTargetGroupsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTargetGroupsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrustStoreAssociationsInput:
    boto3_raw_data: "type_defs.DescribeTrustStoreAssociationsInputTypeDef" = (
        dataclasses.field()
    )

    TrustStoreArn = field("TrustStoreArn")
    Marker = field("Marker")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTrustStoreAssociationsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrustStoreAssociationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrustStoreAssociation:
    boto3_raw_data: "type_defs.TrustStoreAssociationTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrustStoreAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrustStoreAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrustStoreRevocation:
    boto3_raw_data: "type_defs.DescribeTrustStoreRevocationTypeDef" = (
        dataclasses.field()
    )

    TrustStoreArn = field("TrustStoreArn")
    RevocationId = field("RevocationId")
    RevocationType = field("RevocationType")
    NumberOfRevokedEntries = field("NumberOfRevokedEntries")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTrustStoreRevocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrustStoreRevocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrustStoreRevocationsInput:
    boto3_raw_data: "type_defs.DescribeTrustStoreRevocationsInputTypeDef" = (
        dataclasses.field()
    )

    TrustStoreArn = field("TrustStoreArn")
    RevocationIds = field("RevocationIds")
    Marker = field("Marker")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTrustStoreRevocationsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrustStoreRevocationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrustStoresInput:
    boto3_raw_data: "type_defs.DescribeTrustStoresInputTypeDef" = dataclasses.field()

    TrustStoreArns = field("TrustStoreArns")
    Names = field("Names")
    Marker = field("Marker")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTrustStoresInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrustStoresInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetGroupStickinessConfig:
    boto3_raw_data: "type_defs.TargetGroupStickinessConfigTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    DurationSeconds = field("DurationSeconds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetGroupStickinessConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetGroupStickinessConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetGroupTuple:
    boto3_raw_data: "type_defs.TargetGroupTupleTypeDef" = dataclasses.field()

    TargetGroupArn = field("TargetGroupArn")
    Weight = field("Weight")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetGroupTupleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetGroupTupleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePolicyInput:
    boto3_raw_data: "type_defs.GetResourcePolicyInputTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrustStoreCaCertificatesBundleInput:
    boto3_raw_data: "type_defs.GetTrustStoreCaCertificatesBundleInputTypeDef" = (
        dataclasses.field()
    )

    TrustStoreArn = field("TrustStoreArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTrustStoreCaCertificatesBundleInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrustStoreCaCertificatesBundleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrustStoreRevocationContentInput:
    boto3_raw_data: "type_defs.GetTrustStoreRevocationContentInputTypeDef" = (
        dataclasses.field()
    )

    TrustStoreArn = field("TrustStoreArn")
    RevocationId = field("RevocationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTrustStoreRevocationContentInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrustStoreRevocationContentInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HostHeaderConditionConfigOutput:
    boto3_raw_data: "type_defs.HostHeaderConditionConfigOutputTypeDef" = (
        dataclasses.field()
    )

    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.HostHeaderConditionConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HostHeaderConditionConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HostHeaderConditionConfig:
    boto3_raw_data: "type_defs.HostHeaderConditionConfigTypeDef" = dataclasses.field()

    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HostHeaderConditionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HostHeaderConditionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpHeaderConditionConfigOutput:
    boto3_raw_data: "type_defs.HttpHeaderConditionConfigOutputTypeDef" = (
        dataclasses.field()
    )

    HttpHeaderName = field("HttpHeaderName")
    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.HttpHeaderConditionConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpHeaderConditionConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpHeaderConditionConfig:
    boto3_raw_data: "type_defs.HttpHeaderConditionConfigTypeDef" = dataclasses.field()

    HttpHeaderName = field("HttpHeaderName")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HttpHeaderConditionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpHeaderConditionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpRequestMethodConditionConfigOutput:
    boto3_raw_data: "type_defs.HttpRequestMethodConditionConfigOutputTypeDef" = (
        dataclasses.field()
    )

    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.HttpRequestMethodConditionConfigOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpRequestMethodConditionConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HttpRequestMethodConditionConfig:
    boto3_raw_data: "type_defs.HttpRequestMethodConditionConfigTypeDef" = (
        dataclasses.field()
    )

    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.HttpRequestMethodConditionConfigTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HttpRequestMethodConditionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoadBalancerState:
    boto3_raw_data: "type_defs.LoadBalancerStateTypeDef" = dataclasses.field()

    Code = field("Code")
    Reason = field("Reason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoadBalancerStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoadBalancerStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyTrustStoreInput:
    boto3_raw_data: "type_defs.ModifyTrustStoreInputTypeDef" = dataclasses.field()

    TrustStoreArn = field("TrustStoreArn")
    CaCertificatesBundleS3Bucket = field("CaCertificatesBundleS3Bucket")
    CaCertificatesBundleS3Key = field("CaCertificatesBundleS3Key")
    CaCertificatesBundleS3ObjectVersion = field("CaCertificatesBundleS3ObjectVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyTrustStoreInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyTrustStoreInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PathPatternConditionConfigOutput:
    boto3_raw_data: "type_defs.PathPatternConditionConfigOutputTypeDef" = (
        dataclasses.field()
    )

    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PathPatternConditionConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PathPatternConditionConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PathPatternConditionConfig:
    boto3_raw_data: "type_defs.PathPatternConditionConfigTypeDef" = dataclasses.field()

    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PathPatternConditionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PathPatternConditionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryStringKeyValuePair:
    boto3_raw_data: "type_defs.QueryStringKeyValuePairTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryStringKeyValuePairTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryStringKeyValuePairTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveTagsInput:
    boto3_raw_data: "type_defs.RemoveTagsInputTypeDef" = dataclasses.field()

    ResourceArns = field("ResourceArns")
    TagKeys = field("TagKeys")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RemoveTagsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RemoveTagsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveTrustStoreRevocationsInput:
    boto3_raw_data: "type_defs.RemoveTrustStoreRevocationsInputTypeDef" = (
        dataclasses.field()
    )

    TrustStoreArn = field("TrustStoreArn")
    RevocationIds = field("RevocationIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveTrustStoreRevocationsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveTrustStoreRevocationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceIpConditionConfigOutput:
    boto3_raw_data: "type_defs.SourceIpConditionConfigOutputTypeDef" = (
        dataclasses.field()
    )

    Values = field("Values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SourceIpConditionConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceIpConditionConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RulePriorityPair:
    boto3_raw_data: "type_defs.RulePriorityPairTypeDef" = dataclasses.field()

    RuleArn = field("RuleArn")
    Priority = field("Priority")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RulePriorityPairTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RulePriorityPairTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetIpAddressTypeInput:
    boto3_raw_data: "type_defs.SetIpAddressTypeInputTypeDef" = dataclasses.field()

    LoadBalancerArn = field("LoadBalancerArn")
    IpAddressType = field("IpAddressType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetIpAddressTypeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetIpAddressTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetSecurityGroupsInput:
    boto3_raw_data: "type_defs.SetSecurityGroupsInputTypeDef" = dataclasses.field()

    LoadBalancerArn = field("LoadBalancerArn")
    SecurityGroups = field("SecurityGroups")
    EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic = field(
        "EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic"
    )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetSecurityGroupsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetSecurityGroupsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceIpConditionConfig:
    boto3_raw_data: "type_defs.SourceIpConditionConfigTypeDef" = dataclasses.field()

    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceIpConditionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceIpConditionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetHealth:
    boto3_raw_data: "type_defs.TargetHealthTypeDef" = dataclasses.field()

    State = field("State")
    Reason = field("Reason")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetHealthTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetHealthTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddListenerCertificatesInput:
    boto3_raw_data: "type_defs.AddListenerCertificatesInputTypeDef" = (
        dataclasses.field()
    )

    ListenerArn = field("ListenerArn")

    @cached_property
    def Certificates(self):  # pragma: no cover
        return Certificate.make_many(self.boto3_raw_data["Certificates"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddListenerCertificatesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddListenerCertificatesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveListenerCertificatesInput:
    boto3_raw_data: "type_defs.RemoveListenerCertificatesInputTypeDef" = (
        dataclasses.field()
    )

    ListenerArn = field("ListenerArn")

    @cached_property
    def Certificates(self):  # pragma: no cover
        return Certificate.make_many(self.boto3_raw_data["Certificates"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveListenerCertificatesInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveListenerCertificatesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddListenerCertificatesOutput:
    boto3_raw_data: "type_defs.AddListenerCertificatesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Certificates(self):  # pragma: no cover
        return Certificate.make_many(self.boto3_raw_data["Certificates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddListenerCertificatesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddListenerCertificatesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeListenerCertificatesOutput:
    boto3_raw_data: "type_defs.DescribeListenerCertificatesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Certificates(self):  # pragma: no cover
        return Certificate.make_many(self.boto3_raw_data["Certificates"])

    NextMarker = field("NextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeListenerCertificatesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeListenerCertificatesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetResourcePolicyOutput:
    boto3_raw_data: "type_defs.GetResourcePolicyOutputTypeDef" = dataclasses.field()

    Policy = field("Policy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetResourcePolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetResourcePolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrustStoreCaCertificatesBundleOutput:
    boto3_raw_data: "type_defs.GetTrustStoreCaCertificatesBundleOutputTypeDef" = (
        dataclasses.field()
    )

    Location = field("Location")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTrustStoreCaCertificatesBundleOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrustStoreCaCertificatesBundleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrustStoreRevocationContentOutput:
    boto3_raw_data: "type_defs.GetTrustStoreRevocationContentOutputTypeDef" = (
        dataclasses.field()
    )

    Location = field("Location")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTrustStoreRevocationContentOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrustStoreRevocationContentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetIpAddressTypeOutput:
    boto3_raw_data: "type_defs.SetIpAddressTypeOutputTypeDef" = dataclasses.field()

    IpAddressType = field("IpAddressType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetIpAddressTypeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetIpAddressTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetSecurityGroupsOutput:
    boto3_raw_data: "type_defs.SetSecurityGroupsOutputTypeDef" = dataclasses.field()

    SecurityGroupIds = field("SecurityGroupIds")
    EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic = field(
        "EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic"
    )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetSecurityGroupsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetSecurityGroupsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddTagsInput:
    boto3_raw_data: "type_defs.AddTagsInputTypeDef" = dataclasses.field()

    ResourceArns = field("ResourceArns")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddTagsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddTagsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrustStoreInput:
    boto3_raw_data: "type_defs.CreateTrustStoreInputTypeDef" = dataclasses.field()

    Name = field("Name")
    CaCertificatesBundleS3Bucket = field("CaCertificatesBundleS3Bucket")
    CaCertificatesBundleS3Key = field("CaCertificatesBundleS3Key")
    CaCertificatesBundleS3ObjectVersion = field("CaCertificatesBundleS3ObjectVersion")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTrustStoreInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrustStoreInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagDescription:
    boto3_raw_data: "type_defs.TagDescriptionTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagDescriptionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddTrustStoreRevocationsInput:
    boto3_raw_data: "type_defs.AddTrustStoreRevocationsInputTypeDef" = (
        dataclasses.field()
    )

    TrustStoreArn = field("TrustStoreArn")

    @cached_property
    def RevocationContents(self):  # pragma: no cover
        return RevocationContent.make_many(self.boto3_raw_data["RevocationContents"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddTrustStoreRevocationsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddTrustStoreRevocationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddTrustStoreRevocationsOutput:
    boto3_raw_data: "type_defs.AddTrustStoreRevocationsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TrustStoreRevocations(self):  # pragma: no cover
        return TrustStoreRevocation.make_many(
            self.boto3_raw_data["TrustStoreRevocations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddTrustStoreRevocationsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddTrustStoreRevocationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AvailabilityZone:
    boto3_raw_data: "type_defs.AvailabilityZoneTypeDef" = dataclasses.field()

    ZoneName = field("ZoneName")
    SubnetId = field("SubnetId")
    OutpostId = field("OutpostId")

    @cached_property
    def LoadBalancerAddresses(self):  # pragma: no cover
        return LoadBalancerAddress.make_many(
            self.boto3_raw_data["LoadBalancerAddresses"]
        )

    SourceNatIpv6Prefixes = field("SourceNatIpv6Prefixes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AvailabilityZoneTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AvailabilityZoneTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ZonalCapacityReservationState:
    boto3_raw_data: "type_defs.ZonalCapacityReservationStateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def State(self):  # pragma: no cover
        return CapacityReservationStatus.make_one(self.boto3_raw_data["State"])

    AvailabilityZone = field("AvailabilityZone")
    EffectiveCapacityUnits = field("EffectiveCapacityUnits")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ZonalCapacityReservationStateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ZonalCapacityReservationStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SslPolicy:
    boto3_raw_data: "type_defs.SslPolicyTypeDef" = dataclasses.field()

    SslProtocols = field("SslProtocols")

    @cached_property
    def Ciphers(self):  # pragma: no cover
        return Cipher.make_many(self.boto3_raw_data["Ciphers"])

    Name = field("Name")
    SupportedLoadBalancerTypes = field("SupportedLoadBalancerTypes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SslPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SslPolicyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyIpPoolsInput:
    boto3_raw_data: "type_defs.ModifyIpPoolsInputTypeDef" = dataclasses.field()

    LoadBalancerArn = field("LoadBalancerArn")

    @cached_property
    def IpamPools(self):  # pragma: no cover
        return IpamPools.make_one(self.boto3_raw_data["IpamPools"])

    RemoveIpamPools = field("RemoveIpamPools")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyIpPoolsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyIpPoolsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyIpPoolsOutput:
    boto3_raw_data: "type_defs.ModifyIpPoolsOutputTypeDef" = dataclasses.field()

    @cached_property
    def IpamPools(self):  # pragma: no cover
        return IpamPools.make_one(self.boto3_raw_data["IpamPools"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyIpPoolsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyIpPoolsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLoadBalancerInput:
    boto3_raw_data: "type_defs.CreateLoadBalancerInputTypeDef" = dataclasses.field()

    Name = field("Name")
    Subnets = field("Subnets")

    @cached_property
    def SubnetMappings(self):  # pragma: no cover
        return SubnetMapping.make_many(self.boto3_raw_data["SubnetMappings"])

    SecurityGroups = field("SecurityGroups")
    Scheme = field("Scheme")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    Type = field("Type")
    IpAddressType = field("IpAddressType")
    CustomerOwnedIpv4Pool = field("CustomerOwnedIpv4Pool")
    EnablePrefixForIpv6SourceNat = field("EnablePrefixForIpv6SourceNat")

    @cached_property
    def IpamPools(self):  # pragma: no cover
        return IpamPools.make_one(self.boto3_raw_data["IpamPools"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLoadBalancerInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLoadBalancerInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetSubnetsInput:
    boto3_raw_data: "type_defs.SetSubnetsInputTypeDef" = dataclasses.field()

    LoadBalancerArn = field("LoadBalancerArn")
    Subnets = field("Subnets")

    @cached_property
    def SubnetMappings(self):  # pragma: no cover
        return SubnetMapping.make_many(self.boto3_raw_data["SubnetMappings"])

    IpAddressType = field("IpAddressType")
    EnablePrefixForIpv6SourceNat = field("EnablePrefixForIpv6SourceNat")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SetSubnetsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SetSubnetsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTargetGroupInput:
    boto3_raw_data: "type_defs.CreateTargetGroupInputTypeDef" = dataclasses.field()

    Name = field("Name")
    Protocol = field("Protocol")
    ProtocolVersion = field("ProtocolVersion")
    Port = field("Port")
    VpcId = field("VpcId")
    HealthCheckProtocol = field("HealthCheckProtocol")
    HealthCheckPort = field("HealthCheckPort")
    HealthCheckEnabled = field("HealthCheckEnabled")
    HealthCheckPath = field("HealthCheckPath")
    HealthCheckIntervalSeconds = field("HealthCheckIntervalSeconds")
    HealthCheckTimeoutSeconds = field("HealthCheckTimeoutSeconds")
    HealthyThresholdCount = field("HealthyThresholdCount")
    UnhealthyThresholdCount = field("UnhealthyThresholdCount")

    @cached_property
    def Matcher(self):  # pragma: no cover
        return Matcher.make_one(self.boto3_raw_data["Matcher"])

    TargetType = field("TargetType")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    IpAddressType = field("IpAddressType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTargetGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTargetGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyTargetGroupInput:
    boto3_raw_data: "type_defs.ModifyTargetGroupInputTypeDef" = dataclasses.field()

    TargetGroupArn = field("TargetGroupArn")
    HealthCheckProtocol = field("HealthCheckProtocol")
    HealthCheckPort = field("HealthCheckPort")
    HealthCheckPath = field("HealthCheckPath")
    HealthCheckEnabled = field("HealthCheckEnabled")
    HealthCheckIntervalSeconds = field("HealthCheckIntervalSeconds")
    HealthCheckTimeoutSeconds = field("HealthCheckTimeoutSeconds")
    HealthyThresholdCount = field("HealthyThresholdCount")
    UnhealthyThresholdCount = field("UnhealthyThresholdCount")

    @cached_property
    def Matcher(self):  # pragma: no cover
        return Matcher.make_one(self.boto3_raw_data["Matcher"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyTargetGroupInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyTargetGroupInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetGroup:
    boto3_raw_data: "type_defs.TargetGroupTypeDef" = dataclasses.field()

    TargetGroupArn = field("TargetGroupArn")
    TargetGroupName = field("TargetGroupName")
    Protocol = field("Protocol")
    Port = field("Port")
    VpcId = field("VpcId")
    HealthCheckProtocol = field("HealthCheckProtocol")
    HealthCheckPort = field("HealthCheckPort")
    HealthCheckEnabled = field("HealthCheckEnabled")
    HealthCheckIntervalSeconds = field("HealthCheckIntervalSeconds")
    HealthCheckTimeoutSeconds = field("HealthCheckTimeoutSeconds")
    HealthyThresholdCount = field("HealthyThresholdCount")
    UnhealthyThresholdCount = field("UnhealthyThresholdCount")
    HealthCheckPath = field("HealthCheckPath")

    @cached_property
    def Matcher(self):  # pragma: no cover
        return Matcher.make_one(self.boto3_raw_data["Matcher"])

    LoadBalancerArns = field("LoadBalancerArns")
    TargetType = field("TargetType")
    ProtocolVersion = field("ProtocolVersion")
    IpAddressType = field("IpAddressType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TargetGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TargetGroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrustStoreOutput:
    boto3_raw_data: "type_defs.CreateTrustStoreOutputTypeDef" = dataclasses.field()

    @cached_property
    def TrustStores(self):  # pragma: no cover
        return TrustStore.make_many(self.boto3_raw_data["TrustStores"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTrustStoreOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrustStoreOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrustStoresOutput:
    boto3_raw_data: "type_defs.DescribeTrustStoresOutputTypeDef" = dataclasses.field()

    @cached_property
    def TrustStores(self):  # pragma: no cover
        return TrustStore.make_many(self.boto3_raw_data["TrustStores"])

    NextMarker = field("NextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTrustStoresOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrustStoresOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyTrustStoreOutput:
    boto3_raw_data: "type_defs.ModifyTrustStoreOutputTypeDef" = dataclasses.field()

    @cached_property
    def TrustStores(self):  # pragma: no cover
        return TrustStore.make_many(self.boto3_raw_data["TrustStores"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyTrustStoreOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyTrustStoreOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterTargetsInput:
    boto3_raw_data: "type_defs.DeregisterTargetsInputTypeDef" = dataclasses.field()

    TargetGroupArn = field("TargetGroupArn")

    @cached_property
    def Targets(self):  # pragma: no cover
        return TargetDescription.make_many(self.boto3_raw_data["Targets"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeregisterTargetsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterTargetsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTargetHealthInput:
    boto3_raw_data: "type_defs.DescribeTargetHealthInputTypeDef" = dataclasses.field()

    TargetGroupArn = field("TargetGroupArn")

    @cached_property
    def Targets(self):  # pragma: no cover
        return TargetDescription.make_many(self.boto3_raw_data["Targets"])

    Include = field("Include")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTargetHealthInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTargetHealthInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterTargetsInput:
    boto3_raw_data: "type_defs.RegisterTargetsInputTypeDef" = dataclasses.field()

    TargetGroupArn = field("TargetGroupArn")

    @cached_property
    def Targets(self):  # pragma: no cover
        return TargetDescription.make_many(self.boto3_raw_data["Targets"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterTargetsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterTargetsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountLimitsInputPaginate:
    boto3_raw_data: "type_defs.DescribeAccountLimitsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAccountLimitsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountLimitsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeListenerCertificatesInputPaginate:
    boto3_raw_data: "type_defs.DescribeListenerCertificatesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    ListenerArn = field("ListenerArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeListenerCertificatesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeListenerCertificatesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeListenersInputPaginate:
    boto3_raw_data: "type_defs.DescribeListenersInputPaginateTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerArn = field("LoadBalancerArn")
    ListenerArns = field("ListenerArns")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeListenersInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeListenersInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoadBalancersInputPaginate:
    boto3_raw_data: "type_defs.DescribeLoadBalancersInputPaginateTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerArns = field("LoadBalancerArns")
    Names = field("Names")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLoadBalancersInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoadBalancersInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeRulesInputPaginate:
    boto3_raw_data: "type_defs.DescribeRulesInputPaginateTypeDef" = dataclasses.field()

    ListenerArn = field("ListenerArn")
    RuleArns = field("RuleArns")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRulesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRulesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSSLPoliciesInputPaginate:
    boto3_raw_data: "type_defs.DescribeSSLPoliciesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    Names = field("Names")
    LoadBalancerType = field("LoadBalancerType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeSSLPoliciesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSSLPoliciesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTargetGroupsInputPaginate:
    boto3_raw_data: "type_defs.DescribeTargetGroupsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerArn = field("LoadBalancerArn")
    TargetGroupArns = field("TargetGroupArns")
    Names = field("Names")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTargetGroupsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTargetGroupsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrustStoreAssociationsInputPaginate:
    boto3_raw_data: "type_defs.DescribeTrustStoreAssociationsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    TrustStoreArn = field("TrustStoreArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTrustStoreAssociationsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrustStoreAssociationsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrustStoreRevocationsInputPaginate:
    boto3_raw_data: "type_defs.DescribeTrustStoreRevocationsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    TrustStoreArn = field("TrustStoreArn")
    RevocationIds = field("RevocationIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTrustStoreRevocationsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrustStoreRevocationsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrustStoresInputPaginate:
    boto3_raw_data: "type_defs.DescribeTrustStoresInputPaginateTypeDef" = (
        dataclasses.field()
    )

    TrustStoreArns = field("TrustStoreArns")
    Names = field("Names")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeTrustStoresInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrustStoresInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountLimitsOutput:
    boto3_raw_data: "type_defs.DescribeAccountLimitsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Limits(self):  # pragma: no cover
        return Limit.make_many(self.boto3_raw_data["Limits"])

    NextMarker = field("NextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAccountLimitsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountLimitsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyCapacityReservationInput:
    boto3_raw_data: "type_defs.ModifyCapacityReservationInputTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerArn = field("LoadBalancerArn")

    @cached_property
    def MinimumLoadBalancerCapacity(self):  # pragma: no cover
        return MinimumLoadBalancerCapacity.make_one(
            self.boto3_raw_data["MinimumLoadBalancerCapacity"]
        )

    ResetCapacityReservation = field("ResetCapacityReservation")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyCapacityReservationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyCapacityReservationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeListenerAttributesOutput:
    boto3_raw_data: "type_defs.DescribeListenerAttributesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Attributes(self):  # pragma: no cover
        return ListenerAttribute.make_many(self.boto3_raw_data["Attributes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeListenerAttributesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeListenerAttributesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyListenerAttributesInput:
    boto3_raw_data: "type_defs.ModifyListenerAttributesInputTypeDef" = (
        dataclasses.field()
    )

    ListenerArn = field("ListenerArn")

    @cached_property
    def Attributes(self):  # pragma: no cover
        return ListenerAttribute.make_many(self.boto3_raw_data["Attributes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyListenerAttributesInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyListenerAttributesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyListenerAttributesOutput:
    boto3_raw_data: "type_defs.ModifyListenerAttributesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Attributes(self):  # pragma: no cover
        return ListenerAttribute.make_many(self.boto3_raw_data["Attributes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyListenerAttributesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyListenerAttributesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoadBalancerAttributesOutput:
    boto3_raw_data: "type_defs.DescribeLoadBalancerAttributesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Attributes(self):  # pragma: no cover
        return LoadBalancerAttribute.make_many(self.boto3_raw_data["Attributes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLoadBalancerAttributesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoadBalancerAttributesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyLoadBalancerAttributesInput:
    boto3_raw_data: "type_defs.ModifyLoadBalancerAttributesInputTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerArn = field("LoadBalancerArn")

    @cached_property
    def Attributes(self):  # pragma: no cover
        return LoadBalancerAttribute.make_many(self.boto3_raw_data["Attributes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyLoadBalancerAttributesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyLoadBalancerAttributesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyLoadBalancerAttributesOutput:
    boto3_raw_data: "type_defs.ModifyLoadBalancerAttributesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Attributes(self):  # pragma: no cover
        return LoadBalancerAttribute.make_many(self.boto3_raw_data["Attributes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyLoadBalancerAttributesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyLoadBalancerAttributesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoadBalancersInputWaitExtraExtra:
    boto3_raw_data: "type_defs.DescribeLoadBalancersInputWaitExtraExtraTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerArns = field("LoadBalancerArns")
    Names = field("Names")
    Marker = field("Marker")
    PageSize = field("PageSize")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLoadBalancersInputWaitExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoadBalancersInputWaitExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoadBalancersInputWaitExtra:
    boto3_raw_data: "type_defs.DescribeLoadBalancersInputWaitExtraTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerArns = field("LoadBalancerArns")
    Names = field("Names")
    Marker = field("Marker")
    PageSize = field("PageSize")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLoadBalancersInputWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoadBalancersInputWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoadBalancersInputWait:
    boto3_raw_data: "type_defs.DescribeLoadBalancersInputWaitTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerArns = field("LoadBalancerArns")
    Names = field("Names")
    Marker = field("Marker")
    PageSize = field("PageSize")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeLoadBalancersInputWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoadBalancersInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTargetHealthInputWaitExtra:
    boto3_raw_data: "type_defs.DescribeTargetHealthInputWaitExtraTypeDef" = (
        dataclasses.field()
    )

    TargetGroupArn = field("TargetGroupArn")

    @cached_property
    def Targets(self):  # pragma: no cover
        return TargetDescription.make_many(self.boto3_raw_data["Targets"])

    Include = field("Include")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTargetHealthInputWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTargetHealthInputWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTargetHealthInputWait:
    boto3_raw_data: "type_defs.DescribeTargetHealthInputWaitTypeDef" = (
        dataclasses.field()
    )

    TargetGroupArn = field("TargetGroupArn")

    @cached_property
    def Targets(self):  # pragma: no cover
        return TargetDescription.make_many(self.boto3_raw_data["Targets"])

    Include = field("Include")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeTargetHealthInputWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTargetHealthInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTargetGroupAttributesOutput:
    boto3_raw_data: "type_defs.DescribeTargetGroupAttributesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Attributes(self):  # pragma: no cover
        return TargetGroupAttribute.make_many(self.boto3_raw_data["Attributes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTargetGroupAttributesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTargetGroupAttributesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyTargetGroupAttributesInput:
    boto3_raw_data: "type_defs.ModifyTargetGroupAttributesInputTypeDef" = (
        dataclasses.field()
    )

    TargetGroupArn = field("TargetGroupArn")

    @cached_property
    def Attributes(self):  # pragma: no cover
        return TargetGroupAttribute.make_many(self.boto3_raw_data["Attributes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyTargetGroupAttributesInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyTargetGroupAttributesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyTargetGroupAttributesOutput:
    boto3_raw_data: "type_defs.ModifyTargetGroupAttributesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Attributes(self):  # pragma: no cover
        return TargetGroupAttribute.make_many(self.boto3_raw_data["Attributes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyTargetGroupAttributesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyTargetGroupAttributesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrustStoreAssociationsOutput:
    boto3_raw_data: "type_defs.DescribeTrustStoreAssociationsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TrustStoreAssociations(self):  # pragma: no cover
        return TrustStoreAssociation.make_many(
            self.boto3_raw_data["TrustStoreAssociations"]
        )

    NextMarker = field("NextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTrustStoreAssociationsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrustStoreAssociationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTrustStoreRevocationsOutput:
    boto3_raw_data: "type_defs.DescribeTrustStoreRevocationsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TrustStoreRevocations(self):  # pragma: no cover
        return DescribeTrustStoreRevocation.make_many(
            self.boto3_raw_data["TrustStoreRevocations"]
        )

    NextMarker = field("NextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTrustStoreRevocationsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTrustStoreRevocationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ForwardActionConfigOutput:
    boto3_raw_data: "type_defs.ForwardActionConfigOutputTypeDef" = dataclasses.field()

    @cached_property
    def TargetGroups(self):  # pragma: no cover
        return TargetGroupTuple.make_many(self.boto3_raw_data["TargetGroups"])

    @cached_property
    def TargetGroupStickinessConfig(self):  # pragma: no cover
        return TargetGroupStickinessConfig.make_one(
            self.boto3_raw_data["TargetGroupStickinessConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ForwardActionConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ForwardActionConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ForwardActionConfig:
    boto3_raw_data: "type_defs.ForwardActionConfigTypeDef" = dataclasses.field()

    @cached_property
    def TargetGroups(self):  # pragma: no cover
        return TargetGroupTuple.make_many(self.boto3_raw_data["TargetGroups"])

    @cached_property
    def TargetGroupStickinessConfig(self):  # pragma: no cover
        return TargetGroupStickinessConfig.make_one(
            self.boto3_raw_data["TargetGroupStickinessConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ForwardActionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ForwardActionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryStringConditionConfigOutput:
    boto3_raw_data: "type_defs.QueryStringConditionConfigOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Values(self):  # pragma: no cover
        return QueryStringKeyValuePair.make_many(self.boto3_raw_data["Values"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.QueryStringConditionConfigOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryStringConditionConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryStringConditionConfig:
    boto3_raw_data: "type_defs.QueryStringConditionConfigTypeDef" = dataclasses.field()

    @cached_property
    def Values(self):  # pragma: no cover
        return QueryStringKeyValuePair.make_many(self.boto3_raw_data["Values"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryStringConditionConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryStringConditionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetRulePrioritiesInput:
    boto3_raw_data: "type_defs.SetRulePrioritiesInputTypeDef" = dataclasses.field()

    @cached_property
    def RulePriorities(self):  # pragma: no cover
        return RulePriorityPair.make_many(self.boto3_raw_data["RulePriorities"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetRulePrioritiesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetRulePrioritiesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetHealthDescription:
    boto3_raw_data: "type_defs.TargetHealthDescriptionTypeDef" = dataclasses.field()

    @cached_property
    def Target(self):  # pragma: no cover
        return TargetDescription.make_one(self.boto3_raw_data["Target"])

    HealthCheckPort = field("HealthCheckPort")

    @cached_property
    def TargetHealth(self):  # pragma: no cover
        return TargetHealth.make_one(self.boto3_raw_data["TargetHealth"])

    @cached_property
    def AnomalyDetection(self):  # pragma: no cover
        return AnomalyDetection.make_one(self.boto3_raw_data["AnomalyDetection"])

    @cached_property
    def AdministrativeOverride(self):  # pragma: no cover
        return AdministrativeOverride.make_one(
            self.boto3_raw_data["AdministrativeOverride"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetHealthDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetHealthDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTagsOutput:
    boto3_raw_data: "type_defs.DescribeTagsOutputTypeDef" = dataclasses.field()

    @cached_property
    def TagDescriptions(self):  # pragma: no cover
        return TagDescription.make_many(self.boto3_raw_data["TagDescriptions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTagsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTagsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoadBalancer:
    boto3_raw_data: "type_defs.LoadBalancerTypeDef" = dataclasses.field()

    LoadBalancerArn = field("LoadBalancerArn")
    DNSName = field("DNSName")
    CanonicalHostedZoneId = field("CanonicalHostedZoneId")
    CreatedTime = field("CreatedTime")
    LoadBalancerName = field("LoadBalancerName")
    Scheme = field("Scheme")
    VpcId = field("VpcId")

    @cached_property
    def State(self):  # pragma: no cover
        return LoadBalancerState.make_one(self.boto3_raw_data["State"])

    Type = field("Type")

    @cached_property
    def AvailabilityZones(self):  # pragma: no cover
        return AvailabilityZone.make_many(self.boto3_raw_data["AvailabilityZones"])

    SecurityGroups = field("SecurityGroups")
    IpAddressType = field("IpAddressType")
    CustomerOwnedIpv4Pool = field("CustomerOwnedIpv4Pool")
    EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic = field(
        "EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic"
    )
    EnablePrefixForIpv6SourceNat = field("EnablePrefixForIpv6SourceNat")

    @cached_property
    def IpamPools(self):  # pragma: no cover
        return IpamPools.make_one(self.boto3_raw_data["IpamPools"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoadBalancerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoadBalancerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetSubnetsOutput:
    boto3_raw_data: "type_defs.SetSubnetsOutputTypeDef" = dataclasses.field()

    @cached_property
    def AvailabilityZones(self):  # pragma: no cover
        return AvailabilityZone.make_many(self.boto3_raw_data["AvailabilityZones"])

    IpAddressType = field("IpAddressType")
    EnablePrefixForIpv6SourceNat = field("EnablePrefixForIpv6SourceNat")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SetSubnetsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetSubnetsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCapacityReservationOutput:
    boto3_raw_data: "type_defs.DescribeCapacityReservationOutputTypeDef" = (
        dataclasses.field()
    )

    LastModifiedTime = field("LastModifiedTime")
    DecreaseRequestsRemaining = field("DecreaseRequestsRemaining")

    @cached_property
    def MinimumLoadBalancerCapacity(self):  # pragma: no cover
        return MinimumLoadBalancerCapacity.make_one(
            self.boto3_raw_data["MinimumLoadBalancerCapacity"]
        )

    @cached_property
    def CapacityReservationState(self):  # pragma: no cover
        return ZonalCapacityReservationState.make_many(
            self.boto3_raw_data["CapacityReservationState"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCapacityReservationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCapacityReservationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyCapacityReservationOutput:
    boto3_raw_data: "type_defs.ModifyCapacityReservationOutputTypeDef" = (
        dataclasses.field()
    )

    LastModifiedTime = field("LastModifiedTime")
    DecreaseRequestsRemaining = field("DecreaseRequestsRemaining")

    @cached_property
    def MinimumLoadBalancerCapacity(self):  # pragma: no cover
        return MinimumLoadBalancerCapacity.make_one(
            self.boto3_raw_data["MinimumLoadBalancerCapacity"]
        )

    @cached_property
    def CapacityReservationState(self):  # pragma: no cover
        return ZonalCapacityReservationState.make_many(
            self.boto3_raw_data["CapacityReservationState"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ModifyCapacityReservationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyCapacityReservationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSSLPoliciesOutput:
    boto3_raw_data: "type_defs.DescribeSSLPoliciesOutputTypeDef" = dataclasses.field()

    @cached_property
    def SslPolicies(self):  # pragma: no cover
        return SslPolicy.make_many(self.boto3_raw_data["SslPolicies"])

    NextMarker = field("NextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSSLPoliciesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSSLPoliciesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTargetGroupOutput:
    boto3_raw_data: "type_defs.CreateTargetGroupOutputTypeDef" = dataclasses.field()

    @cached_property
    def TargetGroups(self):  # pragma: no cover
        return TargetGroup.make_many(self.boto3_raw_data["TargetGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTargetGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTargetGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTargetGroupsOutput:
    boto3_raw_data: "type_defs.DescribeTargetGroupsOutputTypeDef" = dataclasses.field()

    @cached_property
    def TargetGroups(self):  # pragma: no cover
        return TargetGroup.make_many(self.boto3_raw_data["TargetGroups"])

    NextMarker = field("NextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTargetGroupsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTargetGroupsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyTargetGroupOutput:
    boto3_raw_data: "type_defs.ModifyTargetGroupOutputTypeDef" = dataclasses.field()

    @cached_property
    def TargetGroups(self):  # pragma: no cover
        return TargetGroup.make_many(self.boto3_raw_data["TargetGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyTargetGroupOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyTargetGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionOutput:
    boto3_raw_data: "type_defs.ActionOutputTypeDef" = dataclasses.field()

    Type = field("Type")
    TargetGroupArn = field("TargetGroupArn")

    @cached_property
    def AuthenticateOidcConfig(self):  # pragma: no cover
        return AuthenticateOidcActionConfigOutput.make_one(
            self.boto3_raw_data["AuthenticateOidcConfig"]
        )

    @cached_property
    def AuthenticateCognitoConfig(self):  # pragma: no cover
        return AuthenticateCognitoActionConfigOutput.make_one(
            self.boto3_raw_data["AuthenticateCognitoConfig"]
        )

    Order = field("Order")

    @cached_property
    def RedirectConfig(self):  # pragma: no cover
        return RedirectActionConfig.make_one(self.boto3_raw_data["RedirectConfig"])

    @cached_property
    def FixedResponseConfig(self):  # pragma: no cover
        return FixedResponseActionConfig.make_one(
            self.boto3_raw_data["FixedResponseConfig"]
        )

    @cached_property
    def ForwardConfig(self):  # pragma: no cover
        return ForwardActionConfigOutput.make_one(self.boto3_raw_data["ForwardConfig"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleConditionOutput:
    boto3_raw_data: "type_defs.RuleConditionOutputTypeDef" = dataclasses.field()

    Field = field("Field")
    Values = field("Values")

    @cached_property
    def HostHeaderConfig(self):  # pragma: no cover
        return HostHeaderConditionConfigOutput.make_one(
            self.boto3_raw_data["HostHeaderConfig"]
        )

    @cached_property
    def PathPatternConfig(self):  # pragma: no cover
        return PathPatternConditionConfigOutput.make_one(
            self.boto3_raw_data["PathPatternConfig"]
        )

    @cached_property
    def HttpHeaderConfig(self):  # pragma: no cover
        return HttpHeaderConditionConfigOutput.make_one(
            self.boto3_raw_data["HttpHeaderConfig"]
        )

    @cached_property
    def QueryStringConfig(self):  # pragma: no cover
        return QueryStringConditionConfigOutput.make_one(
            self.boto3_raw_data["QueryStringConfig"]
        )

    @cached_property
    def HttpRequestMethodConfig(self):  # pragma: no cover
        return HttpRequestMethodConditionConfigOutput.make_one(
            self.boto3_raw_data["HttpRequestMethodConfig"]
        )

    @cached_property
    def SourceIpConfig(self):  # pragma: no cover
        return SourceIpConditionConfigOutput.make_one(
            self.boto3_raw_data["SourceIpConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RuleConditionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RuleConditionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTargetHealthOutput:
    boto3_raw_data: "type_defs.DescribeTargetHealthOutputTypeDef" = dataclasses.field()

    @cached_property
    def TargetHealthDescriptions(self):  # pragma: no cover
        return TargetHealthDescription.make_many(
            self.boto3_raw_data["TargetHealthDescriptions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTargetHealthOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTargetHealthOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLoadBalancerOutput:
    boto3_raw_data: "type_defs.CreateLoadBalancerOutputTypeDef" = dataclasses.field()

    @cached_property
    def LoadBalancers(self):  # pragma: no cover
        return LoadBalancer.make_many(self.boto3_raw_data["LoadBalancers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLoadBalancerOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLoadBalancerOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoadBalancersOutput:
    boto3_raw_data: "type_defs.DescribeLoadBalancersOutputTypeDef" = dataclasses.field()

    @cached_property
    def LoadBalancers(self):  # pragma: no cover
        return LoadBalancer.make_many(self.boto3_raw_data["LoadBalancers"])

    NextMarker = field("NextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLoadBalancersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoadBalancersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Listener:
    boto3_raw_data: "type_defs.ListenerTypeDef" = dataclasses.field()

    ListenerArn = field("ListenerArn")
    LoadBalancerArn = field("LoadBalancerArn")
    Port = field("Port")
    Protocol = field("Protocol")

    @cached_property
    def Certificates(self):  # pragma: no cover
        return Certificate.make_many(self.boto3_raw_data["Certificates"])

    SslPolicy = field("SslPolicy")

    @cached_property
    def DefaultActions(self):  # pragma: no cover
        return ActionOutput.make_many(self.boto3_raw_data["DefaultActions"])

    AlpnPolicy = field("AlpnPolicy")

    @cached_property
    def MutualAuthentication(self):  # pragma: no cover
        return MutualAuthenticationAttributes.make_one(
            self.boto3_raw_data["MutualAuthentication"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListenerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListenerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Action:
    boto3_raw_data: "type_defs.ActionTypeDef" = dataclasses.field()

    Type = field("Type")
    TargetGroupArn = field("TargetGroupArn")
    AuthenticateOidcConfig = field("AuthenticateOidcConfig")
    AuthenticateCognitoConfig = field("AuthenticateCognitoConfig")
    Order = field("Order")

    @cached_property
    def RedirectConfig(self):  # pragma: no cover
        return RedirectActionConfig.make_one(self.boto3_raw_data["RedirectConfig"])

    @cached_property
    def FixedResponseConfig(self):  # pragma: no cover
        return FixedResponseActionConfig.make_one(
            self.boto3_raw_data["FixedResponseConfig"]
        )

    ForwardConfig = field("ForwardConfig")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Rule:
    boto3_raw_data: "type_defs.RuleTypeDef" = dataclasses.field()

    RuleArn = field("RuleArn")
    Priority = field("Priority")

    @cached_property
    def Conditions(self):  # pragma: no cover
        return RuleConditionOutput.make_many(self.boto3_raw_data["Conditions"])

    @cached_property
    def Actions(self):  # pragma: no cover
        return ActionOutput.make_many(self.boto3_raw_data["Actions"])

    IsDefault = field("IsDefault")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleCondition:
    boto3_raw_data: "type_defs.RuleConditionTypeDef" = dataclasses.field()

    Field = field("Field")
    Values = field("Values")
    HostHeaderConfig = field("HostHeaderConfig")
    PathPatternConfig = field("PathPatternConfig")
    HttpHeaderConfig = field("HttpHeaderConfig")
    QueryStringConfig = field("QueryStringConfig")
    HttpRequestMethodConfig = field("HttpRequestMethodConfig")
    SourceIpConfig = field("SourceIpConfig")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleConditionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateListenerOutput:
    boto3_raw_data: "type_defs.CreateListenerOutputTypeDef" = dataclasses.field()

    @cached_property
    def Listeners(self):  # pragma: no cover
        return Listener.make_many(self.boto3_raw_data["Listeners"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateListenerOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateListenerOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeListenersOutput:
    boto3_raw_data: "type_defs.DescribeListenersOutputTypeDef" = dataclasses.field()

    @cached_property
    def Listeners(self):  # pragma: no cover
        return Listener.make_many(self.boto3_raw_data["Listeners"])

    NextMarker = field("NextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeListenersOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeListenersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyListenerOutput:
    boto3_raw_data: "type_defs.ModifyListenerOutputTypeDef" = dataclasses.field()

    @cached_property
    def Listeners(self):  # pragma: no cover
        return Listener.make_many(self.boto3_raw_data["Listeners"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyListenerOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyListenerOutputTypeDef"]
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

    @cached_property
    def Rules(self):  # pragma: no cover
        return Rule.make_many(self.boto3_raw_data["Rules"])

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
class DescribeRulesOutput:
    boto3_raw_data: "type_defs.DescribeRulesOutputTypeDef" = dataclasses.field()

    @cached_property
    def Rules(self):  # pragma: no cover
        return Rule.make_many(self.boto3_raw_data["Rules"])

    NextMarker = field("NextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeRulesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeRulesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyRuleOutput:
    boto3_raw_data: "type_defs.ModifyRuleOutputTypeDef" = dataclasses.field()

    @cached_property
    def Rules(self):  # pragma: no cover
        return Rule.make_many(self.boto3_raw_data["Rules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ModifyRuleOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetRulePrioritiesOutput:
    boto3_raw_data: "type_defs.SetRulePrioritiesOutputTypeDef" = dataclasses.field()

    @cached_property
    def Rules(self):  # pragma: no cover
        return Rule.make_many(self.boto3_raw_data["Rules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetRulePrioritiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetRulePrioritiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateListenerInput:
    boto3_raw_data: "type_defs.CreateListenerInputTypeDef" = dataclasses.field()

    LoadBalancerArn = field("LoadBalancerArn")
    DefaultActions = field("DefaultActions")
    Protocol = field("Protocol")
    Port = field("Port")
    SslPolicy = field("SslPolicy")

    @cached_property
    def Certificates(self):  # pragma: no cover
        return Certificate.make_many(self.boto3_raw_data["Certificates"])

    AlpnPolicy = field("AlpnPolicy")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def MutualAuthentication(self):  # pragma: no cover
        return MutualAuthenticationAttributes.make_one(
            self.boto3_raw_data["MutualAuthentication"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateListenerInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateListenerInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyListenerInput:
    boto3_raw_data: "type_defs.ModifyListenerInputTypeDef" = dataclasses.field()

    ListenerArn = field("ListenerArn")
    Port = field("Port")
    Protocol = field("Protocol")
    SslPolicy = field("SslPolicy")

    @cached_property
    def Certificates(self):  # pragma: no cover
        return Certificate.make_many(self.boto3_raw_data["Certificates"])

    DefaultActions = field("DefaultActions")
    AlpnPolicy = field("AlpnPolicy")

    @cached_property
    def MutualAuthentication(self):  # pragma: no cover
        return MutualAuthenticationAttributes.make_one(
            self.boto3_raw_data["MutualAuthentication"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModifyListenerInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyListenerInputTypeDef"]
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

    ListenerArn = field("ListenerArn")
    Conditions = field("Conditions")
    Priority = field("Priority")
    Actions = field("Actions")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

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
class ModifyRuleInput:
    boto3_raw_data: "type_defs.ModifyRuleInputTypeDef" = dataclasses.field()

    RuleArn = field("RuleArn")
    Conditions = field("Conditions")
    Actions = field("Actions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ModifyRuleInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ModifyRuleInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
