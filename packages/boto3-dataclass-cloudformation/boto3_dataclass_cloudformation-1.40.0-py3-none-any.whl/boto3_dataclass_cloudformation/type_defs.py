# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cloudformation import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccountGateResult:
    boto3_raw_data: "type_defs.AccountGateResultTypeDef" = dataclasses.field()

    Status = field("Status")
    StatusReason = field("StatusReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountGateResultTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccountGateResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccountLimit:
    boto3_raw_data: "type_defs.AccountLimitTypeDef" = dataclasses.field()

    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountLimitTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountLimitTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoggingConfig:
    boto3_raw_data: "type_defs.LoggingConfigTypeDef" = dataclasses.field()

    LogRoleArn = field("LogRoleArn")
    LogGroupName = field("LogGroupName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoggingConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoggingConfigTypeDef"]],
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
class AutoDeployment:
    boto3_raw_data: "type_defs.AutoDeploymentTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    RetainStacksOnAccountRemoval = field("RetainStacksOnAccountRemoval")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AutoDeploymentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AutoDeploymentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TypeConfigurationIdentifier:
    boto3_raw_data: "type_defs.TypeConfigurationIdentifierTypeDef" = dataclasses.field()

    TypeArn = field("TypeArn")
    TypeConfigurationAlias = field("TypeConfigurationAlias")
    TypeConfigurationArn = field("TypeConfigurationArn")
    Type = field("Type")
    TypeName = field("TypeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TypeConfigurationIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TypeConfigurationIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TypeConfigurationDetails:
    boto3_raw_data: "type_defs.TypeConfigurationDetailsTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Alias = field("Alias")
    Configuration = field("Configuration")
    LastUpdated = field("LastUpdated")
    TypeArn = field("TypeArn")
    TypeName = field("TypeName")
    IsDefaultConfiguration = field("IsDefaultConfiguration")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TypeConfigurationDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TypeConfigurationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelUpdateStackInputStackCancelUpdate:
    boto3_raw_data: "type_defs.CancelUpdateStackInputStackCancelUpdateTypeDef" = (
        dataclasses.field()
    )

    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CancelUpdateStackInputStackCancelUpdateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelUpdateStackInputStackCancelUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelUpdateStackInput:
    boto3_raw_data: "type_defs.CancelUpdateStackInputTypeDef" = dataclasses.field()

    StackName = field("StackName")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelUpdateStackInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelUpdateStackInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeSetHookResourceTargetDetails:
    boto3_raw_data: "type_defs.ChangeSetHookResourceTargetDetailsTypeDef" = (
        dataclasses.field()
    )

    LogicalResourceId = field("LogicalResourceId")
    ResourceType = field("ResourceType")
    ResourceAction = field("ResourceAction")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ChangeSetHookResourceTargetDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChangeSetHookResourceTargetDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeSetSummary:
    boto3_raw_data: "type_defs.ChangeSetSummaryTypeDef" = dataclasses.field()

    StackId = field("StackId")
    StackName = field("StackName")
    ChangeSetId = field("ChangeSetId")
    ChangeSetName = field("ChangeSetName")
    ExecutionStatus = field("ExecutionStatus")
    Status = field("Status")
    StatusReason = field("StatusReason")
    CreationTime = field("CreationTime")
    Description = field("Description")
    IncludeNestedStacks = field("IncludeNestedStacks")
    ParentChangeSetId = field("ParentChangeSetId")
    RootChangeSetId = field("RootChangeSetId")
    ImportExistingResources = field("ImportExistingResources")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChangeSetSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChangeSetSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContinueUpdateRollbackInput:
    boto3_raw_data: "type_defs.ContinueUpdateRollbackInputTypeDef" = dataclasses.field()

    StackName = field("StackName")
    RoleARN = field("RoleARN")
    ResourcesToSkip = field("ResourcesToSkip")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ContinueUpdateRollbackInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ContinueUpdateRollbackInputTypeDef"]
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

    ParameterKey = field("ParameterKey")
    ParameterValue = field("ParameterValue")
    UsePreviousValue = field("UsePreviousValue")
    ResolvedValue = field("ResolvedValue")

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
class ResourceToImport:
    boto3_raw_data: "type_defs.ResourceToImportTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    LogicalResourceId = field("LogicalResourceId")
    ResourceIdentifier = field("ResourceIdentifier")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceToImportTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceToImportTypeDef"]
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
class ResourceDefinition:
    boto3_raw_data: "type_defs.ResourceDefinitionTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    ResourceIdentifier = field("ResourceIdentifier")
    LogicalResourceId = field("LogicalResourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateConfiguration:
    boto3_raw_data: "type_defs.TemplateConfigurationTypeDef" = dataclasses.field()

    DeletionPolicy = field("DeletionPolicy")
    UpdateReplacePolicy = field("UpdateReplacePolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TemplateConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackDefinition:
    boto3_raw_data: "type_defs.StackDefinitionTypeDef" = dataclasses.field()

    StackName = field("StackName")
    TemplateBody = field("TemplateBody")
    TemplateURL = field("TemplateURL")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StackDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StackDefinitionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedExecution:
    boto3_raw_data: "type_defs.ManagedExecutionTypeDef" = dataclasses.field()

    Active = field("Active")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ManagedExecutionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedExecutionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeactivateTypeInput:
    boto3_raw_data: "type_defs.DeactivateTypeInputTypeDef" = dataclasses.field()

    TypeName = field("TypeName")
    Type = field("Type")
    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeactivateTypeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeactivateTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteChangeSetInput:
    boto3_raw_data: "type_defs.DeleteChangeSetInputTypeDef" = dataclasses.field()

    ChangeSetName = field("ChangeSetName")
    StackName = field("StackName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteChangeSetInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteChangeSetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGeneratedTemplateInput:
    boto3_raw_data: "type_defs.DeleteGeneratedTemplateInputTypeDef" = (
        dataclasses.field()
    )

    GeneratedTemplateName = field("GeneratedTemplateName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGeneratedTemplateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGeneratedTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStackInputStackDelete:
    boto3_raw_data: "type_defs.DeleteStackInputStackDeleteTypeDef" = dataclasses.field()

    RetainResources = field("RetainResources")
    RoleARN = field("RoleARN")
    ClientRequestToken = field("ClientRequestToken")
    DeletionMode = field("DeletionMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteStackInputStackDeleteTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStackInputStackDeleteTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStackInput:
    boto3_raw_data: "type_defs.DeleteStackInputTypeDef" = dataclasses.field()

    StackName = field("StackName")
    RetainResources = field("RetainResources")
    RoleARN = field("RoleARN")
    ClientRequestToken = field("ClientRequestToken")
    DeletionMode = field("DeletionMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteStackInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStackInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStackSetInput:
    boto3_raw_data: "type_defs.DeleteStackSetInputTypeDef" = dataclasses.field()

    StackSetName = field("StackSetName")
    CallAs = field("CallAs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteStackSetInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStackSetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentTargetsOutput:
    boto3_raw_data: "type_defs.DeploymentTargetsOutputTypeDef" = dataclasses.field()

    Accounts = field("Accounts")
    AccountsUrl = field("AccountsUrl")
    OrganizationalUnitIds = field("OrganizationalUnitIds")
    AccountFilterType = field("AccountFilterType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeploymentTargetsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentTargetsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeploymentTargets:
    boto3_raw_data: "type_defs.DeploymentTargetsTypeDef" = dataclasses.field()

    Accounts = field("Accounts")
    AccountsUrl = field("AccountsUrl")
    OrganizationalUnitIds = field("OrganizationalUnitIds")
    AccountFilterType = field("AccountFilterType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeploymentTargetsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeploymentTargetsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterTypeInput:
    boto3_raw_data: "type_defs.DeregisterTypeInputTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Type = field("Type")
    TypeName = field("TypeName")
    VersionId = field("VersionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeregisterTypeInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterTypeInputTypeDef"]
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
class DescribeAccountLimitsInput:
    boto3_raw_data: "type_defs.DescribeAccountLimitsInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")

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
class DescribeChangeSetHooksInput:
    boto3_raw_data: "type_defs.DescribeChangeSetHooksInputTypeDef" = dataclasses.field()

    ChangeSetName = field("ChangeSetName")
    StackName = field("StackName")
    NextToken = field("NextToken")
    LogicalResourceId = field("LogicalResourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeChangeSetHooksInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChangeSetHooksInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChangeSetInput:
    boto3_raw_data: "type_defs.DescribeChangeSetInputTypeDef" = dataclasses.field()

    ChangeSetName = field("ChangeSetName")
    StackName = field("StackName")
    NextToken = field("NextToken")
    IncludePropertyValues = field("IncludePropertyValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeChangeSetInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChangeSetInputTypeDef"]
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
class DescribeGeneratedTemplateInput:
    boto3_raw_data: "type_defs.DescribeGeneratedTemplateInputTypeDef" = (
        dataclasses.field()
    )

    GeneratedTemplateName = field("GeneratedTemplateName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeGeneratedTemplateInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGeneratedTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateProgress:
    boto3_raw_data: "type_defs.TemplateProgressTypeDef" = dataclasses.field()

    ResourcesSucceeded = field("ResourcesSucceeded")
    ResourcesFailed = field("ResourcesFailed")
    ResourcesProcessing = field("ResourcesProcessing")
    ResourcesPending = field("ResourcesPending")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TemplateProgressTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateProgressTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationsAccessInput:
    boto3_raw_data: "type_defs.DescribeOrganizationsAccessInputTypeDef" = (
        dataclasses.field()
    )

    CallAs = field("CallAs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeOrganizationsAccessInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOrganizationsAccessInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePublisherInput:
    boto3_raw_data: "type_defs.DescribePublisherInputTypeDef" = dataclasses.field()

    PublisherId = field("PublisherId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePublisherInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePublisherInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourceScanInput:
    boto3_raw_data: "type_defs.DescribeResourceScanInputTypeDef" = dataclasses.field()

    ResourceScanId = field("ResourceScanId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeResourceScanInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourceScanInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScanFilterOutput:
    boto3_raw_data: "type_defs.ScanFilterOutputTypeDef" = dataclasses.field()

    Types = field("Types")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScanFilterOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScanFilterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStackDriftDetectionStatusInput:
    boto3_raw_data: "type_defs.DescribeStackDriftDetectionStatusInputTypeDef" = (
        dataclasses.field()
    )

    StackDriftDetectionId = field("StackDriftDetectionId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeStackDriftDetectionStatusInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStackDriftDetectionStatusInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStackEventsInput:
    boto3_raw_data: "type_defs.DescribeStackEventsInputTypeDef" = dataclasses.field()

    StackName = field("StackName")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStackEventsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStackEventsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackEvent:
    boto3_raw_data: "type_defs.StackEventTypeDef" = dataclasses.field()

    StackId = field("StackId")
    EventId = field("EventId")
    StackName = field("StackName")
    Timestamp = field("Timestamp")
    LogicalResourceId = field("LogicalResourceId")
    PhysicalResourceId = field("PhysicalResourceId")
    ResourceType = field("ResourceType")
    ResourceStatus = field("ResourceStatus")
    ResourceStatusReason = field("ResourceStatusReason")
    ResourceProperties = field("ResourceProperties")
    ClientRequestToken = field("ClientRequestToken")
    HookType = field("HookType")
    HookStatus = field("HookStatus")
    HookStatusReason = field("HookStatusReason")
    HookInvocationPoint = field("HookInvocationPoint")
    HookInvocationId = field("HookInvocationId")
    HookFailureMode = field("HookFailureMode")
    DetailedStatus = field("DetailedStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StackEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StackEventTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStackInstanceInput:
    boto3_raw_data: "type_defs.DescribeStackInstanceInputTypeDef" = dataclasses.field()

    StackSetName = field("StackSetName")
    StackInstanceAccount = field("StackInstanceAccount")
    StackInstanceRegion = field("StackInstanceRegion")
    CallAs = field("CallAs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStackInstanceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStackInstanceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStackRefactorInput:
    boto3_raw_data: "type_defs.DescribeStackRefactorInputTypeDef" = dataclasses.field()

    StackRefactorId = field("StackRefactorId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStackRefactorInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStackRefactorInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStackResourceDriftsInput:
    boto3_raw_data: "type_defs.DescribeStackResourceDriftsInputTypeDef" = (
        dataclasses.field()
    )

    StackName = field("StackName")
    StackResourceDriftStatusFilters = field("StackResourceDriftStatusFilters")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeStackResourceDriftsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStackResourceDriftsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStackResourceInput:
    boto3_raw_data: "type_defs.DescribeStackResourceInputTypeDef" = dataclasses.field()

    StackName = field("StackName")
    LogicalResourceId = field("LogicalResourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStackResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStackResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStackResourcesInput:
    boto3_raw_data: "type_defs.DescribeStackResourcesInputTypeDef" = dataclasses.field()

    StackName = field("StackName")
    LogicalResourceId = field("LogicalResourceId")
    PhysicalResourceId = field("PhysicalResourceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStackResourcesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStackResourcesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStackSetInput:
    boto3_raw_data: "type_defs.DescribeStackSetInputTypeDef" = dataclasses.field()

    StackSetName = field("StackSetName")
    CallAs = field("CallAs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStackSetInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStackSetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStackSetOperationInput:
    boto3_raw_data: "type_defs.DescribeStackSetOperationInputTypeDef" = (
        dataclasses.field()
    )

    StackSetName = field("StackSetName")
    OperationId = field("OperationId")
    CallAs = field("CallAs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeStackSetOperationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStackSetOperationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStacksInput:
    boto3_raw_data: "type_defs.DescribeStacksInputTypeDef" = dataclasses.field()

    StackName = field("StackName")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStacksInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStacksInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTypeInput:
    boto3_raw_data: "type_defs.DescribeTypeInputTypeDef" = dataclasses.field()

    Type = field("Type")
    TypeName = field("TypeName")
    Arn = field("Arn")
    VersionId = field("VersionId")
    PublisherId = field("PublisherId")
    PublicVersionNumber = field("PublicVersionNumber")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DescribeTypeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequiredActivatedType:
    boto3_raw_data: "type_defs.RequiredActivatedTypeTypeDef" = dataclasses.field()

    TypeNameAlias = field("TypeNameAlias")
    OriginalTypeName = field("OriginalTypeName")
    PublisherId = field("PublisherId")
    SupportedMajorVersions = field("SupportedMajorVersions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RequiredActivatedTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequiredActivatedTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTypeRegistrationInput:
    boto3_raw_data: "type_defs.DescribeTypeRegistrationInputTypeDef" = (
        dataclasses.field()
    )

    RegistrationToken = field("RegistrationToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeTypeRegistrationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTypeRegistrationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectStackDriftInput:
    boto3_raw_data: "type_defs.DetectStackDriftInputTypeDef" = dataclasses.field()

    StackName = field("StackName")
    LogicalResourceIds = field("LogicalResourceIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectStackDriftInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectStackDriftInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectStackResourceDriftInput:
    boto3_raw_data: "type_defs.DetectStackResourceDriftInputTypeDef" = (
        dataclasses.field()
    )

    StackName = field("StackName")
    LogicalResourceId = field("LogicalResourceId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DetectStackResourceDriftInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectStackResourceDriftInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteChangeSetInput:
    boto3_raw_data: "type_defs.ExecuteChangeSetInputTypeDef" = dataclasses.field()

    ChangeSetName = field("ChangeSetName")
    StackName = field("StackName")
    ClientRequestToken = field("ClientRequestToken")
    DisableRollback = field("DisableRollback")
    RetainExceptOnCreate = field("RetainExceptOnCreate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteChangeSetInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteChangeSetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExecuteStackRefactorInput:
    boto3_raw_data: "type_defs.ExecuteStackRefactorInputTypeDef" = dataclasses.field()

    StackRefactorId = field("StackRefactorId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExecuteStackRefactorInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExecuteStackRefactorInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Export:
    boto3_raw_data: "type_defs.ExportTypeDef" = dataclasses.field()

    ExportingStackId = field("ExportingStackId")
    Name = field("Name")
    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExportTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGeneratedTemplateInput:
    boto3_raw_data: "type_defs.GetGeneratedTemplateInputTypeDef" = dataclasses.field()

    GeneratedTemplateName = field("GeneratedTemplateName")
    Format = field("Format")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGeneratedTemplateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGeneratedTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStackPolicyInput:
    boto3_raw_data: "type_defs.GetStackPolicyInputTypeDef" = dataclasses.field()

    StackName = field("StackName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStackPolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStackPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTemplateInput:
    boto3_raw_data: "type_defs.GetTemplateInputTypeDef" = dataclasses.field()

    StackName = field("StackName")
    ChangeSetName = field("ChangeSetName")
    TemplateStage = field("TemplateStage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTemplateInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateSummaryConfig:
    boto3_raw_data: "type_defs.TemplateSummaryConfigTypeDef" = dataclasses.field()

    TreatUnrecognizedResourceTypesAsWarnings = field(
        "TreatUnrecognizedResourceTypesAsWarnings"
    )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TemplateSummaryConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateSummaryConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceIdentifierSummary:
    boto3_raw_data: "type_defs.ResourceIdentifierSummaryTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    LogicalResourceIds = field("LogicalResourceIds")
    ResourceIdentifiers = field("ResourceIdentifiers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceIdentifierSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceIdentifierSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Warnings:
    boto3_raw_data: "type_defs.WarningsTypeDef" = dataclasses.field()

    UnrecognizedResourceTypes = field("UnrecognizedResourceTypes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WarningsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WarningsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class HookResultSummary:
    boto3_raw_data: "type_defs.HookResultSummaryTypeDef" = dataclasses.field()

    HookResultId = field("HookResultId")
    InvocationPoint = field("InvocationPoint")
    FailureMode = field("FailureMode")
    TypeName = field("TypeName")
    TypeVersionId = field("TypeVersionId")
    TypeConfigurationVersionId = field("TypeConfigurationVersionId")
    Status = field("Status")
    HookStatusReason = field("HookStatusReason")
    InvokedAt = field("InvokedAt")
    TargetType = field("TargetType")
    TargetId = field("TargetId")
    TypeArn = field("TypeArn")
    HookExecutionTarget = field("HookExecutionTarget")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HookResultSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.HookResultSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChangeSetsInput:
    boto3_raw_data: "type_defs.ListChangeSetsInputTypeDef" = dataclasses.field()

    StackName = field("StackName")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChangeSetsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChangeSetsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExportsInput:
    boto3_raw_data: "type_defs.ListExportsInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListExportsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExportsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGeneratedTemplatesInput:
    boto3_raw_data: "type_defs.ListGeneratedTemplatesInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGeneratedTemplatesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGeneratedTemplatesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateSummary:
    boto3_raw_data: "type_defs.TemplateSummaryTypeDef" = dataclasses.field()

    GeneratedTemplateId = field("GeneratedTemplateId")
    GeneratedTemplateName = field("GeneratedTemplateName")
    Status = field("Status")
    StatusReason = field("StatusReason")
    CreationTime = field("CreationTime")
    LastUpdatedTime = field("LastUpdatedTime")
    NumberOfResources = field("NumberOfResources")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TemplateSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TemplateSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHookResultsInput:
    boto3_raw_data: "type_defs.ListHookResultsInputTypeDef" = dataclasses.field()

    TargetType = field("TargetType")
    TargetId = field("TargetId")
    TypeArn = field("TypeArn")
    Status = field("Status")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListHookResultsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHookResultsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportsInput:
    boto3_raw_data: "type_defs.ListImportsInputTypeDef" = dataclasses.field()

    ExportName = field("ExportName")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListImportsInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScannedResourceIdentifier:
    boto3_raw_data: "type_defs.ScannedResourceIdentifierTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    ResourceIdentifier = field("ResourceIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScannedResourceIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScannedResourceIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScannedResource:
    boto3_raw_data: "type_defs.ScannedResourceTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    ResourceIdentifier = field("ResourceIdentifier")
    ManagedByStack = field("ManagedByStack")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScannedResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScannedResourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceScanResourcesInput:
    boto3_raw_data: "type_defs.ListResourceScanResourcesInputTypeDef" = (
        dataclasses.field()
    )

    ResourceScanId = field("ResourceScanId")
    ResourceIdentifier = field("ResourceIdentifier")
    ResourceTypePrefix = field("ResourceTypePrefix")
    TagKey = field("TagKey")
    TagValue = field("TagValue")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResourceScanResourcesInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceScanResourcesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceScansInput:
    boto3_raw_data: "type_defs.ListResourceScansInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    ScanTypeFilter = field("ScanTypeFilter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourceScansInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceScansInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceScanSummary:
    boto3_raw_data: "type_defs.ResourceScanSummaryTypeDef" = dataclasses.field()

    ResourceScanId = field("ResourceScanId")
    Status = field("Status")
    StatusReason = field("StatusReason")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    PercentageCompleted = field("PercentageCompleted")
    ScanType = field("ScanType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceScanSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceScanSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackInstanceResourceDriftsInput:
    boto3_raw_data: "type_defs.ListStackInstanceResourceDriftsInputTypeDef" = (
        dataclasses.field()
    )

    StackSetName = field("StackSetName")
    StackInstanceAccount = field("StackInstanceAccount")
    StackInstanceRegion = field("StackInstanceRegion")
    OperationId = field("OperationId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    StackInstanceResourceDriftStatuses = field("StackInstanceResourceDriftStatuses")
    CallAs = field("CallAs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStackInstanceResourceDriftsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackInstanceResourceDriftsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackInstanceFilter:
    boto3_raw_data: "type_defs.StackInstanceFilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StackInstanceFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StackInstanceFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackRefactorActionsInput:
    boto3_raw_data: "type_defs.ListStackRefactorActionsInputTypeDef" = (
        dataclasses.field()
    )

    StackRefactorId = field("StackRefactorId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListStackRefactorActionsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackRefactorActionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackRefactorsInput:
    boto3_raw_data: "type_defs.ListStackRefactorsInputTypeDef" = dataclasses.field()

    ExecutionStatusFilter = field("ExecutionStatusFilter")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStackRefactorsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackRefactorsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackRefactorSummary:
    boto3_raw_data: "type_defs.StackRefactorSummaryTypeDef" = dataclasses.field()

    StackRefactorId = field("StackRefactorId")
    Description = field("Description")
    ExecutionStatus = field("ExecutionStatus")
    ExecutionStatusReason = field("ExecutionStatusReason")
    Status = field("Status")
    StatusReason = field("StatusReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StackRefactorSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StackRefactorSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackResourcesInput:
    boto3_raw_data: "type_defs.ListStackResourcesInputTypeDef" = dataclasses.field()

    StackName = field("StackName")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStackResourcesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackResourcesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackSetAutoDeploymentTargetsInput:
    boto3_raw_data: "type_defs.ListStackSetAutoDeploymentTargetsInputTypeDef" = (
        dataclasses.field()
    )

    StackSetName = field("StackSetName")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    CallAs = field("CallAs")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStackSetAutoDeploymentTargetsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackSetAutoDeploymentTargetsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackSetAutoDeploymentTargetSummary:
    boto3_raw_data: "type_defs.StackSetAutoDeploymentTargetSummaryTypeDef" = (
        dataclasses.field()
    )

    OrganizationalUnitId = field("OrganizationalUnitId")
    Regions = field("Regions")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StackSetAutoDeploymentTargetSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StackSetAutoDeploymentTargetSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OperationResultFilter:
    boto3_raw_data: "type_defs.OperationResultFilterTypeDef" = dataclasses.field()

    Name = field("Name")
    Values = field("Values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OperationResultFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OperationResultFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackSetOperationsInput:
    boto3_raw_data: "type_defs.ListStackSetOperationsInputTypeDef" = dataclasses.field()

    StackSetName = field("StackSetName")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    CallAs = field("CallAs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStackSetOperationsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackSetOperationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackSetsInput:
    boto3_raw_data: "type_defs.ListStackSetsInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    Status = field("Status")
    CallAs = field("CallAs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStackSetsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackSetsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStacksInput:
    boto3_raw_data: "type_defs.ListStacksInputTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    StackStatusFilter = field("StackStatusFilter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListStacksInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListStacksInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTypeRegistrationsInput:
    boto3_raw_data: "type_defs.ListTypeRegistrationsInputTypeDef" = dataclasses.field()

    Type = field("Type")
    TypeName = field("TypeName")
    TypeArn = field("TypeArn")
    RegistrationStatusFilter = field("RegistrationStatusFilter")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTypeRegistrationsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTypeRegistrationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTypeVersionsInput:
    boto3_raw_data: "type_defs.ListTypeVersionsInputTypeDef" = dataclasses.field()

    Type = field("Type")
    TypeName = field("TypeName")
    Arn = field("Arn")
    MaxResults = field("MaxResults")
    NextToken = field("NextToken")
    DeprecatedStatus = field("DeprecatedStatus")
    PublisherId = field("PublisherId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTypeVersionsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTypeVersionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TypeVersionSummary:
    boto3_raw_data: "type_defs.TypeVersionSummaryTypeDef" = dataclasses.field()

    Type = field("Type")
    TypeName = field("TypeName")
    VersionId = field("VersionId")
    IsDefaultVersion = field("IsDefaultVersion")
    Arn = field("Arn")
    TimeCreated = field("TimeCreated")
    Description = field("Description")
    PublicVersionNumber = field("PublicVersionNumber")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TypeVersionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TypeVersionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TypeFilters:
    boto3_raw_data: "type_defs.TypeFiltersTypeDef" = dataclasses.field()

    Category = field("Category")
    PublisherId = field("PublisherId")
    TypeNamePrefix = field("TypeNamePrefix")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TypeFiltersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TypeFiltersTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TypeSummary:
    boto3_raw_data: "type_defs.TypeSummaryTypeDef" = dataclasses.field()

    Type = field("Type")
    TypeName = field("TypeName")
    DefaultVersionId = field("DefaultVersionId")
    TypeArn = field("TypeArn")
    LastUpdated = field("LastUpdated")
    Description = field("Description")
    PublisherId = field("PublisherId")
    OriginalTypeName = field("OriginalTypeName")
    PublicVersionNumber = field("PublicVersionNumber")
    LatestPublicVersion = field("LatestPublicVersion")
    PublisherIdentity = field("PublisherIdentity")
    PublisherName = field("PublisherName")
    IsActivated = field("IsActivated")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TypeSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TypeSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModuleInfo:
    boto3_raw_data: "type_defs.ModuleInfoTypeDef" = dataclasses.field()

    TypeHierarchy = field("TypeHierarchy")
    LogicalIdHierarchy = field("LogicalIdHierarchy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ModuleInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ModuleInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Output:
    boto3_raw_data: "type_defs.OutputTypeDef" = dataclasses.field()

    OutputKey = field("OutputKey")
    OutputValue = field("OutputValue")
    Description = field("Description")
    ExportName = field("ExportName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterConstraints:
    boto3_raw_data: "type_defs.ParameterConstraintsTypeDef" = dataclasses.field()

    AllowedValues = field("AllowedValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParameterConstraintsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParameterConstraintsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PhysicalResourceIdContextKeyValuePair:
    boto3_raw_data: "type_defs.PhysicalResourceIdContextKeyValuePairTypeDef" = (
        dataclasses.field()
    )

    Key = field("Key")
    Value = field("Value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PhysicalResourceIdContextKeyValuePairTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PhysicalResourceIdContextKeyValuePairTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PropertyDifference:
    boto3_raw_data: "type_defs.PropertyDifferenceTypeDef" = dataclasses.field()

    PropertyPath = field("PropertyPath")
    ExpectedValue = field("ExpectedValue")
    ActualValue = field("ActualValue")
    DifferenceType = field("DifferenceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PropertyDifferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PropertyDifferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublishTypeInput:
    boto3_raw_data: "type_defs.PublishTypeInputTypeDef" = dataclasses.field()

    Type = field("Type")
    Arn = field("Arn")
    TypeName = field("TypeName")
    PublicVersionNumber = field("PublicVersionNumber")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PublishTypeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublishTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordHandlerProgressInput:
    boto3_raw_data: "type_defs.RecordHandlerProgressInputTypeDef" = dataclasses.field()

    BearerToken = field("BearerToken")
    OperationStatus = field("OperationStatus")
    CurrentOperationStatus = field("CurrentOperationStatus")
    StatusMessage = field("StatusMessage")
    ErrorCode = field("ErrorCode")
    ResourceModel = field("ResourceModel")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RecordHandlerProgressInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RecordHandlerProgressInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterPublisherInput:
    boto3_raw_data: "type_defs.RegisterPublisherInputTypeDef" = dataclasses.field()

    AcceptTermsAndConditions = field("AcceptTermsAndConditions")
    ConnectionArn = field("ConnectionArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterPublisherInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterPublisherInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceTargetDefinition:
    boto3_raw_data: "type_defs.ResourceTargetDefinitionTypeDef" = dataclasses.field()

    Attribute = field("Attribute")
    Name = field("Name")
    RequiresRecreation = field("RequiresRecreation")
    Path = field("Path")
    BeforeValue = field("BeforeValue")
    AfterValue = field("AfterValue")
    AttributeChangeType = field("AttributeChangeType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceTargetDefinitionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceTargetDefinitionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceLocation:
    boto3_raw_data: "type_defs.ResourceLocationTypeDef" = dataclasses.field()

    StackName = field("StackName")
    LogicalResourceId = field("LogicalResourceId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceLocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceLocationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RollbackTrigger:
    boto3_raw_data: "type_defs.RollbackTriggerTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Type = field("Type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RollbackTriggerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RollbackTriggerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RollbackStackInput:
    boto3_raw_data: "type_defs.RollbackStackInputTypeDef" = dataclasses.field()

    StackName = field("StackName")
    RoleARN = field("RoleARN")
    ClientRequestToken = field("ClientRequestToken")
    RetainExceptOnCreate = field("RetainExceptOnCreate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RollbackStackInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RollbackStackInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScanFilter:
    boto3_raw_data: "type_defs.ScanFilterTypeDef" = dataclasses.field()

    Types = field("Types")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScanFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScanFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetStackPolicyInput:
    boto3_raw_data: "type_defs.SetStackPolicyInputTypeDef" = dataclasses.field()

    StackName = field("StackName")
    StackPolicyBody = field("StackPolicyBody")
    StackPolicyURL = field("StackPolicyURL")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetStackPolicyInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetStackPolicyInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetTypeConfigurationInput:
    boto3_raw_data: "type_defs.SetTypeConfigurationInputTypeDef" = dataclasses.field()

    Configuration = field("Configuration")
    TypeArn = field("TypeArn")
    ConfigurationAlias = field("ConfigurationAlias")
    TypeName = field("TypeName")
    Type = field("Type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetTypeConfigurationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetTypeConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetTypeDefaultVersionInput:
    boto3_raw_data: "type_defs.SetTypeDefaultVersionInputTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Type = field("Type")
    TypeName = field("TypeName")
    VersionId = field("VersionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetTypeDefaultVersionInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetTypeDefaultVersionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SignalResourceInput:
    boto3_raw_data: "type_defs.SignalResourceInputTypeDef" = dataclasses.field()

    StackName = field("StackName")
    LogicalResourceId = field("LogicalResourceId")
    UniqueId = field("UniqueId")
    Status = field("Status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SignalResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SignalResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackDriftInformationSummary:
    boto3_raw_data: "type_defs.StackDriftInformationSummaryTypeDef" = (
        dataclasses.field()
    )

    StackDriftStatus = field("StackDriftStatus")
    LastCheckTimestamp = field("LastCheckTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StackDriftInformationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StackDriftInformationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackDriftInformation:
    boto3_raw_data: "type_defs.StackDriftInformationTypeDef" = dataclasses.field()

    StackDriftStatus = field("StackDriftStatus")
    LastCheckTimestamp = field("LastCheckTimestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StackDriftInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StackDriftInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackInstanceComprehensiveStatus:
    boto3_raw_data: "type_defs.StackInstanceComprehensiveStatusTypeDef" = (
        dataclasses.field()
    )

    DetailedStatus = field("DetailedStatus")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StackInstanceComprehensiveStatusTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StackInstanceComprehensiveStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackResourceDriftInformation:
    boto3_raw_data: "type_defs.StackResourceDriftInformationTypeDef" = (
        dataclasses.field()
    )

    StackResourceDriftStatus = field("StackResourceDriftStatus")
    LastCheckTimestamp = field("LastCheckTimestamp")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StackResourceDriftInformationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StackResourceDriftInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackResourceDriftInformationSummary:
    boto3_raw_data: "type_defs.StackResourceDriftInformationSummaryTypeDef" = (
        dataclasses.field()
    )

    StackResourceDriftStatus = field("StackResourceDriftStatus")
    LastCheckTimestamp = field("LastCheckTimestamp")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StackResourceDriftInformationSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StackResourceDriftInformationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackSetDriftDetectionDetails:
    boto3_raw_data: "type_defs.StackSetDriftDetectionDetailsTypeDef" = (
        dataclasses.field()
    )

    DriftStatus = field("DriftStatus")
    DriftDetectionStatus = field("DriftDetectionStatus")
    LastDriftCheckTimestamp = field("LastDriftCheckTimestamp")
    TotalStackInstancesCount = field("TotalStackInstancesCount")
    DriftedStackInstancesCount = field("DriftedStackInstancesCount")
    InSyncStackInstancesCount = field("InSyncStackInstancesCount")
    InProgressStackInstancesCount = field("InProgressStackInstancesCount")
    FailedStackInstancesCount = field("FailedStackInstancesCount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StackSetDriftDetectionDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StackSetDriftDetectionDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackSetOperationPreferencesOutput:
    boto3_raw_data: "type_defs.StackSetOperationPreferencesOutputTypeDef" = (
        dataclasses.field()
    )

    RegionConcurrencyType = field("RegionConcurrencyType")
    RegionOrder = field("RegionOrder")
    FailureToleranceCount = field("FailureToleranceCount")
    FailureTolerancePercentage = field("FailureTolerancePercentage")
    MaxConcurrentCount = field("MaxConcurrentCount")
    MaxConcurrentPercentage = field("MaxConcurrentPercentage")
    ConcurrencyMode = field("ConcurrencyMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StackSetOperationPreferencesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StackSetOperationPreferencesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackSetOperationPreferences:
    boto3_raw_data: "type_defs.StackSetOperationPreferencesTypeDef" = (
        dataclasses.field()
    )

    RegionConcurrencyType = field("RegionConcurrencyType")
    RegionOrder = field("RegionOrder")
    FailureToleranceCount = field("FailureToleranceCount")
    FailureTolerancePercentage = field("FailureTolerancePercentage")
    MaxConcurrentCount = field("MaxConcurrentCount")
    MaxConcurrentPercentage = field("MaxConcurrentPercentage")
    ConcurrencyMode = field("ConcurrencyMode")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StackSetOperationPreferencesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StackSetOperationPreferencesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackSetOperationStatusDetails:
    boto3_raw_data: "type_defs.StackSetOperationStatusDetailsTypeDef" = (
        dataclasses.field()
    )

    FailedStackInstancesCount = field("FailedStackInstancesCount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StackSetOperationStatusDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StackSetOperationStatusDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopStackSetOperationInput:
    boto3_raw_data: "type_defs.StopStackSetOperationInputTypeDef" = dataclasses.field()

    StackSetName = field("StackSetName")
    OperationId = field("OperationId")
    CallAs = field("CallAs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopStackSetOperationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopStackSetOperationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateParameter:
    boto3_raw_data: "type_defs.TemplateParameterTypeDef" = dataclasses.field()

    ParameterKey = field("ParameterKey")
    DefaultValue = field("DefaultValue")
    NoEcho = field("NoEcho")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TemplateParameterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TemplateParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestTypeInput:
    boto3_raw_data: "type_defs.TestTypeInputTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Type = field("Type")
    TypeName = field("TypeName")
    VersionId = field("VersionId")
    LogDeliveryBucket = field("LogDeliveryBucket")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestTypeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TestTypeInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTerminationProtectionInput:
    boto3_raw_data: "type_defs.UpdateTerminationProtectionInputTypeDef" = (
        dataclasses.field()
    )

    EnableTerminationProtection = field("EnableTerminationProtection")
    StackName = field("StackName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateTerminationProtectionInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTerminationProtectionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidateTemplateInput:
    boto3_raw_data: "type_defs.ValidateTemplateInputTypeDef" = dataclasses.field()

    TemplateBody = field("TemplateBody")
    TemplateURL = field("TemplateURL")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ValidateTemplateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidateTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WarningProperty:
    boto3_raw_data: "type_defs.WarningPropertyTypeDef" = dataclasses.field()

    PropertyPath = field("PropertyPath")
    Required = field("Required")
    Description = field("Description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WarningPropertyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WarningPropertyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackSetOperationResultSummary:
    boto3_raw_data: "type_defs.StackSetOperationResultSummaryTypeDef" = (
        dataclasses.field()
    )

    Account = field("Account")
    Region = field("Region")
    Status = field("Status")
    StatusReason = field("StatusReason")

    @cached_property
    def AccountGateResult(self):  # pragma: no cover
        return AccountGateResult.make_one(self.boto3_raw_data["AccountGateResult"])

    OrganizationalUnitId = field("OrganizationalUnitId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.StackSetOperationResultSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StackSetOperationResultSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivateTypeInput:
    boto3_raw_data: "type_defs.ActivateTypeInputTypeDef" = dataclasses.field()

    Type = field("Type")
    PublicTypeArn = field("PublicTypeArn")
    PublisherId = field("PublisherId")
    TypeName = field("TypeName")
    TypeNameAlias = field("TypeNameAlias")
    AutoUpdate = field("AutoUpdate")

    @cached_property
    def LoggingConfig(self):  # pragma: no cover
        return LoggingConfig.make_one(self.boto3_raw_data["LoggingConfig"])

    ExecutionRoleArn = field("ExecutionRoleArn")
    VersionBump = field("VersionBump")
    MajorVersion = field("MajorVersion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActivateTypeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivateTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterTypeInput:
    boto3_raw_data: "type_defs.RegisterTypeInputTypeDef" = dataclasses.field()

    TypeName = field("TypeName")
    SchemaHandlerPackage = field("SchemaHandlerPackage")
    Type = field("Type")

    @cached_property
    def LoggingConfig(self):  # pragma: no cover
        return LoggingConfig.make_one(self.boto3_raw_data["LoggingConfig"])

    ExecutionRoleArn = field("ExecutionRoleArn")
    ClientRequestToken = field("ClientRequestToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RegisterTypeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterTypeInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActivateTypeOutput:
    boto3_raw_data: "type_defs.ActivateTypeOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ActivateTypeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ActivateTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChangeSetOutput:
    boto3_raw_data: "type_defs.CreateChangeSetOutputTypeDef" = dataclasses.field()

    Id = field("Id")
    StackId = field("StackId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateChangeSetOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChangeSetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGeneratedTemplateOutput:
    boto3_raw_data: "type_defs.CreateGeneratedTemplateOutputTypeDef" = (
        dataclasses.field()
    )

    GeneratedTemplateId = field("GeneratedTemplateId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateGeneratedTemplateOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGeneratedTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStackInstancesOutput:
    boto3_raw_data: "type_defs.CreateStackInstancesOutputTypeDef" = dataclasses.field()

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStackInstancesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStackInstancesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStackOutput:
    boto3_raw_data: "type_defs.CreateStackOutputTypeDef" = dataclasses.field()

    StackId = field("StackId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateStackOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStackOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStackRefactorOutput:
    boto3_raw_data: "type_defs.CreateStackRefactorOutputTypeDef" = dataclasses.field()

    StackRefactorId = field("StackRefactorId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStackRefactorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStackRefactorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStackSetOutput:
    boto3_raw_data: "type_defs.CreateStackSetOutputTypeDef" = dataclasses.field()

    StackSetId = field("StackSetId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStackSetOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStackSetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStackInstancesOutput:
    boto3_raw_data: "type_defs.DeleteStackInstancesOutputTypeDef" = dataclasses.field()

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteStackInstancesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStackInstancesOutputTypeDef"]
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
    def AccountLimits(self):  # pragma: no cover
        return AccountLimit.make_many(self.boto3_raw_data["AccountLimits"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

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
class DescribeOrganizationsAccessOutput:
    boto3_raw_data: "type_defs.DescribeOrganizationsAccessOutputTypeDef" = (
        dataclasses.field()
    )

    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrganizationsAccessOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOrganizationsAccessOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePublisherOutput:
    boto3_raw_data: "type_defs.DescribePublisherOutputTypeDef" = dataclasses.field()

    PublisherId = field("PublisherId")
    PublisherStatus = field("PublisherStatus")
    IdentityProvider = field("IdentityProvider")
    PublisherProfile = field("PublisherProfile")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribePublisherOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePublisherOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStackDriftDetectionStatusOutput:
    boto3_raw_data: "type_defs.DescribeStackDriftDetectionStatusOutputTypeDef" = (
        dataclasses.field()
    )

    StackId = field("StackId")
    StackDriftDetectionId = field("StackDriftDetectionId")
    StackDriftStatus = field("StackDriftStatus")
    DetectionStatus = field("DetectionStatus")
    DetectionStatusReason = field("DetectionStatusReason")
    DriftedStackResourceCount = field("DriftedStackResourceCount")
    Timestamp = field("Timestamp")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeStackDriftDetectionStatusOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStackDriftDetectionStatusOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStackRefactorOutput:
    boto3_raw_data: "type_defs.DescribeStackRefactorOutputTypeDef" = dataclasses.field()

    Description = field("Description")
    StackRefactorId = field("StackRefactorId")
    StackIds = field("StackIds")
    ExecutionStatus = field("ExecutionStatus")
    ExecutionStatusReason = field("ExecutionStatusReason")
    Status = field("Status")
    StatusReason = field("StatusReason")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStackRefactorOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStackRefactorOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTypeRegistrationOutput:
    boto3_raw_data: "type_defs.DescribeTypeRegistrationOutputTypeDef" = (
        dataclasses.field()
    )

    ProgressStatus = field("ProgressStatus")
    Description = field("Description")
    TypeArn = field("TypeArn")
    TypeVersionArn = field("TypeVersionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeTypeRegistrationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTypeRegistrationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectStackDriftOutput:
    boto3_raw_data: "type_defs.DetectStackDriftOutputTypeDef" = dataclasses.field()

    StackDriftDetectionId = field("StackDriftDetectionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectStackDriftOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectStackDriftOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectStackSetDriftOutput:
    boto3_raw_data: "type_defs.DetectStackSetDriftOutputTypeDef" = dataclasses.field()

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectStackSetDriftOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectStackSetDriftOutputTypeDef"]
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
class EstimateTemplateCostOutput:
    boto3_raw_data: "type_defs.EstimateTemplateCostOutputTypeDef" = dataclasses.field()

    Url = field("Url")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EstimateTemplateCostOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EstimateTemplateCostOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetGeneratedTemplateOutput:
    boto3_raw_data: "type_defs.GetGeneratedTemplateOutputTypeDef" = dataclasses.field()

    Status = field("Status")
    TemplateBody = field("TemplateBody")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetGeneratedTemplateOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetGeneratedTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetStackPolicyOutput:
    boto3_raw_data: "type_defs.GetStackPolicyOutputTypeDef" = dataclasses.field()

    StackPolicyBody = field("StackPolicyBody")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetStackPolicyOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetStackPolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTemplateOutput:
    boto3_raw_data: "type_defs.GetTemplateOutputTypeDef" = dataclasses.field()

    TemplateBody = field("TemplateBody")
    StagesAvailable = field("StagesAvailable")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetTemplateOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportStacksToStackSetOutput:
    boto3_raw_data: "type_defs.ImportStacksToStackSetOutputTypeDef" = (
        dataclasses.field()
    )

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportStacksToStackSetOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportStacksToStackSetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportsOutput:
    boto3_raw_data: "type_defs.ListImportsOutputTypeDef" = dataclasses.field()

    Imports = field("Imports")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListImportsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTypeRegistrationsOutput:
    boto3_raw_data: "type_defs.ListTypeRegistrationsOutputTypeDef" = dataclasses.field()

    RegistrationTokenList = field("RegistrationTokenList")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTypeRegistrationsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTypeRegistrationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PublishTypeOutput:
    boto3_raw_data: "type_defs.PublishTypeOutputTypeDef" = dataclasses.field()

    PublicTypeArn = field("PublicTypeArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PublishTypeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PublishTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterPublisherOutput:
    boto3_raw_data: "type_defs.RegisterPublisherOutputTypeDef" = dataclasses.field()

    PublisherId = field("PublisherId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterPublisherOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterPublisherOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterTypeOutput:
    boto3_raw_data: "type_defs.RegisterTypeOutputTypeDef" = dataclasses.field()

    RegistrationToken = field("RegistrationToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterTypeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RollbackStackOutput:
    boto3_raw_data: "type_defs.RollbackStackOutputTypeDef" = dataclasses.field()

    StackId = field("StackId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RollbackStackOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RollbackStackOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SetTypeConfigurationOutput:
    boto3_raw_data: "type_defs.SetTypeConfigurationOutputTypeDef" = dataclasses.field()

    ConfigurationArn = field("ConfigurationArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SetTypeConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SetTypeConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartResourceScanOutput:
    boto3_raw_data: "type_defs.StartResourceScanOutputTypeDef" = dataclasses.field()

    ResourceScanId = field("ResourceScanId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartResourceScanOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartResourceScanOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestTypeOutput:
    boto3_raw_data: "type_defs.TestTypeOutputTypeDef" = dataclasses.field()

    TypeVersionArn = field("TypeVersionArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestTypeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TestTypeOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGeneratedTemplateOutput:
    boto3_raw_data: "type_defs.UpdateGeneratedTemplateOutputTypeDef" = (
        dataclasses.field()
    )

    GeneratedTemplateId = field("GeneratedTemplateId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateGeneratedTemplateOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGeneratedTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStackInstancesOutput:
    boto3_raw_data: "type_defs.UpdateStackInstancesOutputTypeDef" = dataclasses.field()

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateStackInstancesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStackInstancesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStackOutput:
    boto3_raw_data: "type_defs.UpdateStackOutputTypeDef" = dataclasses.field()

    StackId = field("StackId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateStackOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStackOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStackSetOutput:
    boto3_raw_data: "type_defs.UpdateStackSetOutputTypeDef" = dataclasses.field()

    OperationId = field("OperationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateStackSetOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStackSetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTerminationProtectionOutput:
    boto3_raw_data: "type_defs.UpdateTerminationProtectionOutputTypeDef" = (
        dataclasses.field()
    )

    StackId = field("StackId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateTerminationProtectionOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTerminationProtectionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDescribeTypeConfigurationsError:
    boto3_raw_data: "type_defs.BatchDescribeTypeConfigurationsErrorTypeDef" = (
        dataclasses.field()
    )

    ErrorCode = field("ErrorCode")
    ErrorMessage = field("ErrorMessage")

    @cached_property
    def TypeConfigurationIdentifier(self):  # pragma: no cover
        return TypeConfigurationIdentifier.make_one(
            self.boto3_raw_data["TypeConfigurationIdentifier"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDescribeTypeConfigurationsErrorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDescribeTypeConfigurationsErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDescribeTypeConfigurationsInput:
    boto3_raw_data: "type_defs.BatchDescribeTypeConfigurationsInputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def TypeConfigurationIdentifiers(self):  # pragma: no cover
        return TypeConfigurationIdentifier.make_many(
            self.boto3_raw_data["TypeConfigurationIdentifiers"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDescribeTypeConfigurationsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDescribeTypeConfigurationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeSetHookTargetDetails:
    boto3_raw_data: "type_defs.ChangeSetHookTargetDetailsTypeDef" = dataclasses.field()

    TargetType = field("TargetType")

    @cached_property
    def ResourceTargetDetails(self):  # pragma: no cover
        return ChangeSetHookResourceTargetDetails.make_one(
            self.boto3_raw_data["ResourceTargetDetails"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChangeSetHookTargetDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChangeSetHookTargetDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChangeSetsOutput:
    boto3_raw_data: "type_defs.ListChangeSetsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Summaries(self):  # pragma: no cover
        return ChangeSetSummary.make_many(self.boto3_raw_data["Summaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChangeSetsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChangeSetsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EstimateTemplateCostInput:
    boto3_raw_data: "type_defs.EstimateTemplateCostInputTypeDef" = dataclasses.field()

    TemplateBody = field("TemplateBody")
    TemplateURL = field("TemplateURL")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EstimateTemplateCostInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EstimateTemplateCostInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGeneratedTemplateInput:
    boto3_raw_data: "type_defs.CreateGeneratedTemplateInputTypeDef" = (
        dataclasses.field()
    )

    GeneratedTemplateName = field("GeneratedTemplateName")

    @cached_property
    def Resources(self):  # pragma: no cover
        return ResourceDefinition.make_many(self.boto3_raw_data["Resources"])

    StackName = field("StackName")

    @cached_property
    def TemplateConfiguration(self):  # pragma: no cover
        return TemplateConfiguration.make_one(
            self.boto3_raw_data["TemplateConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGeneratedTemplateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGeneratedTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateGeneratedTemplateInput:
    boto3_raw_data: "type_defs.UpdateGeneratedTemplateInputTypeDef" = (
        dataclasses.field()
    )

    GeneratedTemplateName = field("GeneratedTemplateName")
    NewGeneratedTemplateName = field("NewGeneratedTemplateName")

    @cached_property
    def AddResources(self):  # pragma: no cover
        return ResourceDefinition.make_many(self.boto3_raw_data["AddResources"])

    RemoveResources = field("RemoveResources")
    RefreshAllResources = field("RefreshAllResources")

    @cached_property
    def TemplateConfiguration(self):  # pragma: no cover
        return TemplateConfiguration.make_one(
            self.boto3_raw_data["TemplateConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateGeneratedTemplateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateGeneratedTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStackSetInput:
    boto3_raw_data: "type_defs.CreateStackSetInputTypeDef" = dataclasses.field()

    StackSetName = field("StackSetName")
    Description = field("Description")
    TemplateBody = field("TemplateBody")
    TemplateURL = field("TemplateURL")
    StackId = field("StackId")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    Capabilities = field("Capabilities")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    AdministrationRoleARN = field("AdministrationRoleARN")
    ExecutionRoleName = field("ExecutionRoleName")
    PermissionModel = field("PermissionModel")

    @cached_property
    def AutoDeployment(self):  # pragma: no cover
        return AutoDeployment.make_one(self.boto3_raw_data["AutoDeployment"])

    CallAs = field("CallAs")
    ClientRequestToken = field("ClientRequestToken")

    @cached_property
    def ManagedExecution(self):  # pragma: no cover
        return ManagedExecution.make_one(self.boto3_raw_data["ManagedExecution"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStackSetInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStackSetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackSetSummary:
    boto3_raw_data: "type_defs.StackSetSummaryTypeDef" = dataclasses.field()

    StackSetName = field("StackSetName")
    StackSetId = field("StackSetId")
    Description = field("Description")
    Status = field("Status")

    @cached_property
    def AutoDeployment(self):  # pragma: no cover
        return AutoDeployment.make_one(self.boto3_raw_data["AutoDeployment"])

    PermissionModel = field("PermissionModel")
    DriftStatus = field("DriftStatus")
    LastDriftCheckTimestamp = field("LastDriftCheckTimestamp")

    @cached_property
    def ManagedExecution(self):  # pragma: no cover
        return ManagedExecution.make_one(self.boto3_raw_data["ManagedExecution"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StackSetSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StackSetSummaryTypeDef"]],
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
class DescribeChangeSetInputPaginate:
    boto3_raw_data: "type_defs.DescribeChangeSetInputPaginateTypeDef" = (
        dataclasses.field()
    )

    ChangeSetName = field("ChangeSetName")
    StackName = field("StackName")
    IncludePropertyValues = field("IncludePropertyValues")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeChangeSetInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChangeSetInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStackEventsInputPaginate:
    boto3_raw_data: "type_defs.DescribeStackEventsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    StackName = field("StackName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeStackEventsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStackEventsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStacksInputPaginate:
    boto3_raw_data: "type_defs.DescribeStacksInputPaginateTypeDef" = dataclasses.field()

    StackName = field("StackName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStacksInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStacksInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListChangeSetsInputPaginate:
    boto3_raw_data: "type_defs.ListChangeSetsInputPaginateTypeDef" = dataclasses.field()

    StackName = field("StackName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListChangeSetsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListChangeSetsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExportsInputPaginate:
    boto3_raw_data: "type_defs.ListExportsInputPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExportsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExportsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGeneratedTemplatesInputPaginate:
    boto3_raw_data: "type_defs.ListGeneratedTemplatesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListGeneratedTemplatesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGeneratedTemplatesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListImportsInputPaginate:
    boto3_raw_data: "type_defs.ListImportsInputPaginateTypeDef" = dataclasses.field()

    ExportName = field("ExportName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListImportsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListImportsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceScanResourcesInputPaginate:
    boto3_raw_data: "type_defs.ListResourceScanResourcesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceScanId = field("ResourceScanId")
    ResourceIdentifier = field("ResourceIdentifier")
    ResourceTypePrefix = field("ResourceTypePrefix")
    TagKey = field("TagKey")
    TagValue = field("TagValue")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceScanResourcesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceScanResourcesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceScansInputPaginate:
    boto3_raw_data: "type_defs.ListResourceScansInputPaginateTypeDef" = (
        dataclasses.field()
    )

    ScanTypeFilter = field("ScanTypeFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResourceScansInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceScansInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackRefactorActionsInputPaginate:
    boto3_raw_data: "type_defs.ListStackRefactorActionsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    StackRefactorId = field("StackRefactorId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStackRefactorActionsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackRefactorActionsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackRefactorsInputPaginate:
    boto3_raw_data: "type_defs.ListStackRefactorsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    ExecutionStatusFilter = field("ExecutionStatusFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListStackRefactorsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackRefactorsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackResourcesInputPaginate:
    boto3_raw_data: "type_defs.ListStackResourcesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    StackName = field("StackName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListStackResourcesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackResourcesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackSetOperationsInputPaginate:
    boto3_raw_data: "type_defs.ListStackSetOperationsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    StackSetName = field("StackSetName")
    CallAs = field("CallAs")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStackSetOperationsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackSetOperationsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackSetsInputPaginate:
    boto3_raw_data: "type_defs.ListStackSetsInputPaginateTypeDef" = dataclasses.field()

    Status = field("Status")
    CallAs = field("CallAs")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStackSetsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackSetsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStacksInputPaginate:
    boto3_raw_data: "type_defs.ListStacksInputPaginateTypeDef" = dataclasses.field()

    StackStatusFilter = field("StackStatusFilter")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStacksInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStacksInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChangeSetInputWait:
    boto3_raw_data: "type_defs.DescribeChangeSetInputWaitTypeDef" = dataclasses.field()

    ChangeSetName = field("ChangeSetName")
    StackName = field("StackName")
    NextToken = field("NextToken")
    IncludePropertyValues = field("IncludePropertyValues")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeChangeSetInputWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChangeSetInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStackRefactorInputWaitExtra:
    boto3_raw_data: "type_defs.DescribeStackRefactorInputWaitExtraTypeDef" = (
        dataclasses.field()
    )

    StackRefactorId = field("StackRefactorId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeStackRefactorInputWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStackRefactorInputWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStackRefactorInputWait:
    boto3_raw_data: "type_defs.DescribeStackRefactorInputWaitTypeDef" = (
        dataclasses.field()
    )

    StackRefactorId = field("StackRefactorId")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeStackRefactorInputWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStackRefactorInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStacksInputWaitExtraExtraExtraExtraExtra:
    boto3_raw_data: (
        "type_defs.DescribeStacksInputWaitExtraExtraExtraExtraExtraTypeDef"
    ) = dataclasses.field()

    StackName = field("StackName")
    NextToken = field("NextToken")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeStacksInputWaitExtraExtraExtraExtraExtraTypeDef"
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
                "type_defs.DescribeStacksInputWaitExtraExtraExtraExtraExtraTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStacksInputWaitExtraExtraExtraExtra:
    boto3_raw_data: "type_defs.DescribeStacksInputWaitExtraExtraExtraExtraTypeDef" = (
        dataclasses.field()
    )

    StackName = field("StackName")
    NextToken = field("NextToken")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeStacksInputWaitExtraExtraExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStacksInputWaitExtraExtraExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStacksInputWaitExtraExtraExtra:
    boto3_raw_data: "type_defs.DescribeStacksInputWaitExtraExtraExtraTypeDef" = (
        dataclasses.field()
    )

    StackName = field("StackName")
    NextToken = field("NextToken")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeStacksInputWaitExtraExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStacksInputWaitExtraExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStacksInputWaitExtraExtra:
    boto3_raw_data: "type_defs.DescribeStacksInputWaitExtraExtraTypeDef" = (
        dataclasses.field()
    )

    StackName = field("StackName")
    NextToken = field("NextToken")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeStacksInputWaitExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStacksInputWaitExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStacksInputWaitExtra:
    boto3_raw_data: "type_defs.DescribeStacksInputWaitExtraTypeDef" = (
        dataclasses.field()
    )

    StackName = field("StackName")
    NextToken = field("NextToken")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStacksInputWaitExtraTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStacksInputWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStacksInputWait:
    boto3_raw_data: "type_defs.DescribeStacksInputWaitTypeDef" = dataclasses.field()

    StackName = field("StackName")
    NextToken = field("NextToken")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStacksInputWaitTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStacksInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTypeRegistrationInputWait:
    boto3_raw_data: "type_defs.DescribeTypeRegistrationInputWaitTypeDef" = (
        dataclasses.field()
    )

    RegistrationToken = field("RegistrationToken")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeTypeRegistrationInputWaitTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTypeRegistrationInputWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourceScanOutput:
    boto3_raw_data: "type_defs.DescribeResourceScanOutputTypeDef" = dataclasses.field()

    ResourceScanId = field("ResourceScanId")
    Status = field("Status")
    StatusReason = field("StatusReason")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    PercentageCompleted = field("PercentageCompleted")
    ResourceTypes = field("ResourceTypes")
    ResourcesScanned = field("ResourcesScanned")
    ResourcesRead = field("ResourcesRead")

    @cached_property
    def ScanFilters(self):  # pragma: no cover
        return ScanFilterOutput.make_many(self.boto3_raw_data["ScanFilters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeResourceScanOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourceScanOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStackEventsOutput:
    boto3_raw_data: "type_defs.DescribeStackEventsOutputTypeDef" = dataclasses.field()

    @cached_property
    def StackEvents(self):  # pragma: no cover
        return StackEvent.make_many(self.boto3_raw_data["StackEvents"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStackEventsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStackEventsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeTypeOutput:
    boto3_raw_data: "type_defs.DescribeTypeOutputTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Type = field("Type")
    TypeName = field("TypeName")
    DefaultVersionId = field("DefaultVersionId")
    IsDefaultVersion = field("IsDefaultVersion")
    TypeTestsStatus = field("TypeTestsStatus")
    TypeTestsStatusDescription = field("TypeTestsStatusDescription")
    Description = field("Description")
    Schema = field("Schema")
    ProvisioningType = field("ProvisioningType")
    DeprecatedStatus = field("DeprecatedStatus")

    @cached_property
    def LoggingConfig(self):  # pragma: no cover
        return LoggingConfig.make_one(self.boto3_raw_data["LoggingConfig"])

    @cached_property
    def RequiredActivatedTypes(self):  # pragma: no cover
        return RequiredActivatedType.make_many(
            self.boto3_raw_data["RequiredActivatedTypes"]
        )

    ExecutionRoleArn = field("ExecutionRoleArn")
    Visibility = field("Visibility")
    SourceUrl = field("SourceUrl")
    DocumentationUrl = field("DocumentationUrl")
    LastUpdated = field("LastUpdated")
    TimeCreated = field("TimeCreated")
    ConfigurationSchema = field("ConfigurationSchema")
    PublisherId = field("PublisherId")
    OriginalTypeName = field("OriginalTypeName")
    OriginalTypeArn = field("OriginalTypeArn")
    PublicVersionNumber = field("PublicVersionNumber")
    LatestPublicVersion = field("LatestPublicVersion")
    IsActivated = field("IsActivated")
    AutoUpdate = field("AutoUpdate")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeTypeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExportsOutput:
    boto3_raw_data: "type_defs.ListExportsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Exports(self):  # pragma: no cover
        return Export.make_many(self.boto3_raw_data["Exports"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListExportsOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExportsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTemplateSummaryInput:
    boto3_raw_data: "type_defs.GetTemplateSummaryInputTypeDef" = dataclasses.field()

    TemplateBody = field("TemplateBody")
    TemplateURL = field("TemplateURL")
    StackName = field("StackName")
    StackSetName = field("StackSetName")
    CallAs = field("CallAs")

    @cached_property
    def TemplateSummaryConfig(self):  # pragma: no cover
        return TemplateSummaryConfig.make_one(
            self.boto3_raw_data["TemplateSummaryConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTemplateSummaryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTemplateSummaryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListHookResultsOutput:
    boto3_raw_data: "type_defs.ListHookResultsOutputTypeDef" = dataclasses.field()

    TargetType = field("TargetType")
    TargetId = field("TargetId")

    @cached_property
    def HookResults(self):  # pragma: no cover
        return HookResultSummary.make_many(self.boto3_raw_data["HookResults"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListHookResultsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListHookResultsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGeneratedTemplatesOutput:
    boto3_raw_data: "type_defs.ListGeneratedTemplatesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Summaries(self):  # pragma: no cover
        return TemplateSummary.make_many(self.boto3_raw_data["Summaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGeneratedTemplatesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGeneratedTemplatesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceScanRelatedResourcesInputPaginate:
    boto3_raw_data: "type_defs.ListResourceScanRelatedResourcesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    ResourceScanId = field("ResourceScanId")

    @cached_property
    def Resources(self):  # pragma: no cover
        return ScannedResourceIdentifier.make_many(self.boto3_raw_data["Resources"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceScanRelatedResourcesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceScanRelatedResourcesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceScanRelatedResourcesInput:
    boto3_raw_data: "type_defs.ListResourceScanRelatedResourcesInputTypeDef" = (
        dataclasses.field()
    )

    ResourceScanId = field("ResourceScanId")

    @cached_property
    def Resources(self):  # pragma: no cover
        return ScannedResourceIdentifier.make_many(self.boto3_raw_data["Resources"])

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceScanRelatedResourcesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceScanRelatedResourcesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceScanRelatedResourcesOutput:
    boto3_raw_data: "type_defs.ListResourceScanRelatedResourcesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def RelatedResources(self):  # pragma: no cover
        return ScannedResource.make_many(self.boto3_raw_data["RelatedResources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListResourceScanRelatedResourcesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceScanRelatedResourcesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceScanResourcesOutput:
    boto3_raw_data: "type_defs.ListResourceScanResourcesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Resources(self):  # pragma: no cover
        return ScannedResource.make_many(self.boto3_raw_data["Resources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListResourceScanResourcesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceScanResourcesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListResourceScansOutput:
    boto3_raw_data: "type_defs.ListResourceScansOutputTypeDef" = dataclasses.field()

    @cached_property
    def ResourceScanSummaries(self):  # pragma: no cover
        return ResourceScanSummary.make_many(
            self.boto3_raw_data["ResourceScanSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListResourceScansOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListResourceScansOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackInstancesInputPaginate:
    boto3_raw_data: "type_defs.ListStackInstancesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    StackSetName = field("StackSetName")

    @cached_property
    def Filters(self):  # pragma: no cover
        return StackInstanceFilter.make_many(self.boto3_raw_data["Filters"])

    StackInstanceAccount = field("StackInstanceAccount")
    StackInstanceRegion = field("StackInstanceRegion")
    CallAs = field("CallAs")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListStackInstancesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackInstancesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackInstancesInput:
    boto3_raw_data: "type_defs.ListStackInstancesInputTypeDef" = dataclasses.field()

    StackSetName = field("StackSetName")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def Filters(self):  # pragma: no cover
        return StackInstanceFilter.make_many(self.boto3_raw_data["Filters"])

    StackInstanceAccount = field("StackInstanceAccount")
    StackInstanceRegion = field("StackInstanceRegion")
    CallAs = field("CallAs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStackInstancesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackInstancesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackRefactorsOutput:
    boto3_raw_data: "type_defs.ListStackRefactorsOutputTypeDef" = dataclasses.field()

    @cached_property
    def StackRefactorSummaries(self):  # pragma: no cover
        return StackRefactorSummary.make_many(
            self.boto3_raw_data["StackRefactorSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStackRefactorsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackRefactorsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackSetAutoDeploymentTargetsOutput:
    boto3_raw_data: "type_defs.ListStackSetAutoDeploymentTargetsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Summaries(self):  # pragma: no cover
        return StackSetAutoDeploymentTargetSummary.make_many(
            self.boto3_raw_data["Summaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStackSetAutoDeploymentTargetsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackSetAutoDeploymentTargetsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackSetOperationResultsInputPaginate:
    boto3_raw_data: "type_defs.ListStackSetOperationResultsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    StackSetName = field("StackSetName")
    OperationId = field("OperationId")
    CallAs = field("CallAs")

    @cached_property
    def Filters(self):  # pragma: no cover
        return OperationResultFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStackSetOperationResultsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackSetOperationResultsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackSetOperationResultsInput:
    boto3_raw_data: "type_defs.ListStackSetOperationResultsInputTypeDef" = (
        dataclasses.field()
    )

    StackSetName = field("StackSetName")
    OperationId = field("OperationId")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")
    CallAs = field("CallAs")

    @cached_property
    def Filters(self):  # pragma: no cover
        return OperationResultFilter.make_many(self.boto3_raw_data["Filters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStackSetOperationResultsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackSetOperationResultsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTypeVersionsOutput:
    boto3_raw_data: "type_defs.ListTypeVersionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def TypeVersionSummaries(self):  # pragma: no cover
        return TypeVersionSummary.make_many(self.boto3_raw_data["TypeVersionSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTypeVersionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTypeVersionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTypesInputPaginate:
    boto3_raw_data: "type_defs.ListTypesInputPaginateTypeDef" = dataclasses.field()

    Visibility = field("Visibility")
    ProvisioningType = field("ProvisioningType")
    DeprecatedStatus = field("DeprecatedStatus")
    Type = field("Type")

    @cached_property
    def Filters(self):  # pragma: no cover
        return TypeFilters.make_one(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTypesInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTypesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTypesInput:
    boto3_raw_data: "type_defs.ListTypesInputTypeDef" = dataclasses.field()

    Visibility = field("Visibility")
    ProvisioningType = field("ProvisioningType")
    DeprecatedStatus = field("DeprecatedStatus")
    Type = field("Type")

    @cached_property
    def Filters(self):  # pragma: no cover
        return TypeFilters.make_one(self.boto3_raw_data["Filters"])

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTypesInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListTypesInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTypesOutput:
    boto3_raw_data: "type_defs.ListTypesOutputTypeDef" = dataclasses.field()

    @cached_property
    def TypeSummaries(self):  # pragma: no cover
        return TypeSummary.make_many(self.boto3_raw_data["TypeSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListTypesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListTypesOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParameterDeclaration:
    boto3_raw_data: "type_defs.ParameterDeclarationTypeDef" = dataclasses.field()

    ParameterKey = field("ParameterKey")
    DefaultValue = field("DefaultValue")
    ParameterType = field("ParameterType")
    NoEcho = field("NoEcho")
    Description = field("Description")

    @cached_property
    def ParameterConstraints(self):  # pragma: no cover
        return ParameterConstraints.make_one(
            self.boto3_raw_data["ParameterConstraints"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ParameterDeclarationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ParameterDeclarationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackInstanceResourceDriftsSummary:
    boto3_raw_data: "type_defs.StackInstanceResourceDriftsSummaryTypeDef" = (
        dataclasses.field()
    )

    StackId = field("StackId")
    LogicalResourceId = field("LogicalResourceId")
    ResourceType = field("ResourceType")
    StackResourceDriftStatus = field("StackResourceDriftStatus")
    Timestamp = field("Timestamp")
    PhysicalResourceId = field("PhysicalResourceId")

    @cached_property
    def PhysicalResourceIdContext(self):  # pragma: no cover
        return PhysicalResourceIdContextKeyValuePair.make_many(
            self.boto3_raw_data["PhysicalResourceIdContext"]
        )

    @cached_property
    def PropertyDifferences(self):  # pragma: no cover
        return PropertyDifference.make_many(self.boto3_raw_data["PropertyDifferences"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StackInstanceResourceDriftsSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StackInstanceResourceDriftsSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackResourceDrift:
    boto3_raw_data: "type_defs.StackResourceDriftTypeDef" = dataclasses.field()

    StackId = field("StackId")
    LogicalResourceId = field("LogicalResourceId")
    ResourceType = field("ResourceType")
    StackResourceDriftStatus = field("StackResourceDriftStatus")
    Timestamp = field("Timestamp")
    PhysicalResourceId = field("PhysicalResourceId")

    @cached_property
    def PhysicalResourceIdContext(self):  # pragma: no cover
        return PhysicalResourceIdContextKeyValuePair.make_many(
            self.boto3_raw_data["PhysicalResourceIdContext"]
        )

    ExpectedProperties = field("ExpectedProperties")
    ActualProperties = field("ActualProperties")

    @cached_property
    def PropertyDifferences(self):  # pragma: no cover
        return PropertyDifference.make_many(self.boto3_raw_data["PropertyDifferences"])

    @cached_property
    def ModuleInfo(self):  # pragma: no cover
        return ModuleInfo.make_one(self.boto3_raw_data["ModuleInfo"])

    DriftStatusReason = field("DriftStatusReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StackResourceDriftTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StackResourceDriftTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceChangeDetail:
    boto3_raw_data: "type_defs.ResourceChangeDetailTypeDef" = dataclasses.field()

    @cached_property
    def Target(self):  # pragma: no cover
        return ResourceTargetDefinition.make_one(self.boto3_raw_data["Target"])

    Evaluation = field("Evaluation")
    ChangeSource = field("ChangeSource")
    CausingEntity = field("CausingEntity")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceChangeDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceChangeDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceMapping:
    boto3_raw_data: "type_defs.ResourceMappingTypeDef" = dataclasses.field()

    @cached_property
    def Source(self):  # pragma: no cover
        return ResourceLocation.make_one(self.boto3_raw_data["Source"])

    @cached_property
    def Destination(self):  # pragma: no cover
        return ResourceLocation.make_one(self.boto3_raw_data["Destination"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceMappingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RollbackConfigurationOutput:
    boto3_raw_data: "type_defs.RollbackConfigurationOutputTypeDef" = dataclasses.field()

    @cached_property
    def RollbackTriggers(self):  # pragma: no cover
        return RollbackTrigger.make_many(self.boto3_raw_data["RollbackTriggers"])

    MonitoringTimeInMinutes = field("MonitoringTimeInMinutes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RollbackConfigurationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RollbackConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RollbackConfiguration:
    boto3_raw_data: "type_defs.RollbackConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def RollbackTriggers(self):  # pragma: no cover
        return RollbackTrigger.make_many(self.boto3_raw_data["RollbackTriggers"])

    MonitoringTimeInMinutes = field("MonitoringTimeInMinutes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RollbackConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RollbackConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackSummary:
    boto3_raw_data: "type_defs.StackSummaryTypeDef" = dataclasses.field()

    StackName = field("StackName")
    CreationTime = field("CreationTime")
    StackStatus = field("StackStatus")
    StackId = field("StackId")
    TemplateDescription = field("TemplateDescription")
    LastUpdatedTime = field("LastUpdatedTime")
    DeletionTime = field("DeletionTime")
    StackStatusReason = field("StackStatusReason")
    ParentId = field("ParentId")
    RootId = field("RootId")

    @cached_property
    def DriftInformation(self):  # pragma: no cover
        return StackDriftInformationSummary.make_one(
            self.boto3_raw_data["DriftInformation"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StackSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StackSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackInstanceSummary:
    boto3_raw_data: "type_defs.StackInstanceSummaryTypeDef" = dataclasses.field()

    StackSetId = field("StackSetId")
    Region = field("Region")
    Account = field("Account")
    StackId = field("StackId")
    Status = field("Status")
    StatusReason = field("StatusReason")

    @cached_property
    def StackInstanceStatus(self):  # pragma: no cover
        return StackInstanceComprehensiveStatus.make_one(
            self.boto3_raw_data["StackInstanceStatus"]
        )

    OrganizationalUnitId = field("OrganizationalUnitId")
    DriftStatus = field("DriftStatus")
    LastDriftCheckTimestamp = field("LastDriftCheckTimestamp")
    LastOperationId = field("LastOperationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StackInstanceSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StackInstanceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackInstance:
    boto3_raw_data: "type_defs.StackInstanceTypeDef" = dataclasses.field()

    StackSetId = field("StackSetId")
    Region = field("Region")
    Account = field("Account")
    StackId = field("StackId")

    @cached_property
    def ParameterOverrides(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["ParameterOverrides"])

    Status = field("Status")

    @cached_property
    def StackInstanceStatus(self):  # pragma: no cover
        return StackInstanceComprehensiveStatus.make_one(
            self.boto3_raw_data["StackInstanceStatus"]
        )

    StatusReason = field("StatusReason")
    OrganizationalUnitId = field("OrganizationalUnitId")
    DriftStatus = field("DriftStatus")
    LastDriftCheckTimestamp = field("LastDriftCheckTimestamp")
    LastOperationId = field("LastOperationId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StackInstanceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StackInstanceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackResourceDetail:
    boto3_raw_data: "type_defs.StackResourceDetailTypeDef" = dataclasses.field()

    LogicalResourceId = field("LogicalResourceId")
    ResourceType = field("ResourceType")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    ResourceStatus = field("ResourceStatus")
    StackName = field("StackName")
    StackId = field("StackId")
    PhysicalResourceId = field("PhysicalResourceId")
    ResourceStatusReason = field("ResourceStatusReason")
    Description = field("Description")
    Metadata = field("Metadata")

    @cached_property
    def DriftInformation(self):  # pragma: no cover
        return StackResourceDriftInformation.make_one(
            self.boto3_raw_data["DriftInformation"]
        )

    @cached_property
    def ModuleInfo(self):  # pragma: no cover
        return ModuleInfo.make_one(self.boto3_raw_data["ModuleInfo"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StackResourceDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StackResourceDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackResource:
    boto3_raw_data: "type_defs.StackResourceTypeDef" = dataclasses.field()

    LogicalResourceId = field("LogicalResourceId")
    ResourceType = field("ResourceType")
    Timestamp = field("Timestamp")
    ResourceStatus = field("ResourceStatus")
    StackName = field("StackName")
    StackId = field("StackId")
    PhysicalResourceId = field("PhysicalResourceId")
    ResourceStatusReason = field("ResourceStatusReason")
    Description = field("Description")

    @cached_property
    def DriftInformation(self):  # pragma: no cover
        return StackResourceDriftInformation.make_one(
            self.boto3_raw_data["DriftInformation"]
        )

    @cached_property
    def ModuleInfo(self):  # pragma: no cover
        return ModuleInfo.make_one(self.boto3_raw_data["ModuleInfo"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StackResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StackResourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackResourceSummary:
    boto3_raw_data: "type_defs.StackResourceSummaryTypeDef" = dataclasses.field()

    LogicalResourceId = field("LogicalResourceId")
    ResourceType = field("ResourceType")
    LastUpdatedTimestamp = field("LastUpdatedTimestamp")
    ResourceStatus = field("ResourceStatus")
    PhysicalResourceId = field("PhysicalResourceId")
    ResourceStatusReason = field("ResourceStatusReason")

    @cached_property
    def DriftInformation(self):  # pragma: no cover
        return StackResourceDriftInformationSummary.make_one(
            self.boto3_raw_data["DriftInformation"]
        )

    @cached_property
    def ModuleInfo(self):  # pragma: no cover
        return ModuleInfo.make_one(self.boto3_raw_data["ModuleInfo"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StackResourceSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StackResourceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackSet:
    boto3_raw_data: "type_defs.StackSetTypeDef" = dataclasses.field()

    StackSetName = field("StackSetName")
    StackSetId = field("StackSetId")
    Description = field("Description")
    Status = field("Status")
    TemplateBody = field("TemplateBody")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    Capabilities = field("Capabilities")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    StackSetARN = field("StackSetARN")
    AdministrationRoleARN = field("AdministrationRoleARN")
    ExecutionRoleName = field("ExecutionRoleName")

    @cached_property
    def StackSetDriftDetectionDetails(self):  # pragma: no cover
        return StackSetDriftDetectionDetails.make_one(
            self.boto3_raw_data["StackSetDriftDetectionDetails"]
        )

    @cached_property
    def AutoDeployment(self):  # pragma: no cover
        return AutoDeployment.make_one(self.boto3_raw_data["AutoDeployment"])

    PermissionModel = field("PermissionModel")
    OrganizationalUnitIds = field("OrganizationalUnitIds")

    @cached_property
    def ManagedExecution(self):  # pragma: no cover
        return ManagedExecution.make_one(self.boto3_raw_data["ManagedExecution"])

    Regions = field("Regions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StackSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StackSetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackSetOperationSummary:
    boto3_raw_data: "type_defs.StackSetOperationSummaryTypeDef" = dataclasses.field()

    OperationId = field("OperationId")
    Action = field("Action")
    Status = field("Status")
    CreationTimestamp = field("CreationTimestamp")
    EndTimestamp = field("EndTimestamp")
    StatusReason = field("StatusReason")

    @cached_property
    def StatusDetails(self):  # pragma: no cover
        return StackSetOperationStatusDetails.make_one(
            self.boto3_raw_data["StatusDetails"]
        )

    @cached_property
    def OperationPreferences(self):  # pragma: no cover
        return StackSetOperationPreferencesOutput.make_one(
            self.boto3_raw_data["OperationPreferences"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StackSetOperationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StackSetOperationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackSetOperation:
    boto3_raw_data: "type_defs.StackSetOperationTypeDef" = dataclasses.field()

    OperationId = field("OperationId")
    StackSetId = field("StackSetId")
    Action = field("Action")
    Status = field("Status")

    @cached_property
    def OperationPreferences(self):  # pragma: no cover
        return StackSetOperationPreferencesOutput.make_one(
            self.boto3_raw_data["OperationPreferences"]
        )

    RetainStacks = field("RetainStacks")
    AdministrationRoleARN = field("AdministrationRoleARN")
    ExecutionRoleName = field("ExecutionRoleName")
    CreationTimestamp = field("CreationTimestamp")
    EndTimestamp = field("EndTimestamp")

    @cached_property
    def DeploymentTargets(self):  # pragma: no cover
        return DeploymentTargetsOutput.make_one(
            self.boto3_raw_data["DeploymentTargets"]
        )

    @cached_property
    def StackSetDriftDetectionDetails(self):  # pragma: no cover
        return StackSetDriftDetectionDetails.make_one(
            self.boto3_raw_data["StackSetDriftDetectionDetails"]
        )

    StatusReason = field("StatusReason")

    @cached_property
    def StatusDetails(self):  # pragma: no cover
        return StackSetOperationStatusDetails.make_one(
            self.boto3_raw_data["StatusDetails"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StackSetOperationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StackSetOperationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidateTemplateOutput:
    boto3_raw_data: "type_defs.ValidateTemplateOutputTypeDef" = dataclasses.field()

    @cached_property
    def Parameters(self):  # pragma: no cover
        return TemplateParameter.make_many(self.boto3_raw_data["Parameters"])

    Description = field("Description")
    Capabilities = field("Capabilities")
    CapabilitiesReason = field("CapabilitiesReason")
    DeclaredTransforms = field("DeclaredTransforms")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ValidateTemplateOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidateTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WarningDetail:
    boto3_raw_data: "type_defs.WarningDetailTypeDef" = dataclasses.field()

    Type = field("Type")

    @cached_property
    def Properties(self):  # pragma: no cover
        return WarningProperty.make_many(self.boto3_raw_data["Properties"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.WarningDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.WarningDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackSetOperationResultsOutput:
    boto3_raw_data: "type_defs.ListStackSetOperationResultsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Summaries(self):  # pragma: no cover
        return StackSetOperationResultSummary.make_many(
            self.boto3_raw_data["Summaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStackSetOperationResultsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackSetOperationResultsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDescribeTypeConfigurationsOutput:
    boto3_raw_data: "type_defs.BatchDescribeTypeConfigurationsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Errors(self):  # pragma: no cover
        return BatchDescribeTypeConfigurationsError.make_many(
            self.boto3_raw_data["Errors"]
        )

    @cached_property
    def UnprocessedTypeConfigurations(self):  # pragma: no cover
        return TypeConfigurationIdentifier.make_many(
            self.boto3_raw_data["UnprocessedTypeConfigurations"]
        )

    @cached_property
    def TypeConfigurations(self):  # pragma: no cover
        return TypeConfigurationDetails.make_many(
            self.boto3_raw_data["TypeConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDescribeTypeConfigurationsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDescribeTypeConfigurationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeSetHook:
    boto3_raw_data: "type_defs.ChangeSetHookTypeDef" = dataclasses.field()

    InvocationPoint = field("InvocationPoint")
    FailureMode = field("FailureMode")
    TypeName = field("TypeName")
    TypeVersionId = field("TypeVersionId")
    TypeConfigurationVersionId = field("TypeConfigurationVersionId")

    @cached_property
    def TargetDetails(self):  # pragma: no cover
        return ChangeSetHookTargetDetails.make_one(self.boto3_raw_data["TargetDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChangeSetHookTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChangeSetHookTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackSetsOutput:
    boto3_raw_data: "type_defs.ListStackSetsOutputTypeDef" = dataclasses.field()

    @cached_property
    def Summaries(self):  # pragma: no cover
        return StackSetSummary.make_many(self.boto3_raw_data["Summaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStackSetsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackSetsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTemplateSummaryOutput:
    boto3_raw_data: "type_defs.GetTemplateSummaryOutputTypeDef" = dataclasses.field()

    @cached_property
    def Parameters(self):  # pragma: no cover
        return ParameterDeclaration.make_many(self.boto3_raw_data["Parameters"])

    Description = field("Description")
    Capabilities = field("Capabilities")
    CapabilitiesReason = field("CapabilitiesReason")
    ResourceTypes = field("ResourceTypes")
    Version = field("Version")
    Metadata = field("Metadata")
    DeclaredTransforms = field("DeclaredTransforms")

    @cached_property
    def ResourceIdentifierSummaries(self):  # pragma: no cover
        return ResourceIdentifierSummary.make_many(
            self.boto3_raw_data["ResourceIdentifierSummaries"]
        )

    @cached_property
    def Warnings(self):  # pragma: no cover
        return Warnings.make_one(self.boto3_raw_data["Warnings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTemplateSummaryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTemplateSummaryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackInstanceResourceDriftsOutput:
    boto3_raw_data: "type_defs.ListStackInstanceResourceDriftsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Summaries(self):  # pragma: no cover
        return StackInstanceResourceDriftsSummary.make_many(
            self.boto3_raw_data["Summaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListStackInstanceResourceDriftsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackInstanceResourceDriftsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStackResourceDriftsOutput:
    boto3_raw_data: "type_defs.DescribeStackResourceDriftsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StackResourceDrifts(self):  # pragma: no cover
        return StackResourceDrift.make_many(self.boto3_raw_data["StackResourceDrifts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeStackResourceDriftsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStackResourceDriftsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectStackResourceDriftOutput:
    boto3_raw_data: "type_defs.DetectStackResourceDriftOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StackResourceDrift(self):  # pragma: no cover
        return StackResourceDrift.make_one(self.boto3_raw_data["StackResourceDrift"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DetectStackResourceDriftOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectStackResourceDriftOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceChange:
    boto3_raw_data: "type_defs.ResourceChangeTypeDef" = dataclasses.field()

    PolicyAction = field("PolicyAction")
    Action = field("Action")
    LogicalResourceId = field("LogicalResourceId")
    PhysicalResourceId = field("PhysicalResourceId")
    ResourceType = field("ResourceType")
    Replacement = field("Replacement")
    Scope = field("Scope")

    @cached_property
    def Details(self):  # pragma: no cover
        return ResourceChangeDetail.make_many(self.boto3_raw_data["Details"])

    ChangeSetId = field("ChangeSetId")

    @cached_property
    def ModuleInfo(self):  # pragma: no cover
        return ModuleInfo.make_one(self.boto3_raw_data["ModuleInfo"])

    BeforeContext = field("BeforeContext")
    AfterContext = field("AfterContext")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceChangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceChangeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStackRefactorInput:
    boto3_raw_data: "type_defs.CreateStackRefactorInputTypeDef" = dataclasses.field()

    @cached_property
    def StackDefinitions(self):  # pragma: no cover
        return StackDefinition.make_many(self.boto3_raw_data["StackDefinitions"])

    Description = field("Description")
    EnableStackCreation = field("EnableStackCreation")

    @cached_property
    def ResourceMappings(self):  # pragma: no cover
        return ResourceMapping.make_many(self.boto3_raw_data["ResourceMappings"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStackRefactorInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStackRefactorInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StackRefactorAction:
    boto3_raw_data: "type_defs.StackRefactorActionTypeDef" = dataclasses.field()

    Action = field("Action")
    Entity = field("Entity")
    PhysicalResourceId = field("PhysicalResourceId")
    ResourceIdentifier = field("ResourceIdentifier")
    Description = field("Description")
    Detection = field("Detection")
    DetectionReason = field("DetectionReason")

    @cached_property
    def TagResources(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagResources"])

    UntagResources = field("UntagResources")

    @cached_property
    def ResourceMapping(self):  # pragma: no cover
        return ResourceMapping.make_one(self.boto3_raw_data["ResourceMapping"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StackRefactorActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StackRefactorActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Stack:
    boto3_raw_data: "type_defs.StackTypeDef" = dataclasses.field()

    StackName = field("StackName")
    CreationTime = field("CreationTime")
    StackStatus = field("StackStatus")
    StackId = field("StackId")
    ChangeSetId = field("ChangeSetId")
    Description = field("Description")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    DeletionTime = field("DeletionTime")
    LastUpdatedTime = field("LastUpdatedTime")

    @cached_property
    def RollbackConfiguration(self):  # pragma: no cover
        return RollbackConfigurationOutput.make_one(
            self.boto3_raw_data["RollbackConfiguration"]
        )

    StackStatusReason = field("StackStatusReason")
    DisableRollback = field("DisableRollback")
    NotificationARNs = field("NotificationARNs")
    TimeoutInMinutes = field("TimeoutInMinutes")
    Capabilities = field("Capabilities")

    @cached_property
    def Outputs(self):  # pragma: no cover
        return Output.make_many(self.boto3_raw_data["Outputs"])

    RoleARN = field("RoleARN")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    EnableTerminationProtection = field("EnableTerminationProtection")
    ParentId = field("ParentId")
    RootId = field("RootId")

    @cached_property
    def DriftInformation(self):  # pragma: no cover
        return StackDriftInformation.make_one(self.boto3_raw_data["DriftInformation"])

    RetainExceptOnCreate = field("RetainExceptOnCreate")
    DeletionMode = field("DeletionMode")
    DetailedStatus = field("DetailedStatus")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StackTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StackTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartResourceScanInput:
    boto3_raw_data: "type_defs.StartResourceScanInputTypeDef" = dataclasses.field()

    ClientRequestToken = field("ClientRequestToken")
    ScanFilters = field("ScanFilters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartResourceScanInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartResourceScanInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStacksOutput:
    boto3_raw_data: "type_defs.ListStacksOutputTypeDef" = dataclasses.field()

    @cached_property
    def StackSummaries(self):  # pragma: no cover
        return StackSummary.make_many(self.boto3_raw_data["StackSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListStacksOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStacksOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackInstancesOutput:
    boto3_raw_data: "type_defs.ListStackInstancesOutputTypeDef" = dataclasses.field()

    @cached_property
    def Summaries(self):  # pragma: no cover
        return StackInstanceSummary.make_many(self.boto3_raw_data["Summaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStackInstancesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackInstancesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStackInstanceOutput:
    boto3_raw_data: "type_defs.DescribeStackInstanceOutputTypeDef" = dataclasses.field()

    @cached_property
    def StackInstance(self):  # pragma: no cover
        return StackInstance.make_one(self.boto3_raw_data["StackInstance"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStackInstanceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStackInstanceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStackResourceOutput:
    boto3_raw_data: "type_defs.DescribeStackResourceOutputTypeDef" = dataclasses.field()

    @cached_property
    def StackResourceDetail(self):  # pragma: no cover
        return StackResourceDetail.make_one(self.boto3_raw_data["StackResourceDetail"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStackResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStackResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStackResourcesOutput:
    boto3_raw_data: "type_defs.DescribeStackResourcesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StackResources(self):  # pragma: no cover
        return StackResource.make_many(self.boto3_raw_data["StackResources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStackResourcesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStackResourcesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackResourcesOutput:
    boto3_raw_data: "type_defs.ListStackResourcesOutputTypeDef" = dataclasses.field()

    @cached_property
    def StackResourceSummaries(self):  # pragma: no cover
        return StackResourceSummary.make_many(
            self.boto3_raw_data["StackResourceSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStackResourcesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackResourcesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStackSetOutput:
    boto3_raw_data: "type_defs.DescribeStackSetOutputTypeDef" = dataclasses.field()

    @cached_property
    def StackSet(self):  # pragma: no cover
        return StackSet.make_one(self.boto3_raw_data["StackSet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStackSetOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStackSetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStackInstancesInput:
    boto3_raw_data: "type_defs.CreateStackInstancesInputTypeDef" = dataclasses.field()

    StackSetName = field("StackSetName")
    Regions = field("Regions")
    Accounts = field("Accounts")
    DeploymentTargets = field("DeploymentTargets")

    @cached_property
    def ParameterOverrides(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["ParameterOverrides"])

    OperationPreferences = field("OperationPreferences")
    OperationId = field("OperationId")
    CallAs = field("CallAs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateStackInstancesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStackInstancesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteStackInstancesInput:
    boto3_raw_data: "type_defs.DeleteStackInstancesInputTypeDef" = dataclasses.field()

    StackSetName = field("StackSetName")
    Regions = field("Regions")
    RetainStacks = field("RetainStacks")
    Accounts = field("Accounts")
    DeploymentTargets = field("DeploymentTargets")
    OperationPreferences = field("OperationPreferences")
    OperationId = field("OperationId")
    CallAs = field("CallAs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteStackInstancesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteStackInstancesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DetectStackSetDriftInput:
    boto3_raw_data: "type_defs.DetectStackSetDriftInputTypeDef" = dataclasses.field()

    StackSetName = field("StackSetName")
    OperationPreferences = field("OperationPreferences")
    OperationId = field("OperationId")
    CallAs = field("CallAs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DetectStackSetDriftInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DetectStackSetDriftInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImportStacksToStackSetInput:
    boto3_raw_data: "type_defs.ImportStacksToStackSetInputTypeDef" = dataclasses.field()

    StackSetName = field("StackSetName")
    StackIds = field("StackIds")
    StackIdsUrl = field("StackIdsUrl")
    OrganizationalUnitIds = field("OrganizationalUnitIds")
    OperationPreferences = field("OperationPreferences")
    OperationId = field("OperationId")
    CallAs = field("CallAs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImportStacksToStackSetInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImportStacksToStackSetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStackInstancesInput:
    boto3_raw_data: "type_defs.UpdateStackInstancesInputTypeDef" = dataclasses.field()

    StackSetName = field("StackSetName")
    Regions = field("Regions")
    Accounts = field("Accounts")
    DeploymentTargets = field("DeploymentTargets")

    @cached_property
    def ParameterOverrides(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["ParameterOverrides"])

    OperationPreferences = field("OperationPreferences")
    OperationId = field("OperationId")
    CallAs = field("CallAs")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateStackInstancesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStackInstancesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStackSetInput:
    boto3_raw_data: "type_defs.UpdateStackSetInputTypeDef" = dataclasses.field()

    StackSetName = field("StackSetName")
    Description = field("Description")
    TemplateBody = field("TemplateBody")
    TemplateURL = field("TemplateURL")
    UsePreviousTemplate = field("UsePreviousTemplate")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    Capabilities = field("Capabilities")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    OperationPreferences = field("OperationPreferences")
    AdministrationRoleARN = field("AdministrationRoleARN")
    ExecutionRoleName = field("ExecutionRoleName")
    DeploymentTargets = field("DeploymentTargets")
    PermissionModel = field("PermissionModel")

    @cached_property
    def AutoDeployment(self):  # pragma: no cover
        return AutoDeployment.make_one(self.boto3_raw_data["AutoDeployment"])

    OperationId = field("OperationId")
    Accounts = field("Accounts")
    Regions = field("Regions")
    CallAs = field("CallAs")

    @cached_property
    def ManagedExecution(self):  # pragma: no cover
        return ManagedExecution.make_one(self.boto3_raw_data["ManagedExecution"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateStackSetInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStackSetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackSetOperationsOutput:
    boto3_raw_data: "type_defs.ListStackSetOperationsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Summaries(self):  # pragma: no cover
        return StackSetOperationSummary.make_many(self.boto3_raw_data["Summaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListStackSetOperationsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackSetOperationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStackSetOperationOutput:
    boto3_raw_data: "type_defs.DescribeStackSetOperationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StackSetOperation(self):  # pragma: no cover
        return StackSetOperation.make_one(self.boto3_raw_data["StackSetOperation"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeStackSetOperationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStackSetOperationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceDetail:
    boto3_raw_data: "type_defs.ResourceDetailTypeDef" = dataclasses.field()

    ResourceType = field("ResourceType")
    LogicalResourceId = field("LogicalResourceId")
    ResourceIdentifier = field("ResourceIdentifier")
    ResourceStatus = field("ResourceStatus")
    ResourceStatusReason = field("ResourceStatusReason")

    @cached_property
    def Warnings(self):  # pragma: no cover
        return WarningDetail.make_many(self.boto3_raw_data["Warnings"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChangeSetHooksOutput:
    boto3_raw_data: "type_defs.DescribeChangeSetHooksOutputTypeDef" = (
        dataclasses.field()
    )

    ChangeSetId = field("ChangeSetId")
    ChangeSetName = field("ChangeSetName")

    @cached_property
    def Hooks(self):  # pragma: no cover
        return ChangeSetHook.make_many(self.boto3_raw_data["Hooks"])

    Status = field("Status")
    StackId = field("StackId")
    StackName = field("StackName")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeChangeSetHooksOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChangeSetHooksOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Change:
    boto3_raw_data: "type_defs.ChangeTypeDef" = dataclasses.field()

    Type = field("Type")
    HookInvocationCount = field("HookInvocationCount")

    @cached_property
    def ResourceChange(self):  # pragma: no cover
        return ResourceChange.make_one(self.boto3_raw_data["ResourceChange"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChangeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChangeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListStackRefactorActionsOutput:
    boto3_raw_data: "type_defs.ListStackRefactorActionsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def StackRefactorActions(self):  # pragma: no cover
        return StackRefactorAction.make_many(
            self.boto3_raw_data["StackRefactorActions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListStackRefactorActionsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListStackRefactorActionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeStacksOutput:
    boto3_raw_data: "type_defs.DescribeStacksOutputTypeDef" = dataclasses.field()

    @cached_property
    def Stacks(self):  # pragma: no cover
        return Stack.make_many(self.boto3_raw_data["Stacks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeStacksOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeStacksOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateChangeSetInput:
    boto3_raw_data: "type_defs.CreateChangeSetInputTypeDef" = dataclasses.field()

    StackName = field("StackName")
    ChangeSetName = field("ChangeSetName")
    TemplateBody = field("TemplateBody")
    TemplateURL = field("TemplateURL")
    UsePreviousTemplate = field("UsePreviousTemplate")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    Capabilities = field("Capabilities")
    ResourceTypes = field("ResourceTypes")
    RoleARN = field("RoleARN")
    RollbackConfiguration = field("RollbackConfiguration")
    NotificationARNs = field("NotificationARNs")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientToken = field("ClientToken")
    Description = field("Description")
    ChangeSetType = field("ChangeSetType")

    @cached_property
    def ResourcesToImport(self):  # pragma: no cover
        return ResourceToImport.make_many(self.boto3_raw_data["ResourcesToImport"])

    IncludeNestedStacks = field("IncludeNestedStacks")
    OnStackFailure = field("OnStackFailure")
    ImportExistingResources = field("ImportExistingResources")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateChangeSetInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateChangeSetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStackInputServiceResourceCreateStack:
    boto3_raw_data: "type_defs.CreateStackInputServiceResourceCreateStackTypeDef" = (
        dataclasses.field()
    )

    StackName = field("StackName")
    TemplateBody = field("TemplateBody")
    TemplateURL = field("TemplateURL")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    DisableRollback = field("DisableRollback")
    RollbackConfiguration = field("RollbackConfiguration")
    TimeoutInMinutes = field("TimeoutInMinutes")
    NotificationARNs = field("NotificationARNs")
    Capabilities = field("Capabilities")
    ResourceTypes = field("ResourceTypes")
    RoleARN = field("RoleARN")
    OnFailure = field("OnFailure")
    StackPolicyBody = field("StackPolicyBody")
    StackPolicyURL = field("StackPolicyURL")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientRequestToken = field("ClientRequestToken")
    EnableTerminationProtection = field("EnableTerminationProtection")
    RetainExceptOnCreate = field("RetainExceptOnCreate")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateStackInputServiceResourceCreateStackTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStackInputServiceResourceCreateStackTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStackInput:
    boto3_raw_data: "type_defs.CreateStackInputTypeDef" = dataclasses.field()

    StackName = field("StackName")
    TemplateBody = field("TemplateBody")
    TemplateURL = field("TemplateURL")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    DisableRollback = field("DisableRollback")
    RollbackConfiguration = field("RollbackConfiguration")
    TimeoutInMinutes = field("TimeoutInMinutes")
    NotificationARNs = field("NotificationARNs")
    Capabilities = field("Capabilities")
    ResourceTypes = field("ResourceTypes")
    RoleARN = field("RoleARN")
    OnFailure = field("OnFailure")
    StackPolicyBody = field("StackPolicyBody")
    StackPolicyURL = field("StackPolicyURL")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    ClientRequestToken = field("ClientRequestToken")
    EnableTerminationProtection = field("EnableTerminationProtection")
    RetainExceptOnCreate = field("RetainExceptOnCreate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateStackInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStackInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStackInputStackUpdate:
    boto3_raw_data: "type_defs.UpdateStackInputStackUpdateTypeDef" = dataclasses.field()

    TemplateBody = field("TemplateBody")
    TemplateURL = field("TemplateURL")
    UsePreviousTemplate = field("UsePreviousTemplate")
    StackPolicyDuringUpdateBody = field("StackPolicyDuringUpdateBody")
    StackPolicyDuringUpdateURL = field("StackPolicyDuringUpdateURL")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    Capabilities = field("Capabilities")
    ResourceTypes = field("ResourceTypes")
    RoleARN = field("RoleARN")
    RollbackConfiguration = field("RollbackConfiguration")
    StackPolicyBody = field("StackPolicyBody")
    StackPolicyURL = field("StackPolicyURL")
    NotificationARNs = field("NotificationARNs")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    DisableRollback = field("DisableRollback")
    ClientRequestToken = field("ClientRequestToken")
    RetainExceptOnCreate = field("RetainExceptOnCreate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateStackInputStackUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStackInputStackUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateStackInput:
    boto3_raw_data: "type_defs.UpdateStackInputTypeDef" = dataclasses.field()

    StackName = field("StackName")
    TemplateBody = field("TemplateBody")
    TemplateURL = field("TemplateURL")
    UsePreviousTemplate = field("UsePreviousTemplate")
    StackPolicyDuringUpdateBody = field("StackPolicyDuringUpdateBody")
    StackPolicyDuringUpdateURL = field("StackPolicyDuringUpdateURL")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    Capabilities = field("Capabilities")
    ResourceTypes = field("ResourceTypes")
    RoleARN = field("RoleARN")
    RollbackConfiguration = field("RollbackConfiguration")
    StackPolicyBody = field("StackPolicyBody")
    StackPolicyURL = field("StackPolicyURL")
    NotificationARNs = field("NotificationARNs")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    DisableRollback = field("DisableRollback")
    ClientRequestToken = field("ClientRequestToken")
    RetainExceptOnCreate = field("RetainExceptOnCreate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateStackInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateStackInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeGeneratedTemplateOutput:
    boto3_raw_data: "type_defs.DescribeGeneratedTemplateOutputTypeDef" = (
        dataclasses.field()
    )

    GeneratedTemplateId = field("GeneratedTemplateId")
    GeneratedTemplateName = field("GeneratedTemplateName")

    @cached_property
    def Resources(self):  # pragma: no cover
        return ResourceDetail.make_many(self.boto3_raw_data["Resources"])

    Status = field("Status")
    StatusReason = field("StatusReason")
    CreationTime = field("CreationTime")
    LastUpdatedTime = field("LastUpdatedTime")

    @cached_property
    def Progress(self):  # pragma: no cover
        return TemplateProgress.make_one(self.boto3_raw_data["Progress"])

    StackId = field("StackId")

    @cached_property
    def TemplateConfiguration(self):  # pragma: no cover
        return TemplateConfiguration.make_one(
            self.boto3_raw_data["TemplateConfiguration"]
        )

    TotalWarnings = field("TotalWarnings")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeGeneratedTemplateOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeGeneratedTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeChangeSetOutput:
    boto3_raw_data: "type_defs.DescribeChangeSetOutputTypeDef" = dataclasses.field()

    ChangeSetName = field("ChangeSetName")
    ChangeSetId = field("ChangeSetId")
    StackId = field("StackId")
    StackName = field("StackName")
    Description = field("Description")

    @cached_property
    def Parameters(self):  # pragma: no cover
        return Parameter.make_many(self.boto3_raw_data["Parameters"])

    CreationTime = field("CreationTime")
    ExecutionStatus = field("ExecutionStatus")
    Status = field("Status")
    StatusReason = field("StatusReason")
    NotificationARNs = field("NotificationARNs")

    @cached_property
    def RollbackConfiguration(self):  # pragma: no cover
        return RollbackConfigurationOutput.make_one(
            self.boto3_raw_data["RollbackConfiguration"]
        )

    Capabilities = field("Capabilities")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @cached_property
    def Changes(self):  # pragma: no cover
        return Change.make_many(self.boto3_raw_data["Changes"])

    IncludeNestedStacks = field("IncludeNestedStacks")
    ParentChangeSetId = field("ParentChangeSetId")
    RootChangeSetId = field("RootChangeSetId")
    OnStackFailure = field("OnStackFailure")
    ImportExistingResources = field("ImportExistingResources")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeChangeSetOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeChangeSetOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
