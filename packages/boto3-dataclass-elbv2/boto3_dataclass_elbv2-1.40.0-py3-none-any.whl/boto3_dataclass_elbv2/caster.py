# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_elbv2 import type_defs as bs_td


class ELBV2Caster:

    def add_listener_certificates(
        self,
        res: "bs_td.AddListenerCertificatesOutputTypeDef",
    ) -> "dc_td.AddListenerCertificatesOutput":
        return dc_td.AddListenerCertificatesOutput.make_one(res)

    def add_trust_store_revocations(
        self,
        res: "bs_td.AddTrustStoreRevocationsOutputTypeDef",
    ) -> "dc_td.AddTrustStoreRevocationsOutput":
        return dc_td.AddTrustStoreRevocationsOutput.make_one(res)

    def create_listener(
        self,
        res: "bs_td.CreateListenerOutputTypeDef",
    ) -> "dc_td.CreateListenerOutput":
        return dc_td.CreateListenerOutput.make_one(res)

    def create_load_balancer(
        self,
        res: "bs_td.CreateLoadBalancerOutputTypeDef",
    ) -> "dc_td.CreateLoadBalancerOutput":
        return dc_td.CreateLoadBalancerOutput.make_one(res)

    def create_rule(
        self,
        res: "bs_td.CreateRuleOutputTypeDef",
    ) -> "dc_td.CreateRuleOutput":
        return dc_td.CreateRuleOutput.make_one(res)

    def create_target_group(
        self,
        res: "bs_td.CreateTargetGroupOutputTypeDef",
    ) -> "dc_td.CreateTargetGroupOutput":
        return dc_td.CreateTargetGroupOutput.make_one(res)

    def create_trust_store(
        self,
        res: "bs_td.CreateTrustStoreOutputTypeDef",
    ) -> "dc_td.CreateTrustStoreOutput":
        return dc_td.CreateTrustStoreOutput.make_one(res)

    def describe_account_limits(
        self,
        res: "bs_td.DescribeAccountLimitsOutputTypeDef",
    ) -> "dc_td.DescribeAccountLimitsOutput":
        return dc_td.DescribeAccountLimitsOutput.make_one(res)

    def describe_capacity_reservation(
        self,
        res: "bs_td.DescribeCapacityReservationOutputTypeDef",
    ) -> "dc_td.DescribeCapacityReservationOutput":
        return dc_td.DescribeCapacityReservationOutput.make_one(res)

    def describe_listener_attributes(
        self,
        res: "bs_td.DescribeListenerAttributesOutputTypeDef",
    ) -> "dc_td.DescribeListenerAttributesOutput":
        return dc_td.DescribeListenerAttributesOutput.make_one(res)

    def describe_listener_certificates(
        self,
        res: "bs_td.DescribeListenerCertificatesOutputTypeDef",
    ) -> "dc_td.DescribeListenerCertificatesOutput":
        return dc_td.DescribeListenerCertificatesOutput.make_one(res)

    def describe_listeners(
        self,
        res: "bs_td.DescribeListenersOutputTypeDef",
    ) -> "dc_td.DescribeListenersOutput":
        return dc_td.DescribeListenersOutput.make_one(res)

    def describe_load_balancer_attributes(
        self,
        res: "bs_td.DescribeLoadBalancerAttributesOutputTypeDef",
    ) -> "dc_td.DescribeLoadBalancerAttributesOutput":
        return dc_td.DescribeLoadBalancerAttributesOutput.make_one(res)

    def describe_load_balancers(
        self,
        res: "bs_td.DescribeLoadBalancersOutputTypeDef",
    ) -> "dc_td.DescribeLoadBalancersOutput":
        return dc_td.DescribeLoadBalancersOutput.make_one(res)

    def describe_rules(
        self,
        res: "bs_td.DescribeRulesOutputTypeDef",
    ) -> "dc_td.DescribeRulesOutput":
        return dc_td.DescribeRulesOutput.make_one(res)

    def describe_ssl_policies(
        self,
        res: "bs_td.DescribeSSLPoliciesOutputTypeDef",
    ) -> "dc_td.DescribeSSLPoliciesOutput":
        return dc_td.DescribeSSLPoliciesOutput.make_one(res)

    def describe_tags(
        self,
        res: "bs_td.DescribeTagsOutputTypeDef",
    ) -> "dc_td.DescribeTagsOutput":
        return dc_td.DescribeTagsOutput.make_one(res)

    def describe_target_group_attributes(
        self,
        res: "bs_td.DescribeTargetGroupAttributesOutputTypeDef",
    ) -> "dc_td.DescribeTargetGroupAttributesOutput":
        return dc_td.DescribeTargetGroupAttributesOutput.make_one(res)

    def describe_target_groups(
        self,
        res: "bs_td.DescribeTargetGroupsOutputTypeDef",
    ) -> "dc_td.DescribeTargetGroupsOutput":
        return dc_td.DescribeTargetGroupsOutput.make_one(res)

    def describe_target_health(
        self,
        res: "bs_td.DescribeTargetHealthOutputTypeDef",
    ) -> "dc_td.DescribeTargetHealthOutput":
        return dc_td.DescribeTargetHealthOutput.make_one(res)

    def describe_trust_store_associations(
        self,
        res: "bs_td.DescribeTrustStoreAssociationsOutputTypeDef",
    ) -> "dc_td.DescribeTrustStoreAssociationsOutput":
        return dc_td.DescribeTrustStoreAssociationsOutput.make_one(res)

    def describe_trust_store_revocations(
        self,
        res: "bs_td.DescribeTrustStoreRevocationsOutputTypeDef",
    ) -> "dc_td.DescribeTrustStoreRevocationsOutput":
        return dc_td.DescribeTrustStoreRevocationsOutput.make_one(res)

    def describe_trust_stores(
        self,
        res: "bs_td.DescribeTrustStoresOutputTypeDef",
    ) -> "dc_td.DescribeTrustStoresOutput":
        return dc_td.DescribeTrustStoresOutput.make_one(res)

    def get_resource_policy(
        self,
        res: "bs_td.GetResourcePolicyOutputTypeDef",
    ) -> "dc_td.GetResourcePolicyOutput":
        return dc_td.GetResourcePolicyOutput.make_one(res)

    def get_trust_store_ca_certificates_bundle(
        self,
        res: "bs_td.GetTrustStoreCaCertificatesBundleOutputTypeDef",
    ) -> "dc_td.GetTrustStoreCaCertificatesBundleOutput":
        return dc_td.GetTrustStoreCaCertificatesBundleOutput.make_one(res)

    def get_trust_store_revocation_content(
        self,
        res: "bs_td.GetTrustStoreRevocationContentOutputTypeDef",
    ) -> "dc_td.GetTrustStoreRevocationContentOutput":
        return dc_td.GetTrustStoreRevocationContentOutput.make_one(res)

    def modify_capacity_reservation(
        self,
        res: "bs_td.ModifyCapacityReservationOutputTypeDef",
    ) -> "dc_td.ModifyCapacityReservationOutput":
        return dc_td.ModifyCapacityReservationOutput.make_one(res)

    def modify_ip_pools(
        self,
        res: "bs_td.ModifyIpPoolsOutputTypeDef",
    ) -> "dc_td.ModifyIpPoolsOutput":
        return dc_td.ModifyIpPoolsOutput.make_one(res)

    def modify_listener(
        self,
        res: "bs_td.ModifyListenerOutputTypeDef",
    ) -> "dc_td.ModifyListenerOutput":
        return dc_td.ModifyListenerOutput.make_one(res)

    def modify_listener_attributes(
        self,
        res: "bs_td.ModifyListenerAttributesOutputTypeDef",
    ) -> "dc_td.ModifyListenerAttributesOutput":
        return dc_td.ModifyListenerAttributesOutput.make_one(res)

    def modify_load_balancer_attributes(
        self,
        res: "bs_td.ModifyLoadBalancerAttributesOutputTypeDef",
    ) -> "dc_td.ModifyLoadBalancerAttributesOutput":
        return dc_td.ModifyLoadBalancerAttributesOutput.make_one(res)

    def modify_rule(
        self,
        res: "bs_td.ModifyRuleOutputTypeDef",
    ) -> "dc_td.ModifyRuleOutput":
        return dc_td.ModifyRuleOutput.make_one(res)

    def modify_target_group(
        self,
        res: "bs_td.ModifyTargetGroupOutputTypeDef",
    ) -> "dc_td.ModifyTargetGroupOutput":
        return dc_td.ModifyTargetGroupOutput.make_one(res)

    def modify_target_group_attributes(
        self,
        res: "bs_td.ModifyTargetGroupAttributesOutputTypeDef",
    ) -> "dc_td.ModifyTargetGroupAttributesOutput":
        return dc_td.ModifyTargetGroupAttributesOutput.make_one(res)

    def modify_trust_store(
        self,
        res: "bs_td.ModifyTrustStoreOutputTypeDef",
    ) -> "dc_td.ModifyTrustStoreOutput":
        return dc_td.ModifyTrustStoreOutput.make_one(res)

    def set_ip_address_type(
        self,
        res: "bs_td.SetIpAddressTypeOutputTypeDef",
    ) -> "dc_td.SetIpAddressTypeOutput":
        return dc_td.SetIpAddressTypeOutput.make_one(res)

    def set_rule_priorities(
        self,
        res: "bs_td.SetRulePrioritiesOutputTypeDef",
    ) -> "dc_td.SetRulePrioritiesOutput":
        return dc_td.SetRulePrioritiesOutput.make_one(res)

    def set_security_groups(
        self,
        res: "bs_td.SetSecurityGroupsOutputTypeDef",
    ) -> "dc_td.SetSecurityGroupsOutput":
        return dc_td.SetSecurityGroupsOutput.make_one(res)

    def set_subnets(
        self,
        res: "bs_td.SetSubnetsOutputTypeDef",
    ) -> "dc_td.SetSubnetsOutput":
        return dc_td.SetSubnetsOutput.make_one(res)


elbv2_caster = ELBV2Caster()
