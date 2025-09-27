# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_apptest import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class BatchOutput:
    boto3_raw_data: "type_defs.BatchOutputTypeDef" = dataclasses.field()

    batchJobName = field("batchJobName")
    batchJobParameters = field("batchJobParameters")
    exportDataSetNames = field("exportDataSetNames")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BatchOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MainframeActionProperties:
    boto3_raw_data: "type_defs.MainframeActionPropertiesTypeDef" = dataclasses.field()

    dmsTaskArn = field("dmsTaskArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MainframeActionPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MainframeActionPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataSet:
    boto3_raw_data: "type_defs.DataSetTypeDef" = dataclasses.field()

    type = field("type")
    name = field("name")
    ccsid = field("ccsid")
    format = field("format")
    length = field("length")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DataSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DataSetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Batch:
    boto3_raw_data: "type_defs.BatchTypeDef" = dataclasses.field()

    batchJobName = field("batchJobName")
    batchJobParameters = field("batchJobParameters")
    exportDataSetNames = field("exportDataSetNames")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BatchTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudFormationAction:
    boto3_raw_data: "type_defs.CloudFormationActionTypeDef" = dataclasses.field()

    resource = field("resource")
    actionType = field("actionType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudFormationActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudFormationActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudFormationOutput:
    boto3_raw_data: "type_defs.CloudFormationOutputTypeDef" = dataclasses.field()

    templateLocation = field("templateLocation")
    parameters = field("parameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudFormationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudFormationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudFormation:
    boto3_raw_data: "type_defs.CloudFormationTypeDef" = dataclasses.field()

    templateLocation = field("templateLocation")
    parameters = field("parameters")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CloudFormationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CloudFormationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompareDataSetsStepOutput:
    boto3_raw_data: "type_defs.CompareDataSetsStepOutputTypeDef" = dataclasses.field()

    comparisonOutputLocation = field("comparisonOutputLocation")
    comparisonStatus = field("comparisonStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompareDataSetsStepOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompareDataSetsStepOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceDatabaseMetadata:
    boto3_raw_data: "type_defs.SourceDatabaseMetadataTypeDef" = dataclasses.field()

    type = field("type")
    captureTool = field("captureTool")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SourceDatabaseMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SourceDatabaseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TargetDatabaseMetadata:
    boto3_raw_data: "type_defs.TargetDatabaseMetadataTypeDef" = dataclasses.field()

    type = field("type")
    captureTool = field("captureTool")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TargetDatabaseMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TargetDatabaseMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompareDatabaseCDCStepOutput:
    boto3_raw_data: "type_defs.CompareDatabaseCDCStepOutputTypeDef" = (
        dataclasses.field()
    )

    comparisonOutputLocation = field("comparisonOutputLocation")
    comparisonStatus = field("comparisonStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompareDatabaseCDCStepOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompareDatabaseCDCStepOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCloudFormationStepInput:
    boto3_raw_data: "type_defs.CreateCloudFormationStepInputTypeDef" = (
        dataclasses.field()
    )

    templateLocation = field("templateLocation")
    parameters = field("parameters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateCloudFormationStepInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCloudFormationStepInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCloudFormationStepOutput:
    boto3_raw_data: "type_defs.CreateCloudFormationStepOutputTypeDef" = (
        dataclasses.field()
    )

    stackId = field("stackId")
    exports = field("exports")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateCloudFormationStepOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCloudFormationStepOutputTypeDef"]
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
class ServiceSettings:
    boto3_raw_data: "type_defs.ServiceSettingsTypeDef" = dataclasses.field()

    kmsKeyId = field("kmsKeyId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceSettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceSettingsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCloudFormationStepInput:
    boto3_raw_data: "type_defs.DeleteCloudFormationStepInputTypeDef" = (
        dataclasses.field()
    )

    stackId = field("stackId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteCloudFormationStepInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCloudFormationStepInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTestCaseRequest:
    boto3_raw_data: "type_defs.DeleteTestCaseRequestTypeDef" = dataclasses.field()

    testCaseId = field("testCaseId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTestCaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTestCaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTestConfigurationRequest:
    boto3_raw_data: "type_defs.DeleteTestConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    testConfigurationId = field("testConfigurationId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteTestConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTestConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTestRunRequest:
    boto3_raw_data: "type_defs.DeleteTestRunRequestTypeDef" = dataclasses.field()

    testRunId = field("testRunId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTestRunRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTestRunRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTestSuiteRequest:
    boto3_raw_data: "type_defs.DeleteTestSuiteRequestTypeDef" = dataclasses.field()

    testSuiteId = field("testSuiteId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTestSuiteRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTestSuiteRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTestCaseRequest:
    boto3_raw_data: "type_defs.GetTestCaseRequestTypeDef" = dataclasses.field()

    testCaseId = field("testCaseId")
    testCaseVersion = field("testCaseVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTestCaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTestCaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestCaseLatestVersion:
    boto3_raw_data: "type_defs.TestCaseLatestVersionTypeDef" = dataclasses.field()

    version = field("version")
    status = field("status")
    statusReason = field("statusReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestCaseLatestVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestCaseLatestVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTestConfigurationRequest:
    boto3_raw_data: "type_defs.GetTestConfigurationRequestTypeDef" = dataclasses.field()

    testConfigurationId = field("testConfigurationId")
    testConfigurationVersion = field("testConfigurationVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTestConfigurationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTestConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestConfigurationLatestVersion:
    boto3_raw_data: "type_defs.TestConfigurationLatestVersionTypeDef" = (
        dataclasses.field()
    )

    version = field("version")
    status = field("status")
    statusReason = field("statusReason")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.TestConfigurationLatestVersionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestConfigurationLatestVersionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTestRunStepRequest:
    boto3_raw_data: "type_defs.GetTestRunStepRequestTypeDef" = dataclasses.field()

    testRunId = field("testRunId")
    stepName = field("stepName")
    testCaseId = field("testCaseId")
    testSuiteId = field("testSuiteId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTestRunStepRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTestRunStepRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTestSuiteRequest:
    boto3_raw_data: "type_defs.GetTestSuiteRequestTypeDef" = dataclasses.field()

    testSuiteId = field("testSuiteId")
    testSuiteVersion = field("testSuiteVersion")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTestSuiteRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTestSuiteRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestCasesOutput:
    boto3_raw_data: "type_defs.TestCasesOutputTypeDef" = dataclasses.field()

    sequential = field("sequential")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestCasesOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TestCasesOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestSuiteLatestVersion:
    boto3_raw_data: "type_defs.TestSuiteLatestVersionTypeDef" = dataclasses.field()

    version = field("version")
    status = field("status")
    statusReason = field("statusReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestSuiteLatestVersionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestSuiteLatestVersionTypeDef"]
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
class ListTestCasesRequest:
    boto3_raw_data: "type_defs.ListTestCasesRequestTypeDef" = dataclasses.field()

    testCaseIds = field("testCaseIds")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTestCasesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestCasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestCaseSummary:
    boto3_raw_data: "type_defs.TestCaseSummaryTypeDef" = dataclasses.field()

    testCaseId = field("testCaseId")
    testCaseArn = field("testCaseArn")
    name = field("name")
    latestVersion = field("latestVersion")
    status = field("status")
    creationTime = field("creationTime")
    lastUpdateTime = field("lastUpdateTime")
    statusReason = field("statusReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestCaseSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TestCaseSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestConfigurationsRequest:
    boto3_raw_data: "type_defs.ListTestConfigurationsRequestTypeDef" = (
        dataclasses.field()
    )

    testConfigurationIds = field("testConfigurationIds")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTestConfigurationsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestConfigurationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestConfigurationSummary:
    boto3_raw_data: "type_defs.TestConfigurationSummaryTypeDef" = dataclasses.field()

    testConfigurationId = field("testConfigurationId")
    name = field("name")
    latestVersion = field("latestVersion")
    testConfigurationArn = field("testConfigurationArn")
    status = field("status")
    creationTime = field("creationTime")
    lastUpdateTime = field("lastUpdateTime")
    statusReason = field("statusReason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestConfigurationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestConfigurationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestRunStepsRequest:
    boto3_raw_data: "type_defs.ListTestRunStepsRequestTypeDef" = dataclasses.field()

    testRunId = field("testRunId")
    testCaseId = field("testCaseId")
    testSuiteId = field("testSuiteId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTestRunStepsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestRunStepsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestRunStepSummary:
    boto3_raw_data: "type_defs.TestRunStepSummaryTypeDef" = dataclasses.field()

    stepName = field("stepName")
    testRunId = field("testRunId")
    status = field("status")
    runStartTime = field("runStartTime")
    testCaseId = field("testCaseId")
    testCaseVersion = field("testCaseVersion")
    testSuiteId = field("testSuiteId")
    testSuiteVersion = field("testSuiteVersion")
    beforeStep = field("beforeStep")
    afterStep = field("afterStep")
    statusReason = field("statusReason")
    runEndTime = field("runEndTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestRunStepSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestRunStepSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestRunTestCasesRequest:
    boto3_raw_data: "type_defs.ListTestRunTestCasesRequestTypeDef" = dataclasses.field()

    testRunId = field("testRunId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTestRunTestCasesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestRunTestCasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestCaseRunSummary:
    boto3_raw_data: "type_defs.TestCaseRunSummaryTypeDef" = dataclasses.field()

    testCaseId = field("testCaseId")
    testCaseVersion = field("testCaseVersion")
    testRunId = field("testRunId")
    status = field("status")
    runStartTime = field("runStartTime")
    statusReason = field("statusReason")
    runEndTime = field("runEndTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestCaseRunSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestCaseRunSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestRunsRequest:
    boto3_raw_data: "type_defs.ListTestRunsRequestTypeDef" = dataclasses.field()

    testSuiteId = field("testSuiteId")
    testRunIds = field("testRunIds")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTestRunsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestRunsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestRunSummary:
    boto3_raw_data: "type_defs.TestRunSummaryTypeDef" = dataclasses.field()

    testRunId = field("testRunId")
    testRunArn = field("testRunArn")
    testSuiteId = field("testSuiteId")
    testSuiteVersion = field("testSuiteVersion")
    status = field("status")
    runStartTime = field("runStartTime")
    testConfigurationId = field("testConfigurationId")
    testConfigurationVersion = field("testConfigurationVersion")
    statusReason = field("statusReason")
    runEndTime = field("runEndTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestRunSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TestRunSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestSuitesRequest:
    boto3_raw_data: "type_defs.ListTestSuitesRequestTypeDef" = dataclasses.field()

    testSuiteIds = field("testSuiteIds")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTestSuitesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestSuitesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestSuiteSummary:
    boto3_raw_data: "type_defs.TestSuiteSummaryTypeDef" = dataclasses.field()

    testSuiteId = field("testSuiteId")
    name = field("name")
    latestVersion = field("latestVersion")
    testSuiteArn = field("testSuiteArn")
    status = field("status")
    creationTime = field("creationTime")
    lastUpdateTime = field("lastUpdateTime")
    statusReason = field("statusReason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestSuiteSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestSuiteSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class M2ManagedActionProperties:
    boto3_raw_data: "type_defs.M2ManagedActionPropertiesTypeDef" = dataclasses.field()

    forceStop = field("forceStop")
    importDataSetLocation = field("importDataSetLocation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.M2ManagedActionPropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.M2ManagedActionPropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class M2ManagedApplicationStepOutput:
    boto3_raw_data: "type_defs.M2ManagedApplicationStepOutputTypeDef" = (
        dataclasses.field()
    )

    importDataSetSummary = field("importDataSetSummary")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.M2ManagedApplicationStepOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.M2ManagedApplicationStepOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class M2ManagedApplicationSummary:
    boto3_raw_data: "type_defs.M2ManagedApplicationSummaryTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    runtime = field("runtime")
    listenerPort = field("listenerPort")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.M2ManagedApplicationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.M2ManagedApplicationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class M2ManagedApplication:
    boto3_raw_data: "type_defs.M2ManagedApplicationTypeDef" = dataclasses.field()

    applicationId = field("applicationId")
    runtime = field("runtime")
    vpcEndpointServiceName = field("vpcEndpointServiceName")
    listenerPort = field("listenerPort")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.M2ManagedApplicationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.M2ManagedApplicationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class M2NonManagedApplicationAction:
    boto3_raw_data: "type_defs.M2NonManagedApplicationActionTypeDef" = (
        dataclasses.field()
    )

    resource = field("resource")
    actionType = field("actionType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.M2NonManagedApplicationActionTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.M2NonManagedApplicationActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class M2NonManagedApplicationStepInput:
    boto3_raw_data: "type_defs.M2NonManagedApplicationStepInputTypeDef" = (
        dataclasses.field()
    )

    vpcEndpointServiceName = field("vpcEndpointServiceName")
    listenerPort = field("listenerPort")
    runtime = field("runtime")
    actionType = field("actionType")
    webAppName = field("webAppName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.M2NonManagedApplicationStepInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.M2NonManagedApplicationStepInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class M2NonManagedApplicationSummary:
    boto3_raw_data: "type_defs.M2NonManagedApplicationSummaryTypeDef" = (
        dataclasses.field()
    )

    vpcEndpointServiceName = field("vpcEndpointServiceName")
    listenerPort = field("listenerPort")
    runtime = field("runtime")
    webAppName = field("webAppName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.M2NonManagedApplicationSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.M2NonManagedApplicationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class M2NonManagedApplication:
    boto3_raw_data: "type_defs.M2NonManagedApplicationTypeDef" = dataclasses.field()

    vpcEndpointServiceName = field("vpcEndpointServiceName")
    listenerPort = field("listenerPort")
    runtime = field("runtime")
    webAppName = field("webAppName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.M2NonManagedApplicationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.M2NonManagedApplicationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputFile:
    boto3_raw_data: "type_defs.OutputFileTypeDef" = dataclasses.field()

    fileLocation = field("fileLocation")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputFileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputFileTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScriptSummary:
    boto3_raw_data: "type_defs.ScriptSummaryTypeDef" = dataclasses.field()

    scriptLocation = field("scriptLocation")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScriptSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScriptSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Script:
    boto3_raw_data: "type_defs.ScriptTypeDef" = dataclasses.field()

    scriptLocation = field("scriptLocation")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScriptTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScriptTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartTestRunRequest:
    boto3_raw_data: "type_defs.StartTestRunRequestTypeDef" = dataclasses.field()

    testSuiteId = field("testSuiteId")
    testConfigurationId = field("testConfigurationId")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartTestRunRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTestRunRequestTypeDef"]
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
class TestCases:
    boto3_raw_data: "type_defs.TestCasesTypeDef" = dataclasses.field()

    sequential = field("sequential")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TestCasesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TestCasesTypeDef"]]
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
class BatchStepOutput:
    boto3_raw_data: "type_defs.BatchStepOutputTypeDef" = dataclasses.field()

    dataSetExportLocation = field("dataSetExportLocation")
    dmsOutputLocation = field("dmsOutputLocation")

    @cached_property
    def dataSetDetails(self):  # pragma: no cover
        return DataSet.make_many(self.boto3_raw_data["dataSetDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchStepOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BatchStepOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompareDataSetsStepInput:
    boto3_raw_data: "type_defs.CompareDataSetsStepInputTypeDef" = dataclasses.field()

    sourceLocation = field("sourceLocation")
    targetLocation = field("targetLocation")

    @cached_property
    def sourceDataSets(self):  # pragma: no cover
        return DataSet.make_many(self.boto3_raw_data["sourceDataSets"])

    @cached_property
    def targetDataSets(self):  # pragma: no cover
        return DataSet.make_many(self.boto3_raw_data["targetDataSets"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompareDataSetsStepInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompareDataSetsStepInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TN3270StepOutput:
    boto3_raw_data: "type_defs.TN3270StepOutputTypeDef" = dataclasses.field()

    scriptOutputLocation = field("scriptOutputLocation")
    dataSetExportLocation = field("dataSetExportLocation")
    dmsOutputLocation = field("dmsOutputLocation")

    @cached_property
    def dataSetDetails(self):  # pragma: no cover
        return DataSet.make_many(self.boto3_raw_data["dataSetDetails"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TN3270StepOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TN3270StepOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompareDatabaseCDCStepInput:
    boto3_raw_data: "type_defs.CompareDatabaseCDCStepInputTypeDef" = dataclasses.field()

    sourceLocation = field("sourceLocation")
    targetLocation = field("targetLocation")

    @cached_property
    def sourceMetadata(self):  # pragma: no cover
        return SourceDatabaseMetadata.make_one(self.boto3_raw_data["sourceMetadata"])

    @cached_property
    def targetMetadata(self):  # pragma: no cover
        return TargetDatabaseMetadata.make_one(self.boto3_raw_data["targetMetadata"])

    outputLocation = field("outputLocation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompareDatabaseCDCStepInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompareDatabaseCDCStepInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatabaseCDC:
    boto3_raw_data: "type_defs.DatabaseCDCTypeDef" = dataclasses.field()

    @cached_property
    def sourceMetadata(self):  # pragma: no cover
        return SourceDatabaseMetadata.make_one(self.boto3_raw_data["sourceMetadata"])

    @cached_property
    def targetMetadata(self):  # pragma: no cover
        return TargetDatabaseMetadata.make_one(self.boto3_raw_data["targetMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DatabaseCDCTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DatabaseCDCTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCloudFormationSummary:
    boto3_raw_data: "type_defs.CreateCloudFormationSummaryTypeDef" = dataclasses.field()

    @cached_property
    def stepInput(self):  # pragma: no cover
        return CreateCloudFormationStepInput.make_one(self.boto3_raw_data["stepInput"])

    @cached_property
    def stepOutput(self):  # pragma: no cover
        return CreateCloudFormationStepOutput.make_one(
            self.boto3_raw_data["stepOutput"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCloudFormationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCloudFormationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTestCaseResponse:
    boto3_raw_data: "type_defs.CreateTestCaseResponseTypeDef" = dataclasses.field()

    testCaseId = field("testCaseId")
    testCaseVersion = field("testCaseVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTestCaseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTestCaseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTestConfigurationResponse:
    boto3_raw_data: "type_defs.CreateTestConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    testConfigurationId = field("testConfigurationId")
    testConfigurationVersion = field("testConfigurationVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateTestConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTestConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTestSuiteResponse:
    boto3_raw_data: "type_defs.CreateTestSuiteResponseTypeDef" = dataclasses.field()

    testSuiteId = field("testSuiteId")
    testSuiteVersion = field("testSuiteVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTestSuiteResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTestSuiteResponseTypeDef"]
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
class StartTestRunResponse:
    boto3_raw_data: "type_defs.StartTestRunResponseTypeDef" = dataclasses.field()

    testRunId = field("testRunId")
    testRunStatus = field("testRunStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartTestRunResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartTestRunResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTestCaseResponse:
    boto3_raw_data: "type_defs.UpdateTestCaseResponseTypeDef" = dataclasses.field()

    testCaseId = field("testCaseId")
    testCaseVersion = field("testCaseVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTestCaseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTestCaseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTestConfigurationResponse:
    boto3_raw_data: "type_defs.UpdateTestConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    testConfigurationId = field("testConfigurationId")
    testConfigurationVersion = field("testConfigurationVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateTestConfigurationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTestConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTestSuiteResponse:
    boto3_raw_data: "type_defs.UpdateTestSuiteResponseTypeDef" = dataclasses.field()

    testSuiteId = field("testSuiteId")
    testSuiteVersion = field("testSuiteVersion")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTestSuiteResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTestSuiteResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCloudFormationSummary:
    boto3_raw_data: "type_defs.DeleteCloudFormationSummaryTypeDef" = dataclasses.field()

    @cached_property
    def stepInput(self):  # pragma: no cover
        return DeleteCloudFormationStepInput.make_one(self.boto3_raw_data["stepInput"])

    stepOutput = field("stepOutput")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCloudFormationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCloudFormationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestCasesRequestPaginate:
    boto3_raw_data: "type_defs.ListTestCasesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    testCaseIds = field("testCaseIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTestCasesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestCasesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestConfigurationsRequestPaginate:
    boto3_raw_data: "type_defs.ListTestConfigurationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    testConfigurationIds = field("testConfigurationIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTestConfigurationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestConfigurationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestRunStepsRequestPaginate:
    boto3_raw_data: "type_defs.ListTestRunStepsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    testRunId = field("testRunId")
    testCaseId = field("testCaseId")
    testSuiteId = field("testSuiteId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTestRunStepsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestRunStepsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestRunTestCasesRequestPaginate:
    boto3_raw_data: "type_defs.ListTestRunTestCasesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    testRunId = field("testRunId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListTestRunTestCasesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestRunTestCasesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestRunsRequestPaginate:
    boto3_raw_data: "type_defs.ListTestRunsRequestPaginateTypeDef" = dataclasses.field()

    testSuiteId = field("testSuiteId")
    testRunIds = field("testRunIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTestRunsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestRunsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestSuitesRequestPaginate:
    boto3_raw_data: "type_defs.ListTestSuitesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    testSuiteIds = field("testSuiteIds")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTestSuitesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestSuitesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestCasesResponse:
    boto3_raw_data: "type_defs.ListTestCasesResponseTypeDef" = dataclasses.field()

    @cached_property
    def testCases(self):  # pragma: no cover
        return TestCaseSummary.make_many(self.boto3_raw_data["testCases"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTestCasesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestCasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestConfigurationsResponse:
    boto3_raw_data: "type_defs.ListTestConfigurationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def testConfigurations(self):  # pragma: no cover
        return TestConfigurationSummary.make_many(
            self.boto3_raw_data["testConfigurations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListTestConfigurationsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestConfigurationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestRunStepsResponse:
    boto3_raw_data: "type_defs.ListTestRunStepsResponseTypeDef" = dataclasses.field()

    @cached_property
    def testRunSteps(self):  # pragma: no cover
        return TestRunStepSummary.make_many(self.boto3_raw_data["testRunSteps"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTestRunStepsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestRunStepsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestRunTestCasesResponse:
    boto3_raw_data: "type_defs.ListTestRunTestCasesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def testRunTestCases(self):  # pragma: no cover
        return TestCaseRunSummary.make_many(self.boto3_raw_data["testRunTestCases"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTestRunTestCasesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestRunTestCasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestRunsResponse:
    boto3_raw_data: "type_defs.ListTestRunsResponseTypeDef" = dataclasses.field()

    @cached_property
    def testRuns(self):  # pragma: no cover
        return TestRunSummary.make_many(self.boto3_raw_data["testRuns"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTestRunsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestRunsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTestSuitesResponse:
    boto3_raw_data: "type_defs.ListTestSuitesResponseTypeDef" = dataclasses.field()

    @cached_property
    def testSuites(self):  # pragma: no cover
        return TestSuiteSummary.make_many(self.boto3_raw_data["testSuites"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTestSuitesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTestSuitesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class M2ManagedApplicationAction:
    boto3_raw_data: "type_defs.M2ManagedApplicationActionTypeDef" = dataclasses.field()

    resource = field("resource")
    actionType = field("actionType")

    @cached_property
    def properties(self):  # pragma: no cover
        return M2ManagedActionProperties.make_one(self.boto3_raw_data["properties"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.M2ManagedApplicationActionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.M2ManagedApplicationActionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class M2ManagedApplicationStepInput:
    boto3_raw_data: "type_defs.M2ManagedApplicationStepInputTypeDef" = (
        dataclasses.field()
    )

    applicationId = field("applicationId")
    runtime = field("runtime")
    actionType = field("actionType")
    vpcEndpointServiceName = field("vpcEndpointServiceName")
    listenerPort = field("listenerPort")

    @cached_property
    def properties(self):  # pragma: no cover
        return M2ManagedActionProperties.make_one(self.boto3_raw_data["properties"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.M2ManagedApplicationStepInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.M2ManagedApplicationStepInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class M2NonManagedApplicationStepSummary:
    boto3_raw_data: "type_defs.M2NonManagedApplicationStepSummaryTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def stepInput(self):  # pragma: no cover
        return M2NonManagedApplicationStepInput.make_one(
            self.boto3_raw_data["stepInput"]
        )

    stepOutput = field("stepOutput")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.M2NonManagedApplicationStepSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.M2NonManagedApplicationStepSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MainframeResourceSummary:
    boto3_raw_data: "type_defs.MainframeResourceSummaryTypeDef" = dataclasses.field()

    @cached_property
    def m2ManagedApplication(self):  # pragma: no cover
        return M2ManagedApplicationSummary.make_one(
            self.boto3_raw_data["m2ManagedApplication"]
        )

    @cached_property
    def m2NonManagedApplication(self):  # pragma: no cover
        return M2NonManagedApplicationSummary.make_one(
            self.boto3_raw_data["m2NonManagedApplication"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MainframeResourceSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MainframeResourceSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceTypeOutput:
    boto3_raw_data: "type_defs.ResourceTypeOutputTypeDef" = dataclasses.field()

    @cached_property
    def cloudFormation(self):  # pragma: no cover
        return CloudFormationOutput.make_one(self.boto3_raw_data["cloudFormation"])

    @cached_property
    def m2ManagedApplication(self):  # pragma: no cover
        return M2ManagedApplication.make_one(
            self.boto3_raw_data["m2ManagedApplication"]
        )

    @cached_property
    def m2NonManagedApplication(self):  # pragma: no cover
        return M2NonManagedApplication.make_one(
            self.boto3_raw_data["m2NonManagedApplication"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceTypeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Output:
    boto3_raw_data: "type_defs.OutputTypeDef" = dataclasses.field()

    @cached_property
    def file(self):  # pragma: no cover
        return OutputFile.make_one(self.boto3_raw_data["file"])

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
class TN3270Output:
    boto3_raw_data: "type_defs.TN3270OutputTypeDef" = dataclasses.field()

    @cached_property
    def script(self):  # pragma: no cover
        return Script.make_one(self.boto3_raw_data["script"])

    exportDataSetNames = field("exportDataSetNames")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TN3270OutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TN3270OutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TN3270:
    boto3_raw_data: "type_defs.TN3270TypeDef" = dataclasses.field()

    @cached_property
    def script(self):  # pragma: no cover
        return Script.make_one(self.boto3_raw_data["script"])

    exportDataSetNames = field("exportDataSetNames")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TN3270TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TN3270TypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompareDataSetsSummary:
    boto3_raw_data: "type_defs.CompareDataSetsSummaryTypeDef" = dataclasses.field()

    @cached_property
    def stepInput(self):  # pragma: no cover
        return CompareDataSetsStepInput.make_one(self.boto3_raw_data["stepInput"])

    @cached_property
    def stepOutput(self):  # pragma: no cover
        return CompareDataSetsStepOutput.make_one(self.boto3_raw_data["stepOutput"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompareDataSetsSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompareDataSetsSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceType:
    boto3_raw_data: "type_defs.ResourceTypeTypeDef" = dataclasses.field()

    cloudFormation = field("cloudFormation")

    @cached_property
    def m2ManagedApplication(self):  # pragma: no cover
        return M2ManagedApplication.make_one(
            self.boto3_raw_data["m2ManagedApplication"]
        )

    @cached_property
    def m2NonManagedApplication(self):  # pragma: no cover
        return M2NonManagedApplication.make_one(
            self.boto3_raw_data["m2NonManagedApplication"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompareDatabaseCDCSummary:
    boto3_raw_data: "type_defs.CompareDatabaseCDCSummaryTypeDef" = dataclasses.field()

    @cached_property
    def stepInput(self):  # pragma: no cover
        return CompareDatabaseCDCStepInput.make_one(self.boto3_raw_data["stepInput"])

    @cached_property
    def stepOutput(self):  # pragma: no cover
        return CompareDatabaseCDCStepOutput.make_one(self.boto3_raw_data["stepOutput"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompareDatabaseCDCSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompareDatabaseCDCSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileMetadataOutput:
    boto3_raw_data: "type_defs.FileMetadataOutputTypeDef" = dataclasses.field()

    @cached_property
    def dataSets(self):  # pragma: no cover
        return DataSet.make_many(self.boto3_raw_data["dataSets"])

    @cached_property
    def databaseCDC(self):  # pragma: no cover
        return DatabaseCDC.make_one(self.boto3_raw_data["databaseCDC"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FileMetadataOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FileMetadataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileMetadata:
    boto3_raw_data: "type_defs.FileMetadataTypeDef" = dataclasses.field()

    @cached_property
    def dataSets(self):  # pragma: no cover
        return DataSet.make_many(self.boto3_raw_data["dataSets"])

    @cached_property
    def databaseCDC(self):  # pragma: no cover
        return DatabaseCDC.make_one(self.boto3_raw_data["databaseCDC"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FileMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FileMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CloudFormationStepSummary:
    boto3_raw_data: "type_defs.CloudFormationStepSummaryTypeDef" = dataclasses.field()

    @cached_property
    def createCloudformation(self):  # pragma: no cover
        return CreateCloudFormationSummary.make_one(
            self.boto3_raw_data["createCloudformation"]
        )

    @cached_property
    def deleteCloudformation(self):  # pragma: no cover
        return DeleteCloudFormationSummary.make_one(
            self.boto3_raw_data["deleteCloudformation"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CloudFormationStepSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CloudFormationStepSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceAction:
    boto3_raw_data: "type_defs.ResourceActionTypeDef" = dataclasses.field()

    @cached_property
    def m2ManagedApplicationAction(self):  # pragma: no cover
        return M2ManagedApplicationAction.make_one(
            self.boto3_raw_data["m2ManagedApplicationAction"]
        )

    @cached_property
    def m2NonManagedApplicationAction(self):  # pragma: no cover
        return M2NonManagedApplicationAction.make_one(
            self.boto3_raw_data["m2NonManagedApplicationAction"]
        )

    @cached_property
    def cloudFormationAction(self):  # pragma: no cover
        return CloudFormationAction.make_one(
            self.boto3_raw_data["cloudFormationAction"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class M2ManagedApplicationStepSummary:
    boto3_raw_data: "type_defs.M2ManagedApplicationStepSummaryTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def stepInput(self):  # pragma: no cover
        return M2ManagedApplicationStepInput.make_one(self.boto3_raw_data["stepInput"])

    @cached_property
    def stepOutput(self):  # pragma: no cover
        return M2ManagedApplicationStepOutput.make_one(
            self.boto3_raw_data["stepOutput"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.M2ManagedApplicationStepSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.M2ManagedApplicationStepSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchStepInput:
    boto3_raw_data: "type_defs.BatchStepInputTypeDef" = dataclasses.field()

    @cached_property
    def resource(self):  # pragma: no cover
        return MainframeResourceSummary.make_one(self.boto3_raw_data["resource"])

    batchJobName = field("batchJobName")
    batchJobParameters = field("batchJobParameters")
    exportDataSetNames = field("exportDataSetNames")

    @cached_property
    def properties(self):  # pragma: no cover
        return MainframeActionProperties.make_one(self.boto3_raw_data["properties"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchStepInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BatchStepInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TN3270StepInput:
    boto3_raw_data: "type_defs.TN3270StepInputTypeDef" = dataclasses.field()

    @cached_property
    def resource(self):  # pragma: no cover
        return MainframeResourceSummary.make_one(self.boto3_raw_data["resource"])

    @cached_property
    def script(self):  # pragma: no cover
        return ScriptSummary.make_one(self.boto3_raw_data["script"])

    exportDataSetNames = field("exportDataSetNames")

    @cached_property
    def properties(self):  # pragma: no cover
        return MainframeActionProperties.make_one(self.boto3_raw_data["properties"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TN3270StepInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TN3270StepInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceOutput:
    boto3_raw_data: "type_defs.ResourceOutputTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def type(self):  # pragma: no cover
        return ResourceTypeOutput.make_one(self.boto3_raw_data["type"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MainframeActionTypeOutput:
    boto3_raw_data: "type_defs.MainframeActionTypeOutputTypeDef" = dataclasses.field()

    @cached_property
    def batch(self):  # pragma: no cover
        return BatchOutput.make_one(self.boto3_raw_data["batch"])

    @cached_property
    def tn3270(self):  # pragma: no cover
        return TN3270Output.make_one(self.boto3_raw_data["tn3270"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MainframeActionTypeOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MainframeActionTypeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompareFileType:
    boto3_raw_data: "type_defs.CompareFileTypeTypeDef" = dataclasses.field()

    @cached_property
    def datasets(self):  # pragma: no cover
        return CompareDataSetsSummary.make_one(self.boto3_raw_data["datasets"])

    @cached_property
    def databaseCDC(self):  # pragma: no cover
        return CompareDatabaseCDCSummary.make_one(self.boto3_raw_data["databaseCDC"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CompareFileTypeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CompareFileTypeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputFileOutput:
    boto3_raw_data: "type_defs.InputFileOutputTypeDef" = dataclasses.field()

    sourceLocation = field("sourceLocation")
    targetLocation = field("targetLocation")

    @cached_property
    def fileMetadata(self):  # pragma: no cover
        return FileMetadataOutput.make_one(self.boto3_raw_data["fileMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputFileOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputFileOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceActionSummary:
    boto3_raw_data: "type_defs.ResourceActionSummaryTypeDef" = dataclasses.field()

    @cached_property
    def cloudFormation(self):  # pragma: no cover
        return CloudFormationStepSummary.make_one(self.boto3_raw_data["cloudFormation"])

    @cached_property
    def m2ManagedApplication(self):  # pragma: no cover
        return M2ManagedApplicationStepSummary.make_one(
            self.boto3_raw_data["m2ManagedApplication"]
        )

    @cached_property
    def m2NonManagedApplication(self):  # pragma: no cover
        return M2NonManagedApplicationStepSummary.make_one(
            self.boto3_raw_data["m2NonManagedApplication"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ResourceActionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ResourceActionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchSummary:
    boto3_raw_data: "type_defs.BatchSummaryTypeDef" = dataclasses.field()

    @cached_property
    def stepInput(self):  # pragma: no cover
        return BatchStepInput.make_one(self.boto3_raw_data["stepInput"])

    @cached_property
    def stepOutput(self):  # pragma: no cover
        return BatchStepOutput.make_one(self.boto3_raw_data["stepOutput"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BatchSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BatchSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TN3270Summary:
    boto3_raw_data: "type_defs.TN3270SummaryTypeDef" = dataclasses.field()

    @cached_property
    def stepInput(self):  # pragma: no cover
        return TN3270StepInput.make_one(self.boto3_raw_data["stepInput"])

    @cached_property
    def stepOutput(self):  # pragma: no cover
        return TN3270StepOutput.make_one(self.boto3_raw_data["stepOutput"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TN3270SummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TN3270SummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTestConfigurationResponse:
    boto3_raw_data: "type_defs.GetTestConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    testConfigurationId = field("testConfigurationId")
    name = field("name")
    testConfigurationArn = field("testConfigurationArn")

    @cached_property
    def latestVersion(self):  # pragma: no cover
        return TestConfigurationLatestVersion.make_one(
            self.boto3_raw_data["latestVersion"]
        )

    testConfigurationVersion = field("testConfigurationVersion")
    status = field("status")
    statusReason = field("statusReason")
    creationTime = field("creationTime")
    lastUpdateTime = field("lastUpdateTime")
    description = field("description")

    @cached_property
    def resources(self):  # pragma: no cover
        return ResourceOutput.make_many(self.boto3_raw_data["resources"])

    properties = field("properties")
    tags = field("tags")

    @cached_property
    def serviceSettings(self):  # pragma: no cover
        return ServiceSettings.make_one(self.boto3_raw_data["serviceSettings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTestConfigurationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTestConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MainframeActionOutput:
    boto3_raw_data: "type_defs.MainframeActionOutputTypeDef" = dataclasses.field()

    resource = field("resource")

    @cached_property
    def actionType(self):  # pragma: no cover
        return MainframeActionTypeOutput.make_one(self.boto3_raw_data["actionType"])

    @cached_property
    def properties(self):  # pragma: no cover
        return MainframeActionProperties.make_one(self.boto3_raw_data["properties"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MainframeActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MainframeActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MainframeActionType:
    boto3_raw_data: "type_defs.MainframeActionTypeTypeDef" = dataclasses.field()

    batch = field("batch")
    tn3270 = field("tn3270")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MainframeActionTypeTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MainframeActionTypeTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Resource:
    boto3_raw_data: "type_defs.ResourceTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class File:
    boto3_raw_data: "type_defs.FileTypeDef" = dataclasses.field()

    @cached_property
    def fileType(self):  # pragma: no cover
        return CompareFileType.make_one(self.boto3_raw_data["fileType"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FileTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputOutput:
    boto3_raw_data: "type_defs.InputOutputTypeDef" = dataclasses.field()

    @cached_property
    def file(self):  # pragma: no cover
        return InputFileOutput.make_one(self.boto3_raw_data["file"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputFile:
    boto3_raw_data: "type_defs.InputFileTypeDef" = dataclasses.field()

    sourceLocation = field("sourceLocation")
    targetLocation = field("targetLocation")
    fileMetadata = field("fileMetadata")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputFileTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputFileTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MainframeActionSummary:
    boto3_raw_data: "type_defs.MainframeActionSummaryTypeDef" = dataclasses.field()

    @cached_property
    def batch(self):  # pragma: no cover
        return BatchSummary.make_one(self.boto3_raw_data["batch"])

    @cached_property
    def tn3270(self):  # pragma: no cover
        return TN3270Summary.make_one(self.boto3_raw_data["tn3270"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MainframeActionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MainframeActionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompareActionSummary:
    boto3_raw_data: "type_defs.CompareActionSummaryTypeDef" = dataclasses.field()

    @cached_property
    def type(self):  # pragma: no cover
        return File.make_one(self.boto3_raw_data["type"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompareActionSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompareActionSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompareActionOutput:
    boto3_raw_data: "type_defs.CompareActionOutputTypeDef" = dataclasses.field()

    @cached_property
    def input(self):  # pragma: no cover
        return InputOutput.make_one(self.boto3_raw_data["input"])

    @cached_property
    def output(self):  # pragma: no cover
        return Output.make_one(self.boto3_raw_data["output"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CompareActionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CompareActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MainframeAction:
    boto3_raw_data: "type_defs.MainframeActionTypeDef" = dataclasses.field()

    resource = field("resource")
    actionType = field("actionType")

    @cached_property
    def properties(self):  # pragma: no cover
        return MainframeActionProperties.make_one(self.boto3_raw_data["properties"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MainframeActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MainframeActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTestConfigurationRequest:
    boto3_raw_data: "type_defs.CreateTestConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    resources = field("resources")
    description = field("description")
    properties = field("properties")
    clientToken = field("clientToken")
    tags = field("tags")

    @cached_property
    def serviceSettings(self):  # pragma: no cover
        return ServiceSettings.make_one(self.boto3_raw_data["serviceSettings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateTestConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTestConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTestConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateTestConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    testConfigurationId = field("testConfigurationId")
    description = field("description")
    resources = field("resources")
    properties = field("properties")

    @cached_property
    def serviceSettings(self):  # pragma: no cover
        return ServiceSettings.make_one(self.boto3_raw_data["serviceSettings"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateTestConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTestConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepRunSummary:
    boto3_raw_data: "type_defs.StepRunSummaryTypeDef" = dataclasses.field()

    @cached_property
    def mainframeAction(self):  # pragma: no cover
        return MainframeActionSummary.make_one(self.boto3_raw_data["mainframeAction"])

    @cached_property
    def compareAction(self):  # pragma: no cover
        return CompareActionSummary.make_one(self.boto3_raw_data["compareAction"])

    @cached_property
    def resourceAction(self):  # pragma: no cover
        return ResourceActionSummary.make_one(self.boto3_raw_data["resourceAction"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepRunSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StepRunSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepActionOutput:
    boto3_raw_data: "type_defs.StepActionOutputTypeDef" = dataclasses.field()

    @cached_property
    def resourceAction(self):  # pragma: no cover
        return ResourceAction.make_one(self.boto3_raw_data["resourceAction"])

    @cached_property
    def mainframeAction(self):  # pragma: no cover
        return MainframeActionOutput.make_one(self.boto3_raw_data["mainframeAction"])

    @cached_property
    def compareAction(self):  # pragma: no cover
        return CompareActionOutput.make_one(self.boto3_raw_data["compareAction"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepActionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StepActionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Input:
    boto3_raw_data: "type_defs.InputTypeDef" = dataclasses.field()

    file = field("file")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTestRunStepResponse:
    boto3_raw_data: "type_defs.GetTestRunStepResponseTypeDef" = dataclasses.field()

    stepName = field("stepName")
    testRunId = field("testRunId")
    testCaseId = field("testCaseId")
    testCaseVersion = field("testCaseVersion")
    testSuiteId = field("testSuiteId")
    testSuiteVersion = field("testSuiteVersion")
    beforeStep = field("beforeStep")
    afterStep = field("afterStep")
    status = field("status")
    statusReason = field("statusReason")
    runStartTime = field("runStartTime")
    runEndTime = field("runEndTime")

    @cached_property
    def stepRunSummary(self):  # pragma: no cover
        return StepRunSummary.make_one(self.boto3_raw_data["stepRunSummary"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTestRunStepResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTestRunStepResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepOutput:
    boto3_raw_data: "type_defs.StepOutputTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def action(self):  # pragma: no cover
        return StepActionOutput.make_one(self.boto3_raw_data["action"])

    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StepOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTestCaseResponse:
    boto3_raw_data: "type_defs.GetTestCaseResponseTypeDef" = dataclasses.field()

    testCaseId = field("testCaseId")
    testCaseArn = field("testCaseArn")
    name = field("name")
    description = field("description")

    @cached_property
    def latestVersion(self):  # pragma: no cover
        return TestCaseLatestVersion.make_one(self.boto3_raw_data["latestVersion"])

    testCaseVersion = field("testCaseVersion")
    status = field("status")
    statusReason = field("statusReason")
    creationTime = field("creationTime")
    lastUpdateTime = field("lastUpdateTime")

    @cached_property
    def steps(self):  # pragma: no cover
        return StepOutput.make_many(self.boto3_raw_data["steps"])

    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTestCaseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTestCaseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTestSuiteResponse:
    boto3_raw_data: "type_defs.GetTestSuiteResponseTypeDef" = dataclasses.field()

    testSuiteId = field("testSuiteId")
    name = field("name")

    @cached_property
    def latestVersion(self):  # pragma: no cover
        return TestSuiteLatestVersion.make_one(self.boto3_raw_data["latestVersion"])

    testSuiteVersion = field("testSuiteVersion")
    status = field("status")
    statusReason = field("statusReason")
    testSuiteArn = field("testSuiteArn")
    creationTime = field("creationTime")
    lastUpdateTime = field("lastUpdateTime")
    description = field("description")

    @cached_property
    def beforeSteps(self):  # pragma: no cover
        return StepOutput.make_many(self.boto3_raw_data["beforeSteps"])

    @cached_property
    def afterSteps(self):  # pragma: no cover
        return StepOutput.make_many(self.boto3_raw_data["afterSteps"])

    @cached_property
    def testCases(self):  # pragma: no cover
        return TestCasesOutput.make_one(self.boto3_raw_data["testCases"])

    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTestSuiteResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTestSuiteResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CompareAction:
    boto3_raw_data: "type_defs.CompareActionTypeDef" = dataclasses.field()

    input = field("input")

    @cached_property
    def output(self):  # pragma: no cover
        return Output.make_one(self.boto3_raw_data["output"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CompareActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CompareActionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StepAction:
    boto3_raw_data: "type_defs.StepActionTypeDef" = dataclasses.field()

    @cached_property
    def resourceAction(self):  # pragma: no cover
        return ResourceAction.make_one(self.boto3_raw_data["resourceAction"])

    mainframeAction = field("mainframeAction")
    compareAction = field("compareAction")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepActionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StepActionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Step:
    boto3_raw_data: "type_defs.StepTypeDef" = dataclasses.field()

    name = field("name")
    action = field("action")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StepTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StepTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTestCaseRequest:
    boto3_raw_data: "type_defs.CreateTestCaseRequestTypeDef" = dataclasses.field()

    name = field("name")
    steps = field("steps")
    description = field("description")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTestCaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTestCaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTestSuiteRequest:
    boto3_raw_data: "type_defs.CreateTestSuiteRequestTypeDef" = dataclasses.field()

    name = field("name")
    testCases = field("testCases")
    description = field("description")
    beforeSteps = field("beforeSteps")
    afterSteps = field("afterSteps")
    clientToken = field("clientToken")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTestSuiteRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTestSuiteRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTestCaseRequest:
    boto3_raw_data: "type_defs.UpdateTestCaseRequestTypeDef" = dataclasses.field()

    testCaseId = field("testCaseId")
    description = field("description")
    steps = field("steps")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTestCaseRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTestCaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTestSuiteRequest:
    boto3_raw_data: "type_defs.UpdateTestSuiteRequestTypeDef" = dataclasses.field()

    testSuiteId = field("testSuiteId")
    description = field("description")
    beforeSteps = field("beforeSteps")
    afterSteps = field("afterSteps")
    testCases = field("testCases")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTestSuiteRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTestSuiteRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
