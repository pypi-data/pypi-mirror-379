# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_codestar_connections import type_defs as bs_td


class CODESTAR_CONNECTIONSCaster:

    def create_connection(
        self,
        res: "bs_td.CreateConnectionOutputTypeDef",
    ) -> "dc_td.CreateConnectionOutput":
        return dc_td.CreateConnectionOutput.make_one(res)

    def create_host(
        self,
        res: "bs_td.CreateHostOutputTypeDef",
    ) -> "dc_td.CreateHostOutput":
        return dc_td.CreateHostOutput.make_one(res)

    def create_repository_link(
        self,
        res: "bs_td.CreateRepositoryLinkOutputTypeDef",
    ) -> "dc_td.CreateRepositoryLinkOutput":
        return dc_td.CreateRepositoryLinkOutput.make_one(res)

    def create_sync_configuration(
        self,
        res: "bs_td.CreateSyncConfigurationOutputTypeDef",
    ) -> "dc_td.CreateSyncConfigurationOutput":
        return dc_td.CreateSyncConfigurationOutput.make_one(res)

    def get_connection(
        self,
        res: "bs_td.GetConnectionOutputTypeDef",
    ) -> "dc_td.GetConnectionOutput":
        return dc_td.GetConnectionOutput.make_one(res)

    def get_host(
        self,
        res: "bs_td.GetHostOutputTypeDef",
    ) -> "dc_td.GetHostOutput":
        return dc_td.GetHostOutput.make_one(res)

    def get_repository_link(
        self,
        res: "bs_td.GetRepositoryLinkOutputTypeDef",
    ) -> "dc_td.GetRepositoryLinkOutput":
        return dc_td.GetRepositoryLinkOutput.make_one(res)

    def get_repository_sync_status(
        self,
        res: "bs_td.GetRepositorySyncStatusOutputTypeDef",
    ) -> "dc_td.GetRepositorySyncStatusOutput":
        return dc_td.GetRepositorySyncStatusOutput.make_one(res)

    def get_resource_sync_status(
        self,
        res: "bs_td.GetResourceSyncStatusOutputTypeDef",
    ) -> "dc_td.GetResourceSyncStatusOutput":
        return dc_td.GetResourceSyncStatusOutput.make_one(res)

    def get_sync_blocker_summary(
        self,
        res: "bs_td.GetSyncBlockerSummaryOutputTypeDef",
    ) -> "dc_td.GetSyncBlockerSummaryOutput":
        return dc_td.GetSyncBlockerSummaryOutput.make_one(res)

    def get_sync_configuration(
        self,
        res: "bs_td.GetSyncConfigurationOutputTypeDef",
    ) -> "dc_td.GetSyncConfigurationOutput":
        return dc_td.GetSyncConfigurationOutput.make_one(res)

    def list_connections(
        self,
        res: "bs_td.ListConnectionsOutputTypeDef",
    ) -> "dc_td.ListConnectionsOutput":
        return dc_td.ListConnectionsOutput.make_one(res)

    def list_hosts(
        self,
        res: "bs_td.ListHostsOutputTypeDef",
    ) -> "dc_td.ListHostsOutput":
        return dc_td.ListHostsOutput.make_one(res)

    def list_repository_links(
        self,
        res: "bs_td.ListRepositoryLinksOutputTypeDef",
    ) -> "dc_td.ListRepositoryLinksOutput":
        return dc_td.ListRepositoryLinksOutput.make_one(res)

    def list_repository_sync_definitions(
        self,
        res: "bs_td.ListRepositorySyncDefinitionsOutputTypeDef",
    ) -> "dc_td.ListRepositorySyncDefinitionsOutput":
        return dc_td.ListRepositorySyncDefinitionsOutput.make_one(res)

    def list_sync_configurations(
        self,
        res: "bs_td.ListSyncConfigurationsOutputTypeDef",
    ) -> "dc_td.ListSyncConfigurationsOutput":
        return dc_td.ListSyncConfigurationsOutput.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceOutputTypeDef",
    ) -> "dc_td.ListTagsForResourceOutput":
        return dc_td.ListTagsForResourceOutput.make_one(res)

    def update_repository_link(
        self,
        res: "bs_td.UpdateRepositoryLinkOutputTypeDef",
    ) -> "dc_td.UpdateRepositoryLinkOutput":
        return dc_td.UpdateRepositoryLinkOutput.make_one(res)

    def update_sync_blocker(
        self,
        res: "bs_td.UpdateSyncBlockerOutputTypeDef",
    ) -> "dc_td.UpdateSyncBlockerOutput":
        return dc_td.UpdateSyncBlockerOutput.make_one(res)

    def update_sync_configuration(
        self,
        res: "bs_td.UpdateSyncConfigurationOutputTypeDef",
    ) -> "dc_td.UpdateSyncConfigurationOutput":
        return dc_td.UpdateSyncConfigurationOutput.make_one(res)


codestar_connections_caster = CODESTAR_CONNECTIONSCaster()
