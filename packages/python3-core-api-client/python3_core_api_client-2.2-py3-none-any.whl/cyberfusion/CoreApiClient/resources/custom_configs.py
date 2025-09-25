from cyberfusion.CoreApiClient import models
from typing import Optional, List

from cyberfusion.CoreApiClient.http import DtoResponse
from cyberfusion.CoreApiClient.interfaces import Resource


class CustomConfigs(Resource):
    def create_custom_config(
        self,
        request: models.CustomConfigCreateRequest,
    ) -> DtoResponse[models.CustomConfigResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            "/api/v1/custom-configs",
            data=request.dict(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_response(local_response, models.CustomConfigResource)

    def list_custom_configs(
        self,
        *,
        skip: Optional[int] = None,
        limit: Optional[int] = None,
        filter_: Optional[List[str]] = None,
        sort: Optional[List[str]] = None,
    ) -> DtoResponse[list[models.CustomConfigResource]]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            "/api/v1/custom-configs",
            data=None,
            query_parameters={
                "skip": skip,
                "limit": limit,
                "filter": filter_,
                "sort": sort,
            },
        )

        return DtoResponse.from_response(local_response, models.CustomConfigResource)

    def read_custom_config(
        self,
        *,
        id_: int,
    ) -> DtoResponse[models.CustomConfigResource]:
        local_response = self.api_connector.send_or_fail(
            "GET", f"/api/v1/custom-configs/{id_}", data=None, query_parameters={}
        )

        return DtoResponse.from_response(local_response, models.CustomConfigResource)

    def update_custom_config(
        self,
        request: models.CustomConfigUpdateRequest,
        *,
        id_: int,
    ) -> DtoResponse[models.CustomConfigResource]:
        local_response = self.api_connector.send_or_fail(
            "PATCH",
            f"/api/v1/custom-configs/{id_}",
            data=request.dict(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_response(local_response, models.CustomConfigResource)

    def delete_custom_config(
        self,
        *,
        id_: int,
    ) -> DtoResponse[models.DetailMessage]:
        local_response = self.api_connector.send_or_fail(
            "DELETE",
            f"/api/v1/custom-configs/{id_}",
            data=None,
            query_parameters={},
        )

        return DtoResponse.from_response(local_response, models.DetailMessage)
