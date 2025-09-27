# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_evs import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AssociateEipToVlanRequest:
    boto3_raw_data: "type_defs.AssociateEipToVlanRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    vlanName = field("vlanName")
    allocationId = field("allocationId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateEipToVlanRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateEipToVlanRequestTypeDef"]
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
class Check:
    boto3_raw_data: "type_defs.CheckTypeDef" = dataclasses.field()

    type = field("type")
    result = field("result")
    impairedSince = field("impairedSince")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CheckTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CheckTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectivityInfoOutput:
    boto3_raw_data: "type_defs.ConnectivityInfoOutputTypeDef" = dataclasses.field()

    privateRouteServerPeerings = field("privateRouteServerPeerings")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectivityInfoOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectivityInfoOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectivityInfo:
    boto3_raw_data: "type_defs.ConnectivityInfoTypeDef" = dataclasses.field()

    privateRouteServerPeerings = field("privateRouteServerPeerings")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConnectivityInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectivityInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HostInfoForCreate:
    boto3_raw_data: "type_defs.HostInfoForCreateTypeDef" = dataclasses.field()

    hostName = field("hostName")
    keyName = field("keyName")
    instanceType = field("instanceType")
    placementGroupId = field("placementGroupId")
    dedicatedHostId = field("dedicatedHostId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HostInfoForCreateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HostInfoForCreateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentSummary:
    boto3_raw_data: "type_defs.EnvironmentSummaryTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    environmentName = field("environmentName")
    vcfVersion = field("vcfVersion")
    environmentStatus = field("environmentStatus")
    environmentState = field("environmentState")
    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")
    environmentArn = field("environmentArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LicenseInfo:
    boto3_raw_data: "type_defs.LicenseInfoTypeDef" = dataclasses.field()

    solutionKey = field("solutionKey")
    vsanKey = field("vsanKey")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LicenseInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LicenseInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VcfHostnames:
    boto3_raw_data: "type_defs.VcfHostnamesTypeDef" = dataclasses.field()

    vCenter = field("vCenter")
    nsx = field("nsx")
    nsxManager1 = field("nsxManager1")
    nsxManager2 = field("nsxManager2")
    nsxManager3 = field("nsxManager3")
    nsxEdge1 = field("nsxEdge1")
    nsxEdge2 = field("nsxEdge2")
    sddcManager = field("sddcManager")
    cloudBuilder = field("cloudBuilder")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VcfHostnamesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VcfHostnamesTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEnvironmentHostRequest:
    boto3_raw_data: "type_defs.DeleteEnvironmentHostRequestTypeDef" = (
        dataclasses.field()
    )

    environmentId = field("environmentId")
    hostName = field("hostName")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEnvironmentHostRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEnvironmentHostRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEnvironmentRequest:
    boto3_raw_data: "type_defs.DeleteEnvironmentRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEnvironmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateEipFromVlanRequest:
    boto3_raw_data: "type_defs.DisassociateEipFromVlanRequestTypeDef" = (
        dataclasses.field()
    )

    environmentId = field("environmentId")
    vlanName = field("vlanName")
    associationId = field("associationId")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateEipFromVlanRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateEipFromVlanRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EipAssociation:
    boto3_raw_data: "type_defs.EipAssociationTypeDef" = dataclasses.field()

    associationId = field("associationId")
    allocationId = field("allocationId")
    ipAddress = field("ipAddress")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EipAssociationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EipAssociationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Secret:
    boto3_raw_data: "type_defs.SecretTypeDef" = dataclasses.field()

    secretArn = field("secretArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SecretTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SecretTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceAccessSecurityGroupsOutput:
    boto3_raw_data: "type_defs.ServiceAccessSecurityGroupsOutputTypeDef" = (
        dataclasses.field()
    )

    securityGroups = field("securityGroups")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ServiceAccessSecurityGroupsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceAccessSecurityGroupsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentRequest:
    boto3_raw_data: "type_defs.GetEnvironmentRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEnvironmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NetworkInterface:
    boto3_raw_data: "type_defs.NetworkInterfaceTypeDef" = dataclasses.field()

    networkInterfaceId = field("networkInterfaceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NetworkInterfaceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NetworkInterfaceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InitialVlanInfo:
    boto3_raw_data: "type_defs.InitialVlanInfoTypeDef" = dataclasses.field()

    cidr = field("cidr")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InitialVlanInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InitialVlanInfoTypeDef"]],
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
class ListEnvironmentHostsRequest:
    boto3_raw_data: "type_defs.ListEnvironmentHostsRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEnvironmentHostsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentHostsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentVlansRequest:
    boto3_raw_data: "type_defs.ListEnvironmentVlansRequestTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEnvironmentVlansRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentVlansRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentsRequest:
    boto3_raw_data: "type_defs.ListEnvironmentsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    state = field("state")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEnvironmentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceRequest:
    boto3_raw_data: "type_defs.ListTagsForResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceAccessSecurityGroups:
    boto3_raw_data: "type_defs.ServiceAccessSecurityGroupsTypeDef" = dataclasses.field()

    securityGroups = field("securityGroups")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ServiceAccessSecurityGroupsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ServiceAccessSecurityGroupsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceRequest:
    boto3_raw_data: "type_defs.UntagResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceResponse:
    boto3_raw_data: "type_defs.ListTagsForResourceResponseTypeDef" = dataclasses.field()

    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentHostRequest:
    boto3_raw_data: "type_defs.CreateEnvironmentHostRequestTypeDef" = (
        dataclasses.field()
    )

    environmentId = field("environmentId")

    @cached_property
    def host(self):  # pragma: no cover
        return HostInfoForCreate.make_one(self.boto3_raw_data["host"])

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEnvironmentHostRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentHostRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentsResponse:
    boto3_raw_data: "type_defs.ListEnvironmentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def environmentSummaries(self):  # pragma: no cover
        return EnvironmentSummary.make_many(self.boto3_raw_data["environmentSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEnvironmentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Vlan:
    boto3_raw_data: "type_defs.VlanTypeDef" = dataclasses.field()

    vlanId = field("vlanId")
    cidr = field("cidr")
    availabilityZone = field("availabilityZone")
    functionName = field("functionName")
    subnetId = field("subnetId")
    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")
    vlanState = field("vlanState")
    stateDetails = field("stateDetails")

    @cached_property
    def eipAssociations(self):  # pragma: no cover
        return EipAssociation.make_many(self.boto3_raw_data["eipAssociations"])

    isPublic = field("isPublic")
    networkAclId = field("networkAclId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VlanTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VlanTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Environment:
    boto3_raw_data: "type_defs.EnvironmentTypeDef" = dataclasses.field()

    environmentId = field("environmentId")
    environmentState = field("environmentState")
    stateDetails = field("stateDetails")
    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")
    environmentArn = field("environmentArn")
    environmentName = field("environmentName")
    vpcId = field("vpcId")
    serviceAccessSubnetId = field("serviceAccessSubnetId")
    vcfVersion = field("vcfVersion")
    termsAccepted = field("termsAccepted")

    @cached_property
    def licenseInfo(self):  # pragma: no cover
        return LicenseInfo.make_many(self.boto3_raw_data["licenseInfo"])

    siteId = field("siteId")
    environmentStatus = field("environmentStatus")

    @cached_property
    def checks(self):  # pragma: no cover
        return Check.make_many(self.boto3_raw_data["checks"])

    @cached_property
    def connectivityInfo(self):  # pragma: no cover
        return ConnectivityInfoOutput.make_one(self.boto3_raw_data["connectivityInfo"])

    @cached_property
    def vcfHostnames(self):  # pragma: no cover
        return VcfHostnames.make_one(self.boto3_raw_data["vcfHostnames"])

    kmsKeyId = field("kmsKeyId")

    @cached_property
    def serviceAccessSecurityGroups(self):  # pragma: no cover
        return ServiceAccessSecurityGroupsOutput.make_one(
            self.boto3_raw_data["serviceAccessSecurityGroups"]
        )

    @cached_property
    def credentials(self):  # pragma: no cover
        return Secret.make_many(self.boto3_raw_data["credentials"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnvironmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EnvironmentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Host:
    boto3_raw_data: "type_defs.HostTypeDef" = dataclasses.field()

    hostName = field("hostName")
    ipAddress = field("ipAddress")
    keyName = field("keyName")
    instanceType = field("instanceType")
    placementGroupId = field("placementGroupId")
    dedicatedHostId = field("dedicatedHostId")
    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")
    hostState = field("hostState")
    stateDetails = field("stateDetails")
    ec2InstanceId = field("ec2InstanceId")

    @cached_property
    def networkInterfaces(self):  # pragma: no cover
        return NetworkInterface.make_many(self.boto3_raw_data["networkInterfaces"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HostTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HostTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InitialVlans:
    boto3_raw_data: "type_defs.InitialVlansTypeDef" = dataclasses.field()

    @cached_property
    def vmkManagement(self):  # pragma: no cover
        return InitialVlanInfo.make_one(self.boto3_raw_data["vmkManagement"])

    @cached_property
    def vmManagement(self):  # pragma: no cover
        return InitialVlanInfo.make_one(self.boto3_raw_data["vmManagement"])

    @cached_property
    def vMotion(self):  # pragma: no cover
        return InitialVlanInfo.make_one(self.boto3_raw_data["vMotion"])

    @cached_property
    def vSan(self):  # pragma: no cover
        return InitialVlanInfo.make_one(self.boto3_raw_data["vSan"])

    @cached_property
    def vTep(self):  # pragma: no cover
        return InitialVlanInfo.make_one(self.boto3_raw_data["vTep"])

    @cached_property
    def edgeVTep(self):  # pragma: no cover
        return InitialVlanInfo.make_one(self.boto3_raw_data["edgeVTep"])

    @cached_property
    def nsxUplink(self):  # pragma: no cover
        return InitialVlanInfo.make_one(self.boto3_raw_data["nsxUplink"])

    @cached_property
    def hcx(self):  # pragma: no cover
        return InitialVlanInfo.make_one(self.boto3_raw_data["hcx"])

    @cached_property
    def expansionVlan1(self):  # pragma: no cover
        return InitialVlanInfo.make_one(self.boto3_raw_data["expansionVlan1"])

    @cached_property
    def expansionVlan2(self):  # pragma: no cover
        return InitialVlanInfo.make_one(self.boto3_raw_data["expansionVlan2"])

    isHcxPublic = field("isHcxPublic")
    hcxNetworkAclId = field("hcxNetworkAclId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InitialVlansTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InitialVlansTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentHostsRequestPaginate:
    boto3_raw_data: "type_defs.ListEnvironmentHostsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    environmentId = field("environmentId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEnvironmentHostsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentHostsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentVlansRequestPaginate:
    boto3_raw_data: "type_defs.ListEnvironmentVlansRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    environmentId = field("environmentId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEnvironmentVlansRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentVlansRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentsRequestPaginate:
    boto3_raw_data: "type_defs.ListEnvironmentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    state = field("state")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListEnvironmentsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateEipToVlanResponse:
    boto3_raw_data: "type_defs.AssociateEipToVlanResponseTypeDef" = dataclasses.field()

    @cached_property
    def vlan(self):  # pragma: no cover
        return Vlan.make_one(self.boto3_raw_data["vlan"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateEipToVlanResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateEipToVlanResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateEipFromVlanResponse:
    boto3_raw_data: "type_defs.DisassociateEipFromVlanResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def vlan(self):  # pragma: no cover
        return Vlan.make_one(self.boto3_raw_data["vlan"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateEipFromVlanResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateEipFromVlanResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentVlansResponse:
    boto3_raw_data: "type_defs.ListEnvironmentVlansResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def environmentVlans(self):  # pragma: no cover
        return Vlan.make_many(self.boto3_raw_data["environmentVlans"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEnvironmentVlansResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentVlansResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentResponse:
    boto3_raw_data: "type_defs.CreateEnvironmentResponseTypeDef" = dataclasses.field()

    @cached_property
    def environment(self):  # pragma: no cover
        return Environment.make_one(self.boto3_raw_data["environment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEnvironmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEnvironmentResponse:
    boto3_raw_data: "type_defs.DeleteEnvironmentResponseTypeDef" = dataclasses.field()

    @cached_property
    def environment(self):  # pragma: no cover
        return Environment.make_one(self.boto3_raw_data["environment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteEnvironmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEnvironmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentResponse:
    boto3_raw_data: "type_defs.GetEnvironmentResponseTypeDef" = dataclasses.field()

    @cached_property
    def environment(self):  # pragma: no cover
        return Environment.make_one(self.boto3_raw_data["environment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEnvironmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentHostResponse:
    boto3_raw_data: "type_defs.CreateEnvironmentHostResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def environmentSummary(self):  # pragma: no cover
        return EnvironmentSummary.make_one(self.boto3_raw_data["environmentSummary"])

    @cached_property
    def host(self):  # pragma: no cover
        return Host.make_one(self.boto3_raw_data["host"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateEnvironmentHostResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentHostResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEnvironmentHostResponse:
    boto3_raw_data: "type_defs.DeleteEnvironmentHostResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def environmentSummary(self):  # pragma: no cover
        return EnvironmentSummary.make_one(self.boto3_raw_data["environmentSummary"])

    @cached_property
    def host(self):  # pragma: no cover
        return Host.make_one(self.boto3_raw_data["host"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteEnvironmentHostResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEnvironmentHostResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEnvironmentHostsResponse:
    boto3_raw_data: "type_defs.ListEnvironmentHostsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def environmentHosts(self):  # pragma: no cover
        return Host.make_many(self.boto3_raw_data["environmentHosts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListEnvironmentHostsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEnvironmentHostsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentRequest:
    boto3_raw_data: "type_defs.CreateEnvironmentRequestTypeDef" = dataclasses.field()

    vpcId = field("vpcId")
    serviceAccessSubnetId = field("serviceAccessSubnetId")
    vcfVersion = field("vcfVersion")
    termsAccepted = field("termsAccepted")

    @cached_property
    def licenseInfo(self):  # pragma: no cover
        return LicenseInfo.make_many(self.boto3_raw_data["licenseInfo"])

    @cached_property
    def initialVlans(self):  # pragma: no cover
        return InitialVlans.make_one(self.boto3_raw_data["initialVlans"])

    @cached_property
    def hosts(self):  # pragma: no cover
        return HostInfoForCreate.make_many(self.boto3_raw_data["hosts"])

    connectivityInfo = field("connectivityInfo")

    @cached_property
    def vcfHostnames(self):  # pragma: no cover
        return VcfHostnames.make_one(self.boto3_raw_data["vcfHostnames"])

    siteId = field("siteId")
    clientToken = field("clientToken")
    environmentName = field("environmentName")
    kmsKeyId = field("kmsKeyId")
    tags = field("tags")
    serviceAccessSecurityGroups = field("serviceAccessSecurityGroups")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEnvironmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
