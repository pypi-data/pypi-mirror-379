# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_apprunner import type_defs as bs_td


class APPRUNNERCaster:

    def associate_custom_domain(
        self,
        res: "bs_td.AssociateCustomDomainResponseTypeDef",
    ) -> "dc_td.AssociateCustomDomainResponse":
        return dc_td.AssociateCustomDomainResponse.make_one(res)

    def create_auto_scaling_configuration(
        self,
        res: "bs_td.CreateAutoScalingConfigurationResponseTypeDef",
    ) -> "dc_td.CreateAutoScalingConfigurationResponse":
        return dc_td.CreateAutoScalingConfigurationResponse.make_one(res)

    def create_connection(
        self,
        res: "bs_td.CreateConnectionResponseTypeDef",
    ) -> "dc_td.CreateConnectionResponse":
        return dc_td.CreateConnectionResponse.make_one(res)

    def create_observability_configuration(
        self,
        res: "bs_td.CreateObservabilityConfigurationResponseTypeDef",
    ) -> "dc_td.CreateObservabilityConfigurationResponse":
        return dc_td.CreateObservabilityConfigurationResponse.make_one(res)

    def create_service(
        self,
        res: "bs_td.CreateServiceResponseTypeDef",
    ) -> "dc_td.CreateServiceResponse":
        return dc_td.CreateServiceResponse.make_one(res)

    def create_vpc_connector(
        self,
        res: "bs_td.CreateVpcConnectorResponseTypeDef",
    ) -> "dc_td.CreateVpcConnectorResponse":
        return dc_td.CreateVpcConnectorResponse.make_one(res)

    def create_vpc_ingress_connection(
        self,
        res: "bs_td.CreateVpcIngressConnectionResponseTypeDef",
    ) -> "dc_td.CreateVpcIngressConnectionResponse":
        return dc_td.CreateVpcIngressConnectionResponse.make_one(res)

    def delete_auto_scaling_configuration(
        self,
        res: "bs_td.DeleteAutoScalingConfigurationResponseTypeDef",
    ) -> "dc_td.DeleteAutoScalingConfigurationResponse":
        return dc_td.DeleteAutoScalingConfigurationResponse.make_one(res)

    def delete_connection(
        self,
        res: "bs_td.DeleteConnectionResponseTypeDef",
    ) -> "dc_td.DeleteConnectionResponse":
        return dc_td.DeleteConnectionResponse.make_one(res)

    def delete_observability_configuration(
        self,
        res: "bs_td.DeleteObservabilityConfigurationResponseTypeDef",
    ) -> "dc_td.DeleteObservabilityConfigurationResponse":
        return dc_td.DeleteObservabilityConfigurationResponse.make_one(res)

    def delete_service(
        self,
        res: "bs_td.DeleteServiceResponseTypeDef",
    ) -> "dc_td.DeleteServiceResponse":
        return dc_td.DeleteServiceResponse.make_one(res)

    def delete_vpc_connector(
        self,
        res: "bs_td.DeleteVpcConnectorResponseTypeDef",
    ) -> "dc_td.DeleteVpcConnectorResponse":
        return dc_td.DeleteVpcConnectorResponse.make_one(res)

    def delete_vpc_ingress_connection(
        self,
        res: "bs_td.DeleteVpcIngressConnectionResponseTypeDef",
    ) -> "dc_td.DeleteVpcIngressConnectionResponse":
        return dc_td.DeleteVpcIngressConnectionResponse.make_one(res)

    def describe_auto_scaling_configuration(
        self,
        res: "bs_td.DescribeAutoScalingConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeAutoScalingConfigurationResponse":
        return dc_td.DescribeAutoScalingConfigurationResponse.make_one(res)

    def describe_custom_domains(
        self,
        res: "bs_td.DescribeCustomDomainsResponseTypeDef",
    ) -> "dc_td.DescribeCustomDomainsResponse":
        return dc_td.DescribeCustomDomainsResponse.make_one(res)

    def describe_observability_configuration(
        self,
        res: "bs_td.DescribeObservabilityConfigurationResponseTypeDef",
    ) -> "dc_td.DescribeObservabilityConfigurationResponse":
        return dc_td.DescribeObservabilityConfigurationResponse.make_one(res)

    def describe_service(
        self,
        res: "bs_td.DescribeServiceResponseTypeDef",
    ) -> "dc_td.DescribeServiceResponse":
        return dc_td.DescribeServiceResponse.make_one(res)

    def describe_vpc_connector(
        self,
        res: "bs_td.DescribeVpcConnectorResponseTypeDef",
    ) -> "dc_td.DescribeVpcConnectorResponse":
        return dc_td.DescribeVpcConnectorResponse.make_one(res)

    def describe_vpc_ingress_connection(
        self,
        res: "bs_td.DescribeVpcIngressConnectionResponseTypeDef",
    ) -> "dc_td.DescribeVpcIngressConnectionResponse":
        return dc_td.DescribeVpcIngressConnectionResponse.make_one(res)

    def disassociate_custom_domain(
        self,
        res: "bs_td.DisassociateCustomDomainResponseTypeDef",
    ) -> "dc_td.DisassociateCustomDomainResponse":
        return dc_td.DisassociateCustomDomainResponse.make_one(res)

    def list_auto_scaling_configurations(
        self,
        res: "bs_td.ListAutoScalingConfigurationsResponseTypeDef",
    ) -> "dc_td.ListAutoScalingConfigurationsResponse":
        return dc_td.ListAutoScalingConfigurationsResponse.make_one(res)

    def list_connections(
        self,
        res: "bs_td.ListConnectionsResponseTypeDef",
    ) -> "dc_td.ListConnectionsResponse":
        return dc_td.ListConnectionsResponse.make_one(res)

    def list_observability_configurations(
        self,
        res: "bs_td.ListObservabilityConfigurationsResponseTypeDef",
    ) -> "dc_td.ListObservabilityConfigurationsResponse":
        return dc_td.ListObservabilityConfigurationsResponse.make_one(res)

    def list_operations(
        self,
        res: "bs_td.ListOperationsResponseTypeDef",
    ) -> "dc_td.ListOperationsResponse":
        return dc_td.ListOperationsResponse.make_one(res)

    def list_services(
        self,
        res: "bs_td.ListServicesResponseTypeDef",
    ) -> "dc_td.ListServicesResponse":
        return dc_td.ListServicesResponse.make_one(res)

    def list_services_for_auto_scaling_configuration(
        self,
        res: "bs_td.ListServicesForAutoScalingConfigurationResponseTypeDef",
    ) -> "dc_td.ListServicesForAutoScalingConfigurationResponse":
        return dc_td.ListServicesForAutoScalingConfigurationResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_vpc_connectors(
        self,
        res: "bs_td.ListVpcConnectorsResponseTypeDef",
    ) -> "dc_td.ListVpcConnectorsResponse":
        return dc_td.ListVpcConnectorsResponse.make_one(res)

    def list_vpc_ingress_connections(
        self,
        res: "bs_td.ListVpcIngressConnectionsResponseTypeDef",
    ) -> "dc_td.ListVpcIngressConnectionsResponse":
        return dc_td.ListVpcIngressConnectionsResponse.make_one(res)

    def pause_service(
        self,
        res: "bs_td.PauseServiceResponseTypeDef",
    ) -> "dc_td.PauseServiceResponse":
        return dc_td.PauseServiceResponse.make_one(res)

    def resume_service(
        self,
        res: "bs_td.ResumeServiceResponseTypeDef",
    ) -> "dc_td.ResumeServiceResponse":
        return dc_td.ResumeServiceResponse.make_one(res)

    def start_deployment(
        self,
        res: "bs_td.StartDeploymentResponseTypeDef",
    ) -> "dc_td.StartDeploymentResponse":
        return dc_td.StartDeploymentResponse.make_one(res)

    def update_default_auto_scaling_configuration(
        self,
        res: "bs_td.UpdateDefaultAutoScalingConfigurationResponseTypeDef",
    ) -> "dc_td.UpdateDefaultAutoScalingConfigurationResponse":
        return dc_td.UpdateDefaultAutoScalingConfigurationResponse.make_one(res)

    def update_service(
        self,
        res: "bs_td.UpdateServiceResponseTypeDef",
    ) -> "dc_td.UpdateServiceResponse":
        return dc_td.UpdateServiceResponse.make_one(res)

    def update_vpc_ingress_connection(
        self,
        res: "bs_td.UpdateVpcIngressConnectionResponseTypeDef",
    ) -> "dc_td.UpdateVpcIngressConnectionResponse":
        return dc_td.UpdateVpcIngressConnectionResponse.make_one(res)


apprunner_caster = APPRUNNERCaster()
