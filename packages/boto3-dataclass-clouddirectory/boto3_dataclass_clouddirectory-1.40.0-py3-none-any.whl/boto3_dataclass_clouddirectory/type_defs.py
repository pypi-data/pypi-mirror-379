# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_clouddirectory import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ObjectReference:
    boto3_raw_data: "type_defs.ObjectReferenceTypeDef" = dataclasses.field()

    Selector = field("Selector")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ObjectReferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ObjectReferenceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaFacet:
    boto3_raw_data: "type_defs.SchemaFacetTypeDef" = dataclasses.field()

    SchemaArn = field("SchemaArn")
    FacetName = field("FacetName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SchemaFacetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SchemaFacetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplySchemaRequest:
    boto3_raw_data: "type_defs.ApplySchemaRequestTypeDef" = dataclasses.field()

    PublishedSchemaArn = field("PublishedSchemaArn")
    DirectoryArn = field("DirectoryArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplySchemaRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplySchemaRequestTypeDef"]
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
class TypedLinkSchemaAndFacetName:
    boto3_raw_data: "type_defs.TypedLinkSchemaAndFacetNameTypeDef" = dataclasses.field()

    SchemaArn = field("SchemaArn")
    TypedLinkName = field("TypedLinkName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TypedLinkSchemaAndFacetNameTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TypedLinkSchemaAndFacetNameTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeKey:
    boto3_raw_data: "type_defs.AttributeKeyTypeDef" = dataclasses.field()

    SchemaArn = field("SchemaArn")
    FacetName = field("FacetName")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AttributeKeyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AttributeKeyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TypedAttributeValueOutput:
    boto3_raw_data: "type_defs.TypedAttributeValueOutputTypeDef" = dataclasses.field()

    StringValue = field("StringValue")
    BinaryValue = field("BinaryValue")
    BooleanValue = field("BooleanValue")
    NumberValue = field("NumberValue")
    DatetimeValue = field("DatetimeValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TypedAttributeValueOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TypedAttributeValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAttachObjectResponse:
    boto3_raw_data: "type_defs.BatchAttachObjectResponseTypeDef" = dataclasses.field()

    attachedObjectIdentifier = field("attachedObjectIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchAttachObjectResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchAttachObjectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAttachToIndexResponse:
    boto3_raw_data: "type_defs.BatchAttachToIndexResponseTypeDef" = dataclasses.field()

    AttachedObjectIdentifier = field("AttachedObjectIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchAttachToIndexResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchAttachToIndexResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateIndexResponse:
    boto3_raw_data: "type_defs.BatchCreateIndexResponseTypeDef" = dataclasses.field()

    ObjectIdentifier = field("ObjectIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchCreateIndexResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateIndexResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateObjectResponse:
    boto3_raw_data: "type_defs.BatchCreateObjectResponseTypeDef" = dataclasses.field()

    ObjectIdentifier = field("ObjectIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchCreateObjectResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateObjectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDetachFromIndexResponse:
    boto3_raw_data: "type_defs.BatchDetachFromIndexResponseTypeDef" = (
        dataclasses.field()
    )

    DetachedObjectIdentifier = field("DetachedObjectIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDetachFromIndexResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDetachFromIndexResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDetachObjectResponse:
    boto3_raw_data: "type_defs.BatchDetachObjectResponseTypeDef" = dataclasses.field()

    detachedObjectIdentifier = field("detachedObjectIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDetachObjectResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDetachObjectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchListObjectChildrenResponse:
    boto3_raw_data: "type_defs.BatchListObjectChildrenResponseTypeDef" = (
        dataclasses.field()
    )

    Children = field("Children")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchListObjectChildrenResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchListObjectChildrenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PathToObjectIdentifiers:
    boto3_raw_data: "type_defs.PathToObjectIdentifiersTypeDef" = dataclasses.field()

    Path = field("Path")
    ObjectIdentifiers = field("ObjectIdentifiers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PathToObjectIdentifiersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PathToObjectIdentifiersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectIdentifierAndLinkNameTuple:
    boto3_raw_data: "type_defs.ObjectIdentifierAndLinkNameTupleTypeDef" = (
        dataclasses.field()
    )

    ObjectIdentifier = field("ObjectIdentifier")
    LinkName = field("LinkName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ObjectIdentifierAndLinkNameTupleTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectIdentifierAndLinkNameTupleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchListObjectPoliciesResponse:
    boto3_raw_data: "type_defs.BatchListObjectPoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    AttachedPolicyIds = field("AttachedPolicyIds")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchListObjectPoliciesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchListObjectPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchListPolicyAttachmentsResponse:
    boto3_raw_data: "type_defs.BatchListPolicyAttachmentsResponseTypeDef" = (
        dataclasses.field()
    )

    ObjectIdentifiers = field("ObjectIdentifiers")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchListPolicyAttachmentsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchListPolicyAttachmentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchReadException:
    boto3_raw_data: "type_defs.BatchReadExceptionTypeDef" = dataclasses.field()

    Type = field("Type")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchReadExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchReadExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateObjectAttributesResponse:
    boto3_raw_data: "type_defs.BatchUpdateObjectAttributesResponseTypeDef" = (
        dataclasses.field()
    )

    ObjectIdentifier = field("ObjectIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchUpdateObjectAttributesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateObjectAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDirectoryRequest:
    boto3_raw_data: "type_defs.CreateDirectoryRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    SchemaArn = field("SchemaArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDirectoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDirectoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSchemaRequest:
    boto3_raw_data: "type_defs.CreateSchemaRequestTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSchemaRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSchemaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDirectoryRequest:
    boto3_raw_data: "type_defs.DeleteDirectoryRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDirectoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDirectoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFacetRequest:
    boto3_raw_data: "type_defs.DeleteFacetRequestTypeDef" = dataclasses.field()

    SchemaArn = field("SchemaArn")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFacetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFacetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSchemaRequest:
    boto3_raw_data: "type_defs.DeleteSchemaRequestTypeDef" = dataclasses.field()

    SchemaArn = field("SchemaArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSchemaRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSchemaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTypedLinkFacetRequest:
    boto3_raw_data: "type_defs.DeleteTypedLinkFacetRequestTypeDef" = dataclasses.field()

    SchemaArn = field("SchemaArn")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTypedLinkFacetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTypedLinkFacetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Directory:
    boto3_raw_data: "type_defs.DirectoryTypeDef" = dataclasses.field()

    Name = field("Name")
    DirectoryArn = field("DirectoryArn")
    State = field("State")
    CreationDateTime = field("CreationDateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DirectoryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DirectoryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableDirectoryRequest:
    boto3_raw_data: "type_defs.DisableDirectoryRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableDirectoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableDirectoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableDirectoryRequest:
    boto3_raw_data: "type_defs.EnableDirectoryRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnableDirectoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableDirectoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RuleOutput:
    boto3_raw_data: "type_defs.RuleOutputTypeDef" = dataclasses.field()

    Type = field("Type")
    Parameters = field("Parameters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RuleOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RuleOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FacetAttributeReference:
    boto3_raw_data: "type_defs.FacetAttributeReferenceTypeDef" = dataclasses.field()

    TargetFacetName = field("TargetFacetName")
    TargetAttributeName = field("TargetAttributeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FacetAttributeReferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FacetAttributeReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Facet:
    boto3_raw_data: "type_defs.FacetTypeDef" = dataclasses.field()

    Name = field("Name")
    ObjectType = field("ObjectType")
    FacetStyle = field("FacetStyle")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FacetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FacetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAppliedSchemaVersionRequest:
    boto3_raw_data: "type_defs.GetAppliedSchemaVersionRequestTypeDef" = (
        dataclasses.field()
    )

    SchemaArn = field("SchemaArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAppliedSchemaVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAppliedSchemaVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDirectoryRequest:
    boto3_raw_data: "type_defs.GetDirectoryRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDirectoryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDirectoryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFacetRequest:
    boto3_raw_data: "type_defs.GetFacetRequestTypeDef" = dataclasses.field()

    SchemaArn = field("SchemaArn")
    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFacetRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetFacetRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSchemaAsJsonRequest:
    boto3_raw_data: "type_defs.GetSchemaAsJsonRequestTypeDef" = dataclasses.field()

    SchemaArn = field("SchemaArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSchemaAsJsonRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSchemaAsJsonRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTypedLinkFacetInformationRequest:
    boto3_raw_data: "type_defs.GetTypedLinkFacetInformationRequestTypeDef" = (
        dataclasses.field()
    )

    SchemaArn = field("SchemaArn")
    Name = field("Name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTypedLinkFacetInformationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTypedLinkFacetInformationRequestTypeDef"]
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
class ListAppliedSchemaArnsRequest:
    boto3_raw_data: "type_defs.ListAppliedSchemaArnsRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryArn = field("DirectoryArn")
    SchemaArn = field("SchemaArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAppliedSchemaArnsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppliedSchemaArnsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDevelopmentSchemaArnsRequest:
    boto3_raw_data: "type_defs.ListDevelopmentSchemaArnsRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDevelopmentSchemaArnsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDevelopmentSchemaArnsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDirectoriesRequest:
    boto3_raw_data: "type_defs.ListDirectoriesRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    state = field("state")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDirectoriesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDirectoriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFacetAttributesRequest:
    boto3_raw_data: "type_defs.ListFacetAttributesRequestTypeDef" = dataclasses.field()

    SchemaArn = field("SchemaArn")
    Name = field("Name")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFacetAttributesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFacetAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFacetNamesRequest:
    boto3_raw_data: "type_defs.ListFacetNamesRequestTypeDef" = dataclasses.field()

    SchemaArn = field("SchemaArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFacetNamesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFacetNamesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedSchemaArnsRequest:
    boto3_raw_data: "type_defs.ListManagedSchemaArnsRequestTypeDef" = (
        dataclasses.field()
    )

    SchemaArn = field("SchemaArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListManagedSchemaArnsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedSchemaArnsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPublishedSchemaArnsRequest:
    boto3_raw_data: "type_defs.ListPublishedSchemaArnsRequestTypeDef" = (
        dataclasses.field()
    )

    SchemaArn = field("SchemaArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPublishedSchemaArnsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPublishedSchemaArnsRequestTypeDef"]
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

    ResourceArn = field("ResourceArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

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
class ListTypedLinkFacetAttributesRequest:
    boto3_raw_data: "type_defs.ListTypedLinkFacetAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    SchemaArn = field("SchemaArn")
    Name = field("Name")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTypedLinkFacetAttributesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTypedLinkFacetAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTypedLinkFacetNamesRequest:
    boto3_raw_data: "type_defs.ListTypedLinkFacetNamesRequestTypeDef" = (
        dataclasses.field()
    )

    SchemaArn = field("SchemaArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTypedLinkFacetNamesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTypedLinkFacetNamesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyAttachment:
    boto3_raw_data: "type_defs.PolicyAttachmentTypeDef" = dataclasses.field()

    PolicyId = field("PolicyId")
    ObjectIdentifier = field("ObjectIdentifier")
    PolicyType = field("PolicyType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyAttachmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyAttachmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublishSchemaRequest:
    boto3_raw_data: "type_defs.PublishSchemaRequestTypeDef" = dataclasses.field()

    DevelopmentSchemaArn = field("DevelopmentSchemaArn")
    Version = field("Version")
    MinorVersion = field("MinorVersion")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PublishSchemaRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublishSchemaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSchemaFromJsonRequest:
    boto3_raw_data: "type_defs.PutSchemaFromJsonRequestTypeDef" = dataclasses.field()

    SchemaArn = field("SchemaArn")
    Document = field("Document")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutSchemaFromJsonRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutSchemaFromJsonRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Rule:
    boto3_raw_data: "type_defs.RuleTypeDef" = dataclasses.field()

    Type = field("Type")
    Parameters = field("Parameters")

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
class UpdateSchemaRequest:
    boto3_raw_data: "type_defs.UpdateSchemaRequestTypeDef" = dataclasses.field()

    SchemaArn = field("SchemaArn")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSchemaRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSchemaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpgradeAppliedSchemaRequest:
    boto3_raw_data: "type_defs.UpgradeAppliedSchemaRequestTypeDef" = dataclasses.field()

    PublishedSchemaArn = field("PublishedSchemaArn")
    DirectoryArn = field("DirectoryArn")
    DryRun = field("DryRun")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpgradeAppliedSchemaRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpgradeAppliedSchemaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpgradePublishedSchemaRequest:
    boto3_raw_data: "type_defs.UpgradePublishedSchemaRequestTypeDef" = (
        dataclasses.field()
    )

    DevelopmentSchemaArn = field("DevelopmentSchemaArn")
    PublishedSchemaArn = field("PublishedSchemaArn")
    MinorVersion = field("MinorVersion")
    DryRun = field("DryRun")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpgradePublishedSchemaRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpgradePublishedSchemaRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachObjectRequest:
    boto3_raw_data: "type_defs.AttachObjectRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def ParentReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ParentReference"])

    @cached_property
    def ChildReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ChildReference"])

    LinkName = field("LinkName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachObjectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachObjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachPolicyRequest:
    boto3_raw_data: "type_defs.AttachPolicyRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def PolicyReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["PolicyReference"])

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachToIndexRequest:
    boto3_raw_data: "type_defs.AttachToIndexRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def IndexReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["IndexReference"])

    @cached_property
    def TargetReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["TargetReference"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachToIndexRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachToIndexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAttachObject:
    boto3_raw_data: "type_defs.BatchAttachObjectTypeDef" = dataclasses.field()

    @cached_property
    def ParentReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ParentReference"])

    @cached_property
    def ChildReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ChildReference"])

    LinkName = field("LinkName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchAttachObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchAttachObjectTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAttachPolicy:
    boto3_raw_data: "type_defs.BatchAttachPolicyTypeDef" = dataclasses.field()

    @cached_property
    def PolicyReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["PolicyReference"])

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchAttachPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchAttachPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAttachToIndex:
    boto3_raw_data: "type_defs.BatchAttachToIndexTypeDef" = dataclasses.field()

    @cached_property
    def IndexReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["IndexReference"])

    @cached_property
    def TargetReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["TargetReference"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchAttachToIndexTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchAttachToIndexTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteObject:
    boto3_raw_data: "type_defs.BatchDeleteObjectTypeDef" = dataclasses.field()

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchDeleteObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteObjectTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDetachFromIndex:
    boto3_raw_data: "type_defs.BatchDetachFromIndexTypeDef" = dataclasses.field()

    @cached_property
    def IndexReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["IndexReference"])

    @cached_property
    def TargetReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["TargetReference"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDetachFromIndexTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDetachFromIndexTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDetachObject:
    boto3_raw_data: "type_defs.BatchDetachObjectTypeDef" = dataclasses.field()

    @cached_property
    def ParentReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ParentReference"])

    LinkName = field("LinkName")
    BatchReferenceName = field("BatchReferenceName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchDetachObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDetachObjectTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDetachPolicy:
    boto3_raw_data: "type_defs.BatchDetachPolicyTypeDef" = dataclasses.field()

    @cached_property
    def PolicyReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["PolicyReference"])

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchDetachPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDetachPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetObjectInformation:
    boto3_raw_data: "type_defs.BatchGetObjectInformationTypeDef" = dataclasses.field()

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetObjectInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetObjectInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchListAttachedIndices:
    boto3_raw_data: "type_defs.BatchListAttachedIndicesTypeDef" = dataclasses.field()

    @cached_property
    def TargetReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["TargetReference"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchListAttachedIndicesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchListAttachedIndicesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchListObjectChildren:
    boto3_raw_data: "type_defs.BatchListObjectChildrenTypeDef" = dataclasses.field()

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchListObjectChildrenTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchListObjectChildrenTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchListObjectParentPaths:
    boto3_raw_data: "type_defs.BatchListObjectParentPathsTypeDef" = dataclasses.field()

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchListObjectParentPathsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchListObjectParentPathsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchListObjectParents:
    boto3_raw_data: "type_defs.BatchListObjectParentsTypeDef" = dataclasses.field()

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchListObjectParentsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchListObjectParentsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchListObjectPolicies:
    boto3_raw_data: "type_defs.BatchListObjectPoliciesTypeDef" = dataclasses.field()

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchListObjectPoliciesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchListObjectPoliciesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchListPolicyAttachments:
    boto3_raw_data: "type_defs.BatchListPolicyAttachmentsTypeDef" = dataclasses.field()

    @cached_property
    def PolicyReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["PolicyReference"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchListPolicyAttachmentsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchListPolicyAttachmentsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchLookupPolicy:
    boto3_raw_data: "type_defs.BatchLookupPolicyTypeDef" = dataclasses.field()

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchLookupPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchLookupPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteObjectRequest:
    boto3_raw_data: "type_defs.DeleteObjectRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteObjectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteObjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachFromIndexRequest:
    boto3_raw_data: "type_defs.DetachFromIndexRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def IndexReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["IndexReference"])

    @cached_property
    def TargetReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["TargetReference"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetachFromIndexRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachFromIndexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachObjectRequest:
    boto3_raw_data: "type_defs.DetachObjectRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def ParentReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ParentReference"])

    LinkName = field("LinkName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetachObjectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachObjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachPolicyRequest:
    boto3_raw_data: "type_defs.DetachPolicyRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def PolicyReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["PolicyReference"])

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetachPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetObjectInformationRequest:
    boto3_raw_data: "type_defs.GetObjectInformationRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    ConsistencyLevel = field("ConsistencyLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetObjectInformationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetObjectInformationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttachedIndicesRequest:
    boto3_raw_data: "type_defs.ListAttachedIndicesRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def TargetReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["TargetReference"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    ConsistencyLevel = field("ConsistencyLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAttachedIndicesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttachedIndicesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectChildrenRequest:
    boto3_raw_data: "type_defs.ListObjectChildrenRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    ConsistencyLevel = field("ConsistencyLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListObjectChildrenRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectChildrenRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectParentPathsRequest:
    boto3_raw_data: "type_defs.ListObjectParentPathsRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListObjectParentPathsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectParentPathsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectParentsRequest:
    boto3_raw_data: "type_defs.ListObjectParentsRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    ConsistencyLevel = field("ConsistencyLevel")
    IncludeAllLinksToEachParent = field("IncludeAllLinksToEachParent")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListObjectParentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectParentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectPoliciesRequest:
    boto3_raw_data: "type_defs.ListObjectPoliciesRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    ConsistencyLevel = field("ConsistencyLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListObjectPoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyAttachmentsRequest:
    boto3_raw_data: "type_defs.ListPolicyAttachmentsRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def PolicyReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["PolicyReference"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    ConsistencyLevel = field("ConsistencyLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPolicyAttachmentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyAttachmentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LookupPolicyRequest:
    boto3_raw_data: "type_defs.LookupPolicyRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LookupPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LookupPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetObjectAttributes:
    boto3_raw_data: "type_defs.BatchGetObjectAttributesTypeDef" = dataclasses.field()

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    @cached_property
    def SchemaFacet(self):  # pragma: no cover
        return SchemaFacet.make_one(self.boto3_raw_data["SchemaFacet"])

    AttributeNames = field("AttributeNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetObjectAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetObjectAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetObjectInformationResponse:
    boto3_raw_data: "type_defs.BatchGetObjectInformationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SchemaFacets(self):  # pragma: no cover
        return SchemaFacet.make_many(self.boto3_raw_data["SchemaFacets"])

    ObjectIdentifier = field("ObjectIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetObjectInformationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetObjectInformationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchListObjectAttributes:
    boto3_raw_data: "type_defs.BatchListObjectAttributesTypeDef" = dataclasses.field()

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def FacetFilter(self):  # pragma: no cover
        return SchemaFacet.make_one(self.boto3_raw_data["FacetFilter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchListObjectAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchListObjectAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchRemoveFacetFromObject:
    boto3_raw_data: "type_defs.BatchRemoveFacetFromObjectTypeDef" = dataclasses.field()

    @cached_property
    def SchemaFacet(self):  # pragma: no cover
        return SchemaFacet.make_one(self.boto3_raw_data["SchemaFacet"])

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchRemoveFacetFromObjectTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchRemoveFacetFromObjectTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetObjectAttributesRequest:
    boto3_raw_data: "type_defs.GetObjectAttributesRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    @cached_property
    def SchemaFacet(self):  # pragma: no cover
        return SchemaFacet.make_one(self.boto3_raw_data["SchemaFacet"])

    AttributeNames = field("AttributeNames")
    ConsistencyLevel = field("ConsistencyLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetObjectAttributesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetObjectAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectAttributesRequest:
    boto3_raw_data: "type_defs.ListObjectAttributesRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    ConsistencyLevel = field("ConsistencyLevel")

    @cached_property
    def FacetFilter(self):  # pragma: no cover
        return SchemaFacet.make_one(self.boto3_raw_data["FacetFilter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListObjectAttributesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveFacetFromObjectRequest:
    boto3_raw_data: "type_defs.RemoveFacetFromObjectRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def SchemaFacet(self):  # pragma: no cover
        return SchemaFacet.make_one(self.boto3_raw_data["SchemaFacet"])

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveFacetFromObjectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveFacetFromObjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplySchemaResponse:
    boto3_raw_data: "type_defs.ApplySchemaResponseTypeDef" = dataclasses.field()

    AppliedSchemaArn = field("AppliedSchemaArn")
    DirectoryArn = field("DirectoryArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplySchemaResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplySchemaResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachObjectResponse:
    boto3_raw_data: "type_defs.AttachObjectResponseTypeDef" = dataclasses.field()

    AttachedObjectIdentifier = field("AttachedObjectIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachObjectResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachObjectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachToIndexResponse:
    boto3_raw_data: "type_defs.AttachToIndexResponseTypeDef" = dataclasses.field()

    AttachedObjectIdentifier = field("AttachedObjectIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachToIndexResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachToIndexResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDirectoryResponse:
    boto3_raw_data: "type_defs.CreateDirectoryResponseTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")
    Name = field("Name")
    ObjectIdentifier = field("ObjectIdentifier")
    AppliedSchemaArn = field("AppliedSchemaArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDirectoryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDirectoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIndexResponse:
    boto3_raw_data: "type_defs.CreateIndexResponseTypeDef" = dataclasses.field()

    ObjectIdentifier = field("ObjectIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIndexResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIndexResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateObjectResponse:
    boto3_raw_data: "type_defs.CreateObjectResponseTypeDef" = dataclasses.field()

    ObjectIdentifier = field("ObjectIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateObjectResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateObjectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSchemaResponse:
    boto3_raw_data: "type_defs.CreateSchemaResponseTypeDef" = dataclasses.field()

    SchemaArn = field("SchemaArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSchemaResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSchemaResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDirectoryResponse:
    boto3_raw_data: "type_defs.DeleteDirectoryResponseTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDirectoryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDirectoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSchemaResponse:
    boto3_raw_data: "type_defs.DeleteSchemaResponseTypeDef" = dataclasses.field()

    SchemaArn = field("SchemaArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSchemaResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSchemaResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachFromIndexResponse:
    boto3_raw_data: "type_defs.DetachFromIndexResponseTypeDef" = dataclasses.field()

    DetachedObjectIdentifier = field("DetachedObjectIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetachFromIndexResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachFromIndexResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachObjectResponse:
    boto3_raw_data: "type_defs.DetachObjectResponseTypeDef" = dataclasses.field()

    DetachedObjectIdentifier = field("DetachedObjectIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetachObjectResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachObjectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisableDirectoryResponse:
    boto3_raw_data: "type_defs.DisableDirectoryResponseTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisableDirectoryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisableDirectoryResponseTypeDef"]
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
class EnableDirectoryResponse:
    boto3_raw_data: "type_defs.EnableDirectoryResponseTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnableDirectoryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableDirectoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAppliedSchemaVersionResponse:
    boto3_raw_data: "type_defs.GetAppliedSchemaVersionResponseTypeDef" = (
        dataclasses.field()
    )

    AppliedSchemaArn = field("AppliedSchemaArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAppliedSchemaVersionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAppliedSchemaVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetObjectInformationResponse:
    boto3_raw_data: "type_defs.GetObjectInformationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def SchemaFacets(self):  # pragma: no cover
        return SchemaFacet.make_many(self.boto3_raw_data["SchemaFacets"])

    ObjectIdentifier = field("ObjectIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetObjectInformationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetObjectInformationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSchemaAsJsonResponse:
    boto3_raw_data: "type_defs.GetSchemaAsJsonResponseTypeDef" = dataclasses.field()

    Name = field("Name")
    Document = field("Document")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSchemaAsJsonResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSchemaAsJsonResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTypedLinkFacetInformationResponse:
    boto3_raw_data: "type_defs.GetTypedLinkFacetInformationResponseTypeDef" = (
        dataclasses.field()
    )

    IdentityAttributeOrder = field("IdentityAttributeOrder")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTypedLinkFacetInformationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTypedLinkFacetInformationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppliedSchemaArnsResponse:
    boto3_raw_data: "type_defs.ListAppliedSchemaArnsResponseTypeDef" = (
        dataclasses.field()
    )

    SchemaArns = field("SchemaArns")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAppliedSchemaArnsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppliedSchemaArnsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDevelopmentSchemaArnsResponse:
    boto3_raw_data: "type_defs.ListDevelopmentSchemaArnsResponseTypeDef" = (
        dataclasses.field()
    )

    SchemaArns = field("SchemaArns")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDevelopmentSchemaArnsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDevelopmentSchemaArnsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFacetNamesResponse:
    boto3_raw_data: "type_defs.ListFacetNamesResponseTypeDef" = dataclasses.field()

    FacetNames = field("FacetNames")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFacetNamesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFacetNamesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedSchemaArnsResponse:
    boto3_raw_data: "type_defs.ListManagedSchemaArnsResponseTypeDef" = (
        dataclasses.field()
    )

    SchemaArns = field("SchemaArns")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListManagedSchemaArnsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedSchemaArnsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectChildrenResponse:
    boto3_raw_data: "type_defs.ListObjectChildrenResponseTypeDef" = dataclasses.field()

    Children = field("Children")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListObjectChildrenResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectChildrenResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectPoliciesResponse:
    boto3_raw_data: "type_defs.ListObjectPoliciesResponseTypeDef" = dataclasses.field()

    AttachedPolicyIds = field("AttachedPolicyIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListObjectPoliciesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyAttachmentsResponse:
    boto3_raw_data: "type_defs.ListPolicyAttachmentsResponseTypeDef" = (
        dataclasses.field()
    )

    ObjectIdentifiers = field("ObjectIdentifiers")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPolicyAttachmentsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyAttachmentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPublishedSchemaArnsResponse:
    boto3_raw_data: "type_defs.ListPublishedSchemaArnsResponseTypeDef" = (
        dataclasses.field()
    )

    SchemaArns = field("SchemaArns")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPublishedSchemaArnsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPublishedSchemaArnsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTypedLinkFacetNamesResponse:
    boto3_raw_data: "type_defs.ListTypedLinkFacetNamesResponseTypeDef" = (
        dataclasses.field()
    )

    FacetNames = field("FacetNames")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTypedLinkFacetNamesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTypedLinkFacetNamesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublishSchemaResponse:
    boto3_raw_data: "type_defs.PublishSchemaResponseTypeDef" = dataclasses.field()

    PublishedSchemaArn = field("PublishedSchemaArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PublishSchemaResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublishSchemaResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSchemaFromJsonResponse:
    boto3_raw_data: "type_defs.PutSchemaFromJsonResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutSchemaFromJsonResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutSchemaFromJsonResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateObjectAttributesResponse:
    boto3_raw_data: "type_defs.UpdateObjectAttributesResponseTypeDef" = (
        dataclasses.field()
    )

    ObjectIdentifier = field("ObjectIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateObjectAttributesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateObjectAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSchemaResponse:
    boto3_raw_data: "type_defs.UpdateSchemaResponseTypeDef" = dataclasses.field()

    SchemaArn = field("SchemaArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSchemaResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSchemaResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpgradeAppliedSchemaResponse:
    boto3_raw_data: "type_defs.UpgradeAppliedSchemaResponseTypeDef" = (
        dataclasses.field()
    )

    UpgradedSchemaArn = field("UpgradedSchemaArn")
    DirectoryArn = field("DirectoryArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpgradeAppliedSchemaResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpgradeAppliedSchemaResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpgradePublishedSchemaResponse:
    boto3_raw_data: "type_defs.UpgradePublishedSchemaResponseTypeDef" = (
        dataclasses.field()
    )

    UpgradedSchemaArn = field("UpgradedSchemaArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpgradePublishedSchemaResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpgradePublishedSchemaResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateIndex:
    boto3_raw_data: "type_defs.BatchCreateIndexTypeDef" = dataclasses.field()

    @cached_property
    def OrderedIndexedAttributeList(self):  # pragma: no cover
        return AttributeKey.make_many(
            self.boto3_raw_data["OrderedIndexedAttributeList"]
        )

    IsUnique = field("IsUnique")

    @cached_property
    def ParentReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ParentReference"])

    LinkName = field("LinkName")
    BatchReferenceName = field("BatchReferenceName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchCreateIndexTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateIndexTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIndexRequest:
    boto3_raw_data: "type_defs.CreateIndexRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def OrderedIndexedAttributeList(self):  # pragma: no cover
        return AttributeKey.make_many(
            self.boto3_raw_data["OrderedIndexedAttributeList"]
        )

    IsUnique = field("IsUnique")

    @cached_property
    def ParentReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ParentReference"])

    LinkName = field("LinkName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIndexRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIndexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeKeyAndValueOutput:
    boto3_raw_data: "type_defs.AttributeKeyAndValueOutputTypeDef" = dataclasses.field()

    @cached_property
    def Key(self):  # pragma: no cover
        return AttributeKey.make_one(self.boto3_raw_data["Key"])

    @cached_property
    def Value(self):  # pragma: no cover
        return TypedAttributeValueOutput.make_one(self.boto3_raw_data["Value"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeKeyAndValueOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeKeyAndValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeNameAndValueOutput:
    boto3_raw_data: "type_defs.AttributeNameAndValueOutputTypeDef" = dataclasses.field()

    AttributeName = field("AttributeName")

    @cached_property
    def Value(self):  # pragma: no cover
        return TypedAttributeValueOutput.make_one(self.boto3_raw_data["Value"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeNameAndValueOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeNameAndValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchListObjectParentPathsResponse:
    boto3_raw_data: "type_defs.BatchListObjectParentPathsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PathToObjectIdentifiersList(self):  # pragma: no cover
        return PathToObjectIdentifiers.make_many(
            self.boto3_raw_data["PathToObjectIdentifiersList"]
        )

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchListObjectParentPathsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchListObjectParentPathsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectParentPathsResponse:
    boto3_raw_data: "type_defs.ListObjectParentPathsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PathToObjectIdentifiersList(self):  # pragma: no cover
        return PathToObjectIdentifiers.make_many(
            self.boto3_raw_data["PathToObjectIdentifiersList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListObjectParentPathsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectParentPathsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchListObjectParentsResponse:
    boto3_raw_data: "type_defs.BatchListObjectParentsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ParentLinks(self):  # pragma: no cover
        return ObjectIdentifierAndLinkNameTuple.make_many(
            self.boto3_raw_data["ParentLinks"]
        )

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchListObjectParentsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchListObjectParentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectParentsResponse:
    boto3_raw_data: "type_defs.ListObjectParentsResponseTypeDef" = dataclasses.field()

    Parents = field("Parents")

    @cached_property
    def ParentLinks(self):  # pragma: no cover
        return ObjectIdentifierAndLinkNameTuple.make_many(
            self.boto3_raw_data["ParentLinks"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListObjectParentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectParentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDirectoryResponse:
    boto3_raw_data: "type_defs.GetDirectoryResponseTypeDef" = dataclasses.field()

    @cached_property
    def Directory(self):  # pragma: no cover
        return Directory.make_one(self.boto3_raw_data["Directory"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDirectoryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDirectoryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDirectoriesResponse:
    boto3_raw_data: "type_defs.ListDirectoriesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Directories(self):  # pragma: no cover
        return Directory.make_many(self.boto3_raw_data["Directories"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDirectoriesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDirectoriesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FacetAttributeDefinitionOutput:
    boto3_raw_data: "type_defs.FacetAttributeDefinitionOutputTypeDef" = (
        dataclasses.field()
    )

    Type = field("Type")

    @cached_property
    def DefaultValue(self):  # pragma: no cover
        return TypedAttributeValueOutput.make_one(self.boto3_raw_data["DefaultValue"])

    IsImmutable = field("IsImmutable")
    Rules = field("Rules")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FacetAttributeDefinitionOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FacetAttributeDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TypedLinkAttributeDefinitionOutput:
    boto3_raw_data: "type_defs.TypedLinkAttributeDefinitionOutputTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Type = field("Type")
    RequiredBehavior = field("RequiredBehavior")

    @cached_property
    def DefaultValue(self):  # pragma: no cover
        return TypedAttributeValueOutput.make_one(self.boto3_raw_data["DefaultValue"])

    IsImmutable = field("IsImmutable")
    Rules = field("Rules")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TypedLinkAttributeDefinitionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TypedLinkAttributeDefinitionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFacetResponse:
    boto3_raw_data: "type_defs.GetFacetResponseTypeDef" = dataclasses.field()

    @cached_property
    def Facet(self):  # pragma: no cover
        return Facet.make_one(self.boto3_raw_data["Facet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFacetResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFacetResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAppliedSchemaArnsRequestPaginate:
    boto3_raw_data: "type_defs.ListAppliedSchemaArnsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DirectoryArn = field("DirectoryArn")
    SchemaArn = field("SchemaArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAppliedSchemaArnsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAppliedSchemaArnsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttachedIndicesRequestPaginate:
    boto3_raw_data: "type_defs.ListAttachedIndicesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def TargetReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["TargetReference"])

    ConsistencyLevel = field("ConsistencyLevel")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAttachedIndicesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttachedIndicesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDevelopmentSchemaArnsRequestPaginate:
    boto3_raw_data: "type_defs.ListDevelopmentSchemaArnsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDevelopmentSchemaArnsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDevelopmentSchemaArnsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDirectoriesRequestPaginate:
    boto3_raw_data: "type_defs.ListDirectoriesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    state = field("state")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDirectoriesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDirectoriesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFacetAttributesRequestPaginate:
    boto3_raw_data: "type_defs.ListFacetAttributesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    SchemaArn = field("SchemaArn")
    Name = field("Name")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFacetAttributesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFacetAttributesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFacetNamesRequestPaginate:
    boto3_raw_data: "type_defs.ListFacetNamesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    SchemaArn = field("SchemaArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListFacetNamesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFacetNamesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedSchemaArnsRequestPaginate:
    boto3_raw_data: "type_defs.ListManagedSchemaArnsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    SchemaArn = field("SchemaArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListManagedSchemaArnsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedSchemaArnsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectAttributesRequestPaginate:
    boto3_raw_data: "type_defs.ListObjectAttributesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    ConsistencyLevel = field("ConsistencyLevel")

    @cached_property
    def FacetFilter(self):  # pragma: no cover
        return SchemaFacet.make_one(self.boto3_raw_data["FacetFilter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListObjectAttributesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectAttributesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectParentPathsRequestPaginate:
    boto3_raw_data: "type_defs.ListObjectParentPathsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListObjectParentPathsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectParentPathsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectPoliciesRequestPaginate:
    boto3_raw_data: "type_defs.ListObjectPoliciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    ConsistencyLevel = field("ConsistencyLevel")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListObjectPoliciesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectPoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPolicyAttachmentsRequestPaginate:
    boto3_raw_data: "type_defs.ListPolicyAttachmentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def PolicyReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["PolicyReference"])

    ConsistencyLevel = field("ConsistencyLevel")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPolicyAttachmentsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPolicyAttachmentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPublishedSchemaArnsRequestPaginate:
    boto3_raw_data: "type_defs.ListPublishedSchemaArnsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    SchemaArn = field("SchemaArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPublishedSchemaArnsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPublishedSchemaArnsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequestPaginate:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTagsForResourceRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTypedLinkFacetAttributesRequestPaginate:
    boto3_raw_data: "type_defs.ListTypedLinkFacetAttributesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    SchemaArn = field("SchemaArn")
    Name = field("Name")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTypedLinkFacetAttributesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTypedLinkFacetAttributesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTypedLinkFacetNamesRequestPaginate:
    boto3_raw_data: "type_defs.ListTypedLinkFacetNamesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    SchemaArn = field("SchemaArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTypedLinkFacetNamesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTypedLinkFacetNamesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LookupPolicyRequestPaginate:
    boto3_raw_data: "type_defs.LookupPolicyRequestPaginateTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LookupPolicyRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LookupPolicyRequestPaginateTypeDef"]
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
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

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
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

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
class PolicyToPath:
    boto3_raw_data: "type_defs.PolicyToPathTypeDef" = dataclasses.field()

    Path = field("Path")

    @cached_property
    def Policies(self):  # pragma: no cover
        return PolicyAttachment.make_many(self.boto3_raw_data["Policies"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyToPathTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyToPathTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TypedAttributeValue:
    boto3_raw_data: "type_defs.TypedAttributeValueTypeDef" = dataclasses.field()

    StringValue = field("StringValue")
    BinaryValue = field("BinaryValue")
    BooleanValue = field("BooleanValue")
    NumberValue = field("NumberValue")
    DatetimeValue = field("DatetimeValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TypedAttributeValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TypedAttributeValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetLinkAttributesResponse:
    boto3_raw_data: "type_defs.BatchGetLinkAttributesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Attributes(self):  # pragma: no cover
        return AttributeKeyAndValueOutput.make_many(self.boto3_raw_data["Attributes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetLinkAttributesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetLinkAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetObjectAttributesResponse:
    boto3_raw_data: "type_defs.BatchGetObjectAttributesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Attributes(self):  # pragma: no cover
        return AttributeKeyAndValueOutput.make_many(self.boto3_raw_data["Attributes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetObjectAttributesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetObjectAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchListObjectAttributesResponse:
    boto3_raw_data: "type_defs.BatchListObjectAttributesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Attributes(self):  # pragma: no cover
        return AttributeKeyAndValueOutput.make_many(self.boto3_raw_data["Attributes"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchListObjectAttributesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchListObjectAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLinkAttributesResponse:
    boto3_raw_data: "type_defs.GetLinkAttributesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Attributes(self):  # pragma: no cover
        return AttributeKeyAndValueOutput.make_many(self.boto3_raw_data["Attributes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLinkAttributesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLinkAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetObjectAttributesResponse:
    boto3_raw_data: "type_defs.GetObjectAttributesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Attributes(self):  # pragma: no cover
        return AttributeKeyAndValueOutput.make_many(self.boto3_raw_data["Attributes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetObjectAttributesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetObjectAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IndexAttachment:
    boto3_raw_data: "type_defs.IndexAttachmentTypeDef" = dataclasses.field()

    @cached_property
    def IndexedAttributes(self):  # pragma: no cover
        return AttributeKeyAndValueOutput.make_many(
            self.boto3_raw_data["IndexedAttributes"]
        )

    ObjectIdentifier = field("ObjectIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IndexAttachmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IndexAttachmentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectAttributesResponse:
    boto3_raw_data: "type_defs.ListObjectAttributesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Attributes(self):  # pragma: no cover
        return AttributeKeyAndValueOutput.make_many(self.boto3_raw_data["Attributes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListObjectAttributesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TypedLinkSpecifierOutput:
    boto3_raw_data: "type_defs.TypedLinkSpecifierOutputTypeDef" = dataclasses.field()

    @cached_property
    def TypedLinkFacet(self):  # pragma: no cover
        return TypedLinkSchemaAndFacetName.make_one(
            self.boto3_raw_data["TypedLinkFacet"]
        )

    @cached_property
    def SourceObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["SourceObjectReference"])

    @cached_property
    def TargetObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["TargetObjectReference"])

    @cached_property
    def IdentityAttributeValues(self):  # pragma: no cover
        return AttributeNameAndValueOutput.make_many(
            self.boto3_raw_data["IdentityAttributeValues"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TypedLinkSpecifierOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TypedLinkSpecifierOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FacetAttributeOutput:
    boto3_raw_data: "type_defs.FacetAttributeOutputTypeDef" = dataclasses.field()

    Name = field("Name")

    @cached_property
    def AttributeDefinition(self):  # pragma: no cover
        return FacetAttributeDefinitionOutput.make_one(
            self.boto3_raw_data["AttributeDefinition"]
        )

    @cached_property
    def AttributeReference(self):  # pragma: no cover
        return FacetAttributeReference.make_one(
            self.boto3_raw_data["AttributeReference"]
        )

    RequiredBehavior = field("RequiredBehavior")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FacetAttributeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FacetAttributeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTypedLinkFacetAttributesResponse:
    boto3_raw_data: "type_defs.ListTypedLinkFacetAttributesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Attributes(self):  # pragma: no cover
        return TypedLinkAttributeDefinitionOutput.make_many(
            self.boto3_raw_data["Attributes"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTypedLinkFacetAttributesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTypedLinkFacetAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchLookupPolicyResponse:
    boto3_raw_data: "type_defs.BatchLookupPolicyResponseTypeDef" = dataclasses.field()

    @cached_property
    def PolicyToPathList(self):  # pragma: no cover
        return PolicyToPath.make_many(self.boto3_raw_data["PolicyToPathList"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchLookupPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchLookupPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LookupPolicyResponse:
    boto3_raw_data: "type_defs.LookupPolicyResponseTypeDef" = dataclasses.field()

    @cached_property
    def PolicyToPathList(self):  # pragma: no cover
        return PolicyToPath.make_many(self.boto3_raw_data["PolicyToPathList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LookupPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LookupPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchListAttachedIndicesResponse:
    boto3_raw_data: "type_defs.BatchListAttachedIndicesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def IndexAttachments(self):  # pragma: no cover
        return IndexAttachment.make_many(self.boto3_raw_data["IndexAttachments"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchListAttachedIndicesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchListAttachedIndicesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchListIndexResponse:
    boto3_raw_data: "type_defs.BatchListIndexResponseTypeDef" = dataclasses.field()

    @cached_property
    def IndexAttachments(self):  # pragma: no cover
        return IndexAttachment.make_many(self.boto3_raw_data["IndexAttachments"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchListIndexResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchListIndexResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAttachedIndicesResponse:
    boto3_raw_data: "type_defs.ListAttachedIndicesResponseTypeDef" = dataclasses.field()

    @cached_property
    def IndexAttachments(self):  # pragma: no cover
        return IndexAttachment.make_many(self.boto3_raw_data["IndexAttachments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAttachedIndicesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAttachedIndicesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIndexResponse:
    boto3_raw_data: "type_defs.ListIndexResponseTypeDef" = dataclasses.field()

    @cached_property
    def IndexAttachments(self):  # pragma: no cover
        return IndexAttachment.make_many(self.boto3_raw_data["IndexAttachments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListIndexResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIndexResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachTypedLinkResponse:
    boto3_raw_data: "type_defs.AttachTypedLinkResponseTypeDef" = dataclasses.field()

    @cached_property
    def TypedLinkSpecifier(self):  # pragma: no cover
        return TypedLinkSpecifierOutput.make_one(
            self.boto3_raw_data["TypedLinkSpecifier"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachTypedLinkResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachTypedLinkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAttachTypedLinkResponse:
    boto3_raw_data: "type_defs.BatchAttachTypedLinkResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TypedLinkSpecifier(self):  # pragma: no cover
        return TypedLinkSpecifierOutput.make_one(
            self.boto3_raw_data["TypedLinkSpecifier"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchAttachTypedLinkResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchAttachTypedLinkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchListIncomingTypedLinksResponse:
    boto3_raw_data: "type_defs.BatchListIncomingTypedLinksResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LinkSpecifiers(self):  # pragma: no cover
        return TypedLinkSpecifierOutput.make_many(self.boto3_raw_data["LinkSpecifiers"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchListIncomingTypedLinksResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchListIncomingTypedLinksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchListOutgoingTypedLinksResponse:
    boto3_raw_data: "type_defs.BatchListOutgoingTypedLinksResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TypedLinkSpecifiers(self):  # pragma: no cover
        return TypedLinkSpecifierOutput.make_many(
            self.boto3_raw_data["TypedLinkSpecifiers"]
        )

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchListOutgoingTypedLinksResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchListOutgoingTypedLinksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIncomingTypedLinksResponse:
    boto3_raw_data: "type_defs.ListIncomingTypedLinksResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LinkSpecifiers(self):  # pragma: no cover
        return TypedLinkSpecifierOutput.make_many(self.boto3_raw_data["LinkSpecifiers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListIncomingTypedLinksResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIncomingTypedLinksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOutgoingTypedLinksResponse:
    boto3_raw_data: "type_defs.ListOutgoingTypedLinksResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TypedLinkSpecifiers(self):  # pragma: no cover
        return TypedLinkSpecifierOutput.make_many(
            self.boto3_raw_data["TypedLinkSpecifiers"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListOutgoingTypedLinksResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOutgoingTypedLinksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFacetAttributesResponse:
    boto3_raw_data: "type_defs.ListFacetAttributesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Attributes(self):  # pragma: no cover
        return FacetAttributeOutput.make_many(self.boto3_raw_data["Attributes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFacetAttributesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFacetAttributesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeKeyAndValue:
    boto3_raw_data: "type_defs.AttributeKeyAndValueTypeDef" = dataclasses.field()

    @cached_property
    def Key(self):  # pragma: no cover
        return AttributeKey.make_one(self.boto3_raw_data["Key"])

    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeKeyAndValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeKeyAndValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttributeNameAndValue:
    boto3_raw_data: "type_defs.AttributeNameAndValueTypeDef" = dataclasses.field()

    AttributeName = field("AttributeName")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttributeNameAndValueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttributeNameAndValueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FacetAttributeDefinition:
    boto3_raw_data: "type_defs.FacetAttributeDefinitionTypeDef" = dataclasses.field()

    Type = field("Type")
    DefaultValue = field("DefaultValue")
    IsImmutable = field("IsImmutable")
    Rules = field("Rules")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FacetAttributeDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FacetAttributeDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LinkAttributeAction:
    boto3_raw_data: "type_defs.LinkAttributeActionTypeDef" = dataclasses.field()

    AttributeActionType = field("AttributeActionType")
    AttributeUpdateValue = field("AttributeUpdateValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LinkAttributeActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LinkAttributeActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectAttributeAction:
    boto3_raw_data: "type_defs.ObjectAttributeActionTypeDef" = dataclasses.field()

    ObjectAttributeActionType = field("ObjectAttributeActionType")
    ObjectAttributeUpdateValue = field("ObjectAttributeUpdateValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ObjectAttributeActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectAttributeActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TypedAttributeValueRange:
    boto3_raw_data: "type_defs.TypedAttributeValueRangeTypeDef" = dataclasses.field()

    StartMode = field("StartMode")
    EndMode = field("EndMode")
    StartValue = field("StartValue")
    EndValue = field("EndValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TypedAttributeValueRangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TypedAttributeValueRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TypedLinkAttributeDefinition:
    boto3_raw_data: "type_defs.TypedLinkAttributeDefinitionTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    Type = field("Type")
    RequiredBehavior = field("RequiredBehavior")
    DefaultValue = field("DefaultValue")
    IsImmutable = field("IsImmutable")
    Rules = field("Rules")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TypedLinkAttributeDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TypedLinkAttributeDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchWriteOperationResponse:
    boto3_raw_data: "type_defs.BatchWriteOperationResponseTypeDef" = dataclasses.field()

    @cached_property
    def CreateObject(self):  # pragma: no cover
        return BatchCreateObjectResponse.make_one(self.boto3_raw_data["CreateObject"])

    @cached_property
    def AttachObject(self):  # pragma: no cover
        return BatchAttachObjectResponse.make_one(self.boto3_raw_data["AttachObject"])

    @cached_property
    def DetachObject(self):  # pragma: no cover
        return BatchDetachObjectResponse.make_one(self.boto3_raw_data["DetachObject"])

    @cached_property
    def UpdateObjectAttributes(self):  # pragma: no cover
        return BatchUpdateObjectAttributesResponse.make_one(
            self.boto3_raw_data["UpdateObjectAttributes"]
        )

    DeleteObject = field("DeleteObject")
    AddFacetToObject = field("AddFacetToObject")
    RemoveFacetFromObject = field("RemoveFacetFromObject")
    AttachPolicy = field("AttachPolicy")
    DetachPolicy = field("DetachPolicy")

    @cached_property
    def CreateIndex(self):  # pragma: no cover
        return BatchCreateIndexResponse.make_one(self.boto3_raw_data["CreateIndex"])

    @cached_property
    def AttachToIndex(self):  # pragma: no cover
        return BatchAttachToIndexResponse.make_one(self.boto3_raw_data["AttachToIndex"])

    @cached_property
    def DetachFromIndex(self):  # pragma: no cover
        return BatchDetachFromIndexResponse.make_one(
            self.boto3_raw_data["DetachFromIndex"]
        )

    @cached_property
    def AttachTypedLink(self):  # pragma: no cover
        return BatchAttachTypedLinkResponse.make_one(
            self.boto3_raw_data["AttachTypedLink"]
        )

    DetachTypedLink = field("DetachTypedLink")
    UpdateLinkAttributes = field("UpdateLinkAttributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchWriteOperationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchWriteOperationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchReadSuccessfulResponse:
    boto3_raw_data: "type_defs.BatchReadSuccessfulResponseTypeDef" = dataclasses.field()

    @cached_property
    def ListObjectAttributes(self):  # pragma: no cover
        return BatchListObjectAttributesResponse.make_one(
            self.boto3_raw_data["ListObjectAttributes"]
        )

    @cached_property
    def ListObjectChildren(self):  # pragma: no cover
        return BatchListObjectChildrenResponse.make_one(
            self.boto3_raw_data["ListObjectChildren"]
        )

    @cached_property
    def GetObjectInformation(self):  # pragma: no cover
        return BatchGetObjectInformationResponse.make_one(
            self.boto3_raw_data["GetObjectInformation"]
        )

    @cached_property
    def GetObjectAttributes(self):  # pragma: no cover
        return BatchGetObjectAttributesResponse.make_one(
            self.boto3_raw_data["GetObjectAttributes"]
        )

    @cached_property
    def ListAttachedIndices(self):  # pragma: no cover
        return BatchListAttachedIndicesResponse.make_one(
            self.boto3_raw_data["ListAttachedIndices"]
        )

    @cached_property
    def ListObjectParentPaths(self):  # pragma: no cover
        return BatchListObjectParentPathsResponse.make_one(
            self.boto3_raw_data["ListObjectParentPaths"]
        )

    @cached_property
    def ListObjectPolicies(self):  # pragma: no cover
        return BatchListObjectPoliciesResponse.make_one(
            self.boto3_raw_data["ListObjectPolicies"]
        )

    @cached_property
    def ListPolicyAttachments(self):  # pragma: no cover
        return BatchListPolicyAttachmentsResponse.make_one(
            self.boto3_raw_data["ListPolicyAttachments"]
        )

    @cached_property
    def LookupPolicy(self):  # pragma: no cover
        return BatchLookupPolicyResponse.make_one(self.boto3_raw_data["LookupPolicy"])

    @cached_property
    def ListIndex(self):  # pragma: no cover
        return BatchListIndexResponse.make_one(self.boto3_raw_data["ListIndex"])

    @cached_property
    def ListOutgoingTypedLinks(self):  # pragma: no cover
        return BatchListOutgoingTypedLinksResponse.make_one(
            self.boto3_raw_data["ListOutgoingTypedLinks"]
        )

    @cached_property
    def ListIncomingTypedLinks(self):  # pragma: no cover
        return BatchListIncomingTypedLinksResponse.make_one(
            self.boto3_raw_data["ListIncomingTypedLinks"]
        )

    @cached_property
    def GetLinkAttributes(self):  # pragma: no cover
        return BatchGetLinkAttributesResponse.make_one(
            self.boto3_raw_data["GetLinkAttributes"]
        )

    @cached_property
    def ListObjectParents(self):  # pragma: no cover
        return BatchListObjectParentsResponse.make_one(
            self.boto3_raw_data["ListObjectParents"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchReadSuccessfulResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchReadSuccessfulResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateObject:
    boto3_raw_data: "type_defs.BatchCreateObjectTypeDef" = dataclasses.field()

    @cached_property
    def SchemaFacet(self):  # pragma: no cover
        return SchemaFacet.make_many(self.boto3_raw_data["SchemaFacet"])

    @cached_property
    def ObjectAttributeList(self):  # pragma: no cover
        return AttributeKeyAndValue.make_many(
            self.boto3_raw_data["ObjectAttributeList"]
        )

    @cached_property
    def ParentReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ParentReference"])

    LinkName = field("LinkName")
    BatchReferenceName = field("BatchReferenceName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchCreateObjectTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateObjectTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LinkAttributeUpdate:
    boto3_raw_data: "type_defs.LinkAttributeUpdateTypeDef" = dataclasses.field()

    @cached_property
    def AttributeKey(self):  # pragma: no cover
        return AttributeKey.make_one(self.boto3_raw_data["AttributeKey"])

    @cached_property
    def AttributeAction(self):  # pragma: no cover
        return LinkAttributeAction.make_one(self.boto3_raw_data["AttributeAction"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LinkAttributeUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LinkAttributeUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectAttributeUpdate:
    boto3_raw_data: "type_defs.ObjectAttributeUpdateTypeDef" = dataclasses.field()

    @cached_property
    def ObjectAttributeKey(self):  # pragma: no cover
        return AttributeKey.make_one(self.boto3_raw_data["ObjectAttributeKey"])

    @cached_property
    def ObjectAttributeAction(self):  # pragma: no cover
        return ObjectAttributeAction.make_one(
            self.boto3_raw_data["ObjectAttributeAction"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ObjectAttributeUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectAttributeUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectAttributeRange:
    boto3_raw_data: "type_defs.ObjectAttributeRangeTypeDef" = dataclasses.field()

    @cached_property
    def AttributeKey(self):  # pragma: no cover
        return AttributeKey.make_one(self.boto3_raw_data["AttributeKey"])

    @cached_property
    def Range(self):  # pragma: no cover
        return TypedAttributeValueRange.make_one(self.boto3_raw_data["Range"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ObjectAttributeRangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectAttributeRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TypedLinkAttributeRange:
    boto3_raw_data: "type_defs.TypedLinkAttributeRangeTypeDef" = dataclasses.field()

    @cached_property
    def Range(self):  # pragma: no cover
        return TypedAttributeValueRange.make_one(self.boto3_raw_data["Range"])

    AttributeName = field("AttributeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TypedLinkAttributeRangeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TypedLinkAttributeRangeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchWriteResponse:
    boto3_raw_data: "type_defs.BatchWriteResponseTypeDef" = dataclasses.field()

    @cached_property
    def Responses(self):  # pragma: no cover
        return BatchWriteOperationResponse.make_many(self.boto3_raw_data["Responses"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchWriteResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchWriteResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchReadOperationResponse:
    boto3_raw_data: "type_defs.BatchReadOperationResponseTypeDef" = dataclasses.field()

    @cached_property
    def SuccessfulResponse(self):  # pragma: no cover
        return BatchReadSuccessfulResponse.make_one(
            self.boto3_raw_data["SuccessfulResponse"]
        )

    @cached_property
    def ExceptionResponse(self):  # pragma: no cover
        return BatchReadException.make_one(self.boto3_raw_data["ExceptionResponse"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchReadOperationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchReadOperationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddFacetToObjectRequest:
    boto3_raw_data: "type_defs.AddFacetToObjectRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def SchemaFacet(self):  # pragma: no cover
        return SchemaFacet.make_one(self.boto3_raw_data["SchemaFacet"])

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    ObjectAttributeList = field("ObjectAttributeList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddFacetToObjectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddFacetToObjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAddFacetToObject:
    boto3_raw_data: "type_defs.BatchAddFacetToObjectTypeDef" = dataclasses.field()

    @cached_property
    def SchemaFacet(self):  # pragma: no cover
        return SchemaFacet.make_one(self.boto3_raw_data["SchemaFacet"])

    ObjectAttributeList = field("ObjectAttributeList")

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchAddFacetToObjectTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchAddFacetToObjectTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateObjectRequest:
    boto3_raw_data: "type_defs.CreateObjectRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def SchemaFacets(self):  # pragma: no cover
        return SchemaFacet.make_many(self.boto3_raw_data["SchemaFacets"])

    ObjectAttributeList = field("ObjectAttributeList")

    @cached_property
    def ParentReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ParentReference"])

    LinkName = field("LinkName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateObjectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateObjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachTypedLinkRequest:
    boto3_raw_data: "type_defs.AttachTypedLinkRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def SourceObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["SourceObjectReference"])

    @cached_property
    def TargetObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["TargetObjectReference"])

    @cached_property
    def TypedLinkFacet(self):  # pragma: no cover
        return TypedLinkSchemaAndFacetName.make_one(
            self.boto3_raw_data["TypedLinkFacet"]
        )

    Attributes = field("Attributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AttachTypedLinkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachTypedLinkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAttachTypedLink:
    boto3_raw_data: "type_defs.BatchAttachTypedLinkTypeDef" = dataclasses.field()

    @cached_property
    def SourceObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["SourceObjectReference"])

    @cached_property
    def TargetObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["TargetObjectReference"])

    @cached_property
    def TypedLinkFacet(self):  # pragma: no cover
        return TypedLinkSchemaAndFacetName.make_one(
            self.boto3_raw_data["TypedLinkFacet"]
        )

    Attributes = field("Attributes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchAttachTypedLinkTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchAttachTypedLinkTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TypedLinkSpecifier:
    boto3_raw_data: "type_defs.TypedLinkSpecifierTypeDef" = dataclasses.field()

    @cached_property
    def TypedLinkFacet(self):  # pragma: no cover
        return TypedLinkSchemaAndFacetName.make_one(
            self.boto3_raw_data["TypedLinkFacet"]
        )

    @cached_property
    def SourceObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["SourceObjectReference"])

    @cached_property
    def TargetObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["TargetObjectReference"])

    IdentityAttributeValues = field("IdentityAttributeValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TypedLinkSpecifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TypedLinkSpecifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FacetAttribute:
    boto3_raw_data: "type_defs.FacetAttributeTypeDef" = dataclasses.field()

    Name = field("Name")
    AttributeDefinition = field("AttributeDefinition")

    @cached_property
    def AttributeReference(self):  # pragma: no cover
        return FacetAttributeReference.make_one(
            self.boto3_raw_data["AttributeReference"]
        )

    RequiredBehavior = field("RequiredBehavior")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FacetAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FacetAttributeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateObjectAttributes:
    boto3_raw_data: "type_defs.BatchUpdateObjectAttributesTypeDef" = dataclasses.field()

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    @cached_property
    def AttributeUpdates(self):  # pragma: no cover
        return ObjectAttributeUpdate.make_many(self.boto3_raw_data["AttributeUpdates"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchUpdateObjectAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateObjectAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateObjectAttributesRequest:
    boto3_raw_data: "type_defs.UpdateObjectAttributesRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    @cached_property
    def AttributeUpdates(self):  # pragma: no cover
        return ObjectAttributeUpdate.make_many(self.boto3_raw_data["AttributeUpdates"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateObjectAttributesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateObjectAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchListIndex:
    boto3_raw_data: "type_defs.BatchListIndexTypeDef" = dataclasses.field()

    @cached_property
    def IndexReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["IndexReference"])

    @cached_property
    def RangesOnIndexedValues(self):  # pragma: no cover
        return ObjectAttributeRange.make_many(
            self.boto3_raw_data["RangesOnIndexedValues"]
        )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchListIndexTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BatchListIndexTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIndexRequestPaginate:
    boto3_raw_data: "type_defs.ListIndexRequestPaginateTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def IndexReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["IndexReference"])

    @cached_property
    def RangesOnIndexedValues(self):  # pragma: no cover
        return ObjectAttributeRange.make_many(
            self.boto3_raw_data["RangesOnIndexedValues"]
        )

    ConsistencyLevel = field("ConsistencyLevel")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIndexRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIndexRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIndexRequest:
    boto3_raw_data: "type_defs.ListIndexRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def IndexReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["IndexReference"])

    @cached_property
    def RangesOnIndexedValues(self):  # pragma: no cover
        return ObjectAttributeRange.make_many(
            self.boto3_raw_data["RangesOnIndexedValues"]
        )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    ConsistencyLevel = field("ConsistencyLevel")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListIndexRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIndexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchListIncomingTypedLinks:
    boto3_raw_data: "type_defs.BatchListIncomingTypedLinksTypeDef" = dataclasses.field()

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    @cached_property
    def FilterAttributeRanges(self):  # pragma: no cover
        return TypedLinkAttributeRange.make_many(
            self.boto3_raw_data["FilterAttributeRanges"]
        )

    @cached_property
    def FilterTypedLink(self):  # pragma: no cover
        return TypedLinkSchemaAndFacetName.make_one(
            self.boto3_raw_data["FilterTypedLink"]
        )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchListIncomingTypedLinksTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchListIncomingTypedLinksTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchListOutgoingTypedLinks:
    boto3_raw_data: "type_defs.BatchListOutgoingTypedLinksTypeDef" = dataclasses.field()

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    @cached_property
    def FilterAttributeRanges(self):  # pragma: no cover
        return TypedLinkAttributeRange.make_many(
            self.boto3_raw_data["FilterAttributeRanges"]
        )

    @cached_property
    def FilterTypedLink(self):  # pragma: no cover
        return TypedLinkSchemaAndFacetName.make_one(
            self.boto3_raw_data["FilterTypedLink"]
        )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchListOutgoingTypedLinksTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchListOutgoingTypedLinksTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIncomingTypedLinksRequestPaginate:
    boto3_raw_data: "type_defs.ListIncomingTypedLinksRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    @cached_property
    def FilterAttributeRanges(self):  # pragma: no cover
        return TypedLinkAttributeRange.make_many(
            self.boto3_raw_data["FilterAttributeRanges"]
        )

    @cached_property
    def FilterTypedLink(self):  # pragma: no cover
        return TypedLinkSchemaAndFacetName.make_one(
            self.boto3_raw_data["FilterTypedLink"]
        )

    ConsistencyLevel = field("ConsistencyLevel")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListIncomingTypedLinksRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIncomingTypedLinksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIncomingTypedLinksRequest:
    boto3_raw_data: "type_defs.ListIncomingTypedLinksRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    @cached_property
    def FilterAttributeRanges(self):  # pragma: no cover
        return TypedLinkAttributeRange.make_many(
            self.boto3_raw_data["FilterAttributeRanges"]
        )

    @cached_property
    def FilterTypedLink(self):  # pragma: no cover
        return TypedLinkSchemaAndFacetName.make_one(
            self.boto3_raw_data["FilterTypedLink"]
        )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    ConsistencyLevel = field("ConsistencyLevel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListIncomingTypedLinksRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIncomingTypedLinksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOutgoingTypedLinksRequestPaginate:
    boto3_raw_data: "type_defs.ListOutgoingTypedLinksRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    @cached_property
    def FilterAttributeRanges(self):  # pragma: no cover
        return TypedLinkAttributeRange.make_many(
            self.boto3_raw_data["FilterAttributeRanges"]
        )

    @cached_property
    def FilterTypedLink(self):  # pragma: no cover
        return TypedLinkSchemaAndFacetName.make_one(
            self.boto3_raw_data["FilterTypedLink"]
        )

    ConsistencyLevel = field("ConsistencyLevel")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOutgoingTypedLinksRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOutgoingTypedLinksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOutgoingTypedLinksRequest:
    boto3_raw_data: "type_defs.ListOutgoingTypedLinksRequestTypeDef" = (
        dataclasses.field()
    )

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def ObjectReference(self):  # pragma: no cover
        return ObjectReference.make_one(self.boto3_raw_data["ObjectReference"])

    @cached_property
    def FilterAttributeRanges(self):  # pragma: no cover
        return TypedLinkAttributeRange.make_many(
            self.boto3_raw_data["FilterAttributeRanges"]
        )

    @cached_property
    def FilterTypedLink(self):  # pragma: no cover
        return TypedLinkSchemaAndFacetName.make_one(
            self.boto3_raw_data["FilterTypedLink"]
        )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    ConsistencyLevel = field("ConsistencyLevel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListOutgoingTypedLinksRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOutgoingTypedLinksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TypedLinkFacetAttributeUpdate:
    boto3_raw_data: "type_defs.TypedLinkFacetAttributeUpdateTypeDef" = (
        dataclasses.field()
    )

    Attribute = field("Attribute")
    Action = field("Action")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TypedLinkFacetAttributeUpdateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TypedLinkFacetAttributeUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TypedLinkFacet:
    boto3_raw_data: "type_defs.TypedLinkFacetTypeDef" = dataclasses.field()

    Name = field("Name")
    Attributes = field("Attributes")
    IdentityAttributeOrder = field("IdentityAttributeOrder")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TypedLinkFacetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TypedLinkFacetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchReadResponse:
    boto3_raw_data: "type_defs.BatchReadResponseTypeDef" = dataclasses.field()

    @cached_property
    def Responses(self):  # pragma: no cover
        return BatchReadOperationResponse.make_many(self.boto3_raw_data["Responses"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchReadResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchReadResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTypedLinkFacetRequest:
    boto3_raw_data: "type_defs.UpdateTypedLinkFacetRequestTypeDef" = dataclasses.field()

    SchemaArn = field("SchemaArn")
    Name = field("Name")

    @cached_property
    def AttributeUpdates(self):  # pragma: no cover
        return TypedLinkFacetAttributeUpdate.make_many(
            self.boto3_raw_data["AttributeUpdates"]
        )

    IdentityAttributeOrder = field("IdentityAttributeOrder")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTypedLinkFacetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTypedLinkFacetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTypedLinkFacetRequest:
    boto3_raw_data: "type_defs.CreateTypedLinkFacetRequestTypeDef" = dataclasses.field()

    SchemaArn = field("SchemaArn")

    @cached_property
    def Facet(self):  # pragma: no cover
        return TypedLinkFacet.make_one(self.boto3_raw_data["Facet"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTypedLinkFacetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTypedLinkFacetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDetachTypedLink:
    boto3_raw_data: "type_defs.BatchDetachTypedLinkTypeDef" = dataclasses.field()

    TypedLinkSpecifier = field("TypedLinkSpecifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchDetachTypedLinkTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDetachTypedLinkTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetLinkAttributes:
    boto3_raw_data: "type_defs.BatchGetLinkAttributesTypeDef" = dataclasses.field()

    TypedLinkSpecifier = field("TypedLinkSpecifier")
    AttributeNames = field("AttributeNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetLinkAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetLinkAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchUpdateLinkAttributes:
    boto3_raw_data: "type_defs.BatchUpdateLinkAttributesTypeDef" = dataclasses.field()

    TypedLinkSpecifier = field("TypedLinkSpecifier")

    @cached_property
    def AttributeUpdates(self):  # pragma: no cover
        return LinkAttributeUpdate.make_many(self.boto3_raw_data["AttributeUpdates"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchUpdateLinkAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchUpdateLinkAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachTypedLinkRequest:
    boto3_raw_data: "type_defs.DetachTypedLinkRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")
    TypedLinkSpecifier = field("TypedLinkSpecifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetachTypedLinkRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachTypedLinkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLinkAttributesRequest:
    boto3_raw_data: "type_defs.GetLinkAttributesRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")
    TypedLinkSpecifier = field("TypedLinkSpecifier")
    AttributeNames = field("AttributeNames")
    ConsistencyLevel = field("ConsistencyLevel")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLinkAttributesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLinkAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLinkAttributesRequest:
    boto3_raw_data: "type_defs.UpdateLinkAttributesRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")
    TypedLinkSpecifier = field("TypedLinkSpecifier")

    @cached_property
    def AttributeUpdates(self):  # pragma: no cover
        return LinkAttributeUpdate.make_many(self.boto3_raw_data["AttributeUpdates"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLinkAttributesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLinkAttributesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFacetRequest:
    boto3_raw_data: "type_defs.CreateFacetRequestTypeDef" = dataclasses.field()

    SchemaArn = field("SchemaArn")
    Name = field("Name")
    Attributes = field("Attributes")
    ObjectType = field("ObjectType")
    FacetStyle = field("FacetStyle")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFacetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFacetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FacetAttributeUpdate:
    boto3_raw_data: "type_defs.FacetAttributeUpdateTypeDef" = dataclasses.field()

    Attribute = field("Attribute")
    Action = field("Action")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FacetAttributeUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FacetAttributeUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchReadOperation:
    boto3_raw_data: "type_defs.BatchReadOperationTypeDef" = dataclasses.field()

    @cached_property
    def ListObjectAttributes(self):  # pragma: no cover
        return BatchListObjectAttributes.make_one(
            self.boto3_raw_data["ListObjectAttributes"]
        )

    @cached_property
    def ListObjectChildren(self):  # pragma: no cover
        return BatchListObjectChildren.make_one(
            self.boto3_raw_data["ListObjectChildren"]
        )

    @cached_property
    def ListAttachedIndices(self):  # pragma: no cover
        return BatchListAttachedIndices.make_one(
            self.boto3_raw_data["ListAttachedIndices"]
        )

    @cached_property
    def ListObjectParentPaths(self):  # pragma: no cover
        return BatchListObjectParentPaths.make_one(
            self.boto3_raw_data["ListObjectParentPaths"]
        )

    @cached_property
    def GetObjectInformation(self):  # pragma: no cover
        return BatchGetObjectInformation.make_one(
            self.boto3_raw_data["GetObjectInformation"]
        )

    @cached_property
    def GetObjectAttributes(self):  # pragma: no cover
        return BatchGetObjectAttributes.make_one(
            self.boto3_raw_data["GetObjectAttributes"]
        )

    @cached_property
    def ListObjectParents(self):  # pragma: no cover
        return BatchListObjectParents.make_one(self.boto3_raw_data["ListObjectParents"])

    @cached_property
    def ListObjectPolicies(self):  # pragma: no cover
        return BatchListObjectPolicies.make_one(
            self.boto3_raw_data["ListObjectPolicies"]
        )

    @cached_property
    def ListPolicyAttachments(self):  # pragma: no cover
        return BatchListPolicyAttachments.make_one(
            self.boto3_raw_data["ListPolicyAttachments"]
        )

    @cached_property
    def LookupPolicy(self):  # pragma: no cover
        return BatchLookupPolicy.make_one(self.boto3_raw_data["LookupPolicy"])

    @cached_property
    def ListIndex(self):  # pragma: no cover
        return BatchListIndex.make_one(self.boto3_raw_data["ListIndex"])

    @cached_property
    def ListOutgoingTypedLinks(self):  # pragma: no cover
        return BatchListOutgoingTypedLinks.make_one(
            self.boto3_raw_data["ListOutgoingTypedLinks"]
        )

    @cached_property
    def ListIncomingTypedLinks(self):  # pragma: no cover
        return BatchListIncomingTypedLinks.make_one(
            self.boto3_raw_data["ListIncomingTypedLinks"]
        )

    @cached_property
    def GetLinkAttributes(self):  # pragma: no cover
        return BatchGetLinkAttributes.make_one(self.boto3_raw_data["GetLinkAttributes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchReadOperationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchReadOperationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchWriteOperation:
    boto3_raw_data: "type_defs.BatchWriteOperationTypeDef" = dataclasses.field()

    @cached_property
    def CreateObject(self):  # pragma: no cover
        return BatchCreateObject.make_one(self.boto3_raw_data["CreateObject"])

    @cached_property
    def AttachObject(self):  # pragma: no cover
        return BatchAttachObject.make_one(self.boto3_raw_data["AttachObject"])

    @cached_property
    def DetachObject(self):  # pragma: no cover
        return BatchDetachObject.make_one(self.boto3_raw_data["DetachObject"])

    @cached_property
    def UpdateObjectAttributes(self):  # pragma: no cover
        return BatchUpdateObjectAttributes.make_one(
            self.boto3_raw_data["UpdateObjectAttributes"]
        )

    @cached_property
    def DeleteObject(self):  # pragma: no cover
        return BatchDeleteObject.make_one(self.boto3_raw_data["DeleteObject"])

    @cached_property
    def AddFacetToObject(self):  # pragma: no cover
        return BatchAddFacetToObject.make_one(self.boto3_raw_data["AddFacetToObject"])

    @cached_property
    def RemoveFacetFromObject(self):  # pragma: no cover
        return BatchRemoveFacetFromObject.make_one(
            self.boto3_raw_data["RemoveFacetFromObject"]
        )

    @cached_property
    def AttachPolicy(self):  # pragma: no cover
        return BatchAttachPolicy.make_one(self.boto3_raw_data["AttachPolicy"])

    @cached_property
    def DetachPolicy(self):  # pragma: no cover
        return BatchDetachPolicy.make_one(self.boto3_raw_data["DetachPolicy"])

    @cached_property
    def CreateIndex(self):  # pragma: no cover
        return BatchCreateIndex.make_one(self.boto3_raw_data["CreateIndex"])

    @cached_property
    def AttachToIndex(self):  # pragma: no cover
        return BatchAttachToIndex.make_one(self.boto3_raw_data["AttachToIndex"])

    @cached_property
    def DetachFromIndex(self):  # pragma: no cover
        return BatchDetachFromIndex.make_one(self.boto3_raw_data["DetachFromIndex"])

    @cached_property
    def AttachTypedLink(self):  # pragma: no cover
        return BatchAttachTypedLink.make_one(self.boto3_raw_data["AttachTypedLink"])

    @cached_property
    def DetachTypedLink(self):  # pragma: no cover
        return BatchDetachTypedLink.make_one(self.boto3_raw_data["DetachTypedLink"])

    @cached_property
    def UpdateLinkAttributes(self):  # pragma: no cover
        return BatchUpdateLinkAttributes.make_one(
            self.boto3_raw_data["UpdateLinkAttributes"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchWriteOperationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchWriteOperationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateFacetRequest:
    boto3_raw_data: "type_defs.UpdateFacetRequestTypeDef" = dataclasses.field()

    SchemaArn = field("SchemaArn")
    Name = field("Name")

    @cached_property
    def AttributeUpdates(self):  # pragma: no cover
        return FacetAttributeUpdate.make_many(self.boto3_raw_data["AttributeUpdates"])

    ObjectType = field("ObjectType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFacetRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFacetRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchReadRequest:
    boto3_raw_data: "type_defs.BatchReadRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def Operations(self):  # pragma: no cover
        return BatchReadOperation.make_many(self.boto3_raw_data["Operations"])

    ConsistencyLevel = field("ConsistencyLevel")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchReadRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchReadRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchWriteRequest:
    boto3_raw_data: "type_defs.BatchWriteRequestTypeDef" = dataclasses.field()

    DirectoryArn = field("DirectoryArn")

    @cached_property
    def Operations(self):  # pragma: no cover
        return BatchWriteOperation.make_many(self.boto3_raw_data["Operations"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchWriteRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchWriteRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
