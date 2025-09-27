# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_opensearchserverless import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccessPolicyDetail:
    boto3_raw_data: "type_defs.AccessPolicyDetailTypeDef" = dataclasses.field()

    type = field("type")
    name = field("name")
    policyVersion = field("policyVersion")
    description = field("description")
    policy = field("policy")
    createdDate = field("createdDate")
    lastModifiedDate = field("lastModifiedDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessPolicyDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessPolicyDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessPolicyStats:
    boto3_raw_data: "type_defs.AccessPolicyStatsTypeDef" = dataclasses.field()

    DataPolicyCount = field("DataPolicyCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccessPolicyStatsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessPolicyStatsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessPolicySummary:
    boto3_raw_data: "type_defs.AccessPolicySummaryTypeDef" = dataclasses.field()

    type = field("type")
    name = field("name")
    policyVersion = field("policyVersion")
    description = field("description")
    createdDate = field("createdDate")
    lastModifiedDate = field("lastModifiedDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessPolicySummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessPolicySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CapacityLimits:
    boto3_raw_data: "type_defs.CapacityLimitsTypeDef" = dataclasses.field()

    maxIndexingCapacityInOCU = field("maxIndexingCapacityInOCU")
    maxSearchCapacityInOCU = field("maxSearchCapacityInOCU")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CapacityLimitsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CapacityLimitsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetCollectionRequest:
    boto3_raw_data: "type_defs.BatchGetCollectionRequestTypeDef" = dataclasses.field()

    ids = field("ids")
    names = field("names")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetCollectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetCollectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollectionErrorDetail:
    boto3_raw_data: "type_defs.CollectionErrorDetailTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    errorMessage = field("errorMessage")
    errorCode = field("errorCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CollectionErrorDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollectionErrorDetailTypeDef"]
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
class LifecyclePolicyResourceIdentifier:
    boto3_raw_data: "type_defs.LifecyclePolicyResourceIdentifierTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    resource = field("resource")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.LifecyclePolicyResourceIdentifierTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecyclePolicyResourceIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EffectiveLifecyclePolicyDetail:
    boto3_raw_data: "type_defs.EffectiveLifecyclePolicyDetailTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    resource = field("resource")
    policyName = field("policyName")
    resourceType = field("resourceType")
    retentionPeriod = field("retentionPeriod")
    noMinRetentionPeriod = field("noMinRetentionPeriod")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EffectiveLifecyclePolicyDetailTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EffectiveLifecyclePolicyDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EffectiveLifecyclePolicyErrorDetail:
    boto3_raw_data: "type_defs.EffectiveLifecyclePolicyErrorDetailTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    resource = field("resource")
    errorMessage = field("errorMessage")
    errorCode = field("errorCode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EffectiveLifecyclePolicyErrorDetailTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EffectiveLifecyclePolicyErrorDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicyIdentifier:
    boto3_raw_data: "type_defs.LifecyclePolicyIdentifierTypeDef" = dataclasses.field()

    type = field("type")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecyclePolicyIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecyclePolicyIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicyDetail:
    boto3_raw_data: "type_defs.LifecyclePolicyDetailTypeDef" = dataclasses.field()

    type = field("type")
    name = field("name")
    policyVersion = field("policyVersion")
    description = field("description")
    policy = field("policy")
    createdDate = field("createdDate")
    lastModifiedDate = field("lastModifiedDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecyclePolicyDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecyclePolicyDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicyErrorDetail:
    boto3_raw_data: "type_defs.LifecyclePolicyErrorDetailTypeDef" = dataclasses.field()

    type = field("type")
    name = field("name")
    errorMessage = field("errorMessage")
    errorCode = field("errorCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecyclePolicyErrorDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecyclePolicyErrorDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetVpcEndpointRequest:
    boto3_raw_data: "type_defs.BatchGetVpcEndpointRequestTypeDef" = dataclasses.field()

    ids = field("ids")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetVpcEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetVpcEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcEndpointDetail:
    boto3_raw_data: "type_defs.VpcEndpointDetailTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    vpcId = field("vpcId")
    subnetIds = field("subnetIds")
    securityGroupIds = field("securityGroupIds")
    status = field("status")
    createdDate = field("createdDate")
    failureCode = field("failureCode")
    failureMessage = field("failureMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VpcEndpointDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcEndpointDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcEndpointErrorDetail:
    boto3_raw_data: "type_defs.VpcEndpointErrorDetailTypeDef" = dataclasses.field()

    id = field("id")
    errorMessage = field("errorMessage")
    errorCode = field("errorCode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcEndpointErrorDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcEndpointErrorDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FipsEndpoints:
    boto3_raw_data: "type_defs.FipsEndpointsTypeDef" = dataclasses.field()

    collectionEndpoint = field("collectionEndpoint")
    dashboardEndpoint = field("dashboardEndpoint")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FipsEndpointsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FipsEndpointsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollectionFilters:
    boto3_raw_data: "type_defs.CollectionFiltersTypeDef" = dataclasses.field()

    name = field("name")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CollectionFiltersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollectionFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollectionSummary:
    boto3_raw_data: "type_defs.CollectionSummaryTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    status = field("status")
    arn = field("arn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CollectionSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollectionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessPolicyRequest:
    boto3_raw_data: "type_defs.CreateAccessPolicyRequestTypeDef" = dataclasses.field()

    type = field("type")
    name = field("name")
    policy = field("policy")
    description = field("description")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccessPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCollectionDetail:
    boto3_raw_data: "type_defs.CreateCollectionDetailTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    status = field("status")
    type = field("type")
    description = field("description")
    arn = field("arn")
    kmsKeyArn = field("kmsKeyArn")
    standbyReplicas = field("standbyReplicas")
    createdDate = field("createdDate")
    lastModifiedDate = field("lastModifiedDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCollectionDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCollectionDetailTypeDef"]
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

    key = field("key")
    value = field("value")

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
class CreateIamIdentityCenterConfigOptions:
    boto3_raw_data: "type_defs.CreateIamIdentityCenterConfigOptionsTypeDef" = (
        dataclasses.field()
    )

    instanceArn = field("instanceArn")
    userAttribute = field("userAttribute")
    groupAttribute = field("groupAttribute")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateIamIdentityCenterConfigOptionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIamIdentityCenterConfigOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIndexRequest:
    boto3_raw_data: "type_defs.CreateIndexRequestTypeDef" = dataclasses.field()

    id = field("id")
    indexName = field("indexName")
    indexSchema = field("indexSchema")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIndexRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIndexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLifecyclePolicyRequest:
    boto3_raw_data: "type_defs.CreateLifecyclePolicyRequestTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    name = field("name")
    policy = field("policy")
    description = field("description")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLifecyclePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLifecyclePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IamFederationConfigOptions:
    boto3_raw_data: "type_defs.IamFederationConfigOptionsTypeDef" = dataclasses.field()

    groupAttribute = field("groupAttribute")
    userAttribute = field("userAttribute")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IamFederationConfigOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IamFederationConfigOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SamlConfigOptions:
    boto3_raw_data: "type_defs.SamlConfigOptionsTypeDef" = dataclasses.field()

    metadata = field("metadata")
    userAttribute = field("userAttribute")
    groupAttribute = field("groupAttribute")
    openSearchServerlessEntityId = field("openSearchServerlessEntityId")
    sessionTimeout = field("sessionTimeout")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SamlConfigOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SamlConfigOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSecurityPolicyRequest:
    boto3_raw_data: "type_defs.CreateSecurityPolicyRequestTypeDef" = dataclasses.field()

    type = field("type")
    name = field("name")
    policy = field("policy")
    description = field("description")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSecurityPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSecurityPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityPolicyDetail:
    boto3_raw_data: "type_defs.SecurityPolicyDetailTypeDef" = dataclasses.field()

    type = field("type")
    name = field("name")
    policyVersion = field("policyVersion")
    description = field("description")
    policy = field("policy")
    createdDate = field("createdDate")
    lastModifiedDate = field("lastModifiedDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SecurityPolicyDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityPolicyDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVpcEndpointDetail:
    boto3_raw_data: "type_defs.CreateVpcEndpointDetailTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVpcEndpointDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVpcEndpointDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVpcEndpointRequest:
    boto3_raw_data: "type_defs.CreateVpcEndpointRequestTypeDef" = dataclasses.field()

    name = field("name")
    vpcId = field("vpcId")
    subnetIds = field("subnetIds")
    securityGroupIds = field("securityGroupIds")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVpcEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVpcEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccessPolicyRequest:
    boto3_raw_data: "type_defs.DeleteAccessPolicyRequestTypeDef" = dataclasses.field()

    type = field("type")
    name = field("name")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAccessPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccessPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCollectionDetail:
    boto3_raw_data: "type_defs.DeleteCollectionDetailTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCollectionDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCollectionDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCollectionRequest:
    boto3_raw_data: "type_defs.DeleteCollectionRequestTypeDef" = dataclasses.field()

    id = field("id")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCollectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCollectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIndexRequest:
    boto3_raw_data: "type_defs.DeleteIndexRequestTypeDef" = dataclasses.field()

    id = field("id")
    indexName = field("indexName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIndexRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIndexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLifecyclePolicyRequest:
    boto3_raw_data: "type_defs.DeleteLifecyclePolicyRequestTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    name = field("name")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLifecyclePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLifecyclePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSecurityConfigRequest:
    boto3_raw_data: "type_defs.DeleteSecurityConfigRequestTypeDef" = dataclasses.field()

    id = field("id")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSecurityConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSecurityConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSecurityPolicyRequest:
    boto3_raw_data: "type_defs.DeleteSecurityPolicyRequestTypeDef" = dataclasses.field()

    type = field("type")
    name = field("name")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSecurityPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSecurityPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVpcEndpointDetail:
    boto3_raw_data: "type_defs.DeleteVpcEndpointDetailTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVpcEndpointDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVpcEndpointDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVpcEndpointRequest:
    boto3_raw_data: "type_defs.DeleteVpcEndpointRequestTypeDef" = dataclasses.field()

    id = field("id")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVpcEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVpcEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessPolicyRequest:
    boto3_raw_data: "type_defs.GetAccessPolicyRequestTypeDef" = dataclasses.field()

    type = field("type")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccessPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIndexRequest:
    boto3_raw_data: "type_defs.GetIndexRequestTypeDef" = dataclasses.field()

    id = field("id")
    indexName = field("indexName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetIndexRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetIndexRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicyStats:
    boto3_raw_data: "type_defs.LifecyclePolicyStatsTypeDef" = dataclasses.field()

    RetentionPolicyCount = field("RetentionPolicyCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecyclePolicyStatsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecyclePolicyStatsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityConfigStats:
    boto3_raw_data: "type_defs.SecurityConfigStatsTypeDef" = dataclasses.field()

    SamlConfigCount = field("SamlConfigCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SecurityConfigStatsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityConfigStatsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityPolicyStats:
    boto3_raw_data: "type_defs.SecurityPolicyStatsTypeDef" = dataclasses.field()

    EncryptionPolicyCount = field("EncryptionPolicyCount")
    NetworkPolicyCount = field("NetworkPolicyCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SecurityPolicyStatsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityPolicyStatsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSecurityConfigRequest:
    boto3_raw_data: "type_defs.GetSecurityConfigRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSecurityConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSecurityConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSecurityPolicyRequest:
    boto3_raw_data: "type_defs.GetSecurityPolicyRequestTypeDef" = dataclasses.field()

    type = field("type")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSecurityPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSecurityPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IamIdentityCenterConfigOptions:
    boto3_raw_data: "type_defs.IamIdentityCenterConfigOptionsTypeDef" = (
        dataclasses.field()
    )

    instanceArn = field("instanceArn")
    applicationArn = field("applicationArn")
    applicationName = field("applicationName")
    applicationDescription = field("applicationDescription")
    userAttribute = field("userAttribute")
    groupAttribute = field("groupAttribute")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IamIdentityCenterConfigOptionsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IamIdentityCenterConfigOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LifecyclePolicySummary:
    boto3_raw_data: "type_defs.LifecyclePolicySummaryTypeDef" = dataclasses.field()

    type = field("type")
    name = field("name")
    policyVersion = field("policyVersion")
    description = field("description")
    createdDate = field("createdDate")
    lastModifiedDate = field("lastModifiedDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LifecyclePolicySummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LifecyclePolicySummaryTypeDef"]
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

    type = field("type")
    resource = field("resource")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

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
class ListLifecyclePoliciesRequest:
    boto3_raw_data: "type_defs.ListLifecyclePoliciesRequestTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    resources = field("resources")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLifecyclePoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLifecyclePoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityConfigsRequest:
    boto3_raw_data: "type_defs.ListSecurityConfigsRequestTypeDef" = dataclasses.field()

    type = field("type")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSecurityConfigsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityConfigsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityConfigSummary:
    boto3_raw_data: "type_defs.SecurityConfigSummaryTypeDef" = dataclasses.field()

    id = field("id")
    type = field("type")
    configVersion = field("configVersion")
    description = field("description")
    createdDate = field("createdDate")
    lastModifiedDate = field("lastModifiedDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SecurityConfigSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityConfigSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityPoliciesRequest:
    boto3_raw_data: "type_defs.ListSecurityPoliciesRequestTypeDef" = dataclasses.field()

    type = field("type")
    resource = field("resource")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSecurityPoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityPolicySummary:
    boto3_raw_data: "type_defs.SecurityPolicySummaryTypeDef" = dataclasses.field()

    type = field("type")
    name = field("name")
    policyVersion = field("policyVersion")
    description = field("description")
    createdDate = field("createdDate")
    lastModifiedDate = field("lastModifiedDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SecurityPolicySummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityPolicySummaryTypeDef"]
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
class VpcEndpointFilters:
    boto3_raw_data: "type_defs.VpcEndpointFiltersTypeDef" = dataclasses.field()

    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcEndpointFiltersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcEndpointFiltersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VpcEndpointSummary:
    boto3_raw_data: "type_defs.VpcEndpointSummaryTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.VpcEndpointSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.VpcEndpointSummaryTypeDef"]
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
class UpdateAccessPolicyRequest:
    boto3_raw_data: "type_defs.UpdateAccessPolicyRequestTypeDef" = dataclasses.field()

    type = field("type")
    name = field("name")
    policyVersion = field("policyVersion")
    description = field("description")
    policy = field("policy")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAccessPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccessPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCollectionDetail:
    boto3_raw_data: "type_defs.UpdateCollectionDetailTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    status = field("status")
    type = field("type")
    description = field("description")
    arn = field("arn")
    createdDate = field("createdDate")
    lastModifiedDate = field("lastModifiedDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCollectionDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCollectionDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCollectionRequest:
    boto3_raw_data: "type_defs.UpdateCollectionRequestTypeDef" = dataclasses.field()

    id = field("id")
    description = field("description")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCollectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCollectionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIamIdentityCenterConfigOptions:
    boto3_raw_data: "type_defs.UpdateIamIdentityCenterConfigOptionsTypeDef" = (
        dataclasses.field()
    )

    userAttribute = field("userAttribute")
    groupAttribute = field("groupAttribute")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateIamIdentityCenterConfigOptionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIamIdentityCenterConfigOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIndexRequest:
    boto3_raw_data: "type_defs.UpdateIndexRequestTypeDef" = dataclasses.field()

    id = field("id")
    indexName = field("indexName")
    indexSchema = field("indexSchema")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateIndexRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIndexRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLifecyclePolicyRequest:
    boto3_raw_data: "type_defs.UpdateLifecyclePolicyRequestTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    name = field("name")
    policyVersion = field("policyVersion")
    description = field("description")
    policy = field("policy")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLifecyclePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLifecyclePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSecurityPolicyRequest:
    boto3_raw_data: "type_defs.UpdateSecurityPolicyRequestTypeDef" = dataclasses.field()

    type = field("type")
    name = field("name")
    policyVersion = field("policyVersion")
    description = field("description")
    policy = field("policy")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSecurityPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSecurityPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVpcEndpointDetail:
    boto3_raw_data: "type_defs.UpdateVpcEndpointDetailTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    status = field("status")
    subnetIds = field("subnetIds")
    securityGroupIds = field("securityGroupIds")
    lastModifiedDate = field("lastModifiedDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVpcEndpointDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVpcEndpointDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVpcEndpointRequest:
    boto3_raw_data: "type_defs.UpdateVpcEndpointRequestTypeDef" = dataclasses.field()

    id = field("id")
    addSubnetIds = field("addSubnetIds")
    removeSubnetIds = field("removeSubnetIds")
    addSecurityGroupIds = field("addSecurityGroupIds")
    removeSecurityGroupIds = field("removeSecurityGroupIds")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVpcEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVpcEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountSettingsDetail:
    boto3_raw_data: "type_defs.AccountSettingsDetailTypeDef" = dataclasses.field()

    @cached_property
    def capacityLimits(self):  # pragma: no cover
        return CapacityLimits.make_one(self.boto3_raw_data["capacityLimits"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccountSettingsDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountSettingsDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccountSettingsRequest:
    boto3_raw_data: "type_defs.UpdateAccountSettingsRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def capacityLimits(self):  # pragma: no cover
        return CapacityLimits.make_one(self.boto3_raw_data["capacityLimits"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAccountSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccountSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAccessPolicyResponse:
    boto3_raw_data: "type_defs.CreateAccessPolicyResponseTypeDef" = dataclasses.field()

    @cached_property
    def accessPolicyDetail(self):  # pragma: no cover
        return AccessPolicyDetail.make_one(self.boto3_raw_data["accessPolicyDetail"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAccessPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAccessPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccessPolicyResponse:
    boto3_raw_data: "type_defs.GetAccessPolicyResponseTypeDef" = dataclasses.field()

    @cached_property
    def accessPolicyDetail(self):  # pragma: no cover
        return AccessPolicyDetail.make_one(self.boto3_raw_data["accessPolicyDetail"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccessPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccessPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIndexResponse:
    boto3_raw_data: "type_defs.GetIndexResponseTypeDef" = dataclasses.field()

    indexSchema = field("indexSchema")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetIndexResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIndexResponseTypeDef"]
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
    def accessPolicySummaries(self):  # pragma: no cover
        return AccessPolicySummary.make_many(
            self.boto3_raw_data["accessPolicySummaries"]
        )

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
class UpdateAccessPolicyResponse:
    boto3_raw_data: "type_defs.UpdateAccessPolicyResponseTypeDef" = dataclasses.field()

    @cached_property
    def accessPolicyDetail(self):  # pragma: no cover
        return AccessPolicyDetail.make_one(self.boto3_raw_data["accessPolicyDetail"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAccessPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccessPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetEffectiveLifecyclePolicyRequest:
    boto3_raw_data: "type_defs.BatchGetEffectiveLifecyclePolicyRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def resourceIdentifiers(self):  # pragma: no cover
        return LifecyclePolicyResourceIdentifier.make_many(
            self.boto3_raw_data["resourceIdentifiers"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetEffectiveLifecyclePolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetEffectiveLifecyclePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetEffectiveLifecyclePolicyResponse:
    boto3_raw_data: "type_defs.BatchGetEffectiveLifecyclePolicyResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def effectiveLifecyclePolicyDetails(self):  # pragma: no cover
        return EffectiveLifecyclePolicyDetail.make_many(
            self.boto3_raw_data["effectiveLifecyclePolicyDetails"]
        )

    @cached_property
    def effectiveLifecyclePolicyErrorDetails(self):  # pragma: no cover
        return EffectiveLifecyclePolicyErrorDetail.make_many(
            self.boto3_raw_data["effectiveLifecyclePolicyErrorDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetEffectiveLifecyclePolicyResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetEffectiveLifecyclePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetLifecyclePolicyRequest:
    boto3_raw_data: "type_defs.BatchGetLifecyclePolicyRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def identifiers(self):  # pragma: no cover
        return LifecyclePolicyIdentifier.make_many(self.boto3_raw_data["identifiers"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetLifecyclePolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetLifecyclePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLifecyclePolicyResponse:
    boto3_raw_data: "type_defs.CreateLifecyclePolicyResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def lifecyclePolicyDetail(self):  # pragma: no cover
        return LifecyclePolicyDetail.make_one(
            self.boto3_raw_data["lifecyclePolicyDetail"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateLifecyclePolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLifecyclePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLifecyclePolicyResponse:
    boto3_raw_data: "type_defs.UpdateLifecyclePolicyResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def lifecyclePolicyDetail(self):  # pragma: no cover
        return LifecyclePolicyDetail.make_one(
            self.boto3_raw_data["lifecyclePolicyDetail"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateLifecyclePolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLifecyclePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetLifecyclePolicyResponse:
    boto3_raw_data: "type_defs.BatchGetLifecyclePolicyResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def lifecyclePolicyDetails(self):  # pragma: no cover
        return LifecyclePolicyDetail.make_many(
            self.boto3_raw_data["lifecyclePolicyDetails"]
        )

    @cached_property
    def lifecyclePolicyErrorDetails(self):  # pragma: no cover
        return LifecyclePolicyErrorDetail.make_many(
            self.boto3_raw_data["lifecyclePolicyErrorDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetLifecyclePolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetLifecyclePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetVpcEndpointResponse:
    boto3_raw_data: "type_defs.BatchGetVpcEndpointResponseTypeDef" = dataclasses.field()

    @cached_property
    def vpcEndpointDetails(self):  # pragma: no cover
        return VpcEndpointDetail.make_many(self.boto3_raw_data["vpcEndpointDetails"])

    @cached_property
    def vpcEndpointErrorDetails(self):  # pragma: no cover
        return VpcEndpointErrorDetail.make_many(
            self.boto3_raw_data["vpcEndpointErrorDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetVpcEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetVpcEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollectionDetail:
    boto3_raw_data: "type_defs.CollectionDetailTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    status = field("status")
    type = field("type")
    description = field("description")
    arn = field("arn")
    kmsKeyArn = field("kmsKeyArn")
    standbyReplicas = field("standbyReplicas")
    createdDate = field("createdDate")
    lastModifiedDate = field("lastModifiedDate")
    collectionEndpoint = field("collectionEndpoint")
    dashboardEndpoint = field("dashboardEndpoint")

    @cached_property
    def fipsEndpoints(self):  # pragma: no cover
        return FipsEndpoints.make_one(self.boto3_raw_data["fipsEndpoints"])

    failureCode = field("failureCode")
    failureMessage = field("failureMessage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CollectionDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollectionDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollectionsRequest:
    boto3_raw_data: "type_defs.ListCollectionsRequestTypeDef" = dataclasses.field()

    @cached_property
    def collectionFilters(self):  # pragma: no cover
        return CollectionFilters.make_one(self.boto3_raw_data["collectionFilters"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCollectionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollectionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollectionsResponse:
    boto3_raw_data: "type_defs.ListCollectionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def collectionSummaries(self):  # pragma: no cover
        return CollectionSummary.make_many(self.boto3_raw_data["collectionSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCollectionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollectionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCollectionResponse:
    boto3_raw_data: "type_defs.CreateCollectionResponseTypeDef" = dataclasses.field()

    @cached_property
    def createCollectionDetail(self):  # pragma: no cover
        return CreateCollectionDetail.make_one(
            self.boto3_raw_data["createCollectionDetail"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCollectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCollectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCollectionRequest:
    boto3_raw_data: "type_defs.CreateCollectionRequestTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")
    description = field("description")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

    standbyReplicas = field("standbyReplicas")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCollectionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCollectionRequestTypeDef"]
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

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

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
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @cached_property
    def tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["tags"])

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
class CreateSecurityConfigRequest:
    boto3_raw_data: "type_defs.CreateSecurityConfigRequestTypeDef" = dataclasses.field()

    type = field("type")
    name = field("name")
    description = field("description")

    @cached_property
    def samlOptions(self):  # pragma: no cover
        return SamlConfigOptions.make_one(self.boto3_raw_data["samlOptions"])

    @cached_property
    def iamIdentityCenterOptions(self):  # pragma: no cover
        return CreateIamIdentityCenterConfigOptions.make_one(
            self.boto3_raw_data["iamIdentityCenterOptions"]
        )

    @cached_property
    def iamFederationOptions(self):  # pragma: no cover
        return IamFederationConfigOptions.make_one(
            self.boto3_raw_data["iamFederationOptions"]
        )

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSecurityConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSecurityConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSecurityPolicyResponse:
    boto3_raw_data: "type_defs.CreateSecurityPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def securityPolicyDetail(self):  # pragma: no cover
        return SecurityPolicyDetail.make_one(
            self.boto3_raw_data["securityPolicyDetail"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSecurityPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSecurityPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSecurityPolicyResponse:
    boto3_raw_data: "type_defs.GetSecurityPolicyResponseTypeDef" = dataclasses.field()

    @cached_property
    def securityPolicyDetail(self):  # pragma: no cover
        return SecurityPolicyDetail.make_one(
            self.boto3_raw_data["securityPolicyDetail"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSecurityPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSecurityPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSecurityPolicyResponse:
    boto3_raw_data: "type_defs.UpdateSecurityPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def securityPolicyDetail(self):  # pragma: no cover
        return SecurityPolicyDetail.make_one(
            self.boto3_raw_data["securityPolicyDetail"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSecurityPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSecurityPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVpcEndpointResponse:
    boto3_raw_data: "type_defs.CreateVpcEndpointResponseTypeDef" = dataclasses.field()

    @cached_property
    def createVpcEndpointDetail(self):  # pragma: no cover
        return CreateVpcEndpointDetail.make_one(
            self.boto3_raw_data["createVpcEndpointDetail"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVpcEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVpcEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCollectionResponse:
    boto3_raw_data: "type_defs.DeleteCollectionResponseTypeDef" = dataclasses.field()

    @cached_property
    def deleteCollectionDetail(self):  # pragma: no cover
        return DeleteCollectionDetail.make_one(
            self.boto3_raw_data["deleteCollectionDetail"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCollectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCollectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVpcEndpointResponse:
    boto3_raw_data: "type_defs.DeleteVpcEndpointResponseTypeDef" = dataclasses.field()

    @cached_property
    def deleteVpcEndpointDetail(self):  # pragma: no cover
        return DeleteVpcEndpointDetail.make_one(
            self.boto3_raw_data["deleteVpcEndpointDetail"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVpcEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVpcEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPoliciesStatsResponse:
    boto3_raw_data: "type_defs.GetPoliciesStatsResponseTypeDef" = dataclasses.field()

    @cached_property
    def AccessPolicyStats(self):  # pragma: no cover
        return AccessPolicyStats.make_one(self.boto3_raw_data["AccessPolicyStats"])

    @cached_property
    def SecurityPolicyStats(self):  # pragma: no cover
        return SecurityPolicyStats.make_one(self.boto3_raw_data["SecurityPolicyStats"])

    @cached_property
    def SecurityConfigStats(self):  # pragma: no cover
        return SecurityConfigStats.make_one(self.boto3_raw_data["SecurityConfigStats"])

    @cached_property
    def LifecyclePolicyStats(self):  # pragma: no cover
        return LifecyclePolicyStats.make_one(
            self.boto3_raw_data["LifecyclePolicyStats"]
        )

    TotalPolicyCount = field("TotalPolicyCount")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetPoliciesStatsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPoliciesStatsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityConfigDetail:
    boto3_raw_data: "type_defs.SecurityConfigDetailTypeDef" = dataclasses.field()

    id = field("id")
    type = field("type")
    configVersion = field("configVersion")
    description = field("description")

    @cached_property
    def samlOptions(self):  # pragma: no cover
        return SamlConfigOptions.make_one(self.boto3_raw_data["samlOptions"])

    @cached_property
    def iamIdentityCenterOptions(self):  # pragma: no cover
        return IamIdentityCenterConfigOptions.make_one(
            self.boto3_raw_data["iamIdentityCenterOptions"]
        )

    @cached_property
    def iamFederationOptions(self):  # pragma: no cover
        return IamFederationConfigOptions.make_one(
            self.boto3_raw_data["iamFederationOptions"]
        )

    createdDate = field("createdDate")
    lastModifiedDate = field("lastModifiedDate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SecurityConfigDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityConfigDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLifecyclePoliciesResponse:
    boto3_raw_data: "type_defs.ListLifecyclePoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def lifecyclePolicySummaries(self):  # pragma: no cover
        return LifecyclePolicySummary.make_many(
            self.boto3_raw_data["lifecyclePolicySummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListLifecyclePoliciesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLifecyclePoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityConfigsResponse:
    boto3_raw_data: "type_defs.ListSecurityConfigsResponseTypeDef" = dataclasses.field()

    @cached_property
    def securityConfigSummaries(self):  # pragma: no cover
        return SecurityConfigSummary.make_many(
            self.boto3_raw_data["securityConfigSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSecurityConfigsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityConfigsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityPoliciesResponse:
    boto3_raw_data: "type_defs.ListSecurityPoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def securityPolicySummaries(self):  # pragma: no cover
        return SecurityPolicySummary.make_many(
            self.boto3_raw_data["securityPolicySummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSecurityPoliciesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVpcEndpointsRequest:
    boto3_raw_data: "type_defs.ListVpcEndpointsRequestTypeDef" = dataclasses.field()

    @cached_property
    def vpcEndpointFilters(self):  # pragma: no cover
        return VpcEndpointFilters.make_one(self.boto3_raw_data["vpcEndpointFilters"])

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVpcEndpointsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVpcEndpointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVpcEndpointsResponse:
    boto3_raw_data: "type_defs.ListVpcEndpointsResponseTypeDef" = dataclasses.field()

    @cached_property
    def vpcEndpointSummaries(self):  # pragma: no cover
        return VpcEndpointSummary.make_many(self.boto3_raw_data["vpcEndpointSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVpcEndpointsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVpcEndpointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCollectionResponse:
    boto3_raw_data: "type_defs.UpdateCollectionResponseTypeDef" = dataclasses.field()

    @cached_property
    def updateCollectionDetail(self):  # pragma: no cover
        return UpdateCollectionDetail.make_one(
            self.boto3_raw_data["updateCollectionDetail"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCollectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCollectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSecurityConfigRequest:
    boto3_raw_data: "type_defs.UpdateSecurityConfigRequestTypeDef" = dataclasses.field()

    id = field("id")
    configVersion = field("configVersion")
    description = field("description")

    @cached_property
    def samlOptions(self):  # pragma: no cover
        return SamlConfigOptions.make_one(self.boto3_raw_data["samlOptions"])

    @cached_property
    def iamIdentityCenterOptionsUpdates(self):  # pragma: no cover
        return UpdateIamIdentityCenterConfigOptions.make_one(
            self.boto3_raw_data["iamIdentityCenterOptionsUpdates"]
        )

    @cached_property
    def iamFederationOptions(self):  # pragma: no cover
        return IamFederationConfigOptions.make_one(
            self.boto3_raw_data["iamFederationOptions"]
        )

    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSecurityConfigRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSecurityConfigRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateVpcEndpointResponse:
    boto3_raw_data: "type_defs.UpdateVpcEndpointResponseTypeDef" = dataclasses.field()

    @cached_property
    def UpdateVpcEndpointDetail(self):  # pragma: no cover
        return UpdateVpcEndpointDetail.make_one(
            self.boto3_raw_data["UpdateVpcEndpointDetail"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateVpcEndpointResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateVpcEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccountSettingsResponse:
    boto3_raw_data: "type_defs.GetAccountSettingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def accountSettingsDetail(self):  # pragma: no cover
        return AccountSettingsDetail.make_one(
            self.boto3_raw_data["accountSettingsDetail"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccountSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAccountSettingsResponse:
    boto3_raw_data: "type_defs.UpdateAccountSettingsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def accountSettingsDetail(self):  # pragma: no cover
        return AccountSettingsDetail.make_one(
            self.boto3_raw_data["accountSettingsDetail"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAccountSettingsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAccountSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetCollectionResponse:
    boto3_raw_data: "type_defs.BatchGetCollectionResponseTypeDef" = dataclasses.field()

    @cached_property
    def collectionDetails(self):  # pragma: no cover
        return CollectionDetail.make_many(self.boto3_raw_data["collectionDetails"])

    @cached_property
    def collectionErrorDetails(self):  # pragma: no cover
        return CollectionErrorDetail.make_many(
            self.boto3_raw_data["collectionErrorDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetCollectionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetCollectionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSecurityConfigResponse:
    boto3_raw_data: "type_defs.CreateSecurityConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def securityConfigDetail(self):  # pragma: no cover
        return SecurityConfigDetail.make_one(
            self.boto3_raw_data["securityConfigDetail"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateSecurityConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSecurityConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSecurityConfigResponse:
    boto3_raw_data: "type_defs.GetSecurityConfigResponseTypeDef" = dataclasses.field()

    @cached_property
    def securityConfigDetail(self):  # pragma: no cover
        return SecurityConfigDetail.make_one(
            self.boto3_raw_data["securityConfigDetail"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSecurityConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSecurityConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSecurityConfigResponse:
    boto3_raw_data: "type_defs.UpdateSecurityConfigResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def securityConfigDetail(self):  # pragma: no cover
        return SecurityConfigDetail.make_one(
            self.boto3_raw_data["securityConfigDetail"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSecurityConfigResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSecurityConfigResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
