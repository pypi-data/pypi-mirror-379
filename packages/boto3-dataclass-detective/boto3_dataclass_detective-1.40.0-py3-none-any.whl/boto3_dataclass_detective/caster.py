# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_detective import type_defs as bs_td


class DETECTIVECaster:

    def accept_invitation(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def batch_get_graph_member_datasources(
        self,
        res: "bs_td.BatchGetGraphMemberDatasourcesResponseTypeDef",
    ) -> "dc_td.BatchGetGraphMemberDatasourcesResponse":
        return dc_td.BatchGetGraphMemberDatasourcesResponse.make_one(res)

    def batch_get_membership_datasources(
        self,
        res: "bs_td.BatchGetMembershipDatasourcesResponseTypeDef",
    ) -> "dc_td.BatchGetMembershipDatasourcesResponse":
        return dc_td.BatchGetMembershipDatasourcesResponse.make_one(res)

    def create_graph(
        self,
        res: "bs_td.CreateGraphResponseTypeDef",
    ) -> "dc_td.CreateGraphResponse":
        return dc_td.CreateGraphResponse.make_one(res)

    def create_members(
        self,
        res: "bs_td.CreateMembersResponseTypeDef",
    ) -> "dc_td.CreateMembersResponse":
        return dc_td.CreateMembersResponse.make_one(res)

    def delete_graph(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_members(
        self,
        res: "bs_td.DeleteMembersResponseTypeDef",
    ) -> "dc_td.DeleteMembersResponse":
        return dc_td.DeleteMembersResponse.make_one(res)

    def describe_organization_configuration(
        self,
        res: "bs_td.DescribeOrganizationConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeOrganizationConfigurationResponse":
        return dc_td.DescribeOrganizationConfigurationResponse.make_one(res)

    def disable_organization_admin_account(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def disassociate_membership(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def enable_organization_admin_account(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def get_investigation(
        self,
        res: "bs_td.GetInvestigationResponseTypeDef",
    ) -> "dc_td.GetInvestigationResponse":
        return dc_td.GetInvestigationResponse.make_one(res)

    def get_members(
        self,
        res: "bs_td.GetMembersResponseTypeDef",
    ) -> "dc_td.GetMembersResponse":
        return dc_td.GetMembersResponse.make_one(res)

    def list_datasource_packages(
        self,
        res: "bs_td.ListDatasourcePackagesResponseTypeDef",
    ) -> "dc_td.ListDatasourcePackagesResponse":
        return dc_td.ListDatasourcePackagesResponse.make_one(res)

    def list_graphs(
        self,
        res: "bs_td.ListGraphsResponseTypeDef",
    ) -> "dc_td.ListGraphsResponse":
        return dc_td.ListGraphsResponse.make_one(res)

    def list_indicators(
        self,
        res: "bs_td.ListIndicatorsResponseTypeDef",
    ) -> "dc_td.ListIndicatorsResponse":
        return dc_td.ListIndicatorsResponse.make_one(res)

    def list_investigations(
        self,
        res: "bs_td.ListInvestigationsResponseTypeDef",
    ) -> "dc_td.ListInvestigationsResponse":
        return dc_td.ListInvestigationsResponse.make_one(res)

    def list_invitations(
        self,
        res: "bs_td.ListInvitationsResponseTypeDef",
    ) -> "dc_td.ListInvitationsResponse":
        return dc_td.ListInvitationsResponse.make_one(res)

    def list_members(
        self,
        res: "bs_td.ListMembersResponseTypeDef",
    ) -> "dc_td.ListMembersResponse":
        return dc_td.ListMembersResponse.make_one(res)

    def list_organization_admin_accounts(
        self,
        res: "bs_td.ListOrganizationAdminAccountsResponseTypeDef",
    ) -> "dc_td.ListOrganizationAdminAccountsResponse":
        return dc_td.ListOrganizationAdminAccountsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def reject_invitation(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def start_investigation(
        self,
        res: "bs_td.StartInvestigationResponseTypeDef",
    ) -> "dc_td.StartInvestigationResponse":
        return dc_td.StartInvestigationResponse.make_one(res)

    def start_monitoring_member(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_datasource_packages(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_investigation_state(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def update_organization_configuration(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


detective_caster = DETECTIVECaster()
