# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_appconfig import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class DeletionProtectionSettings:
    boto3_raw_data: "type_defs.DeletionProtectionSettingsTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    ProtectionPeriodInMinutes = field("ProtectionPeriodInMinutes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletionProtectionSettingsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletionProtectionSettingsTypeDef"]
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
class ActionInvocation:
    boto3_raw_data: "type_defs.ActionInvocationTypeDef" = dataclasses.field()

    ExtensionIdentifier = field("ExtensionIdentifier")
    ActionName = field("ActionName")
    Uri = field("Uri")
    RoleArn = field("RoleArn")
    ErrorMessage = field("ErrorMessage")
    ErrorCode = field("ErrorCode")
    InvocationId = field("InvocationId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionInvocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActionInvocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Action:
    boto3_raw_data: "type_defs.ActionTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")
    Uri = field("Uri")
    RoleArn = field("RoleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Application:
    boto3_raw_data: "type_defs.ApplicationTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApplicationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApplicationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AppliedExtension:
    boto3_raw_data: "type_defs.AppliedExtensionTypeDef" = dataclasses.field()

    ExtensionId = field("ExtensionId")
    ExtensionAssociationId = field("ExtensionAssociationId")
    VersionNumber = field("VersionNumber")
    Parameters = field("Parameters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AppliedExtensionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AppliedExtensionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationProfileSummary:
    boto3_raw_data: "type_defs.ConfigurationProfileSummaryTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    Id = field("Id")
    Name = field("Name")
    LocationUri = field("LocationUri")
    ValidatorTypes = field("ValidatorTypes")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationProfileSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationProfileSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Validator:
    boto3_raw_data: "type_defs.ValidatorTypeDef" = dataclasses.field()

    Type = field("Type")
    Content = field("Content")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ValidatorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ValidatorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApplicationRequest:
    boto3_raw_data: "type_defs.CreateApplicationRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Description = field("Description")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeploymentStrategyRequest:
    boto3_raw_data: "type_defs.CreateDeploymentStrategyRequestTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")
    DeploymentDurationInMinutes = field("DeploymentDurationInMinutes")
    GrowthFactor = field("GrowthFactor")
    Description = field("Description")
    FinalBakeTimeInMinutes = field("FinalBakeTimeInMinutes")
    GrowthType = field("GrowthType")
    ReplicateTo = field("ReplicateTo")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateDeploymentStrategyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeploymentStrategyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Monitor:
    boto3_raw_data: "type_defs.MonitorTypeDef" = dataclasses.field()

    AlarmArn = field("AlarmArn")
    AlarmRoleArn = field("AlarmRoleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MonitorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MonitorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateExtensionAssociationRequest:
    boto3_raw_data: "type_defs.CreateExtensionAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    ExtensionIdentifier = field("ExtensionIdentifier")
    ResourceIdentifier = field("ResourceIdentifier")
    ExtensionVersionNumber = field("ExtensionVersionNumber")
    Parameters = field("Parameters")
    Tags = field("Tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateExtensionAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExtensionAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Parameter:
    boto3_raw_data: "type_defs.ParameterTypeDef" = dataclasses.field()

    Description = field("Description")
    Required = field("Required")
    Dynamic = field("Dynamic")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParameterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParameterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationRequest:
    boto3_raw_data: "type_defs.DeleteApplicationRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConfigurationProfileRequest:
    boto3_raw_data: "type_defs.DeleteConfigurationProfileRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    ConfigurationProfileId = field("ConfigurationProfileId")
    DeletionProtectionCheck = field("DeletionProtectionCheck")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteConfigurationProfileRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConfigurationProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDeploymentStrategyRequest:
    boto3_raw_data: "type_defs.DeleteDeploymentStrategyRequestTypeDef" = (
        dataclasses.field()
    )

    DeploymentStrategyId = field("DeploymentStrategyId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDeploymentStrategyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDeploymentStrategyRequestTypeDef"]
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

    EnvironmentId = field("EnvironmentId")
    ApplicationId = field("ApplicationId")
    DeletionProtectionCheck = field("DeletionProtectionCheck")

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
class DeleteExtensionAssociationRequest:
    boto3_raw_data: "type_defs.DeleteExtensionAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    ExtensionAssociationId = field("ExtensionAssociationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteExtensionAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteExtensionAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteExtensionRequest:
    boto3_raw_data: "type_defs.DeleteExtensionRequestTypeDef" = dataclasses.field()

    ExtensionIdentifier = field("ExtensionIdentifier")
    VersionNumber = field("VersionNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteExtensionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteExtensionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteHostedConfigurationVersionRequest:
    boto3_raw_data: "type_defs.DeleteHostedConfigurationVersionRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    ConfigurationProfileId = field("ConfigurationProfileId")
    VersionNumber = field("VersionNumber")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteHostedConfigurationVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteHostedConfigurationVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentStrategy:
    boto3_raw_data: "type_defs.DeploymentStrategyTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Description = field("Description")
    DeploymentDurationInMinutes = field("DeploymentDurationInMinutes")
    GrowthType = field("GrowthType")
    GrowthFactor = field("GrowthFactor")
    FinalBakeTimeInMinutes = field("FinalBakeTimeInMinutes")
    ReplicateTo = field("ReplicateTo")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeploymentStrategyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentStrategyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentSummary:
    boto3_raw_data: "type_defs.DeploymentSummaryTypeDef" = dataclasses.field()

    DeploymentNumber = field("DeploymentNumber")
    ConfigurationName = field("ConfigurationName")
    ConfigurationVersion = field("ConfigurationVersion")
    DeploymentDurationInMinutes = field("DeploymentDurationInMinutes")
    GrowthType = field("GrowthType")
    GrowthFactor = field("GrowthFactor")
    FinalBakeTimeInMinutes = field("FinalBakeTimeInMinutes")
    State = field("State")
    PercentageComplete = field("PercentageComplete")
    StartedAt = field("StartedAt")
    CompletedAt = field("CompletedAt")
    VersionLabel = field("VersionLabel")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeploymentSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtensionAssociationSummary:
    boto3_raw_data: "type_defs.ExtensionAssociationSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    ExtensionArn = field("ExtensionArn")
    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExtensionAssociationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExtensionAssociationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtensionSummary:
    boto3_raw_data: "type_defs.ExtensionSummaryTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    VersionNumber = field("VersionNumber")
    Arn = field("Arn")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExtensionSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExtensionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetApplicationRequest:
    boto3_raw_data: "type_defs.GetApplicationRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfigurationProfileRequest:
    boto3_raw_data: "type_defs.GetConfigurationProfileRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    ConfigurationProfileId = field("ConfigurationProfileId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetConfigurationProfileRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfigurationProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfigurationRequest:
    boto3_raw_data: "type_defs.GetConfigurationRequestTypeDef" = dataclasses.field()

    Application = field("Application")
    Environment = field("Environment")
    Configuration = field("Configuration")
    ClientId = field("ClientId")
    ClientConfigurationVersion = field("ClientConfigurationVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConfigurationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentRequest:
    boto3_raw_data: "type_defs.GetDeploymentRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    EnvironmentId = field("EnvironmentId")
    DeploymentNumber = field("DeploymentNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentRequestTypeDef"]
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
class GetDeploymentStrategyRequest:
    boto3_raw_data: "type_defs.GetDeploymentStrategyRequestTypeDef" = (
        dataclasses.field()
    )

    DeploymentStrategyId = field("DeploymentStrategyId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentStrategyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentStrategyRequestTypeDef"]
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

    ApplicationId = field("ApplicationId")
    EnvironmentId = field("EnvironmentId")

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
class GetExtensionAssociationRequest:
    boto3_raw_data: "type_defs.GetExtensionAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    ExtensionAssociationId = field("ExtensionAssociationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetExtensionAssociationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExtensionAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExtensionRequest:
    boto3_raw_data: "type_defs.GetExtensionRequestTypeDef" = dataclasses.field()

    ExtensionIdentifier = field("ExtensionIdentifier")
    VersionNumber = field("VersionNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExtensionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExtensionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetHostedConfigurationVersionRequest:
    boto3_raw_data: "type_defs.GetHostedConfigurationVersionRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    ConfigurationProfileId = field("ConfigurationProfileId")
    VersionNumber = field("VersionNumber")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetHostedConfigurationVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetHostedConfigurationVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HostedConfigurationVersionSummary:
    boto3_raw_data: "type_defs.HostedConfigurationVersionSummaryTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    ConfigurationProfileId = field("ConfigurationProfileId")
    VersionNumber = field("VersionNumber")
    Description = field("Description")
    ContentType = field("ContentType")
    VersionLabel = field("VersionLabel")
    KmsKeyArn = field("KmsKeyArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.HostedConfigurationVersionSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HostedConfigurationVersionSummaryTypeDef"]
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
class ListApplicationsRequest:
    boto3_raw_data: "type_defs.ListApplicationsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListApplicationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfigurationProfilesRequest:
    boto3_raw_data: "type_defs.ListConfigurationProfilesRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    Type = field("Type")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListConfigurationProfilesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfigurationProfilesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentStrategiesRequest:
    boto3_raw_data: "type_defs.ListDeploymentStrategiesRequestTypeDef" = (
        dataclasses.field()
    )

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDeploymentStrategiesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentStrategiesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentsRequest:
    boto3_raw_data: "type_defs.ListDeploymentsRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    EnvironmentId = field("EnvironmentId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDeploymentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentsRequestTypeDef"]
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

    ApplicationId = field("ApplicationId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

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
class ListExtensionAssociationsRequest:
    boto3_raw_data: "type_defs.ListExtensionAssociationsRequestTypeDef" = (
        dataclasses.field()
    )

    ResourceIdentifier = field("ResourceIdentifier")
    ExtensionIdentifier = field("ExtensionIdentifier")
    ExtensionVersionNumber = field("ExtensionVersionNumber")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListExtensionAssociationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExtensionAssociationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExtensionsRequest:
    boto3_raw_data: "type_defs.ListExtensionsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExtensionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExtensionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHostedConfigurationVersionsRequest:
    boto3_raw_data: "type_defs.ListHostedConfigurationVersionsRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    ConfigurationProfileId = field("ConfigurationProfileId")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    VersionLabel = field("VersionLabel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListHostedConfigurationVersionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHostedConfigurationVersionsRequestTypeDef"]
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

    ResourceArn = field("ResourceArn")

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
class StartDeploymentRequest:
    boto3_raw_data: "type_defs.StartDeploymentRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    EnvironmentId = field("EnvironmentId")
    DeploymentStrategyId = field("DeploymentStrategyId")
    ConfigurationProfileId = field("ConfigurationProfileId")
    ConfigurationVersion = field("ConfigurationVersion")
    Description = field("Description")
    Tags = field("Tags")
    KmsKeyIdentifier = field("KmsKeyIdentifier")
    DynamicExtensionParameters = field("DynamicExtensionParameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartDeploymentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartDeploymentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopDeploymentRequest:
    boto3_raw_data: "type_defs.StopDeploymentRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    EnvironmentId = field("EnvironmentId")
    DeploymentNumber = field("DeploymentNumber")
    AllowRevert = field("AllowRevert")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopDeploymentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopDeploymentRequestTypeDef"]
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

    ResourceArn = field("ResourceArn")
    Tags = field("Tags")

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

    ResourceArn = field("ResourceArn")
    TagKeys = field("TagKeys")

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
class UpdateApplicationRequest:
    boto3_raw_data: "type_defs.UpdateApplicationRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    Name = field("Name")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApplicationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApplicationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDeploymentStrategyRequest:
    boto3_raw_data: "type_defs.UpdateDeploymentStrategyRequestTypeDef" = (
        dataclasses.field()
    )

    DeploymentStrategyId = field("DeploymentStrategyId")
    Description = field("Description")
    DeploymentDurationInMinutes = field("DeploymentDurationInMinutes")
    FinalBakeTimeInMinutes = field("FinalBakeTimeInMinutes")
    GrowthFactor = field("GrowthFactor")
    GrowthType = field("GrowthType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateDeploymentStrategyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDeploymentStrategyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateExtensionAssociationRequest:
    boto3_raw_data: "type_defs.UpdateExtensionAssociationRequestTypeDef" = (
        dataclasses.field()
    )

    ExtensionAssociationId = field("ExtensionAssociationId")
    Parameters = field("Parameters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateExtensionAssociationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateExtensionAssociationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidateConfigurationRequest:
    boto3_raw_data: "type_defs.ValidateConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    ConfigurationProfileId = field("ConfigurationProfileId")
    ConfigurationVersion = field("ConfigurationVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ValidateConfigurationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidateConfigurationRequestTypeDef"]
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
    def DeletionProtection(self):  # pragma: no cover
        return DeletionProtectionSettings.make_one(
            self.boto3_raw_data["DeletionProtection"]
        )

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
class AccountSettings:
    boto3_raw_data: "type_defs.AccountSettingsTypeDef" = dataclasses.field()

    @cached_property
    def DeletionProtection(self):  # pragma: no cover
        return DeletionProtectionSettings.make_one(
            self.boto3_raw_data["DeletionProtection"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationResponse:
    boto3_raw_data: "type_defs.ApplicationResponseTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationResponseTypeDef"]
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

    Content = field("Content")
    ConfigurationVersion = field("ConfigurationVersion")
    ContentType = field("ContentType")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

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
class DeploymentStrategyResponse:
    boto3_raw_data: "type_defs.DeploymentStrategyResponseTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    Description = field("Description")
    DeploymentDurationInMinutes = field("DeploymentDurationInMinutes")
    GrowthType = field("GrowthType")
    GrowthFactor = field("GrowthFactor")
    FinalBakeTimeInMinutes = field("FinalBakeTimeInMinutes")
    ReplicateTo = field("ReplicateTo")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeploymentStrategyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentStrategyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EmptyResponseMetadata:
    boto3_raw_data: "type_defs.EmptyResponseMetadataTypeDef" = dataclasses.field()

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EmptyResponseMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EmptyResponseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtensionAssociation:
    boto3_raw_data: "type_defs.ExtensionAssociationTypeDef" = dataclasses.field()

    Id = field("Id")
    ExtensionArn = field("ExtensionArn")
    ResourceArn = field("ResourceArn")
    Arn = field("Arn")
    Parameters = field("Parameters")
    ExtensionVersionNumber = field("ExtensionVersionNumber")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExtensionAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExtensionAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HostedConfigurationVersion:
    boto3_raw_data: "type_defs.HostedConfigurationVersionTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    ConfigurationProfileId = field("ConfigurationProfileId")
    VersionNumber = field("VersionNumber")
    Description = field("Description")
    Content = field("Content")
    ContentType = field("ContentType")
    VersionLabel = field("VersionLabel")
    KmsKeyArn = field("KmsKeyArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HostedConfigurationVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HostedConfigurationVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceTags:
    boto3_raw_data: "type_defs.ResourceTagsTypeDef" = dataclasses.field()

    Tags = field("Tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceTagsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceTagsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentEvent:
    boto3_raw_data: "type_defs.DeploymentEventTypeDef" = dataclasses.field()

    EventType = field("EventType")
    TriggeredBy = field("TriggeredBy")
    Description = field("Description")

    @cached_property
    def ActionInvocations(self):  # pragma: no cover
        return ActionInvocation.make_many(self.boto3_raw_data["ActionInvocations"])

    OccurredAt = field("OccurredAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeploymentEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeploymentEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Applications:
    boto3_raw_data: "type_defs.ApplicationsTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return Application.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ApplicationsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ApplicationsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateHostedConfigurationVersionRequest:
    boto3_raw_data: "type_defs.CreateHostedConfigurationVersionRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    ConfigurationProfileId = field("ConfigurationProfileId")
    Content = field("Content")
    ContentType = field("ContentType")
    Description = field("Description")
    LatestVersionNumber = field("LatestVersionNumber")
    VersionLabel = field("VersionLabel")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateHostedConfigurationVersionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateHostedConfigurationVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationProfiles:
    boto3_raw_data: "type_defs.ConfigurationProfilesTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return ConfigurationProfileSummary.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationProfilesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationProfilesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationProfile:
    boto3_raw_data: "type_defs.ConfigurationProfileTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    Id = field("Id")
    Name = field("Name")
    Description = field("Description")
    LocationUri = field("LocationUri")
    RetrievalRoleArn = field("RetrievalRoleArn")

    @cached_property
    def Validators(self):  # pragma: no cover
        return Validator.make_many(self.boto3_raw_data["Validators"])

    Type = field("Type")
    KmsKeyArn = field("KmsKeyArn")
    KmsKeyIdentifier = field("KmsKeyIdentifier")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationProfileTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationProfileTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfigurationProfileRequest:
    boto3_raw_data: "type_defs.CreateConfigurationProfileRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    Name = field("Name")
    LocationUri = field("LocationUri")
    Description = field("Description")
    RetrievalRoleArn = field("RetrievalRoleArn")

    @cached_property
    def Validators(self):  # pragma: no cover
        return Validator.make_many(self.boto3_raw_data["Validators"])

    Tags = field("Tags")
    Type = field("Type")
    KmsKeyIdentifier = field("KmsKeyIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConfigurationProfileRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConfigurationProfileRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConfigurationProfileRequest:
    boto3_raw_data: "type_defs.UpdateConfigurationProfileRequestTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    ConfigurationProfileId = field("ConfigurationProfileId")
    Name = field("Name")
    Description = field("Description")
    RetrievalRoleArn = field("RetrievalRoleArn")

    @cached_property
    def Validators(self):  # pragma: no cover
        return Validator.make_many(self.boto3_raw_data["Validators"])

    KmsKeyIdentifier = field("KmsKeyIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConfigurationProfileRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConfigurationProfileRequestTypeDef"]
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

    ApplicationId = field("ApplicationId")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def Monitors(self):  # pragma: no cover
        return Monitor.make_many(self.boto3_raw_data["Monitors"])

    Tags = field("Tags")

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


@dataclasses.dataclass(frozen=True)
class EnvironmentResponse:
    boto3_raw_data: "type_defs.EnvironmentResponseTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    Id = field("Id")
    Name = field("Name")
    Description = field("Description")
    State = field("State")

    @cached_property
    def Monitors(self):  # pragma: no cover
        return Monitor.make_many(self.boto3_raw_data["Monitors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Environment:
    boto3_raw_data: "type_defs.EnvironmentTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    Id = field("Id")
    Name = field("Name")
    Description = field("Description")
    State = field("State")

    @cached_property
    def Monitors(self):  # pragma: no cover
        return Monitor.make_many(self.boto3_raw_data["Monitors"])

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
class UpdateEnvironmentRequest:
    boto3_raw_data: "type_defs.UpdateEnvironmentRequestTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    EnvironmentId = field("EnvironmentId")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def Monitors(self):  # pragma: no cover
        return Monitor.make_many(self.boto3_raw_data["Monitors"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEnvironmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnvironmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateExtensionRequest:
    boto3_raw_data: "type_defs.CreateExtensionRequestTypeDef" = dataclasses.field()

    Name = field("Name")
    Actions = field("Actions")
    Description = field("Description")
    Parameters = field("Parameters")
    Tags = field("Tags")
    LatestVersionNumber = field("LatestVersionNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateExtensionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExtensionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Extension:
    boto3_raw_data: "type_defs.ExtensionTypeDef" = dataclasses.field()

    Id = field("Id")
    Name = field("Name")
    VersionNumber = field("VersionNumber")
    Arn = field("Arn")
    Description = field("Description")
    Actions = field("Actions")
    Parameters = field("Parameters")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExtensionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExtensionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateExtensionRequest:
    boto3_raw_data: "type_defs.UpdateExtensionRequestTypeDef" = dataclasses.field()

    ExtensionIdentifier = field("ExtensionIdentifier")
    Description = field("Description")
    Actions = field("Actions")
    Parameters = field("Parameters")
    VersionNumber = field("VersionNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateExtensionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateExtensionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentStrategies:
    boto3_raw_data: "type_defs.DeploymentStrategiesTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return DeploymentStrategy.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeploymentStrategiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentStrategiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Deployments:
    boto3_raw_data: "type_defs.DeploymentsTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return DeploymentSummary.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeploymentsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeploymentsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExtensionAssociations:
    boto3_raw_data: "type_defs.ExtensionAssociationsTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return ExtensionAssociationSummary.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExtensionAssociationsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExtensionAssociationsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Extensions:
    boto3_raw_data: "type_defs.ExtensionsTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return ExtensionSummary.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExtensionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExtensionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeploymentRequestWait:
    boto3_raw_data: "type_defs.GetDeploymentRequestWaitTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    EnvironmentId = field("EnvironmentId")
    DeploymentNumber = field("DeploymentNumber")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeploymentRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeploymentRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEnvironmentRequestWait:
    boto3_raw_data: "type_defs.GetEnvironmentRequestWaitTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    EnvironmentId = field("EnvironmentId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEnvironmentRequestWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEnvironmentRequestWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HostedConfigurationVersions:
    boto3_raw_data: "type_defs.HostedConfigurationVersionsTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return HostedConfigurationVersionSummary.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.HostedConfigurationVersionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HostedConfigurationVersionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListApplicationsRequestPaginate:
    boto3_raw_data: "type_defs.ListApplicationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListApplicationsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListApplicationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfigurationProfilesRequestPaginate:
    boto3_raw_data: "type_defs.ListConfigurationProfilesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    Type = field("Type")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfigurationProfilesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfigurationProfilesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentStrategiesRequestPaginate:
    boto3_raw_data: "type_defs.ListDeploymentStrategiesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListDeploymentStrategiesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentStrategiesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDeploymentsRequestPaginate:
    boto3_raw_data: "type_defs.ListDeploymentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ApplicationId = field("ApplicationId")
    EnvironmentId = field("EnvironmentId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDeploymentsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDeploymentsRequestPaginateTypeDef"]
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

    ApplicationId = field("ApplicationId")

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
class ListExtensionAssociationsRequestPaginate:
    boto3_raw_data: "type_defs.ListExtensionAssociationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceIdentifier = field("ResourceIdentifier")
    ExtensionIdentifier = field("ExtensionIdentifier")
    ExtensionVersionNumber = field("ExtensionVersionNumber")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListExtensionAssociationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExtensionAssociationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExtensionsRequestPaginate:
    boto3_raw_data: "type_defs.ListExtensionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    Name = field("Name")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListExtensionsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExtensionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHostedConfigurationVersionsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListHostedConfigurationVersionsRequestPaginateTypeDef"
    ) = dataclasses.field()

    ApplicationId = field("ApplicationId")
    ConfigurationProfileId = field("ConfigurationProfileId")
    VersionLabel = field("VersionLabel")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListHostedConfigurationVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable[
                "type_defs.ListHostedConfigurationVersionsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Deployment:
    boto3_raw_data: "type_defs.DeploymentTypeDef" = dataclasses.field()

    ApplicationId = field("ApplicationId")
    EnvironmentId = field("EnvironmentId")
    DeploymentStrategyId = field("DeploymentStrategyId")
    ConfigurationProfileId = field("ConfigurationProfileId")
    DeploymentNumber = field("DeploymentNumber")
    ConfigurationName = field("ConfigurationName")
    ConfigurationLocationUri = field("ConfigurationLocationUri")
    ConfigurationVersion = field("ConfigurationVersion")
    Description = field("Description")
    DeploymentDurationInMinutes = field("DeploymentDurationInMinutes")
    GrowthType = field("GrowthType")
    GrowthFactor = field("GrowthFactor")
    FinalBakeTimeInMinutes = field("FinalBakeTimeInMinutes")
    State = field("State")

    @cached_property
    def EventLog(self):  # pragma: no cover
        return DeploymentEvent.make_many(self.boto3_raw_data["EventLog"])

    PercentageComplete = field("PercentageComplete")
    StartedAt = field("StartedAt")
    CompletedAt = field("CompletedAt")

    @cached_property
    def AppliedExtensions(self):  # pragma: no cover
        return AppliedExtension.make_many(self.boto3_raw_data["AppliedExtensions"])

    KmsKeyArn = field("KmsKeyArn")
    KmsKeyIdentifier = field("KmsKeyIdentifier")
    VersionLabel = field("VersionLabel")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeploymentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeploymentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Environments:
    boto3_raw_data: "type_defs.EnvironmentsTypeDef" = dataclasses.field()

    @cached_property
    def Items(self):  # pragma: no cover
        return Environment.make_many(self.boto3_raw_data["Items"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnvironmentsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EnvironmentsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
