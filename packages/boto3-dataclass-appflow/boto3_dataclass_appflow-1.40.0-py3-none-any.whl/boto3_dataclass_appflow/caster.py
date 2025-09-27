# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_appflow import type_defs as bs_td


class APPFLOWCaster:

    def cancel_flow_executions(
        self,
        res: "bs_td.CancelFlowExecutionsResponseTypeDef",
    ) -> "dc_td.CancelFlowExecutionsResponse":
        return dc_td.CancelFlowExecutionsResponse.make_one(res)

    def create_connector_profile(
        self,
        res: "bs_td.CreateConnectorProfileResponseTypeDef",
    ) -> "dc_td.CreateConnectorProfileResponse":
        return dc_td.CreateConnectorProfileResponse.make_one(res)

    def create_flow(
        self,
        res: "bs_td.CreateFlowResponseTypeDef",
    ) -> "dc_td.CreateFlowResponse":
        return dc_td.CreateFlowResponse.make_one(res)

    def describe_connector(
        self,
        res: "bs_td.DescribeConnectorResponseTypeDef",
    ) -> "dc_td.DescribeConnectorResponse":
        return dc_td.DescribeConnectorResponse.make_one(res)

    def describe_connector_entity(
        self,
        res: "bs_td.DescribeConnectorEntityResponseTypeDef",
    ) -> "dc_td.DescribeConnectorEntityResponse":
        return dc_td.DescribeConnectorEntityResponse.make_one(res)

    def describe_connector_profiles(
        self,
        res: "bs_td.DescribeConnectorProfilesResponseTypeDef",
    ) -> "dc_td.DescribeConnectorProfilesResponse":
        return dc_td.DescribeConnectorProfilesResponse.make_one(res)

    def describe_connectors(
        self,
        res: "bs_td.DescribeConnectorsResponseTypeDef",
    ) -> "dc_td.DescribeConnectorsResponse":
        return dc_td.DescribeConnectorsResponse.make_one(res)

    def describe_flow(
        self,
        res: "bs_td.DescribeFlowResponseTypeDef",
    ) -> "dc_td.DescribeFlowResponse":
        return dc_td.DescribeFlowResponse.make_one(res)

    def describe_flow_execution_records(
        self,
        res: "bs_td.DescribeFlowExecutionRecordsResponseTypeDef",
    ) -> "dc_td.DescribeFlowExecutionRecordsResponse":
        return dc_td.DescribeFlowExecutionRecordsResponse.make_one(res)

    def list_connector_entities(
        self,
        res: "bs_td.ListConnectorEntitiesResponseTypeDef",
    ) -> "dc_td.ListConnectorEntitiesResponse":
        return dc_td.ListConnectorEntitiesResponse.make_one(res)

    def list_connectors(
        self,
        res: "bs_td.ListConnectorsResponseTypeDef",
    ) -> "dc_td.ListConnectorsResponse":
        return dc_td.ListConnectorsResponse.make_one(res)

    def list_flows(
        self,
        res: "bs_td.ListFlowsResponseTypeDef",
    ) -> "dc_td.ListFlowsResponse":
        return dc_td.ListFlowsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def register_connector(
        self,
        res: "bs_td.RegisterConnectorResponseTypeDef",
    ) -> "dc_td.RegisterConnectorResponse":
        return dc_td.RegisterConnectorResponse.make_one(res)

    def start_flow(
        self,
        res: "bs_td.StartFlowResponseTypeDef",
    ) -> "dc_td.StartFlowResponse":
        return dc_td.StartFlowResponse.make_one(res)

    def stop_flow(
        self,
        res: "bs_td.StopFlowResponseTypeDef",
    ) -> "dc_td.StopFlowResponse":
        return dc_td.StopFlowResponse.make_one(res)

    def update_connector_profile(
        self,
        res: "bs_td.UpdateConnectorProfileResponseTypeDef",
    ) -> "dc_td.UpdateConnectorProfileResponse":
        return dc_td.UpdateConnectorProfileResponse.make_one(res)

    def update_connector_registration(
        self,
        res: "bs_td.UpdateConnectorRegistrationResponseTypeDef",
    ) -> "dc_td.UpdateConnectorRegistrationResponse":
        return dc_td.UpdateConnectorRegistrationResponse.make_one(res)

    def update_flow(
        self,
        res: "bs_td.UpdateFlowResponseTypeDef",
    ) -> "dc_td.UpdateFlowResponse":
        return dc_td.UpdateFlowResponse.make_one(res)


appflow_caster = APPFLOWCaster()
