# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_emr_containers import type_defs as bs_td


class EMR_CONTAINERSCaster:

    def cancel_job_run(
        self,
        res: "bs_td.CancelJobRunResponseTypeDef",
    ) -> "dc_td.CancelJobRunResponse":
        return dc_td.CancelJobRunResponse.make_one(res)

    def create_job_template(
        self,
        res: "bs_td.CreateJobTemplateResponseTypeDef",
    ) -> "dc_td.CreateJobTemplateResponse":
        return dc_td.CreateJobTemplateResponse.make_one(res)

    def create_managed_endpoint(
        self,
        res: "bs_td.CreateManagedEndpointResponseTypeDef",
    ) -> "dc_td.CreateManagedEndpointResponse":
        return dc_td.CreateManagedEndpointResponse.make_one(res)

    def create_security_configuration(
        self,
        res: "bs_td.CreateSecurityConfigurationResponseTypeDef",
    ) -> "dc_td.CreateSecurityConfigurationResponse":
        return dc_td.CreateSecurityConfigurationResponse.make_one(res)

    def create_virtual_cluster(
        self,
        res: "bs_td.CreateVirtualClusterResponseTypeDef",
    ) -> "dc_td.CreateVirtualClusterResponse":
        return dc_td.CreateVirtualClusterResponse.make_one(res)

    def delete_job_template(
        self,
        res: "bs_td.DeleteJobTemplateResponseTypeDef",
    ) -> "dc_td.DeleteJobTemplateResponse":
        return dc_td.DeleteJobTemplateResponse.make_one(res)

    def delete_managed_endpoint(
        self,
        res: "bs_td.DeleteManagedEndpointResponseTypeDef",
    ) -> "dc_td.DeleteManagedEndpointResponse":
        return dc_td.DeleteManagedEndpointResponse.make_one(res)

    def delete_virtual_cluster(
        self,
        res: "bs_td.DeleteVirtualClusterResponseTypeDef",
    ) -> "dc_td.DeleteVirtualClusterResponse":
        return dc_td.DeleteVirtualClusterResponse.make_one(res)

    def describe_job_run(
        self,
        res: "bs_td.DescribeJobRunResponseTypeDef",
    ) -> "dc_td.DescribeJobRunResponse":
        return dc_td.DescribeJobRunResponse.make_one(res)

    def describe_job_template(
        self,
        res: "bs_td.DescribeJobTemplateResponseTypeDef",
    ) -> "dc_td.DescribeJobTemplateResponse":
        return dc_td.DescribeJobTemplateResponse.make_one(res)

    def describe_managed_endpoint(
        self,
        res: "bs_td.DescribeManagedEndpointResponseTypeDef",
    ) -> "dc_td.DescribeManagedEndpointResponse":
        return dc_td.DescribeManagedEndpointResponse.make_one(res)

    def describe_security_configuration(
        self,
        res: "bs_td.DescribeSecurityConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeSecurityConfigurationResponse":
        return dc_td.DescribeSecurityConfigurationResponse.make_one(res)

    def describe_virtual_cluster(
        self,
        res: "bs_td.DescribeVirtualClusterResponseTypeDef",
    ) -> "dc_td.DescribeVirtualClusterResponse":
        return dc_td.DescribeVirtualClusterResponse.make_one(res)

    def get_managed_endpoint_session_credentials(
        self,
        res: "bs_td.GetManagedEndpointSessionCredentialsResponseTypeDef",
    ) -> "dc_td.GetManagedEndpointSessionCredentialsResponse":
        return dc_td.GetManagedEndpointSessionCredentialsResponse.make_one(res)

    def list_job_runs(
        self,
        res: "bs_td.ListJobRunsResponseTypeDef",
    ) -> "dc_td.ListJobRunsResponse":
        return dc_td.ListJobRunsResponse.make_one(res)

    def list_job_templates(
        self,
        res: "bs_td.ListJobTemplatesResponseTypeDef",
    ) -> "dc_td.ListJobTemplatesResponse":
        return dc_td.ListJobTemplatesResponse.make_one(res)

    def list_managed_endpoints(
        self,
        res: "bs_td.ListManagedEndpointsResponseTypeDef",
    ) -> "dc_td.ListManagedEndpointsResponse":
        return dc_td.ListManagedEndpointsResponse.make_one(res)

    def list_security_configurations(
        self,
        res: "bs_td.ListSecurityConfigurationsResponseTypeDef",
    ) -> "dc_td.ListSecurityConfigurationsResponse":
        return dc_td.ListSecurityConfigurationsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_virtual_clusters(
        self,
        res: "bs_td.ListVirtualClustersResponseTypeDef",
    ) -> "dc_td.ListVirtualClustersResponse":
        return dc_td.ListVirtualClustersResponse.make_one(res)

    def start_job_run(
        self,
        res: "bs_td.StartJobRunResponseTypeDef",
    ) -> "dc_td.StartJobRunResponse":
        return dc_td.StartJobRunResponse.make_one(res)


emr_containers_caster = EMR_CONTAINERSCaster()
