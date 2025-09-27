from cyberfusion.CoreApiClient import models
from typing import Optional, List

from cyberfusion.CoreApiClient.interfaces import Resource
from cyberfusion.CoreApiClient.http import DtoResponse


class FirewallGroups(Resource):
    def create_firewall_group(
        self,
        request: models.FirewallGroupCreateRequest,
    ) -> DtoResponse[models.FirewallGroupResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            "/api/v1/firewall-groups",
            data=request.dict(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_response(local_response, models.FirewallGroupResource)

    def list_firewall_groups(
        self,
        *,
        skip: Optional[int] = None,
        limit: Optional[int] = None,
        filter_: Optional[List[str]] = None,
        sort: Optional[List[str]] = None,
    ) -> DtoResponse[list[models.FirewallGroupResource]]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            "/api/v1/firewall-groups",
            data=None,
            query_parameters={
                "skip": skip,
                "limit": limit,
                "filter": filter_,
                "sort": sort,
            },
        )

        return DtoResponse.from_response(local_response, models.FirewallGroupResource)

    def read_firewall_group(
        self,
        *,
        id_: int,
    ) -> DtoResponse[models.FirewallGroupResource]:
        local_response = self.api_connector.send_or_fail(
            "GET", f"/api/v1/firewall-groups/{id_}", data=None, query_parameters={}
        )

        return DtoResponse.from_response(local_response, models.FirewallGroupResource)

    def update_firewall_group(
        self,
        request: models.FirewallGroupUpdateRequest,
        *,
        id_: int,
    ) -> DtoResponse[models.FirewallGroupResource]:
        local_response = self.api_connector.send_or_fail(
            "PATCH",
            f"/api/v1/firewall-groups/{id_}",
            data=request.dict(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_response(local_response, models.FirewallGroupResource)

    def delete_firewall_group(
        self,
        *,
        id_: int,
    ) -> DtoResponse[models.DetailMessage]:
        local_response = self.api_connector.send_or_fail(
            "DELETE",
            f"/api/v1/firewall-groups/{id_}",
            data=None,
            query_parameters={},
        )

        return DtoResponse.from_response(local_response, models.DetailMessage)
