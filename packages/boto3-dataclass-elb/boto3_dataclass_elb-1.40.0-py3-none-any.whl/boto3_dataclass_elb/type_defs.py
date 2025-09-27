# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_elb import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccessLog:
    boto3_raw_data: "type_defs.AccessLogTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    S3BucketName = field("S3BucketName")
    EmitInterval = field("EmitInterval")
    S3BucketPrefix = field("S3BucketPrefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessLogTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccessLogTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddAvailabilityZonesInput:
    boto3_raw_data: "type_defs.AddAvailabilityZonesInputTypeDef" = dataclasses.field()

    LoadBalancerName = field("LoadBalancerName")
    AvailabilityZones = field("AvailabilityZones")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddAvailabilityZonesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddAvailabilityZonesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResponseMetadata:
    boto3_raw_data: "type_defs.ResponseMetadataTypeDef" = dataclasses.field()

    RequestId = field("RequestId")
    HTTPStatusCode = field("HTTPStatusCode")
    HTTPHeaders = field("HTTPHeaders")
    RetryAttempts = field("RetryAttempts")
    HostId = field("HostId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResponseMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Tag:
    boto3_raw_data: "type_defs.TagTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AdditionalAttribute:
    boto3_raw_data: "type_defs.AdditionalAttributeTypeDef" = dataclasses.field()

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AdditionalAttributeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AdditionalAttributeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppCookieStickinessPolicy:
    boto3_raw_data: "type_defs.AppCookieStickinessPolicyTypeDef" = dataclasses.field()

    PolicyName = field("PolicyName")
    CookieName = field("CookieName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AppCookieStickinessPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppCookieStickinessPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplySecurityGroupsToLoadBalancerInput:
    boto3_raw_data: "type_defs.ApplySecurityGroupsToLoadBalancerInputTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerName = field("LoadBalancerName")
    SecurityGroups = field("SecurityGroups")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplySecurityGroupsToLoadBalancerInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplySecurityGroupsToLoadBalancerInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachLoadBalancerToSubnetsInput:
    boto3_raw_data: "type_defs.AttachLoadBalancerToSubnetsInputTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerName = field("LoadBalancerName")
    Subnets = field("Subnets")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AttachLoadBalancerToSubnetsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachLoadBalancerToSubnetsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BackendServerDescription:
    boto3_raw_data: "type_defs.BackendServerDescriptionTypeDef" = dataclasses.field()

    InstancePort = field("InstancePort")
    PolicyNames = field("PolicyNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BackendServerDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BackendServerDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HealthCheck:
    boto3_raw_data: "type_defs.HealthCheckTypeDef" = dataclasses.field()

    Target = field("Target")
    Interval = field("Interval")
    Timeout = field("Timeout")
    UnhealthyThreshold = field("UnhealthyThreshold")
    HealthyThreshold = field("HealthyThreshold")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HealthCheckTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HealthCheckTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionDraining:
    boto3_raw_data: "type_defs.ConnectionDrainingTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    Timeout = field("Timeout")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectionDrainingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionDrainingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectionSettings:
    boto3_raw_data: "type_defs.ConnectionSettingsTypeDef" = dataclasses.field()

    IdleTimeout = field("IdleTimeout")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectionSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectionSettingsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Listener:
    boto3_raw_data: "type_defs.ListenerTypeDef" = dataclasses.field()

    Protocol = field("Protocol")
    LoadBalancerPort = field("LoadBalancerPort")
    InstancePort = field("InstancePort")
    InstanceProtocol = field("InstanceProtocol")
    SSLCertificateId = field("SSLCertificateId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListenerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListenerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAppCookieStickinessPolicyInput:
    boto3_raw_data: "type_defs.CreateAppCookieStickinessPolicyInputTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerName = field("LoadBalancerName")
    PolicyName = field("PolicyName")
    CookieName = field("CookieName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAppCookieStickinessPolicyInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAppCookieStickinessPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLBCookieStickinessPolicyInput:
    boto3_raw_data: "type_defs.CreateLBCookieStickinessPolicyInputTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerName = field("LoadBalancerName")
    PolicyName = field("PolicyName")
    CookieExpirationPeriod = field("CookieExpirationPeriod")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateLBCookieStickinessPolicyInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLBCookieStickinessPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyAttribute:
    boto3_raw_data: "type_defs.PolicyAttributeTypeDef" = dataclasses.field()

    AttributeName = field("AttributeName")
    AttributeValue = field("AttributeValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyAttributeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyAttributeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CrossZoneLoadBalancing:
    boto3_raw_data: "type_defs.CrossZoneLoadBalancingTypeDef" = dataclasses.field()

    Enabled = field("Enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CrossZoneLoadBalancingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CrossZoneLoadBalancingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccessPointInput:
    boto3_raw_data: "type_defs.DeleteAccessPointInputTypeDef" = dataclasses.field()

    LoadBalancerName = field("LoadBalancerName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAccessPointInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccessPointInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLoadBalancerListenerInput:
    boto3_raw_data: "type_defs.DeleteLoadBalancerListenerInputTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerName = field("LoadBalancerName")
    LoadBalancerPorts = field("LoadBalancerPorts")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteLoadBalancerListenerInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLoadBalancerListenerInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLoadBalancerPolicyInput:
    boto3_raw_data: "type_defs.DeleteLoadBalancerPolicyInputTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerName = field("LoadBalancerName")
    PolicyName = field("PolicyName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteLoadBalancerPolicyInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLoadBalancerPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Instance:
    boto3_raw_data: "type_defs.InstanceTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstanceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PaginatorConfig:
    boto3_raw_data: "type_defs.PaginatorConfigTypeDef" = dataclasses.field()

    MaxItems = field("MaxItems")
    PageSize = field("PageSize")
    StartingToken = field("StartingToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PaginatorConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PaginatorConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccessPointsInput:
    boto3_raw_data: "type_defs.DescribeAccessPointsInputTypeDef" = dataclasses.field()

    LoadBalancerNames = field("LoadBalancerNames")
    Marker = field("Marker")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAccessPointsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccessPointsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountLimitsInput:
    boto3_raw_data: "type_defs.DescribeAccountLimitsInputTypeDef" = dataclasses.field()

    Marker = field("Marker")
    PageSize = field("PageSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAccountLimitsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountLimitsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Limit:
    boto3_raw_data: "type_defs.LimitTypeDef" = dataclasses.field()

    Name = field("Name")
    Max = field("Max")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LimitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LimitTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WaiterConfig:
    boto3_raw_data: "type_defs.WaiterConfigTypeDef" = dataclasses.field()

    Delay = field("Delay")
    MaxAttempts = field("MaxAttempts")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WaiterConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WaiterConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceState:
    boto3_raw_data: "type_defs.InstanceStateTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    State = field("State")
    ReasonCode = field("ReasonCode")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InstanceStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InstanceStateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoadBalancerAttributesInput:
    boto3_raw_data: "type_defs.DescribeLoadBalancerAttributesInputTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerName = field("LoadBalancerName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLoadBalancerAttributesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoadBalancerAttributesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoadBalancerPoliciesInput:
    boto3_raw_data: "type_defs.DescribeLoadBalancerPoliciesInputTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerName = field("LoadBalancerName")
    PolicyNames = field("PolicyNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLoadBalancerPoliciesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoadBalancerPoliciesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoadBalancerPolicyTypesInput:
    boto3_raw_data: "type_defs.DescribeLoadBalancerPolicyTypesInputTypeDef" = (
        dataclasses.field()
    )

    PolicyTypeNames = field("PolicyTypeNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLoadBalancerPolicyTypesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoadBalancerPolicyTypesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTagsInput:
    boto3_raw_data: "type_defs.DescribeTagsInputTypeDef" = dataclasses.field()

    LoadBalancerNames = field("LoadBalancerNames")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DescribeTagsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTagsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachLoadBalancerFromSubnetsInput:
    boto3_raw_data: "type_defs.DetachLoadBalancerFromSubnetsInputTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerName = field("LoadBalancerName")
    Subnets = field("Subnets")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DetachLoadBalancerFromSubnetsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachLoadBalancerFromSubnetsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LBCookieStickinessPolicy:
    boto3_raw_data: "type_defs.LBCookieStickinessPolicyTypeDef" = dataclasses.field()

    PolicyName = field("PolicyName")
    CookieExpirationPeriod = field("CookieExpirationPeriod")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LBCookieStickinessPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LBCookieStickinessPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceSecurityGroup:
    boto3_raw_data: "type_defs.SourceSecurityGroupTypeDef" = dataclasses.field()

    OwnerAlias = field("OwnerAlias")
    GroupName = field("GroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceSecurityGroupTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceSecurityGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyAttributeDescription:
    boto3_raw_data: "type_defs.PolicyAttributeDescriptionTypeDef" = dataclasses.field()

    AttributeName = field("AttributeName")
    AttributeValue = field("AttributeValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolicyAttributeDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyAttributeDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyAttributeTypeDescription:
    boto3_raw_data: "type_defs.PolicyAttributeTypeDescriptionTypeDef" = (
        dataclasses.field()
    )

    AttributeName = field("AttributeName")
    AttributeType = field("AttributeType")
    Description = field("Description")
    DefaultValue = field("DefaultValue")
    Cardinality = field("Cardinality")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PolicyAttributeTypeDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyAttributeTypeDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveAvailabilityZonesInput:
    boto3_raw_data: "type_defs.RemoveAvailabilityZonesInputTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerName = field("LoadBalancerName")
    AvailabilityZones = field("AvailabilityZones")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoveAvailabilityZonesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveAvailabilityZonesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagKeyOnly:
    boto3_raw_data: "type_defs.TagKeyOnlyTypeDef" = dataclasses.field()

    Key = field("Key")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagKeyOnlyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagKeyOnlyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetLoadBalancerListenerSSLCertificateInput:
    boto3_raw_data: "type_defs.SetLoadBalancerListenerSSLCertificateInputTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerName = field("LoadBalancerName")
    LoadBalancerPort = field("LoadBalancerPort")
    SSLCertificateId = field("SSLCertificateId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetLoadBalancerListenerSSLCertificateInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetLoadBalancerListenerSSLCertificateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetLoadBalancerPoliciesForBackendServerInput:
    boto3_raw_data: "type_defs.SetLoadBalancerPoliciesForBackendServerInputTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerName = field("LoadBalancerName")
    InstancePort = field("InstancePort")
    PolicyNames = field("PolicyNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetLoadBalancerPoliciesForBackendServerInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetLoadBalancerPoliciesForBackendServerInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetLoadBalancerPoliciesOfListenerInput:
    boto3_raw_data: "type_defs.SetLoadBalancerPoliciesOfListenerInputTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerName = field("LoadBalancerName")
    LoadBalancerPort = field("LoadBalancerPort")
    PolicyNames = field("PolicyNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SetLoadBalancerPoliciesOfListenerInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetLoadBalancerPoliciesOfListenerInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddAvailabilityZonesOutput:
    boto3_raw_data: "type_defs.AddAvailabilityZonesOutputTypeDef" = dataclasses.field()

    AvailabilityZones = field("AvailabilityZones")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddAvailabilityZonesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddAvailabilityZonesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplySecurityGroupsToLoadBalancerOutput:
    boto3_raw_data: "type_defs.ApplySecurityGroupsToLoadBalancerOutputTypeDef" = (
        dataclasses.field()
    )

    SecurityGroups = field("SecurityGroups")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplySecurityGroupsToLoadBalancerOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplySecurityGroupsToLoadBalancerOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AttachLoadBalancerToSubnetsOutput:
    boto3_raw_data: "type_defs.AttachLoadBalancerToSubnetsOutputTypeDef" = (
        dataclasses.field()
    )

    Subnets = field("Subnets")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AttachLoadBalancerToSubnetsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AttachLoadBalancerToSubnetsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessPointOutput:
    boto3_raw_data: "type_defs.CreateAccessPointOutputTypeDef" = dataclasses.field()

    DNSName = field("DNSName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccessPointOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessPointOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetachLoadBalancerFromSubnetsOutput:
    boto3_raw_data: "type_defs.DetachLoadBalancerFromSubnetsOutputTypeDef" = (
        dataclasses.field()
    )

    Subnets = field("Subnets")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DetachLoadBalancerFromSubnetsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetachLoadBalancerFromSubnetsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveAvailabilityZonesOutput:
    boto3_raw_data: "type_defs.RemoveAvailabilityZonesOutputTypeDef" = (
        dataclasses.field()
    )

    AvailabilityZones = field("AvailabilityZones")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RemoveAvailabilityZonesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoveAvailabilityZonesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddTagsInput:
    boto3_raw_data: "type_defs.AddTagsInputTypeDef" = dataclasses.field()

    LoadBalancerNames = field("LoadBalancerNames")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddTagsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddTagsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagDescription:
    boto3_raw_data: "type_defs.TagDescriptionTypeDef" = dataclasses.field()

    LoadBalancerName = field("LoadBalancerName")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TagDescriptionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigureHealthCheckInput:
    boto3_raw_data: "type_defs.ConfigureHealthCheckInputTypeDef" = dataclasses.field()

    LoadBalancerName = field("LoadBalancerName")

    @cached_property
    def HealthCheck(self):  # pragma: no cover
        return HealthCheck.make_one(self.boto3_raw_data["HealthCheck"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigureHealthCheckInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigureHealthCheckInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigureHealthCheckOutput:
    boto3_raw_data: "type_defs.ConfigureHealthCheckOutputTypeDef" = dataclasses.field()

    @cached_property
    def HealthCheck(self):  # pragma: no cover
        return HealthCheck.make_one(self.boto3_raw_data["HealthCheck"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigureHealthCheckOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigureHealthCheckOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessPointInput:
    boto3_raw_data: "type_defs.CreateAccessPointInputTypeDef" = dataclasses.field()

    LoadBalancerName = field("LoadBalancerName")

    @cached_property
    def Listeners(self):  # pragma: no cover
        return Listener.make_many(self.boto3_raw_data["Listeners"])

    AvailabilityZones = field("AvailabilityZones")
    Subnets = field("Subnets")
    SecurityGroups = field("SecurityGroups")
    Scheme = field("Scheme")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccessPointInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessPointInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLoadBalancerListenerInput:
    boto3_raw_data: "type_defs.CreateLoadBalancerListenerInputTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerName = field("LoadBalancerName")

    @cached_property
    def Listeners(self):  # pragma: no cover
        return Listener.make_many(self.boto3_raw_data["Listeners"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateLoadBalancerListenerInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLoadBalancerListenerInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListenerDescription:
    boto3_raw_data: "type_defs.ListenerDescriptionTypeDef" = dataclasses.field()

    @cached_property
    def Listener(self):  # pragma: no cover
        return Listener.make_one(self.boto3_raw_data["Listener"])

    PolicyNames = field("PolicyNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListenerDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListenerDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLoadBalancerPolicyInput:
    boto3_raw_data: "type_defs.CreateLoadBalancerPolicyInputTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerName = field("LoadBalancerName")
    PolicyName = field("PolicyName")
    PolicyTypeName = field("PolicyTypeName")

    @cached_property
    def PolicyAttributes(self):  # pragma: no cover
        return PolicyAttribute.make_many(self.boto3_raw_data["PolicyAttributes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateLoadBalancerPolicyInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLoadBalancerPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoadBalancerAttributesOutput:
    boto3_raw_data: "type_defs.LoadBalancerAttributesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CrossZoneLoadBalancing(self):  # pragma: no cover
        return CrossZoneLoadBalancing.make_one(
            self.boto3_raw_data["CrossZoneLoadBalancing"]
        )

    @cached_property
    def AccessLog(self):  # pragma: no cover
        return AccessLog.make_one(self.boto3_raw_data["AccessLog"])

    @cached_property
    def ConnectionDraining(self):  # pragma: no cover
        return ConnectionDraining.make_one(self.boto3_raw_data["ConnectionDraining"])

    @cached_property
    def ConnectionSettings(self):  # pragma: no cover
        return ConnectionSettings.make_one(self.boto3_raw_data["ConnectionSettings"])

    @cached_property
    def AdditionalAttributes(self):  # pragma: no cover
        return AdditionalAttribute.make_many(
            self.boto3_raw_data["AdditionalAttributes"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoadBalancerAttributesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoadBalancerAttributesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoadBalancerAttributes:
    boto3_raw_data: "type_defs.LoadBalancerAttributesTypeDef" = dataclasses.field()

    @cached_property
    def CrossZoneLoadBalancing(self):  # pragma: no cover
        return CrossZoneLoadBalancing.make_one(
            self.boto3_raw_data["CrossZoneLoadBalancing"]
        )

    @cached_property
    def AccessLog(self):  # pragma: no cover
        return AccessLog.make_one(self.boto3_raw_data["AccessLog"])

    @cached_property
    def ConnectionDraining(self):  # pragma: no cover
        return ConnectionDraining.make_one(self.boto3_raw_data["ConnectionDraining"])

    @cached_property
    def ConnectionSettings(self):  # pragma: no cover
        return ConnectionSettings.make_one(self.boto3_raw_data["ConnectionSettings"])

    @cached_property
    def AdditionalAttributes(self):  # pragma: no cover
        return AdditionalAttribute.make_many(
            self.boto3_raw_data["AdditionalAttributes"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoadBalancerAttributesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoadBalancerAttributesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterEndPointsInput:
    boto3_raw_data: "type_defs.DeregisterEndPointsInputTypeDef" = dataclasses.field()

    LoadBalancerName = field("LoadBalancerName")

    @cached_property
    def Instances(self):  # pragma: no cover
        return Instance.make_many(self.boto3_raw_data["Instances"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeregisterEndPointsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterEndPointsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterEndPointsOutput:
    boto3_raw_data: "type_defs.DeregisterEndPointsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Instances(self):  # pragma: no cover
        return Instance.make_many(self.boto3_raw_data["Instances"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeregisterEndPointsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterEndPointsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndPointStateInput:
    boto3_raw_data: "type_defs.DescribeEndPointStateInputTypeDef" = dataclasses.field()

    LoadBalancerName = field("LoadBalancerName")

    @cached_property
    def Instances(self):  # pragma: no cover
        return Instance.make_many(self.boto3_raw_data["Instances"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEndPointStateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndPointStateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterEndPointsInput:
    boto3_raw_data: "type_defs.RegisterEndPointsInputTypeDef" = dataclasses.field()

    LoadBalancerName = field("LoadBalancerName")

    @cached_property
    def Instances(self):  # pragma: no cover
        return Instance.make_many(self.boto3_raw_data["Instances"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterEndPointsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterEndPointsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterEndPointsOutput:
    boto3_raw_data: "type_defs.RegisterEndPointsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Instances(self):  # pragma: no cover
        return Instance.make_many(self.boto3_raw_data["Instances"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterEndPointsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterEndPointsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccessPointsInputPaginate:
    boto3_raw_data: "type_defs.DescribeAccessPointsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerNames = field("LoadBalancerNames")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAccessPointsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccessPointsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountLimitsInputPaginate:
    boto3_raw_data: "type_defs.DescribeAccountLimitsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAccountLimitsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountLimitsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountLimitsOutput:
    boto3_raw_data: "type_defs.DescribeAccountLimitsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Limits(self):  # pragma: no cover
        return Limit.make_many(self.boto3_raw_data["Limits"])

    NextMarker = field("NextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAccountLimitsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountLimitsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndPointStateInputWaitExtraExtra:
    boto3_raw_data: "type_defs.DescribeEndPointStateInputWaitExtraExtraTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerName = field("LoadBalancerName")

    @cached_property
    def Instances(self):  # pragma: no cover
        return Instance.make_many(self.boto3_raw_data["Instances"])

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEndPointStateInputWaitExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndPointStateInputWaitExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndPointStateInputWaitExtra:
    boto3_raw_data: "type_defs.DescribeEndPointStateInputWaitExtraTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerName = field("LoadBalancerName")

    @cached_property
    def Instances(self):  # pragma: no cover
        return Instance.make_many(self.boto3_raw_data["Instances"])

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEndPointStateInputWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndPointStateInputWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndPointStateInputWait:
    boto3_raw_data: "type_defs.DescribeEndPointStateInputWaitTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerName = field("LoadBalancerName")

    @cached_property
    def Instances(self):  # pragma: no cover
        return Instance.make_many(self.boto3_raw_data["Instances"])

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEndPointStateInputWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndPointStateInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEndPointStateOutput:
    boto3_raw_data: "type_defs.DescribeEndPointStateOutputTypeDef" = dataclasses.field()

    @cached_property
    def InstanceStates(self):  # pragma: no cover
        return InstanceState.make_many(self.boto3_raw_data["InstanceStates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEndPointStateOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEndPointStateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Policies:
    boto3_raw_data: "type_defs.PoliciesTypeDef" = dataclasses.field()

    @cached_property
    def AppCookieStickinessPolicies(self):  # pragma: no cover
        return AppCookieStickinessPolicy.make_many(
            self.boto3_raw_data["AppCookieStickinessPolicies"]
        )

    @cached_property
    def LBCookieStickinessPolicies(self):  # pragma: no cover
        return LBCookieStickinessPolicy.make_many(
            self.boto3_raw_data["LBCookieStickinessPolicies"]
        )

    OtherPolicies = field("OtherPolicies")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PoliciesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PoliciesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyDescription:
    boto3_raw_data: "type_defs.PolicyDescriptionTypeDef" = dataclasses.field()

    PolicyName = field("PolicyName")
    PolicyTypeName = field("PolicyTypeName")

    @cached_property
    def PolicyAttributeDescriptions(self):  # pragma: no cover
        return PolicyAttributeDescription.make_many(
            self.boto3_raw_data["PolicyAttributeDescriptions"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PolicyTypeDescription:
    boto3_raw_data: "type_defs.PolicyTypeDescriptionTypeDef" = dataclasses.field()

    PolicyTypeName = field("PolicyTypeName")
    Description = field("Description")

    @cached_property
    def PolicyAttributeTypeDescriptions(self):  # pragma: no cover
        return PolicyAttributeTypeDescription.make_many(
            self.boto3_raw_data["PolicyAttributeTypeDescriptions"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PolicyTypeDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PolicyTypeDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoveTagsInput:
    boto3_raw_data: "type_defs.RemoveTagsInputTypeDef" = dataclasses.field()

    LoadBalancerNames = field("LoadBalancerNames")

    @cached_property
    def Tags(self):  # pragma: no cover
        return TagKeyOnly.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RemoveTagsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RemoveTagsInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTagsOutput:
    boto3_raw_data: "type_defs.DescribeTagsOutputTypeDef" = dataclasses.field()

    @cached_property
    def TagDescriptions(self):  # pragma: no cover
        return TagDescription.make_many(self.boto3_raw_data["TagDescriptions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTagsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTagsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoadBalancerAttributesOutput:
    boto3_raw_data: "type_defs.DescribeLoadBalancerAttributesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LoadBalancerAttributes(self):  # pragma: no cover
        return LoadBalancerAttributesOutput.make_one(
            self.boto3_raw_data["LoadBalancerAttributes"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLoadBalancerAttributesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoadBalancerAttributesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyLoadBalancerAttributesOutput:
    boto3_raw_data: "type_defs.ModifyLoadBalancerAttributesOutputTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerName = field("LoadBalancerName")

    @cached_property
    def LoadBalancerAttributes(self):  # pragma: no cover
        return LoadBalancerAttributesOutput.make_one(
            self.boto3_raw_data["LoadBalancerAttributes"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyLoadBalancerAttributesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyLoadBalancerAttributesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoadBalancerDescription:
    boto3_raw_data: "type_defs.LoadBalancerDescriptionTypeDef" = dataclasses.field()

    LoadBalancerName = field("LoadBalancerName")
    DNSName = field("DNSName")
    CanonicalHostedZoneName = field("CanonicalHostedZoneName")
    CanonicalHostedZoneNameID = field("CanonicalHostedZoneNameID")

    @cached_property
    def ListenerDescriptions(self):  # pragma: no cover
        return ListenerDescription.make_many(
            self.boto3_raw_data["ListenerDescriptions"]
        )

    @cached_property
    def Policies(self):  # pragma: no cover
        return Policies.make_one(self.boto3_raw_data["Policies"])

    @cached_property
    def BackendServerDescriptions(self):  # pragma: no cover
        return BackendServerDescription.make_many(
            self.boto3_raw_data["BackendServerDescriptions"]
        )

    AvailabilityZones = field("AvailabilityZones")
    Subnets = field("Subnets")
    VPCId = field("VPCId")

    @cached_property
    def Instances(self):  # pragma: no cover
        return Instance.make_many(self.boto3_raw_data["Instances"])

    @cached_property
    def HealthCheck(self):  # pragma: no cover
        return HealthCheck.make_one(self.boto3_raw_data["HealthCheck"])

    @cached_property
    def SourceSecurityGroup(self):  # pragma: no cover
        return SourceSecurityGroup.make_one(self.boto3_raw_data["SourceSecurityGroup"])

    SecurityGroups = field("SecurityGroups")
    CreatedTime = field("CreatedTime")
    Scheme = field("Scheme")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LoadBalancerDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LoadBalancerDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoadBalancerPoliciesOutput:
    boto3_raw_data: "type_defs.DescribeLoadBalancerPoliciesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PolicyDescriptions(self):  # pragma: no cover
        return PolicyDescription.make_many(self.boto3_raw_data["PolicyDescriptions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLoadBalancerPoliciesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoadBalancerPoliciesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLoadBalancerPolicyTypesOutput:
    boto3_raw_data: "type_defs.DescribeLoadBalancerPolicyTypesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PolicyTypeDescriptions(self):  # pragma: no cover
        return PolicyTypeDescription.make_many(
            self.boto3_raw_data["PolicyTypeDescriptions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLoadBalancerPolicyTypesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLoadBalancerPolicyTypesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModifyLoadBalancerAttributesInput:
    boto3_raw_data: "type_defs.ModifyLoadBalancerAttributesInputTypeDef" = (
        dataclasses.field()
    )

    LoadBalancerName = field("LoadBalancerName")
    LoadBalancerAttributes = field("LoadBalancerAttributes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ModifyLoadBalancerAttributesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModifyLoadBalancerAttributesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccessPointsOutput:
    boto3_raw_data: "type_defs.DescribeAccessPointsOutputTypeDef" = dataclasses.field()

    @cached_property
    def LoadBalancerDescriptions(self):  # pragma: no cover
        return LoadBalancerDescription.make_many(
            self.boto3_raw_data["LoadBalancerDescriptions"]
        )

    NextMarker = field("NextMarker")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAccessPointsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccessPointsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
