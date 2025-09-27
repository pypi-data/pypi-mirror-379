# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_codeartifact import type_defs as bs_td


class CODEARTIFACTCaster:

    def associate_external_connection(
        self,
        res: "bs_td.AssociateExternalConnectionResultTypeDef",
    ) -> "dc_td.AssociateExternalConnectionResult":
        return dc_td.AssociateExternalConnectionResult.make_one(res)

    def copy_package_versions(
        self,
        res: "bs_td.CopyPackageVersionsResultTypeDef",
    ) -> "dc_td.CopyPackageVersionsResult":
        return dc_td.CopyPackageVersionsResult.make_one(res)

    def create_domain(
        self,
        res: "bs_td.CreateDomainResultTypeDef",
    ) -> "dc_td.CreateDomainResult":
        return dc_td.CreateDomainResult.make_one(res)

    def create_package_group(
        self,
        res: "bs_td.CreatePackageGroupResultTypeDef",
    ) -> "dc_td.CreatePackageGroupResult":
        return dc_td.CreatePackageGroupResult.make_one(res)

    def create_repository(
        self,
        res: "bs_td.CreateRepositoryResultTypeDef",
    ) -> "dc_td.CreateRepositoryResult":
        return dc_td.CreateRepositoryResult.make_one(res)

    def delete_domain(
        self,
        res: "bs_td.DeleteDomainResultTypeDef",
    ) -> "dc_td.DeleteDomainResult":
        return dc_td.DeleteDomainResult.make_one(res)

    def delete_domain_permissions_policy(
        self,
        res: "bs_td.DeleteDomainPermissionsPolicyResultTypeDef",
    ) -> "dc_td.DeleteDomainPermissionsPolicyResult":
        return dc_td.DeleteDomainPermissionsPolicyResult.make_one(res)

    def delete_package(
        self,
        res: "bs_td.DeletePackageResultTypeDef",
    ) -> "dc_td.DeletePackageResult":
        return dc_td.DeletePackageResult.make_one(res)

    def delete_package_group(
        self,
        res: "bs_td.DeletePackageGroupResultTypeDef",
    ) -> "dc_td.DeletePackageGroupResult":
        return dc_td.DeletePackageGroupResult.make_one(res)

    def delete_package_versions(
        self,
        res: "bs_td.DeletePackageVersionsResultTypeDef",
    ) -> "dc_td.DeletePackageVersionsResult":
        return dc_td.DeletePackageVersionsResult.make_one(res)

    def delete_repository(
        self,
        res: "bs_td.DeleteRepositoryResultTypeDef",
    ) -> "dc_td.DeleteRepositoryResult":
        return dc_td.DeleteRepositoryResult.make_one(res)

    def delete_repository_permissions_policy(
        self,
        res: "bs_td.DeleteRepositoryPermissionsPolicyResultTypeDef",
    ) -> "dc_td.DeleteRepositoryPermissionsPolicyResult":
        return dc_td.DeleteRepositoryPermissionsPolicyResult.make_one(res)

    def describe_domain(
        self,
        res: "bs_td.DescribeDomainResultTypeDef",
    ) -> "dc_td.DescribeDomainResult":
        return dc_td.DescribeDomainResult.make_one(res)

    def describe_package(
        self,
        res: "bs_td.DescribePackageResultTypeDef",
    ) -> "dc_td.DescribePackageResult":
        return dc_td.DescribePackageResult.make_one(res)

    def describe_package_group(
        self,
        res: "bs_td.DescribePackageGroupResultTypeDef",
    ) -> "dc_td.DescribePackageGroupResult":
        return dc_td.DescribePackageGroupResult.make_one(res)

    def describe_package_version(
        self,
        res: "bs_td.DescribePackageVersionResultTypeDef",
    ) -> "dc_td.DescribePackageVersionResult":
        return dc_td.DescribePackageVersionResult.make_one(res)

    def describe_repository(
        self,
        res: "bs_td.DescribeRepositoryResultTypeDef",
    ) -> "dc_td.DescribeRepositoryResult":
        return dc_td.DescribeRepositoryResult.make_one(res)

    def disassociate_external_connection(
        self,
        res: "bs_td.DisassociateExternalConnectionResultTypeDef",
    ) -> "dc_td.DisassociateExternalConnectionResult":
        return dc_td.DisassociateExternalConnectionResult.make_one(res)

    def dispose_package_versions(
        self,
        res: "bs_td.DisposePackageVersionsResultTypeDef",
    ) -> "dc_td.DisposePackageVersionsResult":
        return dc_td.DisposePackageVersionsResult.make_one(res)

    def get_associated_package_group(
        self,
        res: "bs_td.GetAssociatedPackageGroupResultTypeDef",
    ) -> "dc_td.GetAssociatedPackageGroupResult":
        return dc_td.GetAssociatedPackageGroupResult.make_one(res)

    def get_authorization_token(
        self,
        res: "bs_td.GetAuthorizationTokenResultTypeDef",
    ) -> "dc_td.GetAuthorizationTokenResult":
        return dc_td.GetAuthorizationTokenResult.make_one(res)

    def get_domain_permissions_policy(
        self,
        res: "bs_td.GetDomainPermissionsPolicyResultTypeDef",
    ) -> "dc_td.GetDomainPermissionsPolicyResult":
        return dc_td.GetDomainPermissionsPolicyResult.make_one(res)

    def get_package_version_asset(
        self,
        res: "bs_td.GetPackageVersionAssetResultTypeDef",
    ) -> "dc_td.GetPackageVersionAssetResult":
        return dc_td.GetPackageVersionAssetResult.make_one(res)

    def get_package_version_readme(
        self,
        res: "bs_td.GetPackageVersionReadmeResultTypeDef",
    ) -> "dc_td.GetPackageVersionReadmeResult":
        return dc_td.GetPackageVersionReadmeResult.make_one(res)

    def get_repository_endpoint(
        self,
        res: "bs_td.GetRepositoryEndpointResultTypeDef",
    ) -> "dc_td.GetRepositoryEndpointResult":
        return dc_td.GetRepositoryEndpointResult.make_one(res)

    def get_repository_permissions_policy(
        self,
        res: "bs_td.GetRepositoryPermissionsPolicyResultTypeDef",
    ) -> "dc_td.GetRepositoryPermissionsPolicyResult":
        return dc_td.GetRepositoryPermissionsPolicyResult.make_one(res)

    def list_allowed_repositories_for_group(
        self,
        res: "bs_td.ListAllowedRepositoriesForGroupResultTypeDef",
    ) -> "dc_td.ListAllowedRepositoriesForGroupResult":
        return dc_td.ListAllowedRepositoriesForGroupResult.make_one(res)

    def list_associated_packages(
        self,
        res: "bs_td.ListAssociatedPackagesResultTypeDef",
    ) -> "dc_td.ListAssociatedPackagesResult":
        return dc_td.ListAssociatedPackagesResult.make_one(res)

    def list_domains(
        self,
        res: "bs_td.ListDomainsResultTypeDef",
    ) -> "dc_td.ListDomainsResult":
        return dc_td.ListDomainsResult.make_one(res)

    def list_package_groups(
        self,
        res: "bs_td.ListPackageGroupsResultTypeDef",
    ) -> "dc_td.ListPackageGroupsResult":
        return dc_td.ListPackageGroupsResult.make_one(res)

    def list_package_version_assets(
        self,
        res: "bs_td.ListPackageVersionAssetsResultTypeDef",
    ) -> "dc_td.ListPackageVersionAssetsResult":
        return dc_td.ListPackageVersionAssetsResult.make_one(res)

    def list_package_version_dependencies(
        self,
        res: "bs_td.ListPackageVersionDependenciesResultTypeDef",
    ) -> "dc_td.ListPackageVersionDependenciesResult":
        return dc_td.ListPackageVersionDependenciesResult.make_one(res)

    def list_package_versions(
        self,
        res: "bs_td.ListPackageVersionsResultTypeDef",
    ) -> "dc_td.ListPackageVersionsResult":
        return dc_td.ListPackageVersionsResult.make_one(res)

    def list_packages(
        self,
        res: "bs_td.ListPackagesResultTypeDef",
    ) -> "dc_td.ListPackagesResult":
        return dc_td.ListPackagesResult.make_one(res)

    def list_repositories(
        self,
        res: "bs_td.ListRepositoriesResultTypeDef",
    ) -> "dc_td.ListRepositoriesResult":
        return dc_td.ListRepositoriesResult.make_one(res)

    def list_repositories_in_domain(
        self,
        res: "bs_td.ListRepositoriesInDomainResultTypeDef",
    ) -> "dc_td.ListRepositoriesInDomainResult":
        return dc_td.ListRepositoriesInDomainResult.make_one(res)

    def list_sub_package_groups(
        self,
        res: "bs_td.ListSubPackageGroupsResultTypeDef",
    ) -> "dc_td.ListSubPackageGroupsResult":
        return dc_td.ListSubPackageGroupsResult.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResultTypeDef",
    ) -> "dc_td.ListTagsForResourceResult":
        return dc_td.ListTagsForResourceResult.make_one(res)

    def publish_package_version(
        self,
        res: "bs_td.PublishPackageVersionResultTypeDef",
    ) -> "dc_td.PublishPackageVersionResult":
        return dc_td.PublishPackageVersionResult.make_one(res)

    def put_domain_permissions_policy(
        self,
        res: "bs_td.PutDomainPermissionsPolicyResultTypeDef",
    ) -> "dc_td.PutDomainPermissionsPolicyResult":
        return dc_td.PutDomainPermissionsPolicyResult.make_one(res)

    def put_package_origin_configuration(
        self,
        res: "bs_td.PutPackageOriginConfigurationResultTypeDef",
    ) -> "dc_td.PutPackageOriginConfigurationResult":
        return dc_td.PutPackageOriginConfigurationResult.make_one(res)

    def put_repository_permissions_policy(
        self,
        res: "bs_td.PutRepositoryPermissionsPolicyResultTypeDef",
    ) -> "dc_td.PutRepositoryPermissionsPolicyResult":
        return dc_td.PutRepositoryPermissionsPolicyResult.make_one(res)

    def update_package_group(
        self,
        res: "bs_td.UpdatePackageGroupResultTypeDef",
    ) -> "dc_td.UpdatePackageGroupResult":
        return dc_td.UpdatePackageGroupResult.make_one(res)

    def update_package_group_origin_configuration(
        self,
        res: "bs_td.UpdatePackageGroupOriginConfigurationResultTypeDef",
    ) -> "dc_td.UpdatePackageGroupOriginConfigurationResult":
        return dc_td.UpdatePackageGroupOriginConfigurationResult.make_one(res)

    def update_package_versions_status(
        self,
        res: "bs_td.UpdatePackageVersionsStatusResultTypeDef",
    ) -> "dc_td.UpdatePackageVersionsStatusResult":
        return dc_td.UpdatePackageVersionsStatusResult.make_one(res)

    def update_repository(
        self,
        res: "bs_td.UpdateRepositoryResultTypeDef",
    ) -> "dc_td.UpdateRepositoryResult":
        return dc_td.UpdateRepositoryResult.make_one(res)


codeartifact_caster = CODEARTIFACTCaster()
