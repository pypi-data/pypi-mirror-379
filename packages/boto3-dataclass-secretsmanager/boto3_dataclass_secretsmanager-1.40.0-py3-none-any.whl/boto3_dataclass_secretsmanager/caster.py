# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_secretsmanager import type_defs as bs_td


class SECRETSMANAGERCaster:

    def batch_get_secret_value(
        self,
        res: "bs_td.BatchGetSecretValueResponseTypeDef",
    ) -> "dc_td.BatchGetSecretValueResponse":
        return dc_td.BatchGetSecretValueResponse.make_one(res)

    def cancel_rotate_secret(
        self,
        res: "bs_td.CancelRotateSecretResponseTypeDef",
    ) -> "dc_td.CancelRotateSecretResponse":
        return dc_td.CancelRotateSecretResponse.make_one(res)

    def create_secret(
        self,
        res: "bs_td.CreateSecretResponseTypeDef",
    ) -> "dc_td.CreateSecretResponse":
        return dc_td.CreateSecretResponse.make_one(res)

    def delete_resource_policy(
        self,
        res: "bs_td.DeleteResourcePolicyResponseTypeDef",
    ) -> "dc_td.DeleteResourcePolicyResponse":
        return dc_td.DeleteResourcePolicyResponse.make_one(res)

    def delete_secret(
        self,
        res: "bs_td.DeleteSecretResponseTypeDef",
    ) -> "dc_td.DeleteSecretResponse":
        return dc_td.DeleteSecretResponse.make_one(res)

    def describe_secret(
        self,
        res: "bs_td.DescribeSecretResponseTypeDef",
    ) -> "dc_td.DescribeSecretResponse":
        return dc_td.DescribeSecretResponse.make_one(res)

    def get_random_password(
        self,
        res: "bs_td.GetRandomPasswordResponseTypeDef",
    ) -> "dc_td.GetRandomPasswordResponse":
        return dc_td.GetRandomPasswordResponse.make_one(res)

    def get_resource_policy(
        self,
        res: "bs_td.GetResourcePolicyResponseTypeDef",
    ) -> "dc_td.GetResourcePolicyResponse":
        return dc_td.GetResourcePolicyResponse.make_one(res)

    def get_secret_value(
        self,
        res: "bs_td.GetSecretValueResponseTypeDef",
    ) -> "dc_td.GetSecretValueResponse":
        return dc_td.GetSecretValueResponse.make_one(res)

    def list_secret_version_ids(
        self,
        res: "bs_td.ListSecretVersionIdsResponseTypeDef",
    ) -> "dc_td.ListSecretVersionIdsResponse":
        return dc_td.ListSecretVersionIdsResponse.make_one(res)

    def list_secrets(
        self,
        res: "bs_td.ListSecretsResponseTypeDef",
    ) -> "dc_td.ListSecretsResponse":
        return dc_td.ListSecretsResponse.make_one(res)

    def put_resource_policy(
        self,
        res: "bs_td.PutResourcePolicyResponseTypeDef",
    ) -> "dc_td.PutResourcePolicyResponse":
        return dc_td.PutResourcePolicyResponse.make_one(res)

    def put_secret_value(
        self,
        res: "bs_td.PutSecretValueResponseTypeDef",
    ) -> "dc_td.PutSecretValueResponse":
        return dc_td.PutSecretValueResponse.make_one(res)

    def remove_regions_from_replication(
        self,
        res: "bs_td.RemoveRegionsFromReplicationResponseTypeDef",
    ) -> "dc_td.RemoveRegionsFromReplicationResponse":
        return dc_td.RemoveRegionsFromReplicationResponse.make_one(res)

    def replicate_secret_to_regions(
        self,
        res: "bs_td.ReplicateSecretToRegionsResponseTypeDef",
    ) -> "dc_td.ReplicateSecretToRegionsResponse":
        return dc_td.ReplicateSecretToRegionsResponse.make_one(res)

    def restore_secret(
        self,
        res: "bs_td.RestoreSecretResponseTypeDef",
    ) -> "dc_td.RestoreSecretResponse":
        return dc_td.RestoreSecretResponse.make_one(res)

    def rotate_secret(
        self,
        res: "bs_td.RotateSecretResponseTypeDef",
    ) -> "dc_td.RotateSecretResponse":
        return dc_td.RotateSecretResponse.make_one(res)

    def stop_replication_to_replica(
        self,
        res: "bs_td.StopReplicationToReplicaResponseTypeDef",
    ) -> "dc_td.StopReplicationToReplicaResponse":
        return dc_td.StopReplicationToReplicaResponse.make_one(res)

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

    def update_secret(
        self,
        res: "bs_td.UpdateSecretResponseTypeDef",
    ) -> "dc_td.UpdateSecretResponse":
        return dc_td.UpdateSecretResponse.make_one(res)

    def update_secret_version_stage(
        self,
        res: "bs_td.UpdateSecretVersionStageResponseTypeDef",
    ) -> "dc_td.UpdateSecretVersionStageResponse":
        return dc_td.UpdateSecretVersionStageResponse.make_one(res)

    def validate_resource_policy(
        self,
        res: "bs_td.ValidateResourcePolicyResponseTypeDef",
    ) -> "dc_td.ValidateResourcePolicyResponse":
        return dc_td.ValidateResourcePolicyResponse.make_one(res)


secretsmanager_caster = SECRETSMANAGERCaster()
