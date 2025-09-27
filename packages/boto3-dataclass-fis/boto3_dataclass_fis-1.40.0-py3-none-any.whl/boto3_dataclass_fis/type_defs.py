# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_fis import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class ActionParameter:
    boto3_raw_data: "type_defs.ActionParameterTypeDef" = dataclasses.field()

    description = field("description")
    required = field("required")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionParameterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionParameterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionTarget:
    boto3_raw_data: "type_defs.ActionTargetTypeDef" = dataclasses.field()

    resourceType = field("resourceType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionTargetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateExperimentTemplateActionInput:
    boto3_raw_data: "type_defs.CreateExperimentTemplateActionInputTypeDef" = (
        dataclasses.field()
    )

    actionId = field("actionId")
    description = field("description")
    parameters = field("parameters")
    targets = field("targets")
    startAfter = field("startAfter")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateExperimentTemplateActionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExperimentTemplateActionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateExperimentTemplateExperimentOptionsInput:
    boto3_raw_data: (
        "type_defs.CreateExperimentTemplateExperimentOptionsInputTypeDef"
    ) = dataclasses.field()

    accountTargeting = field("accountTargeting")
    emptyTargetResolutionMode = field("emptyTargetResolutionMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateExperimentTemplateExperimentOptionsInputTypeDef"
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
                "type_defs.CreateExperimentTemplateExperimentOptionsInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentTemplateCloudWatchLogsLogConfigurationInput:
    boto3_raw_data: (
        "type_defs.ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef"
    ) = dataclasses.field()

    logGroupArn = field("logGroupArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef"
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
                "type_defs.ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentTemplateS3LogConfigurationInput:
    boto3_raw_data: "type_defs.ExperimentTemplateS3LogConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    bucketName = field("bucketName")
    prefix = field("prefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExperimentTemplateS3LogConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentTemplateS3LogConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateExperimentTemplateStopConditionInput:
    boto3_raw_data: "type_defs.CreateExperimentTemplateStopConditionInputTypeDef" = (
        dataclasses.field()
    )

    source = field("source")
    value = field("value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateExperimentTemplateStopConditionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExperimentTemplateStopConditionInputTypeDef"]
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
class ExperimentTemplateTargetInputFilter:
    boto3_raw_data: "type_defs.ExperimentTemplateTargetInputFilterTypeDef" = (
        dataclasses.field()
    )

    path = field("path")
    values = field("values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExperimentTemplateTargetInputFilterTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentTemplateTargetInputFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTargetAccountConfigurationRequest:
    boto3_raw_data: "type_defs.CreateTargetAccountConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    experimentTemplateId = field("experimentTemplateId")
    accountId = field("accountId")
    roleArn = field("roleArn")
    clientToken = field("clientToken")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateTargetAccountConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTargetAccountConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetAccountConfiguration:
    boto3_raw_data: "type_defs.TargetAccountConfigurationTypeDef" = dataclasses.field()

    roleArn = field("roleArn")
    accountId = field("accountId")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetAccountConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetAccountConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteExperimentTemplateRequest:
    boto3_raw_data: "type_defs.DeleteExperimentTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteExperimentTemplateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteExperimentTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTargetAccountConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteTargetAccountConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    experimentTemplateId = field("experimentTemplateId")
    accountId = field("accountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteTargetAccountConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTargetAccountConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentActionState:
    boto3_raw_data: "type_defs.ExperimentActionStateTypeDef" = dataclasses.field()

    status = field("status")
    reason = field("reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExperimentActionStateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentActionStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentCloudWatchLogsLogConfiguration:
    boto3_raw_data: "type_defs.ExperimentCloudWatchLogsLogConfigurationTypeDef" = (
        dataclasses.field()
    )

    logGroupArn = field("logGroupArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExperimentCloudWatchLogsLogConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentCloudWatchLogsLogConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentError:
    boto3_raw_data: "type_defs.ExperimentErrorTypeDef" = dataclasses.field()

    accountId = field("accountId")
    code = field("code")
    location = field("location")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExperimentErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExperimentErrorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentS3LogConfiguration:
    boto3_raw_data: "type_defs.ExperimentS3LogConfigurationTypeDef" = (
        dataclasses.field()
    )

    bucketName = field("bucketName")
    prefix = field("prefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExperimentS3LogConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentS3LogConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentOptions:
    boto3_raw_data: "type_defs.ExperimentOptionsTypeDef" = dataclasses.field()

    accountTargeting = field("accountTargeting")
    emptyTargetResolutionMode = field("emptyTargetResolutionMode")
    actionsMode = field("actionsMode")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExperimentOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentReportConfigurationCloudWatchDashboard:
    boto3_raw_data: (
        "type_defs.ExperimentReportConfigurationCloudWatchDashboardTypeDef"
    ) = dataclasses.field()

    dashboardIdentifier = field("dashboardIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExperimentReportConfigurationCloudWatchDashboardTypeDef"
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
                "type_defs.ExperimentReportConfigurationCloudWatchDashboardTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentReportConfigurationOutputsS3Configuration:
    boto3_raw_data: (
        "type_defs.ExperimentReportConfigurationOutputsS3ConfigurationTypeDef"
    ) = dataclasses.field()

    bucketName = field("bucketName")
    prefix = field("prefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExperimentReportConfigurationOutputsS3ConfigurationTypeDef"
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
                "type_defs.ExperimentReportConfigurationOutputsS3ConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentReportError:
    boto3_raw_data: "type_defs.ExperimentReportErrorTypeDef" = dataclasses.field()

    code = field("code")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExperimentReportErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentReportErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentReportS3Report:
    boto3_raw_data: "type_defs.ExperimentReportS3ReportTypeDef" = dataclasses.field()

    arn = field("arn")
    reportType = field("reportType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExperimentReportS3ReportTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentReportS3ReportTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentStopCondition:
    boto3_raw_data: "type_defs.ExperimentStopConditionTypeDef" = dataclasses.field()

    source = field("source")
    value = field("value")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExperimentStopConditionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentStopConditionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentTargetAccountConfigurationSummary:
    boto3_raw_data: "type_defs.ExperimentTargetAccountConfigurationSummaryTypeDef" = (
        dataclasses.field()
    )

    roleArn = field("roleArn")
    accountId = field("accountId")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExperimentTargetAccountConfigurationSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentTargetAccountConfigurationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentTargetAccountConfiguration:
    boto3_raw_data: "type_defs.ExperimentTargetAccountConfigurationTypeDef" = (
        dataclasses.field()
    )

    roleArn = field("roleArn")
    accountId = field("accountId")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExperimentTargetAccountConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentTargetAccountConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentTargetFilter:
    boto3_raw_data: "type_defs.ExperimentTargetFilterTypeDef" = dataclasses.field()

    path = field("path")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExperimentTargetFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentTargetFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentTemplateAction:
    boto3_raw_data: "type_defs.ExperimentTemplateActionTypeDef" = dataclasses.field()

    actionId = field("actionId")
    description = field("description")
    parameters = field("parameters")
    targets = field("targets")
    startAfter = field("startAfter")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExperimentTemplateActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentTemplateActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentTemplateCloudWatchLogsLogConfiguration:
    boto3_raw_data: (
        "type_defs.ExperimentTemplateCloudWatchLogsLogConfigurationTypeDef"
    ) = dataclasses.field()

    logGroupArn = field("logGroupArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExperimentTemplateCloudWatchLogsLogConfigurationTypeDef"
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
                "type_defs.ExperimentTemplateCloudWatchLogsLogConfigurationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentTemplateExperimentOptions:
    boto3_raw_data: "type_defs.ExperimentTemplateExperimentOptionsTypeDef" = (
        dataclasses.field()
    )

    accountTargeting = field("accountTargeting")
    emptyTargetResolutionMode = field("emptyTargetResolutionMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExperimentTemplateExperimentOptionsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentTemplateExperimentOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentTemplateS3LogConfiguration:
    boto3_raw_data: "type_defs.ExperimentTemplateS3LogConfigurationTypeDef" = (
        dataclasses.field()
    )

    bucketName = field("bucketName")
    prefix = field("prefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExperimentTemplateS3LogConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentTemplateS3LogConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentTemplateReportConfigurationCloudWatchDashboard:
    boto3_raw_data: (
        "type_defs.ExperimentTemplateReportConfigurationCloudWatchDashboardTypeDef"
    ) = dataclasses.field()

    dashboardIdentifier = field("dashboardIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExperimentTemplateReportConfigurationCloudWatchDashboardTypeDef"
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
                "type_defs.ExperimentTemplateReportConfigurationCloudWatchDashboardTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportConfigurationCloudWatchDashboardInput:
    boto3_raw_data: "type_defs.ReportConfigurationCloudWatchDashboardInputTypeDef" = (
        dataclasses.field()
    )

    dashboardIdentifier = field("dashboardIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ReportConfigurationCloudWatchDashboardInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReportConfigurationCloudWatchDashboardInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportConfigurationS3OutputInput:
    boto3_raw_data: "type_defs.ReportConfigurationS3OutputInputTypeDef" = (
        dataclasses.field()
    )

    bucketName = field("bucketName")
    prefix = field("prefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ReportConfigurationS3OutputInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReportConfigurationS3OutputInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReportConfigurationS3Output:
    boto3_raw_data: "type_defs.ReportConfigurationS3OutputTypeDef" = dataclasses.field()

    bucketName = field("bucketName")
    prefix = field("prefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReportConfigurationS3OutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReportConfigurationS3OutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentTemplateStopCondition:
    boto3_raw_data: "type_defs.ExperimentTemplateStopConditionTypeDef" = (
        dataclasses.field()
    )

    source = field("source")
    value = field("value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExperimentTemplateStopConditionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentTemplateStopConditionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentTemplateSummary:
    boto3_raw_data: "type_defs.ExperimentTemplateSummaryTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    description = field("description")
    creationTime = field("creationTime")
    lastUpdateTime = field("lastUpdateTime")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExperimentTemplateSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentTemplateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentTemplateTargetFilter:
    boto3_raw_data: "type_defs.ExperimentTemplateTargetFilterTypeDef" = (
        dataclasses.field()
    )

    path = field("path")
    values = field("values")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExperimentTemplateTargetFilterTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentTemplateTargetFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetActionRequest:
    boto3_raw_data: "type_defs.GetActionRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetActionRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetActionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExperimentRequest:
    boto3_raw_data: "type_defs.GetExperimentRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExperimentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExperimentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExperimentTargetAccountConfigurationRequest:
    boto3_raw_data: (
        "type_defs.GetExperimentTargetAccountConfigurationRequestTypeDef"
    ) = dataclasses.field()

    experimentId = field("experimentId")
    accountId = field("accountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetExperimentTargetAccountConfigurationRequestTypeDef"
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
                "type_defs.GetExperimentTargetAccountConfigurationRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExperimentTemplateRequest:
    boto3_raw_data: "type_defs.GetExperimentTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExperimentTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExperimentTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSafetyLeverRequest:
    boto3_raw_data: "type_defs.GetSafetyLeverRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSafetyLeverRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSafetyLeverRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTargetAccountConfigurationRequest:
    boto3_raw_data: "type_defs.GetTargetAccountConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    experimentTemplateId = field("experimentTemplateId")
    accountId = field("accountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTargetAccountConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTargetAccountConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTargetResourceTypeRequest:
    boto3_raw_data: "type_defs.GetTargetResourceTypeRequestTypeDef" = (
        dataclasses.field()
    )

    resourceType = field("resourceType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTargetResourceTypeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTargetResourceTypeRequestTypeDef"]
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
class ListActionsRequest:
    boto3_raw_data: "type_defs.ListActionsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListActionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListActionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExperimentResolvedTargetsRequest:
    boto3_raw_data: "type_defs.ListExperimentResolvedTargetsRequestTypeDef" = (
        dataclasses.field()
    )

    experimentId = field("experimentId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    targetName = field("targetName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListExperimentResolvedTargetsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExperimentResolvedTargetsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResolvedTarget:
    boto3_raw_data: "type_defs.ResolvedTargetTypeDef" = dataclasses.field()

    resourceType = field("resourceType")
    targetName = field("targetName")
    targetInformation = field("targetInformation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResolvedTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResolvedTargetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExperimentTargetAccountConfigurationsRequest:
    boto3_raw_data: (
        "type_defs.ListExperimentTargetAccountConfigurationsRequestTypeDef"
    ) = dataclasses.field()

    experimentId = field("experimentId")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListExperimentTargetAccountConfigurationsRequestTypeDef"
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
                "type_defs.ListExperimentTargetAccountConfigurationsRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExperimentTemplatesRequest:
    boto3_raw_data: "type_defs.ListExperimentTemplatesRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListExperimentTemplatesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExperimentTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExperimentsRequest:
    boto3_raw_data: "type_defs.ListExperimentsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    experimentTemplateId = field("experimentTemplateId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExperimentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExperimentsRequestTypeDef"]
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
class ListTargetAccountConfigurationsRequest:
    boto3_raw_data: "type_defs.ListTargetAccountConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    experimentTemplateId = field("experimentTemplateId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTargetAccountConfigurationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTargetAccountConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetAccountConfigurationSummary:
    boto3_raw_data: "type_defs.TargetAccountConfigurationSummaryTypeDef" = (
        dataclasses.field()
    )

    roleArn = field("roleArn")
    accountId = field("accountId")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.TargetAccountConfigurationSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetAccountConfigurationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTargetResourceTypesRequest:
    boto3_raw_data: "type_defs.ListTargetResourceTypesRequestTypeDef" = (
        dataclasses.field()
    )

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTargetResourceTypesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTargetResourceTypesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetResourceTypeSummary:
    boto3_raw_data: "type_defs.TargetResourceTypeSummaryTypeDef" = dataclasses.field()

    resourceType = field("resourceType")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetResourceTypeSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetResourceTypeSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SafetyLeverState:
    boto3_raw_data: "type_defs.SafetyLeverStateTypeDef" = dataclasses.field()

    status = field("status")
    reason = field("reason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SafetyLeverStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SafetyLeverStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartExperimentExperimentOptionsInput:
    boto3_raw_data: "type_defs.StartExperimentExperimentOptionsInputTypeDef" = (
        dataclasses.field()
    )

    actionsMode = field("actionsMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartExperimentExperimentOptionsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartExperimentExperimentOptionsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopExperimentRequest:
    boto3_raw_data: "type_defs.StopExperimentRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopExperimentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopExperimentRequestTypeDef"]
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
class TargetResourceTypeParameter:
    boto3_raw_data: "type_defs.TargetResourceTypeParameterTypeDef" = dataclasses.field()

    description = field("description")
    required = field("required")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetResourceTypeParameterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetResourceTypeParameterTypeDef"]
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
class UpdateExperimentTemplateActionInputItem:
    boto3_raw_data: "type_defs.UpdateExperimentTemplateActionInputItemTypeDef" = (
        dataclasses.field()
    )

    actionId = field("actionId")
    description = field("description")
    parameters = field("parameters")
    targets = field("targets")
    startAfter = field("startAfter")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateExperimentTemplateActionInputItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateExperimentTemplateActionInputItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateExperimentTemplateExperimentOptionsInput:
    boto3_raw_data: (
        "type_defs.UpdateExperimentTemplateExperimentOptionsInputTypeDef"
    ) = dataclasses.field()

    emptyTargetResolutionMode = field("emptyTargetResolutionMode")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateExperimentTemplateExperimentOptionsInputTypeDef"
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
                "type_defs.UpdateExperimentTemplateExperimentOptionsInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateExperimentTemplateStopConditionInput:
    boto3_raw_data: "type_defs.UpdateExperimentTemplateStopConditionInputTypeDef" = (
        dataclasses.field()
    )

    source = field("source")
    value = field("value")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateExperimentTemplateStopConditionInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateExperimentTemplateStopConditionInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSafetyLeverStateInput:
    boto3_raw_data: "type_defs.UpdateSafetyLeverStateInputTypeDef" = dataclasses.field()

    status = field("status")
    reason = field("reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSafetyLeverStateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSafetyLeverStateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTargetAccountConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateTargetAccountConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    experimentTemplateId = field("experimentTemplateId")
    accountId = field("accountId")
    roleArn = field("roleArn")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateTargetAccountConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTargetAccountConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ActionSummary:
    boto3_raw_data: "type_defs.ActionSummaryTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    description = field("description")
    targets = field("targets")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ActionSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ActionSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Action:
    boto3_raw_data: "type_defs.ActionTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    description = field("description")
    parameters = field("parameters")
    targets = field("targets")
    tags = field("tags")

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
class CreateExperimentTemplateLogConfigurationInput:
    boto3_raw_data: "type_defs.CreateExperimentTemplateLogConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    logSchemaVersion = field("logSchemaVersion")

    @cached_property
    def cloudWatchLogsConfiguration(self):  # pragma: no cover
        return ExperimentTemplateCloudWatchLogsLogConfigurationInput.make_one(
            self.boto3_raw_data["cloudWatchLogsConfiguration"]
        )

    @cached_property
    def s3Configuration(self):  # pragma: no cover
        return ExperimentTemplateS3LogConfigurationInput.make_one(
            self.boto3_raw_data["s3Configuration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateExperimentTemplateLogConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExperimentTemplateLogConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateExperimentTemplateLogConfigurationInput:
    boto3_raw_data: "type_defs.UpdateExperimentTemplateLogConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def cloudWatchLogsConfiguration(self):  # pragma: no cover
        return ExperimentTemplateCloudWatchLogsLogConfigurationInput.make_one(
            self.boto3_raw_data["cloudWatchLogsConfiguration"]
        )

    @cached_property
    def s3Configuration(self):  # pragma: no cover
        return ExperimentTemplateS3LogConfigurationInput.make_one(
            self.boto3_raw_data["s3Configuration"]
        )

    logSchemaVersion = field("logSchemaVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateExperimentTemplateLogConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateExperimentTemplateLogConfigurationInputTypeDef"]
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
class CreateExperimentTemplateTargetInput:
    boto3_raw_data: "type_defs.CreateExperimentTemplateTargetInputTypeDef" = (
        dataclasses.field()
    )

    resourceType = field("resourceType")
    selectionMode = field("selectionMode")
    resourceArns = field("resourceArns")
    resourceTags = field("resourceTags")

    @cached_property
    def filters(self):  # pragma: no cover
        return ExperimentTemplateTargetInputFilter.make_many(
            self.boto3_raw_data["filters"]
        )

    parameters = field("parameters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateExperimentTemplateTargetInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExperimentTemplateTargetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateExperimentTemplateTargetInput:
    boto3_raw_data: "type_defs.UpdateExperimentTemplateTargetInputTypeDef" = (
        dataclasses.field()
    )

    resourceType = field("resourceType")
    selectionMode = field("selectionMode")
    resourceArns = field("resourceArns")
    resourceTags = field("resourceTags")

    @cached_property
    def filters(self):  # pragma: no cover
        return ExperimentTemplateTargetInputFilter.make_many(
            self.boto3_raw_data["filters"]
        )

    parameters = field("parameters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateExperimentTemplateTargetInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateExperimentTemplateTargetInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTargetAccountConfigurationResponse:
    boto3_raw_data: "type_defs.CreateTargetAccountConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def targetAccountConfiguration(self):  # pragma: no cover
        return TargetAccountConfiguration.make_one(
            self.boto3_raw_data["targetAccountConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateTargetAccountConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTargetAccountConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTargetAccountConfigurationResponse:
    boto3_raw_data: "type_defs.DeleteTargetAccountConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def targetAccountConfiguration(self):  # pragma: no cover
        return TargetAccountConfiguration.make_one(
            self.boto3_raw_data["targetAccountConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteTargetAccountConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTargetAccountConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTargetAccountConfigurationResponse:
    boto3_raw_data: "type_defs.GetTargetAccountConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def targetAccountConfiguration(self):  # pragma: no cover
        return TargetAccountConfiguration.make_one(
            self.boto3_raw_data["targetAccountConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetTargetAccountConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTargetAccountConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTargetAccountConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateTargetAccountConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def targetAccountConfiguration(self):  # pragma: no cover
        return TargetAccountConfiguration.make_one(
            self.boto3_raw_data["targetAccountConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateTargetAccountConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTargetAccountConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentAction:
    boto3_raw_data: "type_defs.ExperimentActionTypeDef" = dataclasses.field()

    actionId = field("actionId")
    description = field("description")
    parameters = field("parameters")
    targets = field("targets")
    startAfter = field("startAfter")

    @cached_property
    def state(self):  # pragma: no cover
        return ExperimentActionState.make_one(self.boto3_raw_data["state"])

    startTime = field("startTime")
    endTime = field("endTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExperimentActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentState:
    boto3_raw_data: "type_defs.ExperimentStateTypeDef" = dataclasses.field()

    status = field("status")
    reason = field("reason")

    @cached_property
    def error(self):  # pragma: no cover
        return ExperimentError.make_one(self.boto3_raw_data["error"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExperimentStateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExperimentStateTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentLogConfiguration:
    boto3_raw_data: "type_defs.ExperimentLogConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def cloudWatchLogsConfiguration(self):  # pragma: no cover
        return ExperimentCloudWatchLogsLogConfiguration.make_one(
            self.boto3_raw_data["cloudWatchLogsConfiguration"]
        )

    @cached_property
    def s3Configuration(self):  # pragma: no cover
        return ExperimentS3LogConfiguration.make_one(
            self.boto3_raw_data["s3Configuration"]
        )

    logSchemaVersion = field("logSchemaVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExperimentLogConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentLogConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentReportConfigurationDataSources:
    boto3_raw_data: "type_defs.ExperimentReportConfigurationDataSourcesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def cloudWatchDashboards(self):  # pragma: no cover
        return ExperimentReportConfigurationCloudWatchDashboard.make_many(
            self.boto3_raw_data["cloudWatchDashboards"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExperimentReportConfigurationDataSourcesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentReportConfigurationDataSourcesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentReportConfigurationOutputs:
    boto3_raw_data: "type_defs.ExperimentReportConfigurationOutputsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def s3Configuration(self):  # pragma: no cover
        return ExperimentReportConfigurationOutputsS3Configuration.make_one(
            self.boto3_raw_data["s3Configuration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExperimentReportConfigurationOutputsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentReportConfigurationOutputsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentReportState:
    boto3_raw_data: "type_defs.ExperimentReportStateTypeDef" = dataclasses.field()

    status = field("status")
    reason = field("reason")

    @cached_property
    def error(self):  # pragma: no cover
        return ExperimentReportError.make_one(self.boto3_raw_data["error"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExperimentReportStateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentReportStateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExperimentTargetAccountConfigurationsResponse:
    boto3_raw_data: (
        "type_defs.ListExperimentTargetAccountConfigurationsResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def targetAccountConfigurations(self):  # pragma: no cover
        return ExperimentTargetAccountConfigurationSummary.make_many(
            self.boto3_raw_data["targetAccountConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListExperimentTargetAccountConfigurationsResponseTypeDef"
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
                "type_defs.ListExperimentTargetAccountConfigurationsResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExperimentTargetAccountConfigurationResponse:
    boto3_raw_data: (
        "type_defs.GetExperimentTargetAccountConfigurationResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def targetAccountConfiguration(self):  # pragma: no cover
        return ExperimentTargetAccountConfiguration.make_one(
            self.boto3_raw_data["targetAccountConfiguration"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetExperimentTargetAccountConfigurationResponseTypeDef"
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
                "type_defs.GetExperimentTargetAccountConfigurationResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentTarget:
    boto3_raw_data: "type_defs.ExperimentTargetTypeDef" = dataclasses.field()

    resourceType = field("resourceType")
    resourceArns = field("resourceArns")
    resourceTags = field("resourceTags")

    @cached_property
    def filters(self):  # pragma: no cover
        return ExperimentTargetFilter.make_many(self.boto3_raw_data["filters"])

    selectionMode = field("selectionMode")
    parameters = field("parameters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExperimentTargetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentTemplateLogConfiguration:
    boto3_raw_data: "type_defs.ExperimentTemplateLogConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def cloudWatchLogsConfiguration(self):  # pragma: no cover
        return ExperimentTemplateCloudWatchLogsLogConfiguration.make_one(
            self.boto3_raw_data["cloudWatchLogsConfiguration"]
        )

    @cached_property
    def s3Configuration(self):  # pragma: no cover
        return ExperimentTemplateS3LogConfiguration.make_one(
            self.boto3_raw_data["s3Configuration"]
        )

    logSchemaVersion = field("logSchemaVersion")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExperimentTemplateLogConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentTemplateLogConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentTemplateReportConfigurationDataSources:
    boto3_raw_data: (
        "type_defs.ExperimentTemplateReportConfigurationDataSourcesTypeDef"
    ) = dataclasses.field()

    @cached_property
    def cloudWatchDashboards(self):  # pragma: no cover
        return ExperimentTemplateReportConfigurationCloudWatchDashboard.make_many(
            self.boto3_raw_data["cloudWatchDashboards"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExperimentTemplateReportConfigurationDataSourcesTypeDef"
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
                "type_defs.ExperimentTemplateReportConfigurationDataSourcesTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentTemplateReportConfigurationDataSourcesInput:
    boto3_raw_data: (
        "type_defs.ExperimentTemplateReportConfigurationDataSourcesInputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def cloudWatchDashboards(self):  # pragma: no cover
        return ReportConfigurationCloudWatchDashboardInput.make_many(
            self.boto3_raw_data["cloudWatchDashboards"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExperimentTemplateReportConfigurationDataSourcesInputTypeDef"
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
                "type_defs.ExperimentTemplateReportConfigurationDataSourcesInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentTemplateReportConfigurationOutputsInput:
    boto3_raw_data: (
        "type_defs.ExperimentTemplateReportConfigurationOutputsInputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def s3Configuration(self):  # pragma: no cover
        return ReportConfigurationS3OutputInput.make_one(
            self.boto3_raw_data["s3Configuration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExperimentTemplateReportConfigurationOutputsInputTypeDef"
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
                "type_defs.ExperimentTemplateReportConfigurationOutputsInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentTemplateReportConfigurationOutputs:
    boto3_raw_data: "type_defs.ExperimentTemplateReportConfigurationOutputsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def s3Configuration(self):  # pragma: no cover
        return ReportConfigurationS3Output.make_one(
            self.boto3_raw_data["s3Configuration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExperimentTemplateReportConfigurationOutputsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentTemplateReportConfigurationOutputsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExperimentTemplatesResponse:
    boto3_raw_data: "type_defs.ListExperimentTemplatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def experimentTemplates(self):  # pragma: no cover
        return ExperimentTemplateSummary.make_many(
            self.boto3_raw_data["experimentTemplates"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListExperimentTemplatesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExperimentTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentTemplateTarget:
    boto3_raw_data: "type_defs.ExperimentTemplateTargetTypeDef" = dataclasses.field()

    resourceType = field("resourceType")
    resourceArns = field("resourceArns")
    resourceTags = field("resourceTags")

    @cached_property
    def filters(self):  # pragma: no cover
        return ExperimentTemplateTargetFilter.make_many(self.boto3_raw_data["filters"])

    selectionMode = field("selectionMode")
    parameters = field("parameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExperimentTemplateTargetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentTemplateTargetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListActionsRequestPaginate:
    boto3_raw_data: "type_defs.ListActionsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListActionsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListActionsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExperimentResolvedTargetsRequestPaginate:
    boto3_raw_data: "type_defs.ListExperimentResolvedTargetsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    experimentId = field("experimentId")
    targetName = field("targetName")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListExperimentResolvedTargetsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExperimentResolvedTargetsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExperimentTemplatesRequestPaginate:
    boto3_raw_data: "type_defs.ListExperimentTemplatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListExperimentTemplatesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExperimentTemplatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExperimentsRequestPaginate:
    boto3_raw_data: "type_defs.ListExperimentsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    experimentTemplateId = field("experimentTemplateId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListExperimentsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExperimentsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTargetAccountConfigurationsRequestPaginate:
    boto3_raw_data: (
        "type_defs.ListTargetAccountConfigurationsRequestPaginateTypeDef"
    ) = dataclasses.field()

    experimentTemplateId = field("experimentTemplateId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTargetAccountConfigurationsRequestPaginateTypeDef"
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
                "type_defs.ListTargetAccountConfigurationsRequestPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTargetResourceTypesRequestPaginate:
    boto3_raw_data: "type_defs.ListTargetResourceTypesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTargetResourceTypesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTargetResourceTypesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExperimentResolvedTargetsResponse:
    boto3_raw_data: "type_defs.ListExperimentResolvedTargetsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def resolvedTargets(self):  # pragma: no cover
        return ResolvedTarget.make_many(self.boto3_raw_data["resolvedTargets"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListExperimentResolvedTargetsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExperimentResolvedTargetsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTargetAccountConfigurationsResponse:
    boto3_raw_data: "type_defs.ListTargetAccountConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def targetAccountConfigurations(self):  # pragma: no cover
        return TargetAccountConfigurationSummary.make_many(
            self.boto3_raw_data["targetAccountConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTargetAccountConfigurationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTargetAccountConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTargetResourceTypesResponse:
    boto3_raw_data: "type_defs.ListTargetResourceTypesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def targetResourceTypes(self):  # pragma: no cover
        return TargetResourceTypeSummary.make_many(
            self.boto3_raw_data["targetResourceTypes"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTargetResourceTypesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTargetResourceTypesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SafetyLever:
    boto3_raw_data: "type_defs.SafetyLeverTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")

    @cached_property
    def state(self):  # pragma: no cover
        return SafetyLeverState.make_one(self.boto3_raw_data["state"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SafetyLeverTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SafetyLeverTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartExperimentRequest:
    boto3_raw_data: "type_defs.StartExperimentRequestTypeDef" = dataclasses.field()

    clientToken = field("clientToken")
    experimentTemplateId = field("experimentTemplateId")

    @cached_property
    def experimentOptions(self):  # pragma: no cover
        return StartExperimentExperimentOptionsInput.make_one(
            self.boto3_raw_data["experimentOptions"]
        )

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartExperimentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartExperimentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetResourceType:
    boto3_raw_data: "type_defs.TargetResourceTypeTypeDef" = dataclasses.field()

    resourceType = field("resourceType")
    description = field("description")
    parameters = field("parameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetResourceTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetResourceTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSafetyLeverStateRequest:
    boto3_raw_data: "type_defs.UpdateSafetyLeverStateRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @cached_property
    def state(self):  # pragma: no cover
        return UpdateSafetyLeverStateInput.make_one(self.boto3_raw_data["state"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateSafetyLeverStateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSafetyLeverStateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListActionsResponse:
    boto3_raw_data: "type_defs.ListActionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def actions(self):  # pragma: no cover
        return ActionSummary.make_many(self.boto3_raw_data["actions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListActionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListActionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetActionResponse:
    boto3_raw_data: "type_defs.GetActionResponseTypeDef" = dataclasses.field()

    @cached_property
    def action(self):  # pragma: no cover
        return Action.make_one(self.boto3_raw_data["action"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetActionResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetActionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentSummary:
    boto3_raw_data: "type_defs.ExperimentSummaryTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    experimentTemplateId = field("experimentTemplateId")

    @cached_property
    def state(self):  # pragma: no cover
        return ExperimentState.make_one(self.boto3_raw_data["state"])

    creationTime = field("creationTime")
    tags = field("tags")

    @cached_property
    def experimentOptions(self):  # pragma: no cover
        return ExperimentOptions.make_one(self.boto3_raw_data["experimentOptions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExperimentSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentReportConfiguration:
    boto3_raw_data: "type_defs.ExperimentReportConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def outputs(self):  # pragma: no cover
        return ExperimentReportConfigurationOutputs.make_one(
            self.boto3_raw_data["outputs"]
        )

    @cached_property
    def dataSources(self):  # pragma: no cover
        return ExperimentReportConfigurationDataSources.make_one(
            self.boto3_raw_data["dataSources"]
        )

    preExperimentDuration = field("preExperimentDuration")
    postExperimentDuration = field("postExperimentDuration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ExperimentReportConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentReportConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentReport:
    boto3_raw_data: "type_defs.ExperimentReportTypeDef" = dataclasses.field()

    @cached_property
    def state(self):  # pragma: no cover
        return ExperimentReportState.make_one(self.boto3_raw_data["state"])

    @cached_property
    def s3Reports(self):  # pragma: no cover
        return ExperimentReportS3Report.make_many(self.boto3_raw_data["s3Reports"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExperimentReportTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentReportTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateExperimentTemplateReportConfigurationInput:
    boto3_raw_data: (
        "type_defs.CreateExperimentTemplateReportConfigurationInputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def outputs(self):  # pragma: no cover
        return ExperimentTemplateReportConfigurationOutputsInput.make_one(
            self.boto3_raw_data["outputs"]
        )

    @cached_property
    def dataSources(self):  # pragma: no cover
        return ExperimentTemplateReportConfigurationDataSourcesInput.make_one(
            self.boto3_raw_data["dataSources"]
        )

    preExperimentDuration = field("preExperimentDuration")
    postExperimentDuration = field("postExperimentDuration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateExperimentTemplateReportConfigurationInputTypeDef"
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
                "type_defs.CreateExperimentTemplateReportConfigurationInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateExperimentTemplateReportConfigurationInput:
    boto3_raw_data: (
        "type_defs.UpdateExperimentTemplateReportConfigurationInputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def outputs(self):  # pragma: no cover
        return ExperimentTemplateReportConfigurationOutputsInput.make_one(
            self.boto3_raw_data["outputs"]
        )

    @cached_property
    def dataSources(self):  # pragma: no cover
        return ExperimentTemplateReportConfigurationDataSourcesInput.make_one(
            self.boto3_raw_data["dataSources"]
        )

    preExperimentDuration = field("preExperimentDuration")
    postExperimentDuration = field("postExperimentDuration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateExperimentTemplateReportConfigurationInputTypeDef"
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
                "type_defs.UpdateExperimentTemplateReportConfigurationInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentTemplateReportConfiguration:
    boto3_raw_data: "type_defs.ExperimentTemplateReportConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def outputs(self):  # pragma: no cover
        return ExperimentTemplateReportConfigurationOutputs.make_one(
            self.boto3_raw_data["outputs"]
        )

    @cached_property
    def dataSources(self):  # pragma: no cover
        return ExperimentTemplateReportConfigurationDataSources.make_one(
            self.boto3_raw_data["dataSources"]
        )

    preExperimentDuration = field("preExperimentDuration")
    postExperimentDuration = field("postExperimentDuration")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ExperimentTemplateReportConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentTemplateReportConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSafetyLeverResponse:
    boto3_raw_data: "type_defs.GetSafetyLeverResponseTypeDef" = dataclasses.field()

    @cached_property
    def safetyLever(self):  # pragma: no cover
        return SafetyLever.make_one(self.boto3_raw_data["safetyLever"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSafetyLeverResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSafetyLeverResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSafetyLeverStateResponse:
    boto3_raw_data: "type_defs.UpdateSafetyLeverStateResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def safetyLever(self):  # pragma: no cover
        return SafetyLever.make_one(self.boto3_raw_data["safetyLever"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateSafetyLeverStateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSafetyLeverStateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTargetResourceTypeResponse:
    boto3_raw_data: "type_defs.GetTargetResourceTypeResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def targetResourceType(self):  # pragma: no cover
        return TargetResourceType.make_one(self.boto3_raw_data["targetResourceType"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetTargetResourceTypeResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTargetResourceTypeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListExperimentsResponse:
    boto3_raw_data: "type_defs.ListExperimentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def experiments(self):  # pragma: no cover
        return ExperimentSummary.make_many(self.boto3_raw_data["experiments"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListExperimentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListExperimentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Experiment:
    boto3_raw_data: "type_defs.ExperimentTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    experimentTemplateId = field("experimentTemplateId")
    roleArn = field("roleArn")

    @cached_property
    def state(self):  # pragma: no cover
        return ExperimentState.make_one(self.boto3_raw_data["state"])

    targets = field("targets")
    actions = field("actions")

    @cached_property
    def stopConditions(self):  # pragma: no cover
        return ExperimentStopCondition.make_many(self.boto3_raw_data["stopConditions"])

    creationTime = field("creationTime")
    startTime = field("startTime")
    endTime = field("endTime")
    tags = field("tags")

    @cached_property
    def logConfiguration(self):  # pragma: no cover
        return ExperimentLogConfiguration.make_one(
            self.boto3_raw_data["logConfiguration"]
        )

    @cached_property
    def experimentOptions(self):  # pragma: no cover
        return ExperimentOptions.make_one(self.boto3_raw_data["experimentOptions"])

    targetAccountConfigurationsCount = field("targetAccountConfigurationsCount")

    @cached_property
    def experimentReportConfiguration(self):  # pragma: no cover
        return ExperimentReportConfiguration.make_one(
            self.boto3_raw_data["experimentReportConfiguration"]
        )

    @cached_property
    def experimentReport(self):  # pragma: no cover
        return ExperimentReport.make_one(self.boto3_raw_data["experimentReport"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExperimentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExperimentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateExperimentTemplateRequest:
    boto3_raw_data: "type_defs.CreateExperimentTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    clientToken = field("clientToken")
    description = field("description")

    @cached_property
    def stopConditions(self):  # pragma: no cover
        return CreateExperimentTemplateStopConditionInput.make_many(
            self.boto3_raw_data["stopConditions"]
        )

    actions = field("actions")
    roleArn = field("roleArn")
    targets = field("targets")
    tags = field("tags")

    @cached_property
    def logConfiguration(self):  # pragma: no cover
        return CreateExperimentTemplateLogConfigurationInput.make_one(
            self.boto3_raw_data["logConfiguration"]
        )

    @cached_property
    def experimentOptions(self):  # pragma: no cover
        return CreateExperimentTemplateExperimentOptionsInput.make_one(
            self.boto3_raw_data["experimentOptions"]
        )

    @cached_property
    def experimentReportConfiguration(self):  # pragma: no cover
        return CreateExperimentTemplateReportConfigurationInput.make_one(
            self.boto3_raw_data["experimentReportConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateExperimentTemplateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExperimentTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateExperimentTemplateRequest:
    boto3_raw_data: "type_defs.UpdateExperimentTemplateRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    description = field("description")

    @cached_property
    def stopConditions(self):  # pragma: no cover
        return UpdateExperimentTemplateStopConditionInput.make_many(
            self.boto3_raw_data["stopConditions"]
        )

    targets = field("targets")
    actions = field("actions")
    roleArn = field("roleArn")

    @cached_property
    def logConfiguration(self):  # pragma: no cover
        return UpdateExperimentTemplateLogConfigurationInput.make_one(
            self.boto3_raw_data["logConfiguration"]
        )

    @cached_property
    def experimentOptions(self):  # pragma: no cover
        return UpdateExperimentTemplateExperimentOptionsInput.make_one(
            self.boto3_raw_data["experimentOptions"]
        )

    @cached_property
    def experimentReportConfiguration(self):  # pragma: no cover
        return UpdateExperimentTemplateReportConfigurationInput.make_one(
            self.boto3_raw_data["experimentReportConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateExperimentTemplateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateExperimentTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExperimentTemplate:
    boto3_raw_data: "type_defs.ExperimentTemplateTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    description = field("description")
    targets = field("targets")
    actions = field("actions")

    @cached_property
    def stopConditions(self):  # pragma: no cover
        return ExperimentTemplateStopCondition.make_many(
            self.boto3_raw_data["stopConditions"]
        )

    creationTime = field("creationTime")
    lastUpdateTime = field("lastUpdateTime")
    roleArn = field("roleArn")
    tags = field("tags")

    @cached_property
    def logConfiguration(self):  # pragma: no cover
        return ExperimentTemplateLogConfiguration.make_one(
            self.boto3_raw_data["logConfiguration"]
        )

    @cached_property
    def experimentOptions(self):  # pragma: no cover
        return ExperimentTemplateExperimentOptions.make_one(
            self.boto3_raw_data["experimentOptions"]
        )

    targetAccountConfigurationsCount = field("targetAccountConfigurationsCount")

    @cached_property
    def experimentReportConfiguration(self):  # pragma: no cover
        return ExperimentTemplateReportConfiguration.make_one(
            self.boto3_raw_data["experimentReportConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExperimentTemplateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExperimentTemplateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExperimentResponse:
    boto3_raw_data: "type_defs.GetExperimentResponseTypeDef" = dataclasses.field()

    @cached_property
    def experiment(self):  # pragma: no cover
        return Experiment.make_one(self.boto3_raw_data["experiment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetExperimentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExperimentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartExperimentResponse:
    boto3_raw_data: "type_defs.StartExperimentResponseTypeDef" = dataclasses.field()

    @cached_property
    def experiment(self):  # pragma: no cover
        return Experiment.make_one(self.boto3_raw_data["experiment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartExperimentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartExperimentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopExperimentResponse:
    boto3_raw_data: "type_defs.StopExperimentResponseTypeDef" = dataclasses.field()

    @cached_property
    def experiment(self):  # pragma: no cover
        return Experiment.make_one(self.boto3_raw_data["experiment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StopExperimentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopExperimentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateExperimentTemplateResponse:
    boto3_raw_data: "type_defs.CreateExperimentTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def experimentTemplate(self):  # pragma: no cover
        return ExperimentTemplate.make_one(self.boto3_raw_data["experimentTemplate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateExperimentTemplateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExperimentTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteExperimentTemplateResponse:
    boto3_raw_data: "type_defs.DeleteExperimentTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def experimentTemplate(self):  # pragma: no cover
        return ExperimentTemplate.make_one(self.boto3_raw_data["experimentTemplate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteExperimentTemplateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteExperimentTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetExperimentTemplateResponse:
    boto3_raw_data: "type_defs.GetExperimentTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def experimentTemplate(self):  # pragma: no cover
        return ExperimentTemplate.make_one(self.boto3_raw_data["experimentTemplate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetExperimentTemplateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetExperimentTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateExperimentTemplateResponse:
    boto3_raw_data: "type_defs.UpdateExperimentTemplateResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def experimentTemplate(self):  # pragma: no cover
        return ExperimentTemplate.make_one(self.boto3_raw_data["experimentTemplate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateExperimentTemplateResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateExperimentTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
