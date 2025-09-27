# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_route53 import type_defs as bs_td


class ROUTE53Caster:

    def activate_key_signing_key(
        self,
        res: "bs_td.ActivateKeySigningKeyResponseTypeDef",
    ) -> "dc_td.ActivateKeySigningKeyResponse":
        return dc_td.ActivateKeySigningKeyResponse.make_one(res)

    def associate_vpc_with_hosted_zone(
        self,
        res: "bs_td.AssociateVPCWithHostedZoneResponseTypeDef",
    ) -> "dc_td.AssociateVPCWithHostedZoneResponse":
        return dc_td.AssociateVPCWithHostedZoneResponse.make_one(res)

    def change_cidr_collection(
        self,
        res: "bs_td.ChangeCidrCollectionResponseTypeDef",
    ) -> "dc_td.ChangeCidrCollectionResponse":
        return dc_td.ChangeCidrCollectionResponse.make_one(res)

    def change_resource_record_sets(
        self,
        res: "bs_td.ChangeResourceRecordSetsResponseTypeDef",
    ) -> "dc_td.ChangeResourceRecordSetsResponse":
        return dc_td.ChangeResourceRecordSetsResponse.make_one(res)

    def create_cidr_collection(
        self,
        res: "bs_td.CreateCidrCollectionResponseTypeDef",
    ) -> "dc_td.CreateCidrCollectionResponse":
        return dc_td.CreateCidrCollectionResponse.make_one(res)

    def create_health_check(
        self,
        res: "bs_td.CreateHealthCheckResponseTypeDef",
    ) -> "dc_td.CreateHealthCheckResponse":
        return dc_td.CreateHealthCheckResponse.make_one(res)

    def create_hosted_zone(
        self,
        res: "bs_td.CreateHostedZoneResponseTypeDef",
    ) -> "dc_td.CreateHostedZoneResponse":
        return dc_td.CreateHostedZoneResponse.make_one(res)

    def create_key_signing_key(
        self,
        res: "bs_td.CreateKeySigningKeyResponseTypeDef",
    ) -> "dc_td.CreateKeySigningKeyResponse":
        return dc_td.CreateKeySigningKeyResponse.make_one(res)

    def create_query_logging_config(
        self,
        res: "bs_td.CreateQueryLoggingConfigResponseTypeDef",
    ) -> "dc_td.CreateQueryLoggingConfigResponse":
        return dc_td.CreateQueryLoggingConfigResponse.make_one(res)

    def create_reusable_delegation_set(
        self,
        res: "bs_td.CreateReusableDelegationSetResponseTypeDef",
    ) -> "dc_td.CreateReusableDelegationSetResponse":
        return dc_td.CreateReusableDelegationSetResponse.make_one(res)

    def create_traffic_policy(
        self,
        res: "bs_td.CreateTrafficPolicyResponseTypeDef",
    ) -> "dc_td.CreateTrafficPolicyResponse":
        return dc_td.CreateTrafficPolicyResponse.make_one(res)

    def create_traffic_policy_instance(
        self,
        res: "bs_td.CreateTrafficPolicyInstanceResponseTypeDef",
    ) -> "dc_td.CreateTrafficPolicyInstanceResponse":
        return dc_td.CreateTrafficPolicyInstanceResponse.make_one(res)

    def create_traffic_policy_version(
        self,
        res: "bs_td.CreateTrafficPolicyVersionResponseTypeDef",
    ) -> "dc_td.CreateTrafficPolicyVersionResponse":
        return dc_td.CreateTrafficPolicyVersionResponse.make_one(res)

    def create_vpc_association_authorization(
        self,
        res: "bs_td.CreateVPCAssociationAuthorizationResponseTypeDef",
    ) -> "dc_td.CreateVPCAssociationAuthorizationResponse":
        return dc_td.CreateVPCAssociationAuthorizationResponse.make_one(res)

    def deactivate_key_signing_key(
        self,
        res: "bs_td.DeactivateKeySigningKeyResponseTypeDef",
    ) -> "dc_td.DeactivateKeySigningKeyResponse":
        return dc_td.DeactivateKeySigningKeyResponse.make_one(res)

    def delete_hosted_zone(
        self,
        res: "bs_td.DeleteHostedZoneResponseTypeDef",
    ) -> "dc_td.DeleteHostedZoneResponse":
        return dc_td.DeleteHostedZoneResponse.make_one(res)

    def delete_key_signing_key(
        self,
        res: "bs_td.DeleteKeySigningKeyResponseTypeDef",
    ) -> "dc_td.DeleteKeySigningKeyResponse":
        return dc_td.DeleteKeySigningKeyResponse.make_one(res)

    def disable_hosted_zone_dnssec(
        self,
        res: "bs_td.DisableHostedZoneDNSSECResponseTypeDef",
    ) -> "dc_td.DisableHostedZoneDNSSECResponse":
        return dc_td.DisableHostedZoneDNSSECResponse.make_one(res)

    def disassociate_vpc_from_hosted_zone(
        self,
        res: "bs_td.DisassociateVPCFromHostedZoneResponseTypeDef",
    ) -> "dc_td.DisassociateVPCFromHostedZoneResponse":
        return dc_td.DisassociateVPCFromHostedZoneResponse.make_one(res)

    def enable_hosted_zone_dnssec(
        self,
        res: "bs_td.EnableHostedZoneDNSSECResponseTypeDef",
    ) -> "dc_td.EnableHostedZoneDNSSECResponse":
        return dc_td.EnableHostedZoneDNSSECResponse.make_one(res)

    def get_account_limit(
        self,
        res: "bs_td.GetAccountLimitResponseTypeDef",
    ) -> "dc_td.GetAccountLimitResponse":
        return dc_td.GetAccountLimitResponse.make_one(res)

    def get_change(
        self,
        res: "bs_td.GetChangeResponseTypeDef",
    ) -> "dc_td.GetChangeResponse":
        return dc_td.GetChangeResponse.make_one(res)

    def get_checker_ip_ranges(
        self,
        res: "bs_td.GetCheckerIpRangesResponseTypeDef",
    ) -> "dc_td.GetCheckerIpRangesResponse":
        return dc_td.GetCheckerIpRangesResponse.make_one(res)

    def get_dnssec(
        self,
        res: "bs_td.GetDNSSECResponseTypeDef",
    ) -> "dc_td.GetDNSSECResponse":
        return dc_td.GetDNSSECResponse.make_one(res)

    def get_geo_location(
        self,
        res: "bs_td.GetGeoLocationResponseTypeDef",
    ) -> "dc_td.GetGeoLocationResponse":
        return dc_td.GetGeoLocationResponse.make_one(res)

    def get_health_check(
        self,
        res: "bs_td.GetHealthCheckResponseTypeDef",
    ) -> "dc_td.GetHealthCheckResponse":
        return dc_td.GetHealthCheckResponse.make_one(res)

    def get_health_check_count(
        self,
        res: "bs_td.GetHealthCheckCountResponseTypeDef",
    ) -> "dc_td.GetHealthCheckCountResponse":
        return dc_td.GetHealthCheckCountResponse.make_one(res)

    def get_health_check_last_failure_reason(
        self,
        res: "bs_td.GetHealthCheckLastFailureReasonResponseTypeDef",
    ) -> "dc_td.GetHealthCheckLastFailureReasonResponse":
        return dc_td.GetHealthCheckLastFailureReasonResponse.make_one(res)

    def get_health_check_status(
        self,
        res: "bs_td.GetHealthCheckStatusResponseTypeDef",
    ) -> "dc_td.GetHealthCheckStatusResponse":
        return dc_td.GetHealthCheckStatusResponse.make_one(res)

    def get_hosted_zone(
        self,
        res: "bs_td.GetHostedZoneResponseTypeDef",
    ) -> "dc_td.GetHostedZoneResponse":
        return dc_td.GetHostedZoneResponse.make_one(res)

    def get_hosted_zone_count(
        self,
        res: "bs_td.GetHostedZoneCountResponseTypeDef",
    ) -> "dc_td.GetHostedZoneCountResponse":
        return dc_td.GetHostedZoneCountResponse.make_one(res)

    def get_hosted_zone_limit(
        self,
        res: "bs_td.GetHostedZoneLimitResponseTypeDef",
    ) -> "dc_td.GetHostedZoneLimitResponse":
        return dc_td.GetHostedZoneLimitResponse.make_one(res)

    def get_query_logging_config(
        self,
        res: "bs_td.GetQueryLoggingConfigResponseTypeDef",
    ) -> "dc_td.GetQueryLoggingConfigResponse":
        return dc_td.GetQueryLoggingConfigResponse.make_one(res)

    def get_reusable_delegation_set(
        self,
        res: "bs_td.GetReusableDelegationSetResponseTypeDef",
    ) -> "dc_td.GetReusableDelegationSetResponse":
        return dc_td.GetReusableDelegationSetResponse.make_one(res)

    def get_reusable_delegation_set_limit(
        self,
        res: "bs_td.GetReusableDelegationSetLimitResponseTypeDef",
    ) -> "dc_td.GetReusableDelegationSetLimitResponse":
        return dc_td.GetReusableDelegationSetLimitResponse.make_one(res)

    def get_traffic_policy(
        self,
        res: "bs_td.GetTrafficPolicyResponseTypeDef",
    ) -> "dc_td.GetTrafficPolicyResponse":
        return dc_td.GetTrafficPolicyResponse.make_one(res)

    def get_traffic_policy_instance(
        self,
        res: "bs_td.GetTrafficPolicyInstanceResponseTypeDef",
    ) -> "dc_td.GetTrafficPolicyInstanceResponse":
        return dc_td.GetTrafficPolicyInstanceResponse.make_one(res)

    def get_traffic_policy_instance_count(
        self,
        res: "bs_td.GetTrafficPolicyInstanceCountResponseTypeDef",
    ) -> "dc_td.GetTrafficPolicyInstanceCountResponse":
        return dc_td.GetTrafficPolicyInstanceCountResponse.make_one(res)

    def list_cidr_blocks(
        self,
        res: "bs_td.ListCidrBlocksResponseTypeDef",
    ) -> "dc_td.ListCidrBlocksResponse":
        return dc_td.ListCidrBlocksResponse.make_one(res)

    def list_cidr_collections(
        self,
        res: "bs_td.ListCidrCollectionsResponseTypeDef",
    ) -> "dc_td.ListCidrCollectionsResponse":
        return dc_td.ListCidrCollectionsResponse.make_one(res)

    def list_cidr_locations(
        self,
        res: "bs_td.ListCidrLocationsResponseTypeDef",
    ) -> "dc_td.ListCidrLocationsResponse":
        return dc_td.ListCidrLocationsResponse.make_one(res)

    def list_geo_locations(
        self,
        res: "bs_td.ListGeoLocationsResponseTypeDef",
    ) -> "dc_td.ListGeoLocationsResponse":
        return dc_td.ListGeoLocationsResponse.make_one(res)

    def list_health_checks(
        self,
        res: "bs_td.ListHealthChecksResponseTypeDef",
    ) -> "dc_td.ListHealthChecksResponse":
        return dc_td.ListHealthChecksResponse.make_one(res)

    def list_hosted_zones(
        self,
        res: "bs_td.ListHostedZonesResponseTypeDef",
    ) -> "dc_td.ListHostedZonesResponse":
        return dc_td.ListHostedZonesResponse.make_one(res)

    def list_hosted_zones_by_name(
        self,
        res: "bs_td.ListHostedZonesByNameResponseTypeDef",
    ) -> "dc_td.ListHostedZonesByNameResponse":
        return dc_td.ListHostedZonesByNameResponse.make_one(res)

    def list_hosted_zones_by_vpc(
        self,
        res: "bs_td.ListHostedZonesByVPCResponseTypeDef",
    ) -> "dc_td.ListHostedZonesByVPCResponse":
        return dc_td.ListHostedZonesByVPCResponse.make_one(res)

    def list_query_logging_configs(
        self,
        res: "bs_td.ListQueryLoggingConfigsResponseTypeDef",
    ) -> "dc_td.ListQueryLoggingConfigsResponse":
        return dc_td.ListQueryLoggingConfigsResponse.make_one(res)

    def list_resource_record_sets(
        self,
        res: "bs_td.ListResourceRecordSetsResponseTypeDef",
    ) -> "dc_td.ListResourceRecordSetsResponse":
        return dc_td.ListResourceRecordSetsResponse.make_one(res)

    def list_reusable_delegation_sets(
        self,
        res: "bs_td.ListReusableDelegationSetsResponseTypeDef",
    ) -> "dc_td.ListReusableDelegationSetsResponse":
        return dc_td.ListReusableDelegationSetsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_tags_for_resources(
        self,
        res: "bs_td.ListTagsForResourcesResponseTypeDef",
    ) -> "dc_td.ListTagsForResourcesResponse":
        return dc_td.ListTagsForResourcesResponse.make_one(res)

    def list_traffic_policies(
        self,
        res: "bs_td.ListTrafficPoliciesResponseTypeDef",
    ) -> "dc_td.ListTrafficPoliciesResponse":
        return dc_td.ListTrafficPoliciesResponse.make_one(res)

    def list_traffic_policy_instances(
        self,
        res: "bs_td.ListTrafficPolicyInstancesResponseTypeDef",
    ) -> "dc_td.ListTrafficPolicyInstancesResponse":
        return dc_td.ListTrafficPolicyInstancesResponse.make_one(res)

    def list_traffic_policy_instances_by_hosted_zone(
        self,
        res: "bs_td.ListTrafficPolicyInstancesByHostedZoneResponseTypeDef",
    ) -> "dc_td.ListTrafficPolicyInstancesByHostedZoneResponse":
        return dc_td.ListTrafficPolicyInstancesByHostedZoneResponse.make_one(res)

    def list_traffic_policy_instances_by_policy(
        self,
        res: "bs_td.ListTrafficPolicyInstancesByPolicyResponseTypeDef",
    ) -> "dc_td.ListTrafficPolicyInstancesByPolicyResponse":
        return dc_td.ListTrafficPolicyInstancesByPolicyResponse.make_one(res)

    def list_traffic_policy_versions(
        self,
        res: "bs_td.ListTrafficPolicyVersionsResponseTypeDef",
    ) -> "dc_td.ListTrafficPolicyVersionsResponse":
        return dc_td.ListTrafficPolicyVersionsResponse.make_one(res)

    def list_vpc_association_authorizations(
        self,
        res: "bs_td.ListVPCAssociationAuthorizationsResponseTypeDef",
    ) -> "dc_td.ListVPCAssociationAuthorizationsResponse":
        return dc_td.ListVPCAssociationAuthorizationsResponse.make_one(res)

    def test_dns_answer(
        self,
        res: "bs_td.TestDNSAnswerResponseTypeDef",
    ) -> "dc_td.TestDNSAnswerResponse":
        return dc_td.TestDNSAnswerResponse.make_one(res)

    def update_health_check(
        self,
        res: "bs_td.UpdateHealthCheckResponseTypeDef",
    ) -> "dc_td.UpdateHealthCheckResponse":
        return dc_td.UpdateHealthCheckResponse.make_one(res)

    def update_hosted_zone_comment(
        self,
        res: "bs_td.UpdateHostedZoneCommentResponseTypeDef",
    ) -> "dc_td.UpdateHostedZoneCommentResponse":
        return dc_td.UpdateHostedZoneCommentResponse.make_one(res)

    def update_traffic_policy_comment(
        self,
        res: "bs_td.UpdateTrafficPolicyCommentResponseTypeDef",
    ) -> "dc_td.UpdateTrafficPolicyCommentResponse":
        return dc_td.UpdateTrafficPolicyCommentResponse.make_one(res)

    def update_traffic_policy_instance(
        self,
        res: "bs_td.UpdateTrafficPolicyInstanceResponseTypeDef",
    ) -> "dc_td.UpdateTrafficPolicyInstanceResponse":
        return dc_td.UpdateTrafficPolicyInstanceResponse.make_one(res)


route53_caster = ROUTE53Caster()
