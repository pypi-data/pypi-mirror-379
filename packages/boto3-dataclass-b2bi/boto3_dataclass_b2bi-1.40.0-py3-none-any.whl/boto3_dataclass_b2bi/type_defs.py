# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_b2bi import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class CapabilitySummary:
    boto3_raw_data: "type_defs.CapabilitySummaryTypeDef" = dataclasses.field()

    capabilityId = field("capabilityId")
    name = field("name")
    type = field("type")
    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CapabilitySummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapabilitySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputFileSource:
    boto3_raw_data: "type_defs.InputFileSourceTypeDef" = dataclasses.field()

    fileContent = field("fileContent")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputFileSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputFileSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class X12Details:
    boto3_raw_data: "type_defs.X12DetailsTypeDef" = dataclasses.field()

    transactionSet = field("transactionSet")
    version = field("version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.X12DetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.X12DetailsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Location:
    boto3_raw_data: "type_defs.S3LocationTypeDef" = dataclasses.field()

    bucketName = field("bucketName")
    key = field("key")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3LocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3LocationTypeDef"]]
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
class Mapping:
    boto3_raw_data: "type_defs.MappingTypeDef" = dataclasses.field()

    templateLanguage = field("templateLanguage")
    template = field("template")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MappingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCapabilityRequest:
    boto3_raw_data: "type_defs.DeleteCapabilityRequestTypeDef" = dataclasses.field()

    capabilityId = field("capabilityId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCapabilityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCapabilityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePartnershipRequest:
    boto3_raw_data: "type_defs.DeletePartnershipRequestTypeDef" = dataclasses.field()

    partnershipId = field("partnershipId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePartnershipRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePartnershipRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteProfileRequest:
    boto3_raw_data: "type_defs.DeleteProfileRequestTypeDef" = dataclasses.field()

    profileId = field("profileId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTransformerRequest:
    boto3_raw_data: "type_defs.DeleteTransformerRequestTypeDef" = dataclasses.field()

    transformerId = field("transformerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTransformerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTransformerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GenerateMappingRequest:
    boto3_raw_data: "type_defs.GenerateMappingRequestTypeDef" = dataclasses.field()

    inputFileContent = field("inputFileContent")
    outputFileContent = field("outputFileContent")
    mappingType = field("mappingType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerateMappingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateMappingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCapabilityRequest:
    boto3_raw_data: "type_defs.GetCapabilityRequestTypeDef" = dataclasses.field()

    capabilityId = field("capabilityId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCapabilityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCapabilityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPartnershipRequest:
    boto3_raw_data: "type_defs.GetPartnershipRequestTypeDef" = dataclasses.field()

    partnershipId = field("partnershipId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPartnershipRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPartnershipRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProfileRequest:
    boto3_raw_data: "type_defs.GetProfileRequestTypeDef" = dataclasses.field()

    profileId = field("profileId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetProfileRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTransformerJobRequest:
    boto3_raw_data: "type_defs.GetTransformerJobRequestTypeDef" = dataclasses.field()

    transformerJobId = field("transformerJobId")
    transformerId = field("transformerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTransformerJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTransformerJobRequestTypeDef"]
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
class GetTransformerRequest:
    boto3_raw_data: "type_defs.GetTransformerRequestTypeDef" = dataclasses.field()

    transformerId = field("transformerId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTransformerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTransformerRequestTypeDef"]
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
class ListCapabilitiesRequest:
    boto3_raw_data: "type_defs.ListCapabilitiesRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCapabilitiesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCapabilitiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPartnershipsRequest:
    boto3_raw_data: "type_defs.ListPartnershipsRequestTypeDef" = dataclasses.field()

    profileId = field("profileId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPartnershipsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPartnershipsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfilesRequest:
    boto3_raw_data: "type_defs.ListProfilesRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProfilesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfilesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProfileSummary:
    boto3_raw_data: "type_defs.ProfileSummaryTypeDef" = dataclasses.field()

    profileId = field("profileId")
    name = field("name")
    businessName = field("businessName")
    createdAt = field("createdAt")
    logging = field("logging")
    logGroupName = field("logGroupName")
    modifiedAt = field("modifiedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProfileSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProfileSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    ResourceARN = field("ResourceARN")

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
class ListTransformersRequest:
    boto3_raw_data: "type_defs.ListTransformersRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTransformersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTransformersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SampleDocumentKeys:
    boto3_raw_data: "type_defs.SampleDocumentKeysTypeDef" = dataclasses.field()

    input = field("input")
    output = field("output")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SampleDocumentKeysTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SampleDocumentKeysTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestMappingRequest:
    boto3_raw_data: "type_defs.TestMappingRequestTypeDef" = dataclasses.field()

    inputFileContent = field("inputFileContent")
    mappingTemplate = field("mappingTemplate")
    fileFormat = field("fileFormat")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestMappingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestMappingRequestTypeDef"]
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

    ResourceARN = field("ResourceARN")
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
class UpdateProfileRequest:
    boto3_raw_data: "type_defs.UpdateProfileRequestTypeDef" = dataclasses.field()

    profileId = field("profileId")
    name = field("name")
    email = field("email")
    phone = field("phone")
    businessName = field("businessName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WrapOptions:
    boto3_raw_data: "type_defs.WrapOptionsTypeDef" = dataclasses.field()

    wrapBy = field("wrapBy")
    lineTerminator = field("lineTerminator")
    lineLength = field("lineLength")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WrapOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WrapOptionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class X12AcknowledgmentOptions:
    boto3_raw_data: "type_defs.X12AcknowledgmentOptionsTypeDef" = dataclasses.field()

    functionalAcknowledgment = field("functionalAcknowledgment")
    technicalAcknowledgment = field("technicalAcknowledgment")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.X12AcknowledgmentOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.X12AcknowledgmentOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class X12SplitOptions:
    boto3_raw_data: "type_defs.X12SplitOptionsTypeDef" = dataclasses.field()

    splitBy = field("splitBy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.X12SplitOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.X12SplitOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class X12CodeListValidationRuleOutput:
    boto3_raw_data: "type_defs.X12CodeListValidationRuleOutputTypeDef" = (
        dataclasses.field()
    )

    elementId = field("elementId")
    codesToAdd = field("codesToAdd")
    codesToRemove = field("codesToRemove")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.X12CodeListValidationRuleOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.X12CodeListValidationRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class X12CodeListValidationRule:
    boto3_raw_data: "type_defs.X12CodeListValidationRuleTypeDef" = dataclasses.field()

    elementId = field("elementId")
    codesToAdd = field("codesToAdd")
    codesToRemove = field("codesToRemove")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.X12CodeListValidationRuleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.X12CodeListValidationRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class X12ControlNumbers:
    boto3_raw_data: "type_defs.X12ControlNumbersTypeDef" = dataclasses.field()

    startingInterchangeControlNumber = field("startingInterchangeControlNumber")
    startingFunctionalGroupControlNumber = field("startingFunctionalGroupControlNumber")
    startingTransactionSetControlNumber = field("startingTransactionSetControlNumber")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.X12ControlNumbersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.X12ControlNumbersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class X12Delimiters:
    boto3_raw_data: "type_defs.X12DelimitersTypeDef" = dataclasses.field()

    componentSeparator = field("componentSeparator")
    dataElementSeparator = field("dataElementSeparator")
    segmentTerminator = field("segmentTerminator")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.X12DelimitersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.X12DelimitersTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class X12ElementLengthValidationRule:
    boto3_raw_data: "type_defs.X12ElementLengthValidationRuleTypeDef" = (
        dataclasses.field()
    )

    elementId = field("elementId")
    maxLength = field("maxLength")
    minLength = field("minLength")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.X12ElementLengthValidationRuleTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.X12ElementLengthValidationRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class X12ElementRequirementValidationRule:
    boto3_raw_data: "type_defs.X12ElementRequirementValidationRuleTypeDef" = (
        dataclasses.field()
    )

    elementPosition = field("elementPosition")
    requirement = field("requirement")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.X12ElementRequirementValidationRuleTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.X12ElementRequirementValidationRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class X12FunctionalGroupHeaders:
    boto3_raw_data: "type_defs.X12FunctionalGroupHeadersTypeDef" = dataclasses.field()

    applicationSenderCode = field("applicationSenderCode")
    applicationReceiverCode = field("applicationReceiverCode")
    responsibleAgencyCode = field("responsibleAgencyCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.X12FunctionalGroupHeadersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.X12FunctionalGroupHeadersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class X12InterchangeControlHeaders:
    boto3_raw_data: "type_defs.X12InterchangeControlHeadersTypeDef" = (
        dataclasses.field()
    )

    senderIdQualifier = field("senderIdQualifier")
    senderId = field("senderId")
    receiverIdQualifier = field("receiverIdQualifier")
    receiverId = field("receiverId")
    repetitionSeparator = field("repetitionSeparator")
    acknowledgmentRequestedCode = field("acknowledgmentRequestedCode")
    usageIndicatorCode = field("usageIndicatorCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.X12InterchangeControlHeadersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.X12InterchangeControlHeadersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConversionSource:
    boto3_raw_data: "type_defs.ConversionSourceTypeDef" = dataclasses.field()

    fileFormat = field("fileFormat")

    @cached_property
    def inputFile(self):  # pragma: no cover
        return InputFileSource.make_one(self.boto3_raw_data["inputFile"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConversionSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConversionSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConversionTargetFormatDetails:
    boto3_raw_data: "type_defs.ConversionTargetFormatDetailsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def x12(self):  # pragma: no cover
        return X12Details.make_one(self.boto3_raw_data["x12"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConversionTargetFormatDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConversionTargetFormatDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EdiType:
    boto3_raw_data: "type_defs.EdiTypeTypeDef" = dataclasses.field()

    @cached_property
    def x12Details(self):  # pragma: no cover
        return X12Details.make_one(self.boto3_raw_data["x12Details"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EdiTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EdiTypeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FormatOptions:
    boto3_raw_data: "type_defs.FormatOptionsTypeDef" = dataclasses.field()

    @cached_property
    def x12(self):  # pragma: no cover
        return X12Details.make_one(self.boto3_raw_data["x12"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FormatOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FormatOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateDetails:
    boto3_raw_data: "type_defs.TemplateDetailsTypeDef" = dataclasses.field()

    @cached_property
    def x12(self):  # pragma: no cover
        return X12Details.make_one(self.boto3_raw_data["x12"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TemplateDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TemplateDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputSampleFileSource:
    boto3_raw_data: "type_defs.OutputSampleFileSourceTypeDef" = dataclasses.field()

    @cached_property
    def fileLocation(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["fileLocation"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutputSampleFileSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputSampleFileSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTransformerJobRequest:
    boto3_raw_data: "type_defs.StartTransformerJobRequestTypeDef" = dataclasses.field()

    @cached_property
    def inputFile(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["inputFile"])

    @cached_property
    def outputLocation(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["outputLocation"])

    transformerId = field("transformerId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartTransformerJobRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTransformerJobRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateProfileRequest:
    boto3_raw_data: "type_defs.CreateProfileRequestTypeDef" = dataclasses.field()

    name = field("name")
    phone = field("phone")
    businessName = field("businessName")
    logging = field("logging")
    email = field("email")
    clientToken = field("clientToken")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProfileRequestTypeDef"]
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

    ResourceARN = field("ResourceARN")

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
class CreateProfileResponse:
    boto3_raw_data: "type_defs.CreateProfileResponseTypeDef" = dataclasses.field()

    profileId = field("profileId")
    profileArn = field("profileArn")
    name = field("name")
    businessName = field("businessName")
    phone = field("phone")
    email = field("email")
    logging = field("logging")
    logGroupName = field("logGroupName")
    createdAt = field("createdAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStarterMappingTemplateResponse:
    boto3_raw_data: "type_defs.CreateStarterMappingTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    mappingTemplate = field("mappingTemplate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateStarterMappingTemplateResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStarterMappingTemplateResponseTypeDef"]
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
class GenerateMappingResponse:
    boto3_raw_data: "type_defs.GenerateMappingResponseTypeDef" = dataclasses.field()

    mappingTemplate = field("mappingTemplate")
    mappingAccuracy = field("mappingAccuracy")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GenerateMappingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GenerateMappingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProfileResponse:
    boto3_raw_data: "type_defs.GetProfileResponseTypeDef" = dataclasses.field()

    profileId = field("profileId")
    profileArn = field("profileArn")
    name = field("name")
    email = field("email")
    phone = field("phone")
    businessName = field("businessName")
    logging = field("logging")
    logGroupName = field("logGroupName")
    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTransformerJobResponse:
    boto3_raw_data: "type_defs.GetTransformerJobResponseTypeDef" = dataclasses.field()

    status = field("status")

    @cached_property
    def outputFiles(self):  # pragma: no cover
        return S3Location.make_many(self.boto3_raw_data["outputFiles"])

    message = field("message")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTransformerJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTransformerJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCapabilitiesResponse:
    boto3_raw_data: "type_defs.ListCapabilitiesResponseTypeDef" = dataclasses.field()

    @cached_property
    def capabilities(self):  # pragma: no cover
        return CapabilitySummary.make_many(self.boto3_raw_data["capabilities"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCapabilitiesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCapabilitiesResponseTypeDef"]
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
class StartTransformerJobResponse:
    boto3_raw_data: "type_defs.StartTransformerJobResponseTypeDef" = dataclasses.field()

    transformerJobId = field("transformerJobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartTransformerJobResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTransformerJobResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestConversionResponse:
    boto3_raw_data: "type_defs.TestConversionResponseTypeDef" = dataclasses.field()

    convertedFileContent = field("convertedFileContent")
    validationMessages = field("validationMessages")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestConversionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestConversionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestMappingResponse:
    boto3_raw_data: "type_defs.TestMappingResponseTypeDef" = dataclasses.field()

    mappedFileContent = field("mappedFileContent")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestMappingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestMappingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestParsingResponse:
    boto3_raw_data: "type_defs.TestParsingResponseTypeDef" = dataclasses.field()

    parsedFileContent = field("parsedFileContent")
    parsedSplitFileContents = field("parsedSplitFileContents")
    validationMessages = field("validationMessages")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestParsingResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestParsingResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProfileResponse:
    boto3_raw_data: "type_defs.UpdateProfileResponseTypeDef" = dataclasses.field()

    profileId = field("profileId")
    profileArn = field("profileArn")
    name = field("name")
    email = field("email")
    phone = field("phone")
    businessName = field("businessName")
    logging = field("logging")
    logGroupName = field("logGroupName")
    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTransformerJobRequestWait:
    boto3_raw_data: "type_defs.GetTransformerJobRequestWaitTypeDef" = (
        dataclasses.field()
    )

    transformerJobId = field("transformerJobId")
    transformerId = field("transformerId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTransformerJobRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTransformerJobRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCapabilitiesRequestPaginate:
    boto3_raw_data: "type_defs.ListCapabilitiesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCapabilitiesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCapabilitiesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPartnershipsRequestPaginate:
    boto3_raw_data: "type_defs.ListPartnershipsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    profileId = field("profileId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPartnershipsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPartnershipsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfilesRequestPaginate:
    boto3_raw_data: "type_defs.ListProfilesRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProfilesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfilesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTransformersRequestPaginate:
    boto3_raw_data: "type_defs.ListTransformersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTransformersRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTransformersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProfilesResponse:
    boto3_raw_data: "type_defs.ListProfilesResponseTypeDef" = dataclasses.field()

    @cached_property
    def profiles(self):  # pragma: no cover
        return ProfileSummary.make_many(self.boto3_raw_data["profiles"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProfilesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProfilesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SampleDocumentsOutput:
    boto3_raw_data: "type_defs.SampleDocumentsOutputTypeDef" = dataclasses.field()

    bucketName = field("bucketName")

    @cached_property
    def keys(self):  # pragma: no cover
        return SampleDocumentKeys.make_many(self.boto3_raw_data["keys"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SampleDocumentsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SampleDocumentsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SampleDocuments:
    boto3_raw_data: "type_defs.SampleDocumentsTypeDef" = dataclasses.field()

    bucketName = field("bucketName")

    @cached_property
    def keys(self):  # pragma: no cover
        return SampleDocumentKeys.make_many(self.boto3_raw_data["keys"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SampleDocumentsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SampleDocumentsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class X12InboundEdiOptions:
    boto3_raw_data: "type_defs.X12InboundEdiOptionsTypeDef" = dataclasses.field()

    @cached_property
    def acknowledgmentOptions(self):  # pragma: no cover
        return X12AcknowledgmentOptions.make_one(
            self.boto3_raw_data["acknowledgmentOptions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.X12InboundEdiOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.X12InboundEdiOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class X12ValidationRuleOutput:
    boto3_raw_data: "type_defs.X12ValidationRuleOutputTypeDef" = dataclasses.field()

    @cached_property
    def codeListValidationRule(self):  # pragma: no cover
        return X12CodeListValidationRuleOutput.make_one(
            self.boto3_raw_data["codeListValidationRule"]
        )

    @cached_property
    def elementLengthValidationRule(self):  # pragma: no cover
        return X12ElementLengthValidationRule.make_one(
            self.boto3_raw_data["elementLengthValidationRule"]
        )

    @cached_property
    def elementRequirementValidationRule(self):  # pragma: no cover
        return X12ElementRequirementValidationRule.make_one(
            self.boto3_raw_data["elementRequirementValidationRule"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.X12ValidationRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.X12ValidationRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class X12OutboundEdiHeaders:
    boto3_raw_data: "type_defs.X12OutboundEdiHeadersTypeDef" = dataclasses.field()

    @cached_property
    def interchangeControlHeaders(self):  # pragma: no cover
        return X12InterchangeControlHeaders.make_one(
            self.boto3_raw_data["interchangeControlHeaders"]
        )

    @cached_property
    def functionalGroupHeaders(self):  # pragma: no cover
        return X12FunctionalGroupHeaders.make_one(
            self.boto3_raw_data["functionalGroupHeaders"]
        )

    @cached_property
    def delimiters(self):  # pragma: no cover
        return X12Delimiters.make_one(self.boto3_raw_data["delimiters"])

    validateEdi = field("validateEdi")

    @cached_property
    def controlNumbers(self):  # pragma: no cover
        return X12ControlNumbers.make_one(self.boto3_raw_data["controlNumbers"])

    gs05TimeFormat = field("gs05TimeFormat")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.X12OutboundEdiHeadersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.X12OutboundEdiHeadersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EdiConfiguration:
    boto3_raw_data: "type_defs.EdiConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def type(self):  # pragma: no cover
        return EdiType.make_one(self.boto3_raw_data["type"])

    @cached_property
    def inputLocation(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["inputLocation"])

    @cached_property
    def outputLocation(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["outputLocation"])

    transformerId = field("transformerId")
    capabilityDirection = field("capabilityDirection")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EdiConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EdiConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStarterMappingTemplateRequest:
    boto3_raw_data: "type_defs.CreateStarterMappingTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    mappingType = field("mappingType")

    @cached_property
    def templateDetails(self):  # pragma: no cover
        return TemplateDetails.make_one(self.boto3_raw_data["templateDetails"])

    @cached_property
    def outputSampleLocation(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["outputSampleLocation"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateStarterMappingTemplateRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStarterMappingTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InboundEdiOptions:
    boto3_raw_data: "type_defs.InboundEdiOptionsTypeDef" = dataclasses.field()

    @cached_property
    def x12(self):  # pragma: no cover
        return X12InboundEdiOptions.make_one(self.boto3_raw_data["x12"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InboundEdiOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InboundEdiOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class X12ValidationRule:
    boto3_raw_data: "type_defs.X12ValidationRuleTypeDef" = dataclasses.field()

    codeListValidationRule = field("codeListValidationRule")

    @cached_property
    def elementLengthValidationRule(self):  # pragma: no cover
        return X12ElementLengthValidationRule.make_one(
            self.boto3_raw_data["elementLengthValidationRule"]
        )

    @cached_property
    def elementRequirementValidationRule(self):  # pragma: no cover
        return X12ElementRequirementValidationRule.make_one(
            self.boto3_raw_data["elementRequirementValidationRule"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.X12ValidationRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.X12ValidationRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class X12ValidationOptionsOutput:
    boto3_raw_data: "type_defs.X12ValidationOptionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def validationRules(self):  # pragma: no cover
        return X12ValidationRuleOutput.make_many(self.boto3_raw_data["validationRules"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.X12ValidationOptionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.X12ValidationOptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class X12Envelope:
    boto3_raw_data: "type_defs.X12EnvelopeTypeDef" = dataclasses.field()

    @cached_property
    def common(self):  # pragma: no cover
        return X12OutboundEdiHeaders.make_one(self.boto3_raw_data["common"])

    @cached_property
    def wrapOptions(self):  # pragma: no cover
        return WrapOptions.make_one(self.boto3_raw_data["wrapOptions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.X12EnvelopeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.X12EnvelopeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapabilityConfiguration:
    boto3_raw_data: "type_defs.CapabilityConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def edi(self):  # pragma: no cover
        return EdiConfiguration.make_one(self.boto3_raw_data["edi"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CapabilityConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapabilityConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class X12AdvancedOptionsOutput:
    boto3_raw_data: "type_defs.X12AdvancedOptionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def splitOptions(self):  # pragma: no cover
        return X12SplitOptions.make_one(self.boto3_raw_data["splitOptions"])

    @cached_property
    def validationOptions(self):  # pragma: no cover
        return X12ValidationOptionsOutput.make_one(
            self.boto3_raw_data["validationOptions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.X12AdvancedOptionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.X12AdvancedOptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutboundEdiOptions:
    boto3_raw_data: "type_defs.OutboundEdiOptionsTypeDef" = dataclasses.field()

    @cached_property
    def x12(self):  # pragma: no cover
        return X12Envelope.make_one(self.boto3_raw_data["x12"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutboundEdiOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutboundEdiOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCapabilityRequest:
    boto3_raw_data: "type_defs.CreateCapabilityRequestTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")

    @cached_property
    def configuration(self):  # pragma: no cover
        return CapabilityConfiguration.make_one(self.boto3_raw_data["configuration"])

    @cached_property
    def instructionsDocuments(self):  # pragma: no cover
        return S3Location.make_many(self.boto3_raw_data["instructionsDocuments"])

    clientToken = field("clientToken")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCapabilityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCapabilityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCapabilityResponse:
    boto3_raw_data: "type_defs.CreateCapabilityResponseTypeDef" = dataclasses.field()

    capabilityId = field("capabilityId")
    capabilityArn = field("capabilityArn")
    name = field("name")
    type = field("type")

    @cached_property
    def configuration(self):  # pragma: no cover
        return CapabilityConfiguration.make_one(self.boto3_raw_data["configuration"])

    @cached_property
    def instructionsDocuments(self):  # pragma: no cover
        return S3Location.make_many(self.boto3_raw_data["instructionsDocuments"])

    createdAt = field("createdAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCapabilityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCapabilityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCapabilityResponse:
    boto3_raw_data: "type_defs.GetCapabilityResponseTypeDef" = dataclasses.field()

    capabilityId = field("capabilityId")
    capabilityArn = field("capabilityArn")
    name = field("name")
    type = field("type")

    @cached_property
    def configuration(self):  # pragma: no cover
        return CapabilityConfiguration.make_one(self.boto3_raw_data["configuration"])

    @cached_property
    def instructionsDocuments(self):  # pragma: no cover
        return S3Location.make_many(self.boto3_raw_data["instructionsDocuments"])

    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCapabilityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCapabilityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCapabilityRequest:
    boto3_raw_data: "type_defs.UpdateCapabilityRequestTypeDef" = dataclasses.field()

    capabilityId = field("capabilityId")
    name = field("name")

    @cached_property
    def configuration(self):  # pragma: no cover
        return CapabilityConfiguration.make_one(self.boto3_raw_data["configuration"])

    @cached_property
    def instructionsDocuments(self):  # pragma: no cover
        return S3Location.make_many(self.boto3_raw_data["instructionsDocuments"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCapabilityRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCapabilityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCapabilityResponse:
    boto3_raw_data: "type_defs.UpdateCapabilityResponseTypeDef" = dataclasses.field()

    capabilityId = field("capabilityId")
    capabilityArn = field("capabilityArn")
    name = field("name")
    type = field("type")

    @cached_property
    def configuration(self):  # pragma: no cover
        return CapabilityConfiguration.make_one(self.boto3_raw_data["configuration"])

    @cached_property
    def instructionsDocuments(self):  # pragma: no cover
        return S3Location.make_many(self.boto3_raw_data["instructionsDocuments"])

    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCapabilityResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCapabilityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class X12ValidationOptions:
    boto3_raw_data: "type_defs.X12ValidationOptionsTypeDef" = dataclasses.field()

    validationRules = field("validationRules")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.X12ValidationOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.X12ValidationOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdvancedOptionsOutput:
    boto3_raw_data: "type_defs.AdvancedOptionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def x12(self):  # pragma: no cover
        return X12AdvancedOptionsOutput.make_one(self.boto3_raw_data["x12"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdvancedOptionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdvancedOptionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapabilityOptions:
    boto3_raw_data: "type_defs.CapabilityOptionsTypeDef" = dataclasses.field()

    @cached_property
    def outboundEdi(self):  # pragma: no cover
        return OutboundEdiOptions.make_one(self.boto3_raw_data["outboundEdi"])

    @cached_property
    def inboundEdi(self):  # pragma: no cover
        return InboundEdiOptions.make_one(self.boto3_raw_data["inboundEdi"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CapabilityOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CapabilityOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputConversionOutput:
    boto3_raw_data: "type_defs.InputConversionOutputTypeDef" = dataclasses.field()

    fromFormat = field("fromFormat")

    @cached_property
    def formatOptions(self):  # pragma: no cover
        return FormatOptions.make_one(self.boto3_raw_data["formatOptions"])

    @cached_property
    def advancedOptions(self):  # pragma: no cover
        return AdvancedOptionsOutput.make_one(self.boto3_raw_data["advancedOptions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InputConversionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InputConversionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputConversionOutput:
    boto3_raw_data: "type_defs.OutputConversionOutputTypeDef" = dataclasses.field()

    toFormat = field("toFormat")

    @cached_property
    def formatOptions(self):  # pragma: no cover
        return FormatOptions.make_one(self.boto3_raw_data["formatOptions"])

    @cached_property
    def advancedOptions(self):  # pragma: no cover
        return AdvancedOptionsOutput.make_one(self.boto3_raw_data["advancedOptions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutputConversionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputConversionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePartnershipRequest:
    boto3_raw_data: "type_defs.CreatePartnershipRequestTypeDef" = dataclasses.field()

    profileId = field("profileId")
    name = field("name")
    email = field("email")
    capabilities = field("capabilities")
    phone = field("phone")

    @cached_property
    def capabilityOptions(self):  # pragma: no cover
        return CapabilityOptions.make_one(self.boto3_raw_data["capabilityOptions"])

    clientToken = field("clientToken")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePartnershipRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePartnershipRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePartnershipResponse:
    boto3_raw_data: "type_defs.CreatePartnershipResponseTypeDef" = dataclasses.field()

    profileId = field("profileId")
    partnershipId = field("partnershipId")
    partnershipArn = field("partnershipArn")
    name = field("name")
    email = field("email")
    phone = field("phone")
    capabilities = field("capabilities")

    @cached_property
    def capabilityOptions(self):  # pragma: no cover
        return CapabilityOptions.make_one(self.boto3_raw_data["capabilityOptions"])

    tradingPartnerId = field("tradingPartnerId")
    createdAt = field("createdAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePartnershipResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePartnershipResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPartnershipResponse:
    boto3_raw_data: "type_defs.GetPartnershipResponseTypeDef" = dataclasses.field()

    profileId = field("profileId")
    partnershipId = field("partnershipId")
    partnershipArn = field("partnershipArn")
    name = field("name")
    email = field("email")
    phone = field("phone")
    capabilities = field("capabilities")

    @cached_property
    def capabilityOptions(self):  # pragma: no cover
        return CapabilityOptions.make_one(self.boto3_raw_data["capabilityOptions"])

    tradingPartnerId = field("tradingPartnerId")
    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPartnershipResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPartnershipResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PartnershipSummary:
    boto3_raw_data: "type_defs.PartnershipSummaryTypeDef" = dataclasses.field()

    profileId = field("profileId")
    partnershipId = field("partnershipId")
    createdAt = field("createdAt")
    name = field("name")
    capabilities = field("capabilities")

    @cached_property
    def capabilityOptions(self):  # pragma: no cover
        return CapabilityOptions.make_one(self.boto3_raw_data["capabilityOptions"])

    tradingPartnerId = field("tradingPartnerId")
    modifiedAt = field("modifiedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PartnershipSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PartnershipSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePartnershipRequest:
    boto3_raw_data: "type_defs.UpdatePartnershipRequestTypeDef" = dataclasses.field()

    partnershipId = field("partnershipId")
    name = field("name")
    capabilities = field("capabilities")

    @cached_property
    def capabilityOptions(self):  # pragma: no cover
        return CapabilityOptions.make_one(self.boto3_raw_data["capabilityOptions"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePartnershipRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePartnershipRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePartnershipResponse:
    boto3_raw_data: "type_defs.UpdatePartnershipResponseTypeDef" = dataclasses.field()

    profileId = field("profileId")
    partnershipId = field("partnershipId")
    partnershipArn = field("partnershipArn")
    name = field("name")
    email = field("email")
    phone = field("phone")
    capabilities = field("capabilities")

    @cached_property
    def capabilityOptions(self):  # pragma: no cover
        return CapabilityOptions.make_one(self.boto3_raw_data["capabilityOptions"])

    tradingPartnerId = field("tradingPartnerId")
    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdatePartnershipResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePartnershipResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class X12AdvancedOptions:
    boto3_raw_data: "type_defs.X12AdvancedOptionsTypeDef" = dataclasses.field()

    @cached_property
    def splitOptions(self):  # pragma: no cover
        return X12SplitOptions.make_one(self.boto3_raw_data["splitOptions"])

    validationOptions = field("validationOptions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.X12AdvancedOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.X12AdvancedOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTransformerResponse:
    boto3_raw_data: "type_defs.CreateTransformerResponseTypeDef" = dataclasses.field()

    transformerId = field("transformerId")
    transformerArn = field("transformerArn")
    name = field("name")
    status = field("status")
    createdAt = field("createdAt")
    fileFormat = field("fileFormat")
    mappingTemplate = field("mappingTemplate")

    @cached_property
    def ediType(self):  # pragma: no cover
        return EdiType.make_one(self.boto3_raw_data["ediType"])

    sampleDocument = field("sampleDocument")

    @cached_property
    def inputConversion(self):  # pragma: no cover
        return InputConversionOutput.make_one(self.boto3_raw_data["inputConversion"])

    @cached_property
    def mapping(self):  # pragma: no cover
        return Mapping.make_one(self.boto3_raw_data["mapping"])

    @cached_property
    def outputConversion(self):  # pragma: no cover
        return OutputConversionOutput.make_one(self.boto3_raw_data["outputConversion"])

    @cached_property
    def sampleDocuments(self):  # pragma: no cover
        return SampleDocumentsOutput.make_one(self.boto3_raw_data["sampleDocuments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTransformerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTransformerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTransformerResponse:
    boto3_raw_data: "type_defs.GetTransformerResponseTypeDef" = dataclasses.field()

    transformerId = field("transformerId")
    transformerArn = field("transformerArn")
    name = field("name")
    status = field("status")
    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")
    fileFormat = field("fileFormat")
    mappingTemplate = field("mappingTemplate")

    @cached_property
    def ediType(self):  # pragma: no cover
        return EdiType.make_one(self.boto3_raw_data["ediType"])

    sampleDocument = field("sampleDocument")

    @cached_property
    def inputConversion(self):  # pragma: no cover
        return InputConversionOutput.make_one(self.boto3_raw_data["inputConversion"])

    @cached_property
    def mapping(self):  # pragma: no cover
        return Mapping.make_one(self.boto3_raw_data["mapping"])

    @cached_property
    def outputConversion(self):  # pragma: no cover
        return OutputConversionOutput.make_one(self.boto3_raw_data["outputConversion"])

    @cached_property
    def sampleDocuments(self):  # pragma: no cover
        return SampleDocumentsOutput.make_one(self.boto3_raw_data["sampleDocuments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTransformerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTransformerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransformerSummary:
    boto3_raw_data: "type_defs.TransformerSummaryTypeDef" = dataclasses.field()

    transformerId = field("transformerId")
    name = field("name")
    status = field("status")
    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")
    fileFormat = field("fileFormat")
    mappingTemplate = field("mappingTemplate")

    @cached_property
    def ediType(self):  # pragma: no cover
        return EdiType.make_one(self.boto3_raw_data["ediType"])

    sampleDocument = field("sampleDocument")

    @cached_property
    def inputConversion(self):  # pragma: no cover
        return InputConversionOutput.make_one(self.boto3_raw_data["inputConversion"])

    @cached_property
    def mapping(self):  # pragma: no cover
        return Mapping.make_one(self.boto3_raw_data["mapping"])

    @cached_property
    def outputConversion(self):  # pragma: no cover
        return OutputConversionOutput.make_one(self.boto3_raw_data["outputConversion"])

    @cached_property
    def sampleDocuments(self):  # pragma: no cover
        return SampleDocumentsOutput.make_one(self.boto3_raw_data["sampleDocuments"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TransformerSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransformerSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTransformerResponse:
    boto3_raw_data: "type_defs.UpdateTransformerResponseTypeDef" = dataclasses.field()

    transformerId = field("transformerId")
    transformerArn = field("transformerArn")
    name = field("name")
    status = field("status")
    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")
    fileFormat = field("fileFormat")
    mappingTemplate = field("mappingTemplate")

    @cached_property
    def ediType(self):  # pragma: no cover
        return EdiType.make_one(self.boto3_raw_data["ediType"])

    sampleDocument = field("sampleDocument")

    @cached_property
    def inputConversion(self):  # pragma: no cover
        return InputConversionOutput.make_one(self.boto3_raw_data["inputConversion"])

    @cached_property
    def mapping(self):  # pragma: no cover
        return Mapping.make_one(self.boto3_raw_data["mapping"])

    @cached_property
    def outputConversion(self):  # pragma: no cover
        return OutputConversionOutput.make_one(self.boto3_raw_data["outputConversion"])

    @cached_property
    def sampleDocuments(self):  # pragma: no cover
        return SampleDocumentsOutput.make_one(self.boto3_raw_data["sampleDocuments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTransformerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTransformerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPartnershipsResponse:
    boto3_raw_data: "type_defs.ListPartnershipsResponseTypeDef" = dataclasses.field()

    @cached_property
    def partnerships(self):  # pragma: no cover
        return PartnershipSummary.make_many(self.boto3_raw_data["partnerships"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPartnershipsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPartnershipsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTransformersResponse:
    boto3_raw_data: "type_defs.ListTransformersResponseTypeDef" = dataclasses.field()

    @cached_property
    def transformers(self):  # pragma: no cover
        return TransformerSummary.make_many(self.boto3_raw_data["transformers"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTransformersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTransformersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdvancedOptions:
    boto3_raw_data: "type_defs.AdvancedOptionsTypeDef" = dataclasses.field()

    x12 = field("x12")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AdvancedOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AdvancedOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputConversion:
    boto3_raw_data: "type_defs.InputConversionTypeDef" = dataclasses.field()

    fromFormat = field("fromFormat")

    @cached_property
    def formatOptions(self):  # pragma: no cover
        return FormatOptions.make_one(self.boto3_raw_data["formatOptions"])

    @cached_property
    def advancedOptions(self):  # pragma: no cover
        return AdvancedOptions.make_one(self.boto3_raw_data["advancedOptions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputConversionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputConversionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputConversion:
    boto3_raw_data: "type_defs.OutputConversionTypeDef" = dataclasses.field()

    toFormat = field("toFormat")

    @cached_property
    def formatOptions(self):  # pragma: no cover
        return FormatOptions.make_one(self.boto3_raw_data["formatOptions"])

    @cached_property
    def advancedOptions(self):  # pragma: no cover
        return AdvancedOptions.make_one(self.boto3_raw_data["advancedOptions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputConversionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutputConversionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConversionTarget:
    boto3_raw_data: "type_defs.ConversionTargetTypeDef" = dataclasses.field()

    fileFormat = field("fileFormat")

    @cached_property
    def formatDetails(self):  # pragma: no cover
        return ConversionTargetFormatDetails.make_one(
            self.boto3_raw_data["formatDetails"]
        )

    @cached_property
    def outputSampleFile(self):  # pragma: no cover
        return OutputSampleFileSource.make_one(self.boto3_raw_data["outputSampleFile"])

    advancedOptions = field("advancedOptions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConversionTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConversionTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestParsingRequest:
    boto3_raw_data: "type_defs.TestParsingRequestTypeDef" = dataclasses.field()

    @cached_property
    def inputFile(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["inputFile"])

    fileFormat = field("fileFormat")

    @cached_property
    def ediType(self):  # pragma: no cover
        return EdiType.make_one(self.boto3_raw_data["ediType"])

    advancedOptions = field("advancedOptions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestParsingRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestParsingRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestConversionRequest:
    boto3_raw_data: "type_defs.TestConversionRequestTypeDef" = dataclasses.field()

    @cached_property
    def source(self):  # pragma: no cover
        return ConversionSource.make_one(self.boto3_raw_data["source"])

    @cached_property
    def target(self):  # pragma: no cover
        return ConversionTarget.make_one(self.boto3_raw_data["target"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestConversionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestConversionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTransformerRequest:
    boto3_raw_data: "type_defs.CreateTransformerRequestTypeDef" = dataclasses.field()

    name = field("name")
    clientToken = field("clientToken")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    fileFormat = field("fileFormat")
    mappingTemplate = field("mappingTemplate")

    @cached_property
    def ediType(self):  # pragma: no cover
        return EdiType.make_one(self.boto3_raw_data["ediType"])

    sampleDocument = field("sampleDocument")
    inputConversion = field("inputConversion")

    @cached_property
    def mapping(self):  # pragma: no cover
        return Mapping.make_one(self.boto3_raw_data["mapping"])

    outputConversion = field("outputConversion")
    sampleDocuments = field("sampleDocuments")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTransformerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTransformerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTransformerRequest:
    boto3_raw_data: "type_defs.UpdateTransformerRequestTypeDef" = dataclasses.field()

    transformerId = field("transformerId")
    name = field("name")
    status = field("status")
    fileFormat = field("fileFormat")
    mappingTemplate = field("mappingTemplate")

    @cached_property
    def ediType(self):  # pragma: no cover
        return EdiType.make_one(self.boto3_raw_data["ediType"])

    sampleDocument = field("sampleDocument")
    inputConversion = field("inputConversion")

    @cached_property
    def mapping(self):  # pragma: no cover
        return Mapping.make_one(self.boto3_raw_data["mapping"])

    outputConversion = field("outputConversion")
    sampleDocuments = field("sampleDocuments")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTransformerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTransformerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
