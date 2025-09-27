# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_events import type_defs as bs_td


class EVENTSCaster:

    def activate_event_source(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def cancel_replay(
        self,
        res: "bs_td.CancelReplayResponseTypeDef",
    ) -> "dc_td.CancelReplayResponse":
        return dc_td.CancelReplayResponse.make_one(res)

    def create_api_destination(
        self,
        res: "bs_td.CreateApiDestinationResponseTypeDef",
    ) -> "dc_td.CreateApiDestinationResponse":
        return dc_td.CreateApiDestinationResponse.make_one(res)

    def create_archive(
        self,
        res: "bs_td.CreateArchiveResponseTypeDef",
    ) -> "dc_td.CreateArchiveResponse":
        return dc_td.CreateArchiveResponse.make_one(res)

    def create_connection(
        self,
        res: "bs_td.CreateConnectionResponseTypeDef",
    ) -> "dc_td.CreateConnectionResponse":
        return dc_td.CreateConnectionResponse.make_one(res)

    def create_endpoint(
        self,
        res: "bs_td.CreateEndpointResponseTypeDef",
    ) -> "dc_td.CreateEndpointResponse":
        return dc_td.CreateEndpointResponse.make_one(res)

    def create_event_bus(
        self,
        res: "bs_td.CreateEventBusResponseTypeDef",
    ) -> "dc_td.CreateEventBusResponse":
        return dc_td.CreateEventBusResponse.make_one(res)

    def create_partner_event_source(
        self,
        res: "bs_td.CreatePartnerEventSourceResponseTypeDef",
    ) -> "dc_td.CreatePartnerEventSourceResponse":
        return dc_td.CreatePartnerEventSourceResponse.make_one(res)

    def deactivate_event_source(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def deauthorize_connection(
        self,
        res: "bs_td.DeauthorizeConnectionResponseTypeDef",
    ) -> "dc_td.DeauthorizeConnectionResponse":
        return dc_td.DeauthorizeConnectionResponse.make_one(res)

    def delete_connection(
        self,
        res: "bs_td.DeleteConnectionResponseTypeDef",
    ) -> "dc_td.DeleteConnectionResponse":
        return dc_td.DeleteConnectionResponse.make_one(res)

    def delete_event_bus(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_partner_event_source(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def delete_rule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def describe_api_destination(
        self,
        res: "bs_td.DescribeApiDestinationResponseTypeDef",
    ) -> "dc_td.DescribeApiDestinationResponse":
        return dc_td.DescribeApiDestinationResponse.make_one(res)

    def describe_archive(
        self,
        res: "bs_td.DescribeArchiveResponseTypeDef",
    ) -> "dc_td.DescribeArchiveResponse":
        return dc_td.DescribeArchiveResponse.make_one(res)

    def describe_connection(
        self,
        res: "bs_td.DescribeConnectionResponseTypeDef",
    ) -> "dc_td.DescribeConnectionResponse":
        return dc_td.DescribeConnectionResponse.make_one(res)

    def describe_endpoint(
        self,
        res: "bs_td.DescribeEndpointResponseTypeDef",
    ) -> "dc_td.DescribeEndpointResponse":
        return dc_td.DescribeEndpointResponse.make_one(res)

    def describe_event_bus(
        self,
        res: "bs_td.DescribeEventBusResponseTypeDef",
    ) -> "dc_td.DescribeEventBusResponse":
        return dc_td.DescribeEventBusResponse.make_one(res)

    def describe_event_source(
        self,
        res: "bs_td.DescribeEventSourceResponseTypeDef",
    ) -> "dc_td.DescribeEventSourceResponse":
        return dc_td.DescribeEventSourceResponse.make_one(res)

    def describe_partner_event_source(
        self,
        res: "bs_td.DescribePartnerEventSourceResponseTypeDef",
    ) -> "dc_td.DescribePartnerEventSourceResponse":
        return dc_td.DescribePartnerEventSourceResponse.make_one(res)

    def describe_replay(
        self,
        res: "bs_td.DescribeReplayResponseTypeDef",
    ) -> "dc_td.DescribeReplayResponse":
        return dc_td.DescribeReplayResponse.make_one(res)

    def describe_rule(
        self,
        res: "bs_td.DescribeRuleResponseTypeDef",
    ) -> "dc_td.DescribeRuleResponse":
        return dc_td.DescribeRuleResponse.make_one(res)

    def disable_rule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def enable_rule(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def list_api_destinations(
        self,
        res: "bs_td.ListApiDestinationsResponseTypeDef",
    ) -> "dc_td.ListApiDestinationsResponse":
        return dc_td.ListApiDestinationsResponse.make_one(res)

    def list_archives(
        self,
        res: "bs_td.ListArchivesResponseTypeDef",
    ) -> "dc_td.ListArchivesResponse":
        return dc_td.ListArchivesResponse.make_one(res)

    def list_connections(
        self,
        res: "bs_td.ListConnectionsResponseTypeDef",
    ) -> "dc_td.ListConnectionsResponse":
        return dc_td.ListConnectionsResponse.make_one(res)

    def list_endpoints(
        self,
        res: "bs_td.ListEndpointsResponseTypeDef",
    ) -> "dc_td.ListEndpointsResponse":
        return dc_td.ListEndpointsResponse.make_one(res)

    def list_event_buses(
        self,
        res: "bs_td.ListEventBusesResponseTypeDef",
    ) -> "dc_td.ListEventBusesResponse":
        return dc_td.ListEventBusesResponse.make_one(res)

    def list_event_sources(
        self,
        res: "bs_td.ListEventSourcesResponseTypeDef",
    ) -> "dc_td.ListEventSourcesResponse":
        return dc_td.ListEventSourcesResponse.make_one(res)

    def list_partner_event_source_accounts(
        self,
        res: "bs_td.ListPartnerEventSourceAccountsResponseTypeDef",
    ) -> "dc_td.ListPartnerEventSourceAccountsResponse":
        return dc_td.ListPartnerEventSourceAccountsResponse.make_one(res)

    def list_partner_event_sources(
        self,
        res: "bs_td.ListPartnerEventSourcesResponseTypeDef",
    ) -> "dc_td.ListPartnerEventSourcesResponse":
        return dc_td.ListPartnerEventSourcesResponse.make_one(res)

    def list_replays(
        self,
        res: "bs_td.ListReplaysResponseTypeDef",
    ) -> "dc_td.ListReplaysResponse":
        return dc_td.ListReplaysResponse.make_one(res)

    def list_rule_names_by_target(
        self,
        res: "bs_td.ListRuleNamesByTargetResponseTypeDef",
    ) -> "dc_td.ListRuleNamesByTargetResponse":
        return dc_td.ListRuleNamesByTargetResponse.make_one(res)

    def list_rules(
        self,
        res: "bs_td.ListRulesResponseTypeDef",
    ) -> "dc_td.ListRulesResponse":
        return dc_td.ListRulesResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_targets_by_rule(
        self,
        res: "bs_td.ListTargetsByRuleResponseTypeDef",
    ) -> "dc_td.ListTargetsByRuleResponse":
        return dc_td.ListTargetsByRuleResponse.make_one(res)

    def put_events(
        self,
        res: "bs_td.PutEventsResponseTypeDef",
    ) -> "dc_td.PutEventsResponse":
        return dc_td.PutEventsResponse.make_one(res)

    def put_partner_events(
        self,
        res: "bs_td.PutPartnerEventsResponseTypeDef",
    ) -> "dc_td.PutPartnerEventsResponse":
        return dc_td.PutPartnerEventsResponse.make_one(res)

    def put_permission(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def put_rule(
        self,
        res: "bs_td.PutRuleResponseTypeDef",
    ) -> "dc_td.PutRuleResponse":
        return dc_td.PutRuleResponse.make_one(res)

    def put_targets(
        self,
        res: "bs_td.PutTargetsResponseTypeDef",
    ) -> "dc_td.PutTargetsResponse":
        return dc_td.PutTargetsResponse.make_one(res)

    def remove_permission(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def remove_targets(
        self,
        res: "bs_td.RemoveTargetsResponseTypeDef",
    ) -> "dc_td.RemoveTargetsResponse":
        return dc_td.RemoveTargetsResponse.make_one(res)

    def start_replay(
        self,
        res: "bs_td.StartReplayResponseTypeDef",
    ) -> "dc_td.StartReplayResponse":
        return dc_td.StartReplayResponse.make_one(res)

    def test_event_pattern(
        self,
        res: "bs_td.TestEventPatternResponseTypeDef",
    ) -> "dc_td.TestEventPatternResponse":
        return dc_td.TestEventPatternResponse.make_one(res)

    def update_api_destination(
        self,
        res: "bs_td.UpdateApiDestinationResponseTypeDef",
    ) -> "dc_td.UpdateApiDestinationResponse":
        return dc_td.UpdateApiDestinationResponse.make_one(res)

    def update_archive(
        self,
        res: "bs_td.UpdateArchiveResponseTypeDef",
    ) -> "dc_td.UpdateArchiveResponse":
        return dc_td.UpdateArchiveResponse.make_one(res)

    def update_connection(
        self,
        res: "bs_td.UpdateConnectionResponseTypeDef",
    ) -> "dc_td.UpdateConnectionResponse":
        return dc_td.UpdateConnectionResponse.make_one(res)

    def update_endpoint(
        self,
        res: "bs_td.UpdateEndpointResponseTypeDef",
    ) -> "dc_td.UpdateEndpointResponse":
        return dc_td.UpdateEndpointResponse.make_one(res)

    def update_event_bus(
        self,
        res: "bs_td.UpdateEventBusResponseTypeDef",
    ) -> "dc_td.UpdateEventBusResponse":
        return dc_td.UpdateEventBusResponse.make_one(res)


events_caster = EVENTSCaster()
