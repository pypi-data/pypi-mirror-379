# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_kms import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AliasListEntry:
    boto3_raw_data: "type_defs.AliasListEntryTypeDef" = dataclasses.field()

    AliasName = field("AliasName")
    AliasArn = field("AliasArn")
    TargetKeyId = field("TargetKeyId")
    CreationDate = field("CreationDate")
    LastUpdatedDate = field("LastUpdatedDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AliasListEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AliasListEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelKeyDeletionRequest:
    boto3_raw_data: "type_defs.CancelKeyDeletionRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelKeyDeletionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelKeyDeletionRequestTypeDef"]
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
class ConnectCustomKeyStoreRequest:
    boto3_raw_data: "type_defs.ConnectCustomKeyStoreRequestTypeDef" = (
        dataclasses.field()
    )

    CustomKeyStoreId = field("CustomKeyStoreId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectCustomKeyStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectCustomKeyStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAliasRequest:
    boto3_raw_data: "type_defs.CreateAliasRequestTypeDef" = dataclasses.field()

    AliasName = field("AliasName")
    TargetKeyId = field("TargetKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class XksProxyAuthenticationCredentialType:
    boto3_raw_data: "type_defs.XksProxyAuthenticationCredentialTypeTypeDef" = (
        dataclasses.field()
    )

    AccessKeyId = field("AccessKeyId")
    RawSecretAccessKey = field("RawSecretAccessKey")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.XksProxyAuthenticationCredentialTypeTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.XksProxyAuthenticationCredentialTypeTypeDef"]
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

    TagKey = field("TagKey")
    TagValue = field("TagValue")

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
class XksProxyConfigurationType:
    boto3_raw_data: "type_defs.XksProxyConfigurationTypeTypeDef" = dataclasses.field()

    Connectivity = field("Connectivity")
    AccessKeyId = field("AccessKeyId")
    UriEndpoint = field("UriEndpoint")
    UriPath = field("UriPath")
    VpcEndpointServiceName = field("VpcEndpointServiceName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.XksProxyConfigurationTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.XksProxyConfigurationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAliasRequest:
    boto3_raw_data: "type_defs.DeleteAliasRequestTypeDef" = dataclasses.field()

    AliasName = field("AliasName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCustomKeyStoreRequest:
    boto3_raw_data: "type_defs.DeleteCustomKeyStoreRequestTypeDef" = dataclasses.field()

    CustomKeyStoreId = field("CustomKeyStoreId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCustomKeyStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCustomKeyStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteImportedKeyMaterialRequest:
    boto3_raw_data: "type_defs.DeleteImportedKeyMaterialRequestTypeDef" = (
        dataclasses.field()
    )

    KeyId = field("KeyId")
    KeyMaterialId = field("KeyMaterialId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteImportedKeyMaterialRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteImportedKeyMaterialRequestTypeDef"]
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
class DescribeCustomKeyStoresRequest:
    boto3_raw_data: "type_defs.DescribeCustomKeyStoresRequestTypeDef" = (
        dataclasses.field()
    )

    CustomKeyStoreId = field("CustomKeyStoreId")
    CustomKeyStoreName = field("CustomKeyStoreName")
    Limit = field("Limit")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeCustomKeyStoresRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCustomKeyStoresRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeKeyRequest:
    boto3_raw_data: "type_defs.DescribeKeyRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    GrantTokens = field("GrantTokens")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableKeyRequest:
    boto3_raw_data: "type_defs.DisableKeyRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DisableKeyRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableKeyRotationRequest:
    boto3_raw_data: "type_defs.DisableKeyRotationRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableKeyRotationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableKeyRotationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisconnectCustomKeyStoreRequest:
    boto3_raw_data: "type_defs.DisconnectCustomKeyStoreRequestTypeDef" = (
        dataclasses.field()
    )

    CustomKeyStoreId = field("CustomKeyStoreId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisconnectCustomKeyStoreRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisconnectCustomKeyStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableKeyRequest:
    boto3_raw_data: "type_defs.EnableKeyRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnableKeyRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableKeyRotationRequest:
    boto3_raw_data: "type_defs.EnableKeyRotationRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    RotationPeriodInDays = field("RotationPeriodInDays")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnableKeyRotationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableKeyRotationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateDataKeyPairWithoutPlaintextRequest:
    boto3_raw_data: "type_defs.GenerateDataKeyPairWithoutPlaintextRequestTypeDef" = (
        dataclasses.field()
    )

    KeyId = field("KeyId")
    KeyPairSpec = field("KeyPairSpec")
    EncryptionContext = field("EncryptionContext")
    GrantTokens = field("GrantTokens")
    DryRun = field("DryRun")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GenerateDataKeyPairWithoutPlaintextRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateDataKeyPairWithoutPlaintextRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateDataKeyWithoutPlaintextRequest:
    boto3_raw_data: "type_defs.GenerateDataKeyWithoutPlaintextRequestTypeDef" = (
        dataclasses.field()
    )

    KeyId = field("KeyId")
    EncryptionContext = field("EncryptionContext")
    KeySpec = field("KeySpec")
    NumberOfBytes = field("NumberOfBytes")
    GrantTokens = field("GrantTokens")
    DryRun = field("DryRun")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GenerateDataKeyWithoutPlaintextRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateDataKeyWithoutPlaintextRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKeyPolicyRequest:
    boto3_raw_data: "type_defs.GetKeyPolicyRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    PolicyName = field("PolicyName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKeyPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKeyPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKeyRotationStatusRequest:
    boto3_raw_data: "type_defs.GetKeyRotationStatusRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKeyRotationStatusRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKeyRotationStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetParametersForImportRequest:
    boto3_raw_data: "type_defs.GetParametersForImportRequestTypeDef" = (
        dataclasses.field()
    )

    KeyId = field("KeyId")
    WrappingAlgorithm = field("WrappingAlgorithm")
    WrappingKeySpec = field("WrappingKeySpec")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetParametersForImportRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetParametersForImportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPublicKeyRequest:
    boto3_raw_data: "type_defs.GetPublicKeyRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    GrantTokens = field("GrantTokens")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPublicKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPublicKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrantConstraintsOutput:
    boto3_raw_data: "type_defs.GrantConstraintsOutputTypeDef" = dataclasses.field()

    EncryptionContextSubset = field("EncryptionContextSubset")
    EncryptionContextEquals = field("EncryptionContextEquals")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GrantConstraintsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GrantConstraintsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrantConstraints:
    boto3_raw_data: "type_defs.GrantConstraintsTypeDef" = dataclasses.field()

    EncryptionContextSubset = field("EncryptionContextSubset")
    EncryptionContextEquals = field("EncryptionContextEquals")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GrantConstraintsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GrantConstraintsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyListEntry:
    boto3_raw_data: "type_defs.KeyListEntryTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    KeyArn = field("KeyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyListEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyListEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class XksKeyConfigurationType:
    boto3_raw_data: "type_defs.XksKeyConfigurationTypeTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.XksKeyConfigurationTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.XksKeyConfigurationTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAliasesRequest:
    boto3_raw_data: "type_defs.ListAliasesRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    Limit = field("Limit")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAliasesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAliasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGrantsRequest:
    boto3_raw_data: "type_defs.ListGrantsRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    Limit = field("Limit")
    Marker = field("Marker")
    GrantId = field("GrantId")
    GranteePrincipal = field("GranteePrincipal")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListGrantsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGrantsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeyPoliciesRequest:
    boto3_raw_data: "type_defs.ListKeyPoliciesRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    Limit = field("Limit")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKeyPoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKeyPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeyRotationsRequest:
    boto3_raw_data: "type_defs.ListKeyRotationsRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    IncludeKeyMaterial = field("IncludeKeyMaterial")
    Limit = field("Limit")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKeyRotationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKeyRotationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RotationsListEntry:
    boto3_raw_data: "type_defs.RotationsListEntryTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    KeyMaterialId = field("KeyMaterialId")
    KeyMaterialDescription = field("KeyMaterialDescription")
    ImportState = field("ImportState")
    KeyMaterialState = field("KeyMaterialState")
    ExpirationModel = field("ExpirationModel")
    ValidTo = field("ValidTo")
    RotationDate = field("RotationDate")
    RotationType = field("RotationType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RotationsListEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RotationsListEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeysRequest:
    boto3_raw_data: "type_defs.ListKeysRequestTypeDef" = dataclasses.field()

    Limit = field("Limit")
    Marker = field("Marker")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListKeysRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListKeysRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceTagsRequest:
    boto3_raw_data: "type_defs.ListResourceTagsRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    Limit = field("Limit")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourceTagsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceTagsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRetirableGrantsRequest:
    boto3_raw_data: "type_defs.ListRetirableGrantsRequestTypeDef" = dataclasses.field()

    RetiringPrincipal = field("RetiringPrincipal")
    Limit = field("Limit")
    Marker = field("Marker")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListRetirableGrantsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRetirableGrantsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiRegionKey:
    boto3_raw_data: "type_defs.MultiRegionKeyTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Region = field("Region")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MultiRegionKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MultiRegionKeyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutKeyPolicyRequest:
    boto3_raw_data: "type_defs.PutKeyPolicyRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    Policy = field("Policy")
    PolicyName = field("PolicyName")
    BypassPolicyLockoutSafetyCheck = field("BypassPolicyLockoutSafetyCheck")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutKeyPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutKeyPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetireGrantRequest:
    boto3_raw_data: "type_defs.RetireGrantRequestTypeDef" = dataclasses.field()

    GrantToken = field("GrantToken")
    KeyId = field("KeyId")
    GrantId = field("GrantId")
    DryRun = field("DryRun")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetireGrantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetireGrantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RevokeGrantRequest:
    boto3_raw_data: "type_defs.RevokeGrantRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    GrantId = field("GrantId")
    DryRun = field("DryRun")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RevokeGrantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RevokeGrantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RotateKeyOnDemandRequest:
    boto3_raw_data: "type_defs.RotateKeyOnDemandRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RotateKeyOnDemandRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RotateKeyOnDemandRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduleKeyDeletionRequest:
    boto3_raw_data: "type_defs.ScheduleKeyDeletionRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    PendingWindowInDays = field("PendingWindowInDays")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduleKeyDeletionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduleKeyDeletionRequestTypeDef"]
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

    KeyId = field("KeyId")
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
class UpdateAliasRequest:
    boto3_raw_data: "type_defs.UpdateAliasRequestTypeDef" = dataclasses.field()

    AliasName = field("AliasName")
    TargetKeyId = field("TargetKeyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAliasRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAliasRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateKeyDescriptionRequest:
    boto3_raw_data: "type_defs.UpdateKeyDescriptionRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateKeyDescriptionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateKeyDescriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePrimaryRegionRequest:
    boto3_raw_data: "type_defs.UpdatePrimaryRegionRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    PrimaryRegion = field("PrimaryRegion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePrimaryRegionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePrimaryRegionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptRequest:
    boto3_raw_data: "type_defs.EncryptRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    Plaintext = field("Plaintext")
    EncryptionContext = field("EncryptionContext")
    GrantTokens = field("GrantTokens")
    EncryptionAlgorithm = field("EncryptionAlgorithm")
    DryRun = field("DryRun")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EncryptRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EncryptRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateMacRequest:
    boto3_raw_data: "type_defs.GenerateMacRequestTypeDef" = dataclasses.field()

    Message = field("Message")
    KeyId = field("KeyId")
    MacAlgorithm = field("MacAlgorithm")
    GrantTokens = field("GrantTokens")
    DryRun = field("DryRun")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerateMacRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateMacRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReEncryptRequest:
    boto3_raw_data: "type_defs.ReEncryptRequestTypeDef" = dataclasses.field()

    CiphertextBlob = field("CiphertextBlob")
    DestinationKeyId = field("DestinationKeyId")
    SourceEncryptionContext = field("SourceEncryptionContext")
    SourceKeyId = field("SourceKeyId")
    DestinationEncryptionContext = field("DestinationEncryptionContext")
    SourceEncryptionAlgorithm = field("SourceEncryptionAlgorithm")
    DestinationEncryptionAlgorithm = field("DestinationEncryptionAlgorithm")
    GrantTokens = field("GrantTokens")
    DryRun = field("DryRun")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReEncryptRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReEncryptRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecipientInfo:
    boto3_raw_data: "type_defs.RecipientInfoTypeDef" = dataclasses.field()

    KeyEncryptionAlgorithm = field("KeyEncryptionAlgorithm")
    AttestationDocument = field("AttestationDocument")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecipientInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecipientInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignRequest:
    boto3_raw_data: "type_defs.SignRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    Message = field("Message")
    SigningAlgorithm = field("SigningAlgorithm")
    MessageType = field("MessageType")
    GrantTokens = field("GrantTokens")
    DryRun = field("DryRun")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SignRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SignRequestTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyMacRequest:
    boto3_raw_data: "type_defs.VerifyMacRequestTypeDef" = dataclasses.field()

    Message = field("Message")
    KeyId = field("KeyId")
    MacAlgorithm = field("MacAlgorithm")
    Mac = field("Mac")
    GrantTokens = field("GrantTokens")
    DryRun = field("DryRun")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VerifyMacRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyMacRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyRequest:
    boto3_raw_data: "type_defs.VerifyRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    Message = field("Message")
    Signature = field("Signature")
    SigningAlgorithm = field("SigningAlgorithm")
    MessageType = field("MessageType")
    GrantTokens = field("GrantTokens")
    DryRun = field("DryRun")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VerifyRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VerifyRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelKeyDeletionResponse:
    boto3_raw_data: "type_defs.CancelKeyDeletionResponseTypeDef" = dataclasses.field()

    KeyId = field("KeyId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelKeyDeletionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelKeyDeletionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomKeyStoreResponse:
    boto3_raw_data: "type_defs.CreateCustomKeyStoreResponseTypeDef" = (
        dataclasses.field()
    )

    CustomKeyStoreId = field("CustomKeyStoreId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCustomKeyStoreResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomKeyStoreResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGrantResponse:
    boto3_raw_data: "type_defs.CreateGrantResponseTypeDef" = dataclasses.field()

    GrantToken = field("GrantToken")
    GrantId = field("GrantId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGrantResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGrantResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DecryptResponse:
    boto3_raw_data: "type_defs.DecryptResponseTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    Plaintext = field("Plaintext")
    EncryptionAlgorithm = field("EncryptionAlgorithm")
    CiphertextForRecipient = field("CiphertextForRecipient")
    KeyMaterialId = field("KeyMaterialId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DecryptResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DecryptResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteImportedKeyMaterialResponse:
    boto3_raw_data: "type_defs.DeleteImportedKeyMaterialResponseTypeDef" = (
        dataclasses.field()
    )

    KeyId = field("KeyId")
    KeyMaterialId = field("KeyMaterialId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteImportedKeyMaterialResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteImportedKeyMaterialResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeriveSharedSecretResponse:
    boto3_raw_data: "type_defs.DeriveSharedSecretResponseTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    SharedSecret = field("SharedSecret")
    CiphertextForRecipient = field("CiphertextForRecipient")
    KeyAgreementAlgorithm = field("KeyAgreementAlgorithm")
    KeyOrigin = field("KeyOrigin")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeriveSharedSecretResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeriveSharedSecretResponseTypeDef"]
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
class EncryptResponse:
    boto3_raw_data: "type_defs.EncryptResponseTypeDef" = dataclasses.field()

    CiphertextBlob = field("CiphertextBlob")
    KeyId = field("KeyId")
    EncryptionAlgorithm = field("EncryptionAlgorithm")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EncryptResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EncryptResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateDataKeyPairResponse:
    boto3_raw_data: "type_defs.GenerateDataKeyPairResponseTypeDef" = dataclasses.field()

    PrivateKeyCiphertextBlob = field("PrivateKeyCiphertextBlob")
    PrivateKeyPlaintext = field("PrivateKeyPlaintext")
    PublicKey = field("PublicKey")
    KeyId = field("KeyId")
    KeyPairSpec = field("KeyPairSpec")
    CiphertextForRecipient = field("CiphertextForRecipient")
    KeyMaterialId = field("KeyMaterialId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerateDataKeyPairResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateDataKeyPairResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateDataKeyPairWithoutPlaintextResponse:
    boto3_raw_data: "type_defs.GenerateDataKeyPairWithoutPlaintextResponseTypeDef" = (
        dataclasses.field()
    )

    PrivateKeyCiphertextBlob = field("PrivateKeyCiphertextBlob")
    PublicKey = field("PublicKey")
    KeyId = field("KeyId")
    KeyPairSpec = field("KeyPairSpec")
    KeyMaterialId = field("KeyMaterialId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GenerateDataKeyPairWithoutPlaintextResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateDataKeyPairWithoutPlaintextResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateDataKeyResponse:
    boto3_raw_data: "type_defs.GenerateDataKeyResponseTypeDef" = dataclasses.field()

    CiphertextBlob = field("CiphertextBlob")
    Plaintext = field("Plaintext")
    KeyId = field("KeyId")
    CiphertextForRecipient = field("CiphertextForRecipient")
    KeyMaterialId = field("KeyMaterialId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerateDataKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateDataKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateDataKeyWithoutPlaintextResponse:
    boto3_raw_data: "type_defs.GenerateDataKeyWithoutPlaintextResponseTypeDef" = (
        dataclasses.field()
    )

    CiphertextBlob = field("CiphertextBlob")
    KeyId = field("KeyId")
    KeyMaterialId = field("KeyMaterialId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GenerateDataKeyWithoutPlaintextResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateDataKeyWithoutPlaintextResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateMacResponse:
    boto3_raw_data: "type_defs.GenerateMacResponseTypeDef" = dataclasses.field()

    Mac = field("Mac")
    MacAlgorithm = field("MacAlgorithm")
    KeyId = field("KeyId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerateMacResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateMacResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateRandomResponse:
    boto3_raw_data: "type_defs.GenerateRandomResponseTypeDef" = dataclasses.field()

    Plaintext = field("Plaintext")
    CiphertextForRecipient = field("CiphertextForRecipient")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerateRandomResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateRandomResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKeyPolicyResponse:
    boto3_raw_data: "type_defs.GetKeyPolicyResponseTypeDef" = dataclasses.field()

    Policy = field("Policy")
    PolicyName = field("PolicyName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKeyPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKeyPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetKeyRotationStatusResponse:
    boto3_raw_data: "type_defs.GetKeyRotationStatusResponseTypeDef" = (
        dataclasses.field()
    )

    KeyRotationEnabled = field("KeyRotationEnabled")
    KeyId = field("KeyId")
    RotationPeriodInDays = field("RotationPeriodInDays")
    NextRotationDate = field("NextRotationDate")
    OnDemandRotationStartDate = field("OnDemandRotationStartDate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetKeyRotationStatusResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetKeyRotationStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetParametersForImportResponse:
    boto3_raw_data: "type_defs.GetParametersForImportResponseTypeDef" = (
        dataclasses.field()
    )

    KeyId = field("KeyId")
    ImportToken = field("ImportToken")
    PublicKey = field("PublicKey")
    ParametersValidTo = field("ParametersValidTo")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetParametersForImportResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetParametersForImportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPublicKeyResponse:
    boto3_raw_data: "type_defs.GetPublicKeyResponseTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    PublicKey = field("PublicKey")
    CustomerMasterKeySpec = field("CustomerMasterKeySpec")
    KeySpec = field("KeySpec")
    KeyUsage = field("KeyUsage")
    EncryptionAlgorithms = field("EncryptionAlgorithms")
    SigningAlgorithms = field("SigningAlgorithms")
    KeyAgreementAlgorithms = field("KeyAgreementAlgorithms")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPublicKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPublicKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportKeyMaterialResponse:
    boto3_raw_data: "type_defs.ImportKeyMaterialResponseTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    KeyMaterialId = field("KeyMaterialId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportKeyMaterialResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportKeyMaterialResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAliasesResponse:
    boto3_raw_data: "type_defs.ListAliasesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Aliases(self):  # pragma: no cover
        return AliasListEntry.make_many(self.boto3_raw_data["Aliases"])

    NextMarker = field("NextMarker")
    Truncated = field("Truncated")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAliasesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAliasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeyPoliciesResponse:
    boto3_raw_data: "type_defs.ListKeyPoliciesResponseTypeDef" = dataclasses.field()

    PolicyNames = field("PolicyNames")
    NextMarker = field("NextMarker")
    Truncated = field("Truncated")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKeyPoliciesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKeyPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReEncryptResponse:
    boto3_raw_data: "type_defs.ReEncryptResponseTypeDef" = dataclasses.field()

    CiphertextBlob = field("CiphertextBlob")
    SourceKeyId = field("SourceKeyId")
    KeyId = field("KeyId")
    SourceEncryptionAlgorithm = field("SourceEncryptionAlgorithm")
    DestinationEncryptionAlgorithm = field("DestinationEncryptionAlgorithm")
    SourceKeyMaterialId = field("SourceKeyMaterialId")
    DestinationKeyMaterialId = field("DestinationKeyMaterialId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ReEncryptResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReEncryptResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RotateKeyOnDemandResponse:
    boto3_raw_data: "type_defs.RotateKeyOnDemandResponseTypeDef" = dataclasses.field()

    KeyId = field("KeyId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RotateKeyOnDemandResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RotateKeyOnDemandResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScheduleKeyDeletionResponse:
    boto3_raw_data: "type_defs.ScheduleKeyDeletionResponseTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    DeletionDate = field("DeletionDate")
    KeyState = field("KeyState")
    PendingWindowInDays = field("PendingWindowInDays")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScheduleKeyDeletionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScheduleKeyDeletionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignResponse:
    boto3_raw_data: "type_defs.SignResponseTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    Signature = field("Signature")
    SigningAlgorithm = field("SigningAlgorithm")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SignResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SignResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyMacResponse:
    boto3_raw_data: "type_defs.VerifyMacResponseTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    MacValid = field("MacValid")
    MacAlgorithm = field("MacAlgorithm")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VerifyMacResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VerifyMacResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VerifyResponse:
    boto3_raw_data: "type_defs.VerifyResponseTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    SignatureValid = field("SignatureValid")
    SigningAlgorithm = field("SigningAlgorithm")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VerifyResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VerifyResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCustomKeyStoreRequest:
    boto3_raw_data: "type_defs.CreateCustomKeyStoreRequestTypeDef" = dataclasses.field()

    CustomKeyStoreName = field("CustomKeyStoreName")
    CloudHsmClusterId = field("CloudHsmClusterId")
    TrustAnchorCertificate = field("TrustAnchorCertificate")
    KeyStorePassword = field("KeyStorePassword")
    CustomKeyStoreType = field("CustomKeyStoreType")
    XksProxyUriEndpoint = field("XksProxyUriEndpoint")
    XksProxyUriPath = field("XksProxyUriPath")
    XksProxyVpcEndpointServiceName = field("XksProxyVpcEndpointServiceName")

    @cached_property
    def XksProxyAuthenticationCredential(self):  # pragma: no cover
        return XksProxyAuthenticationCredentialType.make_one(
            self.boto3_raw_data["XksProxyAuthenticationCredential"]
        )

    XksProxyConnectivity = field("XksProxyConnectivity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCustomKeyStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCustomKeyStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCustomKeyStoreRequest:
    boto3_raw_data: "type_defs.UpdateCustomKeyStoreRequestTypeDef" = dataclasses.field()

    CustomKeyStoreId = field("CustomKeyStoreId")
    NewCustomKeyStoreName = field("NewCustomKeyStoreName")
    KeyStorePassword = field("KeyStorePassword")
    CloudHsmClusterId = field("CloudHsmClusterId")
    XksProxyUriEndpoint = field("XksProxyUriEndpoint")
    XksProxyUriPath = field("XksProxyUriPath")
    XksProxyVpcEndpointServiceName = field("XksProxyVpcEndpointServiceName")

    @cached_property
    def XksProxyAuthenticationCredential(self):  # pragma: no cover
        return XksProxyAuthenticationCredentialType.make_one(
            self.boto3_raw_data["XksProxyAuthenticationCredential"]
        )

    XksProxyConnectivity = field("XksProxyConnectivity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCustomKeyStoreRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCustomKeyStoreRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKeyRequest:
    boto3_raw_data: "type_defs.CreateKeyRequestTypeDef" = dataclasses.field()

    Policy = field("Policy")
    Description = field("Description")
    KeyUsage = field("KeyUsage")
    CustomerMasterKeySpec = field("CustomerMasterKeySpec")
    KeySpec = field("KeySpec")
    Origin = field("Origin")
    CustomKeyStoreId = field("CustomKeyStoreId")
    BypassPolicyLockoutSafetyCheck = field("BypassPolicyLockoutSafetyCheck")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    MultiRegion = field("MultiRegion")
    XksKeyId = field("XksKeyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateKeyRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceTagsResponse:
    boto3_raw_data: "type_defs.ListResourceTagsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    NextMarker = field("NextMarker")
    Truncated = field("Truncated")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourceTagsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceTagsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicateKeyRequest:
    boto3_raw_data: "type_defs.ReplicateKeyRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    ReplicaRegion = field("ReplicaRegion")
    Policy = field("Policy")
    BypassPolicyLockoutSafetyCheck = field("BypassPolicyLockoutSafetyCheck")
    Description = field("Description")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicateKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicateKeyRequestTypeDef"]
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

    KeyId = field("KeyId")

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
class CustomKeyStoresListEntry:
    boto3_raw_data: "type_defs.CustomKeyStoresListEntryTypeDef" = dataclasses.field()

    CustomKeyStoreId = field("CustomKeyStoreId")
    CustomKeyStoreName = field("CustomKeyStoreName")
    CloudHsmClusterId = field("CloudHsmClusterId")
    TrustAnchorCertificate = field("TrustAnchorCertificate")
    ConnectionState = field("ConnectionState")
    ConnectionErrorCode = field("ConnectionErrorCode")
    CreationDate = field("CreationDate")
    CustomKeyStoreType = field("CustomKeyStoreType")

    @cached_property
    def XksProxyConfiguration(self):  # pragma: no cover
        return XksProxyConfigurationType.make_one(
            self.boto3_raw_data["XksProxyConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CustomKeyStoresListEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CustomKeyStoresListEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCustomKeyStoresRequestPaginate:
    boto3_raw_data: "type_defs.DescribeCustomKeyStoresRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    CustomKeyStoreId = field("CustomKeyStoreId")
    CustomKeyStoreName = field("CustomKeyStoreName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeCustomKeyStoresRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCustomKeyStoresRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAliasesRequestPaginate:
    boto3_raw_data: "type_defs.ListAliasesRequestPaginateTypeDef" = dataclasses.field()

    KeyId = field("KeyId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAliasesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAliasesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGrantsRequestPaginate:
    boto3_raw_data: "type_defs.ListGrantsRequestPaginateTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    GrantId = field("GrantId")
    GranteePrincipal = field("GranteePrincipal")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGrantsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGrantsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeyPoliciesRequestPaginate:
    boto3_raw_data: "type_defs.ListKeyPoliciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    KeyId = field("KeyId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListKeyPoliciesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKeyPoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeyRotationsRequestPaginate:
    boto3_raw_data: "type_defs.ListKeyRotationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    KeyId = field("KeyId")
    IncludeKeyMaterial = field("IncludeKeyMaterial")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListKeyRotationsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKeyRotationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeysRequestPaginate:
    boto3_raw_data: "type_defs.ListKeysRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKeysRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKeysRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceTagsRequestPaginate:
    boto3_raw_data: "type_defs.ListResourceTagsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    KeyId = field("KeyId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResourceTagsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceTagsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListRetirableGrantsRequestPaginate:
    boto3_raw_data: "type_defs.ListRetirableGrantsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    RetiringPrincipal = field("RetiringPrincipal")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListRetirableGrantsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListRetirableGrantsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GrantListEntry:
    boto3_raw_data: "type_defs.GrantListEntryTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    GrantId = field("GrantId")
    Name = field("Name")
    CreationDate = field("CreationDate")
    GranteePrincipal = field("GranteePrincipal")
    RetiringPrincipal = field("RetiringPrincipal")
    IssuingAccount = field("IssuingAccount")
    Operations = field("Operations")

    @cached_property
    def Constraints(self):  # pragma: no cover
        return GrantConstraintsOutput.make_one(self.boto3_raw_data["Constraints"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GrantListEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GrantListEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportKeyMaterialRequest:
    boto3_raw_data: "type_defs.ImportKeyMaterialRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    ImportToken = field("ImportToken")
    EncryptedKeyMaterial = field("EncryptedKeyMaterial")
    ValidTo = field("ValidTo")
    ExpirationModel = field("ExpirationModel")
    ImportType = field("ImportType")
    KeyMaterialDescription = field("KeyMaterialDescription")
    KeyMaterialId = field("KeyMaterialId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportKeyMaterialRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportKeyMaterialRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeysResponse:
    boto3_raw_data: "type_defs.ListKeysResponseTypeDef" = dataclasses.field()

    @cached_property
    def Keys(self):  # pragma: no cover
        return KeyListEntry.make_many(self.boto3_raw_data["Keys"])

    NextMarker = field("NextMarker")
    Truncated = field("Truncated")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListKeysResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKeysResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeyRotationsResponse:
    boto3_raw_data: "type_defs.ListKeyRotationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Rotations(self):  # pragma: no cover
        return RotationsListEntry.make_many(self.boto3_raw_data["Rotations"])

    NextMarker = field("NextMarker")
    Truncated = field("Truncated")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListKeyRotationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKeyRotationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MultiRegionConfiguration:
    boto3_raw_data: "type_defs.MultiRegionConfigurationTypeDef" = dataclasses.field()

    MultiRegionKeyType = field("MultiRegionKeyType")

    @cached_property
    def PrimaryKey(self):  # pragma: no cover
        return MultiRegionKey.make_one(self.boto3_raw_data["PrimaryKey"])

    @cached_property
    def ReplicaKeys(self):  # pragma: no cover
        return MultiRegionKey.make_many(self.boto3_raw_data["ReplicaKeys"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MultiRegionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MultiRegionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DecryptRequest:
    boto3_raw_data: "type_defs.DecryptRequestTypeDef" = dataclasses.field()

    CiphertextBlob = field("CiphertextBlob")
    EncryptionContext = field("EncryptionContext")
    GrantTokens = field("GrantTokens")
    KeyId = field("KeyId")
    EncryptionAlgorithm = field("EncryptionAlgorithm")

    @cached_property
    def Recipient(self):  # pragma: no cover
        return RecipientInfo.make_one(self.boto3_raw_data["Recipient"])

    DryRun = field("DryRun")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DecryptRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DecryptRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeriveSharedSecretRequest:
    boto3_raw_data: "type_defs.DeriveSharedSecretRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    KeyAgreementAlgorithm = field("KeyAgreementAlgorithm")
    PublicKey = field("PublicKey")
    GrantTokens = field("GrantTokens")
    DryRun = field("DryRun")

    @cached_property
    def Recipient(self):  # pragma: no cover
        return RecipientInfo.make_one(self.boto3_raw_data["Recipient"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeriveSharedSecretRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeriveSharedSecretRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateDataKeyPairRequest:
    boto3_raw_data: "type_defs.GenerateDataKeyPairRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    KeyPairSpec = field("KeyPairSpec")
    EncryptionContext = field("EncryptionContext")
    GrantTokens = field("GrantTokens")

    @cached_property
    def Recipient(self):  # pragma: no cover
        return RecipientInfo.make_one(self.boto3_raw_data["Recipient"])

    DryRun = field("DryRun")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerateDataKeyPairRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateDataKeyPairRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateDataKeyRequest:
    boto3_raw_data: "type_defs.GenerateDataKeyRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    EncryptionContext = field("EncryptionContext")
    NumberOfBytes = field("NumberOfBytes")
    KeySpec = field("KeySpec")
    GrantTokens = field("GrantTokens")

    @cached_property
    def Recipient(self):  # pragma: no cover
        return RecipientInfo.make_one(self.boto3_raw_data["Recipient"])

    DryRun = field("DryRun")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerateDataKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateDataKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateRandomRequest:
    boto3_raw_data: "type_defs.GenerateRandomRequestTypeDef" = dataclasses.field()

    NumberOfBytes = field("NumberOfBytes")
    CustomKeyStoreId = field("CustomKeyStoreId")

    @cached_property
    def Recipient(self):  # pragma: no cover
        return RecipientInfo.make_one(self.boto3_raw_data["Recipient"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerateRandomRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateRandomRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeCustomKeyStoresResponse:
    boto3_raw_data: "type_defs.DescribeCustomKeyStoresResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CustomKeyStores(self):  # pragma: no cover
        return CustomKeyStoresListEntry.make_many(
            self.boto3_raw_data["CustomKeyStores"]
        )

    NextMarker = field("NextMarker")
    Truncated = field("Truncated")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeCustomKeyStoresResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeCustomKeyStoresResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGrantsResponse:
    boto3_raw_data: "type_defs.ListGrantsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Grants(self):  # pragma: no cover
        return GrantListEntry.make_many(self.boto3_raw_data["Grants"])

    NextMarker = field("NextMarker")
    Truncated = field("Truncated")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGrantsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGrantsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGrantRequest:
    boto3_raw_data: "type_defs.CreateGrantRequestTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    GranteePrincipal = field("GranteePrincipal")
    Operations = field("Operations")
    RetiringPrincipal = field("RetiringPrincipal")
    Constraints = field("Constraints")
    GrantTokens = field("GrantTokens")
    Name = field("Name")
    DryRun = field("DryRun")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGrantRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGrantRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KeyMetadata:
    boto3_raw_data: "type_defs.KeyMetadataTypeDef" = dataclasses.field()

    KeyId = field("KeyId")
    AWSAccountId = field("AWSAccountId")
    Arn = field("Arn")
    CreationDate = field("CreationDate")
    Enabled = field("Enabled")
    Description = field("Description")
    KeyUsage = field("KeyUsage")
    KeyState = field("KeyState")
    DeletionDate = field("DeletionDate")
    ValidTo = field("ValidTo")
    Origin = field("Origin")
    CustomKeyStoreId = field("CustomKeyStoreId")
    CloudHsmClusterId = field("CloudHsmClusterId")
    ExpirationModel = field("ExpirationModel")
    KeyManager = field("KeyManager")
    CustomerMasterKeySpec = field("CustomerMasterKeySpec")
    KeySpec = field("KeySpec")
    EncryptionAlgorithms = field("EncryptionAlgorithms")
    SigningAlgorithms = field("SigningAlgorithms")
    KeyAgreementAlgorithms = field("KeyAgreementAlgorithms")
    MultiRegion = field("MultiRegion")

    @cached_property
    def MultiRegionConfiguration(self):  # pragma: no cover
        return MultiRegionConfiguration.make_one(
            self.boto3_raw_data["MultiRegionConfiguration"]
        )

    PendingDeletionWindowInDays = field("PendingDeletionWindowInDays")
    MacAlgorithms = field("MacAlgorithms")

    @cached_property
    def XksKeyConfiguration(self):  # pragma: no cover
        return XksKeyConfigurationType.make_one(
            self.boto3_raw_data["XksKeyConfiguration"]
        )

    CurrentKeyMaterialId = field("CurrentKeyMaterialId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.KeyMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.KeyMetadataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateKeyResponse:
    boto3_raw_data: "type_defs.CreateKeyResponseTypeDef" = dataclasses.field()

    @cached_property
    def KeyMetadata(self):  # pragma: no cover
        return KeyMetadata.make_one(self.boto3_raw_data["KeyMetadata"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateKeyResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeKeyResponse:
    boto3_raw_data: "type_defs.DescribeKeyResponseTypeDef" = dataclasses.field()

    @cached_property
    def KeyMetadata(self):  # pragma: no cover
        return KeyMetadata.make_one(self.boto3_raw_data["KeyMetadata"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReplicateKeyResponse:
    boto3_raw_data: "type_defs.ReplicateKeyResponseTypeDef" = dataclasses.field()

    @cached_property
    def ReplicaKeyMetadata(self):  # pragma: no cover
        return KeyMetadata.make_one(self.boto3_raw_data["ReplicaKeyMetadata"])

    ReplicaPolicy = field("ReplicaPolicy")

    @cached_property
    def ReplicaTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["ReplicaTags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReplicateKeyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReplicateKeyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
