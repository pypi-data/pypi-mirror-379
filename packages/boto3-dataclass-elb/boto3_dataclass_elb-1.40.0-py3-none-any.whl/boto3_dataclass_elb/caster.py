# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_elb import type_defs as bs_td


class ELBCaster:

    def apply_security_groups_to_load_balancer(
        self,
        res: "bs_td.ApplySecurityGroupsToLoadBalancerOutputTypeDef",
    ) -> "dc_td.ApplySecurityGroupsToLoadBalancerOutput":
        return dc_td.ApplySecurityGroupsToLoadBalancerOutput.make_one(res)

    def attach_load_balancer_to_subnets(
        self,
        res: "bs_td.AttachLoadBalancerToSubnetsOutputTypeDef",
    ) -> "dc_td.AttachLoadBalancerToSubnetsOutput":
        return dc_td.AttachLoadBalancerToSubnetsOutput.make_one(res)

    def configure_health_check(
        self,
        res: "bs_td.ConfigureHealthCheckOutputTypeDef",
    ) -> "dc_td.ConfigureHealthCheckOutput":
        return dc_td.ConfigureHealthCheckOutput.make_one(res)

    def create_load_balancer(
        self,
        res: "bs_td.CreateAccessPointOutputTypeDef",
    ) -> "dc_td.CreateAccessPointOutput":
        return dc_td.CreateAccessPointOutput.make_one(res)

    def deregister_instances_from_load_balancer(
        self,
        res: "bs_td.DeregisterEndPointsOutputTypeDef",
    ) -> "dc_td.DeregisterEndPointsOutput":
        return dc_td.DeregisterEndPointsOutput.make_one(res)

    def describe_account_limits(
        self,
        res: "bs_td.DescribeAccountLimitsOutputTypeDef",
    ) -> "dc_td.DescribeAccountLimitsOutput":
        return dc_td.DescribeAccountLimitsOutput.make_one(res)

    def describe_instance_health(
        self,
        res: "bs_td.DescribeEndPointStateOutputTypeDef",
    ) -> "dc_td.DescribeEndPointStateOutput":
        return dc_td.DescribeEndPointStateOutput.make_one(res)

    def describe_load_balancer_attributes(
        self,
        res: "bs_td.DescribeLoadBalancerAttributesOutputTypeDef",
    ) -> "dc_td.DescribeLoadBalancerAttributesOutput":
        return dc_td.DescribeLoadBalancerAttributesOutput.make_one(res)

    def describe_load_balancer_policies(
        self,
        res: "bs_td.DescribeLoadBalancerPoliciesOutputTypeDef",
    ) -> "dc_td.DescribeLoadBalancerPoliciesOutput":
        return dc_td.DescribeLoadBalancerPoliciesOutput.make_one(res)

    def describe_load_balancer_policy_types(
        self,
        res: "bs_td.DescribeLoadBalancerPolicyTypesOutputTypeDef",
    ) -> "dc_td.DescribeLoadBalancerPolicyTypesOutput":
        return dc_td.DescribeLoadBalancerPolicyTypesOutput.make_one(res)

    def describe_load_balancers(
        self,
        res: "bs_td.DescribeAccessPointsOutputTypeDef",
    ) -> "dc_td.DescribeAccessPointsOutput":
        return dc_td.DescribeAccessPointsOutput.make_one(res)

    def describe_tags(
        self,
        res: "bs_td.DescribeTagsOutputTypeDef",
    ) -> "dc_td.DescribeTagsOutput":
        return dc_td.DescribeTagsOutput.make_one(res)

    def detach_load_balancer_from_subnets(
        self,
        res: "bs_td.DetachLoadBalancerFromSubnetsOutputTypeDef",
    ) -> "dc_td.DetachLoadBalancerFromSubnetsOutput":
        return dc_td.DetachLoadBalancerFromSubnetsOutput.make_one(res)

    def disable_availability_zones_for_load_balancer(
        self,
        res: "bs_td.RemoveAvailabilityZonesOutputTypeDef",
    ) -> "dc_td.RemoveAvailabilityZonesOutput":
        return dc_td.RemoveAvailabilityZonesOutput.make_one(res)

    def enable_availability_zones_for_load_balancer(
        self,
        res: "bs_td.AddAvailabilityZonesOutputTypeDef",
    ) -> "dc_td.AddAvailabilityZonesOutput":
        return dc_td.AddAvailabilityZonesOutput.make_one(res)

    def modify_load_balancer_attributes(
        self,
        res: "bs_td.ModifyLoadBalancerAttributesOutputTypeDef",
    ) -> "dc_td.ModifyLoadBalancerAttributesOutput":
        return dc_td.ModifyLoadBalancerAttributesOutput.make_one(res)

    def register_instances_with_load_balancer(
        self,
        res: "bs_td.RegisterEndPointsOutputTypeDef",
    ) -> "dc_td.RegisterEndPointsOutput":
        return dc_td.RegisterEndPointsOutput.make_one(res)


elb_caster = ELBCaster()
