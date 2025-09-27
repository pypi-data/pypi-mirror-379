# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_route53 import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccountLimit:
    boto3_raw_data: "type_defs.AccountLimitTypeDef" = dataclasses.field()

    Type = field("Type")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountLimitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountLimitTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivateKeySigningKeyRequest:
    boto3_raw_data: "type_defs.ActivateKeySigningKeyRequestTypeDef" = (
        dataclasses.field()
    )

    HostedZoneId = field("HostedZoneId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActivateKeySigningKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivateKeySigningKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeInfo:
    boto3_raw_data: "type_defs.ChangeInfoTypeDef" = dataclasses.field()

    Id = field("Id")
    Status = field("Status")
    SubmittedAt = field("SubmittedAt")
    Comment = field("Comment")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChangeInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChangeInfoTypeDef"]]
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
class AlarmIdentifier:
    boto3_raw_data: "type_defs.AlarmIdentifierTypeDef" = dataclasses.field()

    Region = field("Region")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AlarmIdentifierTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AlarmIdentifierTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AliasTarget:
    boto3_raw_data: "type_defs.AliasTargetTypeDef" = dataclasses.field()

    HostedZoneId = field("HostedZoneId")
    DNSName = field("DNSName")
    EvaluateTargetHealth = field("EvaluateTargetHealth")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AliasTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AliasTargetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VPC:
    boto3_raw_data: "type_defs.VPCTypeDef" = dataclasses.field()

    VPCRegion = field("VPCRegion")
    VPCId = field("VPCId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VPCTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VPCTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CidrCollectionChange:
    boto3_raw_data: "type_defs.CidrCollectionChangeTypeDef" = dataclasses.field()

    LocationName = field("LocationName")
    Action = field("Action")
    CidrList = field("CidrList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CidrCollectionChangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CidrCollectionChangeTypeDef"]
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
class CidrBlockSummary:
    boto3_raw_data: "type_defs.CidrBlockSummaryTypeDef" = dataclasses.field()

    CidrBlock = field("CidrBlock")
    LocationName = field("LocationName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CidrBlockSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CidrBlockSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CidrCollection:
    boto3_raw_data: "type_defs.CidrCollectionTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Id = field("Id")
    Name = field("Name")
    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CidrCollectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CidrCollectionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CidrRoutingConfig:
    boto3_raw_data: "type_defs.CidrRoutingConfigTypeDef" = dataclasses.field()

    CollectionId = field("CollectionId")
    LocationName = field("LocationName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CidrRoutingConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CidrRoutingConfigTypeDef"]
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

    Name = field("Name")
    Value = field("Value")

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
class CollectionSummary:
    boto3_raw_data: "type_defs.CollectionSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Id = field("Id")
    Name = field("Name")
    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CollectionSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollectionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Coordinates:
    boto3_raw_data: "type_defs.CoordinatesTypeDef" = dataclasses.field()

    Latitude = field("Latitude")
    Longitude = field("Longitude")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CoordinatesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CoordinatesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCidrCollectionRequest:
    boto3_raw_data: "type_defs.CreateCidrCollectionRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    CallerReference = field("CallerReference")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCidrCollectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCidrCollectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HostedZoneConfig:
    boto3_raw_data: "type_defs.HostedZoneConfigTypeDef" = dataclasses.field()

    Comment = field("Comment")
    PrivateZone = field("PrivateZone")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HostedZoneConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HostedZoneConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DelegationSet:
    boto3_raw_data: "type_defs.DelegationSetTypeDef" = dataclasses.field()

    NameServers = field("NameServers")
    Id = field("Id")
    CallerReference = field("CallerReference")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DelegationSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DelegationSetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKeySigningKeyRequest:
    boto3_raw_data: "type_defs.CreateKeySigningKeyRequestTypeDef" = dataclasses.field()

    CallerReference = field("CallerReference")
    HostedZoneId = field("HostedZoneId")
    KeyManagementServiceArn = field("KeyManagementServiceArn")
    Name = field("Name")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKeySigningKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKeySigningKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeySigningKey:
    boto3_raw_data: "type_defs.KeySigningKeyTypeDef" = dataclasses.field()

    Name = field("Name")
    KmsArn = field("KmsArn")
    Flag = field("Flag")
    SigningAlgorithmMnemonic = field("SigningAlgorithmMnemonic")
    SigningAlgorithmType = field("SigningAlgorithmType")
    DigestAlgorithmMnemonic = field("DigestAlgorithmMnemonic")
    DigestAlgorithmType = field("DigestAlgorithmType")
    KeyTag = field("KeyTag")
    DigestValue = field("DigestValue")
    PublicKey = field("PublicKey")
    DSRecord = field("DSRecord")
    DNSKEYRecord = field("DNSKEYRecord")
    Status = field("Status")
    StatusMessage = field("StatusMessage")
    CreatedDate = field("CreatedDate")
    LastModifiedDate = field("LastModifiedDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeySigningKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeySigningKeyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateQueryLoggingConfigRequest:
    boto3_raw_data: "type_defs.CreateQueryLoggingConfigRequestTypeDef" = (
        dataclasses.field()
    )

    HostedZoneId = field("HostedZoneId")
    CloudWatchLogsLogGroupArn = field("CloudWatchLogsLogGroupArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateQueryLoggingConfigRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateQueryLoggingConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryLoggingConfig:
    boto3_raw_data: "type_defs.QueryLoggingConfigTypeDef" = dataclasses.field()

    Id = field("Id")
    HostedZoneId = field("HostedZoneId")
    CloudWatchLogsLogGroupArn = field("CloudWatchLogsLogGroupArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryLoggingConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryLoggingConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReusableDelegationSetRequest:
    boto3_raw_data: "type_defs.CreateReusableDelegationSetRequestTypeDef" = (
        dataclasses.field()
    )

    CallerReference = field("CallerReference")
    HostedZoneId = field("HostedZoneId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateReusableDelegationSetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReusableDelegationSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrafficPolicyInstanceRequest:
    boto3_raw_data: "type_defs.CreateTrafficPolicyInstanceRequestTypeDef" = (
        dataclasses.field()
    )

    HostedZoneId = field("HostedZoneId")
    Name = field("Name")
    TTL = field("TTL")
    TrafficPolicyId = field("TrafficPolicyId")
    TrafficPolicyVersion = field("TrafficPolicyVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateTrafficPolicyInstanceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrafficPolicyInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrafficPolicyInstance:
    boto3_raw_data: "type_defs.TrafficPolicyInstanceTypeDef" = dataclasses.field()

    Id = field("Id")
    HostedZoneId = field("HostedZoneId")
    Name = field("Name")
    TTL = field("TTL")
    State = field("State")
    Message = field("Message")
    TrafficPolicyId = field("TrafficPolicyId")
    TrafficPolicyVersion = field("TrafficPolicyVersion")
    TrafficPolicyType = field("TrafficPolicyType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrafficPolicyInstanceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrafficPolicyInstanceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrafficPolicyRequest:
    boto3_raw_data: "type_defs.CreateTrafficPolicyRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Document = field("Document")
    Comment = field("Comment")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTrafficPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrafficPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrafficPolicy:
    boto3_raw_data: "type_defs.TrafficPolicyTypeDef" = dataclasses.field()

    Id = field("Id")
    Version = field("Version")
    Name = field("Name")
    Type = field("Type")
    Document = field("Document")
    Comment = field("Comment")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrafficPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TrafficPolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrafficPolicyVersionRequest:
    boto3_raw_data: "type_defs.CreateTrafficPolicyVersionRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Document = field("Document")
    Comment = field("Comment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateTrafficPolicyVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrafficPolicyVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DNSSECStatus:
    boto3_raw_data: "type_defs.DNSSECStatusTypeDef" = dataclasses.field()

    ServeSignature = field("ServeSignature")
    StatusMessage = field("StatusMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DNSSECStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DNSSECStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeactivateKeySigningKeyRequest:
    boto3_raw_data: "type_defs.DeactivateKeySigningKeyRequestTypeDef" = (
        dataclasses.field()
    )

    HostedZoneId = field("HostedZoneId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeactivateKeySigningKeyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeactivateKeySigningKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCidrCollectionRequest:
    boto3_raw_data: "type_defs.DeleteCidrCollectionRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCidrCollectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCidrCollectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteHealthCheckRequest:
    boto3_raw_data: "type_defs.DeleteHealthCheckRequestTypeDef" = dataclasses.field()

    HealthCheckId = field("HealthCheckId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteHealthCheckRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteHealthCheckRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteHostedZoneRequest:
    boto3_raw_data: "type_defs.DeleteHostedZoneRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteHostedZoneRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteHostedZoneRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKeySigningKeyRequest:
    boto3_raw_data: "type_defs.DeleteKeySigningKeyRequestTypeDef" = dataclasses.field()

    HostedZoneId = field("HostedZoneId")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteKeySigningKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKeySigningKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteQueryLoggingConfigRequest:
    boto3_raw_data: "type_defs.DeleteQueryLoggingConfigRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteQueryLoggingConfigRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteQueryLoggingConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteReusableDelegationSetRequest:
    boto3_raw_data: "type_defs.DeleteReusableDelegationSetRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteReusableDelegationSetRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteReusableDelegationSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTrafficPolicyInstanceRequest:
    boto3_raw_data: "type_defs.DeleteTrafficPolicyInstanceRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteTrafficPolicyInstanceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTrafficPolicyInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTrafficPolicyRequest:
    boto3_raw_data: "type_defs.DeleteTrafficPolicyRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTrafficPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTrafficPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableHostedZoneDNSSECRequest:
    boto3_raw_data: "type_defs.DisableHostedZoneDNSSECRequestTypeDef" = (
        dataclasses.field()
    )

    HostedZoneId = field("HostedZoneId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisableHostedZoneDNSSECRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableHostedZoneDNSSECRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableHostedZoneDNSSECRequest:
    boto3_raw_data: "type_defs.EnableHostedZoneDNSSECRequestTypeDef" = (
        dataclasses.field()
    )

    HostedZoneId = field("HostedZoneId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EnableHostedZoneDNSSECRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableHostedZoneDNSSECRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeoLocationDetails:
    boto3_raw_data: "type_defs.GeoLocationDetailsTypeDef" = dataclasses.field()

    ContinentCode = field("ContinentCode")
    ContinentName = field("ContinentName")
    CountryCode = field("CountryCode")
    CountryName = field("CountryName")
    SubdivisionCode = field("SubdivisionCode")
    SubdivisionName = field("SubdivisionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GeoLocationDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeoLocationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeoLocation:
    boto3_raw_data: "type_defs.GeoLocationTypeDef" = dataclasses.field()

    ContinentCode = field("ContinentCode")
    CountryCode = field("CountryCode")
    SubdivisionCode = field("SubdivisionCode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GeoLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GeoLocationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccountLimitRequest:
    boto3_raw_data: "type_defs.GetAccountLimitRequestTypeDef" = dataclasses.field()

    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccountLimitRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountLimitRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChangeRequest:
    boto3_raw_data: "type_defs.GetChangeRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetChangeRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChangeRequestTypeDef"]
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
class GetDNSSECRequest:
    boto3_raw_data: "type_defs.GetDNSSECRequestTypeDef" = dataclasses.field()

    HostedZoneId = field("HostedZoneId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDNSSECRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDNSSECRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGeoLocationRequest:
    boto3_raw_data: "type_defs.GetGeoLocationRequestTypeDef" = dataclasses.field()

    ContinentCode = field("ContinentCode")
    CountryCode = field("CountryCode")
    SubdivisionCode = field("SubdivisionCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGeoLocationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGeoLocationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHealthCheckLastFailureReasonRequest:
    boto3_raw_data: "type_defs.GetHealthCheckLastFailureReasonRequestTypeDef" = (
        dataclasses.field()
    )

    HealthCheckId = field("HealthCheckId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetHealthCheckLastFailureReasonRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetHealthCheckLastFailureReasonRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHealthCheckRequest:
    boto3_raw_data: "type_defs.GetHealthCheckRequestTypeDef" = dataclasses.field()

    HealthCheckId = field("HealthCheckId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetHealthCheckRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetHealthCheckRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHealthCheckStatusRequest:
    boto3_raw_data: "type_defs.GetHealthCheckStatusRequestTypeDef" = dataclasses.field()

    HealthCheckId = field("HealthCheckId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetHealthCheckStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetHealthCheckStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHostedZoneLimitRequest:
    boto3_raw_data: "type_defs.GetHostedZoneLimitRequestTypeDef" = dataclasses.field()

    Type = field("Type")
    HostedZoneId = field("HostedZoneId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetHostedZoneLimitRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetHostedZoneLimitRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HostedZoneLimit:
    boto3_raw_data: "type_defs.HostedZoneLimitTypeDef" = dataclasses.field()

    Type = field("Type")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HostedZoneLimitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HostedZoneLimitTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHostedZoneRequest:
    boto3_raw_data: "type_defs.GetHostedZoneRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetHostedZoneRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetHostedZoneRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryLoggingConfigRequest:
    boto3_raw_data: "type_defs.GetQueryLoggingConfigRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQueryLoggingConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueryLoggingConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReusableDelegationSetLimitRequest:
    boto3_raw_data: "type_defs.GetReusableDelegationSetLimitRequestTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")
    DelegationSetId = field("DelegationSetId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetReusableDelegationSetLimitRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReusableDelegationSetLimitRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReusableDelegationSetLimit:
    boto3_raw_data: "type_defs.ReusableDelegationSetLimitTypeDef" = dataclasses.field()

    Type = field("Type")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReusableDelegationSetLimitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReusableDelegationSetLimitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReusableDelegationSetRequest:
    boto3_raw_data: "type_defs.GetReusableDelegationSetRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetReusableDelegationSetRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReusableDelegationSetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrafficPolicyInstanceRequest:
    boto3_raw_data: "type_defs.GetTrafficPolicyInstanceRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetTrafficPolicyInstanceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrafficPolicyInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrafficPolicyRequest:
    boto3_raw_data: "type_defs.GetTrafficPolicyRequestTypeDef" = dataclasses.field()

    Id = field("Id")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTrafficPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrafficPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatusReport:
    boto3_raw_data: "type_defs.StatusReportTypeDef" = dataclasses.field()

    Status = field("Status")
    CheckedTime = field("CheckedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatusReportTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatusReportTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LinkedService:
    boto3_raw_data: "type_defs.LinkedServiceTypeDef" = dataclasses.field()

    ServicePrincipal = field("ServicePrincipal")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LinkedServiceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LinkedServiceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HostedZoneOwner:
    boto3_raw_data: "type_defs.HostedZoneOwnerTypeDef" = dataclasses.field()

    OwningAccount = field("OwningAccount")
    OwningService = field("OwningService")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HostedZoneOwnerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HostedZoneOwnerTypeDef"]],
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
class ListCidrBlocksRequest:
    boto3_raw_data: "type_defs.ListCidrBlocksRequestTypeDef" = dataclasses.field()

    CollectionId = field("CollectionId")
    LocationName = field("LocationName")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCidrBlocksRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCidrBlocksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCidrCollectionsRequest:
    boto3_raw_data: "type_defs.ListCidrCollectionsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCidrCollectionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCidrCollectionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCidrLocationsRequest:
    boto3_raw_data: "type_defs.ListCidrLocationsRequestTypeDef" = dataclasses.field()

    CollectionId = field("CollectionId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCidrLocationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCidrLocationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LocationSummary:
    boto3_raw_data: "type_defs.LocationSummaryTypeDef" = dataclasses.field()

    LocationName = field("LocationName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LocationSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LocationSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGeoLocationsRequest:
    boto3_raw_data: "type_defs.ListGeoLocationsRequestTypeDef" = dataclasses.field()

    StartContinentCode = field("StartContinentCode")
    StartCountryCode = field("StartCountryCode")
    StartSubdivisionCode = field("StartSubdivisionCode")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGeoLocationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGeoLocationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHealthChecksRequest:
    boto3_raw_data: "type_defs.ListHealthChecksRequestTypeDef" = dataclasses.field()

    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListHealthChecksRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHealthChecksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHostedZonesByNameRequest:
    boto3_raw_data: "type_defs.ListHostedZonesByNameRequestTypeDef" = (
        dataclasses.field()
    )

    DNSName = field("DNSName")
    HostedZoneId = field("HostedZoneId")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListHostedZonesByNameRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHostedZonesByNameRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHostedZonesByVPCRequest:
    boto3_raw_data: "type_defs.ListHostedZonesByVPCRequestTypeDef" = dataclasses.field()

    VPCId = field("VPCId")
    VPCRegion = field("VPCRegion")
    MaxItems = field("MaxItems")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListHostedZonesByVPCRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHostedZonesByVPCRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHostedZonesRequest:
    boto3_raw_data: "type_defs.ListHostedZonesRequestTypeDef" = dataclasses.field()

    Marker = field("Marker")
    MaxItems = field("MaxItems")
    DelegationSetId = field("DelegationSetId")
    HostedZoneType = field("HostedZoneType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListHostedZonesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHostedZonesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueryLoggingConfigsRequest:
    boto3_raw_data: "type_defs.ListQueryLoggingConfigsRequestTypeDef" = (
        dataclasses.field()
    )

    HostedZoneId = field("HostedZoneId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListQueryLoggingConfigsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueryLoggingConfigsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceRecordSetsRequest:
    boto3_raw_data: "type_defs.ListResourceRecordSetsRequestTypeDef" = (
        dataclasses.field()
    )

    HostedZoneId = field("HostedZoneId")
    StartRecordName = field("StartRecordName")
    StartRecordType = field("StartRecordType")
    StartRecordIdentifier = field("StartRecordIdentifier")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResourceRecordSetsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceRecordSetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReusableDelegationSetsRequest:
    boto3_raw_data: "type_defs.ListReusableDelegationSetsRequestTypeDef" = (
        dataclasses.field()
    )

    Marker = field("Marker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListReusableDelegationSetsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReusableDelegationSetsRequestTypeDef"]
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

    ResourceType = field("ResourceType")
    ResourceId = field("ResourceId")

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
class ListTagsForResourcesRequest:
    boto3_raw_data: "type_defs.ListTagsForResourcesRequestTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    ResourceIds = field("ResourceIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourcesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrafficPoliciesRequest:
    boto3_raw_data: "type_defs.ListTrafficPoliciesRequestTypeDef" = dataclasses.field()

    TrafficPolicyIdMarker = field("TrafficPolicyIdMarker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTrafficPoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrafficPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrafficPolicySummary:
    boto3_raw_data: "type_defs.TrafficPolicySummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Type = field("Type")
    LatestVersion = field("LatestVersion")
    TrafficPolicyCount = field("TrafficPolicyCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TrafficPolicySummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrafficPolicySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrafficPolicyInstancesByHostedZoneRequest:
    boto3_raw_data: "type_defs.ListTrafficPolicyInstancesByHostedZoneRequestTypeDef" = (
        dataclasses.field()
    )

    HostedZoneId = field("HostedZoneId")
    TrafficPolicyInstanceNameMarker = field("TrafficPolicyInstanceNameMarker")
    TrafficPolicyInstanceTypeMarker = field("TrafficPolicyInstanceTypeMarker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTrafficPolicyInstancesByHostedZoneRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrafficPolicyInstancesByHostedZoneRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrafficPolicyInstancesByPolicyRequest:
    boto3_raw_data: "type_defs.ListTrafficPolicyInstancesByPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    TrafficPolicyId = field("TrafficPolicyId")
    TrafficPolicyVersion = field("TrafficPolicyVersion")
    HostedZoneIdMarker = field("HostedZoneIdMarker")
    TrafficPolicyInstanceNameMarker = field("TrafficPolicyInstanceNameMarker")
    TrafficPolicyInstanceTypeMarker = field("TrafficPolicyInstanceTypeMarker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTrafficPolicyInstancesByPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrafficPolicyInstancesByPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrafficPolicyInstancesRequest:
    boto3_raw_data: "type_defs.ListTrafficPolicyInstancesRequestTypeDef" = (
        dataclasses.field()
    )

    HostedZoneIdMarker = field("HostedZoneIdMarker")
    TrafficPolicyInstanceNameMarker = field("TrafficPolicyInstanceNameMarker")
    TrafficPolicyInstanceTypeMarker = field("TrafficPolicyInstanceTypeMarker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTrafficPolicyInstancesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrafficPolicyInstancesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrafficPolicyVersionsRequest:
    boto3_raw_data: "type_defs.ListTrafficPolicyVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    TrafficPolicyVersionMarker = field("TrafficPolicyVersionMarker")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTrafficPolicyVersionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrafficPolicyVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVPCAssociationAuthorizationsRequest:
    boto3_raw_data: "type_defs.ListVPCAssociationAuthorizationsRequestTypeDef" = (
        dataclasses.field()
    )

    HostedZoneId = field("HostedZoneId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListVPCAssociationAuthorizationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVPCAssociationAuthorizationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceRecord:
    boto3_raw_data: "type_defs.ResourceRecordTypeDef" = dataclasses.field()

    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceRecordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceRecordTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestDNSAnswerRequest:
    boto3_raw_data: "type_defs.TestDNSAnswerRequestTypeDef" = dataclasses.field()

    HostedZoneId = field("HostedZoneId")
    RecordName = field("RecordName")
    RecordType = field("RecordType")
    ResolverIP = field("ResolverIP")
    EDNS0ClientSubnetIP = field("EDNS0ClientSubnetIP")
    EDNS0ClientSubnetMask = field("EDNS0ClientSubnetMask")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestDNSAnswerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestDNSAnswerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateHostedZoneCommentRequest:
    boto3_raw_data: "type_defs.UpdateHostedZoneCommentRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Comment = field("Comment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateHostedZoneCommentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateHostedZoneCommentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTrafficPolicyCommentRequest:
    boto3_raw_data: "type_defs.UpdateTrafficPolicyCommentRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    Version = field("Version")
    Comment = field("Comment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateTrafficPolicyCommentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTrafficPolicyCommentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTrafficPolicyInstanceRequest:
    boto3_raw_data: "type_defs.UpdateTrafficPolicyInstanceRequestTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")
    TTL = field("TTL")
    TrafficPolicyId = field("TrafficPolicyId")
    TrafficPolicyVersion = field("TrafficPolicyVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateTrafficPolicyInstanceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTrafficPolicyInstanceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivateKeySigningKeyResponse:
    boto3_raw_data: "type_defs.ActivateKeySigningKeyResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ChangeInfo(self):  # pragma: no cover
        return ChangeInfo.make_one(self.boto3_raw_data["ChangeInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ActivateKeySigningKeyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivateKeySigningKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateVPCWithHostedZoneResponse:
    boto3_raw_data: "type_defs.AssociateVPCWithHostedZoneResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ChangeInfo(self):  # pragma: no cover
        return ChangeInfo.make_one(self.boto3_raw_data["ChangeInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateVPCWithHostedZoneResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateVPCWithHostedZoneResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeCidrCollectionResponse:
    boto3_raw_data: "type_defs.ChangeCidrCollectionResponseTypeDef" = (
        dataclasses.field()
    )

    Id = field("Id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChangeCidrCollectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChangeCidrCollectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeResourceRecordSetsResponse:
    boto3_raw_data: "type_defs.ChangeResourceRecordSetsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ChangeInfo(self):  # pragma: no cover
        return ChangeInfo.make_one(self.boto3_raw_data["ChangeInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ChangeResourceRecordSetsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChangeResourceRecordSetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeactivateKeySigningKeyResponse:
    boto3_raw_data: "type_defs.DeactivateKeySigningKeyResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ChangeInfo(self):  # pragma: no cover
        return ChangeInfo.make_one(self.boto3_raw_data["ChangeInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeactivateKeySigningKeyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeactivateKeySigningKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteHostedZoneResponse:
    boto3_raw_data: "type_defs.DeleteHostedZoneResponseTypeDef" = dataclasses.field()

    @cached_property
    def ChangeInfo(self):  # pragma: no cover
        return ChangeInfo.make_one(self.boto3_raw_data["ChangeInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteHostedZoneResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteHostedZoneResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKeySigningKeyResponse:
    boto3_raw_data: "type_defs.DeleteKeySigningKeyResponseTypeDef" = dataclasses.field()

    @cached_property
    def ChangeInfo(self):  # pragma: no cover
        return ChangeInfo.make_one(self.boto3_raw_data["ChangeInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteKeySigningKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKeySigningKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableHostedZoneDNSSECResponse:
    boto3_raw_data: "type_defs.DisableHostedZoneDNSSECResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ChangeInfo(self):  # pragma: no cover
        return ChangeInfo.make_one(self.boto3_raw_data["ChangeInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisableHostedZoneDNSSECResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableHostedZoneDNSSECResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateVPCFromHostedZoneResponse:
    boto3_raw_data: "type_defs.DisassociateVPCFromHostedZoneResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ChangeInfo(self):  # pragma: no cover
        return ChangeInfo.make_one(self.boto3_raw_data["ChangeInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateVPCFromHostedZoneResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateVPCFromHostedZoneResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableHostedZoneDNSSECResponse:
    boto3_raw_data: "type_defs.EnableHostedZoneDNSSECResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ChangeInfo(self):  # pragma: no cover
        return ChangeInfo.make_one(self.boto3_raw_data["ChangeInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EnableHostedZoneDNSSECResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableHostedZoneDNSSECResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccountLimitResponse:
    boto3_raw_data: "type_defs.GetAccountLimitResponseTypeDef" = dataclasses.field()

    @cached_property
    def Limit(self):  # pragma: no cover
        return AccountLimit.make_one(self.boto3_raw_data["Limit"])

    Count = field("Count")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccountLimitResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountLimitResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChangeResponse:
    boto3_raw_data: "type_defs.GetChangeResponseTypeDef" = dataclasses.field()

    @cached_property
    def ChangeInfo(self):  # pragma: no cover
        return ChangeInfo.make_one(self.boto3_raw_data["ChangeInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetChangeResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChangeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCheckerIpRangesResponse:
    boto3_raw_data: "type_defs.GetCheckerIpRangesResponseTypeDef" = dataclasses.field()

    CheckerIpRanges = field("CheckerIpRanges")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCheckerIpRangesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCheckerIpRangesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHealthCheckCountResponse:
    boto3_raw_data: "type_defs.GetHealthCheckCountResponseTypeDef" = dataclasses.field()

    HealthCheckCount = field("HealthCheckCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetHealthCheckCountResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetHealthCheckCountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHostedZoneCountResponse:
    boto3_raw_data: "type_defs.GetHostedZoneCountResponseTypeDef" = dataclasses.field()

    HostedZoneCount = field("HostedZoneCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetHostedZoneCountResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetHostedZoneCountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrafficPolicyInstanceCountResponse:
    boto3_raw_data: "type_defs.GetTrafficPolicyInstanceCountResponseTypeDef" = (
        dataclasses.field()
    )

    TrafficPolicyInstanceCount = field("TrafficPolicyInstanceCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTrafficPolicyInstanceCountResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrafficPolicyInstanceCountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestDNSAnswerResponse:
    boto3_raw_data: "type_defs.TestDNSAnswerResponseTypeDef" = dataclasses.field()

    Nameserver = field("Nameserver")
    RecordName = field("RecordName")
    RecordType = field("RecordType")
    RecordData = field("RecordData")
    ResponseCode = field("ResponseCode")
    Protocol = field("Protocol")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestDNSAnswerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestDNSAnswerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HealthCheckConfigOutput:
    boto3_raw_data: "type_defs.HealthCheckConfigOutputTypeDef" = dataclasses.field()

    Type = field("Type")
    IPAddress = field("IPAddress")
    Port = field("Port")
    ResourcePath = field("ResourcePath")
    FullyQualifiedDomainName = field("FullyQualifiedDomainName")
    SearchString = field("SearchString")
    RequestInterval = field("RequestInterval")
    FailureThreshold = field("FailureThreshold")
    MeasureLatency = field("MeasureLatency")
    Inverted = field("Inverted")
    Disabled = field("Disabled")
    HealthThreshold = field("HealthThreshold")
    ChildHealthChecks = field("ChildHealthChecks")
    EnableSNI = field("EnableSNI")
    Regions = field("Regions")

    @cached_property
    def AlarmIdentifier(self):  # pragma: no cover
        return AlarmIdentifier.make_one(self.boto3_raw_data["AlarmIdentifier"])

    InsufficientDataHealthStatus = field("InsufficientDataHealthStatus")
    RoutingControlArn = field("RoutingControlArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HealthCheckConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HealthCheckConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HealthCheckConfig:
    boto3_raw_data: "type_defs.HealthCheckConfigTypeDef" = dataclasses.field()

    Type = field("Type")
    IPAddress = field("IPAddress")
    Port = field("Port")
    ResourcePath = field("ResourcePath")
    FullyQualifiedDomainName = field("FullyQualifiedDomainName")
    SearchString = field("SearchString")
    RequestInterval = field("RequestInterval")
    FailureThreshold = field("FailureThreshold")
    MeasureLatency = field("MeasureLatency")
    Inverted = field("Inverted")
    Disabled = field("Disabled")
    HealthThreshold = field("HealthThreshold")
    ChildHealthChecks = field("ChildHealthChecks")
    EnableSNI = field("EnableSNI")
    Regions = field("Regions")

    @cached_property
    def AlarmIdentifier(self):  # pragma: no cover
        return AlarmIdentifier.make_one(self.boto3_raw_data["AlarmIdentifier"])

    InsufficientDataHealthStatus = field("InsufficientDataHealthStatus")
    RoutingControlArn = field("RoutingControlArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HealthCheckConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HealthCheckConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateHealthCheckRequest:
    boto3_raw_data: "type_defs.UpdateHealthCheckRequestTypeDef" = dataclasses.field()

    HealthCheckId = field("HealthCheckId")
    HealthCheckVersion = field("HealthCheckVersion")
    IPAddress = field("IPAddress")
    Port = field("Port")
    ResourcePath = field("ResourcePath")
    FullyQualifiedDomainName = field("FullyQualifiedDomainName")
    SearchString = field("SearchString")
    FailureThreshold = field("FailureThreshold")
    Inverted = field("Inverted")
    Disabled = field("Disabled")
    HealthThreshold = field("HealthThreshold")
    ChildHealthChecks = field("ChildHealthChecks")
    EnableSNI = field("EnableSNI")
    Regions = field("Regions")

    @cached_property
    def AlarmIdentifier(self):  # pragma: no cover
        return AlarmIdentifier.make_one(self.boto3_raw_data["AlarmIdentifier"])

    InsufficientDataHealthStatus = field("InsufficientDataHealthStatus")
    ResetElements = field("ResetElements")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateHealthCheckRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateHealthCheckRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateVPCWithHostedZoneRequest:
    boto3_raw_data: "type_defs.AssociateVPCWithHostedZoneRequestTypeDef" = (
        dataclasses.field()
    )

    HostedZoneId = field("HostedZoneId")

    @cached_property
    def VPC(self):  # pragma: no cover
        return VPC.make_one(self.boto3_raw_data["VPC"])

    Comment = field("Comment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateVPCWithHostedZoneRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateVPCWithHostedZoneRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVPCAssociationAuthorizationRequest:
    boto3_raw_data: "type_defs.CreateVPCAssociationAuthorizationRequestTypeDef" = (
        dataclasses.field()
    )

    HostedZoneId = field("HostedZoneId")

    @cached_property
    def VPC(self):  # pragma: no cover
        return VPC.make_one(self.boto3_raw_data["VPC"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateVPCAssociationAuthorizationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVPCAssociationAuthorizationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVPCAssociationAuthorizationResponse:
    boto3_raw_data: "type_defs.CreateVPCAssociationAuthorizationResponseTypeDef" = (
        dataclasses.field()
    )

    HostedZoneId = field("HostedZoneId")

    @cached_property
    def VPC(self):  # pragma: no cover
        return VPC.make_one(self.boto3_raw_data["VPC"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateVPCAssociationAuthorizationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVPCAssociationAuthorizationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVPCAssociationAuthorizationRequest:
    boto3_raw_data: "type_defs.DeleteVPCAssociationAuthorizationRequestTypeDef" = (
        dataclasses.field()
    )

    HostedZoneId = field("HostedZoneId")

    @cached_property
    def VPC(self):  # pragma: no cover
        return VPC.make_one(self.boto3_raw_data["VPC"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteVPCAssociationAuthorizationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVPCAssociationAuthorizationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateVPCFromHostedZoneRequest:
    boto3_raw_data: "type_defs.DisassociateVPCFromHostedZoneRequestTypeDef" = (
        dataclasses.field()
    )

    HostedZoneId = field("HostedZoneId")

    @cached_property
    def VPC(self):  # pragma: no cover
        return VPC.make_one(self.boto3_raw_data["VPC"])

    Comment = field("Comment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateVPCFromHostedZoneRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateVPCFromHostedZoneRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVPCAssociationAuthorizationsResponse:
    boto3_raw_data: "type_defs.ListVPCAssociationAuthorizationsResponseTypeDef" = (
        dataclasses.field()
    )

    HostedZoneId = field("HostedZoneId")

    @cached_property
    def VPCs(self):  # pragma: no cover
        return VPC.make_many(self.boto3_raw_data["VPCs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListVPCAssociationAuthorizationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVPCAssociationAuthorizationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeCidrCollectionRequest:
    boto3_raw_data: "type_defs.ChangeCidrCollectionRequestTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def Changes(self):  # pragma: no cover
        return CidrCollectionChange.make_many(self.boto3_raw_data["Changes"])

    CollectionVersion = field("CollectionVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChangeCidrCollectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChangeCidrCollectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeTagsForResourceRequest:
    boto3_raw_data: "type_defs.ChangeTagsForResourceRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceType = field("ResourceType")
    ResourceId = field("ResourceId")

    @cached_property
    def AddTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["AddTags"])

    RemoveTagKeys = field("RemoveTagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChangeTagsForResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChangeTagsForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceTagSet:
    boto3_raw_data: "type_defs.ResourceTagSetTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    ResourceId = field("ResourceId")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceTagSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceTagSetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCidrBlocksResponse:
    boto3_raw_data: "type_defs.ListCidrBlocksResponseTypeDef" = dataclasses.field()

    @cached_property
    def CidrBlocks(self):  # pragma: no cover
        return CidrBlockSummary.make_many(self.boto3_raw_data["CidrBlocks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCidrBlocksResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCidrBlocksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCidrCollectionResponse:
    boto3_raw_data: "type_defs.CreateCidrCollectionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Collection(self):  # pragma: no cover
        return CidrCollection.make_one(self.boto3_raw_data["Collection"])

    Location = field("Location")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCidrCollectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCidrCollectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudWatchAlarmConfiguration:
    boto3_raw_data: "type_defs.CloudWatchAlarmConfigurationTypeDef" = (
        dataclasses.field()
    )

    EvaluationPeriods = field("EvaluationPeriods")
    Threshold = field("Threshold")
    ComparisonOperator = field("ComparisonOperator")
    Period = field("Period")
    MetricName = field("MetricName")
    Namespace = field("Namespace")
    Statistic = field("Statistic")

    @cached_property
    def Dimensions(self):  # pragma: no cover
        return Dimension.make_many(self.boto3_raw_data["Dimensions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudWatchAlarmConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchAlarmConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCidrCollectionsResponse:
    boto3_raw_data: "type_defs.ListCidrCollectionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def CidrCollections(self):  # pragma: no cover
        return CollectionSummary.make_many(self.boto3_raw_data["CidrCollections"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCidrCollectionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCidrCollectionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GeoProximityLocation:
    boto3_raw_data: "type_defs.GeoProximityLocationTypeDef" = dataclasses.field()

    AWSRegion = field("AWSRegion")
    LocalZoneGroup = field("LocalZoneGroup")

    @cached_property
    def Coordinates(self):  # pragma: no cover
        return Coordinates.make_one(self.boto3_raw_data["Coordinates"])

    Bias = field("Bias")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GeoProximityLocationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GeoProximityLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateHostedZoneRequest:
    boto3_raw_data: "type_defs.CreateHostedZoneRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    CallerReference = field("CallerReference")

    @cached_property
    def VPC(self):  # pragma: no cover
        return VPC.make_one(self.boto3_raw_data["VPC"])

    @cached_property
    def HostedZoneConfig(self):  # pragma: no cover
        return HostedZoneConfig.make_one(self.boto3_raw_data["HostedZoneConfig"])

    DelegationSetId = field("DelegationSetId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateHostedZoneRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHostedZoneRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateReusableDelegationSetResponse:
    boto3_raw_data: "type_defs.CreateReusableDelegationSetResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DelegationSet(self):  # pragma: no cover
        return DelegationSet.make_one(self.boto3_raw_data["DelegationSet"])

    Location = field("Location")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateReusableDelegationSetResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateReusableDelegationSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReusableDelegationSetResponse:
    boto3_raw_data: "type_defs.GetReusableDelegationSetResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DelegationSet(self):  # pragma: no cover
        return DelegationSet.make_one(self.boto3_raw_data["DelegationSet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetReusableDelegationSetResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReusableDelegationSetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListReusableDelegationSetsResponse:
    boto3_raw_data: "type_defs.ListReusableDelegationSetsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DelegationSets(self):  # pragma: no cover
        return DelegationSet.make_many(self.boto3_raw_data["DelegationSets"])

    Marker = field("Marker")
    IsTruncated = field("IsTruncated")
    NextMarker = field("NextMarker")
    MaxItems = field("MaxItems")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListReusableDelegationSetsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListReusableDelegationSetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKeySigningKeyResponse:
    boto3_raw_data: "type_defs.CreateKeySigningKeyResponseTypeDef" = dataclasses.field()

    @cached_property
    def ChangeInfo(self):  # pragma: no cover
        return ChangeInfo.make_one(self.boto3_raw_data["ChangeInfo"])

    @cached_property
    def KeySigningKey(self):  # pragma: no cover
        return KeySigningKey.make_one(self.boto3_raw_data["KeySigningKey"])

    Location = field("Location")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateKeySigningKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKeySigningKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateQueryLoggingConfigResponse:
    boto3_raw_data: "type_defs.CreateQueryLoggingConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def QueryLoggingConfig(self):  # pragma: no cover
        return QueryLoggingConfig.make_one(self.boto3_raw_data["QueryLoggingConfig"])

    Location = field("Location")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateQueryLoggingConfigResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateQueryLoggingConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryLoggingConfigResponse:
    boto3_raw_data: "type_defs.GetQueryLoggingConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def QueryLoggingConfig(self):  # pragma: no cover
        return QueryLoggingConfig.make_one(self.boto3_raw_data["QueryLoggingConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetQueryLoggingConfigResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueryLoggingConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueryLoggingConfigsResponse:
    boto3_raw_data: "type_defs.ListQueryLoggingConfigsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def QueryLoggingConfigs(self):  # pragma: no cover
        return QueryLoggingConfig.make_many(self.boto3_raw_data["QueryLoggingConfigs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListQueryLoggingConfigsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueryLoggingConfigsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrafficPolicyInstanceResponse:
    boto3_raw_data: "type_defs.CreateTrafficPolicyInstanceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TrafficPolicyInstance(self):  # pragma: no cover
        return TrafficPolicyInstance.make_one(
            self.boto3_raw_data["TrafficPolicyInstance"]
        )

    Location = field("Location")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateTrafficPolicyInstanceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrafficPolicyInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrafficPolicyInstanceResponse:
    boto3_raw_data: "type_defs.GetTrafficPolicyInstanceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TrafficPolicyInstance(self):  # pragma: no cover
        return TrafficPolicyInstance.make_one(
            self.boto3_raw_data["TrafficPolicyInstance"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetTrafficPolicyInstanceResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrafficPolicyInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrafficPolicyInstancesByHostedZoneResponse:
    boto3_raw_data: (
        "type_defs.ListTrafficPolicyInstancesByHostedZoneResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def TrafficPolicyInstances(self):  # pragma: no cover
        return TrafficPolicyInstance.make_many(
            self.boto3_raw_data["TrafficPolicyInstances"]
        )

    TrafficPolicyInstanceNameMarker = field("TrafficPolicyInstanceNameMarker")
    TrafficPolicyInstanceTypeMarker = field("TrafficPolicyInstanceTypeMarker")
    IsTruncated = field("IsTruncated")
    MaxItems = field("MaxItems")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTrafficPolicyInstancesByHostedZoneResponseTypeDef"
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
                "type_defs.ListTrafficPolicyInstancesByHostedZoneResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrafficPolicyInstancesByPolicyResponse:
    boto3_raw_data: "type_defs.ListTrafficPolicyInstancesByPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TrafficPolicyInstances(self):  # pragma: no cover
        return TrafficPolicyInstance.make_many(
            self.boto3_raw_data["TrafficPolicyInstances"]
        )

    HostedZoneIdMarker = field("HostedZoneIdMarker")
    TrafficPolicyInstanceNameMarker = field("TrafficPolicyInstanceNameMarker")
    TrafficPolicyInstanceTypeMarker = field("TrafficPolicyInstanceTypeMarker")
    IsTruncated = field("IsTruncated")
    MaxItems = field("MaxItems")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTrafficPolicyInstancesByPolicyResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrafficPolicyInstancesByPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrafficPolicyInstancesResponse:
    boto3_raw_data: "type_defs.ListTrafficPolicyInstancesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TrafficPolicyInstances(self):  # pragma: no cover
        return TrafficPolicyInstance.make_many(
            self.boto3_raw_data["TrafficPolicyInstances"]
        )

    HostedZoneIdMarker = field("HostedZoneIdMarker")
    TrafficPolicyInstanceNameMarker = field("TrafficPolicyInstanceNameMarker")
    TrafficPolicyInstanceTypeMarker = field("TrafficPolicyInstanceTypeMarker")
    IsTruncated = field("IsTruncated")
    MaxItems = field("MaxItems")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTrafficPolicyInstancesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrafficPolicyInstancesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTrafficPolicyInstanceResponse:
    boto3_raw_data: "type_defs.UpdateTrafficPolicyInstanceResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TrafficPolicyInstance(self):  # pragma: no cover
        return TrafficPolicyInstance.make_one(
            self.boto3_raw_data["TrafficPolicyInstance"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateTrafficPolicyInstanceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTrafficPolicyInstanceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrafficPolicyResponse:
    boto3_raw_data: "type_defs.CreateTrafficPolicyResponseTypeDef" = dataclasses.field()

    @cached_property
    def TrafficPolicy(self):  # pragma: no cover
        return TrafficPolicy.make_one(self.boto3_raw_data["TrafficPolicy"])

    Location = field("Location")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTrafficPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrafficPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTrafficPolicyVersionResponse:
    boto3_raw_data: "type_defs.CreateTrafficPolicyVersionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TrafficPolicy(self):  # pragma: no cover
        return TrafficPolicy.make_one(self.boto3_raw_data["TrafficPolicy"])

    Location = field("Location")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateTrafficPolicyVersionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTrafficPolicyVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTrafficPolicyResponse:
    boto3_raw_data: "type_defs.GetTrafficPolicyResponseTypeDef" = dataclasses.field()

    @cached_property
    def TrafficPolicy(self):  # pragma: no cover
        return TrafficPolicy.make_one(self.boto3_raw_data["TrafficPolicy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTrafficPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTrafficPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrafficPolicyVersionsResponse:
    boto3_raw_data: "type_defs.ListTrafficPolicyVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TrafficPolicies(self):  # pragma: no cover
        return TrafficPolicy.make_many(self.boto3_raw_data["TrafficPolicies"])

    IsTruncated = field("IsTruncated")
    TrafficPolicyVersionMarker = field("TrafficPolicyVersionMarker")
    MaxItems = field("MaxItems")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTrafficPolicyVersionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrafficPolicyVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTrafficPolicyCommentResponse:
    boto3_raw_data: "type_defs.UpdateTrafficPolicyCommentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TrafficPolicy(self):  # pragma: no cover
        return TrafficPolicy.make_one(self.boto3_raw_data["TrafficPolicy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateTrafficPolicyCommentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTrafficPolicyCommentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDNSSECResponse:
    boto3_raw_data: "type_defs.GetDNSSECResponseTypeDef" = dataclasses.field()

    @cached_property
    def Status(self):  # pragma: no cover
        return DNSSECStatus.make_one(self.boto3_raw_data["Status"])

    @cached_property
    def KeySigningKeys(self):  # pragma: no cover
        return KeySigningKey.make_many(self.boto3_raw_data["KeySigningKeys"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDNSSECResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDNSSECResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGeoLocationResponse:
    boto3_raw_data: "type_defs.GetGeoLocationResponseTypeDef" = dataclasses.field()

    @cached_property
    def GeoLocationDetails(self):  # pragma: no cover
        return GeoLocationDetails.make_one(self.boto3_raw_data["GeoLocationDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGeoLocationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGeoLocationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGeoLocationsResponse:
    boto3_raw_data: "type_defs.ListGeoLocationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def GeoLocationDetailsList(self):  # pragma: no cover
        return GeoLocationDetails.make_many(
            self.boto3_raw_data["GeoLocationDetailsList"]
        )

    IsTruncated = field("IsTruncated")
    NextContinentCode = field("NextContinentCode")
    NextCountryCode = field("NextCountryCode")
    NextSubdivisionCode = field("NextSubdivisionCode")
    MaxItems = field("MaxItems")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGeoLocationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGeoLocationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChangeRequestWait:
    boto3_raw_data: "type_defs.GetChangeRequestWaitTypeDef" = dataclasses.field()

    Id = field("Id")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetChangeRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChangeRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHostedZoneLimitResponse:
    boto3_raw_data: "type_defs.GetHostedZoneLimitResponseTypeDef" = dataclasses.field()

    @cached_property
    def Limit(self):  # pragma: no cover
        return HostedZoneLimit.make_one(self.boto3_raw_data["Limit"])

    Count = field("Count")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetHostedZoneLimitResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetHostedZoneLimitResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetReusableDelegationSetLimitResponse:
    boto3_raw_data: "type_defs.GetReusableDelegationSetLimitResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Limit(self):  # pragma: no cover
        return ReusableDelegationSetLimit.make_one(self.boto3_raw_data["Limit"])

    Count = field("Count")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetReusableDelegationSetLimitResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetReusableDelegationSetLimitResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HealthCheckObservation:
    boto3_raw_data: "type_defs.HealthCheckObservationTypeDef" = dataclasses.field()

    Region = field("Region")
    IPAddress = field("IPAddress")

    @cached_property
    def StatusReport(self):  # pragma: no cover
        return StatusReport.make_one(self.boto3_raw_data["StatusReport"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HealthCheckObservationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HealthCheckObservationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HostedZone:
    boto3_raw_data: "type_defs.HostedZoneTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    CallerReference = field("CallerReference")

    @cached_property
    def Config(self):  # pragma: no cover
        return HostedZoneConfig.make_one(self.boto3_raw_data["Config"])

    ResourceRecordSetCount = field("ResourceRecordSetCount")

    @cached_property
    def LinkedService(self):  # pragma: no cover
        return LinkedService.make_one(self.boto3_raw_data["LinkedService"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HostedZoneTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HostedZoneTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HostedZoneSummary:
    boto3_raw_data: "type_defs.HostedZoneSummaryTypeDef" = dataclasses.field()

    HostedZoneId = field("HostedZoneId")
    Name = field("Name")

    @cached_property
    def Owner(self):  # pragma: no cover
        return HostedZoneOwner.make_one(self.boto3_raw_data["Owner"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HostedZoneSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HostedZoneSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCidrBlocksRequestPaginate:
    boto3_raw_data: "type_defs.ListCidrBlocksRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    CollectionId = field("CollectionId")
    LocationName = field("LocationName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCidrBlocksRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCidrBlocksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCidrCollectionsRequestPaginate:
    boto3_raw_data: "type_defs.ListCidrCollectionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCidrCollectionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCidrCollectionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCidrLocationsRequestPaginate:
    boto3_raw_data: "type_defs.ListCidrLocationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    CollectionId = field("CollectionId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCidrLocationsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCidrLocationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHealthChecksRequestPaginate:
    boto3_raw_data: "type_defs.ListHealthChecksRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListHealthChecksRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHealthChecksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHostedZonesRequestPaginate:
    boto3_raw_data: "type_defs.ListHostedZonesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DelegationSetId = field("DelegationSetId")
    HostedZoneType = field("HostedZoneType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListHostedZonesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHostedZonesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListQueryLoggingConfigsRequestPaginate:
    boto3_raw_data: "type_defs.ListQueryLoggingConfigsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    HostedZoneId = field("HostedZoneId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListQueryLoggingConfigsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListQueryLoggingConfigsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceRecordSetsRequestPaginate:
    boto3_raw_data: "type_defs.ListResourceRecordSetsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    HostedZoneId = field("HostedZoneId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceRecordSetsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceRecordSetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVPCAssociationAuthorizationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListVPCAssociationAuthorizationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    HostedZoneId = field("HostedZoneId")
    MaxResults = field("MaxResults")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListVPCAssociationAuthorizationsRequestPaginateTypeDef"
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
                "type_defs.ListVPCAssociationAuthorizationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCidrLocationsResponse:
    boto3_raw_data: "type_defs.ListCidrLocationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def CidrLocations(self):  # pragma: no cover
        return LocationSummary.make_many(self.boto3_raw_data["CidrLocations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCidrLocationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCidrLocationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTrafficPoliciesResponse:
    boto3_raw_data: "type_defs.ListTrafficPoliciesResponseTypeDef" = dataclasses.field()

    @cached_property
    def TrafficPolicySummaries(self):  # pragma: no cover
        return TrafficPolicySummary.make_many(
            self.boto3_raw_data["TrafficPolicySummaries"]
        )

    IsTruncated = field("IsTruncated")
    TrafficPolicyIdMarker = field("TrafficPolicyIdMarker")
    MaxItems = field("MaxItems")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTrafficPoliciesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTrafficPoliciesResponseTypeDef"]
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
    def ResourceTagSet(self):  # pragma: no cover
        return ResourceTagSet.make_one(self.boto3_raw_data["ResourceTagSet"])

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
class ListTagsForResourcesResponse:
    boto3_raw_data: "type_defs.ListTagsForResourcesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResourceTagSets(self):  # pragma: no cover
        return ResourceTagSet.make_many(self.boto3_raw_data["ResourceTagSets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourcesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HealthCheck:
    boto3_raw_data: "type_defs.HealthCheckTypeDef" = dataclasses.field()

    Id = field("Id")
    CallerReference = field("CallerReference")

    @cached_property
    def HealthCheckConfig(self):  # pragma: no cover
        return HealthCheckConfigOutput.make_one(
            self.boto3_raw_data["HealthCheckConfig"]
        )

    HealthCheckVersion = field("HealthCheckVersion")

    @cached_property
    def LinkedService(self):  # pragma: no cover
        return LinkedService.make_one(self.boto3_raw_data["LinkedService"])

    @cached_property
    def CloudWatchAlarmConfiguration(self):  # pragma: no cover
        return CloudWatchAlarmConfiguration.make_one(
            self.boto3_raw_data["CloudWatchAlarmConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HealthCheckTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HealthCheckTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceRecordSetOutput:
    boto3_raw_data: "type_defs.ResourceRecordSetOutputTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")
    SetIdentifier = field("SetIdentifier")
    Weight = field("Weight")
    Region = field("Region")

    @cached_property
    def GeoLocation(self):  # pragma: no cover
        return GeoLocation.make_one(self.boto3_raw_data["GeoLocation"])

    Failover = field("Failover")
    MultiValueAnswer = field("MultiValueAnswer")
    TTL = field("TTL")

    @cached_property
    def ResourceRecords(self):  # pragma: no cover
        return ResourceRecord.make_many(self.boto3_raw_data["ResourceRecords"])

    @cached_property
    def AliasTarget(self):  # pragma: no cover
        return AliasTarget.make_one(self.boto3_raw_data["AliasTarget"])

    HealthCheckId = field("HealthCheckId")
    TrafficPolicyInstanceId = field("TrafficPolicyInstanceId")

    @cached_property
    def CidrRoutingConfig(self):  # pragma: no cover
        return CidrRoutingConfig.make_one(self.boto3_raw_data["CidrRoutingConfig"])

    @cached_property
    def GeoProximityLocation(self):  # pragma: no cover
        return GeoProximityLocation.make_one(
            self.boto3_raw_data["GeoProximityLocation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceRecordSetOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceRecordSetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceRecordSet:
    boto3_raw_data: "type_defs.ResourceRecordSetTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")
    SetIdentifier = field("SetIdentifier")
    Weight = field("Weight")
    Region = field("Region")

    @cached_property
    def GeoLocation(self):  # pragma: no cover
        return GeoLocation.make_one(self.boto3_raw_data["GeoLocation"])

    Failover = field("Failover")
    MultiValueAnswer = field("MultiValueAnswer")
    TTL = field("TTL")

    @cached_property
    def ResourceRecords(self):  # pragma: no cover
        return ResourceRecord.make_many(self.boto3_raw_data["ResourceRecords"])

    @cached_property
    def AliasTarget(self):  # pragma: no cover
        return AliasTarget.make_one(self.boto3_raw_data["AliasTarget"])

    HealthCheckId = field("HealthCheckId")
    TrafficPolicyInstanceId = field("TrafficPolicyInstanceId")

    @cached_property
    def CidrRoutingConfig(self):  # pragma: no cover
        return CidrRoutingConfig.make_one(self.boto3_raw_data["CidrRoutingConfig"])

    @cached_property
    def GeoProximityLocation(self):  # pragma: no cover
        return GeoProximityLocation.make_one(
            self.boto3_raw_data["GeoProximityLocation"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceRecordSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceRecordSetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHealthCheckLastFailureReasonResponse:
    boto3_raw_data: "type_defs.GetHealthCheckLastFailureReasonResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def HealthCheckObservations(self):  # pragma: no cover
        return HealthCheckObservation.make_many(
            self.boto3_raw_data["HealthCheckObservations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetHealthCheckLastFailureReasonResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetHealthCheckLastFailureReasonResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHealthCheckStatusResponse:
    boto3_raw_data: "type_defs.GetHealthCheckStatusResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def HealthCheckObservations(self):  # pragma: no cover
        return HealthCheckObservation.make_many(
            self.boto3_raw_data["HealthCheckObservations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetHealthCheckStatusResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetHealthCheckStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateHostedZoneResponse:
    boto3_raw_data: "type_defs.CreateHostedZoneResponseTypeDef" = dataclasses.field()

    @cached_property
    def HostedZone(self):  # pragma: no cover
        return HostedZone.make_one(self.boto3_raw_data["HostedZone"])

    @cached_property
    def ChangeInfo(self):  # pragma: no cover
        return ChangeInfo.make_one(self.boto3_raw_data["ChangeInfo"])

    @cached_property
    def DelegationSet(self):  # pragma: no cover
        return DelegationSet.make_one(self.boto3_raw_data["DelegationSet"])

    @cached_property
    def VPC(self):  # pragma: no cover
        return VPC.make_one(self.boto3_raw_data["VPC"])

    Location = field("Location")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateHostedZoneResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHostedZoneResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHostedZoneResponse:
    boto3_raw_data: "type_defs.GetHostedZoneResponseTypeDef" = dataclasses.field()

    @cached_property
    def HostedZone(self):  # pragma: no cover
        return HostedZone.make_one(self.boto3_raw_data["HostedZone"])

    @cached_property
    def DelegationSet(self):  # pragma: no cover
        return DelegationSet.make_one(self.boto3_raw_data["DelegationSet"])

    @cached_property
    def VPCs(self):  # pragma: no cover
        return VPC.make_many(self.boto3_raw_data["VPCs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetHostedZoneResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetHostedZoneResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHostedZonesByNameResponse:
    boto3_raw_data: "type_defs.ListHostedZonesByNameResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def HostedZones(self):  # pragma: no cover
        return HostedZone.make_many(self.boto3_raw_data["HostedZones"])

    DNSName = field("DNSName")
    HostedZoneId = field("HostedZoneId")
    IsTruncated = field("IsTruncated")
    NextDNSName = field("NextDNSName")
    NextHostedZoneId = field("NextHostedZoneId")
    MaxItems = field("MaxItems")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListHostedZonesByNameResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHostedZonesByNameResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHostedZonesResponse:
    boto3_raw_data: "type_defs.ListHostedZonesResponseTypeDef" = dataclasses.field()

    @cached_property
    def HostedZones(self):  # pragma: no cover
        return HostedZone.make_many(self.boto3_raw_data["HostedZones"])

    Marker = field("Marker")
    IsTruncated = field("IsTruncated")
    NextMarker = field("NextMarker")
    MaxItems = field("MaxItems")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListHostedZonesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHostedZonesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateHostedZoneCommentResponse:
    boto3_raw_data: "type_defs.UpdateHostedZoneCommentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def HostedZone(self):  # pragma: no cover
        return HostedZone.make_one(self.boto3_raw_data["HostedZone"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateHostedZoneCommentResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateHostedZoneCommentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHostedZonesByVPCResponse:
    boto3_raw_data: "type_defs.ListHostedZonesByVPCResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def HostedZoneSummaries(self):  # pragma: no cover
        return HostedZoneSummary.make_many(self.boto3_raw_data["HostedZoneSummaries"])

    MaxItems = field("MaxItems")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListHostedZonesByVPCResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHostedZonesByVPCResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateHealthCheckRequest:
    boto3_raw_data: "type_defs.CreateHealthCheckRequestTypeDef" = dataclasses.field()

    CallerReference = field("CallerReference")
    HealthCheckConfig = field("HealthCheckConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateHealthCheckRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHealthCheckRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateHealthCheckResponse:
    boto3_raw_data: "type_defs.CreateHealthCheckResponseTypeDef" = dataclasses.field()

    @cached_property
    def HealthCheck(self):  # pragma: no cover
        return HealthCheck.make_one(self.boto3_raw_data["HealthCheck"])

    Location = field("Location")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateHealthCheckResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHealthCheckResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHealthCheckResponse:
    boto3_raw_data: "type_defs.GetHealthCheckResponseTypeDef" = dataclasses.field()

    @cached_property
    def HealthCheck(self):  # pragma: no cover
        return HealthCheck.make_one(self.boto3_raw_data["HealthCheck"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetHealthCheckResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetHealthCheckResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHealthChecksResponse:
    boto3_raw_data: "type_defs.ListHealthChecksResponseTypeDef" = dataclasses.field()

    @cached_property
    def HealthChecks(self):  # pragma: no cover
        return HealthCheck.make_many(self.boto3_raw_data["HealthChecks"])

    Marker = field("Marker")
    IsTruncated = field("IsTruncated")
    NextMarker = field("NextMarker")
    MaxItems = field("MaxItems")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListHealthChecksResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHealthChecksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateHealthCheckResponse:
    boto3_raw_data: "type_defs.UpdateHealthCheckResponseTypeDef" = dataclasses.field()

    @cached_property
    def HealthCheck(self):  # pragma: no cover
        return HealthCheck.make_one(self.boto3_raw_data["HealthCheck"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateHealthCheckResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateHealthCheckResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceRecordSetsResponse:
    boto3_raw_data: "type_defs.ListResourceRecordSetsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResourceRecordSets(self):  # pragma: no cover
        return ResourceRecordSetOutput.make_many(
            self.boto3_raw_data["ResourceRecordSets"]
        )

    IsTruncated = field("IsTruncated")
    NextRecordName = field("NextRecordName")
    NextRecordType = field("NextRecordType")
    NextRecordIdentifier = field("NextRecordIdentifier")
    MaxItems = field("MaxItems")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResourceRecordSetsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceRecordSetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Change:
    boto3_raw_data: "type_defs.ChangeTypeDef" = dataclasses.field()

    Action = field("Action")
    ResourceRecordSet = field("ResourceRecordSet")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeBatch:
    boto3_raw_data: "type_defs.ChangeBatchTypeDef" = dataclasses.field()

    @cached_property
    def Changes(self):  # pragma: no cover
        return Change.make_many(self.boto3_raw_data["Changes"])

    Comment = field("Comment")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChangeBatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChangeBatchTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeResourceRecordSetsRequest:
    boto3_raw_data: "type_defs.ChangeResourceRecordSetsRequestTypeDef" = (
        dataclasses.field()
    )

    HostedZoneId = field("HostedZoneId")

    @cached_property
    def ChangeBatch(self):  # pragma: no cover
        return ChangeBatch.make_one(self.boto3_raw_data["ChangeBatch"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ChangeResourceRecordSetsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChangeResourceRecordSetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
