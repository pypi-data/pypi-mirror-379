# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_clouddirectory import type_defs as bs_td


class CLOUDDIRECTORYCaster:

    def apply_schema(
        self,
        res: "bs_td.ApplySchemaResponseTypeDef",
    ) -> "dc_td.ApplySchemaResponse":
        return dc_td.ApplySchemaResponse.make_one(res)

    def attach_object(
        self,
        res: "bs_td.AttachObjectResponseTypeDef",
    ) -> "dc_td.AttachObjectResponse":
        return dc_td.AttachObjectResponse.make_one(res)

    def attach_to_index(
        self,
        res: "bs_td.AttachToIndexResponseTypeDef",
    ) -> "dc_td.AttachToIndexResponse":
        return dc_td.AttachToIndexResponse.make_one(res)

    def attach_typed_link(
        self,
        res: "bs_td.AttachTypedLinkResponseTypeDef",
    ) -> "dc_td.AttachTypedLinkResponse":
        return dc_td.AttachTypedLinkResponse.make_one(res)

    def batch_read(
        self,
        res: "bs_td.BatchReadResponseTypeDef",
    ) -> "dc_td.BatchReadResponse":
        return dc_td.BatchReadResponse.make_one(res)

    def batch_write(
        self,
        res: "bs_td.BatchWriteResponseTypeDef",
    ) -> "dc_td.BatchWriteResponse":
        return dc_td.BatchWriteResponse.make_one(res)

    def create_directory(
        self,
        res: "bs_td.CreateDirectoryResponseTypeDef",
    ) -> "dc_td.CreateDirectoryResponse":
        return dc_td.CreateDirectoryResponse.make_one(res)

    def create_index(
        self,
        res: "bs_td.CreateIndexResponseTypeDef",
    ) -> "dc_td.CreateIndexResponse":
        return dc_td.CreateIndexResponse.make_one(res)

    def create_object(
        self,
        res: "bs_td.CreateObjectResponseTypeDef",
    ) -> "dc_td.CreateObjectResponse":
        return dc_td.CreateObjectResponse.make_one(res)

    def create_schema(
        self,
        res: "bs_td.CreateSchemaResponseTypeDef",
    ) -> "dc_td.CreateSchemaResponse":
        return dc_td.CreateSchemaResponse.make_one(res)

    def delete_directory(
        self,
        res: "bs_td.DeleteDirectoryResponseTypeDef",
    ) -> "dc_td.DeleteDirectoryResponse":
        return dc_td.DeleteDirectoryResponse.make_one(res)

    def delete_schema(
        self,
        res: "bs_td.DeleteSchemaResponseTypeDef",
    ) -> "dc_td.DeleteSchemaResponse":
        return dc_td.DeleteSchemaResponse.make_one(res)

    def detach_from_index(
        self,
        res: "bs_td.DetachFromIndexResponseTypeDef",
    ) -> "dc_td.DetachFromIndexResponse":
        return dc_td.DetachFromIndexResponse.make_one(res)

    def detach_object(
        self,
        res: "bs_td.DetachObjectResponseTypeDef",
    ) -> "dc_td.DetachObjectResponse":
        return dc_td.DetachObjectResponse.make_one(res)

    def detach_typed_link(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disable_directory(
        self,
        res: "bs_td.DisableDirectoryResponseTypeDef",
    ) -> "dc_td.DisableDirectoryResponse":
        return dc_td.DisableDirectoryResponse.make_one(res)

    def enable_directory(
        self,
        res: "bs_td.EnableDirectoryResponseTypeDef",
    ) -> "dc_td.EnableDirectoryResponse":
        return dc_td.EnableDirectoryResponse.make_one(res)

    def get_applied_schema_version(
        self,
        res: "bs_td.GetAppliedSchemaVersionResponseTypeDef",
    ) -> "dc_td.GetAppliedSchemaVersionResponse":
        return dc_td.GetAppliedSchemaVersionResponse.make_one(res)

    def get_directory(
        self,
        res: "bs_td.GetDirectoryResponseTypeDef",
    ) -> "dc_td.GetDirectoryResponse":
        return dc_td.GetDirectoryResponse.make_one(res)

    def get_facet(
        self,
        res: "bs_td.GetFacetResponseTypeDef",
    ) -> "dc_td.GetFacetResponse":
        return dc_td.GetFacetResponse.make_one(res)

    def get_link_attributes(
        self,
        res: "bs_td.GetLinkAttributesResponseTypeDef",
    ) -> "dc_td.GetLinkAttributesResponse":
        return dc_td.GetLinkAttributesResponse.make_one(res)

    def get_object_attributes(
        self,
        res: "bs_td.GetObjectAttributesResponseTypeDef",
    ) -> "dc_td.GetObjectAttributesResponse":
        return dc_td.GetObjectAttributesResponse.make_one(res)

    def get_object_information(
        self,
        res: "bs_td.GetObjectInformationResponseTypeDef",
    ) -> "dc_td.GetObjectInformationResponse":
        return dc_td.GetObjectInformationResponse.make_one(res)

    def get_schema_as_json(
        self,
        res: "bs_td.GetSchemaAsJsonResponseTypeDef",
    ) -> "dc_td.GetSchemaAsJsonResponse":
        return dc_td.GetSchemaAsJsonResponse.make_one(res)

    def get_typed_link_facet_information(
        self,
        res: "bs_td.GetTypedLinkFacetInformationResponseTypeDef",
    ) -> "dc_td.GetTypedLinkFacetInformationResponse":
        return dc_td.GetTypedLinkFacetInformationResponse.make_one(res)

    def list_applied_schema_arns(
        self,
        res: "bs_td.ListAppliedSchemaArnsResponseTypeDef",
    ) -> "dc_td.ListAppliedSchemaArnsResponse":
        return dc_td.ListAppliedSchemaArnsResponse.make_one(res)

    def list_attached_indices(
        self,
        res: "bs_td.ListAttachedIndicesResponseTypeDef",
    ) -> "dc_td.ListAttachedIndicesResponse":
        return dc_td.ListAttachedIndicesResponse.make_one(res)

    def list_development_schema_arns(
        self,
        res: "bs_td.ListDevelopmentSchemaArnsResponseTypeDef",
    ) -> "dc_td.ListDevelopmentSchemaArnsResponse":
        return dc_td.ListDevelopmentSchemaArnsResponse.make_one(res)

    def list_directories(
        self,
        res: "bs_td.ListDirectoriesResponseTypeDef",
    ) -> "dc_td.ListDirectoriesResponse":
        return dc_td.ListDirectoriesResponse.make_one(res)

    def list_facet_attributes(
        self,
        res: "bs_td.ListFacetAttributesResponseTypeDef",
    ) -> "dc_td.ListFacetAttributesResponse":
        return dc_td.ListFacetAttributesResponse.make_one(res)

    def list_facet_names(
        self,
        res: "bs_td.ListFacetNamesResponseTypeDef",
    ) -> "dc_td.ListFacetNamesResponse":
        return dc_td.ListFacetNamesResponse.make_one(res)

    def list_incoming_typed_links(
        self,
        res: "bs_td.ListIncomingTypedLinksResponseTypeDef",
    ) -> "dc_td.ListIncomingTypedLinksResponse":
        return dc_td.ListIncomingTypedLinksResponse.make_one(res)

    def list_index(
        self,
        res: "bs_td.ListIndexResponseTypeDef",
    ) -> "dc_td.ListIndexResponse":
        return dc_td.ListIndexResponse.make_one(res)

    def list_managed_schema_arns(
        self,
        res: "bs_td.ListManagedSchemaArnsResponseTypeDef",
    ) -> "dc_td.ListManagedSchemaArnsResponse":
        return dc_td.ListManagedSchemaArnsResponse.make_one(res)

    def list_object_attributes(
        self,
        res: "bs_td.ListObjectAttributesResponseTypeDef",
    ) -> "dc_td.ListObjectAttributesResponse":
        return dc_td.ListObjectAttributesResponse.make_one(res)

    def list_object_children(
        self,
        res: "bs_td.ListObjectChildrenResponseTypeDef",
    ) -> "dc_td.ListObjectChildrenResponse":
        return dc_td.ListObjectChildrenResponse.make_one(res)

    def list_object_parent_paths(
        self,
        res: "bs_td.ListObjectParentPathsResponseTypeDef",
    ) -> "dc_td.ListObjectParentPathsResponse":
        return dc_td.ListObjectParentPathsResponse.make_one(res)

    def list_object_parents(
        self,
        res: "bs_td.ListObjectParentsResponseTypeDef",
    ) -> "dc_td.ListObjectParentsResponse":
        return dc_td.ListObjectParentsResponse.make_one(res)

    def list_object_policies(
        self,
        res: "bs_td.ListObjectPoliciesResponseTypeDef",
    ) -> "dc_td.ListObjectPoliciesResponse":
        return dc_td.ListObjectPoliciesResponse.make_one(res)

    def list_outgoing_typed_links(
        self,
        res: "bs_td.ListOutgoingTypedLinksResponseTypeDef",
    ) -> "dc_td.ListOutgoingTypedLinksResponse":
        return dc_td.ListOutgoingTypedLinksResponse.make_one(res)

    def list_policy_attachments(
        self,
        res: "bs_td.ListPolicyAttachmentsResponseTypeDef",
    ) -> "dc_td.ListPolicyAttachmentsResponse":
        return dc_td.ListPolicyAttachmentsResponse.make_one(res)

    def list_published_schema_arns(
        self,
        res: "bs_td.ListPublishedSchemaArnsResponseTypeDef",
    ) -> "dc_td.ListPublishedSchemaArnsResponse":
        return dc_td.ListPublishedSchemaArnsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_typed_link_facet_attributes(
        self,
        res: "bs_td.ListTypedLinkFacetAttributesResponseTypeDef",
    ) -> "dc_td.ListTypedLinkFacetAttributesResponse":
        return dc_td.ListTypedLinkFacetAttributesResponse.make_one(res)

    def list_typed_link_facet_names(
        self,
        res: "bs_td.ListTypedLinkFacetNamesResponseTypeDef",
    ) -> "dc_td.ListTypedLinkFacetNamesResponse":
        return dc_td.ListTypedLinkFacetNamesResponse.make_one(res)

    def lookup_policy(
        self,
        res: "bs_td.LookupPolicyResponseTypeDef",
    ) -> "dc_td.LookupPolicyResponse":
        return dc_td.LookupPolicyResponse.make_one(res)

    def publish_schema(
        self,
        res: "bs_td.PublishSchemaResponseTypeDef",
    ) -> "dc_td.PublishSchemaResponse":
        return dc_td.PublishSchemaResponse.make_one(res)

    def put_schema_from_json(
        self,
        res: "bs_td.PutSchemaFromJsonResponseTypeDef",
    ) -> "dc_td.PutSchemaFromJsonResponse":
        return dc_td.PutSchemaFromJsonResponse.make_one(res)

    def update_object_attributes(
        self,
        res: "bs_td.UpdateObjectAttributesResponseTypeDef",
    ) -> "dc_td.UpdateObjectAttributesResponse":
        return dc_td.UpdateObjectAttributesResponse.make_one(res)

    def update_schema(
        self,
        res: "bs_td.UpdateSchemaResponseTypeDef",
    ) -> "dc_td.UpdateSchemaResponse":
        return dc_td.UpdateSchemaResponse.make_one(res)

    def upgrade_applied_schema(
        self,
        res: "bs_td.UpgradeAppliedSchemaResponseTypeDef",
    ) -> "dc_td.UpgradeAppliedSchemaResponse":
        return dc_td.UpgradeAppliedSchemaResponse.make_one(res)

    def upgrade_published_schema(
        self,
        res: "bs_td.UpgradePublishedSchemaResponseTypeDef",
    ) -> "dc_td.UpgradePublishedSchemaResponse":
        return dc_td.UpgradePublishedSchemaResponse.make_one(res)


clouddirectory_caster = CLOUDDIRECTORYCaster()
