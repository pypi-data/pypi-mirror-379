# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_ecr_public import type_defs as bs_td


class ECR_PUBLICCaster:

    def batch_check_layer_availability(
        self,
        res: "bs_td.BatchCheckLayerAvailabilityResponseTypeDef",
    ) -> "dc_td.BatchCheckLayerAvailabilityResponse":
        return dc_td.BatchCheckLayerAvailabilityResponse.make_one(res)

    def batch_delete_image(
        self,
        res: "bs_td.BatchDeleteImageResponseTypeDef",
    ) -> "dc_td.BatchDeleteImageResponse":
        return dc_td.BatchDeleteImageResponse.make_one(res)

    def complete_layer_upload(
        self,
        res: "bs_td.CompleteLayerUploadResponseTypeDef",
    ) -> "dc_td.CompleteLayerUploadResponse":
        return dc_td.CompleteLayerUploadResponse.make_one(res)

    def create_repository(
        self,
        res: "bs_td.CreateRepositoryResponseTypeDef",
    ) -> "dc_td.CreateRepositoryResponse":
        return dc_td.CreateRepositoryResponse.make_one(res)

    def delete_repository(
        self,
        res: "bs_td.DeleteRepositoryResponseTypeDef",
    ) -> "dc_td.DeleteRepositoryResponse":
        return dc_td.DeleteRepositoryResponse.make_one(res)

    def delete_repository_policy(
        self,
        res: "bs_td.DeleteRepositoryPolicyResponseTypeDef",
    ) -> "dc_td.DeleteRepositoryPolicyResponse":
        return dc_td.DeleteRepositoryPolicyResponse.make_one(res)

    def describe_image_tags(
        self,
        res: "bs_td.DescribeImageTagsResponseTypeDef",
    ) -> "dc_td.DescribeImageTagsResponse":
        return dc_td.DescribeImageTagsResponse.make_one(res)

    def describe_images(
        self,
        res: "bs_td.DescribeImagesResponseTypeDef",
    ) -> "dc_td.DescribeImagesResponse":
        return dc_td.DescribeImagesResponse.make_one(res)

    def describe_registries(
        self,
        res: "bs_td.DescribeRegistriesResponseTypeDef",
    ) -> "dc_td.DescribeRegistriesResponse":
        return dc_td.DescribeRegistriesResponse.make_one(res)

    def describe_repositories(
        self,
        res: "bs_td.DescribeRepositoriesResponseTypeDef",
    ) -> "dc_td.DescribeRepositoriesResponse":
        return dc_td.DescribeRepositoriesResponse.make_one(res)

    def get_authorization_token(
        self,
        res: "bs_td.GetAuthorizationTokenResponseTypeDef",
    ) -> "dc_td.GetAuthorizationTokenResponse":
        return dc_td.GetAuthorizationTokenResponse.make_one(res)

    def get_registry_catalog_data(
        self,
        res: "bs_td.GetRegistryCatalogDataResponseTypeDef",
    ) -> "dc_td.GetRegistryCatalogDataResponse":
        return dc_td.GetRegistryCatalogDataResponse.make_one(res)

    def get_repository_catalog_data(
        self,
        res: "bs_td.GetRepositoryCatalogDataResponseTypeDef",
    ) -> "dc_td.GetRepositoryCatalogDataResponse":
        return dc_td.GetRepositoryCatalogDataResponse.make_one(res)

    def get_repository_policy(
        self,
        res: "bs_td.GetRepositoryPolicyResponseTypeDef",
    ) -> "dc_td.GetRepositoryPolicyResponse":
        return dc_td.GetRepositoryPolicyResponse.make_one(res)

    def initiate_layer_upload(
        self,
        res: "bs_td.InitiateLayerUploadResponseTypeDef",
    ) -> "dc_td.InitiateLayerUploadResponse":
        return dc_td.InitiateLayerUploadResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def put_image(
        self,
        res: "bs_td.PutImageResponseTypeDef",
    ) -> "dc_td.PutImageResponse":
        return dc_td.PutImageResponse.make_one(res)

    def put_registry_catalog_data(
        self,
        res: "bs_td.PutRegistryCatalogDataResponseTypeDef",
    ) -> "dc_td.PutRegistryCatalogDataResponse":
        return dc_td.PutRegistryCatalogDataResponse.make_one(res)

    def put_repository_catalog_data(
        self,
        res: "bs_td.PutRepositoryCatalogDataResponseTypeDef",
    ) -> "dc_td.PutRepositoryCatalogDataResponse":
        return dc_td.PutRepositoryCatalogDataResponse.make_one(res)

    def set_repository_policy(
        self,
        res: "bs_td.SetRepositoryPolicyResponseTypeDef",
    ) -> "dc_td.SetRepositoryPolicyResponse":
        return dc_td.SetRepositoryPolicyResponse.make_one(res)

    def upload_layer_part(
        self,
        res: "bs_td.UploadLayerPartResponseTypeDef",
    ) -> "dc_td.UploadLayerPartResponse":
        return dc_td.UploadLayerPartResponse.make_one(res)


ecr_public_caster = ECR_PUBLICCaster()
