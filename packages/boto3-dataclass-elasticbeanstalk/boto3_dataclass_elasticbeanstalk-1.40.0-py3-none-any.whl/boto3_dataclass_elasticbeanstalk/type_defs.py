# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_elasticbeanstalk import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AbortEnvironmentUpdateMessage:
    boto3_raw_data: "type_defs.AbortEnvironmentUpdateMessageTypeDef" = (
        dataclasses.field()
    )

    EnvironmentId = field("EnvironmentId")
    EnvironmentName = field("EnvironmentName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AbortEnvironmentUpdateMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AbortEnvironmentUpdateMessageTypeDef"]
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
class Latency:
    boto3_raw_data: "type_defs.LatencyTypeDef" = dataclasses.field()

    P999 = field("P999")
    P99 = field("P99")
    P95 = field("P95")
    P90 = field("P90")
    P85 = field("P85")
    P75 = field("P75")
    P50 = field("P50")
    P10 = field("P10")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LatencyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LatencyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StatusCodes:
    boto3_raw_data: "type_defs.StatusCodesTypeDef" = dataclasses.field()

    Status2xx = field("Status2xx")
    Status3xx = field("Status3xx")
    Status4xx = field("Status4xx")
    Status5xx = field("Status5xx")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StatusCodesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StatusCodesTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Location:
    boto3_raw_data: "type_defs.S3LocationTypeDef" = dataclasses.field()

    S3Bucket = field("S3Bucket")
    S3Key = field("S3Key")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.S3LocationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.S3LocationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceBuildInformation:
    boto3_raw_data: "type_defs.SourceBuildInformationTypeDef" = dataclasses.field()

    SourceType = field("SourceType")
    SourceRepository = field("SourceRepository")
    SourceLocation = field("SourceLocation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceBuildInformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceBuildInformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MaxAgeRule:
    boto3_raw_data: "type_defs.MaxAgeRuleTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    MaxAgeInDays = field("MaxAgeInDays")
    DeleteSourceFromS3 = field("DeleteSourceFromS3")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MaxAgeRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MaxAgeRuleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MaxCountRule:
    boto3_raw_data: "type_defs.MaxCountRuleTypeDef" = dataclasses.field()

    Enabled = field("Enabled")
    MaxCount = field("MaxCount")
    DeleteSourceFromS3 = field("DeleteSourceFromS3")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MaxCountRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MaxCountRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplyEnvironmentManagedActionRequest:
    boto3_raw_data: "type_defs.ApplyEnvironmentManagedActionRequestTypeDef" = (
        dataclasses.field()
    )

    ActionId = field("ActionId")
    EnvironmentName = field("EnvironmentName")
    EnvironmentId = field("EnvironmentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplyEnvironmentManagedActionRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplyEnvironmentManagedActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateEnvironmentOperationsRoleMessage:
    boto3_raw_data: "type_defs.AssociateEnvironmentOperationsRoleMessageTypeDef" = (
        dataclasses.field()
    )

    EnvironmentName = field("EnvironmentName")
    OperationsRole = field("OperationsRole")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateEnvironmentOperationsRoleMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateEnvironmentOperationsRoleMessageTypeDef"]
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

    Name = field("Name")

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
class BuildConfiguration:
    boto3_raw_data: "type_defs.BuildConfigurationTypeDef" = dataclasses.field()

    CodeBuildServiceRole = field("CodeBuildServiceRole")
    Image = field("Image")
    ArtifactName = field("ArtifactName")
    ComputeType = field("ComputeType")
    TimeoutInMinutes = field("TimeoutInMinutes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BuildConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BuildConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Builder:
    boto3_raw_data: "type_defs.BuilderTypeDef" = dataclasses.field()

    ARN = field("ARN")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BuilderTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BuilderTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CPUUtilization:
    boto3_raw_data: "type_defs.CPUUtilizationTypeDef" = dataclasses.field()

    User = field("User")
    Nice = field("Nice")
    System = field("System")
    Idle = field("Idle")
    IOWait = field("IOWait")
    IRQ = field("IRQ")
    SoftIRQ = field("SoftIRQ")
    Privileged = field("Privileged")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CPUUtilizationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CPUUtilizationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckDNSAvailabilityMessage:
    boto3_raw_data: "type_defs.CheckDNSAvailabilityMessageTypeDef" = dataclasses.field()

    CNAMEPrefix = field("CNAMEPrefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CheckDNSAvailabilityMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CheckDNSAvailabilityMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComposeEnvironmentsMessage:
    boto3_raw_data: "type_defs.ComposeEnvironmentsMessageTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")
    GroupName = field("GroupName")
    VersionLabels = field("VersionLabels")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComposeEnvironmentsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComposeEnvironmentsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OptionRestrictionRegex:
    boto3_raw_data: "type_defs.OptionRestrictionRegexTypeDef" = dataclasses.field()

    Pattern = field("Pattern")
    Label = field("Label")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OptionRestrictionRegexTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OptionRestrictionRegexTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationOptionSetting:
    boto3_raw_data: "type_defs.ConfigurationOptionSettingTypeDef" = dataclasses.field()

    ResourceName = field("ResourceName")
    Namespace = field("Namespace")
    OptionName = field("OptionName")
    Value = field("Value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationOptionSettingTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationOptionSettingTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidationMessage:
    boto3_raw_data: "type_defs.ValidationMessageTypeDef" = dataclasses.field()

    Message = field("Message")
    Severity = field("Severity")
    Namespace = field("Namespace")
    OptionName = field("OptionName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ValidationMessageTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidationMessageTypeDef"]
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
class SourceConfiguration:
    boto3_raw_data: "type_defs.SourceConfigurationTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")
    TemplateName = field("TemplateName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentTier:
    boto3_raw_data: "type_defs.EnvironmentTierTypeDef" = dataclasses.field()

    Name = field("Name")
    Type = field("Type")
    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnvironmentTierTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EnvironmentTierTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OptionSpecification:
    boto3_raw_data: "type_defs.OptionSpecificationTypeDef" = dataclasses.field()

    ResourceName = field("ResourceName")
    Namespace = field("Namespace")
    OptionName = field("OptionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OptionSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OptionSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlatformSummary:
    boto3_raw_data: "type_defs.PlatformSummaryTypeDef" = dataclasses.field()

    PlatformArn = field("PlatformArn")
    PlatformOwner = field("PlatformOwner")
    PlatformStatus = field("PlatformStatus")
    PlatformCategory = field("PlatformCategory")
    OperatingSystemName = field("OperatingSystemName")
    OperatingSystemVersion = field("OperatingSystemVersion")
    SupportedTierList = field("SupportedTierList")
    SupportedAddonList = field("SupportedAddonList")
    PlatformLifecycleState = field("PlatformLifecycleState")
    PlatformVersion = field("PlatformVersion")
    PlatformBranchName = field("PlatformBranchName")
    PlatformBranchLifecycleState = field("PlatformBranchLifecycleState")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PlatformSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PlatformSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CustomAmi:
    boto3_raw_data: "type_defs.CustomAmiTypeDef" = dataclasses.field()

    VirtualizationType = field("VirtualizationType")
    ImageId = field("ImageId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CustomAmiTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CustomAmiTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationMessage:
    boto3_raw_data: "type_defs.DeleteApplicationMessageTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")
    TerminateEnvByForce = field("TerminateEnvByForce")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteApplicationMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteApplicationVersionMessage:
    boto3_raw_data: "type_defs.DeleteApplicationVersionMessageTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    VersionLabel = field("VersionLabel")
    DeleteSourceBundle = field("DeleteSourceBundle")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteApplicationVersionMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteApplicationVersionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConfigurationTemplateMessage:
    boto3_raw_data: "type_defs.DeleteConfigurationTemplateMessageTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    TemplateName = field("TemplateName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteConfigurationTemplateMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConfigurationTemplateMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteEnvironmentConfigurationMessage:
    boto3_raw_data: "type_defs.DeleteEnvironmentConfigurationMessageTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    EnvironmentName = field("EnvironmentName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteEnvironmentConfigurationMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteEnvironmentConfigurationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePlatformVersionRequest:
    boto3_raw_data: "type_defs.DeletePlatformVersionRequestTypeDef" = (
        dataclasses.field()
    )

    PlatformArn = field("PlatformArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePlatformVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePlatformVersionRequestTypeDef"]
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

    VersionLabel = field("VersionLabel")
    DeploymentId = field("DeploymentId")
    Status = field("Status")
    DeploymentTime = field("DeploymentTime")

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
class DescribeApplicationVersionsMessage:
    boto3_raw_data: "type_defs.DescribeApplicationVersionsMessageTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    VersionLabels = field("VersionLabels")
    MaxRecords = field("MaxRecords")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeApplicationVersionsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationVersionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationsMessage:
    boto3_raw_data: "type_defs.DescribeApplicationsMessageTypeDef" = dataclasses.field()

    ApplicationNames = field("ApplicationNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeApplicationsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigurationSettingsMessage:
    boto3_raw_data: "type_defs.DescribeConfigurationSettingsMessageTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    TemplateName = field("TemplateName")
    EnvironmentName = field("EnvironmentName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConfigurationSettingsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigurationSettingsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEnvironmentHealthRequest:
    boto3_raw_data: "type_defs.DescribeEnvironmentHealthRequestTypeDef" = (
        dataclasses.field()
    )

    EnvironmentName = field("EnvironmentName")
    EnvironmentId = field("EnvironmentId")
    AttributeNames = field("AttributeNames")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEnvironmentHealthRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEnvironmentHealthRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InstanceHealthSummary:
    boto3_raw_data: "type_defs.InstanceHealthSummaryTypeDef" = dataclasses.field()

    NoData = field("NoData")
    Unknown = field("Unknown")
    Pending = field("Pending")
    Ok = field("Ok")
    Info = field("Info")
    Warning = field("Warning")
    Degraded = field("Degraded")
    Severe = field("Severe")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InstanceHealthSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InstanceHealthSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEnvironmentManagedActionHistoryRequest:
    boto3_raw_data: (
        "type_defs.DescribeEnvironmentManagedActionHistoryRequestTypeDef"
    ) = dataclasses.field()

    EnvironmentId = field("EnvironmentId")
    EnvironmentName = field("EnvironmentName")
    NextToken = field("NextToken")
    MaxItems = field("MaxItems")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEnvironmentManagedActionHistoryRequestTypeDef"
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
                "type_defs.DescribeEnvironmentManagedActionHistoryRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedActionHistoryItem:
    boto3_raw_data: "type_defs.ManagedActionHistoryItemTypeDef" = dataclasses.field()

    ActionId = field("ActionId")
    ActionType = field("ActionType")
    ActionDescription = field("ActionDescription")
    FailureType = field("FailureType")
    Status = field("Status")
    FailureDescription = field("FailureDescription")
    ExecutedTime = field("ExecutedTime")
    FinishedTime = field("FinishedTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ManagedActionHistoryItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ManagedActionHistoryItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEnvironmentManagedActionsRequest:
    boto3_raw_data: "type_defs.DescribeEnvironmentManagedActionsRequestTypeDef" = (
        dataclasses.field()
    )

    EnvironmentName = field("EnvironmentName")
    EnvironmentId = field("EnvironmentId")
    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEnvironmentManagedActionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEnvironmentManagedActionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManagedAction:
    boto3_raw_data: "type_defs.ManagedActionTypeDef" = dataclasses.field()

    ActionId = field("ActionId")
    ActionDescription = field("ActionDescription")
    ActionType = field("ActionType")
    Status = field("Status")
    WindowStartTime = field("WindowStartTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ManagedActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ManagedActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEnvironmentResourcesMessage:
    boto3_raw_data: "type_defs.DescribeEnvironmentResourcesMessageTypeDef" = (
        dataclasses.field()
    )

    EnvironmentId = field("EnvironmentId")
    EnvironmentName = field("EnvironmentName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEnvironmentResourcesMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEnvironmentResourcesMessageTypeDef"]
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
class DescribeInstancesHealthRequest:
    boto3_raw_data: "type_defs.DescribeInstancesHealthRequestTypeDef" = (
        dataclasses.field()
    )

    EnvironmentName = field("EnvironmentName")
    EnvironmentId = field("EnvironmentId")
    AttributeNames = field("AttributeNames")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeInstancesHealthRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstancesHealthRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePlatformVersionRequest:
    boto3_raw_data: "type_defs.DescribePlatformVersionRequestTypeDef" = (
        dataclasses.field()
    )

    PlatformArn = field("PlatformArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribePlatformVersionRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePlatformVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateEnvironmentOperationsRoleMessage:
    boto3_raw_data: "type_defs.DisassociateEnvironmentOperationsRoleMessageTypeDef" = (
        dataclasses.field()
    )

    EnvironmentName = field("EnvironmentName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateEnvironmentOperationsRoleMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateEnvironmentOperationsRoleMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentLink:
    boto3_raw_data: "type_defs.EnvironmentLinkTypeDef" = dataclasses.field()

    LinkName = field("LinkName")
    EnvironmentName = field("EnvironmentName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EnvironmentLinkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EnvironmentLinkTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentInfoDescription:
    boto3_raw_data: "type_defs.EnvironmentInfoDescriptionTypeDef" = dataclasses.field()

    InfoType = field("InfoType")
    Ec2InstanceId = field("Ec2InstanceId")
    SampleTimestamp = field("SampleTimestamp")
    Message = field("Message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentInfoDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentInfoDescriptionTypeDef"]
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

    Id = field("Id")

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
class LaunchConfiguration:
    boto3_raw_data: "type_defs.LaunchConfigurationTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LaunchConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LaunchConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LaunchTemplate:
    boto3_raw_data: "type_defs.LaunchTemplateTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LaunchTemplateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LaunchTemplateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LoadBalancer:
    boto3_raw_data: "type_defs.LoadBalancerTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LoadBalancerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LoadBalancerTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Queue:
    boto3_raw_data: "type_defs.QueueTypeDef" = dataclasses.field()

    Name = field("Name")
    URL = field("URL")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueueTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Trigger:
    boto3_raw_data: "type_defs.TriggerTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TriggerTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TriggerTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventDescription:
    boto3_raw_data: "type_defs.EventDescriptionTypeDef" = dataclasses.field()

    EventDate = field("EventDate")
    Message = field("Message")
    ApplicationName = field("ApplicationName")
    VersionLabel = field("VersionLabel")
    TemplateName = field("TemplateName")
    EnvironmentName = field("EnvironmentName")
    PlatformArn = field("PlatformArn")
    RequestId = field("RequestId")
    Severity = field("Severity")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventDescriptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SolutionStackDescription:
    boto3_raw_data: "type_defs.SolutionStackDescriptionTypeDef" = dataclasses.field()

    SolutionStackName = field("SolutionStackName")
    PermittedFileTypes = field("PermittedFileTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SolutionStackDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SolutionStackDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchFilter:
    boto3_raw_data: "type_defs.SearchFilterTypeDef" = dataclasses.field()

    Attribute = field("Attribute")
    Operator = field("Operator")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SearchFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlatformBranchSummary:
    boto3_raw_data: "type_defs.PlatformBranchSummaryTypeDef" = dataclasses.field()

    PlatformName = field("PlatformName")
    BranchName = field("BranchName")
    LifecycleState = field("LifecycleState")
    BranchOrder = field("BranchOrder")
    SupportedTierList = field("SupportedTierList")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PlatformBranchSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PlatformBranchSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlatformFilter:
    boto3_raw_data: "type_defs.PlatformFilterTypeDef" = dataclasses.field()

    Type = field("Type")
    Operator = field("Operator")
    Values = field("Values")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PlatformFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PlatformFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceMessage:
    boto3_raw_data: "type_defs.ListTagsForResourceMessageTypeDef" = dataclasses.field()

    ResourceArn = field("ResourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceMessageTypeDef"]
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
    Port = field("Port")

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
class PlatformFramework:
    boto3_raw_data: "type_defs.PlatformFrameworkTypeDef" = dataclasses.field()

    Name = field("Name")
    Version = field("Version")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PlatformFrameworkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PlatformFrameworkTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PlatformProgrammingLanguage:
    boto3_raw_data: "type_defs.PlatformProgrammingLanguageTypeDef" = dataclasses.field()

    Name = field("Name")
    Version = field("Version")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PlatformProgrammingLanguageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PlatformProgrammingLanguageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RebuildEnvironmentMessage:
    boto3_raw_data: "type_defs.RebuildEnvironmentMessageTypeDef" = dataclasses.field()

    EnvironmentId = field("EnvironmentId")
    EnvironmentName = field("EnvironmentName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RebuildEnvironmentMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RebuildEnvironmentMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequestEnvironmentInfoMessage:
    boto3_raw_data: "type_defs.RequestEnvironmentInfoMessageTypeDef" = (
        dataclasses.field()
    )

    InfoType = field("InfoType")
    EnvironmentId = field("EnvironmentId")
    EnvironmentName = field("EnvironmentName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RequestEnvironmentInfoMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequestEnvironmentInfoMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceQuota:
    boto3_raw_data: "type_defs.ResourceQuotaTypeDef" = dataclasses.field()

    Maximum = field("Maximum")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceQuotaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceQuotaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RestartAppServerMessage:
    boto3_raw_data: "type_defs.RestartAppServerMessageTypeDef" = dataclasses.field()

    EnvironmentId = field("EnvironmentId")
    EnvironmentName = field("EnvironmentName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RestartAppServerMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RestartAppServerMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveEnvironmentInfoMessage:
    boto3_raw_data: "type_defs.RetrieveEnvironmentInfoMessageTypeDef" = (
        dataclasses.field()
    )

    InfoType = field("InfoType")
    EnvironmentId = field("EnvironmentId")
    EnvironmentName = field("EnvironmentName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.RetrieveEnvironmentInfoMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveEnvironmentInfoMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SwapEnvironmentCNAMEsMessage:
    boto3_raw_data: "type_defs.SwapEnvironmentCNAMEsMessageTypeDef" = (
        dataclasses.field()
    )

    SourceEnvironmentId = field("SourceEnvironmentId")
    SourceEnvironmentName = field("SourceEnvironmentName")
    DestinationEnvironmentId = field("DestinationEnvironmentId")
    DestinationEnvironmentName = field("DestinationEnvironmentName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SwapEnvironmentCNAMEsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SwapEnvironmentCNAMEsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TerminateEnvironmentMessage:
    boto3_raw_data: "type_defs.TerminateEnvironmentMessageTypeDef" = dataclasses.field()

    EnvironmentId = field("EnvironmentId")
    EnvironmentName = field("EnvironmentName")
    TerminateResources = field("TerminateResources")
    ForceTerminate = field("ForceTerminate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TerminateEnvironmentMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TerminateEnvironmentMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApplicationMessage:
    boto3_raw_data: "type_defs.UpdateApplicationMessageTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")
    Description = field("Description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateApplicationMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApplicationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApplicationVersionMessage:
    boto3_raw_data: "type_defs.UpdateApplicationVersionMessageTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    VersionLabel = field("VersionLabel")
    Description = field("Description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateApplicationVersionMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApplicationVersionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplyEnvironmentManagedActionResult:
    boto3_raw_data: "type_defs.ApplyEnvironmentManagedActionResultTypeDef" = (
        dataclasses.field()
    )

    ActionId = field("ActionId")
    ActionDescription = field("ActionDescription")
    ActionType = field("ActionType")
    Status = field("Status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplyEnvironmentManagedActionResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplyEnvironmentManagedActionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CheckDNSAvailabilityResultMessage:
    boto3_raw_data: "type_defs.CheckDNSAvailabilityResultMessageTypeDef" = (
        dataclasses.field()
    )

    Available = field("Available")
    FullyQualifiedCNAME = field("FullyQualifiedCNAME")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CheckDNSAvailabilityResultMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CheckDNSAvailabilityResultMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateStorageLocationResultMessage:
    boto3_raw_data: "type_defs.CreateStorageLocationResultMessageTypeDef" = (
        dataclasses.field()
    )

    S3Bucket = field("S3Bucket")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateStorageLocationResultMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateStorageLocationResultMessageTypeDef"]
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
class ApplicationMetrics:
    boto3_raw_data: "type_defs.ApplicationMetricsTypeDef" = dataclasses.field()

    Duration = field("Duration")
    RequestCount = field("RequestCount")

    @cached_property
    def StatusCodes(self):  # pragma: no cover
        return StatusCodes.make_one(self.boto3_raw_data["StatusCodes"])

    @cached_property
    def Latency(self):  # pragma: no cover
        return Latency.make_one(self.boto3_raw_data["Latency"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationMetricsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationMetricsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationVersionDescription:
    boto3_raw_data: "type_defs.ApplicationVersionDescriptionTypeDef" = (
        dataclasses.field()
    )

    ApplicationVersionArn = field("ApplicationVersionArn")
    ApplicationName = field("ApplicationName")
    Description = field("Description")
    VersionLabel = field("VersionLabel")

    @cached_property
    def SourceBuildInformation(self):  # pragma: no cover
        return SourceBuildInformation.make_one(
            self.boto3_raw_data["SourceBuildInformation"]
        )

    BuildArn = field("BuildArn")

    @cached_property
    def SourceBundle(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["SourceBundle"])

    DateCreated = field("DateCreated")
    DateUpdated = field("DateUpdated")
    Status = field("Status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ApplicationVersionDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationVersionDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationVersionLifecycleConfig:
    boto3_raw_data: "type_defs.ApplicationVersionLifecycleConfigTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MaxCountRule(self):  # pragma: no cover
        return MaxCountRule.make_one(self.boto3_raw_data["MaxCountRule"])

    @cached_property
    def MaxAgeRule(self):  # pragma: no cover
        return MaxAgeRule.make_one(self.boto3_raw_data["MaxAgeRule"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplicationVersionLifecycleConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationVersionLifecycleConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SystemStatus:
    boto3_raw_data: "type_defs.SystemStatusTypeDef" = dataclasses.field()

    @cached_property
    def CPUUtilization(self):  # pragma: no cover
        return CPUUtilization.make_one(self.boto3_raw_data["CPUUtilization"])

    LoadAverage = field("LoadAverage")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SystemStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SystemStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationOptionDescription:
    boto3_raw_data: "type_defs.ConfigurationOptionDescriptionTypeDef" = (
        dataclasses.field()
    )

    Namespace = field("Namespace")
    Name = field("Name")
    DefaultValue = field("DefaultValue")
    ChangeSeverity = field("ChangeSeverity")
    UserDefined = field("UserDefined")
    ValueType = field("ValueType")
    ValueOptions = field("ValueOptions")
    MinValue = field("MinValue")
    MaxValue = field("MaxValue")
    MaxLength = field("MaxLength")

    @cached_property
    def Regex(self):  # pragma: no cover
        return OptionRestrictionRegex.make_one(self.boto3_raw_data["Regex"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConfigurationOptionDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationOptionDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationSettingsDescriptionResponse:
    boto3_raw_data: "type_defs.ConfigurationSettingsDescriptionResponseTypeDef" = (
        dataclasses.field()
    )

    SolutionStackName = field("SolutionStackName")
    PlatformArn = field("PlatformArn")
    ApplicationName = field("ApplicationName")
    TemplateName = field("TemplateName")
    Description = field("Description")
    EnvironmentName = field("EnvironmentName")
    DeploymentStatus = field("DeploymentStatus")
    DateCreated = field("DateCreated")
    DateUpdated = field("DateUpdated")

    @cached_property
    def OptionSettings(self):  # pragma: no cover
        return ConfigurationOptionSetting.make_many(
            self.boto3_raw_data["OptionSettings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfigurationSettingsDescriptionResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationSettingsDescriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationSettingsDescription:
    boto3_raw_data: "type_defs.ConfigurationSettingsDescriptionTypeDef" = (
        dataclasses.field()
    )

    SolutionStackName = field("SolutionStackName")
    PlatformArn = field("PlatformArn")
    ApplicationName = field("ApplicationName")
    TemplateName = field("TemplateName")
    Description = field("Description")
    EnvironmentName = field("EnvironmentName")
    DeploymentStatus = field("DeploymentStatus")
    DateCreated = field("DateCreated")
    DateUpdated = field("DateUpdated")

    @cached_property
    def OptionSettings(self):  # pragma: no cover
        return ConfigurationOptionSetting.make_many(
            self.boto3_raw_data["OptionSettings"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConfigurationSettingsDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationSettingsDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidateConfigurationSettingsMessage:
    boto3_raw_data: "type_defs.ValidateConfigurationSettingsMessageTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")

    @cached_property
    def OptionSettings(self):  # pragma: no cover
        return ConfigurationOptionSetting.make_many(
            self.boto3_raw_data["OptionSettings"]
        )

    TemplateName = field("TemplateName")
    EnvironmentName = field("EnvironmentName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ValidateConfigurationSettingsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidateConfigurationSettingsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationSettingsValidationMessages:
    boto3_raw_data: "type_defs.ConfigurationSettingsValidationMessagesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Messages(self):  # pragma: no cover
        return ValidationMessage.make_many(self.boto3_raw_data["Messages"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfigurationSettingsValidationMessagesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationSettingsValidationMessagesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApplicationVersionMessage:
    boto3_raw_data: "type_defs.CreateApplicationVersionMessageTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    VersionLabel = field("VersionLabel")
    Description = field("Description")

    @cached_property
    def SourceBuildInformation(self):  # pragma: no cover
        return SourceBuildInformation.make_one(
            self.boto3_raw_data["SourceBuildInformation"]
        )

    @cached_property
    def SourceBundle(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["SourceBundle"])

    @cached_property
    def BuildConfiguration(self):  # pragma: no cover
        return BuildConfiguration.make_one(self.boto3_raw_data["BuildConfiguration"])

    AutoCreateApplication = field("AutoCreateApplication")
    Process = field("Process")

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateApplicationVersionMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationVersionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePlatformVersionRequest:
    boto3_raw_data: "type_defs.CreatePlatformVersionRequestTypeDef" = (
        dataclasses.field()
    )

    PlatformName = field("PlatformName")
    PlatformVersion = field("PlatformVersion")

    @cached_property
    def PlatformDefinitionBundle(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["PlatformDefinitionBundle"])

    EnvironmentName = field("EnvironmentName")

    @cached_property
    def OptionSettings(self):  # pragma: no cover
        return ConfigurationOptionSetting.make_many(
            self.boto3_raw_data["OptionSettings"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePlatformVersionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePlatformVersionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceTagsDescriptionMessage:
    boto3_raw_data: "type_defs.ResourceTagsDescriptionMessageTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")

    @cached_property
    def ResourceTags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["ResourceTags"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ResourceTagsDescriptionMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceTagsDescriptionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTagsForResourceMessage:
    boto3_raw_data: "type_defs.UpdateTagsForResourceMessageTypeDef" = (
        dataclasses.field()
    )

    ResourceArn = field("ResourceArn")

    @cached_property
    def TagsToAdd(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["TagsToAdd"])

    TagsToRemove = field("TagsToRemove")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTagsForResourceMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTagsForResourceMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfigurationTemplateMessage:
    boto3_raw_data: "type_defs.CreateConfigurationTemplateMessageTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    TemplateName = field("TemplateName")
    SolutionStackName = field("SolutionStackName")
    PlatformArn = field("PlatformArn")

    @cached_property
    def SourceConfiguration(self):  # pragma: no cover
        return SourceConfiguration.make_one(self.boto3_raw_data["SourceConfiguration"])

    EnvironmentId = field("EnvironmentId")
    Description = field("Description")

    @cached_property
    def OptionSettings(self):  # pragma: no cover
        return ConfigurationOptionSetting.make_many(
            self.boto3_raw_data["OptionSettings"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConfigurationTemplateMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConfigurationTemplateMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateEnvironmentMessage:
    boto3_raw_data: "type_defs.CreateEnvironmentMessageTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")
    EnvironmentName = field("EnvironmentName")
    GroupName = field("GroupName")
    Description = field("Description")
    CNAMEPrefix = field("CNAMEPrefix")

    @cached_property
    def Tier(self):  # pragma: no cover
        return EnvironmentTier.make_one(self.boto3_raw_data["Tier"])

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    VersionLabel = field("VersionLabel")
    TemplateName = field("TemplateName")
    SolutionStackName = field("SolutionStackName")
    PlatformArn = field("PlatformArn")

    @cached_property
    def OptionSettings(self):  # pragma: no cover
        return ConfigurationOptionSetting.make_many(
            self.boto3_raw_data["OptionSettings"]
        )

    @cached_property
    def OptionsToRemove(self):  # pragma: no cover
        return OptionSpecification.make_many(self.boto3_raw_data["OptionsToRemove"])

    OperationsRole = field("OperationsRole")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateEnvironmentMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateEnvironmentMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigurationOptionsMessage:
    boto3_raw_data: "type_defs.DescribeConfigurationOptionsMessageTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    TemplateName = field("TemplateName")
    EnvironmentName = field("EnvironmentName")
    SolutionStackName = field("SolutionStackName")
    PlatformArn = field("PlatformArn")

    @cached_property
    def Options(self):  # pragma: no cover
        return OptionSpecification.make_many(self.boto3_raw_data["Options"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConfigurationOptionsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigurationOptionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConfigurationTemplateMessage:
    boto3_raw_data: "type_defs.UpdateConfigurationTemplateMessageTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    TemplateName = field("TemplateName")
    Description = field("Description")

    @cached_property
    def OptionSettings(self):  # pragma: no cover
        return ConfigurationOptionSetting.make_many(
            self.boto3_raw_data["OptionSettings"]
        )

    @cached_property
    def OptionsToRemove(self):  # pragma: no cover
        return OptionSpecification.make_many(self.boto3_raw_data["OptionsToRemove"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConfigurationTemplateMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConfigurationTemplateMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateEnvironmentMessage:
    boto3_raw_data: "type_defs.UpdateEnvironmentMessageTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")
    EnvironmentId = field("EnvironmentId")
    EnvironmentName = field("EnvironmentName")
    GroupName = field("GroupName")
    Description = field("Description")

    @cached_property
    def Tier(self):  # pragma: no cover
        return EnvironmentTier.make_one(self.boto3_raw_data["Tier"])

    VersionLabel = field("VersionLabel")
    TemplateName = field("TemplateName")
    SolutionStackName = field("SolutionStackName")
    PlatformArn = field("PlatformArn")

    @cached_property
    def OptionSettings(self):  # pragma: no cover
        return ConfigurationOptionSetting.make_many(
            self.boto3_raw_data["OptionSettings"]
        )

    @cached_property
    def OptionsToRemove(self):  # pragma: no cover
        return OptionSpecification.make_many(self.boto3_raw_data["OptionsToRemove"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateEnvironmentMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateEnvironmentMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePlatformVersionResult:
    boto3_raw_data: "type_defs.CreatePlatformVersionResultTypeDef" = dataclasses.field()

    @cached_property
    def PlatformSummary(self):  # pragma: no cover
        return PlatformSummary.make_one(self.boto3_raw_data["PlatformSummary"])

    @cached_property
    def Builder(self):  # pragma: no cover
        return Builder.make_one(self.boto3_raw_data["Builder"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreatePlatformVersionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePlatformVersionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePlatformVersionResult:
    boto3_raw_data: "type_defs.DeletePlatformVersionResultTypeDef" = dataclasses.field()

    @cached_property
    def PlatformSummary(self):  # pragma: no cover
        return PlatformSummary.make_one(self.boto3_raw_data["PlatformSummary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeletePlatformVersionResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePlatformVersionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPlatformVersionsResult:
    boto3_raw_data: "type_defs.ListPlatformVersionsResultTypeDef" = dataclasses.field()

    @cached_property
    def PlatformSummaryList(self):  # pragma: no cover
        return PlatformSummary.make_many(self.boto3_raw_data["PlatformSummaryList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPlatformVersionsResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPlatformVersionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeApplicationVersionsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeApplicationVersionsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    VersionLabels = field("VersionLabels")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeApplicationVersionsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeApplicationVersionsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEnvironmentManagedActionHistoryRequestPaginate:
    boto3_raw_data: (
        "type_defs.DescribeEnvironmentManagedActionHistoryRequestPaginateTypeDef"
    ) = dataclasses.field()

    EnvironmentId = field("EnvironmentId")
    EnvironmentName = field("EnvironmentName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEnvironmentManagedActionHistoryRequestPaginateTypeDef"
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
                "type_defs.DescribeEnvironmentManagedActionHistoryRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEnvironmentManagedActionHistoryResult:
    boto3_raw_data: "type_defs.DescribeEnvironmentManagedActionHistoryResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ManagedActionHistoryItems(self):  # pragma: no cover
        return ManagedActionHistoryItem.make_many(
            self.boto3_raw_data["ManagedActionHistoryItems"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEnvironmentManagedActionHistoryResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEnvironmentManagedActionHistoryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEnvironmentManagedActionsResult:
    boto3_raw_data: "type_defs.DescribeEnvironmentManagedActionsResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ManagedActions(self):  # pragma: no cover
        return ManagedAction.make_many(self.boto3_raw_data["ManagedActions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEnvironmentManagedActionsResultTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEnvironmentManagedActionsResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEnvironmentsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeEnvironmentsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    VersionLabel = field("VersionLabel")
    EnvironmentIds = field("EnvironmentIds")
    EnvironmentNames = field("EnvironmentNames")
    IncludeDeleted = field("IncludeDeleted")
    IncludedDeletedBackTo = field("IncludedDeletedBackTo")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEnvironmentsMessagePaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEnvironmentsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEnvironmentsMessage:
    boto3_raw_data: "type_defs.DescribeEnvironmentsMessageTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")
    VersionLabel = field("VersionLabel")
    EnvironmentIds = field("EnvironmentIds")
    EnvironmentNames = field("EnvironmentNames")
    IncludeDeleted = field("IncludeDeleted")
    IncludedDeletedBackTo = field("IncludedDeletedBackTo")
    MaxRecords = field("MaxRecords")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEnvironmentsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEnvironmentsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventsMessagePaginate:
    boto3_raw_data: "type_defs.DescribeEventsMessagePaginateTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    VersionLabel = field("VersionLabel")
    TemplateName = field("TemplateName")
    EnvironmentId = field("EnvironmentId")
    EnvironmentName = field("EnvironmentName")
    PlatformArn = field("PlatformArn")
    RequestId = field("RequestId")
    Severity = field("Severity")
    StartTime = field("StartTime")
    EndTime = field("EndTime")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEventsMessagePaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventsMessagePaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEventsMessage:
    boto3_raw_data: "type_defs.DescribeEventsMessageTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")
    VersionLabel = field("VersionLabel")
    TemplateName = field("TemplateName")
    EnvironmentId = field("EnvironmentId")
    EnvironmentName = field("EnvironmentName")
    PlatformArn = field("PlatformArn")
    RequestId = field("RequestId")
    Severity = field("Severity")
    StartTime = field("StartTime")
    EndTime = field("EndTime")
    MaxRecords = field("MaxRecords")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeEventsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEventsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEnvironmentsMessageWaitExtraExtra:
    boto3_raw_data: "type_defs.DescribeEnvironmentsMessageWaitExtraExtraTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    VersionLabel = field("VersionLabel")
    EnvironmentIds = field("EnvironmentIds")
    EnvironmentNames = field("EnvironmentNames")
    IncludeDeleted = field("IncludeDeleted")
    IncludedDeletedBackTo = field("IncludedDeletedBackTo")
    MaxRecords = field("MaxRecords")
    NextToken = field("NextToken")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEnvironmentsMessageWaitExtraExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEnvironmentsMessageWaitExtraExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEnvironmentsMessageWaitExtra:
    boto3_raw_data: "type_defs.DescribeEnvironmentsMessageWaitExtraTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    VersionLabel = field("VersionLabel")
    EnvironmentIds = field("EnvironmentIds")
    EnvironmentNames = field("EnvironmentNames")
    IncludeDeleted = field("IncludeDeleted")
    IncludedDeletedBackTo = field("IncludedDeletedBackTo")
    MaxRecords = field("MaxRecords")
    NextToken = field("NextToken")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeEnvironmentsMessageWaitExtraTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEnvironmentsMessageWaitExtraTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEnvironmentsMessageWait:
    boto3_raw_data: "type_defs.DescribeEnvironmentsMessageWaitTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")
    VersionLabel = field("VersionLabel")
    EnvironmentIds = field("EnvironmentIds")
    EnvironmentNames = field("EnvironmentNames")
    IncludeDeleted = field("IncludeDeleted")
    IncludedDeletedBackTo = field("IncludedDeletedBackTo")
    MaxRecords = field("MaxRecords")
    NextToken = field("NextToken")

    @cached_property
    def WaiterConfig(self):  # pragma: no cover
        return WaiterConfig.make_one(self.boto3_raw_data["WaiterConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEnvironmentsMessageWaitTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEnvironmentsMessageWaitTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RetrieveEnvironmentInfoResultMessage:
    boto3_raw_data: "type_defs.RetrieveEnvironmentInfoResultMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EnvironmentInfo(self):  # pragma: no cover
        return EnvironmentInfoDescription.make_many(
            self.boto3_raw_data["EnvironmentInfo"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RetrieveEnvironmentInfoResultMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RetrieveEnvironmentInfoResultMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentResourceDescription:
    boto3_raw_data: "type_defs.EnvironmentResourceDescriptionTypeDef" = (
        dataclasses.field()
    )

    EnvironmentName = field("EnvironmentName")

    @cached_property
    def AutoScalingGroups(self):  # pragma: no cover
        return AutoScalingGroup.make_many(self.boto3_raw_data["AutoScalingGroups"])

    @cached_property
    def Instances(self):  # pragma: no cover
        return Instance.make_many(self.boto3_raw_data["Instances"])

    @cached_property
    def LaunchConfigurations(self):  # pragma: no cover
        return LaunchConfiguration.make_many(
            self.boto3_raw_data["LaunchConfigurations"]
        )

    @cached_property
    def LaunchTemplates(self):  # pragma: no cover
        return LaunchTemplate.make_many(self.boto3_raw_data["LaunchTemplates"])

    @cached_property
    def LoadBalancers(self):  # pragma: no cover
        return LoadBalancer.make_many(self.boto3_raw_data["LoadBalancers"])

    @cached_property
    def Triggers(self):  # pragma: no cover
        return Trigger.make_many(self.boto3_raw_data["Triggers"])

    @cached_property
    def Queues(self):  # pragma: no cover
        return Queue.make_many(self.boto3_raw_data["Queues"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EnvironmentResourceDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentResourceDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventDescriptionsMessage:
    boto3_raw_data: "type_defs.EventDescriptionsMessageTypeDef" = dataclasses.field()

    @cached_property
    def Events(self):  # pragma: no cover
        return EventDescription.make_many(self.boto3_raw_data["Events"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventDescriptionsMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventDescriptionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAvailableSolutionStacksResultMessage:
    boto3_raw_data: "type_defs.ListAvailableSolutionStacksResultMessageTypeDef" = (
        dataclasses.field()
    )

    SolutionStacks = field("SolutionStacks")

    @cached_property
    def SolutionStackDetails(self):  # pragma: no cover
        return SolutionStackDescription.make_many(
            self.boto3_raw_data["SolutionStackDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAvailableSolutionStacksResultMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAvailableSolutionStacksResultMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPlatformBranchesRequest:
    boto3_raw_data: "type_defs.ListPlatformBranchesRequestTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return SearchFilter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPlatformBranchesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPlatformBranchesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPlatformBranchesResult:
    boto3_raw_data: "type_defs.ListPlatformBranchesResultTypeDef" = dataclasses.field()

    @cached_property
    def PlatformBranchSummaryList(self):  # pragma: no cover
        return PlatformBranchSummary.make_many(
            self.boto3_raw_data["PlatformBranchSummaryList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPlatformBranchesResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPlatformBranchesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPlatformVersionsRequestPaginate:
    boto3_raw_data: "type_defs.ListPlatformVersionsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filters(self):  # pragma: no cover
        return PlatformFilter.make_many(self.boto3_raw_data["Filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPlatformVersionsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPlatformVersionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPlatformVersionsRequest:
    boto3_raw_data: "type_defs.ListPlatformVersionsRequestTypeDef" = dataclasses.field()

    @cached_property
    def Filters(self):  # pragma: no cover
        return PlatformFilter.make_many(self.boto3_raw_data["Filters"])

    MaxRecords = field("MaxRecords")
    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPlatformVersionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPlatformVersionsRequestTypeDef"]
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
    Domain = field("Domain")

    @cached_property
    def Listeners(self):  # pragma: no cover
        return Listener.make_many(self.boto3_raw_data["Listeners"])

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
class PlatformDescription:
    boto3_raw_data: "type_defs.PlatformDescriptionTypeDef" = dataclasses.field()

    PlatformArn = field("PlatformArn")
    PlatformOwner = field("PlatformOwner")
    PlatformName = field("PlatformName")
    PlatformVersion = field("PlatformVersion")
    SolutionStackName = field("SolutionStackName")
    PlatformStatus = field("PlatformStatus")
    DateCreated = field("DateCreated")
    DateUpdated = field("DateUpdated")
    PlatformCategory = field("PlatformCategory")
    Description = field("Description")
    Maintainer = field("Maintainer")
    OperatingSystemName = field("OperatingSystemName")
    OperatingSystemVersion = field("OperatingSystemVersion")

    @cached_property
    def ProgrammingLanguages(self):  # pragma: no cover
        return PlatformProgrammingLanguage.make_many(
            self.boto3_raw_data["ProgrammingLanguages"]
        )

    @cached_property
    def Frameworks(self):  # pragma: no cover
        return PlatformFramework.make_many(self.boto3_raw_data["Frameworks"])

    @cached_property
    def CustomAmiList(self):  # pragma: no cover
        return CustomAmi.make_many(self.boto3_raw_data["CustomAmiList"])

    SupportedTierList = field("SupportedTierList")
    SupportedAddonList = field("SupportedAddonList")
    PlatformLifecycleState = field("PlatformLifecycleState")
    PlatformBranchName = field("PlatformBranchName")
    PlatformBranchLifecycleState = field("PlatformBranchLifecycleState")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PlatformDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PlatformDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceQuotas:
    boto3_raw_data: "type_defs.ResourceQuotasTypeDef" = dataclasses.field()

    @cached_property
    def ApplicationQuota(self):  # pragma: no cover
        return ResourceQuota.make_one(self.boto3_raw_data["ApplicationQuota"])

    @cached_property
    def ApplicationVersionQuota(self):  # pragma: no cover
        return ResourceQuota.make_one(self.boto3_raw_data["ApplicationVersionQuota"])

    @cached_property
    def EnvironmentQuota(self):  # pragma: no cover
        return ResourceQuota.make_one(self.boto3_raw_data["EnvironmentQuota"])

    @cached_property
    def ConfigurationTemplateQuota(self):  # pragma: no cover
        return ResourceQuota.make_one(self.boto3_raw_data["ConfigurationTemplateQuota"])

    @cached_property
    def CustomPlatformQuota(self):  # pragma: no cover
        return ResourceQuota.make_one(self.boto3_raw_data["CustomPlatformQuota"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceQuotasTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceQuotasTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeEnvironmentHealthResult:
    boto3_raw_data: "type_defs.DescribeEnvironmentHealthResultTypeDef" = (
        dataclasses.field()
    )

    EnvironmentName = field("EnvironmentName")
    HealthStatus = field("HealthStatus")
    Status = field("Status")
    Color = field("Color")
    Causes = field("Causes")

    @cached_property
    def ApplicationMetrics(self):  # pragma: no cover
        return ApplicationMetrics.make_one(self.boto3_raw_data["ApplicationMetrics"])

    @cached_property
    def InstancesHealth(self):  # pragma: no cover
        return InstanceHealthSummary.make_one(self.boto3_raw_data["InstancesHealth"])

    RefreshedAt = field("RefreshedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeEnvironmentHealthResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeEnvironmentHealthResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationVersionDescriptionMessage:
    boto3_raw_data: "type_defs.ApplicationVersionDescriptionMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ApplicationVersion(self):  # pragma: no cover
        return ApplicationVersionDescription.make_one(
            self.boto3_raw_data["ApplicationVersion"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplicationVersionDescriptionMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationVersionDescriptionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationVersionDescriptionsMessage:
    boto3_raw_data: "type_defs.ApplicationVersionDescriptionsMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ApplicationVersions(self):  # pragma: no cover
        return ApplicationVersionDescription.make_many(
            self.boto3_raw_data["ApplicationVersions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplicationVersionDescriptionsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationVersionDescriptionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationResourceLifecycleConfig:
    boto3_raw_data: "type_defs.ApplicationResourceLifecycleConfigTypeDef" = (
        dataclasses.field()
    )

    ServiceRole = field("ServiceRole")

    @cached_property
    def VersionLifecycleConfig(self):  # pragma: no cover
        return ApplicationVersionLifecycleConfig.make_one(
            self.boto3_raw_data["VersionLifecycleConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplicationResourceLifecycleConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationResourceLifecycleConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SingleInstanceHealth:
    boto3_raw_data: "type_defs.SingleInstanceHealthTypeDef" = dataclasses.field()

    InstanceId = field("InstanceId")
    HealthStatus = field("HealthStatus")
    Color = field("Color")
    Causes = field("Causes")
    LaunchedAt = field("LaunchedAt")

    @cached_property
    def ApplicationMetrics(self):  # pragma: no cover
        return ApplicationMetrics.make_one(self.boto3_raw_data["ApplicationMetrics"])

    @cached_property
    def System(self):  # pragma: no cover
        return SystemStatus.make_one(self.boto3_raw_data["System"])

    @cached_property
    def Deployment(self):  # pragma: no cover
        return Deployment.make_one(self.boto3_raw_data["Deployment"])

    AvailabilityZone = field("AvailabilityZone")
    InstanceType = field("InstanceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SingleInstanceHealthTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SingleInstanceHealthTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationOptionsDescription:
    boto3_raw_data: "type_defs.ConfigurationOptionsDescriptionTypeDef" = (
        dataclasses.field()
    )

    SolutionStackName = field("SolutionStackName")
    PlatformArn = field("PlatformArn")

    @cached_property
    def Options(self):  # pragma: no cover
        return ConfigurationOptionDescription.make_many(self.boto3_raw_data["Options"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConfigurationOptionsDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationOptionsDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationSettingsDescriptions:
    boto3_raw_data: "type_defs.ConfigurationSettingsDescriptionsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ConfigurationSettings(self):  # pragma: no cover
        return ConfigurationSettingsDescription.make_many(
            self.boto3_raw_data["ConfigurationSettings"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfigurationSettingsDescriptionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationSettingsDescriptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentResourceDescriptionsMessage:
    boto3_raw_data: "type_defs.EnvironmentResourceDescriptionsMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def EnvironmentResources(self):  # pragma: no cover
        return EnvironmentResourceDescription.make_one(
            self.boto3_raw_data["EnvironmentResources"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnvironmentResourceDescriptionsMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentResourceDescriptionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentResourcesDescription:
    boto3_raw_data: "type_defs.EnvironmentResourcesDescriptionTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def LoadBalancer(self):  # pragma: no cover
        return LoadBalancerDescription.make_one(self.boto3_raw_data["LoadBalancer"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EnvironmentResourcesDescriptionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentResourcesDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribePlatformVersionResult:
    boto3_raw_data: "type_defs.DescribePlatformVersionResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PlatformDescription(self):  # pragma: no cover
        return PlatformDescription.make_one(self.boto3_raw_data["PlatformDescription"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribePlatformVersionResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribePlatformVersionResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountAttributesResult:
    boto3_raw_data: "type_defs.DescribeAccountAttributesResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ResourceQuotas(self):  # pragma: no cover
        return ResourceQuotas.make_one(self.boto3_raw_data["ResourceQuotas"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAccountAttributesResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountAttributesResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationDescription:
    boto3_raw_data: "type_defs.ApplicationDescriptionTypeDef" = dataclasses.field()

    ApplicationArn = field("ApplicationArn")
    ApplicationName = field("ApplicationName")
    Description = field("Description")
    DateCreated = field("DateCreated")
    DateUpdated = field("DateUpdated")
    Versions = field("Versions")
    ConfigurationTemplates = field("ConfigurationTemplates")

    @cached_property
    def ResourceLifecycleConfig(self):  # pragma: no cover
        return ApplicationResourceLifecycleConfig.make_one(
            self.boto3_raw_data["ResourceLifecycleConfig"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ApplicationDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationResourceLifecycleDescriptionMessage:
    boto3_raw_data: (
        "type_defs.ApplicationResourceLifecycleDescriptionMessageTypeDef"
    ) = dataclasses.field()

    ApplicationName = field("ApplicationName")

    @cached_property
    def ResourceLifecycleConfig(self):  # pragma: no cover
        return ApplicationResourceLifecycleConfig.make_one(
            self.boto3_raw_data["ResourceLifecycleConfig"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ApplicationResourceLifecycleDescriptionMessageTypeDef"
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
                "type_defs.ApplicationResourceLifecycleDescriptionMessageTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateApplicationMessage:
    boto3_raw_data: "type_defs.CreateApplicationMessageTypeDef" = dataclasses.field()

    ApplicationName = field("ApplicationName")
    Description = field("Description")

    @cached_property
    def ResourceLifecycleConfig(self):  # pragma: no cover
        return ApplicationResourceLifecycleConfig.make_one(
            self.boto3_raw_data["ResourceLifecycleConfig"]
        )

    @cached_property
    def Tags(self):  # pragma: no cover
        return Tag.make_many(self.boto3_raw_data["Tags"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateApplicationMessageTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateApplicationMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateApplicationResourceLifecycleMessage:
    boto3_raw_data: "type_defs.UpdateApplicationResourceLifecycleMessageTypeDef" = (
        dataclasses.field()
    )

    ApplicationName = field("ApplicationName")

    @cached_property
    def ResourceLifecycleConfig(self):  # pragma: no cover
        return ApplicationResourceLifecycleConfig.make_one(
            self.boto3_raw_data["ResourceLifecycleConfig"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateApplicationResourceLifecycleMessageTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateApplicationResourceLifecycleMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeInstancesHealthResult:
    boto3_raw_data: "type_defs.DescribeInstancesHealthResultTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def InstanceHealthList(self):  # pragma: no cover
        return SingleInstanceHealth.make_many(self.boto3_raw_data["InstanceHealthList"])

    RefreshedAt = field("RefreshedAt")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeInstancesHealthResultTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeInstancesHealthResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentDescriptionResponse:
    boto3_raw_data: "type_defs.EnvironmentDescriptionResponseTypeDef" = (
        dataclasses.field()
    )

    EnvironmentName = field("EnvironmentName")
    EnvironmentId = field("EnvironmentId")
    ApplicationName = field("ApplicationName")
    VersionLabel = field("VersionLabel")
    SolutionStackName = field("SolutionStackName")
    PlatformArn = field("PlatformArn")
    TemplateName = field("TemplateName")
    Description = field("Description")
    EndpointURL = field("EndpointURL")
    CNAME = field("CNAME")
    DateCreated = field("DateCreated")
    DateUpdated = field("DateUpdated")
    Status = field("Status")
    AbortableOperationInProgress = field("AbortableOperationInProgress")
    Health = field("Health")
    HealthStatus = field("HealthStatus")

    @cached_property
    def Resources(self):  # pragma: no cover
        return EnvironmentResourcesDescription.make_one(
            self.boto3_raw_data["Resources"]
        )

    @cached_property
    def Tier(self):  # pragma: no cover
        return EnvironmentTier.make_one(self.boto3_raw_data["Tier"])

    @cached_property
    def EnvironmentLinks(self):  # pragma: no cover
        return EnvironmentLink.make_many(self.boto3_raw_data["EnvironmentLinks"])

    EnvironmentArn = field("EnvironmentArn")
    OperationsRole = field("OperationsRole")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EnvironmentDescriptionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentDescriptionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentDescription:
    boto3_raw_data: "type_defs.EnvironmentDescriptionTypeDef" = dataclasses.field()

    EnvironmentName = field("EnvironmentName")
    EnvironmentId = field("EnvironmentId")
    ApplicationName = field("ApplicationName")
    VersionLabel = field("VersionLabel")
    SolutionStackName = field("SolutionStackName")
    PlatformArn = field("PlatformArn")
    TemplateName = field("TemplateName")
    Description = field("Description")
    EndpointURL = field("EndpointURL")
    CNAME = field("CNAME")
    DateCreated = field("DateCreated")
    DateUpdated = field("DateUpdated")
    Status = field("Status")
    AbortableOperationInProgress = field("AbortableOperationInProgress")
    Health = field("Health")
    HealthStatus = field("HealthStatus")

    @cached_property
    def Resources(self):  # pragma: no cover
        return EnvironmentResourcesDescription.make_one(
            self.boto3_raw_data["Resources"]
        )

    @cached_property
    def Tier(self):  # pragma: no cover
        return EnvironmentTier.make_one(self.boto3_raw_data["Tier"])

    @cached_property
    def EnvironmentLinks(self):  # pragma: no cover
        return EnvironmentLink.make_many(self.boto3_raw_data["EnvironmentLinks"])

    EnvironmentArn = field("EnvironmentArn")
    OperationsRole = field("OperationsRole")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EnvironmentDescriptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentDescriptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationDescriptionMessage:
    boto3_raw_data: "type_defs.ApplicationDescriptionMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Application(self):  # pragma: no cover
        return ApplicationDescription.make_one(self.boto3_raw_data["Application"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ApplicationDescriptionMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationDescriptionMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ApplicationDescriptionsMessage:
    boto3_raw_data: "type_defs.ApplicationDescriptionsMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Applications(self):  # pragma: no cover
        return ApplicationDescription.make_many(self.boto3_raw_data["Applications"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ApplicationDescriptionsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ApplicationDescriptionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnvironmentDescriptionsMessage:
    boto3_raw_data: "type_defs.EnvironmentDescriptionsMessageTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Environments(self):  # pragma: no cover
        return EnvironmentDescription.make_many(self.boto3_raw_data["Environments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EnvironmentDescriptionsMessageTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnvironmentDescriptionsMessageTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
