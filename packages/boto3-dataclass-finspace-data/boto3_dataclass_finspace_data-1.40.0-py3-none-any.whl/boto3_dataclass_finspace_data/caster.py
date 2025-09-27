# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_finspace_data import type_defs as bs_td


class FINSPACE_DATACaster:

    def associate_user_to_permission_group(
        self,
        res: "bs_td.AssociateUserToPermissionGroupResponseTypeDef",
    ) -> "dc_td.AssociateUserToPermissionGroupResponse":
        return dc_td.AssociateUserToPermissionGroupResponse.make_one(res)

    def create_changeset(
        self,
        res: "bs_td.CreateChangesetResponseTypeDef",
    ) -> "dc_td.CreateChangesetResponse":
        return dc_td.CreateChangesetResponse.make_one(res)

    def create_data_view(
        self,
        res: "bs_td.CreateDataViewResponseTypeDef",
    ) -> "dc_td.CreateDataViewResponse":
        return dc_td.CreateDataViewResponse.make_one(res)

    def create_dataset(
        self,
        res: "bs_td.CreateDatasetResponseTypeDef",
    ) -> "dc_td.CreateDatasetResponse":
        return dc_td.CreateDatasetResponse.make_one(res)

    def create_permission_group(
        self,
        res: "bs_td.CreatePermissionGroupResponseTypeDef",
    ) -> "dc_td.CreatePermissionGroupResponse":
        return dc_td.CreatePermissionGroupResponse.make_one(res)

    def create_user(
        self,
        res: "bs_td.CreateUserResponseTypeDef",
    ) -> "dc_td.CreateUserResponse":
        return dc_td.CreateUserResponse.make_one(res)

    def delete_dataset(
        self,
        res: "bs_td.DeleteDatasetResponseTypeDef",
    ) -> "dc_td.DeleteDatasetResponse":
        return dc_td.DeleteDatasetResponse.make_one(res)

    def delete_permission_group(
        self,
        res: "bs_td.DeletePermissionGroupResponseTypeDef",
    ) -> "dc_td.DeletePermissionGroupResponse":
        return dc_td.DeletePermissionGroupResponse.make_one(res)

    def disable_user(
        self,
        res: "bs_td.DisableUserResponseTypeDef",
    ) -> "dc_td.DisableUserResponse":
        return dc_td.DisableUserResponse.make_one(res)

    def disassociate_user_from_permission_group(
        self,
        res: "bs_td.DisassociateUserFromPermissionGroupResponseTypeDef",
    ) -> "dc_td.DisassociateUserFromPermissionGroupResponse":
        return dc_td.DisassociateUserFromPermissionGroupResponse.make_one(res)

    def enable_user(
        self,
        res: "bs_td.EnableUserResponseTypeDef",
    ) -> "dc_td.EnableUserResponse":
        return dc_td.EnableUserResponse.make_one(res)

    def get_changeset(
        self,
        res: "bs_td.GetChangesetResponseTypeDef",
    ) -> "dc_td.GetChangesetResponse":
        return dc_td.GetChangesetResponse.make_one(res)

    def get_data_view(
        self,
        res: "bs_td.GetDataViewResponseTypeDef",
    ) -> "dc_td.GetDataViewResponse":
        return dc_td.GetDataViewResponse.make_one(res)

    def get_dataset(
        self,
        res: "bs_td.GetDatasetResponseTypeDef",
    ) -> "dc_td.GetDatasetResponse":
        return dc_td.GetDatasetResponse.make_one(res)

    def get_external_data_view_access_details(
        self,
        res: "bs_td.GetExternalDataViewAccessDetailsResponseTypeDef",
    ) -> "dc_td.GetExternalDataViewAccessDetailsResponse":
        return dc_td.GetExternalDataViewAccessDetailsResponse.make_one(res)

    def get_permission_group(
        self,
        res: "bs_td.GetPermissionGroupResponseTypeDef",
    ) -> "dc_td.GetPermissionGroupResponse":
        return dc_td.GetPermissionGroupResponse.make_one(res)

    def get_programmatic_access_credentials(
        self,
        res: "bs_td.GetProgrammaticAccessCredentialsResponseTypeDef",
    ) -> "dc_td.GetProgrammaticAccessCredentialsResponse":
        return dc_td.GetProgrammaticAccessCredentialsResponse.make_one(res)

    def get_user(
        self,
        res: "bs_td.GetUserResponseTypeDef",
    ) -> "dc_td.GetUserResponse":
        return dc_td.GetUserResponse.make_one(res)

    def get_working_location(
        self,
        res: "bs_td.GetWorkingLocationResponseTypeDef",
    ) -> "dc_td.GetWorkingLocationResponse":
        return dc_td.GetWorkingLocationResponse.make_one(res)

    def list_changesets(
        self,
        res: "bs_td.ListChangesetsResponseTypeDef",
    ) -> "dc_td.ListChangesetsResponse":
        return dc_td.ListChangesetsResponse.make_one(res)

    def list_data_views(
        self,
        res: "bs_td.ListDataViewsResponseTypeDef",
    ) -> "dc_td.ListDataViewsResponse":
        return dc_td.ListDataViewsResponse.make_one(res)

    def list_datasets(
        self,
        res: "bs_td.ListDatasetsResponseTypeDef",
    ) -> "dc_td.ListDatasetsResponse":
        return dc_td.ListDatasetsResponse.make_one(res)

    def list_permission_groups(
        self,
        res: "bs_td.ListPermissionGroupsResponseTypeDef",
    ) -> "dc_td.ListPermissionGroupsResponse":
        return dc_td.ListPermissionGroupsResponse.make_one(res)

    def list_permission_groups_by_user(
        self,
        res: "bs_td.ListPermissionGroupsByUserResponseTypeDef",
    ) -> "dc_td.ListPermissionGroupsByUserResponse":
        return dc_td.ListPermissionGroupsByUserResponse.make_one(res)

    def list_users(
        self,
        res: "bs_td.ListUsersResponseTypeDef",
    ) -> "dc_td.ListUsersResponse":
        return dc_td.ListUsersResponse.make_one(res)

    def list_users_by_permission_group(
        self,
        res: "bs_td.ListUsersByPermissionGroupResponseTypeDef",
    ) -> "dc_td.ListUsersByPermissionGroupResponse":
        return dc_td.ListUsersByPermissionGroupResponse.make_one(res)

    def reset_user_password(
        self,
        res: "bs_td.ResetUserPasswordResponseTypeDef",
    ) -> "dc_td.ResetUserPasswordResponse":
        return dc_td.ResetUserPasswordResponse.make_one(res)

    def update_changeset(
        self,
        res: "bs_td.UpdateChangesetResponseTypeDef",
    ) -> "dc_td.UpdateChangesetResponse":
        return dc_td.UpdateChangesetResponse.make_one(res)

    def update_dataset(
        self,
        res: "bs_td.UpdateDatasetResponseTypeDef",
    ) -> "dc_td.UpdateDatasetResponse":
        return dc_td.UpdateDatasetResponse.make_one(res)

    def update_permission_group(
        self,
        res: "bs_td.UpdatePermissionGroupResponseTypeDef",
    ) -> "dc_td.UpdatePermissionGroupResponse":
        return dc_td.UpdatePermissionGroupResponse.make_one(res)

    def update_user(
        self,
        res: "bs_td.UpdateUserResponseTypeDef",
    ) -> "dc_td.UpdateUserResponse":
        return dc_td.UpdateUserResponse.make_one(res)


finspace_data_caster = FINSPACE_DATACaster()
