# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_s3 import type_defs as bs_td


class S3Caster:

    def abort_multipart_upload(
        self,
        res: "bs_td.AbortMultipartUploadOutputTypeDef",
    ) -> "dc_td.AbortMultipartUploadOutput":
        return dc_td.AbortMultipartUploadOutput.make_one(res)

    def complete_multipart_upload(
        self,
        res: "bs_td.CompleteMultipartUploadOutputTypeDef",
    ) -> "dc_td.CompleteMultipartUploadOutput":
        return dc_td.CompleteMultipartUploadOutput.make_one(res)

    def copy_object(
        self,
        res: "bs_td.CopyObjectOutputTypeDef",
    ) -> "dc_td.CopyObjectOutput":
        return dc_td.CopyObjectOutput.make_one(res)

    def create_bucket(
        self,
        res: "bs_td.CreateBucketOutputTypeDef",
    ) -> "dc_td.CreateBucketOutput":
        return dc_td.CreateBucketOutput.make_one(res)

    def create_bucket_metadata_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_bucket_metadata_table_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def create_multipart_upload(
        self,
        res: "bs_td.CreateMultipartUploadOutputTypeDef",
    ) -> "dc_td.CreateMultipartUploadOutput":
        return dc_td.CreateMultipartUploadOutput.make_one(res)

    def create_session(
        self,
        res: "bs_td.CreateSessionOutputTypeDef",
    ) -> "dc_td.CreateSessionOutput":
        return dc_td.CreateSessionOutput.make_one(res)

    def delete_bucket(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_bucket_analytics_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_bucket_cors(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_bucket_encryption(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_bucket_intelligent_tiering_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_bucket_inventory_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_bucket_lifecycle(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_bucket_metadata_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_bucket_metadata_table_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_bucket_metrics_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_bucket_ownership_controls(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_bucket_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_bucket_replication(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_bucket_tagging(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_bucket_website(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_object(
        self,
        res: "bs_td.DeleteObjectOutputTypeDef",
    ) -> "dc_td.DeleteObjectOutput":
        return dc_td.DeleteObjectOutput.make_one(res)

    def delete_object_tagging(
        self,
        res: "bs_td.DeleteObjectTaggingOutputTypeDef",
    ) -> "dc_td.DeleteObjectTaggingOutput":
        return dc_td.DeleteObjectTaggingOutput.make_one(res)

    def delete_objects(
        self,
        res: "bs_td.DeleteObjectsOutputTypeDef",
    ) -> "dc_td.DeleteObjectsOutput":
        return dc_td.DeleteObjectsOutput.make_one(res)

    def delete_public_access_block(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_bucket_accelerate_configuration(
        self,
        res: "bs_td.GetBucketAccelerateConfigurationOutputTypeDef",
    ) -> "dc_td.GetBucketAccelerateConfigurationOutput":
        return dc_td.GetBucketAccelerateConfigurationOutput.make_one(res)

    def get_bucket_acl(
        self,
        res: "bs_td.GetBucketAclOutputTypeDef",
    ) -> "dc_td.GetBucketAclOutput":
        return dc_td.GetBucketAclOutput.make_one(res)

    def get_bucket_analytics_configuration(
        self,
        res: "bs_td.GetBucketAnalyticsConfigurationOutputTypeDef",
    ) -> "dc_td.GetBucketAnalyticsConfigurationOutput":
        return dc_td.GetBucketAnalyticsConfigurationOutput.make_one(res)

    def get_bucket_cors(
        self,
        res: "bs_td.GetBucketCorsOutputTypeDef",
    ) -> "dc_td.GetBucketCorsOutput":
        return dc_td.GetBucketCorsOutput.make_one(res)

    def get_bucket_encryption(
        self,
        res: "bs_td.GetBucketEncryptionOutputTypeDef",
    ) -> "dc_td.GetBucketEncryptionOutput":
        return dc_td.GetBucketEncryptionOutput.make_one(res)

    def get_bucket_intelligent_tiering_configuration(
        self,
        res: "bs_td.GetBucketIntelligentTieringConfigurationOutputTypeDef",
    ) -> "dc_td.GetBucketIntelligentTieringConfigurationOutput":
        return dc_td.GetBucketIntelligentTieringConfigurationOutput.make_one(res)

    def get_bucket_inventory_configuration(
        self,
        res: "bs_td.GetBucketInventoryConfigurationOutputTypeDef",
    ) -> "dc_td.GetBucketInventoryConfigurationOutput":
        return dc_td.GetBucketInventoryConfigurationOutput.make_one(res)

    def get_bucket_lifecycle(
        self,
        res: "bs_td.GetBucketLifecycleOutputTypeDef",
    ) -> "dc_td.GetBucketLifecycleOutput":
        return dc_td.GetBucketLifecycleOutput.make_one(res)

    def get_bucket_lifecycle_configuration(
        self,
        res: "bs_td.GetBucketLifecycleConfigurationOutputTypeDef",
    ) -> "dc_td.GetBucketLifecycleConfigurationOutput":
        return dc_td.GetBucketLifecycleConfigurationOutput.make_one(res)

    def get_bucket_location(
        self,
        res: "bs_td.GetBucketLocationOutputTypeDef",
    ) -> "dc_td.GetBucketLocationOutput":
        return dc_td.GetBucketLocationOutput.make_one(res)

    def get_bucket_logging(
        self,
        res: "bs_td.GetBucketLoggingOutputTypeDef",
    ) -> "dc_td.GetBucketLoggingOutput":
        return dc_td.GetBucketLoggingOutput.make_one(res)

    def get_bucket_metadata_configuration(
        self,
        res: "bs_td.GetBucketMetadataConfigurationOutputTypeDef",
    ) -> "dc_td.GetBucketMetadataConfigurationOutput":
        return dc_td.GetBucketMetadataConfigurationOutput.make_one(res)

    def get_bucket_metadata_table_configuration(
        self,
        res: "bs_td.GetBucketMetadataTableConfigurationOutputTypeDef",
    ) -> "dc_td.GetBucketMetadataTableConfigurationOutput":
        return dc_td.GetBucketMetadataTableConfigurationOutput.make_one(res)

    def get_bucket_metrics_configuration(
        self,
        res: "bs_td.GetBucketMetricsConfigurationOutputTypeDef",
    ) -> "dc_td.GetBucketMetricsConfigurationOutput":
        return dc_td.GetBucketMetricsConfigurationOutput.make_one(res)

    def get_bucket_notification(
        self,
        res: "bs_td.NotificationConfigurationDeprecatedResponseTypeDef",
    ) -> "dc_td.NotificationConfigurationDeprecatedResponse":
        return dc_td.NotificationConfigurationDeprecatedResponse.make_one(res)

    def get_bucket_notification_configuration(
        self,
        res: "bs_td.NotificationConfigurationResponseTypeDef",
    ) -> "dc_td.NotificationConfigurationResponse":
        return dc_td.NotificationConfigurationResponse.make_one(res)

    def get_bucket_ownership_controls(
        self,
        res: "bs_td.GetBucketOwnershipControlsOutputTypeDef",
    ) -> "dc_td.GetBucketOwnershipControlsOutput":
        return dc_td.GetBucketOwnershipControlsOutput.make_one(res)

    def get_bucket_policy(
        self,
        res: "bs_td.GetBucketPolicyOutputTypeDef",
    ) -> "dc_td.GetBucketPolicyOutput":
        return dc_td.GetBucketPolicyOutput.make_one(res)

    def get_bucket_policy_status(
        self,
        res: "bs_td.GetBucketPolicyStatusOutputTypeDef",
    ) -> "dc_td.GetBucketPolicyStatusOutput":
        return dc_td.GetBucketPolicyStatusOutput.make_one(res)

    def get_bucket_replication(
        self,
        res: "bs_td.GetBucketReplicationOutputTypeDef",
    ) -> "dc_td.GetBucketReplicationOutput":
        return dc_td.GetBucketReplicationOutput.make_one(res)

    def get_bucket_request_payment(
        self,
        res: "bs_td.GetBucketRequestPaymentOutputTypeDef",
    ) -> "dc_td.GetBucketRequestPaymentOutput":
        return dc_td.GetBucketRequestPaymentOutput.make_one(res)

    def get_bucket_tagging(
        self,
        res: "bs_td.GetBucketTaggingOutputTypeDef",
    ) -> "dc_td.GetBucketTaggingOutput":
        return dc_td.GetBucketTaggingOutput.make_one(res)

    def get_bucket_versioning(
        self,
        res: "bs_td.GetBucketVersioningOutputTypeDef",
    ) -> "dc_td.GetBucketVersioningOutput":
        return dc_td.GetBucketVersioningOutput.make_one(res)

    def get_bucket_website(
        self,
        res: "bs_td.GetBucketWebsiteOutputTypeDef",
    ) -> "dc_td.GetBucketWebsiteOutput":
        return dc_td.GetBucketWebsiteOutput.make_one(res)

    def get_object(
        self,
        res: "bs_td.GetObjectOutputTypeDef",
    ) -> "dc_td.GetObjectOutput":
        return dc_td.GetObjectOutput.make_one(res)

    def get_object_acl(
        self,
        res: "bs_td.GetObjectAclOutputTypeDef",
    ) -> "dc_td.GetObjectAclOutput":
        return dc_td.GetObjectAclOutput.make_one(res)

    def get_object_attributes(
        self,
        res: "bs_td.GetObjectAttributesOutputTypeDef",
    ) -> "dc_td.GetObjectAttributesOutput":
        return dc_td.GetObjectAttributesOutput.make_one(res)

    def get_object_legal_hold(
        self,
        res: "bs_td.GetObjectLegalHoldOutputTypeDef",
    ) -> "dc_td.GetObjectLegalHoldOutput":
        return dc_td.GetObjectLegalHoldOutput.make_one(res)

    def get_object_lock_configuration(
        self,
        res: "bs_td.GetObjectLockConfigurationOutputTypeDef",
    ) -> "dc_td.GetObjectLockConfigurationOutput":
        return dc_td.GetObjectLockConfigurationOutput.make_one(res)

    def get_object_retention(
        self,
        res: "bs_td.GetObjectRetentionOutputTypeDef",
    ) -> "dc_td.GetObjectRetentionOutput":
        return dc_td.GetObjectRetentionOutput.make_one(res)

    def get_object_tagging(
        self,
        res: "bs_td.GetObjectTaggingOutputTypeDef",
    ) -> "dc_td.GetObjectTaggingOutput":
        return dc_td.GetObjectTaggingOutput.make_one(res)

    def get_object_torrent(
        self,
        res: "bs_td.GetObjectTorrentOutputTypeDef",
    ) -> "dc_td.GetObjectTorrentOutput":
        return dc_td.GetObjectTorrentOutput.make_one(res)

    def get_public_access_block(
        self,
        res: "bs_td.GetPublicAccessBlockOutputTypeDef",
    ) -> "dc_td.GetPublicAccessBlockOutput":
        return dc_td.GetPublicAccessBlockOutput.make_one(res)

    def head_bucket(
        self,
        res: "bs_td.HeadBucketOutputTypeDef",
    ) -> "dc_td.HeadBucketOutput":
        return dc_td.HeadBucketOutput.make_one(res)

    def head_object(
        self,
        res: "bs_td.HeadObjectOutputTypeDef",
    ) -> "dc_td.HeadObjectOutput":
        return dc_td.HeadObjectOutput.make_one(res)

    def list_bucket_analytics_configurations(
        self,
        res: "bs_td.ListBucketAnalyticsConfigurationsOutputTypeDef",
    ) -> "dc_td.ListBucketAnalyticsConfigurationsOutput":
        return dc_td.ListBucketAnalyticsConfigurationsOutput.make_one(res)

    def list_bucket_intelligent_tiering_configurations(
        self,
        res: "bs_td.ListBucketIntelligentTieringConfigurationsOutputTypeDef",
    ) -> "dc_td.ListBucketIntelligentTieringConfigurationsOutput":
        return dc_td.ListBucketIntelligentTieringConfigurationsOutput.make_one(res)

    def list_bucket_inventory_configurations(
        self,
        res: "bs_td.ListBucketInventoryConfigurationsOutputTypeDef",
    ) -> "dc_td.ListBucketInventoryConfigurationsOutput":
        return dc_td.ListBucketInventoryConfigurationsOutput.make_one(res)

    def list_bucket_metrics_configurations(
        self,
        res: "bs_td.ListBucketMetricsConfigurationsOutputTypeDef",
    ) -> "dc_td.ListBucketMetricsConfigurationsOutput":
        return dc_td.ListBucketMetricsConfigurationsOutput.make_one(res)

    def list_buckets(
        self,
        res: "bs_td.ListBucketsOutputTypeDef",
    ) -> "dc_td.ListBucketsOutput":
        return dc_td.ListBucketsOutput.make_one(res)

    def list_directory_buckets(
        self,
        res: "bs_td.ListDirectoryBucketsOutputTypeDef",
    ) -> "dc_td.ListDirectoryBucketsOutput":
        return dc_td.ListDirectoryBucketsOutput.make_one(res)

    def list_multipart_uploads(
        self,
        res: "bs_td.ListMultipartUploadsOutputTypeDef",
    ) -> "dc_td.ListMultipartUploadsOutput":
        return dc_td.ListMultipartUploadsOutput.make_one(res)

    def list_object_versions(
        self,
        res: "bs_td.ListObjectVersionsOutputTypeDef",
    ) -> "dc_td.ListObjectVersionsOutput":
        return dc_td.ListObjectVersionsOutput.make_one(res)

    def list_objects(
        self,
        res: "bs_td.ListObjectsOutputTypeDef",
    ) -> "dc_td.ListObjectsOutput":
        return dc_td.ListObjectsOutput.make_one(res)

    def list_objects_v2(
        self,
        res: "bs_td.ListObjectsV2OutputTypeDef",
    ) -> "dc_td.ListObjectsV2Output":
        return dc_td.ListObjectsV2Output.make_one(res)

    def list_parts(
        self,
        res: "bs_td.ListPartsOutputTypeDef",
    ) -> "dc_td.ListPartsOutput":
        return dc_td.ListPartsOutput.make_one(res)

    def put_bucket_accelerate_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_bucket_acl(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_bucket_analytics_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_bucket_cors(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_bucket_encryption(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_bucket_intelligent_tiering_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_bucket_inventory_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_bucket_lifecycle(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_bucket_lifecycle_configuration(
        self,
        res: "bs_td.PutBucketLifecycleConfigurationOutputTypeDef",
    ) -> "dc_td.PutBucketLifecycleConfigurationOutput":
        return dc_td.PutBucketLifecycleConfigurationOutput.make_one(res)

    def put_bucket_logging(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_bucket_metrics_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_bucket_notification(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_bucket_notification_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_bucket_ownership_controls(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_bucket_policy(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_bucket_replication(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_bucket_request_payment(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_bucket_tagging(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_bucket_versioning(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_bucket_website(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_object(
        self,
        res: "bs_td.PutObjectOutputTypeDef",
    ) -> "dc_td.PutObjectOutput":
        return dc_td.PutObjectOutput.make_one(res)

    def put_object_acl(
        self,
        res: "bs_td.PutObjectAclOutputTypeDef",
    ) -> "dc_td.PutObjectAclOutput":
        return dc_td.PutObjectAclOutput.make_one(res)

    def put_object_legal_hold(
        self,
        res: "bs_td.PutObjectLegalHoldOutputTypeDef",
    ) -> "dc_td.PutObjectLegalHoldOutput":
        return dc_td.PutObjectLegalHoldOutput.make_one(res)

    def put_object_lock_configuration(
        self,
        res: "bs_td.PutObjectLockConfigurationOutputTypeDef",
    ) -> "dc_td.PutObjectLockConfigurationOutput":
        return dc_td.PutObjectLockConfigurationOutput.make_one(res)

    def put_object_retention(
        self,
        res: "bs_td.PutObjectRetentionOutputTypeDef",
    ) -> "dc_td.PutObjectRetentionOutput":
        return dc_td.PutObjectRetentionOutput.make_one(res)

    def put_object_tagging(
        self,
        res: "bs_td.PutObjectTaggingOutputTypeDef",
    ) -> "dc_td.PutObjectTaggingOutput":
        return dc_td.PutObjectTaggingOutput.make_one(res)

    def put_public_access_block(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def restore_object(
        self,
        res: "bs_td.RestoreObjectOutputTypeDef",
    ) -> "dc_td.RestoreObjectOutput":
        return dc_td.RestoreObjectOutput.make_one(res)

    def select_object_content(
        self,
        res: "bs_td.SelectObjectContentOutputTypeDef",
    ) -> "dc_td.SelectObjectContentOutput":
        return dc_td.SelectObjectContentOutput.make_one(res)

    def update_bucket_metadata_inventory_table_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_bucket_metadata_journal_table_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def upload_part(
        self,
        res: "bs_td.UploadPartOutputTypeDef",
    ) -> "dc_td.UploadPartOutput":
        return dc_td.UploadPartOutput.make_one(res)

    def upload_part_copy(
        self,
        res: "bs_td.UploadPartCopyOutputTypeDef",
    ) -> "dc_td.UploadPartCopyOutput":
        return dc_td.UploadPartCopyOutput.make_one(res)

    def write_get_object_response(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


s3_caster = S3Caster()
