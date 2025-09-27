# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_amplifybackend import type_defs as bs_td


class AMPLIFYBACKENDCaster:

    def clone_backend(
        self,
        res: "bs_td.CloneBackendResponseTypeDef",
    ) -> "dc_td.CloneBackendResponse":
        return dc_td.CloneBackendResponse.make_one(res)

    def create_backend(
        self,
        res: "bs_td.CreateBackendResponseTypeDef",
    ) -> "dc_td.CreateBackendResponse":
        return dc_td.CreateBackendResponse.make_one(res)

    def create_backend_api(
        self,
        res: "bs_td.CreateBackendAPIResponseTypeDef",
    ) -> "dc_td.CreateBackendAPIResponse":
        return dc_td.CreateBackendAPIResponse.make_one(res)

    def create_backend_auth(
        self,
        res: "bs_td.CreateBackendAuthResponseTypeDef",
    ) -> "dc_td.CreateBackendAuthResponse":
        return dc_td.CreateBackendAuthResponse.make_one(res)

    def create_backend_config(
        self,
        res: "bs_td.CreateBackendConfigResponseTypeDef",
    ) -> "dc_td.CreateBackendConfigResponse":
        return dc_td.CreateBackendConfigResponse.make_one(res)

    def create_backend_storage(
        self,
        res: "bs_td.CreateBackendStorageResponseTypeDef",
    ) -> "dc_td.CreateBackendStorageResponse":
        return dc_td.CreateBackendStorageResponse.make_one(res)

    def create_token(
        self,
        res: "bs_td.CreateTokenResponseTypeDef",
    ) -> "dc_td.CreateTokenResponse":
        return dc_td.CreateTokenResponse.make_one(res)

    def delete_backend(
        self,
        res: "bs_td.DeleteBackendResponseTypeDef",
    ) -> "dc_td.DeleteBackendResponse":
        return dc_td.DeleteBackendResponse.make_one(res)

    def delete_backend_api(
        self,
        res: "bs_td.DeleteBackendAPIResponseTypeDef",
    ) -> "dc_td.DeleteBackendAPIResponse":
        return dc_td.DeleteBackendAPIResponse.make_one(res)

    def delete_backend_auth(
        self,
        res: "bs_td.DeleteBackendAuthResponseTypeDef",
    ) -> "dc_td.DeleteBackendAuthResponse":
        return dc_td.DeleteBackendAuthResponse.make_one(res)

    def delete_backend_storage(
        self,
        res: "bs_td.DeleteBackendStorageResponseTypeDef",
    ) -> "dc_td.DeleteBackendStorageResponse":
        return dc_td.DeleteBackendStorageResponse.make_one(res)

    def delete_token(
        self,
        res: "bs_td.DeleteTokenResponseTypeDef",
    ) -> "dc_td.DeleteTokenResponse":
        return dc_td.DeleteTokenResponse.make_one(res)

    def generate_backend_api_models(
        self,
        res: "bs_td.GenerateBackendAPIModelsResponseTypeDef",
    ) -> "dc_td.GenerateBackendAPIModelsResponse":
        return dc_td.GenerateBackendAPIModelsResponse.make_one(res)

    def get_backend(
        self,
        res: "bs_td.GetBackendResponseTypeDef",
    ) -> "dc_td.GetBackendResponse":
        return dc_td.GetBackendResponse.make_one(res)

    def get_backend_api(
        self,
        res: "bs_td.GetBackendAPIResponseTypeDef",
    ) -> "dc_td.GetBackendAPIResponse":
        return dc_td.GetBackendAPIResponse.make_one(res)

    def get_backend_api_models(
        self,
        res: "bs_td.GetBackendAPIModelsResponseTypeDef",
    ) -> "dc_td.GetBackendAPIModelsResponse":
        return dc_td.GetBackendAPIModelsResponse.make_one(res)

    def get_backend_auth(
        self,
        res: "bs_td.GetBackendAuthResponseTypeDef",
    ) -> "dc_td.GetBackendAuthResponse":
        return dc_td.GetBackendAuthResponse.make_one(res)

    def get_backend_job(
        self,
        res: "bs_td.GetBackendJobResponseTypeDef",
    ) -> "dc_td.GetBackendJobResponse":
        return dc_td.GetBackendJobResponse.make_one(res)

    def get_backend_storage(
        self,
        res: "bs_td.GetBackendStorageResponseTypeDef",
    ) -> "dc_td.GetBackendStorageResponse":
        return dc_td.GetBackendStorageResponse.make_one(res)

    def get_token(
        self,
        res: "bs_td.GetTokenResponseTypeDef",
    ) -> "dc_td.GetTokenResponse":
        return dc_td.GetTokenResponse.make_one(res)

    def import_backend_auth(
        self,
        res: "bs_td.ImportBackendAuthResponseTypeDef",
    ) -> "dc_td.ImportBackendAuthResponse":
        return dc_td.ImportBackendAuthResponse.make_one(res)

    def import_backend_storage(
        self,
        res: "bs_td.ImportBackendStorageResponseTypeDef",
    ) -> "dc_td.ImportBackendStorageResponse":
        return dc_td.ImportBackendStorageResponse.make_one(res)

    def list_backend_jobs(
        self,
        res: "bs_td.ListBackendJobsResponseTypeDef",
    ) -> "dc_td.ListBackendJobsResponse":
        return dc_td.ListBackendJobsResponse.make_one(res)

    def list_s3_buckets(
        self,
        res: "bs_td.ListS3BucketsResponseTypeDef",
    ) -> "dc_td.ListS3BucketsResponse":
        return dc_td.ListS3BucketsResponse.make_one(res)

    def remove_all_backends(
        self,
        res: "bs_td.RemoveAllBackendsResponseTypeDef",
    ) -> "dc_td.RemoveAllBackendsResponse":
        return dc_td.RemoveAllBackendsResponse.make_one(res)

    def remove_backend_config(
        self,
        res: "bs_td.RemoveBackendConfigResponseTypeDef",
    ) -> "dc_td.RemoveBackendConfigResponse":
        return dc_td.RemoveBackendConfigResponse.make_one(res)

    def update_backend_api(
        self,
        res: "bs_td.UpdateBackendAPIResponseTypeDef",
    ) -> "dc_td.UpdateBackendAPIResponse":
        return dc_td.UpdateBackendAPIResponse.make_one(res)

    def update_backend_auth(
        self,
        res: "bs_td.UpdateBackendAuthResponseTypeDef",
    ) -> "dc_td.UpdateBackendAuthResponse":
        return dc_td.UpdateBackendAuthResponse.make_one(res)

    def update_backend_config(
        self,
        res: "bs_td.UpdateBackendConfigResponseTypeDef",
    ) -> "dc_td.UpdateBackendConfigResponse":
        return dc_td.UpdateBackendConfigResponse.make_one(res)

    def update_backend_job(
        self,
        res: "bs_td.UpdateBackendJobResponseTypeDef",
    ) -> "dc_td.UpdateBackendJobResponse":
        return dc_td.UpdateBackendJobResponse.make_one(res)

    def update_backend_storage(
        self,
        res: "bs_td.UpdateBackendStorageResponseTypeDef",
    ) -> "dc_td.UpdateBackendStorageResponse":
        return dc_td.UpdateBackendStorageResponse.make_one(res)


amplifybackend_caster = AMPLIFYBACKENDCaster()
