# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_kms import type_defs as bs_td


class KMSCaster:

    def cancel_key_deletion(
        self,
        res: "bs_td.CancelKeyDeletionResponseTypeDef",
    ) -> "dc_td.CancelKeyDeletionResponse":
        return dc_td.CancelKeyDeletionResponse.make_one(res)

    def create_alias(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_custom_key_store(
        self,
        res: "bs_td.CreateCustomKeyStoreResponseTypeDef",
    ) -> "dc_td.CreateCustomKeyStoreResponse":
        return dc_td.CreateCustomKeyStoreResponse.make_one(res)

    def create_grant(
        self,
        res: "bs_td.CreateGrantResponseTypeDef",
    ) -> "dc_td.CreateGrantResponse":
        return dc_td.CreateGrantResponse.make_one(res)

    def create_key(
        self,
        res: "bs_td.CreateKeyResponseTypeDef",
    ) -> "dc_td.CreateKeyResponse":
        return dc_td.CreateKeyResponse.make_one(res)

    def decrypt(
        self,
        res: "bs_td.DecryptResponseTypeDef",
    ) -> "dc_td.DecryptResponse":
        return dc_td.DecryptResponse.make_one(res)

    def delete_alias(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_imported_key_material(
        self,
        res: "bs_td.DeleteImportedKeyMaterialResponseTypeDef",
    ) -> "dc_td.DeleteImportedKeyMaterialResponse":
        return dc_td.DeleteImportedKeyMaterialResponse.make_one(res)

    def derive_shared_secret(
        self,
        res: "bs_td.DeriveSharedSecretResponseTypeDef",
    ) -> "dc_td.DeriveSharedSecretResponse":
        return dc_td.DeriveSharedSecretResponse.make_one(res)

    def describe_custom_key_stores(
        self,
        res: "bs_td.DescribeCustomKeyStoresResponseTypeDef",
    ) -> "dc_td.DescribeCustomKeyStoresResponse":
        return dc_td.DescribeCustomKeyStoresResponse.make_one(res)

    def describe_key(
        self,
        res: "bs_td.DescribeKeyResponseTypeDef",
    ) -> "dc_td.DescribeKeyResponse":
        return dc_td.DescribeKeyResponse.make_one(res)

    def disable_key(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disable_key_rotation(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def enable_key(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def enable_key_rotation(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def encrypt(
        self,
        res: "bs_td.EncryptResponseTypeDef",
    ) -> "dc_td.EncryptResponse":
        return dc_td.EncryptResponse.make_one(res)

    def generate_data_key(
        self,
        res: "bs_td.GenerateDataKeyResponseTypeDef",
    ) -> "dc_td.GenerateDataKeyResponse":
        return dc_td.GenerateDataKeyResponse.make_one(res)

    def generate_data_key_pair(
        self,
        res: "bs_td.GenerateDataKeyPairResponseTypeDef",
    ) -> "dc_td.GenerateDataKeyPairResponse":
        return dc_td.GenerateDataKeyPairResponse.make_one(res)

    def generate_data_key_pair_without_plaintext(
        self,
        res: "bs_td.GenerateDataKeyPairWithoutPlaintextResponseTypeDef",
    ) -> "dc_td.GenerateDataKeyPairWithoutPlaintextResponse":
        return dc_td.GenerateDataKeyPairWithoutPlaintextResponse.make_one(res)

    def generate_data_key_without_plaintext(
        self,
        res: "bs_td.GenerateDataKeyWithoutPlaintextResponseTypeDef",
    ) -> "dc_td.GenerateDataKeyWithoutPlaintextResponse":
        return dc_td.GenerateDataKeyWithoutPlaintextResponse.make_one(res)

    def generate_mac(
        self,
        res: "bs_td.GenerateMacResponseTypeDef",
    ) -> "dc_td.GenerateMacResponse":
        return dc_td.GenerateMacResponse.make_one(res)

    def generate_random(
        self,
        res: "bs_td.GenerateRandomResponseTypeDef",
    ) -> "dc_td.GenerateRandomResponse":
        return dc_td.GenerateRandomResponse.make_one(res)

    def get_key_policy(
        self,
        res: "bs_td.GetKeyPolicyResponseTypeDef",
    ) -> "dc_td.GetKeyPolicyResponse":
        return dc_td.GetKeyPolicyResponse.make_one(res)

    def get_key_rotation_status(
        self,
        res: "bs_td.GetKeyRotationStatusResponseTypeDef",
    ) -> "dc_td.GetKeyRotationStatusResponse":
        return dc_td.GetKeyRotationStatusResponse.make_one(res)

    def get_parameters_for_import(
        self,
        res: "bs_td.GetParametersForImportResponseTypeDef",
    ) -> "dc_td.GetParametersForImportResponse":
        return dc_td.GetParametersForImportResponse.make_one(res)

    def get_public_key(
        self,
        res: "bs_td.GetPublicKeyResponseTypeDef",
    ) -> "dc_td.GetPublicKeyResponse":
        return dc_td.GetPublicKeyResponse.make_one(res)

    def import_key_material(
        self,
        res: "bs_td.ImportKeyMaterialResponseTypeDef",
    ) -> "dc_td.ImportKeyMaterialResponse":
        return dc_td.ImportKeyMaterialResponse.make_one(res)

    def list_aliases(
        self,
        res: "bs_td.ListAliasesResponseTypeDef",
    ) -> "dc_td.ListAliasesResponse":
        return dc_td.ListAliasesResponse.make_one(res)

    def list_grants(
        self,
        res: "bs_td.ListGrantsResponseTypeDef",
    ) -> "dc_td.ListGrantsResponse":
        return dc_td.ListGrantsResponse.make_one(res)

    def list_key_policies(
        self,
        res: "bs_td.ListKeyPoliciesResponseTypeDef",
    ) -> "dc_td.ListKeyPoliciesResponse":
        return dc_td.ListKeyPoliciesResponse.make_one(res)

    def list_key_rotations(
        self,
        res: "bs_td.ListKeyRotationsResponseTypeDef",
    ) -> "dc_td.ListKeyRotationsResponse":
        return dc_td.ListKeyRotationsResponse.make_one(res)

    def list_keys(
        self,
        res: "bs_td.ListKeysResponseTypeDef",
    ) -> "dc_td.ListKeysResponse":
        return dc_td.ListKeysResponse.make_one(res)

    def list_resource_tags(
        self,
        res: "bs_td.ListResourceTagsResponseTypeDef",
    ) -> "dc_td.ListResourceTagsResponse":
        return dc_td.ListResourceTagsResponse.make_one(res)

    def list_retirable_grants(
        self,
        res: "bs_td.ListGrantsResponseTypeDef",
    ) -> "dc_td.ListGrantsResponse":
        return dc_td.ListGrantsResponse.make_one(res)

    def put_key_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def re_encrypt(
        self,
        res: "bs_td.ReEncryptResponseTypeDef",
    ) -> "dc_td.ReEncryptResponse":
        return dc_td.ReEncryptResponse.make_one(res)

    def replicate_key(
        self,
        res: "bs_td.ReplicateKeyResponseTypeDef",
    ) -> "dc_td.ReplicateKeyResponse":
        return dc_td.ReplicateKeyResponse.make_one(res)

    def retire_grant(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def revoke_grant(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def rotate_key_on_demand(
        self,
        res: "bs_td.RotateKeyOnDemandResponseTypeDef",
    ) -> "dc_td.RotateKeyOnDemandResponse":
        return dc_td.RotateKeyOnDemandResponse.make_one(res)

    def schedule_key_deletion(
        self,
        res: "bs_td.ScheduleKeyDeletionResponseTypeDef",
    ) -> "dc_td.ScheduleKeyDeletionResponse":
        return dc_td.ScheduleKeyDeletionResponse.make_one(res)

    def sign(
        self,
        res: "bs_td.SignResponseTypeDef",
    ) -> "dc_td.SignResponse":
        return dc_td.SignResponse.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_alias(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_key_description(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_primary_region(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def verify(
        self,
        res: "bs_td.VerifyResponseTypeDef",
    ) -> "dc_td.VerifyResponse":
        return dc_td.VerifyResponse.make_one(res)

    def verify_mac(
        self,
        res: "bs_td.VerifyMacResponseTypeDef",
    ) -> "dc_td.VerifyMacResponse":
        return dc_td.VerifyMacResponse.make_one(res)


kms_caster = KMSCaster()
