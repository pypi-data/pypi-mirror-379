# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_emr_containers import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class CancelJobRunRequest:
    boto3_raw_data: "type_defs.CancelJobRunRequestTypeDef" = dataclasses.field()

    id = field("id")
    virtualClusterId = field("virtualClusterId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelJobRunRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelJobRunRequestTypeDef"]
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
class Certificate:
    boto3_raw_data: "type_defs.CertificateTypeDef" = dataclasses.field()

    certificateArn = field("certificateArn")
    certificateData = field("certificateData")

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
class CloudWatchMonitoringConfiguration:
    boto3_raw_data: "type_defs.CloudWatchMonitoringConfigurationTypeDef" = (
        dataclasses.field()
    )

    logGroupName = field("logGroupName")
    logStreamNamePrefix = field("logStreamNamePrefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CloudWatchMonitoringConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudWatchMonitoringConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationOutput:
    boto3_raw_data: "type_defs.ConfigurationOutputTypeDef" = dataclasses.field()

    classification = field("classification")
    properties = field("properties")
    configurations = field("configurations")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationPaginator:
    boto3_raw_data: "type_defs.ConfigurationPaginatorTypeDef" = dataclasses.field()

    classification = field("classification")
    properties = field("properties")
    configurations = field("configurations")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Configuration:
    boto3_raw_data: "type_defs.ConfigurationTypeDef" = dataclasses.field()

    classification = field("classification")
    properties = field("properties")
    configurations = field("configurations")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConfigurationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EksInfo:
    boto3_raw_data: "type_defs.EksInfoTypeDef" = dataclasses.field()

    namespace = field("namespace")
    nodeLabel = field("nodeLabel")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EksInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EksInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerLogRotationConfiguration:
    boto3_raw_data: "type_defs.ContainerLogRotationConfigurationTypeDef" = (
        dataclasses.field()
    )

    rotationSize = field("rotationSize")
    maxFilesToKeep = field("maxFilesToKeep")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ContainerLogRotationConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerLogRotationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Credentials:
    boto3_raw_data: "type_defs.CredentialsTypeDef" = dataclasses.field()

    token = field("token")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CredentialsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CredentialsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteJobTemplateRequest:
    boto3_raw_data: "type_defs.DeleteJobTemplateRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteJobTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteJobTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteManagedEndpointRequest:
    boto3_raw_data: "type_defs.DeleteManagedEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    virtualClusterId = field("virtualClusterId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteManagedEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteManagedEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVirtualClusterRequest:
    boto3_raw_data: "type_defs.DeleteVirtualClusterRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVirtualClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVirtualClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobRunRequest:
    boto3_raw_data: "type_defs.DescribeJobRunRequestTypeDef" = dataclasses.field()

    id = field("id")
    virtualClusterId = field("virtualClusterId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobRunRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobRunRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobTemplateRequest:
    boto3_raw_data: "type_defs.DescribeJobTemplateRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeManagedEndpointRequest:
    boto3_raw_data: "type_defs.DescribeManagedEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    virtualClusterId = field("virtualClusterId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeManagedEndpointRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeManagedEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSecurityConfigurationRequest:
    boto3_raw_data: "type_defs.DescribeSecurityConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSecurityConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSecurityConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVirtualClusterRequest:
    boto3_raw_data: "type_defs.DescribeVirtualClusterRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeVirtualClusterRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVirtualClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetManagedEndpointSessionCredentialsRequest:
    boto3_raw_data: "type_defs.GetManagedEndpointSessionCredentialsRequestTypeDef" = (
        dataclasses.field()
    )

    endpointIdentifier = field("endpointIdentifier")
    virtualClusterIdentifier = field("virtualClusterIdentifier")
    executionRoleArn = field("executionRoleArn")
    credentialType = field("credentialType")
    durationInSeconds = field("durationInSeconds")
    logContext = field("logContext")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetManagedEndpointSessionCredentialsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetManagedEndpointSessionCredentialsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TLSCertificateConfiguration:
    boto3_raw_data: "type_defs.TLSCertificateConfigurationTypeDef" = dataclasses.field()

    certificateProviderType = field("certificateProviderType")
    publicCertificateSecretArn = field("publicCertificateSecretArn")
    privateCertificateSecretArn = field("privateCertificateSecretArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TLSCertificateConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TLSCertificateConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SparkSqlJobDriver:
    boto3_raw_data: "type_defs.SparkSqlJobDriverTypeDef" = dataclasses.field()

    entryPoint = field("entryPoint")
    sparkSqlParameters = field("sparkSqlParameters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SparkSqlJobDriverTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SparkSqlJobDriverTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SparkSubmitJobDriverOutput:
    boto3_raw_data: "type_defs.SparkSubmitJobDriverOutputTypeDef" = dataclasses.field()

    entryPoint = field("entryPoint")
    entryPointArguments = field("entryPointArguments")
    sparkSubmitParameters = field("sparkSubmitParameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SparkSubmitJobDriverOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SparkSubmitJobDriverOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SparkSubmitJobDriver:
    boto3_raw_data: "type_defs.SparkSubmitJobDriverTypeDef" = dataclasses.field()

    entryPoint = field("entryPoint")
    entryPointArguments = field("entryPointArguments")
    sparkSubmitParameters = field("sparkSubmitParameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SparkSubmitJobDriverTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SparkSubmitJobDriverTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetryPolicyConfiguration:
    boto3_raw_data: "type_defs.RetryPolicyConfigurationTypeDef" = dataclasses.field()

    maxAttempts = field("maxAttempts")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetryPolicyConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetryPolicyConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetryPolicyExecution:
    boto3_raw_data: "type_defs.RetryPolicyExecutionTypeDef" = dataclasses.field()

    currentAttemptCount = field("currentAttemptCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RetryPolicyExecutionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetryPolicyExecutionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateParameterConfiguration:
    boto3_raw_data: "type_defs.TemplateParameterConfigurationTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    defaultValue = field("defaultValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TemplateParameterConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateParameterConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecureNamespaceInfo:
    boto3_raw_data: "type_defs.SecureNamespaceInfoTypeDef" = dataclasses.field()

    clusterId = field("clusterId")
    namespace = field("namespace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SecureNamespaceInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecureNamespaceInfoTypeDef"]
        ],
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
class ManagedLogs:
    boto3_raw_data: "type_defs.ManagedLogsTypeDef" = dataclasses.field()

    allowAWSToRetainLogs = field("allowAWSToRetainLogs")
    encryptionKeyArn = field("encryptionKeyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ManagedLogsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ManagedLogsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3MonitoringConfiguration:
    boto3_raw_data: "type_defs.S3MonitoringConfigurationTypeDef" = dataclasses.field()

    logUri = field("logUri")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3MonitoringConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3MonitoringConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParametricCloudWatchMonitoringConfiguration:
    boto3_raw_data: "type_defs.ParametricCloudWatchMonitoringConfigurationTypeDef" = (
        dataclasses.field()
    )

    logGroupName = field("logGroupName")
    logStreamNamePrefix = field("logStreamNamePrefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ParametricCloudWatchMonitoringConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParametricCloudWatchMonitoringConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParametricS3MonitoringConfiguration:
    boto3_raw_data: "type_defs.ParametricS3MonitoringConfigurationTypeDef" = (
        dataclasses.field()
    )

    logUri = field("logUri")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ParametricS3MonitoringConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParametricS3MonitoringConfigurationTypeDef"]
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
class CancelJobRunResponse:
    boto3_raw_data: "type_defs.CancelJobRunResponseTypeDef" = dataclasses.field()

    id = field("id")
    virtualClusterId = field("virtualClusterId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelJobRunResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelJobRunResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobTemplateResponse:
    boto3_raw_data: "type_defs.CreateJobTemplateResponseTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    createdAt = field("createdAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateJobTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateJobTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateManagedEndpointResponse:
    boto3_raw_data: "type_defs.CreateManagedEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    name = field("name")
    arn = field("arn")
    virtualClusterId = field("virtualClusterId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateManagedEndpointResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateManagedEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSecurityConfigurationResponse:
    boto3_raw_data: "type_defs.CreateSecurityConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    name = field("name")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSecurityConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSecurityConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVirtualClusterResponse:
    boto3_raw_data: "type_defs.CreateVirtualClusterResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    name = field("name")
    arn = field("arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVirtualClusterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVirtualClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteJobTemplateResponse:
    boto3_raw_data: "type_defs.DeleteJobTemplateResponseTypeDef" = dataclasses.field()

    id = field("id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteJobTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteJobTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteManagedEndpointResponse:
    boto3_raw_data: "type_defs.DeleteManagedEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    virtualClusterId = field("virtualClusterId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteManagedEndpointResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteManagedEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteVirtualClusterResponse:
    boto3_raw_data: "type_defs.DeleteVirtualClusterResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteVirtualClusterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteVirtualClusterResponseTypeDef"]
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
class StartJobRunResponse:
    boto3_raw_data: "type_defs.StartJobRunResponseTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    virtualClusterId = field("virtualClusterId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartJobRunResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartJobRunResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerInfo:
    boto3_raw_data: "type_defs.ContainerInfoTypeDef" = dataclasses.field()

    @cached_property
    def eksInfo(self):  # pragma: no cover
        return EksInfo.make_one(self.boto3_raw_data["eksInfo"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContainerInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContainerInfoTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetManagedEndpointSessionCredentialsResponse:
    boto3_raw_data: "type_defs.GetManagedEndpointSessionCredentialsResponseTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @cached_property
    def credentials(self):  # pragma: no cover
        return Credentials.make_one(self.boto3_raw_data["credentials"])

    expiresAt = field("expiresAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetManagedEndpointSessionCredentialsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetManagedEndpointSessionCredentialsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InTransitEncryptionConfiguration:
    boto3_raw_data: "type_defs.InTransitEncryptionConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def tlsCertificateConfiguration(self):  # pragma: no cover
        return TLSCertificateConfiguration.make_one(
            self.boto3_raw_data["tlsCertificateConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.InTransitEncryptionConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InTransitEncryptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobDriverOutput:
    boto3_raw_data: "type_defs.JobDriverOutputTypeDef" = dataclasses.field()

    @cached_property
    def sparkSubmitJobDriver(self):  # pragma: no cover
        return SparkSubmitJobDriverOutput.make_one(
            self.boto3_raw_data["sparkSubmitJobDriver"]
        )

    @cached_property
    def sparkSqlJobDriver(self):  # pragma: no cover
        return SparkSqlJobDriver.make_one(self.boto3_raw_data["sparkSqlJobDriver"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobDriverOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobDriverOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobDriver:
    boto3_raw_data: "type_defs.JobDriverTypeDef" = dataclasses.field()

    @cached_property
    def sparkSubmitJobDriver(self):  # pragma: no cover
        return SparkSubmitJobDriver.make_one(
            self.boto3_raw_data["sparkSubmitJobDriver"]
        )

    @cached_property
    def sparkSqlJobDriver(self):  # pragma: no cover
        return SparkSqlJobDriver.make_one(self.boto3_raw_data["sparkSqlJobDriver"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobDriverTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobDriverTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LakeFormationConfiguration:
    boto3_raw_data: "type_defs.LakeFormationConfigurationTypeDef" = dataclasses.field()

    authorizedSessionTagValue = field("authorizedSessionTagValue")

    @cached_property
    def secureNamespaceInfo(self):  # pragma: no cover
        return SecureNamespaceInfo.make_one(self.boto3_raw_data["secureNamespaceInfo"])

    queryEngineRoleArn = field("queryEngineRoleArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LakeFormationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LakeFormationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobRunsRequestPaginate:
    boto3_raw_data: "type_defs.ListJobRunsRequestPaginateTypeDef" = dataclasses.field()

    virtualClusterId = field("virtualClusterId")
    createdBefore = field("createdBefore")
    createdAfter = field("createdAfter")
    name = field("name")
    states = field("states")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobRunsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobRunsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobRunsRequest:
    boto3_raw_data: "type_defs.ListJobRunsRequestTypeDef" = dataclasses.field()

    virtualClusterId = field("virtualClusterId")
    createdBefore = field("createdBefore")
    createdAfter = field("createdAfter")
    name = field("name")
    states = field("states")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobRunsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobRunsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobTemplatesRequestPaginate:
    boto3_raw_data: "type_defs.ListJobTemplatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    createdAfter = field("createdAfter")
    createdBefore = field("createdBefore")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListJobTemplatesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobTemplatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobTemplatesRequest:
    boto3_raw_data: "type_defs.ListJobTemplatesRequestTypeDef" = dataclasses.field()

    createdAfter = field("createdAfter")
    createdBefore = field("createdBefore")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobTemplatesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedEndpointsRequestPaginate:
    boto3_raw_data: "type_defs.ListManagedEndpointsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    virtualClusterId = field("virtualClusterId")
    createdBefore = field("createdBefore")
    createdAfter = field("createdAfter")
    types = field("types")
    states = field("states")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListManagedEndpointsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedEndpointsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedEndpointsRequest:
    boto3_raw_data: "type_defs.ListManagedEndpointsRequestTypeDef" = dataclasses.field()

    virtualClusterId = field("virtualClusterId")
    createdBefore = field("createdBefore")
    createdAfter = field("createdAfter")
    types = field("types")
    states = field("states")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListManagedEndpointsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedEndpointsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityConfigurationsRequestPaginate:
    boto3_raw_data: "type_defs.ListSecurityConfigurationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    createdAfter = field("createdAfter")
    createdBefore = field("createdBefore")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSecurityConfigurationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityConfigurationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityConfigurationsRequest:
    boto3_raw_data: "type_defs.ListSecurityConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    createdAfter = field("createdAfter")
    createdBefore = field("createdBefore")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSecurityConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVirtualClustersRequestPaginate:
    boto3_raw_data: "type_defs.ListVirtualClustersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    containerProviderId = field("containerProviderId")
    containerProviderType = field("containerProviderType")
    createdAfter = field("createdAfter")
    createdBefore = field("createdBefore")
    states = field("states")
    eksAccessEntryIntegrated = field("eksAccessEntryIntegrated")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListVirtualClustersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVirtualClustersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVirtualClustersRequest:
    boto3_raw_data: "type_defs.ListVirtualClustersRequestTypeDef" = dataclasses.field()

    containerProviderId = field("containerProviderId")
    containerProviderType = field("containerProviderType")
    createdAfter = field("createdAfter")
    createdBefore = field("createdBefore")
    states = field("states")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    eksAccessEntryIntegrated = field("eksAccessEntryIntegrated")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVirtualClustersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVirtualClustersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MonitoringConfiguration:
    boto3_raw_data: "type_defs.MonitoringConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def managedLogs(self):  # pragma: no cover
        return ManagedLogs.make_one(self.boto3_raw_data["managedLogs"])

    persistentAppUI = field("persistentAppUI")

    @cached_property
    def cloudWatchMonitoringConfiguration(self):  # pragma: no cover
        return CloudWatchMonitoringConfiguration.make_one(
            self.boto3_raw_data["cloudWatchMonitoringConfiguration"]
        )

    @cached_property
    def s3MonitoringConfiguration(self):  # pragma: no cover
        return S3MonitoringConfiguration.make_one(
            self.boto3_raw_data["s3MonitoringConfiguration"]
        )

    @cached_property
    def containerLogRotationConfiguration(self):  # pragma: no cover
        return ContainerLogRotationConfiguration.make_one(
            self.boto3_raw_data["containerLogRotationConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MonitoringConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MonitoringConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParametricMonitoringConfiguration:
    boto3_raw_data: "type_defs.ParametricMonitoringConfigurationTypeDef" = (
        dataclasses.field()
    )

    persistentAppUI = field("persistentAppUI")

    @cached_property
    def cloudWatchMonitoringConfiguration(self):  # pragma: no cover
        return ParametricCloudWatchMonitoringConfiguration.make_one(
            self.boto3_raw_data["cloudWatchMonitoringConfiguration"]
        )

    @cached_property
    def s3MonitoringConfiguration(self):  # pragma: no cover
        return ParametricS3MonitoringConfiguration.make_one(
            self.boto3_raw_data["s3MonitoringConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ParametricMonitoringConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParametricMonitoringConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContainerProvider:
    boto3_raw_data: "type_defs.ContainerProviderTypeDef" = dataclasses.field()

    type = field("type")
    id = field("id")

    @cached_property
    def info(self):  # pragma: no cover
        return ContainerInfo.make_one(self.boto3_raw_data["info"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContainerProviderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContainerProviderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EncryptionConfiguration:
    boto3_raw_data: "type_defs.EncryptionConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def inTransitEncryptionConfiguration(self):  # pragma: no cover
        return InTransitEncryptionConfiguration.make_one(
            self.boto3_raw_data["inTransitEncryptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EncryptionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EncryptionConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationOverridesOutput:
    boto3_raw_data: "type_defs.ConfigurationOverridesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def applicationConfiguration(self):  # pragma: no cover
        return ConfigurationOutput.make_many(
            self.boto3_raw_data["applicationConfiguration"]
        )

    @cached_property
    def monitoringConfiguration(self):  # pragma: no cover
        return MonitoringConfiguration.make_one(
            self.boto3_raw_data["monitoringConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationOverridesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationOverridesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationOverridesPaginator:
    boto3_raw_data: "type_defs.ConfigurationOverridesPaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def applicationConfiguration(self):  # pragma: no cover
        return ConfigurationPaginator.make_many(
            self.boto3_raw_data["applicationConfiguration"]
        )

    @cached_property
    def monitoringConfiguration(self):  # pragma: no cover
        return MonitoringConfiguration.make_one(
            self.boto3_raw_data["monitoringConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConfigurationOverridesPaginatorTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationOverridesPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationOverrides:
    boto3_raw_data: "type_defs.ConfigurationOverridesTypeDef" = dataclasses.field()

    @cached_property
    def applicationConfiguration(self):  # pragma: no cover
        return Configuration.make_many(self.boto3_raw_data["applicationConfiguration"])

    @cached_property
    def monitoringConfiguration(self):  # pragma: no cover
        return MonitoringConfiguration.make_one(
            self.boto3_raw_data["monitoringConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationOverridesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationOverridesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParametricConfigurationOverridesOutput:
    boto3_raw_data: "type_defs.ParametricConfigurationOverridesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def applicationConfiguration(self):  # pragma: no cover
        return ConfigurationOutput.make_many(
            self.boto3_raw_data["applicationConfiguration"]
        )

    @cached_property
    def monitoringConfiguration(self):  # pragma: no cover
        return ParametricMonitoringConfiguration.make_one(
            self.boto3_raw_data["monitoringConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ParametricConfigurationOverridesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParametricConfigurationOverridesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParametricConfigurationOverridesPaginator:
    boto3_raw_data: "type_defs.ParametricConfigurationOverridesPaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def applicationConfiguration(self):  # pragma: no cover
        return ConfigurationPaginator.make_many(
            self.boto3_raw_data["applicationConfiguration"]
        )

    @cached_property
    def monitoringConfiguration(self):  # pragma: no cover
        return ParametricMonitoringConfiguration.make_one(
            self.boto3_raw_data["monitoringConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ParametricConfigurationOverridesPaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParametricConfigurationOverridesPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParametricConfigurationOverrides:
    boto3_raw_data: "type_defs.ParametricConfigurationOverridesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def applicationConfiguration(self):  # pragma: no cover
        return Configuration.make_many(self.boto3_raw_data["applicationConfiguration"])

    @cached_property
    def monitoringConfiguration(self):  # pragma: no cover
        return ParametricMonitoringConfiguration.make_one(
            self.boto3_raw_data["monitoringConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ParametricConfigurationOverridesTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParametricConfigurationOverridesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateVirtualClusterRequest:
    boto3_raw_data: "type_defs.CreateVirtualClusterRequestTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def containerProvider(self):  # pragma: no cover
        return ContainerProvider.make_one(self.boto3_raw_data["containerProvider"])

    clientToken = field("clientToken")
    tags = field("tags")
    securityConfigurationId = field("securityConfigurationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateVirtualClusterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateVirtualClusterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class VirtualCluster:
    boto3_raw_data: "type_defs.VirtualClusterTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    state = field("state")

    @cached_property
    def containerProvider(self):  # pragma: no cover
        return ContainerProvider.make_one(self.boto3_raw_data["containerProvider"])

    createdAt = field("createdAt")
    tags = field("tags")
    securityConfigurationId = field("securityConfigurationId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.VirtualClusterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.VirtualClusterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuthorizationConfiguration:
    boto3_raw_data: "type_defs.AuthorizationConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def lakeFormationConfiguration(self):  # pragma: no cover
        return LakeFormationConfiguration.make_one(
            self.boto3_raw_data["lakeFormationConfiguration"]
        )

    @cached_property
    def encryptionConfiguration(self):  # pragma: no cover
        return EncryptionConfiguration.make_one(
            self.boto3_raw_data["encryptionConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuthorizationConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuthorizationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Endpoint:
    boto3_raw_data: "type_defs.EndpointTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    virtualClusterId = field("virtualClusterId")
    type = field("type")
    state = field("state")
    releaseLabel = field("releaseLabel")
    executionRoleArn = field("executionRoleArn")
    certificateArn = field("certificateArn")

    @cached_property
    def certificateAuthority(self):  # pragma: no cover
        return Certificate.make_one(self.boto3_raw_data["certificateAuthority"])

    @cached_property
    def configurationOverrides(self):  # pragma: no cover
        return ConfigurationOverridesOutput.make_one(
            self.boto3_raw_data["configurationOverrides"]
        )

    serverUrl = field("serverUrl")
    createdAt = field("createdAt")
    securityGroup = field("securityGroup")
    subnetIds = field("subnetIds")
    stateDetails = field("stateDetails")
    failureReason = field("failureReason")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EndpointTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobRun:
    boto3_raw_data: "type_defs.JobRunTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    virtualClusterId = field("virtualClusterId")
    arn = field("arn")
    state = field("state")
    clientToken = field("clientToken")
    executionRoleArn = field("executionRoleArn")
    releaseLabel = field("releaseLabel")

    @cached_property
    def configurationOverrides(self):  # pragma: no cover
        return ConfigurationOverridesOutput.make_one(
            self.boto3_raw_data["configurationOverrides"]
        )

    @cached_property
    def jobDriver(self):  # pragma: no cover
        return JobDriverOutput.make_one(self.boto3_raw_data["jobDriver"])

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    finishedAt = field("finishedAt")
    stateDetails = field("stateDetails")
    failureReason = field("failureReason")
    tags = field("tags")

    @cached_property
    def retryPolicyConfiguration(self):  # pragma: no cover
        return RetryPolicyConfiguration.make_one(
            self.boto3_raw_data["retryPolicyConfiguration"]
        )

    @cached_property
    def retryPolicyExecution(self):  # pragma: no cover
        return RetryPolicyExecution.make_one(
            self.boto3_raw_data["retryPolicyExecution"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobRunTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobRunTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EndpointPaginator:
    boto3_raw_data: "type_defs.EndpointPaginatorTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    virtualClusterId = field("virtualClusterId")
    type = field("type")
    state = field("state")
    releaseLabel = field("releaseLabel")
    executionRoleArn = field("executionRoleArn")
    certificateArn = field("certificateArn")

    @cached_property
    def certificateAuthority(self):  # pragma: no cover
        return Certificate.make_one(self.boto3_raw_data["certificateAuthority"])

    @cached_property
    def configurationOverrides(self):  # pragma: no cover
        return ConfigurationOverridesPaginator.make_one(
            self.boto3_raw_data["configurationOverrides"]
        )

    serverUrl = field("serverUrl")
    createdAt = field("createdAt")
    securityGroup = field("securityGroup")
    subnetIds = field("subnetIds")
    stateDetails = field("stateDetails")
    failureReason = field("failureReason")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EndpointPaginatorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EndpointPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobRunPaginator:
    boto3_raw_data: "type_defs.JobRunPaginatorTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    virtualClusterId = field("virtualClusterId")
    arn = field("arn")
    state = field("state")
    clientToken = field("clientToken")
    executionRoleArn = field("executionRoleArn")
    releaseLabel = field("releaseLabel")

    @cached_property
    def configurationOverrides(self):  # pragma: no cover
        return ConfigurationOverridesPaginator.make_one(
            self.boto3_raw_data["configurationOverrides"]
        )

    @cached_property
    def jobDriver(self):  # pragma: no cover
        return JobDriverOutput.make_one(self.boto3_raw_data["jobDriver"])

    createdAt = field("createdAt")
    createdBy = field("createdBy")
    finishedAt = field("finishedAt")
    stateDetails = field("stateDetails")
    failureReason = field("failureReason")
    tags = field("tags")

    @cached_property
    def retryPolicyConfiguration(self):  # pragma: no cover
        return RetryPolicyConfiguration.make_one(
            self.boto3_raw_data["retryPolicyConfiguration"]
        )

    @cached_property
    def retryPolicyExecution(self):  # pragma: no cover
        return RetryPolicyExecution.make_one(
            self.boto3_raw_data["retryPolicyExecution"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobRunPaginatorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobRunPaginatorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobTemplateDataOutput:
    boto3_raw_data: "type_defs.JobTemplateDataOutputTypeDef" = dataclasses.field()

    executionRoleArn = field("executionRoleArn")
    releaseLabel = field("releaseLabel")

    @cached_property
    def jobDriver(self):  # pragma: no cover
        return JobDriverOutput.make_one(self.boto3_raw_data["jobDriver"])

    @cached_property
    def configurationOverrides(self):  # pragma: no cover
        return ParametricConfigurationOverridesOutput.make_one(
            self.boto3_raw_data["configurationOverrides"]
        )

    parameterConfiguration = field("parameterConfiguration")
    jobTags = field("jobTags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobTemplateDataOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobTemplateDataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobTemplateDataPaginator:
    boto3_raw_data: "type_defs.JobTemplateDataPaginatorTypeDef" = dataclasses.field()

    executionRoleArn = field("executionRoleArn")
    releaseLabel = field("releaseLabel")

    @cached_property
    def jobDriver(self):  # pragma: no cover
        return JobDriverOutput.make_one(self.boto3_raw_data["jobDriver"])

    @cached_property
    def configurationOverrides(self):  # pragma: no cover
        return ParametricConfigurationOverridesPaginator.make_one(
            self.boto3_raw_data["configurationOverrides"]
        )

    parameterConfiguration = field("parameterConfiguration")
    jobTags = field("jobTags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobTemplateDataPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobTemplateDataPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobTemplateData:
    boto3_raw_data: "type_defs.JobTemplateDataTypeDef" = dataclasses.field()

    executionRoleArn = field("executionRoleArn")
    releaseLabel = field("releaseLabel")

    @cached_property
    def jobDriver(self):  # pragma: no cover
        return JobDriver.make_one(self.boto3_raw_data["jobDriver"])

    @cached_property
    def configurationOverrides(self):  # pragma: no cover
        return ParametricConfigurationOverrides.make_one(
            self.boto3_raw_data["configurationOverrides"]
        )

    parameterConfiguration = field("parameterConfiguration")
    jobTags = field("jobTags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobTemplateDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobTemplateDataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeVirtualClusterResponse:
    boto3_raw_data: "type_defs.DescribeVirtualClusterResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def virtualCluster(self):  # pragma: no cover
        return VirtualCluster.make_one(self.boto3_raw_data["virtualCluster"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeVirtualClusterResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeVirtualClusterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListVirtualClustersResponse:
    boto3_raw_data: "type_defs.ListVirtualClustersResponseTypeDef" = dataclasses.field()

    @cached_property
    def virtualClusters(self):  # pragma: no cover
        return VirtualCluster.make_many(self.boto3_raw_data["virtualClusters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListVirtualClustersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListVirtualClustersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityConfigurationData:
    boto3_raw_data: "type_defs.SecurityConfigurationDataTypeDef" = dataclasses.field()

    @cached_property
    def authorizationConfiguration(self):  # pragma: no cover
        return AuthorizationConfiguration.make_one(
            self.boto3_raw_data["authorizationConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SecurityConfigurationDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityConfigurationDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeManagedEndpointResponse:
    boto3_raw_data: "type_defs.DescribeManagedEndpointResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def endpoint(self):  # pragma: no cover
        return Endpoint.make_one(self.boto3_raw_data["endpoint"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeManagedEndpointResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeManagedEndpointResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedEndpointsResponse:
    boto3_raw_data: "type_defs.ListManagedEndpointsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def endpoints(self):  # pragma: no cover
        return Endpoint.make_many(self.boto3_raw_data["endpoints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListManagedEndpointsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedEndpointsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobRunResponse:
    boto3_raw_data: "type_defs.DescribeJobRunResponseTypeDef" = dataclasses.field()

    @cached_property
    def jobRun(self):  # pragma: no cover
        return JobRun.make_one(self.boto3_raw_data["jobRun"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobRunResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobRunResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobRunsResponse:
    boto3_raw_data: "type_defs.ListJobRunsResponseTypeDef" = dataclasses.field()

    @cached_property
    def jobRuns(self):  # pragma: no cover
        return JobRun.make_many(self.boto3_raw_data["jobRuns"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobRunsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobRunsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListManagedEndpointsResponsePaginator:
    boto3_raw_data: "type_defs.ListManagedEndpointsResponsePaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def endpoints(self):  # pragma: no cover
        return EndpointPaginator.make_many(self.boto3_raw_data["endpoints"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListManagedEndpointsResponsePaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListManagedEndpointsResponsePaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobRunsResponsePaginator:
    boto3_raw_data: "type_defs.ListJobRunsResponsePaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def jobRuns(self):  # pragma: no cover
        return JobRunPaginator.make_many(self.boto3_raw_data["jobRuns"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobRunsResponsePaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobRunsResponsePaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateManagedEndpointRequest:
    boto3_raw_data: "type_defs.CreateManagedEndpointRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    virtualClusterId = field("virtualClusterId")
    type = field("type")
    releaseLabel = field("releaseLabel")
    executionRoleArn = field("executionRoleArn")
    clientToken = field("clientToken")
    certificateArn = field("certificateArn")
    configurationOverrides = field("configurationOverrides")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateManagedEndpointRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateManagedEndpointRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartJobRunRequest:
    boto3_raw_data: "type_defs.StartJobRunRequestTypeDef" = dataclasses.field()

    virtualClusterId = field("virtualClusterId")
    clientToken = field("clientToken")
    name = field("name")
    executionRoleArn = field("executionRoleArn")
    releaseLabel = field("releaseLabel")
    jobDriver = field("jobDriver")
    configurationOverrides = field("configurationOverrides")
    tags = field("tags")
    jobTemplateId = field("jobTemplateId")
    jobTemplateParameters = field("jobTemplateParameters")

    @cached_property
    def retryPolicyConfiguration(self):  # pragma: no cover
        return RetryPolicyConfiguration.make_one(
            self.boto3_raw_data["retryPolicyConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartJobRunRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartJobRunRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobTemplate:
    boto3_raw_data: "type_defs.JobTemplateTypeDef" = dataclasses.field()

    @cached_property
    def jobTemplateData(self):  # pragma: no cover
        return JobTemplateDataOutput.make_one(self.boto3_raw_data["jobTemplateData"])

    name = field("name")
    id = field("id")
    arn = field("arn")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    tags = field("tags")
    kmsKeyArn = field("kmsKeyArn")
    decryptionError = field("decryptionError")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.JobTemplateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.JobTemplateTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobTemplatePaginator:
    boto3_raw_data: "type_defs.JobTemplatePaginatorTypeDef" = dataclasses.field()

    @cached_property
    def jobTemplateData(self):  # pragma: no cover
        return JobTemplateDataPaginator.make_one(self.boto3_raw_data["jobTemplateData"])

    name = field("name")
    id = field("id")
    arn = field("arn")
    createdAt = field("createdAt")
    createdBy = field("createdBy")
    tags = field("tags")
    kmsKeyArn = field("kmsKeyArn")
    decryptionError = field("decryptionError")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobTemplatePaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobTemplatePaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateSecurityConfigurationRequest:
    boto3_raw_data: "type_defs.CreateSecurityConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    clientToken = field("clientToken")
    name = field("name")

    @cached_property
    def securityConfigurationData(self):  # pragma: no cover
        return SecurityConfigurationData.make_one(
            self.boto3_raw_data["securityConfigurationData"]
        )

    @cached_property
    def containerProvider(self):  # pragma: no cover
        return ContainerProvider.make_one(self.boto3_raw_data["containerProvider"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateSecurityConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateSecurityConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SecurityConfiguration:
    boto3_raw_data: "type_defs.SecurityConfigurationTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    arn = field("arn")
    createdAt = field("createdAt")
    createdBy = field("createdBy")

    @cached_property
    def securityConfigurationData(self):  # pragma: no cover
        return SecurityConfigurationData.make_one(
            self.boto3_raw_data["securityConfigurationData"]
        )

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SecurityConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SecurityConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeJobTemplateResponse:
    boto3_raw_data: "type_defs.DescribeJobTemplateResponseTypeDef" = dataclasses.field()

    @cached_property
    def jobTemplate(self):  # pragma: no cover
        return JobTemplate.make_one(self.boto3_raw_data["jobTemplate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeJobTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeJobTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobTemplatesResponse:
    boto3_raw_data: "type_defs.ListJobTemplatesResponseTypeDef" = dataclasses.field()

    @cached_property
    def templates(self):  # pragma: no cover
        return JobTemplate.make_many(self.boto3_raw_data["templates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListJobTemplatesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListJobTemplatesResponsePaginator:
    boto3_raw_data: "type_defs.ListJobTemplatesResponsePaginatorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def templates(self):  # pragma: no cover
        return JobTemplatePaginator.make_many(self.boto3_raw_data["templates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListJobTemplatesResponsePaginatorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListJobTemplatesResponsePaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateJobTemplateRequest:
    boto3_raw_data: "type_defs.CreateJobTemplateRequestTypeDef" = dataclasses.field()

    name = field("name")
    clientToken = field("clientToken")
    jobTemplateData = field("jobTemplateData")
    tags = field("tags")
    kmsKeyArn = field("kmsKeyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateJobTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateJobTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSecurityConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeSecurityConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def securityConfiguration(self):  # pragma: no cover
        return SecurityConfiguration.make_one(
            self.boto3_raw_data["securityConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSecurityConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSecurityConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSecurityConfigurationsResponse:
    boto3_raw_data: "type_defs.ListSecurityConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def securityConfigurations(self):  # pragma: no cover
        return SecurityConfiguration.make_many(
            self.boto3_raw_data["securityConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListSecurityConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSecurityConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
