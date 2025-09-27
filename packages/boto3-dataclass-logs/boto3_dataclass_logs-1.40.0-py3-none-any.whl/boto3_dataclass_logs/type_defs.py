# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_logs import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AccountPolicy:
    boto3_raw_data: "type_defs.AccountPolicyTypeDef" = dataclasses.field()

    policyName = field("policyName")
    policyDocument = field("policyDocument")
    lastUpdatedTime = field("lastUpdatedTime")
    policyType = field("policyType")
    scope = field("scope")
    selectionCriteria = field("selectionCriteria")
    accountId = field("accountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountPolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddKeyEntry:
    boto3_raw_data: "type_defs.AddKeyEntryTypeDef" = dataclasses.field()

    key = field("key")
    value = field("value")
    overwriteIfExists = field("overwriteIfExists")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddKeyEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddKeyEntryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnomalyDetector:
    boto3_raw_data: "type_defs.AnomalyDetectorTypeDef" = dataclasses.field()

    anomalyDetectorArn = field("anomalyDetectorArn")
    detectorName = field("detectorName")
    logGroupArnList = field("logGroupArnList")
    evaluationFrequency = field("evaluationFrequency")
    filterPattern = field("filterPattern")
    anomalyDetectorStatus = field("anomalyDetectorStatus")
    kmsKeyId = field("kmsKeyId")
    creationTimeStamp = field("creationTimeStamp")
    lastModifiedTimeStamp = field("lastModifiedTimeStamp")
    anomalyVisibilityTime = field("anomalyVisibilityTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnomalyDetectorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnomalyDetectorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogEvent:
    boto3_raw_data: "type_defs.LogEventTypeDef" = dataclasses.field()

    timestamp = field("timestamp")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LogEventTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PatternToken:
    boto3_raw_data: "type_defs.PatternTokenTypeDef" = dataclasses.field()

    dynamicTokenPosition = field("dynamicTokenPosition")
    isDynamic = field("isDynamic")
    tokenString = field("tokenString")
    enumerations = field("enumerations")
    inferredTokenName = field("inferredTokenName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PatternTokenTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PatternTokenTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateKmsKeyRequest:
    boto3_raw_data: "type_defs.AssociateKmsKeyRequestTypeDef" = dataclasses.field()

    kmsKeyId = field("kmsKeyId")
    logGroupName = field("logGroupName")
    resourceIdentifier = field("resourceIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociateKmsKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociateKmsKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CSVOutput:
    boto3_raw_data: "type_defs.CSVOutputTypeDef" = dataclasses.field()

    quoteCharacter = field("quoteCharacter")
    delimiter = field("delimiter")
    columns = field("columns")
    source = field("source")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CSVOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CSVOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CSV:
    boto3_raw_data: "type_defs.CSVTypeDef" = dataclasses.field()

    quoteCharacter = field("quoteCharacter")
    delimiter = field("delimiter")
    columns = field("columns")
    source = field("source")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CSVTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CSVTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CancelExportTaskRequest:
    boto3_raw_data: "type_defs.CancelExportTaskRequestTypeDef" = dataclasses.field()

    taskId = field("taskId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CancelExportTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CancelExportTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3DeliveryConfiguration:
    boto3_raw_data: "type_defs.S3DeliveryConfigurationTypeDef" = dataclasses.field()

    suffixPath = field("suffixPath")
    enableHiveCompatiblePath = field("enableHiveCompatiblePath")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.S3DeliveryConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.S3DeliveryConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RecordField:
    boto3_raw_data: "type_defs.RecordFieldTypeDef" = dataclasses.field()

    name = field("name")
    mandatory = field("mandatory")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RecordFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RecordFieldTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyValueEntry:
    boto3_raw_data: "type_defs.CopyValueEntryTypeDef" = dataclasses.field()

    source = field("source")
    target = field("target")
    overwriteIfExists = field("overwriteIfExists")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CopyValueEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CopyValueEntryTypeDef"]],
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
class CreateExportTaskRequest:
    boto3_raw_data: "type_defs.CreateExportTaskRequestTypeDef" = dataclasses.field()

    logGroupName = field("logGroupName")
    fromTime = field("fromTime")
    to = field("to")
    destination = field("destination")
    taskName = field("taskName")
    logStreamNamePrefix = field("logStreamNamePrefix")
    destinationPrefix = field("destinationPrefix")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateExportTaskRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExportTaskRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLogAnomalyDetectorRequest:
    boto3_raw_data: "type_defs.CreateLogAnomalyDetectorRequestTypeDef" = (
        dataclasses.field()
    )

    logGroupArnList = field("logGroupArnList")
    detectorName = field("detectorName")
    evaluationFrequency = field("evaluationFrequency")
    filterPattern = field("filterPattern")
    kmsKeyId = field("kmsKeyId")
    anomalyVisibilityTime = field("anomalyVisibilityTime")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateLogAnomalyDetectorRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLogAnomalyDetectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLogGroupRequest:
    boto3_raw_data: "type_defs.CreateLogGroupRequestTypeDef" = dataclasses.field()

    logGroupName = field("logGroupName")
    kmsKeyId = field("kmsKeyId")
    tags = field("tags")
    logGroupClass = field("logGroupClass")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLogGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLogGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLogStreamRequest:
    boto3_raw_data: "type_defs.CreateLogStreamRequestTypeDef" = dataclasses.field()

    logGroupName = field("logGroupName")
    logStreamName = field("logStreamName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLogStreamRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLogStreamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DateTimeConverterOutput:
    boto3_raw_data: "type_defs.DateTimeConverterOutputTypeDef" = dataclasses.field()

    source = field("source")
    target = field("target")
    matchPatterns = field("matchPatterns")
    targetFormat = field("targetFormat")
    sourceTimezone = field("sourceTimezone")
    targetTimezone = field("targetTimezone")
    locale = field("locale")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DateTimeConverterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DateTimeConverterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DateTimeConverter:
    boto3_raw_data: "type_defs.DateTimeConverterTypeDef" = dataclasses.field()

    source = field("source")
    target = field("target")
    matchPatterns = field("matchPatterns")
    targetFormat = field("targetFormat")
    sourceTimezone = field("sourceTimezone")
    targetTimezone = field("targetTimezone")
    locale = field("locale")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DateTimeConverterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DateTimeConverterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAccountPolicyRequest:
    boto3_raw_data: "type_defs.DeleteAccountPolicyRequestTypeDef" = dataclasses.field()

    policyName = field("policyName")
    policyType = field("policyType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAccountPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAccountPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDataProtectionPolicyRequest:
    boto3_raw_data: "type_defs.DeleteDataProtectionPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    logGroupIdentifier = field("logGroupIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDataProtectionPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDataProtectionPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDeliveryDestinationPolicyRequest:
    boto3_raw_data: "type_defs.DeleteDeliveryDestinationPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    deliveryDestinationName = field("deliveryDestinationName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteDeliveryDestinationPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDeliveryDestinationPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDeliveryDestinationRequest:
    boto3_raw_data: "type_defs.DeleteDeliveryDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteDeliveryDestinationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDeliveryDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDeliveryRequest:
    boto3_raw_data: "type_defs.DeleteDeliveryRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDeliveryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDeliveryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDeliverySourceRequest:
    boto3_raw_data: "type_defs.DeleteDeliverySourceRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDeliverySourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDeliverySourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDestinationRequest:
    boto3_raw_data: "type_defs.DeleteDestinationRequestTypeDef" = dataclasses.field()

    destinationName = field("destinationName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDestinationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIndexPolicyRequest:
    boto3_raw_data: "type_defs.DeleteIndexPolicyRequestTypeDef" = dataclasses.field()

    logGroupIdentifier = field("logGroupIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIndexPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIndexPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIntegrationRequest:
    boto3_raw_data: "type_defs.DeleteIntegrationRequestTypeDef" = dataclasses.field()

    integrationName = field("integrationName")
    force = field("force")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIntegrationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIntegrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKeysOutput:
    boto3_raw_data: "type_defs.DeleteKeysOutputTypeDef" = dataclasses.field()

    withKeys = field("withKeys")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteKeysOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteKeysOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteKeys:
    boto3_raw_data: "type_defs.DeleteKeysTypeDef" = dataclasses.field()

    withKeys = field("withKeys")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteKeysTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeleteKeysTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLogAnomalyDetectorRequest:
    boto3_raw_data: "type_defs.DeleteLogAnomalyDetectorRequestTypeDef" = (
        dataclasses.field()
    )

    anomalyDetectorArn = field("anomalyDetectorArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteLogAnomalyDetectorRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLogAnomalyDetectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLogGroupRequest:
    boto3_raw_data: "type_defs.DeleteLogGroupRequestTypeDef" = dataclasses.field()

    logGroupName = field("logGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLogGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLogGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLogStreamRequest:
    boto3_raw_data: "type_defs.DeleteLogStreamRequestTypeDef" = dataclasses.field()

    logGroupName = field("logGroupName")
    logStreamName = field("logStreamName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLogStreamRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLogStreamRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMetricFilterRequest:
    boto3_raw_data: "type_defs.DeleteMetricFilterRequestTypeDef" = dataclasses.field()

    logGroupName = field("logGroupName")
    filterName = field("filterName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMetricFilterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMetricFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteQueryDefinitionRequest:
    boto3_raw_data: "type_defs.DeleteQueryDefinitionRequestTypeDef" = (
        dataclasses.field()
    )

    queryDefinitionId = field("queryDefinitionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteQueryDefinitionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteQueryDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteResourcePolicyRequest:
    boto3_raw_data: "type_defs.DeleteResourcePolicyRequestTypeDef" = dataclasses.field()

    policyName = field("policyName")
    resourceArn = field("resourceArn")
    expectedRevisionId = field("expectedRevisionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRetentionPolicyRequest:
    boto3_raw_data: "type_defs.DeleteRetentionPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    logGroupName = field("logGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRetentionPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRetentionPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSubscriptionFilterRequest:
    boto3_raw_data: "type_defs.DeleteSubscriptionFilterRequestTypeDef" = (
        dataclasses.field()
    )

    logGroupName = field("logGroupName")
    filterName = field("filterName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteSubscriptionFilterRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSubscriptionFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTransformerRequest:
    boto3_raw_data: "type_defs.DeleteTransformerRequestTypeDef" = dataclasses.field()

    logGroupIdentifier = field("logGroupIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTransformerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTransformerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeliveryDestinationConfiguration:
    boto3_raw_data: "type_defs.DeliveryDestinationConfigurationTypeDef" = (
        dataclasses.field()
    )

    destinationResourceArn = field("destinationResourceArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeliveryDestinationConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeliveryDestinationConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeliverySource:
    boto3_raw_data: "type_defs.DeliverySourceTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    resourceArns = field("resourceArns")
    service = field("service")
    logType = field("logType")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeliverySourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeliverySourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountPoliciesRequest:
    boto3_raw_data: "type_defs.DescribeAccountPoliciesRequestTypeDef" = (
        dataclasses.field()
    )

    policyType = field("policyType")
    policyName = field("policyName")
    accountIdentifiers = field("accountIdentifiers")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAccountPoliciesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountPoliciesRequestTypeDef"]
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
class DescribeConfigurationTemplatesRequest:
    boto3_raw_data: "type_defs.DescribeConfigurationTemplatesRequestTypeDef" = (
        dataclasses.field()
    )

    service = field("service")
    logTypes = field("logTypes")
    resourceTypes = field("resourceTypes")
    deliveryDestinationTypes = field("deliveryDestinationTypes")
    nextToken = field("nextToken")
    limit = field("limit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConfigurationTemplatesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigurationTemplatesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDeliveriesRequest:
    boto3_raw_data: "type_defs.DescribeDeliveriesRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    limit = field("limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDeliveriesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDeliveriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDeliveryDestinationsRequest:
    boto3_raw_data: "type_defs.DescribeDeliveryDestinationsRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    limit = field("limit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDeliveryDestinationsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDeliveryDestinationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDeliverySourcesRequest:
    boto3_raw_data: "type_defs.DescribeDeliverySourcesRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    limit = field("limit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDeliverySourcesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDeliverySourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDestinationsRequest:
    boto3_raw_data: "type_defs.DescribeDestinationsRequestTypeDef" = dataclasses.field()

    DestinationNamePrefix = field("DestinationNamePrefix")
    nextToken = field("nextToken")
    limit = field("limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDestinationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDestinationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Destination:
    boto3_raw_data: "type_defs.DestinationTypeDef" = dataclasses.field()

    destinationName = field("destinationName")
    targetArn = field("targetArn")
    roleArn = field("roleArn")
    accessPolicy = field("accessPolicy")
    arn = field("arn")
    creationTime = field("creationTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DestinationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DestinationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeExportTasksRequest:
    boto3_raw_data: "type_defs.DescribeExportTasksRequestTypeDef" = dataclasses.field()

    taskId = field("taskId")
    statusCode = field("statusCode")
    nextToken = field("nextToken")
    limit = field("limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeExportTasksRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExportTasksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFieldIndexesRequest:
    boto3_raw_data: "type_defs.DescribeFieldIndexesRequestTypeDef" = dataclasses.field()

    logGroupIdentifiers = field("logGroupIdentifiers")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFieldIndexesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFieldIndexesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldIndex:
    boto3_raw_data: "type_defs.FieldIndexTypeDef" = dataclasses.field()

    logGroupIdentifier = field("logGroupIdentifier")
    fieldIndexName = field("fieldIndexName")
    lastScanTime = field("lastScanTime")
    firstEventTime = field("firstEventTime")
    lastEventTime = field("lastEventTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldIndexTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FieldIndexTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIndexPoliciesRequest:
    boto3_raw_data: "type_defs.DescribeIndexPoliciesRequestTypeDef" = (
        dataclasses.field()
    )

    logGroupIdentifiers = field("logGroupIdentifiers")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeIndexPoliciesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIndexPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IndexPolicy:
    boto3_raw_data: "type_defs.IndexPolicyTypeDef" = dataclasses.field()

    logGroupIdentifier = field("logGroupIdentifier")
    lastUpdateTime = field("lastUpdateTime")
    policyDocument = field("policyDocument")
    policyName = field("policyName")
    source = field("source")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IndexPolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IndexPolicyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLogGroupsRequest:
    boto3_raw_data: "type_defs.DescribeLogGroupsRequestTypeDef" = dataclasses.field()

    accountIdentifiers = field("accountIdentifiers")
    logGroupNamePrefix = field("logGroupNamePrefix")
    logGroupNamePattern = field("logGroupNamePattern")
    nextToken = field("nextToken")
    limit = field("limit")
    includeLinkedAccounts = field("includeLinkedAccounts")
    logGroupClass = field("logGroupClass")
    logGroupIdentifiers = field("logGroupIdentifiers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLogGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLogGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogGroup:
    boto3_raw_data: "type_defs.LogGroupTypeDef" = dataclasses.field()

    logGroupName = field("logGroupName")
    creationTime = field("creationTime")
    retentionInDays = field("retentionInDays")
    metricFilterCount = field("metricFilterCount")
    arn = field("arn")
    storedBytes = field("storedBytes")
    kmsKeyId = field("kmsKeyId")
    dataProtectionStatus = field("dataProtectionStatus")
    inheritedProperties = field("inheritedProperties")
    logGroupClass = field("logGroupClass")
    logGroupArn = field("logGroupArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LogGroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLogStreamsRequest:
    boto3_raw_data: "type_defs.DescribeLogStreamsRequestTypeDef" = dataclasses.field()

    logGroupName = field("logGroupName")
    logGroupIdentifier = field("logGroupIdentifier")
    logStreamNamePrefix = field("logStreamNamePrefix")
    orderBy = field("orderBy")
    descending = field("descending")
    nextToken = field("nextToken")
    limit = field("limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLogStreamsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLogStreamsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogStream:
    boto3_raw_data: "type_defs.LogStreamTypeDef" = dataclasses.field()

    logStreamName = field("logStreamName")
    creationTime = field("creationTime")
    firstEventTimestamp = field("firstEventTimestamp")
    lastEventTimestamp = field("lastEventTimestamp")
    lastIngestionTime = field("lastIngestionTime")
    uploadSequenceToken = field("uploadSequenceToken")
    arn = field("arn")
    storedBytes = field("storedBytes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogStreamTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LogStreamTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMetricFiltersRequest:
    boto3_raw_data: "type_defs.DescribeMetricFiltersRequestTypeDef" = (
        dataclasses.field()
    )

    logGroupName = field("logGroupName")
    filterNamePrefix = field("filterNamePrefix")
    nextToken = field("nextToken")
    limit = field("limit")
    metricName = field("metricName")
    metricNamespace = field("metricNamespace")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeMetricFiltersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMetricFiltersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeQueriesRequest:
    boto3_raw_data: "type_defs.DescribeQueriesRequestTypeDef" = dataclasses.field()

    logGroupName = field("logGroupName")
    status = field("status")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    queryLanguage = field("queryLanguage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeQueriesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeQueriesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryInfo:
    boto3_raw_data: "type_defs.QueryInfoTypeDef" = dataclasses.field()

    queryLanguage = field("queryLanguage")
    queryId = field("queryId")
    queryString = field("queryString")
    status = field("status")
    createTime = field("createTime")
    logGroupName = field("logGroupName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryInfoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryInfoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeQueryDefinitionsRequest:
    boto3_raw_data: "type_defs.DescribeQueryDefinitionsRequestTypeDef" = (
        dataclasses.field()
    )

    queryLanguage = field("queryLanguage")
    queryDefinitionNamePrefix = field("queryDefinitionNamePrefix")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeQueryDefinitionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeQueryDefinitionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryDefinition:
    boto3_raw_data: "type_defs.QueryDefinitionTypeDef" = dataclasses.field()

    queryLanguage = field("queryLanguage")
    queryDefinitionId = field("queryDefinitionId")
    name = field("name")
    queryString = field("queryString")
    lastModified = field("lastModified")
    logGroupNames = field("logGroupNames")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryDefinitionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryDefinitionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourcePoliciesRequest:
    boto3_raw_data: "type_defs.DescribeResourcePoliciesRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    limit = field("limit")
    resourceArn = field("resourceArn")
    policyScope = field("policyScope")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeResourcePoliciesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourcePoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourcePolicy:
    boto3_raw_data: "type_defs.ResourcePolicyTypeDef" = dataclasses.field()

    policyName = field("policyName")
    policyDocument = field("policyDocument")
    lastUpdatedTime = field("lastUpdatedTime")
    policyScope = field("policyScope")
    resourceArn = field("resourceArn")
    revisionId = field("revisionId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourcePolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourcePolicyTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSubscriptionFiltersRequest:
    boto3_raw_data: "type_defs.DescribeSubscriptionFiltersRequestTypeDef" = (
        dataclasses.field()
    )

    logGroupName = field("logGroupName")
    filterNamePrefix = field("filterNamePrefix")
    nextToken = field("nextToken")
    limit = field("limit")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSubscriptionFiltersRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSubscriptionFiltersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubscriptionFilter:
    boto3_raw_data: "type_defs.SubscriptionFilterTypeDef" = dataclasses.field()

    filterName = field("filterName")
    logGroupName = field("logGroupName")
    filterPattern = field("filterPattern")
    destinationArn = field("destinationArn")
    roleArn = field("roleArn")
    distribution = field("distribution")
    applyOnTransformedLogs = field("applyOnTransformedLogs")
    creationTime = field("creationTime")
    fieldSelectionCriteria = field("fieldSelectionCriteria")
    emitSystemFields = field("emitSystemFields")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubscriptionFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubscriptionFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateKmsKeyRequest:
    boto3_raw_data: "type_defs.DisassociateKmsKeyRequestTypeDef" = dataclasses.field()

    logGroupName = field("logGroupName")
    resourceIdentifier = field("resourceIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DisassociateKmsKeyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateKmsKeyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Entity:
    boto3_raw_data: "type_defs.EntityTypeDef" = dataclasses.field()

    keyAttributes = field("keyAttributes")
    attributes = field("attributes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EntityTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EntityTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportTaskExecutionInfo:
    boto3_raw_data: "type_defs.ExportTaskExecutionInfoTypeDef" = dataclasses.field()

    creationTime = field("creationTime")
    completionTime = field("completionTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ExportTaskExecutionInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportTaskExecutionInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportTaskStatus:
    boto3_raw_data: "type_defs.ExportTaskStatusTypeDef" = dataclasses.field()

    code = field("code")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportTaskStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExportTaskStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldsData:
    boto3_raw_data: "type_defs.FieldsDataTypeDef" = dataclasses.field()

    data = field("data")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldsDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FieldsDataTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterLogEventsRequest:
    boto3_raw_data: "type_defs.FilterLogEventsRequestTypeDef" = dataclasses.field()

    logGroupName = field("logGroupName")
    logGroupIdentifier = field("logGroupIdentifier")
    logStreamNames = field("logStreamNames")
    logStreamNamePrefix = field("logStreamNamePrefix")
    startTime = field("startTime")
    endTime = field("endTime")
    filterPattern = field("filterPattern")
    nextToken = field("nextToken")
    limit = field("limit")
    interleaved = field("interleaved")
    unmask = field("unmask")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FilterLogEventsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FilterLogEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilteredLogEvent:
    boto3_raw_data: "type_defs.FilteredLogEventTypeDef" = dataclasses.field()

    logStreamName = field("logStreamName")
    timestamp = field("timestamp")
    message = field("message")
    ingestionTime = field("ingestionTime")
    eventId = field("eventId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilteredLogEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FilteredLogEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchedLogStream:
    boto3_raw_data: "type_defs.SearchedLogStreamTypeDef" = dataclasses.field()

    logStreamName = field("logStreamName")
    searchedCompletely = field("searchedCompletely")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SearchedLogStreamTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchedLogStreamTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDataProtectionPolicyRequest:
    boto3_raw_data: "type_defs.GetDataProtectionPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    logGroupIdentifier = field("logGroupIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDataProtectionPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataProtectionPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeliveryDestinationPolicyRequest:
    boto3_raw_data: "type_defs.GetDeliveryDestinationPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    deliveryDestinationName = field("deliveryDestinationName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDeliveryDestinationPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeliveryDestinationPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Policy:
    boto3_raw_data: "type_defs.PolicyTypeDef" = dataclasses.field()

    deliveryDestinationPolicy = field("deliveryDestinationPolicy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PolicyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PolicyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeliveryDestinationRequest:
    boto3_raw_data: "type_defs.GetDeliveryDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDeliveryDestinationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeliveryDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeliveryRequest:
    boto3_raw_data: "type_defs.GetDeliveryRequestTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeliveryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeliveryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeliverySourceRequest:
    boto3_raw_data: "type_defs.GetDeliverySourceRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeliverySourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeliverySourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIntegrationRequest:
    boto3_raw_data: "type_defs.GetIntegrationRequestTypeDef" = dataclasses.field()

    integrationName = field("integrationName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIntegrationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIntegrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLogAnomalyDetectorRequest:
    boto3_raw_data: "type_defs.GetLogAnomalyDetectorRequestTypeDef" = (
        dataclasses.field()
    )

    anomalyDetectorArn = field("anomalyDetectorArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLogAnomalyDetectorRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLogAnomalyDetectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLogEventsRequest:
    boto3_raw_data: "type_defs.GetLogEventsRequestTypeDef" = dataclasses.field()

    logStreamName = field("logStreamName")
    logGroupName = field("logGroupName")
    logGroupIdentifier = field("logGroupIdentifier")
    startTime = field("startTime")
    endTime = field("endTime")
    nextToken = field("nextToken")
    limit = field("limit")
    startFromHead = field("startFromHead")
    unmask = field("unmask")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLogEventsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLogEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OutputLogEvent:
    boto3_raw_data: "type_defs.OutputLogEventTypeDef" = dataclasses.field()

    timestamp = field("timestamp")
    message = field("message")
    ingestionTime = field("ingestionTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OutputLogEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OutputLogEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLogGroupFieldsRequest:
    boto3_raw_data: "type_defs.GetLogGroupFieldsRequestTypeDef" = dataclasses.field()

    logGroupName = field("logGroupName")
    time = field("time")
    logGroupIdentifier = field("logGroupIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLogGroupFieldsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLogGroupFieldsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogGroupField:
    boto3_raw_data: "type_defs.LogGroupFieldTypeDef" = dataclasses.field()

    name = field("name")
    percent = field("percent")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogGroupFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LogGroupFieldTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLogObjectRequest:
    boto3_raw_data: "type_defs.GetLogObjectRequestTypeDef" = dataclasses.field()

    logObjectPointer = field("logObjectPointer")
    unmask = field("unmask")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLogObjectRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLogObjectRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InternalStreamingException:
    boto3_raw_data: "type_defs.InternalStreamingExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InternalStreamingExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InternalStreamingExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLogRecordRequest:
    boto3_raw_data: "type_defs.GetLogRecordRequestTypeDef" = dataclasses.field()

    logRecordPointer = field("logRecordPointer")
    unmask = field("unmask")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLogRecordRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLogRecordRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryResultsRequest:
    boto3_raw_data: "type_defs.GetQueryResultsRequestTypeDef" = dataclasses.field()

    queryId = field("queryId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQueryResultsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueryResultsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryStatistics:
    boto3_raw_data: "type_defs.QueryStatisticsTypeDef" = dataclasses.field()

    recordsMatched = field("recordsMatched")
    recordsScanned = field("recordsScanned")
    estimatedRecordsSkipped = field("estimatedRecordsSkipped")
    bytesScanned = field("bytesScanned")
    estimatedBytesSkipped = field("estimatedBytesSkipped")
    logGroupsScanned = field("logGroupsScanned")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryStatisticsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryStatisticsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResultField:
    boto3_raw_data: "type_defs.ResultFieldTypeDef" = dataclasses.field()

    field = field("field")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResultFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResultFieldTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTransformerRequest:
    boto3_raw_data: "type_defs.GetTransformerRequestTypeDef" = dataclasses.field()

    logGroupIdentifier = field("logGroupIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTransformerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTransformerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Grok:
    boto3_raw_data: "type_defs.GrokTypeDef" = dataclasses.field()

    match = field("match")
    source = field("source")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GrokTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GrokTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InputLogEvent:
    boto3_raw_data: "type_defs.InputLogEventTypeDef" = dataclasses.field()

    timestamp = field("timestamp")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InputLogEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InputLogEventTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntegrationSummary:
    boto3_raw_data: "type_defs.IntegrationSummaryTypeDef" = dataclasses.field()

    integrationName = field("integrationName")
    integrationType = field("integrationType")
    integrationStatus = field("integrationStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IntegrationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntegrationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnomaliesRequest:
    boto3_raw_data: "type_defs.ListAnomaliesRequestTypeDef" = dataclasses.field()

    anomalyDetectorArn = field("anomalyDetectorArn")
    suppressionState = field("suppressionState")
    limit = field("limit")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAnomaliesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnomaliesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIntegrationsRequest:
    boto3_raw_data: "type_defs.ListIntegrationsRequestTypeDef" = dataclasses.field()

    integrationNamePrefix = field("integrationNamePrefix")
    integrationType = field("integrationType")
    integrationStatus = field("integrationStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIntegrationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIntegrationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLogAnomalyDetectorsRequest:
    boto3_raw_data: "type_defs.ListLogAnomalyDetectorsRequestTypeDef" = (
        dataclasses.field()
    )

    filterLogGroupArn = field("filterLogGroupArn")
    limit = field("limit")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListLogAnomalyDetectorsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLogAnomalyDetectorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLogGroupsForQueryRequest:
    boto3_raw_data: "type_defs.ListLogGroupsForQueryRequestTypeDef" = (
        dataclasses.field()
    )

    queryId = field("queryId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLogGroupsForQueryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLogGroupsForQueryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLogGroupsRequest:
    boto3_raw_data: "type_defs.ListLogGroupsRequestTypeDef" = dataclasses.field()

    logGroupNamePattern = field("logGroupNamePattern")
    logGroupClass = field("logGroupClass")
    includeLinkedAccounts = field("includeLinkedAccounts")
    accountIdentifiers = field("accountIdentifiers")
    nextToken = field("nextToken")
    limit = field("limit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLogGroupsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLogGroupsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LogGroupSummary:
    boto3_raw_data: "type_defs.LogGroupSummaryTypeDef" = dataclasses.field()

    logGroupName = field("logGroupName")
    logGroupArn = field("logGroupArn")
    logGroupClass = field("logGroupClass")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LogGroupSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LogGroupSummaryTypeDef"]],
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
class ListTagsLogGroupRequest:
    boto3_raw_data: "type_defs.ListTagsLogGroupRequestTypeDef" = dataclasses.field()

    logGroupName = field("logGroupName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsLogGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsLogGroupRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListToMap:
    boto3_raw_data: "type_defs.ListToMapTypeDef" = dataclasses.field()

    source = field("source")
    key = field("key")
    valueKey = field("valueKey")
    target = field("target")
    flatten = field("flatten")
    flattenedElement = field("flattenedElement")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListToMapTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ListToMapTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LiveTailSessionLogEvent:
    boto3_raw_data: "type_defs.LiveTailSessionLogEventTypeDef" = dataclasses.field()

    logStreamName = field("logStreamName")
    logGroupIdentifier = field("logGroupIdentifier")
    message = field("message")
    timestamp = field("timestamp")
    ingestionTime = field("ingestionTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LiveTailSessionLogEventTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LiveTailSessionLogEventTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LiveTailSessionMetadata:
    boto3_raw_data: "type_defs.LiveTailSessionMetadataTypeDef" = dataclasses.field()

    sampled = field("sampled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LiveTailSessionMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LiveTailSessionMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LiveTailSessionStart:
    boto3_raw_data: "type_defs.LiveTailSessionStartTypeDef" = dataclasses.field()

    requestId = field("requestId")
    sessionId = field("sessionId")
    logGroupIdentifiers = field("logGroupIdentifiers")
    logStreamNames = field("logStreamNames")
    logStreamNamePrefixes = field("logStreamNamePrefixes")
    logEventFilterPattern = field("logEventFilterPattern")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LiveTailSessionStartTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LiveTailSessionStartTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LowerCaseStringOutput:
    boto3_raw_data: "type_defs.LowerCaseStringOutputTypeDef" = dataclasses.field()

    withKeys = field("withKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LowerCaseStringOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LowerCaseStringOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LowerCaseString:
    boto3_raw_data: "type_defs.LowerCaseStringTypeDef" = dataclasses.field()

    withKeys = field("withKeys")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LowerCaseStringTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LowerCaseStringTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricFilterMatchRecord:
    boto3_raw_data: "type_defs.MetricFilterMatchRecordTypeDef" = dataclasses.field()

    eventNumber = field("eventNumber")
    eventMessage = field("eventMessage")
    extractedValues = field("extractedValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricFilterMatchRecordTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricFilterMatchRecordTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricTransformationOutput:
    boto3_raw_data: "type_defs.MetricTransformationOutputTypeDef" = dataclasses.field()

    metricName = field("metricName")
    metricNamespace = field("metricNamespace")
    metricValue = field("metricValue")
    defaultValue = field("defaultValue")
    dimensions = field("dimensions")
    unit = field("unit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricTransformationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricTransformationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricTransformation:
    boto3_raw_data: "type_defs.MetricTransformationTypeDef" = dataclasses.field()

    metricName = field("metricName")
    metricNamespace = field("metricNamespace")
    metricValue = field("metricValue")
    defaultValue = field("defaultValue")
    dimensions = field("dimensions")
    unit = field("unit")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MetricTransformationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MetricTransformationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MoveKeyEntry:
    boto3_raw_data: "type_defs.MoveKeyEntryTypeDef" = dataclasses.field()

    source = field("source")
    target = field("target")
    overwriteIfExists = field("overwriteIfExists")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MoveKeyEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MoveKeyEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenSearchResourceStatus:
    boto3_raw_data: "type_defs.OpenSearchResourceStatusTypeDef" = dataclasses.field()

    status = field("status")
    statusMessage = field("statusMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpenSearchResourceStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenSearchResourceStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenSearchResourceConfig:
    boto3_raw_data: "type_defs.OpenSearchResourceConfigTypeDef" = dataclasses.field()

    dataSourceRoleArn = field("dataSourceRoleArn")
    dashboardViewerPrincipals = field("dashboardViewerPrincipals")
    retentionDays = field("retentionDays")
    kmsKeyArn = field("kmsKeyArn")
    applicationArn = field("applicationArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpenSearchResourceConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenSearchResourceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParseCloudfront:
    boto3_raw_data: "type_defs.ParseCloudfrontTypeDef" = dataclasses.field()

    source = field("source")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParseCloudfrontTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParseCloudfrontTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParseJSON:
    boto3_raw_data: "type_defs.ParseJSONTypeDef" = dataclasses.field()

    source = field("source")
    destination = field("destination")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParseJSONTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParseJSONTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParseKeyValue:
    boto3_raw_data: "type_defs.ParseKeyValueTypeDef" = dataclasses.field()

    source = field("source")
    destination = field("destination")
    fieldDelimiter = field("fieldDelimiter")
    keyValueDelimiter = field("keyValueDelimiter")
    keyPrefix = field("keyPrefix")
    nonMatchValue = field("nonMatchValue")
    overwriteIfExists = field("overwriteIfExists")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParseKeyValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParseKeyValueTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParsePostgres:
    boto3_raw_data: "type_defs.ParsePostgresTypeDef" = dataclasses.field()

    source = field("source")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParsePostgresTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParsePostgresTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParseRoute53:
    boto3_raw_data: "type_defs.ParseRoute53TypeDef" = dataclasses.field()

    source = field("source")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParseRoute53TypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParseRoute53TypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParseToOCSF:
    boto3_raw_data: "type_defs.ParseToOCSFTypeDef" = dataclasses.field()

    eventSource = field("eventSource")
    ocsfVersion = field("ocsfVersion")
    source = field("source")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParseToOCSFTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParseToOCSFTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParseVPC:
    boto3_raw_data: "type_defs.ParseVPCTypeDef" = dataclasses.field()

    source = field("source")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParseVPCTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParseVPCTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ParseWAF:
    boto3_raw_data: "type_defs.ParseWAFTypeDef" = dataclasses.field()

    source = field("source")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ParseWAFTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ParseWAFTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrimStringOutput:
    boto3_raw_data: "type_defs.TrimStringOutputTypeDef" = dataclasses.field()

    withKeys = field("withKeys")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrimStringOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TrimStringOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpperCaseStringOutput:
    boto3_raw_data: "type_defs.UpperCaseStringOutputTypeDef" = dataclasses.field()

    withKeys = field("withKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpperCaseStringOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpperCaseStringOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAccountPolicyRequest:
    boto3_raw_data: "type_defs.PutAccountPolicyRequestTypeDef" = dataclasses.field()

    policyName = field("policyName")
    policyDocument = field("policyDocument")
    policyType = field("policyType")
    scope = field("scope")
    selectionCriteria = field("selectionCriteria")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAccountPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAccountPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutDataProtectionPolicyRequest:
    boto3_raw_data: "type_defs.PutDataProtectionPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    logGroupIdentifier = field("logGroupIdentifier")
    policyDocument = field("policyDocument")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutDataProtectionPolicyRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDataProtectionPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutDeliveryDestinationPolicyRequest:
    boto3_raw_data: "type_defs.PutDeliveryDestinationPolicyRequestTypeDef" = (
        dataclasses.field()
    )

    deliveryDestinationName = field("deliveryDestinationName")
    deliveryDestinationPolicy = field("deliveryDestinationPolicy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutDeliveryDestinationPolicyRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDeliveryDestinationPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutDeliverySourceRequest:
    boto3_raw_data: "type_defs.PutDeliverySourceRequestTypeDef" = dataclasses.field()

    name = field("name")
    resourceArn = field("resourceArn")
    logType = field("logType")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutDeliverySourceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDeliverySourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutDestinationPolicyRequest:
    boto3_raw_data: "type_defs.PutDestinationPolicyRequestTypeDef" = dataclasses.field()

    destinationName = field("destinationName")
    accessPolicy = field("accessPolicy")
    forceUpdate = field("forceUpdate")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutDestinationPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDestinationPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutDestinationRequest:
    boto3_raw_data: "type_defs.PutDestinationRequestTypeDef" = dataclasses.field()

    destinationName = field("destinationName")
    targetArn = field("targetArn")
    roleArn = field("roleArn")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutDestinationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutIndexPolicyRequest:
    boto3_raw_data: "type_defs.PutIndexPolicyRequestTypeDef" = dataclasses.field()

    logGroupIdentifier = field("logGroupIdentifier")
    policyDocument = field("policyDocument")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutIndexPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutIndexPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectedEntityInfo:
    boto3_raw_data: "type_defs.RejectedEntityInfoTypeDef" = dataclasses.field()

    errorType = field("errorType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RejectedEntityInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectedEntityInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RejectedLogEventsInfo:
    boto3_raw_data: "type_defs.RejectedLogEventsInfoTypeDef" = dataclasses.field()

    tooNewLogEventStartIndex = field("tooNewLogEventStartIndex")
    tooOldLogEventEndIndex = field("tooOldLogEventEndIndex")
    expiredLogEventEndIndex = field("expiredLogEventEndIndex")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RejectedLogEventsInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectedLogEventsInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutQueryDefinitionRequest:
    boto3_raw_data: "type_defs.PutQueryDefinitionRequestTypeDef" = dataclasses.field()

    name = field("name")
    queryString = field("queryString")
    queryLanguage = field("queryLanguage")
    queryDefinitionId = field("queryDefinitionId")
    logGroupNames = field("logGroupNames")
    clientToken = field("clientToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutQueryDefinitionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutQueryDefinitionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourcePolicyRequest:
    boto3_raw_data: "type_defs.PutResourcePolicyRequestTypeDef" = dataclasses.field()

    policyName = field("policyName")
    policyDocument = field("policyDocument")
    resourceArn = field("resourceArn")
    expectedRevisionId = field("expectedRevisionId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourcePolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourcePolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutRetentionPolicyRequest:
    boto3_raw_data: "type_defs.PutRetentionPolicyRequestTypeDef" = dataclasses.field()

    logGroupName = field("logGroupName")
    retentionInDays = field("retentionInDays")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutRetentionPolicyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutRetentionPolicyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutSubscriptionFilterRequest:
    boto3_raw_data: "type_defs.PutSubscriptionFilterRequestTypeDef" = (
        dataclasses.field()
    )

    logGroupName = field("logGroupName")
    filterName = field("filterName")
    filterPattern = field("filterPattern")
    destinationArn = field("destinationArn")
    roleArn = field("roleArn")
    distribution = field("distribution")
    applyOnTransformedLogs = field("applyOnTransformedLogs")
    fieldSelectionCriteria = field("fieldSelectionCriteria")
    emitSystemFields = field("emitSystemFields")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutSubscriptionFilterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutSubscriptionFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RenameKeyEntry:
    boto3_raw_data: "type_defs.RenameKeyEntryTypeDef" = dataclasses.field()

    key = field("key")
    renameTo = field("renameTo")
    overwriteIfExists = field("overwriteIfExists")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RenameKeyEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RenameKeyEntryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionStreamingException:
    boto3_raw_data: "type_defs.SessionStreamingExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SessionStreamingExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionStreamingExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SessionTimeoutException:
    boto3_raw_data: "type_defs.SessionTimeoutExceptionTypeDef" = dataclasses.field()

    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SessionTimeoutExceptionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SessionTimeoutExceptionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SplitStringEntry:
    boto3_raw_data: "type_defs.SplitStringEntryTypeDef" = dataclasses.field()

    source = field("source")
    delimiter = field("delimiter")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SplitStringEntryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SplitStringEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartLiveTailRequest:
    boto3_raw_data: "type_defs.StartLiveTailRequestTypeDef" = dataclasses.field()

    logGroupIdentifiers = field("logGroupIdentifiers")
    logStreamNames = field("logStreamNames")
    logStreamNamePrefixes = field("logStreamNamePrefixes")
    logEventFilterPattern = field("logEventFilterPattern")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartLiveTailRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartLiveTailRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartQueryRequest:
    boto3_raw_data: "type_defs.StartQueryRequestTypeDef" = dataclasses.field()

    startTime = field("startTime")
    endTime = field("endTime")
    queryString = field("queryString")
    queryLanguage = field("queryLanguage")
    logGroupName = field("logGroupName")
    logGroupNames = field("logGroupNames")
    logGroupIdentifiers = field("logGroupIdentifiers")
    limit = field("limit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StartQueryRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartQueryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopQueryRequest:
    boto3_raw_data: "type_defs.StopQueryRequestTypeDef" = dataclasses.field()

    queryId = field("queryId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopQueryRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopQueryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubstituteStringEntry:
    boto3_raw_data: "type_defs.SubstituteStringEntryTypeDef" = dataclasses.field()

    source = field("source")
    from_ = field("from")
    to = field("to")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubstituteStringEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubstituteStringEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuppressionPeriod:
    boto3_raw_data: "type_defs.SuppressionPeriodTypeDef" = dataclasses.field()

    value = field("value")
    suppressionUnit = field("suppressionUnit")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SuppressionPeriodTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SuppressionPeriodTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagLogGroupRequest:
    boto3_raw_data: "type_defs.TagLogGroupRequestTypeDef" = dataclasses.field()

    logGroupName = field("logGroupName")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TagLogGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagLogGroupRequestTypeDef"]
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
class TestMetricFilterRequest:
    boto3_raw_data: "type_defs.TestMetricFilterRequestTypeDef" = dataclasses.field()

    filterPattern = field("filterPattern")
    logEventMessages = field("logEventMessages")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestMetricFilterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestMetricFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TransformedLogRecord:
    boto3_raw_data: "type_defs.TransformedLogRecordTypeDef" = dataclasses.field()

    eventNumber = field("eventNumber")
    eventMessage = field("eventMessage")
    transformedEventMessage = field("transformedEventMessage")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TransformedLogRecordTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TransformedLogRecordTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TrimString:
    boto3_raw_data: "type_defs.TrimStringTypeDef" = dataclasses.field()

    withKeys = field("withKeys")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TrimStringTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TrimStringTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TypeConverterEntry:
    boto3_raw_data: "type_defs.TypeConverterEntryTypeDef" = dataclasses.field()

    key = field("key")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TypeConverterEntryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TypeConverterEntryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagLogGroupRequest:
    boto3_raw_data: "type_defs.UntagLogGroupRequestTypeDef" = dataclasses.field()

    logGroupName = field("logGroupName")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagLogGroupRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagLogGroupRequestTypeDef"]
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
class UpdateLogAnomalyDetectorRequest:
    boto3_raw_data: "type_defs.UpdateLogAnomalyDetectorRequestTypeDef" = (
        dataclasses.field()
    )

    anomalyDetectorArn = field("anomalyDetectorArn")
    enabled = field("enabled")
    evaluationFrequency = field("evaluationFrequency")
    filterPattern = field("filterPattern")
    anomalyVisibilityTime = field("anomalyVisibilityTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateLogAnomalyDetectorRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLogAnomalyDetectorRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpperCaseString:
    boto3_raw_data: "type_defs.UpperCaseStringTypeDef" = dataclasses.field()

    withKeys = field("withKeys")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpperCaseStringTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UpperCaseStringTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddKeysOutput:
    boto3_raw_data: "type_defs.AddKeysOutputTypeDef" = dataclasses.field()

    @cached_property
    def entries(self):  # pragma: no cover
        return AddKeyEntry.make_many(self.boto3_raw_data["entries"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddKeysOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddKeysOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AddKeys:
    boto3_raw_data: "type_defs.AddKeysTypeDef" = dataclasses.field()

    @cached_property
    def entries(self):  # pragma: no cover
        return AddKeyEntry.make_many(self.boto3_raw_data["entries"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AddKeysTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AddKeysTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Anomaly:
    boto3_raw_data: "type_defs.AnomalyTypeDef" = dataclasses.field()

    anomalyId = field("anomalyId")
    patternId = field("patternId")
    anomalyDetectorArn = field("anomalyDetectorArn")
    patternString = field("patternString")
    firstSeen = field("firstSeen")
    lastSeen = field("lastSeen")
    description = field("description")
    active = field("active")
    state = field("state")
    histogram = field("histogram")

    @cached_property
    def logSamples(self):  # pragma: no cover
        return LogEvent.make_many(self.boto3_raw_data["logSamples"])

    @cached_property
    def patternTokens(self):  # pragma: no cover
        return PatternToken.make_many(self.boto3_raw_data["patternTokens"])

    logGroupArnList = field("logGroupArnList")
    patternRegex = field("patternRegex")
    priority = field("priority")
    suppressed = field("suppressed")
    suppressedDate = field("suppressedDate")
    suppressedUntil = field("suppressedUntil")
    isPatternLevelSuppression = field("isPatternLevelSuppression")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnomalyTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnomalyTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationTemplateDeliveryConfigValues:
    boto3_raw_data: "type_defs.ConfigurationTemplateDeliveryConfigValuesTypeDef" = (
        dataclasses.field()
    )

    recordFields = field("recordFields")
    fieldDelimiter = field("fieldDelimiter")

    @cached_property
    def s3DeliveryConfiguration(self):  # pragma: no cover
        return S3DeliveryConfiguration.make_one(
            self.boto3_raw_data["s3DeliveryConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfigurationTemplateDeliveryConfigValuesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationTemplateDeliveryConfigValuesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeliveryRequest:
    boto3_raw_data: "type_defs.CreateDeliveryRequestTypeDef" = dataclasses.field()

    deliverySourceName = field("deliverySourceName")
    deliveryDestinationArn = field("deliveryDestinationArn")
    recordFields = field("recordFields")
    fieldDelimiter = field("fieldDelimiter")

    @cached_property
    def s3DeliveryConfiguration(self):  # pragma: no cover
        return S3DeliveryConfiguration.make_one(
            self.boto3_raw_data["s3DeliveryConfiguration"]
        )

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeliveryRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeliveryRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Delivery:
    boto3_raw_data: "type_defs.DeliveryTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    deliverySourceName = field("deliverySourceName")
    deliveryDestinationArn = field("deliveryDestinationArn")
    deliveryDestinationType = field("deliveryDestinationType")
    recordFields = field("recordFields")
    fieldDelimiter = field("fieldDelimiter")

    @cached_property
    def s3DeliveryConfiguration(self):  # pragma: no cover
        return S3DeliveryConfiguration.make_one(
            self.boto3_raw_data["s3DeliveryConfiguration"]
        )

    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeliveryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DeliveryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDeliveryConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateDeliveryConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    recordFields = field("recordFields")
    fieldDelimiter = field("fieldDelimiter")

    @cached_property
    def s3DeliveryConfiguration(self):  # pragma: no cover
        return S3DeliveryConfiguration.make_one(
            self.boto3_raw_data["s3DeliveryConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDeliveryConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDeliveryConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyValueOutput:
    boto3_raw_data: "type_defs.CopyValueOutputTypeDef" = dataclasses.field()

    @cached_property
    def entries(self):  # pragma: no cover
        return CopyValueEntry.make_many(self.boto3_raw_data["entries"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CopyValueOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CopyValueOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CopyValue:
    boto3_raw_data: "type_defs.CopyValueTypeDef" = dataclasses.field()

    @cached_property
    def entries(self):  # pragma: no cover
        return CopyValueEntry.make_many(self.boto3_raw_data["entries"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CopyValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CopyValueTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateExportTaskResponse:
    boto3_raw_data: "type_defs.CreateExportTaskResponseTypeDef" = dataclasses.field()

    taskId = field("taskId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateExportTaskResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateExportTaskResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLogAnomalyDetectorResponse:
    boto3_raw_data: "type_defs.CreateLogAnomalyDetectorResponseTypeDef" = (
        dataclasses.field()
    )

    anomalyDetectorArn = field("anomalyDetectorArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateLogAnomalyDetectorResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLogAnomalyDetectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteQueryDefinitionResponse:
    boto3_raw_data: "type_defs.DeleteQueryDefinitionResponseTypeDef" = (
        dataclasses.field()
    )

    success = field("success")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteQueryDefinitionResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteQueryDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAccountPoliciesResponse:
    boto3_raw_data: "type_defs.DescribeAccountPoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def accountPolicies(self):  # pragma: no cover
        return AccountPolicy.make_many(self.boto3_raw_data["accountPolicies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAccountPoliciesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAccountPoliciesResponseTypeDef"]
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
class GetDataProtectionPolicyResponse:
    boto3_raw_data: "type_defs.GetDataProtectionPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    logGroupIdentifier = field("logGroupIdentifier")
    policyDocument = field("policyDocument")
    lastUpdatedTime = field("lastUpdatedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDataProtectionPolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDataProtectionPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLogAnomalyDetectorResponse:
    boto3_raw_data: "type_defs.GetLogAnomalyDetectorResponseTypeDef" = (
        dataclasses.field()
    )

    detectorName = field("detectorName")
    logGroupArnList = field("logGroupArnList")
    evaluationFrequency = field("evaluationFrequency")
    filterPattern = field("filterPattern")
    anomalyDetectorStatus = field("anomalyDetectorStatus")
    kmsKeyId = field("kmsKeyId")
    creationTimeStamp = field("creationTimeStamp")
    lastModifiedTimeStamp = field("lastModifiedTimeStamp")
    anomalyVisibilityTime = field("anomalyVisibilityTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetLogAnomalyDetectorResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLogAnomalyDetectorResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLogRecordResponse:
    boto3_raw_data: "type_defs.GetLogRecordResponseTypeDef" = dataclasses.field()

    logRecord = field("logRecord")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLogRecordResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLogRecordResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLogAnomalyDetectorsResponse:
    boto3_raw_data: "type_defs.ListLogAnomalyDetectorsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def anomalyDetectors(self):  # pragma: no cover
        return AnomalyDetector.make_many(self.boto3_raw_data["anomalyDetectors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListLogAnomalyDetectorsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLogAnomalyDetectorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLogGroupsForQueryResponse:
    boto3_raw_data: "type_defs.ListLogGroupsForQueryResponseTypeDef" = (
        dataclasses.field()
    )

    logGroupIdentifiers = field("logGroupIdentifiers")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListLogGroupsForQueryResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLogGroupsForQueryResponseTypeDef"]
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
class ListTagsLogGroupResponse:
    boto3_raw_data: "type_defs.ListTagsLogGroupResponseTypeDef" = dataclasses.field()

    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsLogGroupResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsLogGroupResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutAccountPolicyResponse:
    boto3_raw_data: "type_defs.PutAccountPolicyResponseTypeDef" = dataclasses.field()

    @cached_property
    def accountPolicy(self):  # pragma: no cover
        return AccountPolicy.make_one(self.boto3_raw_data["accountPolicy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutAccountPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutAccountPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutDataProtectionPolicyResponse:
    boto3_raw_data: "type_defs.PutDataProtectionPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    logGroupIdentifier = field("logGroupIdentifier")
    policyDocument = field("policyDocument")
    lastUpdatedTime = field("lastUpdatedTime")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutDataProtectionPolicyResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDataProtectionPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutIntegrationResponse:
    boto3_raw_data: "type_defs.PutIntegrationResponseTypeDef" = dataclasses.field()

    integrationName = field("integrationName")
    integrationStatus = field("integrationStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutIntegrationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutIntegrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutQueryDefinitionResponse:
    boto3_raw_data: "type_defs.PutQueryDefinitionResponseTypeDef" = dataclasses.field()

    queryDefinitionId = field("queryDefinitionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutQueryDefinitionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutQueryDefinitionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartQueryResponse:
    boto3_raw_data: "type_defs.StartQueryResponseTypeDef" = dataclasses.field()

    queryId = field("queryId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartQueryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartQueryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StopQueryResponse:
    boto3_raw_data: "type_defs.StopQueryResponseTypeDef" = dataclasses.field()

    success = field("success")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StopQueryResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StopQueryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeliveryDestination:
    boto3_raw_data: "type_defs.DeliveryDestinationTypeDef" = dataclasses.field()

    name = field("name")
    arn = field("arn")
    deliveryDestinationType = field("deliveryDestinationType")
    outputFormat = field("outputFormat")

    @cached_property
    def deliveryDestinationConfiguration(self):  # pragma: no cover
        return DeliveryDestinationConfiguration.make_one(
            self.boto3_raw_data["deliveryDestinationConfiguration"]
        )

    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeliveryDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeliveryDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutDeliveryDestinationRequest:
    boto3_raw_data: "type_defs.PutDeliveryDestinationRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    outputFormat = field("outputFormat")

    @cached_property
    def deliveryDestinationConfiguration(self):  # pragma: no cover
        return DeliveryDestinationConfiguration.make_one(
            self.boto3_raw_data["deliveryDestinationConfiguration"]
        )

    deliveryDestinationType = field("deliveryDestinationType")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutDeliveryDestinationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDeliveryDestinationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDeliverySourcesResponse:
    boto3_raw_data: "type_defs.DescribeDeliverySourcesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def deliverySources(self):  # pragma: no cover
        return DeliverySource.make_many(self.boto3_raw_data["deliverySources"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeDeliverySourcesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDeliverySourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeliverySourceResponse:
    boto3_raw_data: "type_defs.GetDeliverySourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def deliverySource(self):  # pragma: no cover
        return DeliverySource.make_one(self.boto3_raw_data["deliverySource"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeliverySourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeliverySourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutDeliverySourceResponse:
    boto3_raw_data: "type_defs.PutDeliverySourceResponseTypeDef" = dataclasses.field()

    @cached_property
    def deliverySource(self):  # pragma: no cover
        return DeliverySource.make_one(self.boto3_raw_data["deliverySource"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutDeliverySourceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDeliverySourceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigurationTemplatesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeConfigurationTemplatesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    service = field("service")
    logTypes = field("logTypes")
    resourceTypes = field("resourceTypes")
    deliveryDestinationTypes = field("deliveryDestinationTypes")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConfigurationTemplatesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigurationTemplatesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDeliveriesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeDeliveriesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDeliveriesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDeliveriesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDeliveryDestinationsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeDeliveryDestinationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDeliveryDestinationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDeliveryDestinationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDeliverySourcesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeDeliverySourcesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDeliverySourcesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDeliverySourcesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDestinationsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeDestinationsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    DestinationNamePrefix = field("DestinationNamePrefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDestinationsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDestinationsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeExportTasksRequestPaginate:
    boto3_raw_data: "type_defs.DescribeExportTasksRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    taskId = field("taskId")
    statusCode = field("statusCode")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeExportTasksRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExportTasksRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLogGroupsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeLogGroupsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    accountIdentifiers = field("accountIdentifiers")
    logGroupNamePrefix = field("logGroupNamePrefix")
    logGroupNamePattern = field("logGroupNamePattern")
    includeLinkedAccounts = field("includeLinkedAccounts")
    logGroupClass = field("logGroupClass")
    logGroupIdentifiers = field("logGroupIdentifiers")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeLogGroupsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLogGroupsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLogStreamsRequestPaginate:
    boto3_raw_data: "type_defs.DescribeLogStreamsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    logGroupName = field("logGroupName")
    logGroupIdentifier = field("logGroupIdentifier")
    logStreamNamePrefix = field("logStreamNamePrefix")
    orderBy = field("orderBy")
    descending = field("descending")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeLogStreamsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLogStreamsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMetricFiltersRequestPaginate:
    boto3_raw_data: "type_defs.DescribeMetricFiltersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    logGroupName = field("logGroupName")
    filterNamePrefix = field("filterNamePrefix")
    metricName = field("metricName")
    metricNamespace = field("metricNamespace")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeMetricFiltersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMetricFiltersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeQueriesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeQueriesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    logGroupName = field("logGroupName")
    status = field("status")
    queryLanguage = field("queryLanguage")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeQueriesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeQueriesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourcePoliciesRequestPaginate:
    boto3_raw_data: "type_defs.DescribeResourcePoliciesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    resourceArn = field("resourceArn")
    policyScope = field("policyScope")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeResourcePoliciesRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourcePoliciesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSubscriptionFiltersRequestPaginate:
    boto3_raw_data: "type_defs.DescribeSubscriptionFiltersRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    logGroupName = field("logGroupName")
    filterNamePrefix = field("filterNamePrefix")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSubscriptionFiltersRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSubscriptionFiltersRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterLogEventsRequestPaginate:
    boto3_raw_data: "type_defs.FilterLogEventsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    logGroupName = field("logGroupName")
    logGroupIdentifier = field("logGroupIdentifier")
    logStreamNames = field("logStreamNames")
    logStreamNamePrefix = field("logStreamNamePrefix")
    startTime = field("startTime")
    endTime = field("endTime")
    filterPattern = field("filterPattern")
    interleaved = field("interleaved")
    unmask = field("unmask")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.FilterLogEventsRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FilterLogEventsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnomaliesRequestPaginate:
    boto3_raw_data: "type_defs.ListAnomaliesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    anomalyDetectorArn = field("anomalyDetectorArn")
    suppressionState = field("suppressionState")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAnomaliesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnomaliesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLogAnomalyDetectorsRequestPaginate:
    boto3_raw_data: "type_defs.ListLogAnomalyDetectorsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    filterLogGroupArn = field("filterLogGroupArn")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLogAnomalyDetectorsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLogAnomalyDetectorsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLogGroupsForQueryRequestPaginate:
    boto3_raw_data: "type_defs.ListLogGroupsForQueryRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    queryId = field("queryId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListLogGroupsForQueryRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLogGroupsForQueryRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDestinationsResponse:
    boto3_raw_data: "type_defs.DescribeDestinationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def destinations(self):  # pragma: no cover
        return Destination.make_many(self.boto3_raw_data["destinations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDestinationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDestinationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutDestinationResponse:
    boto3_raw_data: "type_defs.PutDestinationResponseTypeDef" = dataclasses.field()

    @cached_property
    def destination(self):  # pragma: no cover
        return Destination.make_one(self.boto3_raw_data["destination"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutDestinationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDestinationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeFieldIndexesResponse:
    boto3_raw_data: "type_defs.DescribeFieldIndexesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def fieldIndexes(self):  # pragma: no cover
        return FieldIndex.make_many(self.boto3_raw_data["fieldIndexes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeFieldIndexesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeFieldIndexesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIndexPoliciesResponse:
    boto3_raw_data: "type_defs.DescribeIndexPoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def indexPolicies(self):  # pragma: no cover
        return IndexPolicy.make_many(self.boto3_raw_data["indexPolicies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeIndexPoliciesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIndexPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutIndexPolicyResponse:
    boto3_raw_data: "type_defs.PutIndexPolicyResponseTypeDef" = dataclasses.field()

    @cached_property
    def indexPolicy(self):  # pragma: no cover
        return IndexPolicy.make_one(self.boto3_raw_data["indexPolicy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutIndexPolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutIndexPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLogGroupsResponse:
    boto3_raw_data: "type_defs.DescribeLogGroupsResponseTypeDef" = dataclasses.field()

    @cached_property
    def logGroups(self):  # pragma: no cover
        return LogGroup.make_many(self.boto3_raw_data["logGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLogGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLogGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeLogStreamsResponse:
    boto3_raw_data: "type_defs.DescribeLogStreamsResponseTypeDef" = dataclasses.field()

    @cached_property
    def logStreams(self):  # pragma: no cover
        return LogStream.make_many(self.boto3_raw_data["logStreams"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeLogStreamsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeLogStreamsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeQueriesResponse:
    boto3_raw_data: "type_defs.DescribeQueriesResponseTypeDef" = dataclasses.field()

    @cached_property
    def queries(self):  # pragma: no cover
        return QueryInfo.make_many(self.boto3_raw_data["queries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeQueriesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeQueriesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeQueryDefinitionsResponse:
    boto3_raw_data: "type_defs.DescribeQueryDefinitionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def queryDefinitions(self):  # pragma: no cover
        return QueryDefinition.make_many(self.boto3_raw_data["queryDefinitions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeQueryDefinitionsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeQueryDefinitionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeResourcePoliciesResponse:
    boto3_raw_data: "type_defs.DescribeResourcePoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def resourcePolicies(self):  # pragma: no cover
        return ResourcePolicy.make_many(self.boto3_raw_data["resourcePolicies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeResourcePoliciesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeResourcePoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutResourcePolicyResponse:
    boto3_raw_data: "type_defs.PutResourcePolicyResponseTypeDef" = dataclasses.field()

    @cached_property
    def resourcePolicy(self):  # pragma: no cover
        return ResourcePolicy.make_one(self.boto3_raw_data["resourcePolicy"])

    revisionId = field("revisionId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutResourcePolicyResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutResourcePolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSubscriptionFiltersResponse:
    boto3_raw_data: "type_defs.DescribeSubscriptionFiltersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def subscriptionFilters(self):  # pragma: no cover
        return SubscriptionFilter.make_many(self.boto3_raw_data["subscriptionFilters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeSubscriptionFiltersResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSubscriptionFiltersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExportTask:
    boto3_raw_data: "type_defs.ExportTaskTypeDef" = dataclasses.field()

    taskId = field("taskId")
    taskName = field("taskName")
    logGroupName = field("logGroupName")
    from_ = field("from")
    to = field("to")
    destination = field("destination")
    destinationPrefix = field("destinationPrefix")

    @cached_property
    def status(self):  # pragma: no cover
        return ExportTaskStatus.make_one(self.boto3_raw_data["status"])

    @cached_property
    def executionInfo(self):  # pragma: no cover
        return ExportTaskExecutionInfo.make_one(self.boto3_raw_data["executionInfo"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExportTaskTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExportTaskTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterLogEventsResponse:
    boto3_raw_data: "type_defs.FilterLogEventsResponseTypeDef" = dataclasses.field()

    @cached_property
    def events(self):  # pragma: no cover
        return FilteredLogEvent.make_many(self.boto3_raw_data["events"])

    @cached_property
    def searchedLogStreams(self):  # pragma: no cover
        return SearchedLogStream.make_many(self.boto3_raw_data["searchedLogStreams"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FilterLogEventsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FilterLogEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeliveryDestinationPolicyResponse:
    boto3_raw_data: "type_defs.GetDeliveryDestinationPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def policy(self):  # pragma: no cover
        return Policy.make_one(self.boto3_raw_data["policy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetDeliveryDestinationPolicyResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeliveryDestinationPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutDeliveryDestinationPolicyResponse:
    boto3_raw_data: "type_defs.PutDeliveryDestinationPolicyResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def policy(self):  # pragma: no cover
        return Policy.make_one(self.boto3_raw_data["policy"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PutDeliveryDestinationPolicyResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDeliveryDestinationPolicyResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLogEventsResponse:
    boto3_raw_data: "type_defs.GetLogEventsResponseTypeDef" = dataclasses.field()

    @cached_property
    def events(self):  # pragma: no cover
        return OutputLogEvent.make_many(self.boto3_raw_data["events"])

    nextForwardToken = field("nextForwardToken")
    nextBackwardToken = field("nextBackwardToken")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLogEventsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLogEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLogGroupFieldsResponse:
    boto3_raw_data: "type_defs.GetLogGroupFieldsResponseTypeDef" = dataclasses.field()

    @cached_property
    def logGroupFields(self):  # pragma: no cover
        return LogGroupField.make_many(self.boto3_raw_data["logGroupFields"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLogGroupFieldsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLogGroupFieldsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLogObjectResponseStream:
    boto3_raw_data: "type_defs.GetLogObjectResponseStreamTypeDef" = dataclasses.field()

    @cached_property
    def fields(self):  # pragma: no cover
        return FieldsData.make_one(self.boto3_raw_data["fields"])

    @cached_property
    def InternalStreamingException(self):  # pragma: no cover
        return InternalStreamingException.make_one(
            self.boto3_raw_data["InternalStreamingException"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLogObjectResponseStreamTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLogObjectResponseStreamTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetQueryResultsResponse:
    boto3_raw_data: "type_defs.GetQueryResultsResponseTypeDef" = dataclasses.field()

    queryLanguage = field("queryLanguage")

    @cached_property
    def results(self):  # pragma: no cover
        return ResultField.make_many(self.boto3_raw_data["results"])

    @cached_property
    def statistics(self):  # pragma: no cover
        return QueryStatistics.make_one(self.boto3_raw_data["statistics"])

    status = field("status")
    encryptionKey = field("encryptionKey")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetQueryResultsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetQueryResultsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutLogEventsRequest:
    boto3_raw_data: "type_defs.PutLogEventsRequestTypeDef" = dataclasses.field()

    logGroupName = field("logGroupName")
    logStreamName = field("logStreamName")

    @cached_property
    def logEvents(self):  # pragma: no cover
        return InputLogEvent.make_many(self.boto3_raw_data["logEvents"])

    sequenceToken = field("sequenceToken")

    @cached_property
    def entity(self):  # pragma: no cover
        return Entity.make_one(self.boto3_raw_data["entity"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutLogEventsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutLogEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIntegrationsResponse:
    boto3_raw_data: "type_defs.ListIntegrationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def integrationSummaries(self):  # pragma: no cover
        return IntegrationSummary.make_many(self.boto3_raw_data["integrationSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIntegrationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIntegrationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLogGroupsResponse:
    boto3_raw_data: "type_defs.ListLogGroupsResponseTypeDef" = dataclasses.field()

    @cached_property
    def logGroups(self):  # pragma: no cover
        return LogGroupSummary.make_many(self.boto3_raw_data["logGroups"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLogGroupsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLogGroupsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LiveTailSessionUpdate:
    boto3_raw_data: "type_defs.LiveTailSessionUpdateTypeDef" = dataclasses.field()

    @cached_property
    def sessionMetadata(self):  # pragma: no cover
        return LiveTailSessionMetadata.make_one(self.boto3_raw_data["sessionMetadata"])

    @cached_property
    def sessionResults(self):  # pragma: no cover
        return LiveTailSessionLogEvent.make_many(self.boto3_raw_data["sessionResults"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LiveTailSessionUpdateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LiveTailSessionUpdateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestMetricFilterResponse:
    boto3_raw_data: "type_defs.TestMetricFilterResponseTypeDef" = dataclasses.field()

    @cached_property
    def matches(self):  # pragma: no cover
        return MetricFilterMatchRecord.make_many(self.boto3_raw_data["matches"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestMetricFilterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestMetricFilterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MetricFilter:
    boto3_raw_data: "type_defs.MetricFilterTypeDef" = dataclasses.field()

    filterName = field("filterName")
    filterPattern = field("filterPattern")

    @cached_property
    def metricTransformations(self):  # pragma: no cover
        return MetricTransformationOutput.make_many(
            self.boto3_raw_data["metricTransformations"]
        )

    creationTime = field("creationTime")
    logGroupName = field("logGroupName")
    applyOnTransformedLogs = field("applyOnTransformedLogs")
    fieldSelectionCriteria = field("fieldSelectionCriteria")
    emitSystemFieldDimensions = field("emitSystemFieldDimensions")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MetricFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MetricFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MoveKeysOutput:
    boto3_raw_data: "type_defs.MoveKeysOutputTypeDef" = dataclasses.field()

    @cached_property
    def entries(self):  # pragma: no cover
        return MoveKeyEntry.make_many(self.boto3_raw_data["entries"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MoveKeysOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MoveKeysOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MoveKeys:
    boto3_raw_data: "type_defs.MoveKeysTypeDef" = dataclasses.field()

    @cached_property
    def entries(self):  # pragma: no cover
        return MoveKeyEntry.make_many(self.boto3_raw_data["entries"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MoveKeysTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MoveKeysTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenSearchApplication:
    boto3_raw_data: "type_defs.OpenSearchApplicationTypeDef" = dataclasses.field()

    applicationEndpoint = field("applicationEndpoint")
    applicationArn = field("applicationArn")
    applicationId = field("applicationId")

    @cached_property
    def status(self):  # pragma: no cover
        return OpenSearchResourceStatus.make_one(self.boto3_raw_data["status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpenSearchApplicationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenSearchApplicationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenSearchCollection:
    boto3_raw_data: "type_defs.OpenSearchCollectionTypeDef" = dataclasses.field()

    collectionEndpoint = field("collectionEndpoint")
    collectionArn = field("collectionArn")

    @cached_property
    def status(self):  # pragma: no cover
        return OpenSearchResourceStatus.make_one(self.boto3_raw_data["status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpenSearchCollectionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenSearchCollectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenSearchDataAccessPolicy:
    boto3_raw_data: "type_defs.OpenSearchDataAccessPolicyTypeDef" = dataclasses.field()

    policyName = field("policyName")

    @cached_property
    def status(self):  # pragma: no cover
        return OpenSearchResourceStatus.make_one(self.boto3_raw_data["status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpenSearchDataAccessPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenSearchDataAccessPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenSearchDataSource:
    boto3_raw_data: "type_defs.OpenSearchDataSourceTypeDef" = dataclasses.field()

    dataSourceName = field("dataSourceName")

    @cached_property
    def status(self):  # pragma: no cover
        return OpenSearchResourceStatus.make_one(self.boto3_raw_data["status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpenSearchDataSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenSearchDataSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenSearchEncryptionPolicy:
    boto3_raw_data: "type_defs.OpenSearchEncryptionPolicyTypeDef" = dataclasses.field()

    policyName = field("policyName")

    @cached_property
    def status(self):  # pragma: no cover
        return OpenSearchResourceStatus.make_one(self.boto3_raw_data["status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpenSearchEncryptionPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenSearchEncryptionPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenSearchLifecyclePolicy:
    boto3_raw_data: "type_defs.OpenSearchLifecyclePolicyTypeDef" = dataclasses.field()

    policyName = field("policyName")

    @cached_property
    def status(self):  # pragma: no cover
        return OpenSearchResourceStatus.make_one(self.boto3_raw_data["status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpenSearchLifecyclePolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenSearchLifecyclePolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenSearchNetworkPolicy:
    boto3_raw_data: "type_defs.OpenSearchNetworkPolicyTypeDef" = dataclasses.field()

    policyName = field("policyName")

    @cached_property
    def status(self):  # pragma: no cover
        return OpenSearchResourceStatus.make_one(self.boto3_raw_data["status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpenSearchNetworkPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenSearchNetworkPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenSearchWorkspace:
    boto3_raw_data: "type_defs.OpenSearchWorkspaceTypeDef" = dataclasses.field()

    workspaceId = field("workspaceId")

    @cached_property
    def status(self):  # pragma: no cover
        return OpenSearchResourceStatus.make_one(self.boto3_raw_data["status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpenSearchWorkspaceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenSearchWorkspaceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ResourceConfig:
    boto3_raw_data: "type_defs.ResourceConfigTypeDef" = dataclasses.field()

    @cached_property
    def openSearchResourceConfig(self):  # pragma: no cover
        return OpenSearchResourceConfig.make_one(
            self.boto3_raw_data["openSearchResourceConfig"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ResourceConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ResourceConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutLogEventsResponse:
    boto3_raw_data: "type_defs.PutLogEventsResponseTypeDef" = dataclasses.field()

    nextSequenceToken = field("nextSequenceToken")

    @cached_property
    def rejectedLogEventsInfo(self):  # pragma: no cover
        return RejectedLogEventsInfo.make_one(
            self.boto3_raw_data["rejectedLogEventsInfo"]
        )

    @cached_property
    def rejectedEntityInfo(self):  # pragma: no cover
        return RejectedEntityInfo.make_one(self.boto3_raw_data["rejectedEntityInfo"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutLogEventsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutLogEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RenameKeysOutput:
    boto3_raw_data: "type_defs.RenameKeysOutputTypeDef" = dataclasses.field()

    @cached_property
    def entries(self):  # pragma: no cover
        return RenameKeyEntry.make_many(self.boto3_raw_data["entries"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RenameKeysOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RenameKeysOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RenameKeys:
    boto3_raw_data: "type_defs.RenameKeysTypeDef" = dataclasses.field()

    @cached_property
    def entries(self):  # pragma: no cover
        return RenameKeyEntry.make_many(self.boto3_raw_data["entries"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RenameKeysTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RenameKeysTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SplitStringOutput:
    boto3_raw_data: "type_defs.SplitStringOutputTypeDef" = dataclasses.field()

    @cached_property
    def entries(self):  # pragma: no cover
        return SplitStringEntry.make_many(self.boto3_raw_data["entries"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SplitStringOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SplitStringOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SplitString:
    boto3_raw_data: "type_defs.SplitStringTypeDef" = dataclasses.field()

    @cached_property
    def entries(self):  # pragma: no cover
        return SplitStringEntry.make_many(self.boto3_raw_data["entries"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SplitStringTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SplitStringTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubstituteStringOutput:
    boto3_raw_data: "type_defs.SubstituteStringOutputTypeDef" = dataclasses.field()

    @cached_property
    def entries(self):  # pragma: no cover
        return SubstituteStringEntry.make_many(self.boto3_raw_data["entries"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SubstituteStringOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubstituteStringOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SubstituteString:
    boto3_raw_data: "type_defs.SubstituteStringTypeDef" = dataclasses.field()

    @cached_property
    def entries(self):  # pragma: no cover
        return SubstituteStringEntry.make_many(self.boto3_raw_data["entries"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SubstituteStringTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SubstituteStringTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAnomalyRequest:
    boto3_raw_data: "type_defs.UpdateAnomalyRequestTypeDef" = dataclasses.field()

    anomalyDetectorArn = field("anomalyDetectorArn")
    anomalyId = field("anomalyId")
    patternId = field("patternId")
    suppressionType = field("suppressionType")

    @cached_property
    def suppressionPeriod(self):  # pragma: no cover
        return SuppressionPeriod.make_one(self.boto3_raw_data["suppressionPeriod"])

    baseline = field("baseline")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAnomalyRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAnomalyRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestTransformerResponse:
    boto3_raw_data: "type_defs.TestTransformerResponseTypeDef" = dataclasses.field()

    @cached_property
    def transformedLogs(self):  # pragma: no cover
        return TransformedLogRecord.make_many(self.boto3_raw_data["transformedLogs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestTransformerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestTransformerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TypeConverterOutput:
    boto3_raw_data: "type_defs.TypeConverterOutputTypeDef" = dataclasses.field()

    @cached_property
    def entries(self):  # pragma: no cover
        return TypeConverterEntry.make_many(self.boto3_raw_data["entries"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TypeConverterOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TypeConverterOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TypeConverter:
    boto3_raw_data: "type_defs.TypeConverterTypeDef" = dataclasses.field()

    @cached_property
    def entries(self):  # pragma: no cover
        return TypeConverterEntry.make_many(self.boto3_raw_data["entries"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TypeConverterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TypeConverterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnomaliesResponse:
    boto3_raw_data: "type_defs.ListAnomaliesResponseTypeDef" = dataclasses.field()

    @cached_property
    def anomalies(self):  # pragma: no cover
        return Anomaly.make_many(self.boto3_raw_data["anomalies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAnomaliesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnomaliesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationTemplate:
    boto3_raw_data: "type_defs.ConfigurationTemplateTypeDef" = dataclasses.field()

    service = field("service")
    logType = field("logType")
    resourceType = field("resourceType")
    deliveryDestinationType = field("deliveryDestinationType")

    @cached_property
    def defaultDeliveryConfigValues(self):  # pragma: no cover
        return ConfigurationTemplateDeliveryConfigValues.make_one(
            self.boto3_raw_data["defaultDeliveryConfigValues"]
        )

    @cached_property
    def allowedFields(self):  # pragma: no cover
        return RecordField.make_many(self.boto3_raw_data["allowedFields"])

    allowedOutputFormats = field("allowedOutputFormats")
    allowedActionForAllowVendedLogsDeliveryForResource = field(
        "allowedActionForAllowVendedLogsDeliveryForResource"
    )
    allowedFieldDelimiters = field("allowedFieldDelimiters")
    allowedSuffixPathFields = field("allowedSuffixPathFields")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationTemplateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationTemplateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDeliveryResponse:
    boto3_raw_data: "type_defs.CreateDeliveryResponseTypeDef" = dataclasses.field()

    @cached_property
    def delivery(self):  # pragma: no cover
        return Delivery.make_one(self.boto3_raw_data["delivery"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDeliveryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDeliveryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDeliveriesResponse:
    boto3_raw_data: "type_defs.DescribeDeliveriesResponseTypeDef" = dataclasses.field()

    @cached_property
    def deliveries(self):  # pragma: no cover
        return Delivery.make_many(self.boto3_raw_data["deliveries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDeliveriesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDeliveriesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeliveryResponse:
    boto3_raw_data: "type_defs.GetDeliveryResponseTypeDef" = dataclasses.field()

    @cached_property
    def delivery(self):  # pragma: no cover
        return Delivery.make_one(self.boto3_raw_data["delivery"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDeliveryResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeliveryResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDeliveryDestinationsResponse:
    boto3_raw_data: "type_defs.DescribeDeliveryDestinationsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def deliveryDestinations(self):  # pragma: no cover
        return DeliveryDestination.make_many(
            self.boto3_raw_data["deliveryDestinations"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDeliveryDestinationsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDeliveryDestinationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDeliveryDestinationResponse:
    boto3_raw_data: "type_defs.GetDeliveryDestinationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def deliveryDestination(self):  # pragma: no cover
        return DeliveryDestination.make_one(self.boto3_raw_data["deliveryDestination"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetDeliveryDestinationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDeliveryDestinationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutDeliveryDestinationResponse:
    boto3_raw_data: "type_defs.PutDeliveryDestinationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def deliveryDestination(self):  # pragma: no cover
        return DeliveryDestination.make_one(self.boto3_raw_data["deliveryDestination"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutDeliveryDestinationResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutDeliveryDestinationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeExportTasksResponse:
    boto3_raw_data: "type_defs.DescribeExportTasksResponseTypeDef" = dataclasses.field()

    @cached_property
    def exportTasks(self):  # pragma: no cover
        return ExportTask.make_many(self.boto3_raw_data["exportTasks"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeExportTasksResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExportTasksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLogObjectResponse:
    boto3_raw_data: "type_defs.GetLogObjectResponseTypeDef" = dataclasses.field()

    fieldStream = field("fieldStream")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetLogObjectResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLogObjectResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartLiveTailResponseStream:
    boto3_raw_data: "type_defs.StartLiveTailResponseStreamTypeDef" = dataclasses.field()

    @cached_property
    def sessionStart(self):  # pragma: no cover
        return LiveTailSessionStart.make_one(self.boto3_raw_data["sessionStart"])

    @cached_property
    def sessionUpdate(self):  # pragma: no cover
        return LiveTailSessionUpdate.make_one(self.boto3_raw_data["sessionUpdate"])

    @cached_property
    def SessionTimeoutException(self):  # pragma: no cover
        return SessionTimeoutException.make_one(
            self.boto3_raw_data["SessionTimeoutException"]
        )

    @cached_property
    def SessionStreamingException(self):  # pragma: no cover
        return SessionStreamingException.make_one(
            self.boto3_raw_data["SessionStreamingException"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartLiveTailResponseStreamTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartLiveTailResponseStreamTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeMetricFiltersResponse:
    boto3_raw_data: "type_defs.DescribeMetricFiltersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def metricFilters(self):  # pragma: no cover
        return MetricFilter.make_many(self.boto3_raw_data["metricFilters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeMetricFiltersResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeMetricFiltersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutMetricFilterRequest:
    boto3_raw_data: "type_defs.PutMetricFilterRequestTypeDef" = dataclasses.field()

    logGroupName = field("logGroupName")
    filterName = field("filterName")
    filterPattern = field("filterPattern")
    metricTransformations = field("metricTransformations")
    applyOnTransformedLogs = field("applyOnTransformedLogs")
    fieldSelectionCriteria = field("fieldSelectionCriteria")
    emitSystemFieldDimensions = field("emitSystemFieldDimensions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutMetricFilterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutMetricFilterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OpenSearchIntegrationDetails:
    boto3_raw_data: "type_defs.OpenSearchIntegrationDetailsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def dataSource(self):  # pragma: no cover
        return OpenSearchDataSource.make_one(self.boto3_raw_data["dataSource"])

    @cached_property
    def application(self):  # pragma: no cover
        return OpenSearchApplication.make_one(self.boto3_raw_data["application"])

    @cached_property
    def collection(self):  # pragma: no cover
        return OpenSearchCollection.make_one(self.boto3_raw_data["collection"])

    @cached_property
    def workspace(self):  # pragma: no cover
        return OpenSearchWorkspace.make_one(self.boto3_raw_data["workspace"])

    @cached_property
    def encryptionPolicy(self):  # pragma: no cover
        return OpenSearchEncryptionPolicy.make_one(
            self.boto3_raw_data["encryptionPolicy"]
        )

    @cached_property
    def networkPolicy(self):  # pragma: no cover
        return OpenSearchNetworkPolicy.make_one(self.boto3_raw_data["networkPolicy"])

    @cached_property
    def accessPolicy(self):  # pragma: no cover
        return OpenSearchDataAccessPolicy.make_one(self.boto3_raw_data["accessPolicy"])

    @cached_property
    def lifecyclePolicy(self):  # pragma: no cover
        return OpenSearchLifecyclePolicy.make_one(
            self.boto3_raw_data["lifecyclePolicy"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.OpenSearchIntegrationDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OpenSearchIntegrationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutIntegrationRequest:
    boto3_raw_data: "type_defs.PutIntegrationRequestTypeDef" = dataclasses.field()

    integrationName = field("integrationName")

    @cached_property
    def resourceConfig(self):  # pragma: no cover
        return ResourceConfig.make_one(self.boto3_raw_data["resourceConfig"])

    integrationType = field("integrationType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutIntegrationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutIntegrationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProcessorOutput:
    boto3_raw_data: "type_defs.ProcessorOutputTypeDef" = dataclasses.field()

    @cached_property
    def addKeys(self):  # pragma: no cover
        return AddKeysOutput.make_one(self.boto3_raw_data["addKeys"])

    @cached_property
    def copyValue(self):  # pragma: no cover
        return CopyValueOutput.make_one(self.boto3_raw_data["copyValue"])

    @cached_property
    def csv(self):  # pragma: no cover
        return CSVOutput.make_one(self.boto3_raw_data["csv"])

    @cached_property
    def dateTimeConverter(self):  # pragma: no cover
        return DateTimeConverterOutput.make_one(
            self.boto3_raw_data["dateTimeConverter"]
        )

    @cached_property
    def deleteKeys(self):  # pragma: no cover
        return DeleteKeysOutput.make_one(self.boto3_raw_data["deleteKeys"])

    @cached_property
    def grok(self):  # pragma: no cover
        return Grok.make_one(self.boto3_raw_data["grok"])

    @cached_property
    def listToMap(self):  # pragma: no cover
        return ListToMap.make_one(self.boto3_raw_data["listToMap"])

    @cached_property
    def lowerCaseString(self):  # pragma: no cover
        return LowerCaseStringOutput.make_one(self.boto3_raw_data["lowerCaseString"])

    @cached_property
    def moveKeys(self):  # pragma: no cover
        return MoveKeysOutput.make_one(self.boto3_raw_data["moveKeys"])

    @cached_property
    def parseCloudfront(self):  # pragma: no cover
        return ParseCloudfront.make_one(self.boto3_raw_data["parseCloudfront"])

    @cached_property
    def parseJSON(self):  # pragma: no cover
        return ParseJSON.make_one(self.boto3_raw_data["parseJSON"])

    @cached_property
    def parseKeyValue(self):  # pragma: no cover
        return ParseKeyValue.make_one(self.boto3_raw_data["parseKeyValue"])

    @cached_property
    def parseRoute53(self):  # pragma: no cover
        return ParseRoute53.make_one(self.boto3_raw_data["parseRoute53"])

    @cached_property
    def parseToOCSF(self):  # pragma: no cover
        return ParseToOCSF.make_one(self.boto3_raw_data["parseToOCSF"])

    @cached_property
    def parsePostgres(self):  # pragma: no cover
        return ParsePostgres.make_one(self.boto3_raw_data["parsePostgres"])

    @cached_property
    def parseVPC(self):  # pragma: no cover
        return ParseVPC.make_one(self.boto3_raw_data["parseVPC"])

    @cached_property
    def parseWAF(self):  # pragma: no cover
        return ParseWAF.make_one(self.boto3_raw_data["parseWAF"])

    @cached_property
    def renameKeys(self):  # pragma: no cover
        return RenameKeysOutput.make_one(self.boto3_raw_data["renameKeys"])

    @cached_property
    def splitString(self):  # pragma: no cover
        return SplitStringOutput.make_one(self.boto3_raw_data["splitString"])

    @cached_property
    def substituteString(self):  # pragma: no cover
        return SubstituteStringOutput.make_one(self.boto3_raw_data["substituteString"])

    @cached_property
    def trimString(self):  # pragma: no cover
        return TrimStringOutput.make_one(self.boto3_raw_data["trimString"])

    @cached_property
    def typeConverter(self):  # pragma: no cover
        return TypeConverterOutput.make_one(self.boto3_raw_data["typeConverter"])

    @cached_property
    def upperCaseString(self):  # pragma: no cover
        return UpperCaseStringOutput.make_one(self.boto3_raw_data["upperCaseString"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProcessorOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProcessorOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeConfigurationTemplatesResponse:
    boto3_raw_data: "type_defs.DescribeConfigurationTemplatesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def configurationTemplates(self):  # pragma: no cover
        return ConfigurationTemplate.make_many(
            self.boto3_raw_data["configurationTemplates"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeConfigurationTemplatesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeConfigurationTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartLiveTailResponse:
    boto3_raw_data: "type_defs.StartLiveTailResponseTypeDef" = dataclasses.field()

    responseStream = field("responseStream")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartLiveTailResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartLiveTailResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntegrationDetails:
    boto3_raw_data: "type_defs.IntegrationDetailsTypeDef" = dataclasses.field()

    @cached_property
    def openSearchIntegrationDetails(self):  # pragma: no cover
        return OpenSearchIntegrationDetails.make_one(
            self.boto3_raw_data["openSearchIntegrationDetails"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IntegrationDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IntegrationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTransformerResponse:
    boto3_raw_data: "type_defs.GetTransformerResponseTypeDef" = dataclasses.field()

    logGroupIdentifier = field("logGroupIdentifier")
    creationTime = field("creationTime")
    lastModifiedTime = field("lastModifiedTime")

    @cached_property
    def transformerConfig(self):  # pragma: no cover
        return ProcessorOutput.make_many(self.boto3_raw_data["transformerConfig"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTransformerResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTransformerResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Processor:
    boto3_raw_data: "type_defs.ProcessorTypeDef" = dataclasses.field()

    addKeys = field("addKeys")
    copyValue = field("copyValue")
    csv = field("csv")
    dateTimeConverter = field("dateTimeConverter")
    deleteKeys = field("deleteKeys")

    @cached_property
    def grok(self):  # pragma: no cover
        return Grok.make_one(self.boto3_raw_data["grok"])

    @cached_property
    def listToMap(self):  # pragma: no cover
        return ListToMap.make_one(self.boto3_raw_data["listToMap"])

    lowerCaseString = field("lowerCaseString")
    moveKeys = field("moveKeys")

    @cached_property
    def parseCloudfront(self):  # pragma: no cover
        return ParseCloudfront.make_one(self.boto3_raw_data["parseCloudfront"])

    @cached_property
    def parseJSON(self):  # pragma: no cover
        return ParseJSON.make_one(self.boto3_raw_data["parseJSON"])

    @cached_property
    def parseKeyValue(self):  # pragma: no cover
        return ParseKeyValue.make_one(self.boto3_raw_data["parseKeyValue"])

    @cached_property
    def parseRoute53(self):  # pragma: no cover
        return ParseRoute53.make_one(self.boto3_raw_data["parseRoute53"])

    @cached_property
    def parseToOCSF(self):  # pragma: no cover
        return ParseToOCSF.make_one(self.boto3_raw_data["parseToOCSF"])

    @cached_property
    def parsePostgres(self):  # pragma: no cover
        return ParsePostgres.make_one(self.boto3_raw_data["parsePostgres"])

    @cached_property
    def parseVPC(self):  # pragma: no cover
        return ParseVPC.make_one(self.boto3_raw_data["parseVPC"])

    @cached_property
    def parseWAF(self):  # pragma: no cover
        return ParseWAF.make_one(self.boto3_raw_data["parseWAF"])

    renameKeys = field("renameKeys")
    splitString = field("splitString")
    substituteString = field("substituteString")
    trimString = field("trimString")
    typeConverter = field("typeConverter")
    upperCaseString = field("upperCaseString")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProcessorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProcessorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIntegrationResponse:
    boto3_raw_data: "type_defs.GetIntegrationResponseTypeDef" = dataclasses.field()

    integrationName = field("integrationName")
    integrationType = field("integrationType")
    integrationStatus = field("integrationStatus")

    @cached_property
    def integrationDetails(self):  # pragma: no cover
        return IntegrationDetails.make_one(self.boto3_raw_data["integrationDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIntegrationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIntegrationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutTransformerRequest:
    boto3_raw_data: "type_defs.PutTransformerRequestTypeDef" = dataclasses.field()

    logGroupIdentifier = field("logGroupIdentifier")
    transformerConfig = field("transformerConfig")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PutTransformerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutTransformerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TestTransformerRequest:
    boto3_raw_data: "type_defs.TestTransformerRequestTypeDef" = dataclasses.field()

    transformerConfig = field("transformerConfig")
    logEventMessages = field("logEventMessages")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TestTransformerRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TestTransformerRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
