# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_eks import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccessConfigResponse:
    boto3_raw_data: "type_defs.AccessConfigResponseTypeDef" = dataclasses.field()

    bootstrapClusterCreatorAdminPermissions = field(
        "bootstrapClusterCreatorAdminPermissions"
    )
    authenticationMode = field("authenticationMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessEntry:
    boto3_raw_data: "type_defs.AccessEntryTypeDef" = dataclasses.field()

    clusterName = field("clusterName")
    principalArn = field("principalArn")
    kubernetesGroups = field("kubernetesGroups")
    accessEntryArn = field("accessEntryArn")
    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")
    tags = field("tags")
    username = field("username")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccessEntryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessPolicy:
    boto3_raw_data: "type_defs.AccessPolicyTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccessPolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessScopeOutput:
    boto3_raw_data: "type_defs.AccessScopeOutputTypeDef" = dataclasses.field()

    type = field("type")
    namespaces = field("namespaces")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessScopeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessScopeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessScope:
    boto3_raw_data: "type_defs.AccessScopeTypeDef" = dataclasses.field()

    type = field("type")
    namespaces = field("namespaces")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessScopeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccessScopeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddonCompatibilityDetail:
    boto3_raw_data: "type_defs.AddonCompatibilityDetailTypeDef" = dataclasses.field()

    name = field("name")
    compatibleVersions = field("compatibleVersions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddonCompatibilityDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddonCompatibilityDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddonIssue:
    boto3_raw_data: "type_defs.AddonIssueTypeDef" = dataclasses.field()

    code = field("code")
    message = field("message")
    resourceIds = field("resourceIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddonIssueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddonIssueTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MarketplaceInformation:
    boto3_raw_data: "type_defs.MarketplaceInformationTypeDef" = dataclasses.field()

    productId = field("productId")
    productUrl = field("productUrl")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MarketplaceInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MarketplaceInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddonNamespaceConfigRequest:
    boto3_raw_data: "type_defs.AddonNamespaceConfigRequestTypeDef" = dataclasses.field()

    namespace = field("namespace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddonNamespaceConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddonNamespaceConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddonNamespaceConfigResponse:
    boto3_raw_data: "type_defs.AddonNamespaceConfigResponseTypeDef" = (
        dataclasses.field()
    )

    namespace = field("namespace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddonNamespaceConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddonNamespaceConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddonPodIdentityAssociations:
    boto3_raw_data: "type_defs.AddonPodIdentityAssociationsTypeDef" = (
        dataclasses.field()
    )

    serviceAccount = field("serviceAccount")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AddonPodIdentityAssociationsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddonPodIdentityAssociationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddonPodIdentityConfiguration:
    boto3_raw_data: "type_defs.AddonPodIdentityConfigurationTypeDef" = (
        dataclasses.field()
    )

    serviceAccount = field("serviceAccount")
    recommendedManagedPolicies = field("recommendedManagedPolicies")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AddonPodIdentityConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddonPodIdentityConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Compatibility:
    boto3_raw_data: "type_defs.CompatibilityTypeDef" = dataclasses.field()

    clusterVersion = field("clusterVersion")
    platformVersions = field("platformVersions")
    defaultVersion = field("defaultVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CompatibilityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CompatibilityTypeDef"]],
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
class OidcIdentityProviderConfigRequest:
    boto3_raw_data: "type_defs.OidcIdentityProviderConfigRequestTypeDef" = (
        dataclasses.field()
    )

    identityProviderConfigName = field("identityProviderConfigName")
    issuerUrl = field("issuerUrl")
    clientId = field("clientId")
    usernameClaim = field("usernameClaim")
    usernamePrefix = field("usernamePrefix")
    groupsClaim = field("groupsClaim")
    groupsPrefix = field("groupsPrefix")
    requiredClaims = field("requiredClaims")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.OidcIdentityProviderConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OidcIdentityProviderConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AutoScalingGroup:
    boto3_raw_data: "type_defs.AutoScalingGroupTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutoScalingGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AutoScalingGroupTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BlockStorage:
    boto3_raw_data: "type_defs.BlockStorageTypeDef" = dataclasses.field()

    enabled = field("enabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BlockStorageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BlockStorageTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Certificate:
    boto3_raw_data: "type_defs.CertificateTypeDef" = dataclasses.field()

    data = field("data")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CertificateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CertificateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClientStat:
    boto3_raw_data: "type_defs.ClientStatTypeDef" = dataclasses.field()

    userAgent = field("userAgent")
    numberOfRequestsLast30Days = field("numberOfRequestsLast30Days")
    lastRequestTime = field("lastRequestTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClientStatTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClientStatTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterIssue:
    boto3_raw_data: "type_defs.ClusterIssueTypeDef" = dataclasses.field()

    code = field("code")
    message = field("message")
    resourceIds = field("resourceIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClusterIssueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClusterIssueTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeConfigResponse:
    boto3_raw_data: "type_defs.ComputeConfigResponseTypeDef" = dataclasses.field()

    enabled = field("enabled")
    nodePools = field("nodePools")
    nodeRoleArn = field("nodeRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComputeConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputeConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectorConfigResponse:
    boto3_raw_data: "type_defs.ConnectorConfigResponseTypeDef" = dataclasses.field()

    activationId = field("activationId")
    activationCode = field("activationCode")
    activationExpiry = field("activationExpiry")
    provider = field("provider")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectorConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectorConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpgradePolicyResponse:
    boto3_raw_data: "type_defs.UpgradePolicyResponseTypeDef" = dataclasses.field()

    supportType = field("supportType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpgradePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpgradePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfigResponse:
    boto3_raw_data: "type_defs.VpcConfigResponseTypeDef" = dataclasses.field()

    subnetIds = field("subnetIds")
    securityGroupIds = field("securityGroupIds")
    clusterSecurityGroupId = field("clusterSecurityGroupId")
    vpcId = field("vpcId")
    endpointPublicAccess = field("endpointPublicAccess")
    endpointPrivateAccess = field("endpointPrivateAccess")
    publicAccessCidrs = field("publicAccessCidrs")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConfigResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ZonalShiftConfigResponse:
    boto3_raw_data: "type_defs.ZonalShiftConfigResponseTypeDef" = dataclasses.field()

    enabled = field("enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ZonalShiftConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ZonalShiftConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterVersionInformation:
    boto3_raw_data: "type_defs.ClusterVersionInformationTypeDef" = dataclasses.field()

    clusterVersion = field("clusterVersion")
    clusterType = field("clusterType")
    defaultPlatformVersion = field("defaultPlatformVersion")
    defaultVersion = field("defaultVersion")
    releaseDate = field("releaseDate")
    endOfStandardSupportDate = field("endOfStandardSupportDate")
    endOfExtendedSupportDate = field("endOfExtendedSupportDate")
    status = field("status")
    versionStatus = field("versionStatus")
    kubernetesPatchVersion = field("kubernetesPatchVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ClusterVersionInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ClusterVersionInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeConfigRequest:
    boto3_raw_data: "type_defs.ComputeConfigRequestTypeDef" = dataclasses.field()

    enabled = field("enabled")
    nodePools = field("nodePools")
    nodeRoleArn = field("nodeRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComputeConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputeConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConnectorConfigRequest:
    boto3_raw_data: "type_defs.ConnectorConfigRequestTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    provider = field("provider")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConnectorConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConnectorConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ControlPlanePlacementRequest:
    boto3_raw_data: "type_defs.ControlPlanePlacementRequestTypeDef" = (
        dataclasses.field()
    )

    groupName = field("groupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ControlPlanePlacementRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ControlPlanePlacementRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ControlPlanePlacementResponse:
    boto3_raw_data: "type_defs.ControlPlanePlacementResponseTypeDef" = (
        dataclasses.field()
    )

    groupName = field("groupName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ControlPlanePlacementResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ControlPlanePlacementResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessConfigRequest:
    boto3_raw_data: "type_defs.CreateAccessConfigRequestTypeDef" = dataclasses.field()

    bootstrapClusterCreatorAdminPermissions = field(
        "bootstrapClusterCreatorAdminPermissions"
    )
    authenticationMode = field("authenticationMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccessConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessEntryRequest:
    boto3_raw_data: "type_defs.CreateAccessEntryRequestTypeDef" = dataclasses.field()

    clusterName = field("clusterName")
    principalArn = field("principalArn")
    kubernetesGroups = field("kubernetesGroups")
    tags = field("tags")
    clientRequestToken = field("clientRequestToken")
    username = field("username")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccessEntryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessEntryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpgradePolicyRequest:
    boto3_raw_data: "type_defs.UpgradePolicyRequestTypeDef" = dataclasses.field()

    supportType = field("supportType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpgradePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpgradePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcConfigRequest:
    boto3_raw_data: "type_defs.VpcConfigRequestTypeDef" = dataclasses.field()

    subnetIds = field("subnetIds")
    securityGroupIds = field("securityGroupIds")
    endpointPublicAccess = field("endpointPublicAccess")
    endpointPrivateAccess = field("endpointPrivateAccess")
    publicAccessCidrs = field("publicAccessCidrs")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcConfigRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ZonalShiftConfigRequest:
    boto3_raw_data: "type_defs.ZonalShiftConfigRequestTypeDef" = dataclasses.field()

    enabled = field("enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ZonalShiftConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ZonalShiftConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksAnywhereSubscriptionTerm:
    boto3_raw_data: "type_defs.EksAnywhereSubscriptionTermTypeDef" = dataclasses.field()

    duration = field("duration")
    unit = field("unit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EksAnywhereSubscriptionTermTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EksAnywhereSubscriptionTermTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchTemplateSpecification:
    boto3_raw_data: "type_defs.LaunchTemplateSpecificationTypeDef" = dataclasses.field()

    name = field("name")
    version = field("version")
    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LaunchTemplateSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchTemplateSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodegroupScalingConfig:
    boto3_raw_data: "type_defs.NodegroupScalingConfigTypeDef" = dataclasses.field()

    minSize = field("minSize")
    maxSize = field("maxSize")
    desiredSize = field("desiredSize")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NodegroupScalingConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodegroupScalingConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodegroupUpdateConfig:
    boto3_raw_data: "type_defs.NodegroupUpdateConfigTypeDef" = dataclasses.field()

    maxUnavailable = field("maxUnavailable")
    maxUnavailablePercentage = field("maxUnavailablePercentage")
    updateStrategy = field("updateStrategy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NodegroupUpdateConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodegroupUpdateConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Taint:
    boto3_raw_data: "type_defs.TaintTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")
    effect = field("effect")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TaintTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TaintTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePodIdentityAssociationRequest:
    boto3_raw_data: "type_defs.CreatePodIdentityAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")
    namespace = field("namespace")
    serviceAccount = field("serviceAccount")
    roleArn = field("roleArn")
    clientRequestToken = field("clientRequestToken")
    tags = field("tags")
    disableSessionTags = field("disableSessionTags")
    targetRoleArn = field("targetRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePodIdentityAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePodIdentityAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PodIdentityAssociation:
    boto3_raw_data: "type_defs.PodIdentityAssociationTypeDef" = dataclasses.field()

    clusterName = field("clusterName")
    namespace = field("namespace")
    serviceAccount = field("serviceAccount")
    roleArn = field("roleArn")
    associationArn = field("associationArn")
    associationId = field("associationId")
    tags = field("tags")
    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")
    ownerArn = field("ownerArn")
    disableSessionTags = field("disableSessionTags")
    targetRoleArn = field("targetRoleArn")
    externalId = field("externalId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PodIdentityAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PodIdentityAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccessEntryRequest:
    boto3_raw_data: "type_defs.DeleteAccessEntryRequestTypeDef" = dataclasses.field()

    clusterName = field("clusterName")
    principalArn = field("principalArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAccessEntryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccessEntryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAddonRequest:
    boto3_raw_data: "type_defs.DeleteAddonRequestTypeDef" = dataclasses.field()

    clusterName = field("clusterName")
    addonName = field("addonName")
    preserve = field("preserve")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAddonRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAddonRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteClusterRequest:
    boto3_raw_data: "type_defs.DeleteClusterRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEksAnywhereSubscriptionRequest:
    boto3_raw_data: "type_defs.DeleteEksAnywhereSubscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteEksAnywhereSubscriptionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEksAnywhereSubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFargateProfileRequest:
    boto3_raw_data: "type_defs.DeleteFargateProfileRequestTypeDef" = dataclasses.field()

    clusterName = field("clusterName")
    fargateProfileName = field("fargateProfileName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFargateProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFargateProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteNodegroupRequest:
    boto3_raw_data: "type_defs.DeleteNodegroupRequestTypeDef" = dataclasses.field()

    clusterName = field("clusterName")
    nodegroupName = field("nodegroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteNodegroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteNodegroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePodIdentityAssociationRequest:
    boto3_raw_data: "type_defs.DeletePodIdentityAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")
    associationId = field("associationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeletePodIdentityAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePodIdentityAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterClusterRequest:
    boto3_raw_data: "type_defs.DeregisterClusterRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeregisterClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccessEntryRequest:
    boto3_raw_data: "type_defs.DescribeAccessEntryRequestTypeDef" = dataclasses.field()

    clusterName = field("clusterName")
    principalArn = field("principalArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAccessEntryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccessEntryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAddonConfigurationRequest:
    boto3_raw_data: "type_defs.DescribeAddonConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    addonName = field("addonName")
    addonVersion = field("addonVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAddonConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAddonConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAddonRequest:
    boto3_raw_data: "type_defs.DescribeAddonRequestTypeDef" = dataclasses.field()

    clusterName = field("clusterName")
    addonName = field("addonName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAddonRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAddonRequestTypeDef"]
        ],
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
class DescribeAddonVersionsRequest:
    boto3_raw_data: "type_defs.DescribeAddonVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    kubernetesVersion = field("kubernetesVersion")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    addonName = field("addonName")
    types = field("types")
    publishers = field("publishers")
    owners = field("owners")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAddonVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAddonVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterRequest:
    boto3_raw_data: "type_defs.DescribeClusterRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterVersionsRequest:
    boto3_raw_data: "type_defs.DescribeClusterVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    clusterType = field("clusterType")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    defaultOnly = field("defaultOnly")
    includeAll = field("includeAll")
    clusterVersions = field("clusterVersions")
    status = field("status")
    versionStatus = field("versionStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeClusterVersionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterVersionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEksAnywhereSubscriptionRequest:
    boto3_raw_data: "type_defs.DescribeEksAnywhereSubscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEksAnywhereSubscriptionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEksAnywhereSubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFargateProfileRequest:
    boto3_raw_data: "type_defs.DescribeFargateProfileRequestTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")
    fargateProfileName = field("fargateProfileName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFargateProfileRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFargateProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityProviderConfig:
    boto3_raw_data: "type_defs.IdentityProviderConfigTypeDef" = dataclasses.field()

    type = field("type")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdentityProviderConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityProviderConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInsightRequest:
    boto3_raw_data: "type_defs.DescribeInsightRequestTypeDef" = dataclasses.field()

    clusterName = field("clusterName")
    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeInsightRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInsightRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInsightsRefreshRequest:
    boto3_raw_data: "type_defs.DescribeInsightsRefreshRequestTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeInsightsRefreshRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInsightsRefreshRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNodegroupRequest:
    boto3_raw_data: "type_defs.DescribeNodegroupRequestTypeDef" = dataclasses.field()

    clusterName = field("clusterName")
    nodegroupName = field("nodegroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeNodegroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNodegroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePodIdentityAssociationRequest:
    boto3_raw_data: "type_defs.DescribePodIdentityAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")
    associationId = field("associationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePodIdentityAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePodIdentityAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUpdateRequest:
    boto3_raw_data: "type_defs.DescribeUpdateRequestTypeDef" = dataclasses.field()

    name = field("name")
    updateId = field("updateId")
    nodegroupName = field("nodegroupName")
    addonName = field("addonName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUpdateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUpdateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateAccessPolicyRequest:
    boto3_raw_data: "type_defs.DisassociateAccessPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")
    principalArn = field("principalArn")
    policyArn = field("policyArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateAccessPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateAccessPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class License:
    boto3_raw_data: "type_defs.LicenseTypeDef" = dataclasses.field()

    id = field("id")
    token = field("token")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LicenseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LicenseTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ElasticLoadBalancing:
    boto3_raw_data: "type_defs.ElasticLoadBalancingTypeDef" = dataclasses.field()

    enabled = field("enabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ElasticLoadBalancingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ElasticLoadBalancingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Provider:
    boto3_raw_data: "type_defs.ProviderTypeDef" = dataclasses.field()

    keyArn = field("keyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProviderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProviderTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorDetail:
    boto3_raw_data: "type_defs.ErrorDetailTypeDef" = dataclasses.field()

    errorCode = field("errorCode")
    errorMessage = field("errorMessage")
    resourceIds = field("resourceIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ErrorDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ErrorDetailTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FargateProfileIssue:
    boto3_raw_data: "type_defs.FargateProfileIssueTypeDef" = dataclasses.field()

    code = field("code")
    message = field("message")
    resourceIds = field("resourceIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FargateProfileIssueTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FargateProfileIssueTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FargateProfileSelectorOutput:
    boto3_raw_data: "type_defs.FargateProfileSelectorOutputTypeDef" = (
        dataclasses.field()
    )

    namespace = field("namespace")
    labels = field("labels")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FargateProfileSelectorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FargateProfileSelectorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FargateProfileSelector:
    boto3_raw_data: "type_defs.FargateProfileSelectorTypeDef" = dataclasses.field()

    namespace = field("namespace")
    labels = field("labels")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FargateProfileSelectorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FargateProfileSelectorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OidcIdentityProviderConfig:
    boto3_raw_data: "type_defs.OidcIdentityProviderConfigTypeDef" = dataclasses.field()

    identityProviderConfigName = field("identityProviderConfigName")
    identityProviderConfigArn = field("identityProviderConfigArn")
    clusterName = field("clusterName")
    issuerUrl = field("issuerUrl")
    clientId = field("clientId")
    usernameClaim = field("usernameClaim")
    usernamePrefix = field("usernamePrefix")
    groupsClaim = field("groupsClaim")
    groupsPrefix = field("groupsPrefix")
    requiredClaims = field("requiredClaims")
    tags = field("tags")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OidcIdentityProviderConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OidcIdentityProviderConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OIDC:
    boto3_raw_data: "type_defs.OIDCTypeDef" = dataclasses.field()

    issuer = field("issuer")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OIDCTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OIDCTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InsightStatus:
    boto3_raw_data: "type_defs.InsightStatusTypeDef" = dataclasses.field()

    status = field("status")
    reason = field("reason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InsightStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InsightStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InsightsFilter:
    boto3_raw_data: "type_defs.InsightsFilterTypeDef" = dataclasses.field()

    categories = field("categories")
    kubernetesVersions = field("kubernetesVersions")
    statuses = field("statuses")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InsightsFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InsightsFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Issue:
    boto3_raw_data: "type_defs.IssueTypeDef" = dataclasses.field()

    code = field("code")
    message = field("message")
    resourceIds = field("resourceIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IssueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IssueTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessEntriesRequest:
    boto3_raw_data: "type_defs.ListAccessEntriesRequestTypeDef" = dataclasses.field()

    clusterName = field("clusterName")
    associatedPolicyArn = field("associatedPolicyArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccessEntriesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessEntriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessPoliciesRequest:
    boto3_raw_data: "type_defs.ListAccessPoliciesRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccessPoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAddonsRequest:
    boto3_raw_data: "type_defs.ListAddonsRequestTypeDef" = dataclasses.field()

    clusterName = field("clusterName")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListAddonsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAddonsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociatedAccessPoliciesRequest:
    boto3_raw_data: "type_defs.ListAssociatedAccessPoliciesRequestTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")
    principalArn = field("principalArn")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssociatedAccessPoliciesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssociatedAccessPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClustersRequest:
    boto3_raw_data: "type_defs.ListClustersRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    include = field("include")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListClustersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClustersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEksAnywhereSubscriptionsRequest:
    boto3_raw_data: "type_defs.ListEksAnywhereSubscriptionsRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    includeStatus = field("includeStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEksAnywhereSubscriptionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEksAnywhereSubscriptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFargateProfilesRequest:
    boto3_raw_data: "type_defs.ListFargateProfilesRequestTypeDef" = dataclasses.field()

    clusterName = field("clusterName")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFargateProfilesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFargateProfilesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentityProviderConfigsRequest:
    boto3_raw_data: "type_defs.ListIdentityProviderConfigsRequestTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListIdentityProviderConfigsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentityProviderConfigsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNodegroupsRequest:
    boto3_raw_data: "type_defs.ListNodegroupsRequestTypeDef" = dataclasses.field()

    clusterName = field("clusterName")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNodegroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNodegroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPodIdentityAssociationsRequest:
    boto3_raw_data: "type_defs.ListPodIdentityAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")
    namespace = field("namespace")
    serviceAccount = field("serviceAccount")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPodIdentityAssociationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPodIdentityAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PodIdentityAssociationSummary:
    boto3_raw_data: "type_defs.PodIdentityAssociationSummaryTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")
    namespace = field("namespace")
    serviceAccount = field("serviceAccount")
    associationArn = field("associationArn")
    associationId = field("associationId")
    ownerArn = field("ownerArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PodIdentityAssociationSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PodIdentityAssociationSummaryTypeDef"]
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
class ListUpdatesRequest:
    boto3_raw_data: "type_defs.ListUpdatesRequestTypeDef" = dataclasses.field()

    name = field("name")
    nodegroupName = field("nodegroupName")
    addonName = field("addonName")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUpdatesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUpdatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogSetupOutput:
    boto3_raw_data: "type_defs.LogSetupOutputTypeDef" = dataclasses.field()

    types = field("types")
    enabled = field("enabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogSetupOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LogSetupOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogSetup:
    boto3_raw_data: "type_defs.LogSetupTypeDef" = dataclasses.field()

    types = field("types")
    enabled = field("enabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogSetupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LogSetupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeRepairConfigOverrides:
    boto3_raw_data: "type_defs.NodeRepairConfigOverridesTypeDef" = dataclasses.field()

    nodeMonitoringCondition = field("nodeMonitoringCondition")
    nodeUnhealthyReason = field("nodeUnhealthyReason")
    minRepairWaitTimeMins = field("minRepairWaitTimeMins")
    repairAction = field("repairAction")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NodeRepairConfigOverridesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeRepairConfigOverridesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoteAccessConfigOutput:
    boto3_raw_data: "type_defs.RemoteAccessConfigOutputTypeDef" = dataclasses.field()

    ec2SshKey = field("ec2SshKey")
    sourceSecurityGroups = field("sourceSecurityGroups")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoteAccessConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoteAccessConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoteAccessConfig:
    boto3_raw_data: "type_defs.RemoteAccessConfigTypeDef" = dataclasses.field()

    ec2SshKey = field("ec2SshKey")
    sourceSecurityGroups = field("sourceSecurityGroups")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoteAccessConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoteAccessConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoteNodeNetworkOutput:
    boto3_raw_data: "type_defs.RemoteNodeNetworkOutputTypeDef" = dataclasses.field()

    cidrs = field("cidrs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoteNodeNetworkOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoteNodeNetworkOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemotePodNetworkOutput:
    boto3_raw_data: "type_defs.RemotePodNetworkOutputTypeDef" = dataclasses.field()

    cidrs = field("cidrs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemotePodNetworkOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemotePodNetworkOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoteNodeNetwork:
    boto3_raw_data: "type_defs.RemoteNodeNetworkTypeDef" = dataclasses.field()

    cidrs = field("cidrs")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RemoteNodeNetworkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoteNodeNetworkTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemotePodNetwork:
    boto3_raw_data: "type_defs.RemotePodNetworkTypeDef" = dataclasses.field()

    cidrs = field("cidrs")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RemotePodNetworkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemotePodNetworkTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartInsightsRefreshRequest:
    boto3_raw_data: "type_defs.StartInsightsRefreshRequestTypeDef" = dataclasses.field()

    clusterName = field("clusterName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartInsightsRefreshRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartInsightsRefreshRequestTypeDef"]
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
class UpdateAccessConfigRequest:
    boto3_raw_data: "type_defs.UpdateAccessConfigRequestTypeDef" = dataclasses.field()

    authenticationMode = field("authenticationMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAccessConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccessConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccessEntryRequest:
    boto3_raw_data: "type_defs.UpdateAccessEntryRequestTypeDef" = dataclasses.field()

    clusterName = field("clusterName")
    principalArn = field("principalArn")
    kubernetesGroups = field("kubernetesGroups")
    clientRequestToken = field("clientRequestToken")
    username = field("username")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAccessEntryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccessEntryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateClusterVersionRequest:
    boto3_raw_data: "type_defs.UpdateClusterVersionRequestTypeDef" = dataclasses.field()

    name = field("name")
    version = field("version")
    clientRequestToken = field("clientRequestToken")
    force = field("force")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateClusterVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateClusterVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEksAnywhereSubscriptionRequest:
    boto3_raw_data: "type_defs.UpdateEksAnywhereSubscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    autoRenew = field("autoRenew")
    clientRequestToken = field("clientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateEksAnywhereSubscriptionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEksAnywhereSubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLabelsPayload:
    boto3_raw_data: "type_defs.UpdateLabelsPayloadTypeDef" = dataclasses.field()

    addOrUpdateLabels = field("addOrUpdateLabels")
    removeLabels = field("removeLabels")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLabelsPayloadTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLabelsPayloadTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateParam:
    boto3_raw_data: "type_defs.UpdateParamTypeDef" = dataclasses.field()

    type = field("type")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateParamTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateParamTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePodIdentityAssociationRequest:
    boto3_raw_data: "type_defs.UpdatePodIdentityAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")
    associationId = field("associationId")
    roleArn = field("roleArn")
    clientRequestToken = field("clientRequestToken")
    disableSessionTags = field("disableSessionTags")
    targetRoleArn = field("targetRoleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePodIdentityAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePodIdentityAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociatedAccessPolicy:
    boto3_raw_data: "type_defs.AssociatedAccessPolicyTypeDef" = dataclasses.field()

    policyArn = field("policyArn")

    @cached_property
    def accessScope(self):  # pragma: no cover
        return AccessScopeOutput.make_one(self.boto3_raw_data["accessScope"])

    associatedAt = field("associatedAt")
    modifiedAt = field("modifiedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociatedAccessPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociatedAccessPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddonHealth:
    boto3_raw_data: "type_defs.AddonHealthTypeDef" = dataclasses.field()

    @cached_property
    def issues(self):  # pragma: no cover
        return AddonIssue.make_many(self.boto3_raw_data["issues"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddonHealthTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddonHealthTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAddonRequest:
    boto3_raw_data: "type_defs.CreateAddonRequestTypeDef" = dataclasses.field()

    clusterName = field("clusterName")
    addonName = field("addonName")
    addonVersion = field("addonVersion")
    serviceAccountRoleArn = field("serviceAccountRoleArn")
    resolveConflicts = field("resolveConflicts")
    clientRequestToken = field("clientRequestToken")
    tags = field("tags")
    configurationValues = field("configurationValues")

    @cached_property
    def podIdentityAssociations(self):  # pragma: no cover
        return AddonPodIdentityAssociations.make_many(
            self.boto3_raw_data["podIdentityAssociations"]
        )

    @cached_property
    def namespaceConfig(self):  # pragma: no cover
        return AddonNamespaceConfigRequest.make_one(
            self.boto3_raw_data["namespaceConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAddonRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAddonRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAddonRequest:
    boto3_raw_data: "type_defs.UpdateAddonRequestTypeDef" = dataclasses.field()

    clusterName = field("clusterName")
    addonName = field("addonName")
    addonVersion = field("addonVersion")
    serviceAccountRoleArn = field("serviceAccountRoleArn")
    resolveConflicts = field("resolveConflicts")
    clientRequestToken = field("clientRequestToken")
    configurationValues = field("configurationValues")

    @cached_property
    def podIdentityAssociations(self):  # pragma: no cover
        return AddonPodIdentityAssociations.make_many(
            self.boto3_raw_data["podIdentityAssociations"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAddonRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAddonRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddonVersionInfo:
    boto3_raw_data: "type_defs.AddonVersionInfoTypeDef" = dataclasses.field()

    addonVersion = field("addonVersion")
    architecture = field("architecture")
    computeTypes = field("computeTypes")

    @cached_property
    def compatibilities(self):  # pragma: no cover
        return Compatibility.make_many(self.boto3_raw_data["compatibilities"])

    requiresConfiguration = field("requiresConfiguration")
    requiresIamPermissions = field("requiresIamPermissions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddonVersionInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AddonVersionInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessEntryResponse:
    boto3_raw_data: "type_defs.CreateAccessEntryResponseTypeDef" = dataclasses.field()

    @cached_property
    def accessEntry(self):  # pragma: no cover
        return AccessEntry.make_one(self.boto3_raw_data["accessEntry"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccessEntryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessEntryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccessEntryResponse:
    boto3_raw_data: "type_defs.DescribeAccessEntryResponseTypeDef" = dataclasses.field()

    @cached_property
    def accessEntry(self):  # pragma: no cover
        return AccessEntry.make_one(self.boto3_raw_data["accessEntry"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAccessEntryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccessEntryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAddonConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeAddonConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    addonName = field("addonName")
    addonVersion = field("addonVersion")
    configurationSchema = field("configurationSchema")

    @cached_property
    def podIdentityConfiguration(self):  # pragma: no cover
        return AddonPodIdentityConfiguration.make_many(
            self.boto3_raw_data["podIdentityConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAddonConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAddonConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInsightsRefreshResponse:
    boto3_raw_data: "type_defs.DescribeInsightsRefreshResponseTypeDef" = (
        dataclasses.field()
    )

    message = field("message")
    status = field("status")
    startedAt = field("startedAt")
    endedAt = field("endedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeInsightsRefreshResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInsightsRefreshResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessEntriesResponse:
    boto3_raw_data: "type_defs.ListAccessEntriesResponseTypeDef" = dataclasses.field()

    accessEntries = field("accessEntries")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccessEntriesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessEntriesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessPoliciesResponse:
    boto3_raw_data: "type_defs.ListAccessPoliciesResponseTypeDef" = dataclasses.field()

    @cached_property
    def accessPolicies(self):  # pragma: no cover
        return AccessPolicy.make_many(self.boto3_raw_data["accessPolicies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAccessPoliciesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAddonsResponse:
    boto3_raw_data: "type_defs.ListAddonsResponseTypeDef" = dataclasses.field()

    addons = field("addons")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAddonsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAddonsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClustersResponse:
    boto3_raw_data: "type_defs.ListClustersResponseTypeDef" = dataclasses.field()

    clusters = field("clusters")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListClustersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClustersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFargateProfilesResponse:
    boto3_raw_data: "type_defs.ListFargateProfilesResponseTypeDef" = dataclasses.field()

    fargateProfileNames = field("fargateProfileNames")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFargateProfilesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFargateProfilesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNodegroupsResponse:
    boto3_raw_data: "type_defs.ListNodegroupsResponseTypeDef" = dataclasses.field()

    nodegroups = field("nodegroups")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNodegroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNodegroupsResponseTypeDef"]
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
class ListUpdatesResponse:
    boto3_raw_data: "type_defs.ListUpdatesResponseTypeDef" = dataclasses.field()

    updateIds = field("updateIds")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUpdatesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUpdatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartInsightsRefreshResponse:
    boto3_raw_data: "type_defs.StartInsightsRefreshResponseTypeDef" = (
        dataclasses.field()
    )

    message = field("message")
    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartInsightsRefreshResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartInsightsRefreshResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccessEntryResponse:
    boto3_raw_data: "type_defs.UpdateAccessEntryResponseTypeDef" = dataclasses.field()

    @cached_property
    def accessEntry(self):  # pragma: no cover
        return AccessEntry.make_one(self.boto3_raw_data["accessEntry"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAccessEntryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccessEntryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateIdentityProviderConfigRequest:
    boto3_raw_data: "type_defs.AssociateIdentityProviderConfigRequestTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")

    @cached_property
    def oidc(self):  # pragma: no cover
        return OidcIdentityProviderConfigRequest.make_one(self.boto3_raw_data["oidc"])

    tags = field("tags")
    clientRequestToken = field("clientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateIdentityProviderConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateIdentityProviderConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodegroupResources:
    boto3_raw_data: "type_defs.NodegroupResourcesTypeDef" = dataclasses.field()

    @cached_property
    def autoScalingGroups(self):  # pragma: no cover
        return AutoScalingGroup.make_many(self.boto3_raw_data["autoScalingGroups"])

    remoteAccessSecurityGroup = field("remoteAccessSecurityGroup")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NodegroupResourcesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodegroupResourcesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageConfigRequest:
    boto3_raw_data: "type_defs.StorageConfigRequestTypeDef" = dataclasses.field()

    @cached_property
    def blockStorage(self):  # pragma: no cover
        return BlockStorage.make_one(self.boto3_raw_data["blockStorage"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StorageConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StorageConfigResponse:
    boto3_raw_data: "type_defs.StorageConfigResponseTypeDef" = dataclasses.field()

    @cached_property
    def blockStorage(self):  # pragma: no cover
        return BlockStorage.make_one(self.boto3_raw_data["blockStorage"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StorageConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StorageConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeprecationDetail:
    boto3_raw_data: "type_defs.DeprecationDetailTypeDef" = dataclasses.field()

    usage = field("usage")
    replacedWith = field("replacedWith")
    stopServingVersion = field("stopServingVersion")
    startServingReplacementVersion = field("startServingReplacementVersion")

    @cached_property
    def clientStats(self):  # pragma: no cover
        return ClientStat.make_many(self.boto3_raw_data["clientStats"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeprecationDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeprecationDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ClusterHealth:
    boto3_raw_data: "type_defs.ClusterHealthTypeDef" = dataclasses.field()

    @cached_property
    def issues(self):  # pragma: no cover
        return ClusterIssue.make_many(self.boto3_raw_data["issues"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClusterHealthTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClusterHealthTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterVersionsResponse:
    boto3_raw_data: "type_defs.DescribeClusterVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def clusterVersions(self):  # pragma: no cover
        return ClusterVersionInformation.make_many(
            self.boto3_raw_data["clusterVersions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeClusterVersionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterClusterRequest:
    boto3_raw_data: "type_defs.RegisterClusterRequestTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def connectorConfig(self):  # pragma: no cover
        return ConnectorConfigRequest.make_one(self.boto3_raw_data["connectorConfig"])

    clientRequestToken = field("clientRequestToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutpostConfigRequest:
    boto3_raw_data: "type_defs.OutpostConfigRequestTypeDef" = dataclasses.field()

    outpostArns = field("outpostArns")
    controlPlaneInstanceType = field("controlPlaneInstanceType")

    @cached_property
    def controlPlanePlacement(self):  # pragma: no cover
        return ControlPlanePlacementRequest.make_one(
            self.boto3_raw_data["controlPlanePlacement"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutpostConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutpostConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutpostConfigResponse:
    boto3_raw_data: "type_defs.OutpostConfigResponseTypeDef" = dataclasses.field()

    outpostArns = field("outpostArns")
    controlPlaneInstanceType = field("controlPlaneInstanceType")

    @cached_property
    def controlPlanePlacement(self):  # pragma: no cover
        return ControlPlanePlacementResponse.make_one(
            self.boto3_raw_data["controlPlanePlacement"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OutpostConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OutpostConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEksAnywhereSubscriptionRequest:
    boto3_raw_data: "type_defs.CreateEksAnywhereSubscriptionRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def term(self):  # pragma: no cover
        return EksAnywhereSubscriptionTerm.make_one(self.boto3_raw_data["term"])

    licenseQuantity = field("licenseQuantity")
    licenseType = field("licenseType")
    autoRenew = field("autoRenew")
    clientRequestToken = field("clientRequestToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateEksAnywhereSubscriptionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEksAnywhereSubscriptionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNodegroupVersionRequest:
    boto3_raw_data: "type_defs.UpdateNodegroupVersionRequestTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")
    nodegroupName = field("nodegroupName")
    version = field("version")
    releaseVersion = field("releaseVersion")

    @cached_property
    def launchTemplate(self):  # pragma: no cover
        return LaunchTemplateSpecification.make_one(
            self.boto3_raw_data["launchTemplate"]
        )

    force = field("force")
    clientRequestToken = field("clientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateNodegroupVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNodegroupVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTaintsPayload:
    boto3_raw_data: "type_defs.UpdateTaintsPayloadTypeDef" = dataclasses.field()

    @cached_property
    def addOrUpdateTaints(self):  # pragma: no cover
        return Taint.make_many(self.boto3_raw_data["addOrUpdateTaints"])

    @cached_property
    def removeTaints(self):  # pragma: no cover
        return Taint.make_many(self.boto3_raw_data["removeTaints"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTaintsPayloadTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTaintsPayloadTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePodIdentityAssociationResponse:
    boto3_raw_data: "type_defs.CreatePodIdentityAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def association(self):  # pragma: no cover
        return PodIdentityAssociation.make_one(self.boto3_raw_data["association"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePodIdentityAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePodIdentityAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePodIdentityAssociationResponse:
    boto3_raw_data: "type_defs.DeletePodIdentityAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def association(self):  # pragma: no cover
        return PodIdentityAssociation.make_one(self.boto3_raw_data["association"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeletePodIdentityAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePodIdentityAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePodIdentityAssociationResponse:
    boto3_raw_data: "type_defs.DescribePodIdentityAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def association(self):  # pragma: no cover
        return PodIdentityAssociation.make_one(self.boto3_raw_data["association"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribePodIdentityAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePodIdentityAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePodIdentityAssociationResponse:
    boto3_raw_data: "type_defs.UpdatePodIdentityAssociationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def association(self):  # pragma: no cover
        return PodIdentityAssociation.make_one(self.boto3_raw_data["association"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePodIdentityAssociationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePodIdentityAssociationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAddonRequestWaitExtra:
    boto3_raw_data: "type_defs.DescribeAddonRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")
    addonName = field("addonName")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAddonRequestWaitExtraTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAddonRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAddonRequestWait:
    boto3_raw_data: "type_defs.DescribeAddonRequestWaitTypeDef" = dataclasses.field()

    clusterName = field("clusterName")
    addonName = field("addonName")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAddonRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAddonRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterRequestWaitExtra:
    boto3_raw_data: "type_defs.DescribeClusterRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeClusterRequestWaitExtraTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterRequestWait:
    boto3_raw_data: "type_defs.DescribeClusterRequestWaitTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeClusterRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFargateProfileRequestWaitExtra:
    boto3_raw_data: "type_defs.DescribeFargateProfileRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")
    fargateProfileName = field("fargateProfileName")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFargateProfileRequestWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFargateProfileRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFargateProfileRequestWait:
    boto3_raw_data: "type_defs.DescribeFargateProfileRequestWaitTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")
    fargateProfileName = field("fargateProfileName")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeFargateProfileRequestWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFargateProfileRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNodegroupRequestWaitExtra:
    boto3_raw_data: "type_defs.DescribeNodegroupRequestWaitExtraTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")
    nodegroupName = field("nodegroupName")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeNodegroupRequestWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNodegroupRequestWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNodegroupRequestWait:
    boto3_raw_data: "type_defs.DescribeNodegroupRequestWaitTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")
    nodegroupName = field("nodegroupName")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeNodegroupRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNodegroupRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAddonVersionsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeAddonVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    kubernetesVersion = field("kubernetesVersion")
    addonName = field("addonName")
    types = field("types")
    publishers = field("publishers")
    owners = field("owners")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAddonVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAddonVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterVersionsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeClusterVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    clusterType = field("clusterType")
    defaultOnly = field("defaultOnly")
    includeAll = field("includeAll")
    clusterVersions = field("clusterVersions")
    status = field("status")
    versionStatus = field("versionStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeClusterVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessEntriesRequestPaginate:
    boto3_raw_data: "type_defs.ListAccessEntriesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")
    associatedPolicyArn = field("associatedPolicyArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAccessEntriesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessEntriesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAccessPoliciesRequestPaginate:
    boto3_raw_data: "type_defs.ListAccessPoliciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAccessPoliciesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAccessPoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAddonsRequestPaginate:
    boto3_raw_data: "type_defs.ListAddonsRequestPaginateTypeDef" = dataclasses.field()

    clusterName = field("clusterName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAddonsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAddonsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociatedAccessPoliciesRequestPaginate:
    boto3_raw_data: "type_defs.ListAssociatedAccessPoliciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")
    principalArn = field("principalArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssociatedAccessPoliciesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssociatedAccessPoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListClustersRequestPaginate:
    boto3_raw_data: "type_defs.ListClustersRequestPaginateTypeDef" = dataclasses.field()

    include = field("include")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListClustersRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListClustersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEksAnywhereSubscriptionsRequestPaginate:
    boto3_raw_data: "type_defs.ListEksAnywhereSubscriptionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    includeStatus = field("includeStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEksAnywhereSubscriptionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEksAnywhereSubscriptionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFargateProfilesRequestPaginate:
    boto3_raw_data: "type_defs.ListFargateProfilesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListFargateProfilesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFargateProfilesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentityProviderConfigsRequestPaginate:
    boto3_raw_data: "type_defs.ListIdentityProviderConfigsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListIdentityProviderConfigsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentityProviderConfigsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNodegroupsRequestPaginate:
    boto3_raw_data: "type_defs.ListNodegroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListNodegroupsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNodegroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPodIdentityAssociationsRequestPaginate:
    boto3_raw_data: "type_defs.ListPodIdentityAssociationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")
    namespace = field("namespace")
    serviceAccount = field("serviceAccount")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPodIdentityAssociationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPodIdentityAssociationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListUpdatesRequestPaginate:
    boto3_raw_data: "type_defs.ListUpdatesRequestPaginateTypeDef" = dataclasses.field()

    name = field("name")
    nodegroupName = field("nodegroupName")
    addonName = field("addonName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListUpdatesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListUpdatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIdentityProviderConfigRequest:
    boto3_raw_data: "type_defs.DescribeIdentityProviderConfigRequestTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")

    @cached_property
    def identityProviderConfig(self):  # pragma: no cover
        return IdentityProviderConfig.make_one(
            self.boto3_raw_data["identityProviderConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeIdentityProviderConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIdentityProviderConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateIdentityProviderConfigRequest:
    boto3_raw_data: "type_defs.DisassociateIdentityProviderConfigRequestTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")

    @cached_property
    def identityProviderConfig(self):  # pragma: no cover
        return IdentityProviderConfig.make_one(
            self.boto3_raw_data["identityProviderConfig"]
        )

    clientRequestToken = field("clientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateIdentityProviderConfigRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateIdentityProviderConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdentityProviderConfigsResponse:
    boto3_raw_data: "type_defs.ListIdentityProviderConfigsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def identityProviderConfigs(self):  # pragma: no cover
        return IdentityProviderConfig.make_many(
            self.boto3_raw_data["identityProviderConfigs"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListIdentityProviderConfigsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdentityProviderConfigsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksAnywhereSubscription:
    boto3_raw_data: "type_defs.EksAnywhereSubscriptionTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    createdAt = field("createdAt")
    effectiveDate = field("effectiveDate")
    expirationDate = field("expirationDate")
    licenseQuantity = field("licenseQuantity")
    licenseType = field("licenseType")

    @cached_property
    def term(self):  # pragma: no cover
        return EksAnywhereSubscriptionTerm.make_one(self.boto3_raw_data["term"])

    status = field("status")
    autoRenew = field("autoRenew")
    licenseArns = field("licenseArns")

    @cached_property
    def licenses(self):  # pragma: no cover
        return License.make_many(self.boto3_raw_data["licenses"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EksAnywhereSubscriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EksAnywhereSubscriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KubernetesNetworkConfigRequest:
    boto3_raw_data: "type_defs.KubernetesNetworkConfigRequestTypeDef" = (
        dataclasses.field()
    )

    serviceIpv4Cidr = field("serviceIpv4Cidr")
    ipFamily = field("ipFamily")

    @cached_property
    def elasticLoadBalancing(self):  # pragma: no cover
        return ElasticLoadBalancing.make_one(
            self.boto3_raw_data["elasticLoadBalancing"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KubernetesNetworkConfigRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KubernetesNetworkConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class KubernetesNetworkConfigResponse:
    boto3_raw_data: "type_defs.KubernetesNetworkConfigResponseTypeDef" = (
        dataclasses.field()
    )

    serviceIpv4Cidr = field("serviceIpv4Cidr")
    serviceIpv6Cidr = field("serviceIpv6Cidr")
    ipFamily = field("ipFamily")

    @cached_property
    def elasticLoadBalancing(self):  # pragma: no cover
        return ElasticLoadBalancing.make_one(
            self.boto3_raw_data["elasticLoadBalancing"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.KubernetesNetworkConfigResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.KubernetesNetworkConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionConfigOutput:
    boto3_raw_data: "type_defs.EncryptionConfigOutputTypeDef" = dataclasses.field()

    resources = field("resources")

    @cached_property
    def provider(self):  # pragma: no cover
        return Provider.make_one(self.boto3_raw_data["provider"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncryptionConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionConfig:
    boto3_raw_data: "type_defs.EncryptionConfigTypeDef" = dataclasses.field()

    resources = field("resources")

    @cached_property
    def provider(self):  # pragma: no cover
        return Provider.make_one(self.boto3_raw_data["provider"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EncryptionConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FargateProfileHealth:
    boto3_raw_data: "type_defs.FargateProfileHealthTypeDef" = dataclasses.field()

    @cached_property
    def issues(self):  # pragma: no cover
        return FargateProfileIssue.make_many(self.boto3_raw_data["issues"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FargateProfileHealthTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FargateProfileHealthTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdentityProviderConfigResponse:
    boto3_raw_data: "type_defs.IdentityProviderConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def oidc(self):  # pragma: no cover
        return OidcIdentityProviderConfig.make_one(self.boto3_raw_data["oidc"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IdentityProviderConfigResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdentityProviderConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Identity:
    boto3_raw_data: "type_defs.IdentityTypeDef" = dataclasses.field()

    @cached_property
    def oidc(self):  # pragma: no cover
        return OIDC.make_one(self.boto3_raw_data["oidc"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IdentityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IdentityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InsightResourceDetail:
    boto3_raw_data: "type_defs.InsightResourceDetailTypeDef" = dataclasses.field()

    @cached_property
    def insightStatus(self):  # pragma: no cover
        return InsightStatus.make_one(self.boto3_raw_data["insightStatus"])

    kubernetesResourceUri = field("kubernetesResourceUri")
    arn = field("arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InsightResourceDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InsightResourceDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InsightSummary:
    boto3_raw_data: "type_defs.InsightSummaryTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    category = field("category")
    kubernetesVersion = field("kubernetesVersion")
    lastRefreshTime = field("lastRefreshTime")
    lastTransitionTime = field("lastTransitionTime")
    description = field("description")

    @cached_property
    def insightStatus(self):  # pragma: no cover
        return InsightStatus.make_one(self.boto3_raw_data["insightStatus"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InsightSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InsightSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInsightsRequestPaginate:
    boto3_raw_data: "type_defs.ListInsightsRequestPaginateTypeDef" = dataclasses.field()

    clusterName = field("clusterName")

    @cached_property
    def filter(self):  # pragma: no cover
        return InsightsFilter.make_one(self.boto3_raw_data["filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInsightsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInsightsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInsightsRequest:
    boto3_raw_data: "type_defs.ListInsightsRequestTypeDef" = dataclasses.field()

    clusterName = field("clusterName")

    @cached_property
    def filter(self):  # pragma: no cover
        return InsightsFilter.make_one(self.boto3_raw_data["filter"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInsightsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInsightsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodegroupHealth:
    boto3_raw_data: "type_defs.NodegroupHealthTypeDef" = dataclasses.field()

    @cached_property
    def issues(self):  # pragma: no cover
        return Issue.make_many(self.boto3_raw_data["issues"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodegroupHealthTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodegroupHealthTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPodIdentityAssociationsResponse:
    boto3_raw_data: "type_defs.ListPodIdentityAssociationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def associations(self):  # pragma: no cover
        return PodIdentityAssociationSummary.make_many(
            self.boto3_raw_data["associations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPodIdentityAssociationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPodIdentityAssociationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingOutput:
    boto3_raw_data: "type_defs.LoggingOutputTypeDef" = dataclasses.field()

    @cached_property
    def clusterLogging(self):  # pragma: no cover
        return LogSetupOutput.make_many(self.boto3_raw_data["clusterLogging"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoggingOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoggingOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Logging:
    boto3_raw_data: "type_defs.LoggingTypeDef" = dataclasses.field()

    @cached_property
    def clusterLogging(self):  # pragma: no cover
        return LogSetup.make_many(self.boto3_raw_data["clusterLogging"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoggingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoggingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeRepairConfigOutput:
    boto3_raw_data: "type_defs.NodeRepairConfigOutputTypeDef" = dataclasses.field()

    enabled = field("enabled")
    maxUnhealthyNodeThresholdCount = field("maxUnhealthyNodeThresholdCount")
    maxUnhealthyNodeThresholdPercentage = field("maxUnhealthyNodeThresholdPercentage")
    maxParallelNodesRepairedCount = field("maxParallelNodesRepairedCount")
    maxParallelNodesRepairedPercentage = field("maxParallelNodesRepairedPercentage")

    @cached_property
    def nodeRepairConfigOverrides(self):  # pragma: no cover
        return NodeRepairConfigOverrides.make_many(
            self.boto3_raw_data["nodeRepairConfigOverrides"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NodeRepairConfigOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeRepairConfigOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NodeRepairConfig:
    boto3_raw_data: "type_defs.NodeRepairConfigTypeDef" = dataclasses.field()

    enabled = field("enabled")
    maxUnhealthyNodeThresholdCount = field("maxUnhealthyNodeThresholdCount")
    maxUnhealthyNodeThresholdPercentage = field("maxUnhealthyNodeThresholdPercentage")
    maxParallelNodesRepairedCount = field("maxParallelNodesRepairedCount")
    maxParallelNodesRepairedPercentage = field("maxParallelNodesRepairedPercentage")

    @cached_property
    def nodeRepairConfigOverrides(self):  # pragma: no cover
        return NodeRepairConfigOverrides.make_many(
            self.boto3_raw_data["nodeRepairConfigOverrides"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodeRepairConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NodeRepairConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoteNetworkConfigResponse:
    boto3_raw_data: "type_defs.RemoteNetworkConfigResponseTypeDef" = dataclasses.field()

    @cached_property
    def remoteNodeNetworks(self):  # pragma: no cover
        return RemoteNodeNetworkOutput.make_many(
            self.boto3_raw_data["remoteNodeNetworks"]
        )

    @cached_property
    def remotePodNetworks(self):  # pragma: no cover
        return RemotePodNetworkOutput.make_many(
            self.boto3_raw_data["remotePodNetworks"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoteNetworkConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoteNetworkConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Update:
    boto3_raw_data: "type_defs.UpdateTypeDef" = dataclasses.field()

    id = field("id")
    status = field("status")
    type = field("type")

    @cached_property
    def params(self):  # pragma: no cover
        return UpdateParam.make_many(self.boto3_raw_data["params"])

    createdAt = field("createdAt")

    @cached_property
    def errors(self):  # pragma: no cover
        return ErrorDetail.make_many(self.boto3_raw_data["errors"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpdateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateAccessPolicyResponse:
    boto3_raw_data: "type_defs.AssociateAccessPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")
    principalArn = field("principalArn")

    @cached_property
    def associatedAccessPolicy(self):  # pragma: no cover
        return AssociatedAccessPolicy.make_one(
            self.boto3_raw_data["associatedAccessPolicy"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateAccessPolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateAccessPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssociatedAccessPoliciesResponse:
    boto3_raw_data: "type_defs.ListAssociatedAccessPoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")
    principalArn = field("principalArn")

    @cached_property
    def associatedAccessPolicies(self):  # pragma: no cover
        return AssociatedAccessPolicy.make_many(
            self.boto3_raw_data["associatedAccessPolicies"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssociatedAccessPoliciesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssociatedAccessPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateAccessPolicyRequest:
    boto3_raw_data: "type_defs.AssociateAccessPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")
    principalArn = field("principalArn")
    policyArn = field("policyArn")
    accessScope = field("accessScope")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateAccessPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateAccessPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Addon:
    boto3_raw_data: "type_defs.AddonTypeDef" = dataclasses.field()

    addonName = field("addonName")
    clusterName = field("clusterName")
    status = field("status")
    addonVersion = field("addonVersion")

    @cached_property
    def health(self):  # pragma: no cover
        return AddonHealth.make_one(self.boto3_raw_data["health"])

    addonArn = field("addonArn")
    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")
    serviceAccountRoleArn = field("serviceAccountRoleArn")
    tags = field("tags")
    publisher = field("publisher")
    owner = field("owner")

    @cached_property
    def marketplaceInformation(self):  # pragma: no cover
        return MarketplaceInformation.make_one(
            self.boto3_raw_data["marketplaceInformation"]
        )

    configurationValues = field("configurationValues")
    podIdentityAssociations = field("podIdentityAssociations")

    @cached_property
    def namespaceConfig(self):  # pragma: no cover
        return AddonNamespaceConfigResponse.make_one(
            self.boto3_raw_data["namespaceConfig"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddonTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddonTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddonInfo:
    boto3_raw_data: "type_defs.AddonInfoTypeDef" = dataclasses.field()

    addonName = field("addonName")
    type = field("type")

    @cached_property
    def addonVersions(self):  # pragma: no cover
        return AddonVersionInfo.make_many(self.boto3_raw_data["addonVersions"])

    publisher = field("publisher")
    owner = field("owner")

    @cached_property
    def marketplaceInformation(self):  # pragma: no cover
        return MarketplaceInformation.make_one(
            self.boto3_raw_data["marketplaceInformation"]
        )

    defaultNamespace = field("defaultNamespace")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddonInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddonInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InsightCategorySpecificSummary:
    boto3_raw_data: "type_defs.InsightCategorySpecificSummaryTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def deprecationDetails(self):  # pragma: no cover
        return DeprecationDetail.make_many(self.boto3_raw_data["deprecationDetails"])

    @cached_property
    def addonCompatibilityDetails(self):  # pragma: no cover
        return AddonCompatibilityDetail.make_many(
            self.boto3_raw_data["addonCompatibilityDetails"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InsightCategorySpecificSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InsightCategorySpecificSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEksAnywhereSubscriptionResponse:
    boto3_raw_data: "type_defs.CreateEksAnywhereSubscriptionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def subscription(self):  # pragma: no cover
        return EksAnywhereSubscription.make_one(self.boto3_raw_data["subscription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateEksAnywhereSubscriptionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEksAnywhereSubscriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEksAnywhereSubscriptionResponse:
    boto3_raw_data: "type_defs.DeleteEksAnywhereSubscriptionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def subscription(self):  # pragma: no cover
        return EksAnywhereSubscription.make_one(self.boto3_raw_data["subscription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteEksAnywhereSubscriptionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEksAnywhereSubscriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEksAnywhereSubscriptionResponse:
    boto3_raw_data: "type_defs.DescribeEksAnywhereSubscriptionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def subscription(self):  # pragma: no cover
        return EksAnywhereSubscription.make_one(self.boto3_raw_data["subscription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEksAnywhereSubscriptionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEksAnywhereSubscriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListEksAnywhereSubscriptionsResponse:
    boto3_raw_data: "type_defs.ListEksAnywhereSubscriptionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def subscriptions(self):  # pragma: no cover
        return EksAnywhereSubscription.make_many(self.boto3_raw_data["subscriptions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListEksAnywhereSubscriptionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListEksAnywhereSubscriptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEksAnywhereSubscriptionResponse:
    boto3_raw_data: "type_defs.UpdateEksAnywhereSubscriptionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def subscription(self):  # pragma: no cover
        return EksAnywhereSubscription.make_one(self.boto3_raw_data["subscription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateEksAnywhereSubscriptionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEksAnywhereSubscriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FargateProfile:
    boto3_raw_data: "type_defs.FargateProfileTypeDef" = dataclasses.field()

    fargateProfileName = field("fargateProfileName")
    fargateProfileArn = field("fargateProfileArn")
    clusterName = field("clusterName")
    createdAt = field("createdAt")
    podExecutionRoleArn = field("podExecutionRoleArn")
    subnets = field("subnets")

    @cached_property
    def selectors(self):  # pragma: no cover
        return FargateProfileSelectorOutput.make_many(self.boto3_raw_data["selectors"])

    status = field("status")
    tags = field("tags")

    @cached_property
    def health(self):  # pragma: no cover
        return FargateProfileHealth.make_one(self.boto3_raw_data["health"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FargateProfileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FargateProfileTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFargateProfileRequest:
    boto3_raw_data: "type_defs.CreateFargateProfileRequestTypeDef" = dataclasses.field()

    fargateProfileName = field("fargateProfileName")
    clusterName = field("clusterName")
    podExecutionRoleArn = field("podExecutionRoleArn")
    subnets = field("subnets")
    selectors = field("selectors")
    clientRequestToken = field("clientRequestToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFargateProfileRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFargateProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIdentityProviderConfigResponse:
    boto3_raw_data: "type_defs.DescribeIdentityProviderConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def identityProviderConfig(self):  # pragma: no cover
        return IdentityProviderConfigResponse.make_one(
            self.boto3_raw_data["identityProviderConfig"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeIdentityProviderConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIdentityProviderConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInsightsResponse:
    boto3_raw_data: "type_defs.ListInsightsResponseTypeDef" = dataclasses.field()

    @cached_property
    def insights(self):  # pragma: no cover
        return InsightSummary.make_many(self.boto3_raw_data["insights"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInsightsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInsightsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Nodegroup:
    boto3_raw_data: "type_defs.NodegroupTypeDef" = dataclasses.field()

    nodegroupName = field("nodegroupName")
    nodegroupArn = field("nodegroupArn")
    clusterName = field("clusterName")
    version = field("version")
    releaseVersion = field("releaseVersion")
    createdAt = field("createdAt")
    modifiedAt = field("modifiedAt")
    status = field("status")
    capacityType = field("capacityType")

    @cached_property
    def scalingConfig(self):  # pragma: no cover
        return NodegroupScalingConfig.make_one(self.boto3_raw_data["scalingConfig"])

    instanceTypes = field("instanceTypes")
    subnets = field("subnets")

    @cached_property
    def remoteAccess(self):  # pragma: no cover
        return RemoteAccessConfigOutput.make_one(self.boto3_raw_data["remoteAccess"])

    amiType = field("amiType")
    nodeRole = field("nodeRole")
    labels = field("labels")

    @cached_property
    def taints(self):  # pragma: no cover
        return Taint.make_many(self.boto3_raw_data["taints"])

    @cached_property
    def resources(self):  # pragma: no cover
        return NodegroupResources.make_one(self.boto3_raw_data["resources"])

    diskSize = field("diskSize")

    @cached_property
    def health(self):  # pragma: no cover
        return NodegroupHealth.make_one(self.boto3_raw_data["health"])

    @cached_property
    def updateConfig(self):  # pragma: no cover
        return NodegroupUpdateConfig.make_one(self.boto3_raw_data["updateConfig"])

    @cached_property
    def nodeRepairConfig(self):  # pragma: no cover
        return NodeRepairConfigOutput.make_one(self.boto3_raw_data["nodeRepairConfig"])

    @cached_property
    def launchTemplate(self):  # pragma: no cover
        return LaunchTemplateSpecification.make_one(
            self.boto3_raw_data["launchTemplate"]
        )

    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NodegroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NodegroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Cluster:
    boto3_raw_data: "type_defs.ClusterTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    createdAt = field("createdAt")
    version = field("version")
    endpoint = field("endpoint")
    roleArn = field("roleArn")

    @cached_property
    def resourcesVpcConfig(self):  # pragma: no cover
        return VpcConfigResponse.make_one(self.boto3_raw_data["resourcesVpcConfig"])

    @cached_property
    def kubernetesNetworkConfig(self):  # pragma: no cover
        return KubernetesNetworkConfigResponse.make_one(
            self.boto3_raw_data["kubernetesNetworkConfig"]
        )

    @cached_property
    def logging(self):  # pragma: no cover
        return LoggingOutput.make_one(self.boto3_raw_data["logging"])

    @cached_property
    def identity(self):  # pragma: no cover
        return Identity.make_one(self.boto3_raw_data["identity"])

    status = field("status")

    @cached_property
    def certificateAuthority(self):  # pragma: no cover
        return Certificate.make_one(self.boto3_raw_data["certificateAuthority"])

    clientRequestToken = field("clientRequestToken")
    platformVersion = field("platformVersion")
    tags = field("tags")

    @cached_property
    def encryptionConfig(self):  # pragma: no cover
        return EncryptionConfigOutput.make_many(self.boto3_raw_data["encryptionConfig"])

    @cached_property
    def connectorConfig(self):  # pragma: no cover
        return ConnectorConfigResponse.make_one(self.boto3_raw_data["connectorConfig"])

    id = field("id")

    @cached_property
    def health(self):  # pragma: no cover
        return ClusterHealth.make_one(self.boto3_raw_data["health"])

    @cached_property
    def outpostConfig(self):  # pragma: no cover
        return OutpostConfigResponse.make_one(self.boto3_raw_data["outpostConfig"])

    @cached_property
    def accessConfig(self):  # pragma: no cover
        return AccessConfigResponse.make_one(self.boto3_raw_data["accessConfig"])

    @cached_property
    def upgradePolicy(self):  # pragma: no cover
        return UpgradePolicyResponse.make_one(self.boto3_raw_data["upgradePolicy"])

    @cached_property
    def zonalShiftConfig(self):  # pragma: no cover
        return ZonalShiftConfigResponse.make_one(
            self.boto3_raw_data["zonalShiftConfig"]
        )

    @cached_property
    def remoteNetworkConfig(self):  # pragma: no cover
        return RemoteNetworkConfigResponse.make_one(
            self.boto3_raw_data["remoteNetworkConfig"]
        )

    @cached_property
    def computeConfig(self):  # pragma: no cover
        return ComputeConfigResponse.make_one(self.boto3_raw_data["computeConfig"])

    @cached_property
    def storageConfig(self):  # pragma: no cover
        return StorageConfigResponse.make_one(self.boto3_raw_data["storageConfig"])

    deletionProtection = field("deletionProtection")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ClusterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ClusterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RemoteNetworkConfigRequest:
    boto3_raw_data: "type_defs.RemoteNetworkConfigRequestTypeDef" = dataclasses.field()

    remoteNodeNetworks = field("remoteNodeNetworks")
    remotePodNetworks = field("remotePodNetworks")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RemoteNetworkConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RemoteNetworkConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateEncryptionConfigResponse:
    boto3_raw_data: "type_defs.AssociateEncryptionConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def update(self):  # pragma: no cover
        return Update.make_one(self.boto3_raw_data["update"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateEncryptionConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateEncryptionConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateIdentityProviderConfigResponse:
    boto3_raw_data: "type_defs.AssociateIdentityProviderConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def update(self):  # pragma: no cover
        return Update.make_one(self.boto3_raw_data["update"])

    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateIdentityProviderConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateIdentityProviderConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeUpdateResponse:
    boto3_raw_data: "type_defs.DescribeUpdateResponseTypeDef" = dataclasses.field()

    @cached_property
    def update(self):  # pragma: no cover
        return Update.make_one(self.boto3_raw_data["update"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeUpdateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeUpdateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateIdentityProviderConfigResponse:
    boto3_raw_data: "type_defs.DisassociateIdentityProviderConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def update(self):  # pragma: no cover
        return Update.make_one(self.boto3_raw_data["update"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateIdentityProviderConfigResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateIdentityProviderConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAddonResponse:
    boto3_raw_data: "type_defs.UpdateAddonResponseTypeDef" = dataclasses.field()

    @cached_property
    def update(self):  # pragma: no cover
        return Update.make_one(self.boto3_raw_data["update"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAddonResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAddonResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateClusterConfigResponse:
    boto3_raw_data: "type_defs.UpdateClusterConfigResponseTypeDef" = dataclasses.field()

    @cached_property
    def update(self):  # pragma: no cover
        return Update.make_one(self.boto3_raw_data["update"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateClusterConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateClusterConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateClusterVersionResponse:
    boto3_raw_data: "type_defs.UpdateClusterVersionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def update(self):  # pragma: no cover
        return Update.make_one(self.boto3_raw_data["update"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateClusterVersionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateClusterVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNodegroupConfigResponse:
    boto3_raw_data: "type_defs.UpdateNodegroupConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def update(self):  # pragma: no cover
        return Update.make_one(self.boto3_raw_data["update"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateNodegroupConfigResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNodegroupConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNodegroupVersionResponse:
    boto3_raw_data: "type_defs.UpdateNodegroupVersionResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def update(self):  # pragma: no cover
        return Update.make_one(self.boto3_raw_data["update"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateNodegroupVersionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNodegroupVersionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAddonResponse:
    boto3_raw_data: "type_defs.CreateAddonResponseTypeDef" = dataclasses.field()

    @cached_property
    def addon(self):  # pragma: no cover
        return Addon.make_one(self.boto3_raw_data["addon"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAddonResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAddonResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAddonResponse:
    boto3_raw_data: "type_defs.DeleteAddonResponseTypeDef" = dataclasses.field()

    @cached_property
    def addon(self):  # pragma: no cover
        return Addon.make_one(self.boto3_raw_data["addon"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAddonResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAddonResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAddonResponse:
    boto3_raw_data: "type_defs.DescribeAddonResponseTypeDef" = dataclasses.field()

    @cached_property
    def addon(self):  # pragma: no cover
        return Addon.make_one(self.boto3_raw_data["addon"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeAddonResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAddonResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAddonVersionsResponse:
    boto3_raw_data: "type_defs.DescribeAddonVersionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def addons(self):  # pragma: no cover
        return AddonInfo.make_many(self.boto3_raw_data["addons"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAddonVersionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAddonVersionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Insight:
    boto3_raw_data: "type_defs.InsightTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    category = field("category")
    kubernetesVersion = field("kubernetesVersion")
    lastRefreshTime = field("lastRefreshTime")
    lastTransitionTime = field("lastTransitionTime")
    description = field("description")

    @cached_property
    def insightStatus(self):  # pragma: no cover
        return InsightStatus.make_one(self.boto3_raw_data["insightStatus"])

    recommendation = field("recommendation")
    additionalInfo = field("additionalInfo")

    @cached_property
    def resources(self):  # pragma: no cover
        return InsightResourceDetail.make_many(self.boto3_raw_data["resources"])

    @cached_property
    def categorySpecificSummary(self):  # pragma: no cover
        return InsightCategorySpecificSummary.make_one(
            self.boto3_raw_data["categorySpecificSummary"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InsightTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InsightTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateEncryptionConfigRequest:
    boto3_raw_data: "type_defs.AssociateEncryptionConfigRequestTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")
    encryptionConfig = field("encryptionConfig")
    clientRequestToken = field("clientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssociateEncryptionConfigRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateEncryptionConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFargateProfileResponse:
    boto3_raw_data: "type_defs.CreateFargateProfileResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def fargateProfile(self):  # pragma: no cover
        return FargateProfile.make_one(self.boto3_raw_data["fargateProfile"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFargateProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFargateProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFargateProfileResponse:
    boto3_raw_data: "type_defs.DeleteFargateProfileResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def fargateProfile(self):  # pragma: no cover
        return FargateProfile.make_one(self.boto3_raw_data["fargateProfile"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFargateProfileResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFargateProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFargateProfileResponse:
    boto3_raw_data: "type_defs.DescribeFargateProfileResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def fargateProfile(self):  # pragma: no cover
        return FargateProfile.make_one(self.boto3_raw_data["fargateProfile"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeFargateProfileResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFargateProfileResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNodegroupResponse:
    boto3_raw_data: "type_defs.CreateNodegroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def nodegroup(self):  # pragma: no cover
        return Nodegroup.make_one(self.boto3_raw_data["nodegroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateNodegroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNodegroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteNodegroupResponse:
    boto3_raw_data: "type_defs.DeleteNodegroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def nodegroup(self):  # pragma: no cover
        return Nodegroup.make_one(self.boto3_raw_data["nodegroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteNodegroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteNodegroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeNodegroupResponse:
    boto3_raw_data: "type_defs.DescribeNodegroupResponseTypeDef" = dataclasses.field()

    @cached_property
    def nodegroup(self):  # pragma: no cover
        return Nodegroup.make_one(self.boto3_raw_data["nodegroup"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeNodegroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeNodegroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateNodegroupRequest:
    boto3_raw_data: "type_defs.CreateNodegroupRequestTypeDef" = dataclasses.field()

    clusterName = field("clusterName")
    nodegroupName = field("nodegroupName")
    subnets = field("subnets")
    nodeRole = field("nodeRole")

    @cached_property
    def scalingConfig(self):  # pragma: no cover
        return NodegroupScalingConfig.make_one(self.boto3_raw_data["scalingConfig"])

    diskSize = field("diskSize")
    instanceTypes = field("instanceTypes")
    amiType = field("amiType")
    remoteAccess = field("remoteAccess")
    labels = field("labels")

    @cached_property
    def taints(self):  # pragma: no cover
        return Taint.make_many(self.boto3_raw_data["taints"])

    tags = field("tags")
    clientRequestToken = field("clientRequestToken")

    @cached_property
    def launchTemplate(self):  # pragma: no cover
        return LaunchTemplateSpecification.make_one(
            self.boto3_raw_data["launchTemplate"]
        )

    @cached_property
    def updateConfig(self):  # pragma: no cover
        return NodegroupUpdateConfig.make_one(self.boto3_raw_data["updateConfig"])

    nodeRepairConfig = field("nodeRepairConfig")
    capacityType = field("capacityType")
    version = field("version")
    releaseVersion = field("releaseVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateNodegroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateNodegroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateNodegroupConfigRequest:
    boto3_raw_data: "type_defs.UpdateNodegroupConfigRequestTypeDef" = (
        dataclasses.field()
    )

    clusterName = field("clusterName")
    nodegroupName = field("nodegroupName")

    @cached_property
    def labels(self):  # pragma: no cover
        return UpdateLabelsPayload.make_one(self.boto3_raw_data["labels"])

    @cached_property
    def taints(self):  # pragma: no cover
        return UpdateTaintsPayload.make_one(self.boto3_raw_data["taints"])

    @cached_property
    def scalingConfig(self):  # pragma: no cover
        return NodegroupScalingConfig.make_one(self.boto3_raw_data["scalingConfig"])

    @cached_property
    def updateConfig(self):  # pragma: no cover
        return NodegroupUpdateConfig.make_one(self.boto3_raw_data["updateConfig"])

    nodeRepairConfig = field("nodeRepairConfig")
    clientRequestToken = field("clientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateNodegroupConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateNodegroupConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateClusterResponse:
    boto3_raw_data: "type_defs.CreateClusterResponseTypeDef" = dataclasses.field()

    @cached_property
    def cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateClusterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteClusterResponse:
    boto3_raw_data: "type_defs.DeleteClusterResponseTypeDef" = dataclasses.field()

    @cached_property
    def cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteClusterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterClusterResponse:
    boto3_raw_data: "type_defs.DeregisterClusterResponseTypeDef" = dataclasses.field()

    @cached_property
    def cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeregisterClusterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeClusterResponse:
    boto3_raw_data: "type_defs.DescribeClusterResponseTypeDef" = dataclasses.field()

    @cached_property
    def cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeClusterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterClusterResponse:
    boto3_raw_data: "type_defs.RegisterClusterResponseTypeDef" = dataclasses.field()

    @cached_property
    def cluster(self):  # pragma: no cover
        return Cluster.make_one(self.boto3_raw_data["cluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterClusterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateClusterRequest:
    boto3_raw_data: "type_defs.CreateClusterRequestTypeDef" = dataclasses.field()

    name = field("name")
    roleArn = field("roleArn")

    @cached_property
    def resourcesVpcConfig(self):  # pragma: no cover
        return VpcConfigRequest.make_one(self.boto3_raw_data["resourcesVpcConfig"])

    version = field("version")

    @cached_property
    def kubernetesNetworkConfig(self):  # pragma: no cover
        return KubernetesNetworkConfigRequest.make_one(
            self.boto3_raw_data["kubernetesNetworkConfig"]
        )

    logging = field("logging")
    clientRequestToken = field("clientRequestToken")
    tags = field("tags")
    encryptionConfig = field("encryptionConfig")

    @cached_property
    def outpostConfig(self):  # pragma: no cover
        return OutpostConfigRequest.make_one(self.boto3_raw_data["outpostConfig"])

    @cached_property
    def accessConfig(self):  # pragma: no cover
        return CreateAccessConfigRequest.make_one(self.boto3_raw_data["accessConfig"])

    bootstrapSelfManagedAddons = field("bootstrapSelfManagedAddons")

    @cached_property
    def upgradePolicy(self):  # pragma: no cover
        return UpgradePolicyRequest.make_one(self.boto3_raw_data["upgradePolicy"])

    @cached_property
    def zonalShiftConfig(self):  # pragma: no cover
        return ZonalShiftConfigRequest.make_one(self.boto3_raw_data["zonalShiftConfig"])

    @cached_property
    def remoteNetworkConfig(self):  # pragma: no cover
        return RemoteNetworkConfigRequest.make_one(
            self.boto3_raw_data["remoteNetworkConfig"]
        )

    @cached_property
    def computeConfig(self):  # pragma: no cover
        return ComputeConfigRequest.make_one(self.boto3_raw_data["computeConfig"])

    @cached_property
    def storageConfig(self):  # pragma: no cover
        return StorageConfigRequest.make_one(self.boto3_raw_data["storageConfig"])

    deletionProtection = field("deletionProtection")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateClusterConfigRequest:
    boto3_raw_data: "type_defs.UpdateClusterConfigRequestTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def resourcesVpcConfig(self):  # pragma: no cover
        return VpcConfigRequest.make_one(self.boto3_raw_data["resourcesVpcConfig"])

    logging = field("logging")
    clientRequestToken = field("clientRequestToken")

    @cached_property
    def accessConfig(self):  # pragma: no cover
        return UpdateAccessConfigRequest.make_one(self.boto3_raw_data["accessConfig"])

    @cached_property
    def upgradePolicy(self):  # pragma: no cover
        return UpgradePolicyRequest.make_one(self.boto3_raw_data["upgradePolicy"])

    @cached_property
    def zonalShiftConfig(self):  # pragma: no cover
        return ZonalShiftConfigRequest.make_one(self.boto3_raw_data["zonalShiftConfig"])

    @cached_property
    def computeConfig(self):  # pragma: no cover
        return ComputeConfigRequest.make_one(self.boto3_raw_data["computeConfig"])

    @cached_property
    def kubernetesNetworkConfig(self):  # pragma: no cover
        return KubernetesNetworkConfigRequest.make_one(
            self.boto3_raw_data["kubernetesNetworkConfig"]
        )

    @cached_property
    def storageConfig(self):  # pragma: no cover
        return StorageConfigRequest.make_one(self.boto3_raw_data["storageConfig"])

    @cached_property
    def remoteNetworkConfig(self):  # pragma: no cover
        return RemoteNetworkConfigRequest.make_one(
            self.boto3_raw_data["remoteNetworkConfig"]
        )

    deletionProtection = field("deletionProtection")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateClusterConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateClusterConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInsightResponse:
    boto3_raw_data: "type_defs.DescribeInsightResponseTypeDef" = dataclasses.field()

    @cached_property
    def insight(self):  # pragma: no cover
        return Insight.make_one(self.boto3_raw_data["insight"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeInsightResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInsightResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
