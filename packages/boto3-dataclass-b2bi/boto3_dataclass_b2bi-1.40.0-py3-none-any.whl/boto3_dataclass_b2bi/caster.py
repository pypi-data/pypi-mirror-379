# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_b2bi import type_defs as bs_td


class B2BICaster:

    def create_capability(
        self,
        res: "bs_td.CreateCapabilityResponseTypeDef",
    ) -> "dc_td.CreateCapabilityResponse":
        return dc_td.CreateCapabilityResponse.make_one(res)

    def create_partnership(
        self,
        res: "bs_td.CreatePartnershipResponseTypeDef",
    ) -> "dc_td.CreatePartnershipResponse":
        return dc_td.CreatePartnershipResponse.make_one(res)

    def create_profile(
        self,
        res: "bs_td.CreateProfileResponseTypeDef",
    ) -> "dc_td.CreateProfileResponse":
        return dc_td.CreateProfileResponse.make_one(res)

    def create_starter_mapping_template(
        self,
        res: "bs_td.CreateStarterMappingTemplateResponseTypeDef",
    ) -> "dc_td.CreateStarterMappingTemplateResponse":
        return dc_td.CreateStarterMappingTemplateResponse.make_one(res)

    def create_transformer(
        self,
        res: "bs_td.CreateTransformerResponseTypeDef",
    ) -> "dc_td.CreateTransformerResponse":
        return dc_td.CreateTransformerResponse.make_one(res)

    def delete_capability(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_partnership(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_profile(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_transformer(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def generate_mapping(
        self,
        res: "bs_td.GenerateMappingResponseTypeDef",
    ) -> "dc_td.GenerateMappingResponse":
        return dc_td.GenerateMappingResponse.make_one(res)

    def get_capability(
        self,
        res: "bs_td.GetCapabilityResponseTypeDef",
    ) -> "dc_td.GetCapabilityResponse":
        return dc_td.GetCapabilityResponse.make_one(res)

    def get_partnership(
        self,
        res: "bs_td.GetPartnershipResponseTypeDef",
    ) -> "dc_td.GetPartnershipResponse":
        return dc_td.GetPartnershipResponse.make_one(res)

    def get_profile(
        self,
        res: "bs_td.GetProfileResponseTypeDef",
    ) -> "dc_td.GetProfileResponse":
        return dc_td.GetProfileResponse.make_one(res)

    def get_transformer(
        self,
        res: "bs_td.GetTransformerResponseTypeDef",
    ) -> "dc_td.GetTransformerResponse":
        return dc_td.GetTransformerResponse.make_one(res)

    def get_transformer_job(
        self,
        res: "bs_td.GetTransformerJobResponseTypeDef",
    ) -> "dc_td.GetTransformerJobResponse":
        return dc_td.GetTransformerJobResponse.make_one(res)

    def list_capabilities(
        self,
        res: "bs_td.ListCapabilitiesResponseTypeDef",
    ) -> "dc_td.ListCapabilitiesResponse":
        return dc_td.ListCapabilitiesResponse.make_one(res)

    def list_partnerships(
        self,
        res: "bs_td.ListPartnershipsResponseTypeDef",
    ) -> "dc_td.ListPartnershipsResponse":
        return dc_td.ListPartnershipsResponse.make_one(res)

    def list_profiles(
        self,
        res: "bs_td.ListProfilesResponseTypeDef",
    ) -> "dc_td.ListProfilesResponse":
        return dc_td.ListProfilesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_transformers(
        self,
        res: "bs_td.ListTransformersResponseTypeDef",
    ) -> "dc_td.ListTransformersResponse":
        return dc_td.ListTransformersResponse.make_one(res)

    def start_transformer_job(
        self,
        res: "bs_td.StartTransformerJobResponseTypeDef",
    ) -> "dc_td.StartTransformerJobResponse":
        return dc_td.StartTransformerJobResponse.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def test_conversion(
        self,
        res: "bs_td.TestConversionResponseTypeDef",
    ) -> "dc_td.TestConversionResponse":
        return dc_td.TestConversionResponse.make_one(res)

    def test_mapping(
        self,
        res: "bs_td.TestMappingResponseTypeDef",
    ) -> "dc_td.TestMappingResponse":
        return dc_td.TestMappingResponse.make_one(res)

    def test_parsing(
        self,
        res: "bs_td.TestParsingResponseTypeDef",
    ) -> "dc_td.TestParsingResponse":
        return dc_td.TestParsingResponse.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_capability(
        self,
        res: "bs_td.UpdateCapabilityResponseTypeDef",
    ) -> "dc_td.UpdateCapabilityResponse":
        return dc_td.UpdateCapabilityResponse.make_one(res)

    def update_partnership(
        self,
        res: "bs_td.UpdatePartnershipResponseTypeDef",
    ) -> "dc_td.UpdatePartnershipResponse":
        return dc_td.UpdatePartnershipResponse.make_one(res)

    def update_profile(
        self,
        res: "bs_td.UpdateProfileResponseTypeDef",
    ) -> "dc_td.UpdateProfileResponse":
        return dc_td.UpdateProfileResponse.make_one(res)

    def update_transformer(
        self,
        res: "bs_td.UpdateTransformerResponseTypeDef",
    ) -> "dc_td.UpdateTransformerResponse":
        return dc_td.UpdateTransformerResponse.make_one(res)


b2bi_caster = B2BICaster()
