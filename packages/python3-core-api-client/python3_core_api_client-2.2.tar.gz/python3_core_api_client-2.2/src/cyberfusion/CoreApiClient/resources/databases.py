from cyberfusion.CoreApiClient import models
from typing import Optional, List

from cyberfusion.CoreApiClient.interfaces import Resource
from cyberfusion.CoreApiClient.http import DtoResponse


class Databases(Resource):
    def create_database(
        self,
        request: models.DatabaseCreateRequest,
    ) -> DtoResponse[models.DatabaseResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            "/api/v1/databases",
            data=request.dict(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_response(local_response, models.DatabaseResource)

    def list_databases(
        self,
        *,
        skip: Optional[int] = None,
        limit: Optional[int] = None,
        filter_: Optional[List[str]] = None,
        sort: Optional[List[str]] = None,
    ) -> DtoResponse[list[models.DatabaseResource]]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            "/api/v1/databases",
            data=None,
            query_parameters={
                "skip": skip,
                "limit": limit,
                "filter": filter_,
                "sort": sort,
            },
        )

        return DtoResponse.from_response(local_response, models.DatabaseResource)

    def read_database(
        self,
        *,
        id_: int,
    ) -> DtoResponse[models.DatabaseResource]:
        local_response = self.api_connector.send_or_fail(
            "GET", f"/api/v1/databases/{id_}", data=None, query_parameters={}
        )

        return DtoResponse.from_response(local_response, models.DatabaseResource)

    def update_database(
        self,
        request: models.DatabaseUpdateRequest,
        *,
        id_: int,
    ) -> DtoResponse[models.DatabaseResource]:
        local_response = self.api_connector.send_or_fail(
            "PATCH",
            f"/api/v1/databases/{id_}",
            data=request.dict(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_response(local_response, models.DatabaseResource)

    def delete_database(
        self,
        *,
        id_: int,
        delete_on_cluster: Optional[bool] = None,
    ) -> DtoResponse[models.DetailMessage]:
        local_response = self.api_connector.send_or_fail(
            "DELETE",
            f"/api/v1/databases/{id_}",
            data=None,
            query_parameters={
                "delete_on_cluster": delete_on_cluster,
            },
        )

        return DtoResponse.from_response(local_response, models.DetailMessage)

    def compare_databases(
        self,
        *,
        left_database_id: int,
        right_database_id: int,
    ) -> DtoResponse[models.DatabaseComparison]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/databases/{left_database_id}/comparison",
            data=None,
            query_parameters={
                "right_database_id": right_database_id,
            },
        )

        return DtoResponse.from_response(local_response, models.DatabaseComparison)

    def sync_databases(
        self,
        *,
        left_database_id: int,
        right_database_id: int,
        callback_url: Optional[str] = None,
        exclude_tables_names: Optional[List[str]] = None,
    ) -> DtoResponse[models.TaskCollectionResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            f"/api/v1/databases/{left_database_id}/sync",
            data=None,
            query_parameters={
                "callback_url": callback_url,
                "right_database_id": right_database_id,
                "exclude_tables_names": exclude_tables_names,
            },
        )

        return DtoResponse.from_response(local_response, models.TaskCollectionResource)

    def list_database_usages(
        self,
        *,
        database_id: int,
        timestamp: str,
        time_unit: Optional[models.DatabaseUsageResource] = None,
    ) -> DtoResponse[list[models.DatabaseUsageResource]]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/databases/usages/{database_id}",
            data=None,
            query_parameters={
                "timestamp": timestamp,
                "time_unit": time_unit,
            },
        )

        return DtoResponse.from_response(local_response, models.DatabaseUsageResource)
