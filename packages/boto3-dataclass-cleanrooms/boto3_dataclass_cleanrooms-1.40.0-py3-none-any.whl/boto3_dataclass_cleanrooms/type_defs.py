# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cleanrooms import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AggregateColumnOutput:
    boto3_raw_data: "type_defs.AggregateColumnOutputTypeDef" = dataclasses.field()

    columnNames = field("columnNames")
    function = field("function")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AggregateColumnOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregateColumnOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregateColumn:
    boto3_raw_data: "type_defs.AggregateColumnTypeDef" = dataclasses.field()

    columnNames = field("columnNames")
    function = field("function")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AggregateColumnTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AggregateColumnTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AggregationConstraint:
    boto3_raw_data: "type_defs.AggregationConstraintTypeDef" = dataclasses.field()

    columnName = field("columnName")
    minimum = field("minimum")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AggregationConstraintTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AggregationConstraintTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisParameter:
    boto3_raw_data: "type_defs.AnalysisParameterTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")
    defaultValue = field("defaultValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnalysisParameterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisRuleListOutput:
    boto3_raw_data: "type_defs.AnalysisRuleListOutputTypeDef" = dataclasses.field()

    joinColumns = field("joinColumns")
    listColumns = field("listColumns")
    allowedJoinOperators = field("allowedJoinOperators")
    additionalAnalyses = field("additionalAnalyses")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalysisRuleListOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisRuleListOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisRuleList:
    boto3_raw_data: "type_defs.AnalysisRuleListTypeDef" = dataclasses.field()

    joinColumns = field("joinColumns")
    listColumns = field("listColumns")
    allowedJoinOperators = field("allowedJoinOperators")
    additionalAnalyses = field("additionalAnalyses")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnalysisRuleListTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisRuleListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisSchemaOutput:
    boto3_raw_data: "type_defs.AnalysisSchemaOutputTypeDef" = dataclasses.field()

    referencedTables = field("referencedTables")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalysisSchemaOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisSchemaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisSchema:
    boto3_raw_data: "type_defs.AnalysisSchemaTypeDef" = dataclasses.field()

    referencedTables = field("referencedTables")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnalysisSchemaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnalysisSchemaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Hash:
    boto3_raw_data: "type_defs.HashTypeDef" = dataclasses.field()

    sha256 = field("sha256")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.HashTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.HashTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class S3Location:
    boto3_raw_data: "type_defs.S3LocationTypeDef" = dataclasses.field()

    bucket = field("bucket")
    key = field("key")

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
class AnalysisTemplateSummary:
    boto3_raw_data: "type_defs.AnalysisTemplateSummaryTypeDef" = dataclasses.field()

    arn = field("arn")
    createTime = field("createTime")
    id = field("id")
    name = field("name")
    updateTime = field("updateTime")
    membershipArn = field("membershipArn")
    membershipId = field("membershipId")
    collaborationArn = field("collaborationArn")
    collaborationId = field("collaborationId")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalysisTemplateSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisTemplateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ErrorMessageConfiguration:
    boto3_raw_data: "type_defs.ErrorMessageConfigurationTypeDef" = dataclasses.field()

    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ErrorMessageConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ErrorMessageConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisTemplateValidationStatusReason:
    boto3_raw_data: "type_defs.AnalysisTemplateValidationStatusReasonTypeDef" = (
        dataclasses.field()
    )

    message = field("message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AnalysisTemplateValidationStatusReasonTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisTemplateValidationStatusReasonTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AthenaTableReference:
    boto3_raw_data: "type_defs.AthenaTableReferenceTypeDef" = dataclasses.field()

    workGroup = field("workGroup")
    databaseName = field("databaseName")
    tableName = field("tableName")
    outputLocation = field("outputLocation")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AthenaTableReferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AthenaTableReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetCollaborationAnalysisTemplateError:
    boto3_raw_data: "type_defs.BatchGetCollaborationAnalysisTemplateErrorTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    code = field("code")
    message = field("message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetCollaborationAnalysisTemplateErrorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetCollaborationAnalysisTemplateErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetCollaborationAnalysisTemplateInput:
    boto3_raw_data: "type_defs.BatchGetCollaborationAnalysisTemplateInputTypeDef" = (
        dataclasses.field()
    )

    collaborationIdentifier = field("collaborationIdentifier")
    analysisTemplateArns = field("analysisTemplateArns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetCollaborationAnalysisTemplateInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetCollaborationAnalysisTemplateInputTypeDef"]
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
class BatchGetSchemaAnalysisRuleError:
    boto3_raw_data: "type_defs.BatchGetSchemaAnalysisRuleErrorTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    type = field("type")
    code = field("code")
    message = field("message")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetSchemaAnalysisRuleErrorTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetSchemaAnalysisRuleErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaAnalysisRuleRequest:
    boto3_raw_data: "type_defs.SchemaAnalysisRuleRequestTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SchemaAnalysisRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchemaAnalysisRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetSchemaError:
    boto3_raw_data: "type_defs.BatchGetSchemaErrorTypeDef" = dataclasses.field()

    name = field("name")
    code = field("code")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetSchemaErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetSchemaErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetSchemaInput:
    boto3_raw_data: "type_defs.BatchGetSchemaInputTypeDef" = dataclasses.field()

    collaborationIdentifier = field("collaborationIdentifier")
    names = field("names")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetSchemaInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetSchemaInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BilledJobResourceUtilization:
    boto3_raw_data: "type_defs.BilledJobResourceUtilizationTypeDef" = (
        dataclasses.field()
    )

    units = field("units")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BilledJobResourceUtilizationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BilledJobResourceUtilizationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BilledResourceUtilization:
    boto3_raw_data: "type_defs.BilledResourceUtilizationTypeDef" = dataclasses.field()

    units = field("units")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BilledResourceUtilizationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BilledResourceUtilizationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberChangeSpecificationOutput:
    boto3_raw_data: "type_defs.MemberChangeSpecificationOutputTypeDef" = (
        dataclasses.field()
    )

    accountId = field("accountId")
    memberAbilities = field("memberAbilities")
    displayName = field("displayName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MemberChangeSpecificationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemberChangeSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollaborationAnalysisTemplateSummary:
    boto3_raw_data: "type_defs.CollaborationAnalysisTemplateSummaryTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    createTime = field("createTime")
    id = field("id")
    name = field("name")
    updateTime = field("updateTime")
    collaborationArn = field("collaborationArn")
    collaborationId = field("collaborationId")
    creatorAccountId = field("creatorAccountId")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CollaborationAnalysisTemplateSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollaborationAnalysisTemplateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollaborationConfiguredAudienceModelAssociationSummary:
    boto3_raw_data: (
        "type_defs.CollaborationConfiguredAudienceModelAssociationSummaryTypeDef"
    ) = dataclasses.field()

    arn = field("arn")
    createTime = field("createTime")
    id = field("id")
    name = field("name")
    updateTime = field("updateTime")
    collaborationArn = field("collaborationArn")
    collaborationId = field("collaborationId")
    creatorAccountId = field("creatorAccountId")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CollaborationConfiguredAudienceModelAssociationSummaryTypeDef"
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
                "type_defs.CollaborationConfiguredAudienceModelAssociationSummaryTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollaborationConfiguredAudienceModelAssociation:
    boto3_raw_data: (
        "type_defs.CollaborationConfiguredAudienceModelAssociationTypeDef"
    ) = dataclasses.field()

    id = field("id")
    arn = field("arn")
    collaborationId = field("collaborationId")
    collaborationArn = field("collaborationArn")
    configuredAudienceModelArn = field("configuredAudienceModelArn")
    name = field("name")
    creatorAccountId = field("creatorAccountId")
    createTime = field("createTime")
    updateTime = field("updateTime")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CollaborationConfiguredAudienceModelAssociationTypeDef"
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
                "type_defs.CollaborationConfiguredAudienceModelAssociationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdNamespaceAssociationInputReferenceConfig:
    boto3_raw_data: "type_defs.IdNamespaceAssociationInputReferenceConfigTypeDef" = (
        dataclasses.field()
    )

    inputReferenceArn = field("inputReferenceArn")
    manageResourcePolicies = field("manageResourcePolicies")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IdNamespaceAssociationInputReferenceConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdNamespaceAssociationInputReferenceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdNamespaceAssociationInputReferencePropertiesSummary:
    boto3_raw_data: (
        "type_defs.IdNamespaceAssociationInputReferencePropertiesSummaryTypeDef"
    ) = dataclasses.field()

    idNamespaceType = field("idNamespaceType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IdNamespaceAssociationInputReferencePropertiesSummaryTypeDef"
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
                "type_defs.IdNamespaceAssociationInputReferencePropertiesSummaryTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdMappingConfig:
    boto3_raw_data: "type_defs.IdMappingConfigTypeDef" = dataclasses.field()

    allowUseAsDimensionColumn = field("allowUseAsDimensionColumn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IdMappingConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IdMappingConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdNamespaceAssociationInputReferenceProperties:
    boto3_raw_data: (
        "type_defs.IdNamespaceAssociationInputReferencePropertiesTypeDef"
    ) = dataclasses.field()

    idNamespaceType = field("idNamespaceType")
    idMappingWorkflowsSupported = field("idMappingWorkflowsSupported")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IdNamespaceAssociationInputReferencePropertiesTypeDef"
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
                "type_defs.IdNamespaceAssociationInputReferencePropertiesTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollaborationPrivacyBudgetTemplateSummary:
    boto3_raw_data: "type_defs.CollaborationPrivacyBudgetTemplateSummaryTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    arn = field("arn")
    collaborationId = field("collaborationId")
    collaborationArn = field("collaborationArn")
    creatorAccountId = field("creatorAccountId")
    privacyBudgetType = field("privacyBudgetType")
    createTime = field("createTime")
    updateTime = field("updateTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CollaborationPrivacyBudgetTemplateSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollaborationPrivacyBudgetTemplateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollaborationSummary:
    boto3_raw_data: "type_defs.CollaborationSummaryTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    name = field("name")
    creatorAccountId = field("creatorAccountId")
    creatorDisplayName = field("creatorDisplayName")
    createTime = field("createTime")
    updateTime = field("updateTime")
    memberStatus = field("memberStatus")
    membershipId = field("membershipId")
    membershipArn = field("membershipArn")
    analyticsEngine = field("analyticsEngine")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CollaborationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollaborationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DataEncryptionMetadata:
    boto3_raw_data: "type_defs.DataEncryptionMetadataTypeDef" = dataclasses.field()

    allowCleartext = field("allowCleartext")
    allowDuplicates = field("allowDuplicates")
    allowJoinsOnColumnsWithDifferentNames = field(
        "allowJoinsOnColumnsWithDifferentNames"
    )
    preserveNulls = field("preserveNulls")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DataEncryptionMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DataEncryptionMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Column:
    boto3_raw_data: "type_defs.ColumnTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ColumnTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ColumnTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class WorkerComputeConfiguration:
    boto3_raw_data: "type_defs.WorkerComputeConfigurationTypeDef" = dataclasses.field()

    type = field("type")
    number = field("number")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.WorkerComputeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.WorkerComputeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DirectAnalysisConfigurationDetails:
    boto3_raw_data: "type_defs.DirectAnalysisConfigurationDetailsTypeDef" = (
        dataclasses.field()
    )

    receiverAccountIds = field("receiverAccountIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DirectAnalysisConfigurationDetailsTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DirectAnalysisConfigurationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredAudienceModelAssociationSummary:
    boto3_raw_data: "type_defs.ConfiguredAudienceModelAssociationSummaryTypeDef" = (
        dataclasses.field()
    )

    membershipId = field("membershipId")
    membershipArn = field("membershipArn")
    collaborationArn = field("collaborationArn")
    collaborationId = field("collaborationId")
    createTime = field("createTime")
    updateTime = field("updateTime")
    id = field("id")
    arn = field("arn")
    name = field("name")
    configuredAudienceModelArn = field("configuredAudienceModelArn")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfiguredAudienceModelAssociationSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfiguredAudienceModelAssociationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredAudienceModelAssociation:
    boto3_raw_data: "type_defs.ConfiguredAudienceModelAssociationTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    arn = field("arn")
    configuredAudienceModelArn = field("configuredAudienceModelArn")
    membershipId = field("membershipId")
    membershipArn = field("membershipArn")
    collaborationId = field("collaborationId")
    collaborationArn = field("collaborationArn")
    name = field("name")
    manageResourcePolicies = field("manageResourcePolicies")
    createTime = field("createTime")
    updateTime = field("updateTime")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfiguredAudienceModelAssociationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfiguredAudienceModelAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredTableAssociationAnalysisRuleAggregationOutput:
    boto3_raw_data: (
        "type_defs.ConfiguredTableAssociationAnalysisRuleAggregationOutputTypeDef"
    ) = dataclasses.field()

    allowedResultReceivers = field("allowedResultReceivers")
    allowedAdditionalAnalyses = field("allowedAdditionalAnalyses")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfiguredTableAssociationAnalysisRuleAggregationOutputTypeDef"
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
                "type_defs.ConfiguredTableAssociationAnalysisRuleAggregationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredTableAssociationAnalysisRuleAggregation:
    boto3_raw_data: (
        "type_defs.ConfiguredTableAssociationAnalysisRuleAggregationTypeDef"
    ) = dataclasses.field()

    allowedResultReceivers = field("allowedResultReceivers")
    allowedAdditionalAnalyses = field("allowedAdditionalAnalyses")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfiguredTableAssociationAnalysisRuleAggregationTypeDef"
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
                "type_defs.ConfiguredTableAssociationAnalysisRuleAggregationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredTableAssociationAnalysisRuleCustomOutput:
    boto3_raw_data: (
        "type_defs.ConfiguredTableAssociationAnalysisRuleCustomOutputTypeDef"
    ) = dataclasses.field()

    allowedResultReceivers = field("allowedResultReceivers")
    allowedAdditionalAnalyses = field("allowedAdditionalAnalyses")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfiguredTableAssociationAnalysisRuleCustomOutputTypeDef"
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
                "type_defs.ConfiguredTableAssociationAnalysisRuleCustomOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredTableAssociationAnalysisRuleCustom:
    boto3_raw_data: "type_defs.ConfiguredTableAssociationAnalysisRuleCustomTypeDef" = (
        dataclasses.field()
    )

    allowedResultReceivers = field("allowedResultReceivers")
    allowedAdditionalAnalyses = field("allowedAdditionalAnalyses")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfiguredTableAssociationAnalysisRuleCustomTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfiguredTableAssociationAnalysisRuleCustomTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredTableAssociationAnalysisRuleListOutput:
    boto3_raw_data: (
        "type_defs.ConfiguredTableAssociationAnalysisRuleListOutputTypeDef"
    ) = dataclasses.field()

    allowedResultReceivers = field("allowedResultReceivers")
    allowedAdditionalAnalyses = field("allowedAdditionalAnalyses")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfiguredTableAssociationAnalysisRuleListOutputTypeDef"
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
                "type_defs.ConfiguredTableAssociationAnalysisRuleListOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredTableAssociationAnalysisRuleList:
    boto3_raw_data: "type_defs.ConfiguredTableAssociationAnalysisRuleListTypeDef" = (
        dataclasses.field()
    )

    allowedResultReceivers = field("allowedResultReceivers")
    allowedAdditionalAnalyses = field("allowedAdditionalAnalyses")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfiguredTableAssociationAnalysisRuleListTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfiguredTableAssociationAnalysisRuleListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredTableAssociationSummary:
    boto3_raw_data: "type_defs.ConfiguredTableAssociationSummaryTypeDef" = (
        dataclasses.field()
    )

    configuredTableId = field("configuredTableId")
    membershipId = field("membershipId")
    membershipArn = field("membershipArn")
    name = field("name")
    createTime = field("createTime")
    updateTime = field("updateTime")
    id = field("id")
    arn = field("arn")
    analysisRuleTypes = field("analysisRuleTypes")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfiguredTableAssociationSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfiguredTableAssociationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredTableAssociation:
    boto3_raw_data: "type_defs.ConfiguredTableAssociationTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")
    configuredTableId = field("configuredTableId")
    configuredTableArn = field("configuredTableArn")
    membershipId = field("membershipId")
    membershipArn = field("membershipArn")
    roleArn = field("roleArn")
    name = field("name")
    createTime = field("createTime")
    updateTime = field("updateTime")
    description = field("description")
    analysisRuleTypes = field("analysisRuleTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfiguredTableAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfiguredTableAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredTableSummary:
    boto3_raw_data: "type_defs.ConfiguredTableSummaryTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    name = field("name")
    createTime = field("createTime")
    updateTime = field("updateTime")
    analysisRuleTypes = field("analysisRuleTypes")
    analysisMethod = field("analysisMethod")
    selectedAnalysisMethods = field("selectedAnalysisMethods")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfiguredTableSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfiguredTableSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConsolidatedPolicyList:
    boto3_raw_data: "type_defs.ConsolidatedPolicyListTypeDef" = dataclasses.field()

    joinColumns = field("joinColumns")
    listColumns = field("listColumns")
    allowedJoinOperators = field("allowedJoinOperators")
    additionalAnalyses = field("additionalAnalyses")
    allowedResultReceivers = field("allowedResultReceivers")
    allowedAdditionalAnalyses = field("allowedAdditionalAnalyses")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConsolidatedPolicyListTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConsolidatedPolicyListTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfiguredAudienceModelAssociationInput:
    boto3_raw_data: "type_defs.CreateConfiguredAudienceModelAssociationInputTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")
    configuredAudienceModelArn = field("configuredAudienceModelArn")
    configuredAudienceModelAssociationName = field(
        "configuredAudienceModelAssociationName"
    )
    manageResourcePolicies = field("manageResourcePolicies")
    tags = field("tags")
    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConfiguredAudienceModelAssociationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConfiguredAudienceModelAssociationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfiguredTableAssociationInput:
    boto3_raw_data: "type_defs.CreateConfiguredTableAssociationInputTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    membershipIdentifier = field("membershipIdentifier")
    configuredTableIdentifier = field("configuredTableIdentifier")
    roleArn = field("roleArn")
    description = field("description")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConfiguredTableAssociationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConfiguredTableAssociationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdMappingTableInputReferenceConfig:
    boto3_raw_data: "type_defs.IdMappingTableInputReferenceConfigTypeDef" = (
        dataclasses.field()
    )

    inputReferenceArn = field("inputReferenceArn")
    manageResourcePolicies = field("manageResourcePolicies")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IdMappingTableInputReferenceConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdMappingTableInputReferenceConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAnalysisTemplateInput:
    boto3_raw_data: "type_defs.DeleteAnalysisTemplateInputTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    analysisTemplateIdentifier = field("analysisTemplateIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAnalysisTemplateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAnalysisTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCollaborationInput:
    boto3_raw_data: "type_defs.DeleteCollaborationInputTypeDef" = dataclasses.field()

    collaborationIdentifier = field("collaborationIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCollaborationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCollaborationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConfiguredAudienceModelAssociationInput:
    boto3_raw_data: "type_defs.DeleteConfiguredAudienceModelAssociationInputTypeDef" = (
        dataclasses.field()
    )

    configuredAudienceModelAssociationIdentifier = field(
        "configuredAudienceModelAssociationIdentifier"
    )
    membershipIdentifier = field("membershipIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteConfiguredAudienceModelAssociationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConfiguredAudienceModelAssociationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConfiguredTableAnalysisRuleInput:
    boto3_raw_data: "type_defs.DeleteConfiguredTableAnalysisRuleInputTypeDef" = (
        dataclasses.field()
    )

    configuredTableIdentifier = field("configuredTableIdentifier")
    analysisRuleType = field("analysisRuleType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteConfiguredTableAnalysisRuleInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConfiguredTableAnalysisRuleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConfiguredTableAssociationAnalysisRuleInput:
    boto3_raw_data: (
        "type_defs.DeleteConfiguredTableAssociationAnalysisRuleInputTypeDef"
    ) = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    configuredTableAssociationIdentifier = field("configuredTableAssociationIdentifier")
    analysisRuleType = field("analysisRuleType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteConfiguredTableAssociationAnalysisRuleInputTypeDef"
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
                "type_defs.DeleteConfiguredTableAssociationAnalysisRuleInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConfiguredTableAssociationInput:
    boto3_raw_data: "type_defs.DeleteConfiguredTableAssociationInputTypeDef" = (
        dataclasses.field()
    )

    configuredTableAssociationIdentifier = field("configuredTableAssociationIdentifier")
    membershipIdentifier = field("membershipIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteConfiguredTableAssociationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConfiguredTableAssociationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteConfiguredTableInput:
    boto3_raw_data: "type_defs.DeleteConfiguredTableInputTypeDef" = dataclasses.field()

    configuredTableIdentifier = field("configuredTableIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteConfiguredTableInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteConfiguredTableInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIdMappingTableInput:
    boto3_raw_data: "type_defs.DeleteIdMappingTableInputTypeDef" = dataclasses.field()

    idMappingTableIdentifier = field("idMappingTableIdentifier")
    membershipIdentifier = field("membershipIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIdMappingTableInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIdMappingTableInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIdNamespaceAssociationInput:
    boto3_raw_data: "type_defs.DeleteIdNamespaceAssociationInputTypeDef" = (
        dataclasses.field()
    )

    idNamespaceAssociationIdentifier = field("idNamespaceAssociationIdentifier")
    membershipIdentifier = field("membershipIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteIdNamespaceAssociationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIdNamespaceAssociationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMemberInput:
    boto3_raw_data: "type_defs.DeleteMemberInputTypeDef" = dataclasses.field()

    collaborationIdentifier = field("collaborationIdentifier")
    accountId = field("accountId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteMemberInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMemberInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMembershipInput:
    boto3_raw_data: "type_defs.DeleteMembershipInputTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMembershipInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMembershipInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeletePrivacyBudgetTemplateInput:
    boto3_raw_data: "type_defs.DeletePrivacyBudgetTemplateInputTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")
    privacyBudgetTemplateIdentifier = field("privacyBudgetTemplateIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeletePrivacyBudgetTemplateInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeletePrivacyBudgetTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DifferentialPrivacyColumn:
    boto3_raw_data: "type_defs.DifferentialPrivacyColumnTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DifferentialPrivacyColumnTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DifferentialPrivacyColumnTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DifferentialPrivacySensitivityParameters:
    boto3_raw_data: "type_defs.DifferentialPrivacySensitivityParametersTypeDef" = (
        dataclasses.field()
    )

    aggregationType = field("aggregationType")
    aggregationExpression = field("aggregationExpression")
    userContributionLimit = field("userContributionLimit")
    minColumnValue = field("minColumnValue")
    maxColumnValue = field("maxColumnValue")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DifferentialPrivacySensitivityParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DifferentialPrivacySensitivityParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DifferentialPrivacyPreviewAggregation:
    boto3_raw_data: "type_defs.DifferentialPrivacyPreviewAggregationTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    maxCount = field("maxCount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DifferentialPrivacyPreviewAggregationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DifferentialPrivacyPreviewAggregationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DifferentialPrivacyPreviewParametersInput:
    boto3_raw_data: "type_defs.DifferentialPrivacyPreviewParametersInputTypeDef" = (
        dataclasses.field()
    )

    epsilon = field("epsilon")
    usersNoisePerQuery = field("usersNoisePerQuery")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DifferentialPrivacyPreviewParametersInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DifferentialPrivacyPreviewParametersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DifferentialPrivacyPrivacyBudgetAggregation:
    boto3_raw_data: "type_defs.DifferentialPrivacyPrivacyBudgetAggregationTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    maxCount = field("maxCount")
    remainingCount = field("remainingCount")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DifferentialPrivacyPrivacyBudgetAggregationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DifferentialPrivacyPrivacyBudgetAggregationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DifferentialPrivacyTemplateParametersInput:
    boto3_raw_data: "type_defs.DifferentialPrivacyTemplateParametersInputTypeDef" = (
        dataclasses.field()
    )

    epsilon = field("epsilon")
    usersNoisePerQuery = field("usersNoisePerQuery")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DifferentialPrivacyTemplateParametersInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DifferentialPrivacyTemplateParametersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DifferentialPrivacyTemplateParametersOutput:
    boto3_raw_data: "type_defs.DifferentialPrivacyTemplateParametersOutputTypeDef" = (
        dataclasses.field()
    )

    epsilon = field("epsilon")
    usersNoisePerQuery = field("usersNoisePerQuery")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DifferentialPrivacyTemplateParametersOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DifferentialPrivacyTemplateParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DifferentialPrivacyTemplateUpdateParameters:
    boto3_raw_data: "type_defs.DifferentialPrivacyTemplateUpdateParametersTypeDef" = (
        dataclasses.field()
    )

    epsilon = field("epsilon")
    usersNoisePerQuery = field("usersNoisePerQuery")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DifferentialPrivacyTemplateUpdateParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DifferentialPrivacyTemplateUpdateParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnalysisTemplateInput:
    boto3_raw_data: "type_defs.GetAnalysisTemplateInputTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    analysisTemplateIdentifier = field("analysisTemplateIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAnalysisTemplateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnalysisTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCollaborationAnalysisTemplateInput:
    boto3_raw_data: "type_defs.GetCollaborationAnalysisTemplateInputTypeDef" = (
        dataclasses.field()
    )

    collaborationIdentifier = field("collaborationIdentifier")
    analysisTemplateArn = field("analysisTemplateArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCollaborationAnalysisTemplateInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCollaborationAnalysisTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCollaborationChangeRequestInput:
    boto3_raw_data: "type_defs.GetCollaborationChangeRequestInputTypeDef" = (
        dataclasses.field()
    )

    collaborationIdentifier = field("collaborationIdentifier")
    changeRequestIdentifier = field("changeRequestIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCollaborationChangeRequestInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCollaborationChangeRequestInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCollaborationConfiguredAudienceModelAssociationInput:
    boto3_raw_data: (
        "type_defs.GetCollaborationConfiguredAudienceModelAssociationInputTypeDef"
    ) = dataclasses.field()

    collaborationIdentifier = field("collaborationIdentifier")
    configuredAudienceModelAssociationIdentifier = field(
        "configuredAudienceModelAssociationIdentifier"
    )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCollaborationConfiguredAudienceModelAssociationInputTypeDef"
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
                "type_defs.GetCollaborationConfiguredAudienceModelAssociationInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCollaborationIdNamespaceAssociationInput:
    boto3_raw_data: "type_defs.GetCollaborationIdNamespaceAssociationInputTypeDef" = (
        dataclasses.field()
    )

    collaborationIdentifier = field("collaborationIdentifier")
    idNamespaceAssociationIdentifier = field("idNamespaceAssociationIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCollaborationIdNamespaceAssociationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCollaborationIdNamespaceAssociationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCollaborationInput:
    boto3_raw_data: "type_defs.GetCollaborationInputTypeDef" = dataclasses.field()

    collaborationIdentifier = field("collaborationIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCollaborationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCollaborationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCollaborationPrivacyBudgetTemplateInput:
    boto3_raw_data: "type_defs.GetCollaborationPrivacyBudgetTemplateInputTypeDef" = (
        dataclasses.field()
    )

    collaborationIdentifier = field("collaborationIdentifier")
    privacyBudgetTemplateIdentifier = field("privacyBudgetTemplateIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCollaborationPrivacyBudgetTemplateInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCollaborationPrivacyBudgetTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfiguredAudienceModelAssociationInput:
    boto3_raw_data: "type_defs.GetConfiguredAudienceModelAssociationInputTypeDef" = (
        dataclasses.field()
    )

    configuredAudienceModelAssociationIdentifier = field(
        "configuredAudienceModelAssociationIdentifier"
    )
    membershipIdentifier = field("membershipIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConfiguredAudienceModelAssociationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfiguredAudienceModelAssociationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfiguredTableAnalysisRuleInput:
    boto3_raw_data: "type_defs.GetConfiguredTableAnalysisRuleInputTypeDef" = (
        dataclasses.field()
    )

    configuredTableIdentifier = field("configuredTableIdentifier")
    analysisRuleType = field("analysisRuleType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConfiguredTableAnalysisRuleInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfiguredTableAnalysisRuleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfiguredTableAssociationAnalysisRuleInput:
    boto3_raw_data: (
        "type_defs.GetConfiguredTableAssociationAnalysisRuleInputTypeDef"
    ) = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    configuredTableAssociationIdentifier = field("configuredTableAssociationIdentifier")
    analysisRuleType = field("analysisRuleType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConfiguredTableAssociationAnalysisRuleInputTypeDef"
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
                "type_defs.GetConfiguredTableAssociationAnalysisRuleInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfiguredTableAssociationInput:
    boto3_raw_data: "type_defs.GetConfiguredTableAssociationInputTypeDef" = (
        dataclasses.field()
    )

    configuredTableAssociationIdentifier = field("configuredTableAssociationIdentifier")
    membershipIdentifier = field("membershipIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConfiguredTableAssociationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfiguredTableAssociationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfiguredTableInput:
    boto3_raw_data: "type_defs.GetConfiguredTableInputTypeDef" = dataclasses.field()

    configuredTableIdentifier = field("configuredTableIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConfiguredTableInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfiguredTableInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdMappingTableInput:
    boto3_raw_data: "type_defs.GetIdMappingTableInputTypeDef" = dataclasses.field()

    idMappingTableIdentifier = field("idMappingTableIdentifier")
    membershipIdentifier = field("membershipIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIdMappingTableInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdMappingTableInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdNamespaceAssociationInput:
    boto3_raw_data: "type_defs.GetIdNamespaceAssociationInputTypeDef" = (
        dataclasses.field()
    )

    idNamespaceAssociationIdentifier = field("idNamespaceAssociationIdentifier")
    membershipIdentifier = field("membershipIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetIdNamespaceAssociationInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdNamespaceAssociationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMembershipInput:
    boto3_raw_data: "type_defs.GetMembershipInputTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMembershipInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMembershipInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPrivacyBudgetTemplateInput:
    boto3_raw_data: "type_defs.GetPrivacyBudgetTemplateInputTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")
    privacyBudgetTemplateIdentifier = field("privacyBudgetTemplateIdentifier")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPrivacyBudgetTemplateInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPrivacyBudgetTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProtectedJobInput:
    boto3_raw_data: "type_defs.GetProtectedJobInputTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    protectedJobIdentifier = field("protectedJobIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetProtectedJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProtectedJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProtectedQueryInput:
    boto3_raw_data: "type_defs.GetProtectedQueryInputTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    protectedQueryIdentifier = field("protectedQueryIdentifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetProtectedQueryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProtectedQueryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSchemaAnalysisRuleInput:
    boto3_raw_data: "type_defs.GetSchemaAnalysisRuleInputTypeDef" = dataclasses.field()

    collaborationIdentifier = field("collaborationIdentifier")
    name = field("name")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSchemaAnalysisRuleInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSchemaAnalysisRuleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSchemaInput:
    boto3_raw_data: "type_defs.GetSchemaInputTypeDef" = dataclasses.field()

    collaborationIdentifier = field("collaborationIdentifier")
    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSchemaInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetSchemaInputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GlueTableReference:
    boto3_raw_data: "type_defs.GlueTableReferenceTypeDef" = dataclasses.field()

    tableName = field("tableName")
    databaseName = field("databaseName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GlueTableReferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GlueTableReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdMappingTableInputSource:
    boto3_raw_data: "type_defs.IdMappingTableInputSourceTypeDef" = dataclasses.field()

    idNamespaceAssociationId = field("idNamespaceAssociationId")
    type = field("type")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdMappingTableInputSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdMappingTableInputSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class JobComputePaymentConfig:
    boto3_raw_data: "type_defs.JobComputePaymentConfigTypeDef" = dataclasses.field()

    isResponsible = field("isResponsible")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.JobComputePaymentConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.JobComputePaymentConfigTypeDef"]
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
class ListAnalysisTemplatesInput:
    boto3_raw_data: "type_defs.ListAnalysisTemplatesInputTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAnalysisTemplatesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnalysisTemplatesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationAnalysisTemplatesInput:
    boto3_raw_data: "type_defs.ListCollaborationAnalysisTemplatesInputTypeDef" = (
        dataclasses.field()
    )

    collaborationIdentifier = field("collaborationIdentifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationAnalysisTemplatesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollaborationAnalysisTemplatesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationChangeRequestsInput:
    boto3_raw_data: "type_defs.ListCollaborationChangeRequestsInputTypeDef" = (
        dataclasses.field()
    )

    collaborationIdentifier = field("collaborationIdentifier")
    status = field("status")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationChangeRequestsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollaborationChangeRequestsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationConfiguredAudienceModelAssociationsInput:
    boto3_raw_data: (
        "type_defs.ListCollaborationConfiguredAudienceModelAssociationsInputTypeDef"
    ) = dataclasses.field()

    collaborationIdentifier = field("collaborationIdentifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationConfiguredAudienceModelAssociationsInputTypeDef"
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
                "type_defs.ListCollaborationConfiguredAudienceModelAssociationsInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationIdNamespaceAssociationsInput:
    boto3_raw_data: "type_defs.ListCollaborationIdNamespaceAssociationsInputTypeDef" = (
        dataclasses.field()
    )

    collaborationIdentifier = field("collaborationIdentifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationIdNamespaceAssociationsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollaborationIdNamespaceAssociationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationPrivacyBudgetTemplatesInput:
    boto3_raw_data: "type_defs.ListCollaborationPrivacyBudgetTemplatesInputTypeDef" = (
        dataclasses.field()
    )

    collaborationIdentifier = field("collaborationIdentifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationPrivacyBudgetTemplatesInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollaborationPrivacyBudgetTemplatesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationPrivacyBudgetsInput:
    boto3_raw_data: "type_defs.ListCollaborationPrivacyBudgetsInputTypeDef" = (
        dataclasses.field()
    )

    collaborationIdentifier = field("collaborationIdentifier")
    privacyBudgetType = field("privacyBudgetType")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationPrivacyBudgetsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollaborationPrivacyBudgetsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationsInput:
    boto3_raw_data: "type_defs.ListCollaborationsInputTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    memberStatus = field("memberStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCollaborationsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollaborationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfiguredAudienceModelAssociationsInput:
    boto3_raw_data: "type_defs.ListConfiguredAudienceModelAssociationsInputTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfiguredAudienceModelAssociationsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfiguredAudienceModelAssociationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfiguredTableAssociationsInput:
    boto3_raw_data: "type_defs.ListConfiguredTableAssociationsInputTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfiguredTableAssociationsInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfiguredTableAssociationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfiguredTablesInput:
    boto3_raw_data: "type_defs.ListConfiguredTablesInputTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConfiguredTablesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfiguredTablesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdMappingTablesInput:
    boto3_raw_data: "type_defs.ListIdMappingTablesInputTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIdMappingTablesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdMappingTablesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdNamespaceAssociationsInput:
    boto3_raw_data: "type_defs.ListIdNamespaceAssociationsInputTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListIdNamespaceAssociationsInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdNamespaceAssociationsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMembersInput:
    boto3_raw_data: "type_defs.ListMembersInputTypeDef" = dataclasses.field()

    collaborationIdentifier = field("collaborationIdentifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListMembersInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMembersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMembershipsInput:
    boto3_raw_data: "type_defs.ListMembershipsInputTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMembershipsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMembershipsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPrivacyBudgetTemplatesInput:
    boto3_raw_data: "type_defs.ListPrivacyBudgetTemplatesInputTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPrivacyBudgetTemplatesInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPrivacyBudgetTemplatesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivacyBudgetTemplateSummary:
    boto3_raw_data: "type_defs.PrivacyBudgetTemplateSummaryTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    arn = field("arn")
    membershipId = field("membershipId")
    membershipArn = field("membershipArn")
    collaborationId = field("collaborationId")
    collaborationArn = field("collaborationArn")
    privacyBudgetType = field("privacyBudgetType")
    createTime = field("createTime")
    updateTime = field("updateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrivacyBudgetTemplateSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivacyBudgetTemplateSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPrivacyBudgetsInput:
    boto3_raw_data: "type_defs.ListPrivacyBudgetsInputTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    privacyBudgetType = field("privacyBudgetType")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPrivacyBudgetsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPrivacyBudgetsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProtectedJobsInput:
    boto3_raw_data: "type_defs.ListProtectedJobsInputTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    status = field("status")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProtectedJobsInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProtectedJobsInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProtectedQueriesInput:
    boto3_raw_data: "type_defs.ListProtectedQueriesInputTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    status = field("status")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProtectedQueriesInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProtectedQueriesInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSchemasInput:
    boto3_raw_data: "type_defs.ListSchemasInputTypeDef" = dataclasses.field()

    collaborationIdentifier = field("collaborationIdentifier")
    schemaType = field("schemaType")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListSchemasInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSchemasInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaSummary:
    boto3_raw_data: "type_defs.SchemaSummaryTypeDef" = dataclasses.field()

    name = field("name")
    type = field("type")
    creatorAccountId = field("creatorAccountId")
    createTime = field("createTime")
    updateTime = field("updateTime")
    collaborationId = field("collaborationId")
    collaborationArn = field("collaborationArn")
    analysisRuleTypes = field("analysisRuleTypes")
    analysisMethod = field("analysisMethod")
    selectedAnalysisMethods = field("selectedAnalysisMethods")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SchemaSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SchemaSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceInput:
    boto3_raw_data: "type_defs.ListTagsForResourceInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MLMemberAbilitiesOutput:
    boto3_raw_data: "type_defs.MLMemberAbilitiesOutputTypeDef" = dataclasses.field()

    customMLMemberAbilities = field("customMLMemberAbilities")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MLMemberAbilitiesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MLMemberAbilitiesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MLMemberAbilities:
    boto3_raw_data: "type_defs.MLMemberAbilitiesTypeDef" = dataclasses.field()

    customMLMemberAbilities = field("customMLMemberAbilities")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MLMemberAbilitiesTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MLMemberAbilitiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelInferencePaymentConfig:
    boto3_raw_data: "type_defs.ModelInferencePaymentConfigTypeDef" = dataclasses.field()

    isResponsible = field("isResponsible")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModelInferencePaymentConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelInferencePaymentConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ModelTrainingPaymentConfig:
    boto3_raw_data: "type_defs.ModelTrainingPaymentConfigTypeDef" = dataclasses.field()

    isResponsible = field("isResponsible")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ModelTrainingPaymentConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ModelTrainingPaymentConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberChangeSpecification:
    boto3_raw_data: "type_defs.MemberChangeSpecificationTypeDef" = dataclasses.field()

    accountId = field("accountId")
    memberAbilities = field("memberAbilities")
    displayName = field("displayName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MemberChangeSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemberChangeSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MembershipJobComputePaymentConfig:
    boto3_raw_data: "type_defs.MembershipJobComputePaymentConfigTypeDef" = (
        dataclasses.field()
    )

    isResponsible = field("isResponsible")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MembershipJobComputePaymentConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MembershipJobComputePaymentConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MembershipModelInferencePaymentConfig:
    boto3_raw_data: "type_defs.MembershipModelInferencePaymentConfigTypeDef" = (
        dataclasses.field()
    )

    isResponsible = field("isResponsible")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MembershipModelInferencePaymentConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MembershipModelInferencePaymentConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MembershipModelTrainingPaymentConfig:
    boto3_raw_data: "type_defs.MembershipModelTrainingPaymentConfigTypeDef" = (
        dataclasses.field()
    )

    isResponsible = field("isResponsible")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MembershipModelTrainingPaymentConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MembershipModelTrainingPaymentConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MembershipQueryComputePaymentConfig:
    boto3_raw_data: "type_defs.MembershipQueryComputePaymentConfigTypeDef" = (
        dataclasses.field()
    )

    isResponsible = field("isResponsible")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MembershipQueryComputePaymentConfigTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MembershipQueryComputePaymentConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedJobS3OutputConfigurationInput:
    boto3_raw_data: "type_defs.ProtectedJobS3OutputConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    bucket = field("bucket")
    keyPrefix = field("keyPrefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectedJobS3OutputConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedJobS3OutputConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedQueryS3OutputConfiguration:
    boto3_raw_data: "type_defs.ProtectedQueryS3OutputConfigurationTypeDef" = (
        dataclasses.field()
    )

    resultFormat = field("resultFormat")
    bucket = field("bucket")
    keyPrefix = field("keyPrefix")
    singleFileOutput = field("singleFileOutput")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectedQueryS3OutputConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedQueryS3OutputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryComputePaymentConfig:
    boto3_raw_data: "type_defs.QueryComputePaymentConfigTypeDef" = dataclasses.field()

    isResponsible = field("isResponsible")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.QueryComputePaymentConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryComputePaymentConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PopulateIdMappingTableInput:
    boto3_raw_data: "type_defs.PopulateIdMappingTableInputTypeDef" = dataclasses.field()

    idMappingTableIdentifier = field("idMappingTableIdentifier")
    membershipIdentifier = field("membershipIdentifier")
    jobType = field("jobType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PopulateIdMappingTableInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PopulateIdMappingTableInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedJobWorkerComputeConfiguration:
    boto3_raw_data: "type_defs.ProtectedJobWorkerComputeConfigurationTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    number = field("number")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectedJobWorkerComputeConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedJobWorkerComputeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedJobDirectAnalysisConfigurationDetails:
    boto3_raw_data: (
        "type_defs.ProtectedJobDirectAnalysisConfigurationDetailsTypeDef"
    ) = dataclasses.field()

    receiverAccountIds = field("receiverAccountIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectedJobDirectAnalysisConfigurationDetailsTypeDef"
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
                "type_defs.ProtectedJobDirectAnalysisConfigurationDetailsTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedJobError:
    boto3_raw_data: "type_defs.ProtectedJobErrorTypeDef" = dataclasses.field()

    message = field("message")
    code = field("code")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProtectedJobErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedJobErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedJobMemberOutputConfigurationInput:
    boto3_raw_data: "type_defs.ProtectedJobMemberOutputConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    accountId = field("accountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectedJobMemberOutputConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedJobMemberOutputConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedJobMemberOutputConfigurationOutput:
    boto3_raw_data: "type_defs.ProtectedJobMemberOutputConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    accountId = field("accountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectedJobMemberOutputConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedJobMemberOutputConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedJobS3OutputConfigurationOutput:
    boto3_raw_data: "type_defs.ProtectedJobS3OutputConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    bucket = field("bucket")
    keyPrefix = field("keyPrefix")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectedJobS3OutputConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedJobS3OutputConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedJobS3Output:
    boto3_raw_data: "type_defs.ProtectedJobS3OutputTypeDef" = dataclasses.field()

    location = field("location")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProtectedJobS3OutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedJobS3OutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedJobSingleMemberOutput:
    boto3_raw_data: "type_defs.ProtectedJobSingleMemberOutputTypeDef" = (
        dataclasses.field()
    )

    accountId = field("accountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProtectedJobSingleMemberOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedJobSingleMemberOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedJobParameters:
    boto3_raw_data: "type_defs.ProtectedJobParametersTypeDef" = dataclasses.field()

    analysisTemplateArn = field("analysisTemplateArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProtectedJobParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedJobParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedQueryMemberOutputConfiguration:
    boto3_raw_data: "type_defs.ProtectedQueryMemberOutputConfigurationTypeDef" = (
        dataclasses.field()
    )

    accountId = field("accountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectedQueryMemberOutputConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedQueryMemberOutputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedQueryS3Output:
    boto3_raw_data: "type_defs.ProtectedQueryS3OutputTypeDef" = dataclasses.field()

    location = field("location")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProtectedQueryS3OutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedQueryS3OutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedQuerySingleMemberOutput:
    boto3_raw_data: "type_defs.ProtectedQuerySingleMemberOutputTypeDef" = (
        dataclasses.field()
    )

    accountId = field("accountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProtectedQuerySingleMemberOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedQuerySingleMemberOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedQueryError:
    boto3_raw_data: "type_defs.ProtectedQueryErrorTypeDef" = dataclasses.field()

    message = field("message")
    code = field("code")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProtectedQueryErrorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedQueryErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedQuerySQLParametersOutput:
    boto3_raw_data: "type_defs.ProtectedQuerySQLParametersOutputTypeDef" = (
        dataclasses.field()
    )

    queryString = field("queryString")
    analysisTemplateArn = field("analysisTemplateArn")
    parameters = field("parameters")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectedQuerySQLParametersOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedQuerySQLParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedQuerySQLParameters:
    boto3_raw_data: "type_defs.ProtectedQuerySQLParametersTypeDef" = dataclasses.field()

    queryString = field("queryString")
    analysisTemplateArn = field("analysisTemplateArn")
    parameters = field("parameters")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProtectedQuerySQLParametersTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedQuerySQLParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryConstraintRequireOverlap:
    boto3_raw_data: "type_defs.QueryConstraintRequireOverlapTypeDef" = (
        dataclasses.field()
    )

    columns = field("columns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.QueryConstraintRequireOverlapTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.QueryConstraintRequireOverlapTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaStatusReason:
    boto3_raw_data: "type_defs.SchemaStatusReasonTypeDef" = dataclasses.field()

    code = field("code")
    message = field("message")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SchemaStatusReasonTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchemaStatusReasonTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnowflakeTableSchemaV1:
    boto3_raw_data: "type_defs.SnowflakeTableSchemaV1TypeDef" = dataclasses.field()

    columnName = field("columnName")
    columnType = field("columnType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SnowflakeTableSchemaV1TypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnowflakeTableSchemaV1TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceInput:
    boto3_raw_data: "type_defs.TagResourceInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TagResourceInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UntagResourceInput:
    boto3_raw_data: "type_defs.UntagResourceInputTypeDef" = dataclasses.field()

    resourceArn = field("resourceArn")
    tagKeys = field("tagKeys")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UntagResourceInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UntagResourceInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAnalysisTemplateInput:
    boto3_raw_data: "type_defs.UpdateAnalysisTemplateInputTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    analysisTemplateIdentifier = field("analysisTemplateIdentifier")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAnalysisTemplateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAnalysisTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCollaborationInput:
    boto3_raw_data: "type_defs.UpdateCollaborationInputTypeDef" = dataclasses.field()

    collaborationIdentifier = field("collaborationIdentifier")
    name = field("name")
    description = field("description")
    analyticsEngine = field("analyticsEngine")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCollaborationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCollaborationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConfiguredAudienceModelAssociationInput:
    boto3_raw_data: "type_defs.UpdateConfiguredAudienceModelAssociationInputTypeDef" = (
        dataclasses.field()
    )

    configuredAudienceModelAssociationIdentifier = field(
        "configuredAudienceModelAssociationIdentifier"
    )
    membershipIdentifier = field("membershipIdentifier")
    description = field("description")
    name = field("name")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConfiguredAudienceModelAssociationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConfiguredAudienceModelAssociationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConfiguredTableAssociationInput:
    boto3_raw_data: "type_defs.UpdateConfiguredTableAssociationInputTypeDef" = (
        dataclasses.field()
    )

    configuredTableAssociationIdentifier = field("configuredTableAssociationIdentifier")
    membershipIdentifier = field("membershipIdentifier")
    description = field("description")
    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConfiguredTableAssociationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConfiguredTableAssociationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIdMappingTableInput:
    boto3_raw_data: "type_defs.UpdateIdMappingTableInputTypeDef" = dataclasses.field()

    idMappingTableIdentifier = field("idMappingTableIdentifier")
    membershipIdentifier = field("membershipIdentifier")
    description = field("description")
    kmsKeyArn = field("kmsKeyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateIdMappingTableInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIdMappingTableInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProtectedJobInput:
    boto3_raw_data: "type_defs.UpdateProtectedJobInputTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    protectedJobIdentifier = field("protectedJobIdentifier")
    targetStatus = field("targetStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProtectedJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProtectedJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProtectedQueryInput:
    boto3_raw_data: "type_defs.UpdateProtectedQueryInputTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    protectedQueryIdentifier = field("protectedQueryIdentifier")
    targetStatus = field("targetStatus")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProtectedQueryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProtectedQueryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisRuleAggregationOutput:
    boto3_raw_data: "type_defs.AnalysisRuleAggregationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def aggregateColumns(self):  # pragma: no cover
        return AggregateColumnOutput.make_many(self.boto3_raw_data["aggregateColumns"])

    joinColumns = field("joinColumns")
    dimensionColumns = field("dimensionColumns")
    scalarFunctions = field("scalarFunctions")

    @cached_property
    def outputConstraints(self):  # pragma: no cover
        return AggregationConstraint.make_many(self.boto3_raw_data["outputConstraints"])

    joinRequired = field("joinRequired")
    allowedJoinOperators = field("allowedJoinOperators")
    additionalAnalyses = field("additionalAnalyses")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AnalysisRuleAggregationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisRuleAggregationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisRuleAggregation:
    boto3_raw_data: "type_defs.AnalysisRuleAggregationTypeDef" = dataclasses.field()

    @cached_property
    def aggregateColumns(self):  # pragma: no cover
        return AggregateColumn.make_many(self.boto3_raw_data["aggregateColumns"])

    joinColumns = field("joinColumns")
    dimensionColumns = field("dimensionColumns")
    scalarFunctions = field("scalarFunctions")

    @cached_property
    def outputConstraints(self):  # pragma: no cover
        return AggregationConstraint.make_many(self.boto3_raw_data["outputConstraints"])

    joinRequired = field("joinRequired")
    allowedJoinOperators = field("allowedJoinOperators")
    additionalAnalyses = field("additionalAnalyses")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalysisRuleAggregationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisRuleAggregationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConsolidatedPolicyAggregation:
    boto3_raw_data: "type_defs.ConsolidatedPolicyAggregationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def aggregateColumns(self):  # pragma: no cover
        return AggregateColumnOutput.make_many(self.boto3_raw_data["aggregateColumns"])

    joinColumns = field("joinColumns")
    dimensionColumns = field("dimensionColumns")
    scalarFunctions = field("scalarFunctions")

    @cached_property
    def outputConstraints(self):  # pragma: no cover
        return AggregationConstraint.make_many(self.boto3_raw_data["outputConstraints"])

    joinRequired = field("joinRequired")
    allowedJoinOperators = field("allowedJoinOperators")
    additionalAnalyses = field("additionalAnalyses")
    allowedResultReceivers = field("allowedResultReceivers")
    allowedAdditionalAnalyses = field("allowedAdditionalAnalyses")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ConsolidatedPolicyAggregationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConsolidatedPolicyAggregationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisTemplateArtifactMetadata:
    boto3_raw_data: "type_defs.AnalysisTemplateArtifactMetadataTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def entryPointHash(self):  # pragma: no cover
        return Hash.make_one(self.boto3_raw_data["entryPointHash"])

    @cached_property
    def additionalArtifactHashes(self):  # pragma: no cover
        return Hash.make_many(self.boto3_raw_data["additionalArtifactHashes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AnalysisTemplateArtifactMetadataTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisTemplateArtifactMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisTemplateArtifact:
    boto3_raw_data: "type_defs.AnalysisTemplateArtifactTypeDef" = dataclasses.field()

    @cached_property
    def location(self):  # pragma: no cover
        return S3Location.make_one(self.boto3_raw_data["location"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalysisTemplateArtifactTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisTemplateArtifactTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisTemplateValidationStatusDetail:
    boto3_raw_data: "type_defs.AnalysisTemplateValidationStatusDetailTypeDef" = (
        dataclasses.field()
    )

    type = field("type")
    status = field("status")

    @cached_property
    def reasons(self):  # pragma: no cover
        return AnalysisTemplateValidationStatusReason.make_many(
            self.boto3_raw_data["reasons"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AnalysisTemplateValidationStatusDetailTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisTemplateValidationStatusDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnalysisTemplatesOutput:
    boto3_raw_data: "type_defs.ListAnalysisTemplatesOutputTypeDef" = dataclasses.field()

    @cached_property
    def analysisTemplateSummaries(self):  # pragma: no cover
        return AnalysisTemplateSummary.make_many(
            self.boto3_raw_data["analysisTemplateSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAnalysisTemplatesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnalysisTemplatesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTagsForResourceOutput:
    boto3_raw_data: "type_defs.ListTagsForResourceOutputTypeDef" = dataclasses.field()

    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTagsForResourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTagsForResourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PopulateIdMappingTableOutput:
    boto3_raw_data: "type_defs.PopulateIdMappingTableOutputTypeDef" = (
        dataclasses.field()
    )

    idMappingJobId = field("idMappingJobId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PopulateIdMappingTableOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PopulateIdMappingTableOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetSchemaAnalysisRuleInput:
    boto3_raw_data: "type_defs.BatchGetSchemaAnalysisRuleInputTypeDef" = (
        dataclasses.field()
    )

    collaborationIdentifier = field("collaborationIdentifier")

    @cached_property
    def schemaAnalysisRuleRequests(self):  # pragma: no cover
        return SchemaAnalysisRuleRequest.make_many(
            self.boto3_raw_data["schemaAnalysisRuleRequests"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetSchemaAnalysisRuleInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetSchemaAnalysisRuleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedJobStatistics:
    boto3_raw_data: "type_defs.ProtectedJobStatisticsTypeDef" = dataclasses.field()

    totalDurationInMillis = field("totalDurationInMillis")

    @cached_property
    def billedResourceUtilization(self):  # pragma: no cover
        return BilledJobResourceUtilization.make_one(
            self.boto3_raw_data["billedResourceUtilization"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProtectedJobStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedJobStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedQueryStatistics:
    boto3_raw_data: "type_defs.ProtectedQueryStatisticsTypeDef" = dataclasses.field()

    totalDurationInMillis = field("totalDurationInMillis")

    @cached_property
    def billedResourceUtilization(self):  # pragma: no cover
        return BilledResourceUtilization.make_one(
            self.boto3_raw_data["billedResourceUtilization"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProtectedQueryStatisticsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedQueryStatisticsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeSpecificationOutput:
    boto3_raw_data: "type_defs.ChangeSpecificationOutputTypeDef" = dataclasses.field()

    @cached_property
    def member(self):  # pragma: no cover
        return MemberChangeSpecificationOutput.make_one(self.boto3_raw_data["member"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChangeSpecificationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChangeSpecificationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationAnalysisTemplatesOutput:
    boto3_raw_data: "type_defs.ListCollaborationAnalysisTemplatesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def collaborationAnalysisTemplateSummaries(self):  # pragma: no cover
        return CollaborationAnalysisTemplateSummary.make_many(
            self.boto3_raw_data["collaborationAnalysisTemplateSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationAnalysisTemplatesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollaborationAnalysisTemplatesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationConfiguredAudienceModelAssociationsOutput:
    boto3_raw_data: (
        "type_defs.ListCollaborationConfiguredAudienceModelAssociationsOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def collaborationConfiguredAudienceModelAssociationSummaries(
        self,
    ):  # pragma: no cover
        return CollaborationConfiguredAudienceModelAssociationSummary.make_many(
            self.boto3_raw_data[
                "collaborationConfiguredAudienceModelAssociationSummaries"
            ]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationConfiguredAudienceModelAssociationsOutputTypeDef"
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
                "type_defs.ListCollaborationConfiguredAudienceModelAssociationsOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCollaborationConfiguredAudienceModelAssociationOutput:
    boto3_raw_data: (
        "type_defs.GetCollaborationConfiguredAudienceModelAssociationOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def collaborationConfiguredAudienceModelAssociation(self):  # pragma: no cover
        return CollaborationConfiguredAudienceModelAssociation.make_one(
            self.boto3_raw_data["collaborationConfiguredAudienceModelAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCollaborationConfiguredAudienceModelAssociationOutputTypeDef"
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
                "type_defs.GetCollaborationConfiguredAudienceModelAssociationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollaborationIdNamespaceAssociationSummary:
    boto3_raw_data: "type_defs.CollaborationIdNamespaceAssociationSummaryTypeDef" = (
        dataclasses.field()
    )

    arn = field("arn")
    createTime = field("createTime")
    id = field("id")
    updateTime = field("updateTime")
    collaborationArn = field("collaborationArn")
    collaborationId = field("collaborationId")
    creatorAccountId = field("creatorAccountId")

    @cached_property
    def inputReferenceConfig(self):  # pragma: no cover
        return IdNamespaceAssociationInputReferenceConfig.make_one(
            self.boto3_raw_data["inputReferenceConfig"]
        )

    name = field("name")

    @cached_property
    def inputReferenceProperties(self):  # pragma: no cover
        return IdNamespaceAssociationInputReferencePropertiesSummary.make_one(
            self.boto3_raw_data["inputReferenceProperties"]
        )

    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CollaborationIdNamespaceAssociationSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollaborationIdNamespaceAssociationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdNamespaceAssociationSummary:
    boto3_raw_data: "type_defs.IdNamespaceAssociationSummaryTypeDef" = (
        dataclasses.field()
    )

    membershipId = field("membershipId")
    membershipArn = field("membershipArn")
    collaborationArn = field("collaborationArn")
    collaborationId = field("collaborationId")
    createTime = field("createTime")
    updateTime = field("updateTime")
    id = field("id")
    arn = field("arn")

    @cached_property
    def inputReferenceConfig(self):  # pragma: no cover
        return IdNamespaceAssociationInputReferenceConfig.make_one(
            self.boto3_raw_data["inputReferenceConfig"]
        )

    name = field("name")

    @cached_property
    def inputReferenceProperties(self):  # pragma: no cover
        return IdNamespaceAssociationInputReferencePropertiesSummary.make_one(
            self.boto3_raw_data["inputReferenceProperties"]
        )

    description = field("description")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.IdNamespaceAssociationSummaryTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdNamespaceAssociationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIdNamespaceAssociationInput:
    boto3_raw_data: "type_defs.CreateIdNamespaceAssociationInputTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")

    @cached_property
    def inputReferenceConfig(self):  # pragma: no cover
        return IdNamespaceAssociationInputReferenceConfig.make_one(
            self.boto3_raw_data["inputReferenceConfig"]
        )

    name = field("name")
    tags = field("tags")
    description = field("description")

    @cached_property
    def idMappingConfig(self):  # pragma: no cover
        return IdMappingConfig.make_one(self.boto3_raw_data["idMappingConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateIdNamespaceAssociationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIdNamespaceAssociationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIdNamespaceAssociationInput:
    boto3_raw_data: "type_defs.UpdateIdNamespaceAssociationInputTypeDef" = (
        dataclasses.field()
    )

    idNamespaceAssociationIdentifier = field("idNamespaceAssociationIdentifier")
    membershipIdentifier = field("membershipIdentifier")
    name = field("name")
    description = field("description")

    @cached_property
    def idMappingConfig(self):  # pragma: no cover
        return IdMappingConfig.make_one(self.boto3_raw_data["idMappingConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateIdNamespaceAssociationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIdNamespaceAssociationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollaborationIdNamespaceAssociation:
    boto3_raw_data: "type_defs.CollaborationIdNamespaceAssociationTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    arn = field("arn")
    collaborationId = field("collaborationId")
    collaborationArn = field("collaborationArn")
    name = field("name")
    creatorAccountId = field("creatorAccountId")
    createTime = field("createTime")
    updateTime = field("updateTime")

    @cached_property
    def inputReferenceConfig(self):  # pragma: no cover
        return IdNamespaceAssociationInputReferenceConfig.make_one(
            self.boto3_raw_data["inputReferenceConfig"]
        )

    @cached_property
    def inputReferenceProperties(self):  # pragma: no cover
        return IdNamespaceAssociationInputReferenceProperties.make_one(
            self.boto3_raw_data["inputReferenceProperties"]
        )

    description = field("description")

    @cached_property
    def idMappingConfig(self):  # pragma: no cover
        return IdMappingConfig.make_one(self.boto3_raw_data["idMappingConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CollaborationIdNamespaceAssociationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollaborationIdNamespaceAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdNamespaceAssociation:
    boto3_raw_data: "type_defs.IdNamespaceAssociationTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    membershipId = field("membershipId")
    membershipArn = field("membershipArn")
    collaborationId = field("collaborationId")
    collaborationArn = field("collaborationArn")
    name = field("name")
    createTime = field("createTime")
    updateTime = field("updateTime")

    @cached_property
    def inputReferenceConfig(self):  # pragma: no cover
        return IdNamespaceAssociationInputReferenceConfig.make_one(
            self.boto3_raw_data["inputReferenceConfig"]
        )

    @cached_property
    def inputReferenceProperties(self):  # pragma: no cover
        return IdNamespaceAssociationInputReferenceProperties.make_one(
            self.boto3_raw_data["inputReferenceProperties"]
        )

    description = field("description")

    @cached_property
    def idMappingConfig(self):  # pragma: no cover
        return IdMappingConfig.make_one(self.boto3_raw_data["idMappingConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdNamespaceAssociationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdNamespaceAssociationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationPrivacyBudgetTemplatesOutput:
    boto3_raw_data: "type_defs.ListCollaborationPrivacyBudgetTemplatesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def collaborationPrivacyBudgetTemplateSummaries(self):  # pragma: no cover
        return CollaborationPrivacyBudgetTemplateSummary.make_many(
            self.boto3_raw_data["collaborationPrivacyBudgetTemplateSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationPrivacyBudgetTemplatesOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollaborationPrivacyBudgetTemplatesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationsOutput:
    boto3_raw_data: "type_defs.ListCollaborationsOutputTypeDef" = dataclasses.field()

    @cached_property
    def collaborationList(self):  # pragma: no cover
        return CollaborationSummary.make_many(self.boto3_raw_data["collaborationList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCollaborationsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollaborationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Collaboration:
    boto3_raw_data: "type_defs.CollaborationTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    name = field("name")
    creatorAccountId = field("creatorAccountId")
    creatorDisplayName = field("creatorDisplayName")
    createTime = field("createTime")
    updateTime = field("updateTime")
    memberStatus = field("memberStatus")
    queryLogStatus = field("queryLogStatus")
    description = field("description")
    membershipId = field("membershipId")
    membershipArn = field("membershipArn")

    @cached_property
    def dataEncryptionMetadata(self):  # pragma: no cover
        return DataEncryptionMetadata.make_one(
            self.boto3_raw_data["dataEncryptionMetadata"]
        )

    jobLogStatus = field("jobLogStatus")
    analyticsEngine = field("analyticsEngine")
    autoApprovedChangeTypes = field("autoApprovedChangeTypes")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CollaborationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CollaborationTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ComputeConfiguration:
    boto3_raw_data: "type_defs.ComputeConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def worker(self):  # pragma: no cover
        return WorkerComputeConfiguration.make_one(self.boto3_raw_data["worker"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ComputeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ComputeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfigurationDetails:
    boto3_raw_data: "type_defs.ConfigurationDetailsTypeDef" = dataclasses.field()

    @cached_property
    def directAnalysisConfigurationDetails(self):  # pragma: no cover
        return DirectAnalysisConfigurationDetails.make_one(
            self.boto3_raw_data["directAnalysisConfigurationDetails"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfigurationDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfigurationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfiguredAudienceModelAssociationsOutput:
    boto3_raw_data: "type_defs.ListConfiguredAudienceModelAssociationsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def configuredAudienceModelAssociationSummaries(self):  # pragma: no cover
        return ConfiguredAudienceModelAssociationSummary.make_many(
            self.boto3_raw_data["configuredAudienceModelAssociationSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfiguredAudienceModelAssociationsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfiguredAudienceModelAssociationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfiguredAudienceModelAssociationOutput:
    boto3_raw_data: (
        "type_defs.CreateConfiguredAudienceModelAssociationOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def configuredAudienceModelAssociation(self):  # pragma: no cover
        return ConfiguredAudienceModelAssociation.make_one(
            self.boto3_raw_data["configuredAudienceModelAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConfiguredAudienceModelAssociationOutputTypeDef"
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
                "type_defs.CreateConfiguredAudienceModelAssociationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfiguredAudienceModelAssociationOutput:
    boto3_raw_data: "type_defs.GetConfiguredAudienceModelAssociationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def configuredAudienceModelAssociation(self):  # pragma: no cover
        return ConfiguredAudienceModelAssociation.make_one(
            self.boto3_raw_data["configuredAudienceModelAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConfiguredAudienceModelAssociationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfiguredAudienceModelAssociationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConfiguredAudienceModelAssociationOutput:
    boto3_raw_data: (
        "type_defs.UpdateConfiguredAudienceModelAssociationOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def configuredAudienceModelAssociation(self):  # pragma: no cover
        return ConfiguredAudienceModelAssociation.make_one(
            self.boto3_raw_data["configuredAudienceModelAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConfiguredAudienceModelAssociationOutputTypeDef"
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
                "type_defs.UpdateConfiguredAudienceModelAssociationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredTableAssociationAnalysisRulePolicyV1Output:
    boto3_raw_data: (
        "type_defs.ConfiguredTableAssociationAnalysisRulePolicyV1OutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def list(self):  # pragma: no cover
        return ConfiguredTableAssociationAnalysisRuleListOutput.make_one(
            self.boto3_raw_data["list"]
        )

    @cached_property
    def aggregation(self):  # pragma: no cover
        return ConfiguredTableAssociationAnalysisRuleAggregationOutput.make_one(
            self.boto3_raw_data["aggregation"]
        )

    @cached_property
    def custom(self):  # pragma: no cover
        return ConfiguredTableAssociationAnalysisRuleCustomOutput.make_one(
            self.boto3_raw_data["custom"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfiguredTableAssociationAnalysisRulePolicyV1OutputTypeDef"
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
                "type_defs.ConfiguredTableAssociationAnalysisRulePolicyV1OutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredTableAssociationAnalysisRulePolicyV1:
    boto3_raw_data: (
        "type_defs.ConfiguredTableAssociationAnalysisRulePolicyV1TypeDef"
    ) = dataclasses.field()

    @cached_property
    def list(self):  # pragma: no cover
        return ConfiguredTableAssociationAnalysisRuleList.make_one(
            self.boto3_raw_data["list"]
        )

    @cached_property
    def aggregation(self):  # pragma: no cover
        return ConfiguredTableAssociationAnalysisRuleAggregation.make_one(
            self.boto3_raw_data["aggregation"]
        )

    @cached_property
    def custom(self):  # pragma: no cover
        return ConfiguredTableAssociationAnalysisRuleCustom.make_one(
            self.boto3_raw_data["custom"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfiguredTableAssociationAnalysisRulePolicyV1TypeDef"
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
                "type_defs.ConfiguredTableAssociationAnalysisRulePolicyV1TypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfiguredTableAssociationsOutput:
    boto3_raw_data: "type_defs.ListConfiguredTableAssociationsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def configuredTableAssociationSummaries(self):  # pragma: no cover
        return ConfiguredTableAssociationSummary.make_many(
            self.boto3_raw_data["configuredTableAssociationSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfiguredTableAssociationsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfiguredTableAssociationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfiguredTableAssociationOutput:
    boto3_raw_data: "type_defs.CreateConfiguredTableAssociationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def configuredTableAssociation(self):  # pragma: no cover
        return ConfiguredTableAssociation.make_one(
            self.boto3_raw_data["configuredTableAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConfiguredTableAssociationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConfiguredTableAssociationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfiguredTableAssociationOutput:
    boto3_raw_data: "type_defs.GetConfiguredTableAssociationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def configuredTableAssociation(self):  # pragma: no cover
        return ConfiguredTableAssociation.make_one(
            self.boto3_raw_data["configuredTableAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConfiguredTableAssociationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfiguredTableAssociationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConfiguredTableAssociationOutput:
    boto3_raw_data: "type_defs.UpdateConfiguredTableAssociationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def configuredTableAssociation(self):  # pragma: no cover
        return ConfiguredTableAssociation.make_one(
            self.boto3_raw_data["configuredTableAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConfiguredTableAssociationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConfiguredTableAssociationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfiguredTablesOutput:
    boto3_raw_data: "type_defs.ListConfiguredTablesOutputTypeDef" = dataclasses.field()

    @cached_property
    def configuredTableSummaries(self):  # pragma: no cover
        return ConfiguredTableSummary.make_many(
            self.boto3_raw_data["configuredTableSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListConfiguredTablesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfiguredTablesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIdMappingTableInput:
    boto3_raw_data: "type_defs.CreateIdMappingTableInputTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    name = field("name")

    @cached_property
    def inputReferenceConfig(self):  # pragma: no cover
        return IdMappingTableInputReferenceConfig.make_one(
            self.boto3_raw_data["inputReferenceConfig"]
        )

    description = field("description")
    tags = field("tags")
    kmsKeyArn = field("kmsKeyArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIdMappingTableInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIdMappingTableInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdMappingTableSummary:
    boto3_raw_data: "type_defs.IdMappingTableSummaryTypeDef" = dataclasses.field()

    collaborationArn = field("collaborationArn")
    collaborationId = field("collaborationId")
    membershipId = field("membershipId")
    membershipArn = field("membershipArn")
    createTime = field("createTime")
    updateTime = field("updateTime")
    id = field("id")
    arn = field("arn")

    @cached_property
    def inputReferenceConfig(self):  # pragma: no cover
        return IdMappingTableInputReferenceConfig.make_one(
            self.boto3_raw_data["inputReferenceConfig"]
        )

    name = field("name")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IdMappingTableSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdMappingTableSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DifferentialPrivacyConfigurationOutput:
    boto3_raw_data: "type_defs.DifferentialPrivacyConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def columns(self):  # pragma: no cover
        return DifferentialPrivacyColumn.make_many(self.boto3_raw_data["columns"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DifferentialPrivacyConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DifferentialPrivacyConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DifferentialPrivacyConfiguration:
    boto3_raw_data: "type_defs.DifferentialPrivacyConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def columns(self):  # pragma: no cover
        return DifferentialPrivacyColumn.make_many(self.boto3_raw_data["columns"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DifferentialPrivacyConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DifferentialPrivacyConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DifferentialPrivacyParameters:
    boto3_raw_data: "type_defs.DifferentialPrivacyParametersTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def sensitivityParameters(self):  # pragma: no cover
        return DifferentialPrivacySensitivityParameters.make_many(
            self.boto3_raw_data["sensitivityParameters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DifferentialPrivacyParametersTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DifferentialPrivacyParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DifferentialPrivacyPrivacyImpact:
    boto3_raw_data: "type_defs.DifferentialPrivacyPrivacyImpactTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def aggregations(self):  # pragma: no cover
        return DifferentialPrivacyPreviewAggregation.make_many(
            self.boto3_raw_data["aggregations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DifferentialPrivacyPrivacyImpactTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DifferentialPrivacyPrivacyImpactTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PreviewPrivacyImpactParametersInput:
    boto3_raw_data: "type_defs.PreviewPrivacyImpactParametersInputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def differentialPrivacy(self):  # pragma: no cover
        return DifferentialPrivacyPreviewParametersInput.make_one(
            self.boto3_raw_data["differentialPrivacy"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PreviewPrivacyImpactParametersInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PreviewPrivacyImpactParametersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DifferentialPrivacyPrivacyBudget:
    boto3_raw_data: "type_defs.DifferentialPrivacyPrivacyBudgetTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def aggregations(self):  # pragma: no cover
        return DifferentialPrivacyPrivacyBudgetAggregation.make_many(
            self.boto3_raw_data["aggregations"]
        )

    epsilon = field("epsilon")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DifferentialPrivacyPrivacyBudgetTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DifferentialPrivacyPrivacyBudgetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivacyBudgetTemplateParametersInput:
    boto3_raw_data: "type_defs.PrivacyBudgetTemplateParametersInputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def differentialPrivacy(self):  # pragma: no cover
        return DifferentialPrivacyTemplateParametersInput.make_one(
            self.boto3_raw_data["differentialPrivacy"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PrivacyBudgetTemplateParametersInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivacyBudgetTemplateParametersInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivacyBudgetTemplateParametersOutput:
    boto3_raw_data: "type_defs.PrivacyBudgetTemplateParametersOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def differentialPrivacy(self):  # pragma: no cover
        return DifferentialPrivacyTemplateParametersOutput.make_one(
            self.boto3_raw_data["differentialPrivacy"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PrivacyBudgetTemplateParametersOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivacyBudgetTemplateParametersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivacyBudgetTemplateUpdateParameters:
    boto3_raw_data: "type_defs.PrivacyBudgetTemplateUpdateParametersTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def differentialPrivacy(self):  # pragma: no cover
        return DifferentialPrivacyTemplateUpdateParameters.make_one(
            self.boto3_raw_data["differentialPrivacy"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.PrivacyBudgetTemplateUpdateParametersTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivacyBudgetTemplateUpdateParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdMappingTableInputReferenceProperties:
    boto3_raw_data: "type_defs.IdMappingTableInputReferencePropertiesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def idMappingTableInputSource(self):  # pragma: no cover
        return IdMappingTableInputSource.make_many(
            self.boto3_raw_data["idMappingTableInputSource"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IdMappingTableInputReferencePropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdMappingTableInputReferencePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdMappingTableSchemaTypeProperties:
    boto3_raw_data: "type_defs.IdMappingTableSchemaTypePropertiesTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def idMappingTableInputSource(self):  # pragma: no cover
        return IdMappingTableInputSource.make_many(
            self.boto3_raw_data["idMappingTableInputSource"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.IdMappingTableSchemaTypePropertiesTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IdMappingTableSchemaTypePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAnalysisTemplatesInputPaginate:
    boto3_raw_data: "type_defs.ListAnalysisTemplatesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAnalysisTemplatesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAnalysisTemplatesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationAnalysisTemplatesInputPaginate:
    boto3_raw_data: (
        "type_defs.ListCollaborationAnalysisTemplatesInputPaginateTypeDef"
    ) = dataclasses.field()

    collaborationIdentifier = field("collaborationIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationAnalysisTemplatesInputPaginateTypeDef"
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
                "type_defs.ListCollaborationAnalysisTemplatesInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationChangeRequestsInputPaginate:
    boto3_raw_data: "type_defs.ListCollaborationChangeRequestsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    collaborationIdentifier = field("collaborationIdentifier")
    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationChangeRequestsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollaborationChangeRequestsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationConfiguredAudienceModelAssociationsInputPaginate:
    boto3_raw_data: "type_defs.ListCollaborationConfiguredAudienceModelAssociationsInputPaginateTypeDef" = (dataclasses.field())

    collaborationIdentifier = field("collaborationIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationConfiguredAudienceModelAssociationsInputPaginateTypeDef"
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
                "type_defs.ListCollaborationConfiguredAudienceModelAssociationsInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationIdNamespaceAssociationsInputPaginate:
    boto3_raw_data: (
        "type_defs.ListCollaborationIdNamespaceAssociationsInputPaginateTypeDef"
    ) = dataclasses.field()

    collaborationIdentifier = field("collaborationIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationIdNamespaceAssociationsInputPaginateTypeDef"
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
                "type_defs.ListCollaborationIdNamespaceAssociationsInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationPrivacyBudgetTemplatesInputPaginate:
    boto3_raw_data: (
        "type_defs.ListCollaborationPrivacyBudgetTemplatesInputPaginateTypeDef"
    ) = dataclasses.field()

    collaborationIdentifier = field("collaborationIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationPrivacyBudgetTemplatesInputPaginateTypeDef"
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
                "type_defs.ListCollaborationPrivacyBudgetTemplatesInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationPrivacyBudgetsInputPaginate:
    boto3_raw_data: "type_defs.ListCollaborationPrivacyBudgetsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    collaborationIdentifier = field("collaborationIdentifier")
    privacyBudgetType = field("privacyBudgetType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationPrivacyBudgetsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollaborationPrivacyBudgetsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationsInputPaginate:
    boto3_raw_data: "type_defs.ListCollaborationsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    memberStatus = field("memberStatus")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListCollaborationsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollaborationsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfiguredAudienceModelAssociationsInputPaginate:
    boto3_raw_data: (
        "type_defs.ListConfiguredAudienceModelAssociationsInputPaginateTypeDef"
    ) = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfiguredAudienceModelAssociationsInputPaginateTypeDef"
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
                "type_defs.ListConfiguredAudienceModelAssociationsInputPaginateTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfiguredTableAssociationsInputPaginate:
    boto3_raw_data: "type_defs.ListConfiguredTableAssociationsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfiguredTableAssociationsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfiguredTableAssociationsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListConfiguredTablesInputPaginate:
    boto3_raw_data: "type_defs.ListConfiguredTablesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListConfiguredTablesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListConfiguredTablesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdMappingTablesInputPaginate:
    boto3_raw_data: "type_defs.ListIdMappingTablesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListIdMappingTablesInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdMappingTablesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdNamespaceAssociationsInputPaginate:
    boto3_raw_data: "type_defs.ListIdNamespaceAssociationsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListIdNamespaceAssociationsInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdNamespaceAssociationsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMembersInputPaginate:
    boto3_raw_data: "type_defs.ListMembersInputPaginateTypeDef" = dataclasses.field()

    collaborationIdentifier = field("collaborationIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMembersInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMembersInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMembershipsInputPaginate:
    boto3_raw_data: "type_defs.ListMembershipsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMembershipsInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMembershipsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPrivacyBudgetTemplatesInputPaginate:
    boto3_raw_data: "type_defs.ListPrivacyBudgetTemplatesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListPrivacyBudgetTemplatesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPrivacyBudgetTemplatesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPrivacyBudgetsInputPaginate:
    boto3_raw_data: "type_defs.ListPrivacyBudgetsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")
    privacyBudgetType = field("privacyBudgetType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPrivacyBudgetsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPrivacyBudgetsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProtectedJobsInputPaginate:
    boto3_raw_data: "type_defs.ListProtectedJobsInputPaginateTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")
    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListProtectedJobsInputPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProtectedJobsInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProtectedQueriesInputPaginate:
    boto3_raw_data: "type_defs.ListProtectedQueriesInputPaginateTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")
    status = field("status")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListProtectedQueriesInputPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProtectedQueriesInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSchemasInputPaginate:
    boto3_raw_data: "type_defs.ListSchemasInputPaginateTypeDef" = dataclasses.field()

    collaborationIdentifier = field("collaborationIdentifier")
    schemaType = field("schemaType")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListSchemasInputPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSchemasInputPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPrivacyBudgetTemplatesOutput:
    boto3_raw_data: "type_defs.ListPrivacyBudgetTemplatesOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def privacyBudgetTemplateSummaries(self):  # pragma: no cover
        return PrivacyBudgetTemplateSummary.make_many(
            self.boto3_raw_data["privacyBudgetTemplateSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListPrivacyBudgetTemplatesOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPrivacyBudgetTemplatesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListSchemasOutput:
    boto3_raw_data: "type_defs.ListSchemasOutputTypeDef" = dataclasses.field()

    @cached_property
    def schemaSummaries(self):  # pragma: no cover
        return SchemaSummary.make_many(self.boto3_raw_data["schemaSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListSchemasOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListSchemasOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MLPaymentConfig:
    boto3_raw_data: "type_defs.MLPaymentConfigTypeDef" = dataclasses.field()

    @cached_property
    def modelTraining(self):  # pragma: no cover
        return ModelTrainingPaymentConfig.make_one(self.boto3_raw_data["modelTraining"])

    @cached_property
    def modelInference(self):  # pragma: no cover
        return ModelInferencePaymentConfig.make_one(
            self.boto3_raw_data["modelInference"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MLPaymentConfigTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MLPaymentConfigTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MembershipMLPaymentConfig:
    boto3_raw_data: "type_defs.MembershipMLPaymentConfigTypeDef" = dataclasses.field()

    @cached_property
    def modelTraining(self):  # pragma: no cover
        return MembershipModelTrainingPaymentConfig.make_one(
            self.boto3_raw_data["modelTraining"]
        )

    @cached_property
    def modelInference(self):  # pragma: no cover
        return MembershipModelInferencePaymentConfig.make_one(
            self.boto3_raw_data["modelInference"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MembershipMLPaymentConfigTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MembershipMLPaymentConfigTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MembershipProtectedJobOutputConfiguration:
    boto3_raw_data: "type_defs.MembershipProtectedJobOutputConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def s3(self):  # pragma: no cover
        return ProtectedJobS3OutputConfigurationInput.make_one(
            self.boto3_raw_data["s3"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MembershipProtectedJobOutputConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MembershipProtectedJobOutputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MembershipProtectedQueryOutputConfiguration:
    boto3_raw_data: "type_defs.MembershipProtectedQueryOutputConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def s3(self):  # pragma: no cover
        return ProtectedQueryS3OutputConfiguration.make_one(self.boto3_raw_data["s3"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MembershipProtectedQueryOutputConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MembershipProtectedQueryOutputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedJobComputeConfiguration:
    boto3_raw_data: "type_defs.ProtectedJobComputeConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def worker(self):  # pragma: no cover
        return ProtectedJobWorkerComputeConfiguration.make_one(
            self.boto3_raw_data["worker"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProtectedJobComputeConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedJobComputeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedJobConfigurationDetails:
    boto3_raw_data: "type_defs.ProtectedJobConfigurationDetailsTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def directAnalysisConfigurationDetails(self):  # pragma: no cover
        return ProtectedJobDirectAnalysisConfigurationDetails.make_one(
            self.boto3_raw_data["directAnalysisConfigurationDetails"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProtectedJobConfigurationDetailsTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedJobConfigurationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedJobOutputConfigurationInput:
    boto3_raw_data: "type_defs.ProtectedJobOutputConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def member(self):  # pragma: no cover
        return ProtectedJobMemberOutputConfigurationInput.make_one(
            self.boto3_raw_data["member"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectedJobOutputConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedJobOutputConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedJobOutputConfigurationOutput:
    boto3_raw_data: "type_defs.ProtectedJobOutputConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def s3(self):  # pragma: no cover
        return ProtectedJobS3OutputConfigurationOutput.make_one(
            self.boto3_raw_data["s3"]
        )

    @cached_property
    def member(self):  # pragma: no cover
        return ProtectedJobMemberOutputConfigurationOutput.make_one(
            self.boto3_raw_data["member"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectedJobOutputConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedJobOutputConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedJobOutput:
    boto3_raw_data: "type_defs.ProtectedJobOutputTypeDef" = dataclasses.field()

    @cached_property
    def s3(self):  # pragma: no cover
        return ProtectedJobS3Output.make_one(self.boto3_raw_data["s3"])

    @cached_property
    def memberList(self):  # pragma: no cover
        return ProtectedJobSingleMemberOutput.make_many(
            self.boto3_raw_data["memberList"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProtectedJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedQueryDistributeOutputConfigurationLocation:
    boto3_raw_data: (
        "type_defs.ProtectedQueryDistributeOutputConfigurationLocationTypeDef"
    ) = dataclasses.field()

    @cached_property
    def s3(self):  # pragma: no cover
        return ProtectedQueryS3OutputConfiguration.make_one(self.boto3_raw_data["s3"])

    @cached_property
    def member(self):  # pragma: no cover
        return ProtectedQueryMemberOutputConfiguration.make_one(
            self.boto3_raw_data["member"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectedQueryDistributeOutputConfigurationLocationTypeDef"
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
                "type_defs.ProtectedQueryDistributeOutputConfigurationLocationTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedQueryDistributeOutput:
    boto3_raw_data: "type_defs.ProtectedQueryDistributeOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def s3(self):  # pragma: no cover
        return ProtectedQueryS3Output.make_one(self.boto3_raw_data["s3"])

    @cached_property
    def memberList(self):  # pragma: no cover
        return ProtectedQuerySingleMemberOutput.make_many(
            self.boto3_raw_data["memberList"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ProtectedQueryDistributeOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedQueryDistributeOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class QueryConstraint:
    boto3_raw_data: "type_defs.QueryConstraintTypeDef" = dataclasses.field()

    @cached_property
    def requireOverlap(self):  # pragma: no cover
        return QueryConstraintRequireOverlap.make_one(
            self.boto3_raw_data["requireOverlap"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.QueryConstraintTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.QueryConstraintTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaStatusDetail:
    boto3_raw_data: "type_defs.SchemaStatusDetailTypeDef" = dataclasses.field()

    status = field("status")
    analysisType = field("analysisType")

    @cached_property
    def reasons(self):  # pragma: no cover
        return SchemaStatusReason.make_many(self.boto3_raw_data["reasons"])

    analysisRuleType = field("analysisRuleType")
    configurations = field("configurations")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SchemaStatusDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchemaStatusDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnowflakeTableSchemaOutput:
    boto3_raw_data: "type_defs.SnowflakeTableSchemaOutputTypeDef" = dataclasses.field()

    @cached_property
    def v1(self):  # pragma: no cover
        return SnowflakeTableSchemaV1.make_many(self.boto3_raw_data["v1"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SnowflakeTableSchemaOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnowflakeTableSchemaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnowflakeTableSchema:
    boto3_raw_data: "type_defs.SnowflakeTableSchemaTypeDef" = dataclasses.field()

    @cached_property
    def v1(self):  # pragma: no cover
        return SnowflakeTableSchemaV1.make_many(self.boto3_raw_data["v1"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SnowflakeTableSchemaTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnowflakeTableSchemaTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisSourceMetadata:
    boto3_raw_data: "type_defs.AnalysisSourceMetadataTypeDef" = dataclasses.field()

    @cached_property
    def artifacts(self):  # pragma: no cover
        return AnalysisTemplateArtifactMetadata.make_one(
            self.boto3_raw_data["artifacts"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalysisSourceMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisSourceMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisTemplateArtifactsOutput:
    boto3_raw_data: "type_defs.AnalysisTemplateArtifactsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def entryPoint(self):  # pragma: no cover
        return AnalysisTemplateArtifact.make_one(self.boto3_raw_data["entryPoint"])

    roleArn = field("roleArn")

    @cached_property
    def additionalArtifacts(self):  # pragma: no cover
        return AnalysisTemplateArtifact.make_many(
            self.boto3_raw_data["additionalArtifacts"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AnalysisTemplateArtifactsOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisTemplateArtifactsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisTemplateArtifacts:
    boto3_raw_data: "type_defs.AnalysisTemplateArtifactsTypeDef" = dataclasses.field()

    @cached_property
    def entryPoint(self):  # pragma: no cover
        return AnalysisTemplateArtifact.make_one(self.boto3_raw_data["entryPoint"])

    roleArn = field("roleArn")

    @cached_property
    def additionalArtifacts(self):  # pragma: no cover
        return AnalysisTemplateArtifact.make_many(
            self.boto3_raw_data["additionalArtifacts"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalysisTemplateArtifactsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisTemplateArtifactsTypeDef"]
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

    specificationType = field("specificationType")

    @cached_property
    def specification(self):  # pragma: no cover
        return ChangeSpecificationOutput.make_one(self.boto3_raw_data["specification"])

    types = field("types")

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
class ListCollaborationIdNamespaceAssociationsOutput:
    boto3_raw_data: (
        "type_defs.ListCollaborationIdNamespaceAssociationsOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def collaborationIdNamespaceAssociationSummaries(self):  # pragma: no cover
        return CollaborationIdNamespaceAssociationSummary.make_many(
            self.boto3_raw_data["collaborationIdNamespaceAssociationSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationIdNamespaceAssociationsOutputTypeDef"
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
                "type_defs.ListCollaborationIdNamespaceAssociationsOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdNamespaceAssociationsOutput:
    boto3_raw_data: "type_defs.ListIdNamespaceAssociationsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def idNamespaceAssociationSummaries(self):  # pragma: no cover
        return IdNamespaceAssociationSummary.make_many(
            self.boto3_raw_data["idNamespaceAssociationSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListIdNamespaceAssociationsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdNamespaceAssociationsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCollaborationIdNamespaceAssociationOutput:
    boto3_raw_data: "type_defs.GetCollaborationIdNamespaceAssociationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def collaborationIdNamespaceAssociation(self):  # pragma: no cover
        return CollaborationIdNamespaceAssociation.make_one(
            self.boto3_raw_data["collaborationIdNamespaceAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCollaborationIdNamespaceAssociationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCollaborationIdNamespaceAssociationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIdNamespaceAssociationOutput:
    boto3_raw_data: "type_defs.CreateIdNamespaceAssociationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def idNamespaceAssociation(self):  # pragma: no cover
        return IdNamespaceAssociation.make_one(
            self.boto3_raw_data["idNamespaceAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateIdNamespaceAssociationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIdNamespaceAssociationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdNamespaceAssociationOutput:
    boto3_raw_data: "type_defs.GetIdNamespaceAssociationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def idNamespaceAssociation(self):  # pragma: no cover
        return IdNamespaceAssociation.make_one(
            self.boto3_raw_data["idNamespaceAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetIdNamespaceAssociationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdNamespaceAssociationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIdNamespaceAssociationOutput:
    boto3_raw_data: "type_defs.UpdateIdNamespaceAssociationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def idNamespaceAssociation(self):  # pragma: no cover
        return IdNamespaceAssociation.make_one(
            self.boto3_raw_data["idNamespaceAssociation"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateIdNamespaceAssociationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIdNamespaceAssociationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCollaborationOutput:
    boto3_raw_data: "type_defs.CreateCollaborationOutputTypeDef" = dataclasses.field()

    @cached_property
    def collaboration(self):  # pragma: no cover
        return Collaboration.make_one(self.boto3_raw_data["collaboration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCollaborationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCollaborationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCollaborationOutput:
    boto3_raw_data: "type_defs.GetCollaborationOutputTypeDef" = dataclasses.field()

    @cached_property
    def collaboration(self):  # pragma: no cover
        return Collaboration.make_one(self.boto3_raw_data["collaboration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCollaborationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCollaborationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCollaborationOutput:
    boto3_raw_data: "type_defs.UpdateCollaborationOutputTypeDef" = dataclasses.field()

    @cached_property
    def collaboration(self):  # pragma: no cover
        return Collaboration.make_one(self.boto3_raw_data["collaboration"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCollaborationOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCollaborationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ReceiverConfiguration:
    boto3_raw_data: "type_defs.ReceiverConfigurationTypeDef" = dataclasses.field()

    analysisType = field("analysisType")

    @cached_property
    def configurationDetails(self):  # pragma: no cover
        return ConfigurationDetails.make_one(
            self.boto3_raw_data["configurationDetails"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ReceiverConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ReceiverConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredTableAssociationAnalysisRulePolicyOutput:
    boto3_raw_data: (
        "type_defs.ConfiguredTableAssociationAnalysisRulePolicyOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def v1(self):  # pragma: no cover
        return ConfiguredTableAssociationAnalysisRulePolicyV1Output.make_one(
            self.boto3_raw_data["v1"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfiguredTableAssociationAnalysisRulePolicyOutputTypeDef"
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
                "type_defs.ConfiguredTableAssociationAnalysisRulePolicyOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredTableAssociationAnalysisRulePolicy:
    boto3_raw_data: "type_defs.ConfiguredTableAssociationAnalysisRulePolicyTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def v1(self):  # pragma: no cover
        return ConfiguredTableAssociationAnalysisRulePolicyV1.make_one(
            self.boto3_raw_data["v1"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfiguredTableAssociationAnalysisRulePolicyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfiguredTableAssociationAnalysisRulePolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIdMappingTablesOutput:
    boto3_raw_data: "type_defs.ListIdMappingTablesOutputTypeDef" = dataclasses.field()

    @cached_property
    def idMappingTableSummaries(self):  # pragma: no cover
        return IdMappingTableSummary.make_many(
            self.boto3_raw_data["idMappingTableSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIdMappingTablesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIdMappingTablesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisRuleCustomOutput:
    boto3_raw_data: "type_defs.AnalysisRuleCustomOutputTypeDef" = dataclasses.field()

    allowedAnalyses = field("allowedAnalyses")
    allowedAnalysisProviders = field("allowedAnalysisProviders")
    additionalAnalyses = field("additionalAnalyses")
    disallowedOutputColumns = field("disallowedOutputColumns")

    @cached_property
    def differentialPrivacy(self):  # pragma: no cover
        return DifferentialPrivacyConfigurationOutput.make_one(
            self.boto3_raw_data["differentialPrivacy"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalysisRuleCustomOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisRuleCustomOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConsolidatedPolicyCustom:
    boto3_raw_data: "type_defs.ConsolidatedPolicyCustomTypeDef" = dataclasses.field()

    allowedAnalyses = field("allowedAnalyses")
    allowedAnalysisProviders = field("allowedAnalysisProviders")
    additionalAnalyses = field("additionalAnalyses")
    disallowedOutputColumns = field("disallowedOutputColumns")

    @cached_property
    def differentialPrivacy(self):  # pragma: no cover
        return DifferentialPrivacyConfigurationOutput.make_one(
            self.boto3_raw_data["differentialPrivacy"]
        )

    allowedResultReceivers = field("allowedResultReceivers")
    allowedAdditionalAnalyses = field("allowedAdditionalAnalyses")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConsolidatedPolicyCustomTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConsolidatedPolicyCustomTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisRuleCustom:
    boto3_raw_data: "type_defs.AnalysisRuleCustomTypeDef" = dataclasses.field()

    allowedAnalyses = field("allowedAnalyses")
    allowedAnalysisProviders = field("allowedAnalysisProviders")
    additionalAnalyses = field("additionalAnalyses")
    disallowedOutputColumns = field("disallowedOutputColumns")

    @cached_property
    def differentialPrivacy(self):  # pragma: no cover
        return DifferentialPrivacyConfiguration.make_one(
            self.boto3_raw_data["differentialPrivacy"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalysisRuleCustomTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisRuleCustomTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivacyImpact:
    boto3_raw_data: "type_defs.PrivacyImpactTypeDef" = dataclasses.field()

    @cached_property
    def differentialPrivacy(self):  # pragma: no cover
        return DifferentialPrivacyPrivacyImpact.make_one(
            self.boto3_raw_data["differentialPrivacy"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PrivacyImpactTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PrivacyImpactTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PreviewPrivacyImpactInput:
    boto3_raw_data: "type_defs.PreviewPrivacyImpactInputTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")

    @cached_property
    def parameters(self):  # pragma: no cover
        return PreviewPrivacyImpactParametersInput.make_one(
            self.boto3_raw_data["parameters"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PreviewPrivacyImpactInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PreviewPrivacyImpactInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivacyBudget:
    boto3_raw_data: "type_defs.PrivacyBudgetTypeDef" = dataclasses.field()

    @cached_property
    def differentialPrivacy(self):  # pragma: no cover
        return DifferentialPrivacyPrivacyBudget.make_one(
            self.boto3_raw_data["differentialPrivacy"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.PrivacyBudgetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.PrivacyBudgetTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePrivacyBudgetTemplateInput:
    boto3_raw_data: "type_defs.CreatePrivacyBudgetTemplateInputTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")
    autoRefresh = field("autoRefresh")
    privacyBudgetType = field("privacyBudgetType")

    @cached_property
    def parameters(self):  # pragma: no cover
        return PrivacyBudgetTemplateParametersInput.make_one(
            self.boto3_raw_data["parameters"]
        )

    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreatePrivacyBudgetTemplateInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePrivacyBudgetTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollaborationPrivacyBudgetTemplate:
    boto3_raw_data: "type_defs.CollaborationPrivacyBudgetTemplateTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    arn = field("arn")
    collaborationId = field("collaborationId")
    collaborationArn = field("collaborationArn")
    creatorAccountId = field("creatorAccountId")
    createTime = field("createTime")
    updateTime = field("updateTime")
    privacyBudgetType = field("privacyBudgetType")
    autoRefresh = field("autoRefresh")

    @cached_property
    def parameters(self):  # pragma: no cover
        return PrivacyBudgetTemplateParametersOutput.make_one(
            self.boto3_raw_data["parameters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CollaborationPrivacyBudgetTemplateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollaborationPrivacyBudgetTemplateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivacyBudgetTemplate:
    boto3_raw_data: "type_defs.PrivacyBudgetTemplateTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    membershipId = field("membershipId")
    membershipArn = field("membershipArn")
    collaborationId = field("collaborationId")
    collaborationArn = field("collaborationArn")
    createTime = field("createTime")
    updateTime = field("updateTime")
    privacyBudgetType = field("privacyBudgetType")
    autoRefresh = field("autoRefresh")

    @cached_property
    def parameters(self):  # pragma: no cover
        return PrivacyBudgetTemplateParametersOutput.make_one(
            self.boto3_raw_data["parameters"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrivacyBudgetTemplateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivacyBudgetTemplateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePrivacyBudgetTemplateInput:
    boto3_raw_data: "type_defs.UpdatePrivacyBudgetTemplateInputTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")
    privacyBudgetTemplateIdentifier = field("privacyBudgetTemplateIdentifier")
    privacyBudgetType = field("privacyBudgetType")

    @cached_property
    def parameters(self):  # pragma: no cover
        return PrivacyBudgetTemplateUpdateParameters.make_one(
            self.boto3_raw_data["parameters"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdatePrivacyBudgetTemplateInputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePrivacyBudgetTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IdMappingTable:
    boto3_raw_data: "type_defs.IdMappingTableTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")

    @cached_property
    def inputReferenceConfig(self):  # pragma: no cover
        return IdMappingTableInputReferenceConfig.make_one(
            self.boto3_raw_data["inputReferenceConfig"]
        )

    membershipId = field("membershipId")
    membershipArn = field("membershipArn")
    collaborationId = field("collaborationId")
    collaborationArn = field("collaborationArn")
    name = field("name")
    createTime = field("createTime")
    updateTime = field("updateTime")

    @cached_property
    def inputReferenceProperties(self):  # pragma: no cover
        return IdMappingTableInputReferenceProperties.make_one(
            self.boto3_raw_data["inputReferenceProperties"]
        )

    description = field("description")
    kmsKeyArn = field("kmsKeyArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IdMappingTableTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IdMappingTableTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SchemaTypeProperties:
    boto3_raw_data: "type_defs.SchemaTypePropertiesTypeDef" = dataclasses.field()

    @cached_property
    def idMappingTable(self):  # pragma: no cover
        return IdMappingTableSchemaTypeProperties.make_one(
            self.boto3_raw_data["idMappingTable"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SchemaTypePropertiesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SchemaTypePropertiesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PaymentConfiguration:
    boto3_raw_data: "type_defs.PaymentConfigurationTypeDef" = dataclasses.field()

    @cached_property
    def queryCompute(self):  # pragma: no cover
        return QueryComputePaymentConfig.make_one(self.boto3_raw_data["queryCompute"])

    @cached_property
    def machineLearning(self):  # pragma: no cover
        return MLPaymentConfig.make_one(self.boto3_raw_data["machineLearning"])

    @cached_property
    def jobCompute(self):  # pragma: no cover
        return JobComputePaymentConfig.make_one(self.boto3_raw_data["jobCompute"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PaymentConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PaymentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeSpecification:
    boto3_raw_data: "type_defs.ChangeSpecificationTypeDef" = dataclasses.field()

    member = field("member")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ChangeSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ChangeSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MembershipPaymentConfiguration:
    boto3_raw_data: "type_defs.MembershipPaymentConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def queryCompute(self):  # pragma: no cover
        return MembershipQueryComputePaymentConfig.make_one(
            self.boto3_raw_data["queryCompute"]
        )

    @cached_property
    def machineLearning(self):  # pragma: no cover
        return MembershipMLPaymentConfig.make_one(
            self.boto3_raw_data["machineLearning"]
        )

    @cached_property
    def jobCompute(self):  # pragma: no cover
        return MembershipJobComputePaymentConfig.make_one(
            self.boto3_raw_data["jobCompute"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.MembershipPaymentConfigurationTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MembershipPaymentConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MembershipProtectedJobResultConfiguration:
    boto3_raw_data: "type_defs.MembershipProtectedJobResultConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def outputConfiguration(self):  # pragma: no cover
        return MembershipProtectedJobOutputConfiguration.make_one(
            self.boto3_raw_data["outputConfiguration"]
        )

    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MembershipProtectedJobResultConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MembershipProtectedJobResultConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MembershipProtectedQueryResultConfiguration:
    boto3_raw_data: "type_defs.MembershipProtectedQueryResultConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def outputConfiguration(self):  # pragma: no cover
        return MembershipProtectedQueryOutputConfiguration.make_one(
            self.boto3_raw_data["outputConfiguration"]
        )

    roleArn = field("roleArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.MembershipProtectedQueryResultConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MembershipProtectedQueryResultConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedJobReceiverConfiguration:
    boto3_raw_data: "type_defs.ProtectedJobReceiverConfigurationTypeDef" = (
        dataclasses.field()
    )

    analysisType = field("analysisType")

    @cached_property
    def configurationDetails(self):  # pragma: no cover
        return ProtectedJobConfigurationDetails.make_one(
            self.boto3_raw_data["configurationDetails"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectedJobReceiverConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedJobReceiverConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedJobResultConfigurationInput:
    boto3_raw_data: "type_defs.ProtectedJobResultConfigurationInputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def outputConfiguration(self):  # pragma: no cover
        return ProtectedJobOutputConfigurationInput.make_one(
            self.boto3_raw_data["outputConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectedJobResultConfigurationInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedJobResultConfigurationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedJobResultConfigurationOutput:
    boto3_raw_data: "type_defs.ProtectedJobResultConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def outputConfiguration(self):  # pragma: no cover
        return ProtectedJobOutputConfigurationOutput.make_one(
            self.boto3_raw_data["outputConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectedJobResultConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedJobResultConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedJobResult:
    boto3_raw_data: "type_defs.ProtectedJobResultTypeDef" = dataclasses.field()

    @cached_property
    def output(self):  # pragma: no cover
        return ProtectedJobOutput.make_one(self.boto3_raw_data["output"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProtectedJobResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedJobResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedQueryDistributeOutputConfigurationOutput:
    boto3_raw_data: (
        "type_defs.ProtectedQueryDistributeOutputConfigurationOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def locations(self):  # pragma: no cover
        return ProtectedQueryDistributeOutputConfigurationLocation.make_many(
            self.boto3_raw_data["locations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectedQueryDistributeOutputConfigurationOutputTypeDef"
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
                "type_defs.ProtectedQueryDistributeOutputConfigurationOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedQueryDistributeOutputConfiguration:
    boto3_raw_data: "type_defs.ProtectedQueryDistributeOutputConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def locations(self):  # pragma: no cover
        return ProtectedQueryDistributeOutputConfigurationLocation.make_many(
            self.boto3_raw_data["locations"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectedQueryDistributeOutputConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedQueryDistributeOutputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedQueryOutput:
    boto3_raw_data: "type_defs.ProtectedQueryOutputTypeDef" = dataclasses.field()

    @cached_property
    def s3(self):  # pragma: no cover
        return ProtectedQueryS3Output.make_one(self.boto3_raw_data["s3"])

    @cached_property
    def memberList(self):  # pragma: no cover
        return ProtectedQuerySingleMemberOutput.make_many(
            self.boto3_raw_data["memberList"]
        )

    @cached_property
    def distribute(self):  # pragma: no cover
        return ProtectedQueryDistributeOutput.make_one(
            self.boto3_raw_data["distribute"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProtectedQueryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedQueryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisRuleIdMappingTable:
    boto3_raw_data: "type_defs.AnalysisRuleIdMappingTableTypeDef" = dataclasses.field()

    joinColumns = field("joinColumns")

    @cached_property
    def queryConstraints(self):  # pragma: no cover
        return QueryConstraint.make_many(self.boto3_raw_data["queryConstraints"])

    dimensionColumns = field("dimensionColumns")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalysisRuleIdMappingTableTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisRuleIdMappingTableTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnowflakeTableReferenceOutput:
    boto3_raw_data: "type_defs.SnowflakeTableReferenceOutputTypeDef" = (
        dataclasses.field()
    )

    secretArn = field("secretArn")
    accountIdentifier = field("accountIdentifier")
    databaseName = field("databaseName")
    tableName = field("tableName")
    schemaName = field("schemaName")

    @cached_property
    def tableSchema(self):  # pragma: no cover
        return SnowflakeTableSchemaOutput.make_one(self.boto3_raw_data["tableSchema"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SnowflakeTableReferenceOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnowflakeTableReferenceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SnowflakeTableReference:
    boto3_raw_data: "type_defs.SnowflakeTableReferenceTypeDef" = dataclasses.field()

    secretArn = field("secretArn")
    accountIdentifier = field("accountIdentifier")
    databaseName = field("databaseName")
    tableName = field("tableName")
    schemaName = field("schemaName")

    @cached_property
    def tableSchema(self):  # pragma: no cover
        return SnowflakeTableSchema.make_one(self.boto3_raw_data["tableSchema"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SnowflakeTableReferenceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SnowflakeTableReferenceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisSourceOutput:
    boto3_raw_data: "type_defs.AnalysisSourceOutputTypeDef" = dataclasses.field()

    text = field("text")

    @cached_property
    def artifacts(self):  # pragma: no cover
        return AnalysisTemplateArtifactsOutput.make_one(
            self.boto3_raw_data["artifacts"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalysisSourceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisSourceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisSource:
    boto3_raw_data: "type_defs.AnalysisSourceTypeDef" = dataclasses.field()

    text = field("text")

    @cached_property
    def artifacts(self):  # pragma: no cover
        return AnalysisTemplateArtifacts.make_one(self.boto3_raw_data["artifacts"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnalysisSourceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnalysisSourceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollaborationChangeRequestSummary:
    boto3_raw_data: "type_defs.CollaborationChangeRequestSummaryTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    collaborationId = field("collaborationId")
    createTime = field("createTime")
    updateTime = field("updateTime")
    status = field("status")
    isAutoApproved = field("isAutoApproved")

    @cached_property
    def changes(self):  # pragma: no cover
        return Change.make_many(self.boto3_raw_data["changes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CollaborationChangeRequestSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollaborationChangeRequestSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollaborationChangeRequest:
    boto3_raw_data: "type_defs.CollaborationChangeRequestTypeDef" = dataclasses.field()

    id = field("id")
    collaborationId = field("collaborationId")
    createTime = field("createTime")
    updateTime = field("updateTime")
    status = field("status")
    isAutoApproved = field("isAutoApproved")

    @cached_property
    def changes(self):  # pragma: no cover
        return Change.make_many(self.boto3_raw_data["changes"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CollaborationChangeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollaborationChangeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedQuerySummary:
    boto3_raw_data: "type_defs.ProtectedQuerySummaryTypeDef" = dataclasses.field()

    id = field("id")
    membershipId = field("membershipId")
    membershipArn = field("membershipArn")
    createTime = field("createTime")
    status = field("status")

    @cached_property
    def receiverConfigurations(self):  # pragma: no cover
        return ReceiverConfiguration.make_many(
            self.boto3_raw_data["receiverConfigurations"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProtectedQuerySummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedQuerySummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredTableAssociationAnalysisRule:
    boto3_raw_data: "type_defs.ConfiguredTableAssociationAnalysisRuleTypeDef" = (
        dataclasses.field()
    )

    membershipIdentifier = field("membershipIdentifier")
    configuredTableAssociationId = field("configuredTableAssociationId")
    configuredTableAssociationArn = field("configuredTableAssociationArn")

    @cached_property
    def policy(self):  # pragma: no cover
        return ConfiguredTableAssociationAnalysisRulePolicyOutput.make_one(
            self.boto3_raw_data["policy"]
        )

    type = field("type")
    createTime = field("createTime")
    updateTime = field("updateTime")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfiguredTableAssociationAnalysisRuleTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfiguredTableAssociationAnalysisRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredTableAnalysisRulePolicyV1Output:
    boto3_raw_data: "type_defs.ConfiguredTableAnalysisRulePolicyV1OutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def list(self):  # pragma: no cover
        return AnalysisRuleListOutput.make_one(self.boto3_raw_data["list"])

    @cached_property
    def aggregation(self):  # pragma: no cover
        return AnalysisRuleAggregationOutput.make_one(
            self.boto3_raw_data["aggregation"]
        )

    @cached_property
    def custom(self):  # pragma: no cover
        return AnalysisRuleCustomOutput.make_one(self.boto3_raw_data["custom"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfiguredTableAnalysisRulePolicyV1OutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfiguredTableAnalysisRulePolicyV1OutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConsolidatedPolicyV1:
    boto3_raw_data: "type_defs.ConsolidatedPolicyV1TypeDef" = dataclasses.field()

    @cached_property
    def list(self):  # pragma: no cover
        return ConsolidatedPolicyList.make_one(self.boto3_raw_data["list"])

    @cached_property
    def aggregation(self):  # pragma: no cover
        return ConsolidatedPolicyAggregation.make_one(
            self.boto3_raw_data["aggregation"]
        )

    @cached_property
    def custom(self):  # pragma: no cover
        return ConsolidatedPolicyCustom.make_one(self.boto3_raw_data["custom"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConsolidatedPolicyV1TypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConsolidatedPolicyV1TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredTableAnalysisRulePolicyV1:
    boto3_raw_data: "type_defs.ConfiguredTableAnalysisRulePolicyV1TypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def list(self):  # pragma: no cover
        return AnalysisRuleList.make_one(self.boto3_raw_data["list"])

    @cached_property
    def aggregation(self):  # pragma: no cover
        return AnalysisRuleAggregation.make_one(self.boto3_raw_data["aggregation"])

    @cached_property
    def custom(self):  # pragma: no cover
        return AnalysisRuleCustom.make_one(self.boto3_raw_data["custom"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfiguredTableAnalysisRulePolicyV1TypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfiguredTableAnalysisRulePolicyV1TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PreviewPrivacyImpactOutput:
    boto3_raw_data: "type_defs.PreviewPrivacyImpactOutputTypeDef" = dataclasses.field()

    @cached_property
    def privacyImpact(self):  # pragma: no cover
        return PrivacyImpact.make_one(self.boto3_raw_data["privacyImpact"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PreviewPrivacyImpactOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PreviewPrivacyImpactOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollaborationPrivacyBudgetSummary:
    boto3_raw_data: "type_defs.CollaborationPrivacyBudgetSummaryTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    privacyBudgetTemplateId = field("privacyBudgetTemplateId")
    privacyBudgetTemplateArn = field("privacyBudgetTemplateArn")
    collaborationId = field("collaborationId")
    collaborationArn = field("collaborationArn")
    creatorAccountId = field("creatorAccountId")
    type = field("type")
    createTime = field("createTime")
    updateTime = field("updateTime")

    @cached_property
    def budget(self):  # pragma: no cover
        return PrivacyBudget.make_one(self.boto3_raw_data["budget"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CollaborationPrivacyBudgetSummaryTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollaborationPrivacyBudgetSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PrivacyBudgetSummary:
    boto3_raw_data: "type_defs.PrivacyBudgetSummaryTypeDef" = dataclasses.field()

    id = field("id")
    privacyBudgetTemplateId = field("privacyBudgetTemplateId")
    privacyBudgetTemplateArn = field("privacyBudgetTemplateArn")
    membershipId = field("membershipId")
    membershipArn = field("membershipArn")
    collaborationId = field("collaborationId")
    collaborationArn = field("collaborationArn")
    type = field("type")
    createTime = field("createTime")
    updateTime = field("updateTime")

    @cached_property
    def budget(self):  # pragma: no cover
        return PrivacyBudget.make_one(self.boto3_raw_data["budget"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.PrivacyBudgetSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PrivacyBudgetSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCollaborationPrivacyBudgetTemplateOutput:
    boto3_raw_data: "type_defs.GetCollaborationPrivacyBudgetTemplateOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def collaborationPrivacyBudgetTemplate(self):  # pragma: no cover
        return CollaborationPrivacyBudgetTemplate.make_one(
            self.boto3_raw_data["collaborationPrivacyBudgetTemplate"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCollaborationPrivacyBudgetTemplateOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCollaborationPrivacyBudgetTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreatePrivacyBudgetTemplateOutput:
    boto3_raw_data: "type_defs.CreatePrivacyBudgetTemplateOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def privacyBudgetTemplate(self):  # pragma: no cover
        return PrivacyBudgetTemplate.make_one(
            self.boto3_raw_data["privacyBudgetTemplate"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreatePrivacyBudgetTemplateOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreatePrivacyBudgetTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetPrivacyBudgetTemplateOutput:
    boto3_raw_data: "type_defs.GetPrivacyBudgetTemplateOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def privacyBudgetTemplate(self):  # pragma: no cover
        return PrivacyBudgetTemplate.make_one(
            self.boto3_raw_data["privacyBudgetTemplate"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetPrivacyBudgetTemplateOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetPrivacyBudgetTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdatePrivacyBudgetTemplateOutput:
    boto3_raw_data: "type_defs.UpdatePrivacyBudgetTemplateOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def privacyBudgetTemplate(self):  # pragma: no cover
        return PrivacyBudgetTemplate.make_one(
            self.boto3_raw_data["privacyBudgetTemplate"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdatePrivacyBudgetTemplateOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdatePrivacyBudgetTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateIdMappingTableOutput:
    boto3_raw_data: "type_defs.CreateIdMappingTableOutputTypeDef" = dataclasses.field()

    @cached_property
    def idMappingTable(self):  # pragma: no cover
        return IdMappingTable.make_one(self.boto3_raw_data["idMappingTable"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateIdMappingTableOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateIdMappingTableOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetIdMappingTableOutput:
    boto3_raw_data: "type_defs.GetIdMappingTableOutputTypeDef" = dataclasses.field()

    @cached_property
    def idMappingTable(self):  # pragma: no cover
        return IdMappingTable.make_one(self.boto3_raw_data["idMappingTable"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetIdMappingTableOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetIdMappingTableOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateIdMappingTableOutput:
    boto3_raw_data: "type_defs.UpdateIdMappingTableOutputTypeDef" = dataclasses.field()

    @cached_property
    def idMappingTable(self):  # pragma: no cover
        return IdMappingTable.make_one(self.boto3_raw_data["idMappingTable"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateIdMappingTableOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateIdMappingTableOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Schema:
    boto3_raw_data: "type_defs.SchemaTypeDef" = dataclasses.field()

    @cached_property
    def columns(self):  # pragma: no cover
        return Column.make_many(self.boto3_raw_data["columns"])

    @cached_property
    def partitionKeys(self):  # pragma: no cover
        return Column.make_many(self.boto3_raw_data["partitionKeys"])

    analysisRuleTypes = field("analysisRuleTypes")
    creatorAccountId = field("creatorAccountId")
    name = field("name")
    collaborationId = field("collaborationId")
    collaborationArn = field("collaborationArn")
    description = field("description")
    createTime = field("createTime")
    updateTime = field("updateTime")
    type = field("type")

    @cached_property
    def schemaStatusDetails(self):  # pragma: no cover
        return SchemaStatusDetail.make_many(self.boto3_raw_data["schemaStatusDetails"])

    analysisMethod = field("analysisMethod")
    selectedAnalysisMethods = field("selectedAnalysisMethods")

    @cached_property
    def schemaTypeProperties(self):  # pragma: no cover
        return SchemaTypeProperties.make_one(
            self.boto3_raw_data["schemaTypeProperties"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SchemaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SchemaTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberSpecification:
    boto3_raw_data: "type_defs.MemberSpecificationTypeDef" = dataclasses.field()

    accountId = field("accountId")
    memberAbilities = field("memberAbilities")
    displayName = field("displayName")
    mlMemberAbilities = field("mlMemberAbilities")

    @cached_property
    def paymentConfiguration(self):  # pragma: no cover
        return PaymentConfiguration.make_one(
            self.boto3_raw_data["paymentConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MemberSpecificationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MemberSpecificationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberSummary:
    boto3_raw_data: "type_defs.MemberSummaryTypeDef" = dataclasses.field()

    accountId = field("accountId")
    status = field("status")
    displayName = field("displayName")
    abilities = field("abilities")
    createTime = field("createTime")
    updateTime = field("updateTime")

    @cached_property
    def paymentConfiguration(self):  # pragma: no cover
        return PaymentConfiguration.make_one(
            self.boto3_raw_data["paymentConfiguration"]
        )

    @cached_property
    def mlAbilities(self):  # pragma: no cover
        return MLMemberAbilitiesOutput.make_one(self.boto3_raw_data["mlAbilities"])

    membershipId = field("membershipId")
    membershipArn = field("membershipArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MemberSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MemberSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MembershipSummary:
    boto3_raw_data: "type_defs.MembershipSummaryTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    collaborationArn = field("collaborationArn")
    collaborationId = field("collaborationId")
    collaborationCreatorAccountId = field("collaborationCreatorAccountId")
    collaborationCreatorDisplayName = field("collaborationCreatorDisplayName")
    collaborationName = field("collaborationName")
    createTime = field("createTime")
    updateTime = field("updateTime")
    status = field("status")
    memberAbilities = field("memberAbilities")

    @cached_property
    def paymentConfiguration(self):  # pragma: no cover
        return MembershipPaymentConfiguration.make_one(
            self.boto3_raw_data["paymentConfiguration"]
        )

    @cached_property
    def mlMemberAbilities(self):  # pragma: no cover
        return MLMemberAbilitiesOutput.make_one(
            self.boto3_raw_data["mlMemberAbilities"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MembershipSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MembershipSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMembershipInput:
    boto3_raw_data: "type_defs.CreateMembershipInputTypeDef" = dataclasses.field()

    collaborationIdentifier = field("collaborationIdentifier")
    queryLogStatus = field("queryLogStatus")
    jobLogStatus = field("jobLogStatus")
    tags = field("tags")

    @cached_property
    def defaultResultConfiguration(self):  # pragma: no cover
        return MembershipProtectedQueryResultConfiguration.make_one(
            self.boto3_raw_data["defaultResultConfiguration"]
        )

    @cached_property
    def defaultJobResultConfiguration(self):  # pragma: no cover
        return MembershipProtectedJobResultConfiguration.make_one(
            self.boto3_raw_data["defaultJobResultConfiguration"]
        )

    @cached_property
    def paymentConfiguration(self):  # pragma: no cover
        return MembershipPaymentConfiguration.make_one(
            self.boto3_raw_data["paymentConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMembershipInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMembershipInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Membership:
    boto3_raw_data: "type_defs.MembershipTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    collaborationArn = field("collaborationArn")
    collaborationId = field("collaborationId")
    collaborationCreatorAccountId = field("collaborationCreatorAccountId")
    collaborationCreatorDisplayName = field("collaborationCreatorDisplayName")
    collaborationName = field("collaborationName")
    createTime = field("createTime")
    updateTime = field("updateTime")
    status = field("status")
    memberAbilities = field("memberAbilities")
    queryLogStatus = field("queryLogStatus")

    @cached_property
    def paymentConfiguration(self):  # pragma: no cover
        return MembershipPaymentConfiguration.make_one(
            self.boto3_raw_data["paymentConfiguration"]
        )

    @cached_property
    def mlMemberAbilities(self):  # pragma: no cover
        return MLMemberAbilitiesOutput.make_one(
            self.boto3_raw_data["mlMemberAbilities"]
        )

    jobLogStatus = field("jobLogStatus")

    @cached_property
    def defaultResultConfiguration(self):  # pragma: no cover
        return MembershipProtectedQueryResultConfiguration.make_one(
            self.boto3_raw_data["defaultResultConfiguration"]
        )

    @cached_property
    def defaultJobResultConfiguration(self):  # pragma: no cover
        return MembershipProtectedJobResultConfiguration.make_one(
            self.boto3_raw_data["defaultJobResultConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MembershipTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MembershipTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMembershipInput:
    boto3_raw_data: "type_defs.UpdateMembershipInputTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    queryLogStatus = field("queryLogStatus")
    jobLogStatus = field("jobLogStatus")

    @cached_property
    def defaultResultConfiguration(self):  # pragma: no cover
        return MembershipProtectedQueryResultConfiguration.make_one(
            self.boto3_raw_data["defaultResultConfiguration"]
        )

    @cached_property
    def defaultJobResultConfiguration(self):  # pragma: no cover
        return MembershipProtectedJobResultConfiguration.make_one(
            self.boto3_raw_data["defaultJobResultConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMembershipInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMembershipInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedJobSummary:
    boto3_raw_data: "type_defs.ProtectedJobSummaryTypeDef" = dataclasses.field()

    id = field("id")
    membershipId = field("membershipId")
    membershipArn = field("membershipArn")
    createTime = field("createTime")
    status = field("status")

    @cached_property
    def receiverConfigurations(self):  # pragma: no cover
        return ProtectedJobReceiverConfiguration.make_many(
            self.boto3_raw_data["receiverConfigurations"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProtectedJobSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedJobSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartProtectedJobInput:
    boto3_raw_data: "type_defs.StartProtectedJobInputTypeDef" = dataclasses.field()

    type = field("type")
    membershipIdentifier = field("membershipIdentifier")

    @cached_property
    def jobParameters(self):  # pragma: no cover
        return ProtectedJobParameters.make_one(self.boto3_raw_data["jobParameters"])

    @cached_property
    def resultConfiguration(self):  # pragma: no cover
        return ProtectedJobResultConfigurationInput.make_one(
            self.boto3_raw_data["resultConfiguration"]
        )

    @cached_property
    def computeConfiguration(self):  # pragma: no cover
        return ProtectedJobComputeConfiguration.make_one(
            self.boto3_raw_data["computeConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartProtectedJobInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartProtectedJobInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedJob:
    boto3_raw_data: "type_defs.ProtectedJobTypeDef" = dataclasses.field()

    id = field("id")
    membershipId = field("membershipId")
    membershipArn = field("membershipArn")
    createTime = field("createTime")
    status = field("status")

    @cached_property
    def jobParameters(self):  # pragma: no cover
        return ProtectedJobParameters.make_one(self.boto3_raw_data["jobParameters"])

    @cached_property
    def resultConfiguration(self):  # pragma: no cover
        return ProtectedJobResultConfigurationOutput.make_one(
            self.boto3_raw_data["resultConfiguration"]
        )

    @cached_property
    def statistics(self):  # pragma: no cover
        return ProtectedJobStatistics.make_one(self.boto3_raw_data["statistics"])

    @cached_property
    def result(self):  # pragma: no cover
        return ProtectedJobResult.make_one(self.boto3_raw_data["result"])

    @cached_property
    def error(self):  # pragma: no cover
        return ProtectedJobError.make_one(self.boto3_raw_data["error"])

    @cached_property
    def computeConfiguration(self):  # pragma: no cover
        return ProtectedJobComputeConfiguration.make_one(
            self.boto3_raw_data["computeConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProtectedJobTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProtectedJobTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedQueryOutputConfigurationOutput:
    boto3_raw_data: "type_defs.ProtectedQueryOutputConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def s3(self):  # pragma: no cover
        return ProtectedQueryS3OutputConfiguration.make_one(self.boto3_raw_data["s3"])

    @cached_property
    def member(self):  # pragma: no cover
        return ProtectedQueryMemberOutputConfiguration.make_one(
            self.boto3_raw_data["member"]
        )

    @cached_property
    def distribute(self):  # pragma: no cover
        return ProtectedQueryDistributeOutputConfigurationOutput.make_one(
            self.boto3_raw_data["distribute"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectedQueryOutputConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedQueryOutputConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedQueryOutputConfiguration:
    boto3_raw_data: "type_defs.ProtectedQueryOutputConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def s3(self):  # pragma: no cover
        return ProtectedQueryS3OutputConfiguration.make_one(self.boto3_raw_data["s3"])

    @cached_property
    def member(self):  # pragma: no cover
        return ProtectedQueryMemberOutputConfiguration.make_one(
            self.boto3_raw_data["member"]
        )

    @cached_property
    def distribute(self):  # pragma: no cover
        return ProtectedQueryDistributeOutputConfiguration.make_one(
            self.boto3_raw_data["distribute"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectedQueryOutputConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedQueryOutputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedQueryResult:
    boto3_raw_data: "type_defs.ProtectedQueryResultTypeDef" = dataclasses.field()

    @cached_property
    def output(self):  # pragma: no cover
        return ProtectedQueryOutput.make_one(self.boto3_raw_data["output"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ProtectedQueryResultTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedQueryResultTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisRulePolicyV1:
    boto3_raw_data: "type_defs.AnalysisRulePolicyV1TypeDef" = dataclasses.field()

    @cached_property
    def list(self):  # pragma: no cover
        return AnalysisRuleListOutput.make_one(self.boto3_raw_data["list"])

    @cached_property
    def aggregation(self):  # pragma: no cover
        return AnalysisRuleAggregationOutput.make_one(
            self.boto3_raw_data["aggregation"]
        )

    @cached_property
    def custom(self):  # pragma: no cover
        return AnalysisRuleCustomOutput.make_one(self.boto3_raw_data["custom"])

    @cached_property
    def idMappingTable(self):  # pragma: no cover
        return AnalysisRuleIdMappingTable.make_one(
            self.boto3_raw_data["idMappingTable"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalysisRulePolicyV1TypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisRulePolicyV1TypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableReferenceOutput:
    boto3_raw_data: "type_defs.TableReferenceOutputTypeDef" = dataclasses.field()

    @cached_property
    def glue(self):  # pragma: no cover
        return GlueTableReference.make_one(self.boto3_raw_data["glue"])

    @cached_property
    def snowflake(self):  # pragma: no cover
        return SnowflakeTableReferenceOutput.make_one(self.boto3_raw_data["snowflake"])

    @cached_property
    def athena(self):  # pragma: no cover
        return AthenaTableReference.make_one(self.boto3_raw_data["athena"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TableReferenceOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TableReferenceOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TableReference:
    boto3_raw_data: "type_defs.TableReferenceTypeDef" = dataclasses.field()

    @cached_property
    def glue(self):  # pragma: no cover
        return GlueTableReference.make_one(self.boto3_raw_data["glue"])

    @cached_property
    def snowflake(self):  # pragma: no cover
        return SnowflakeTableReference.make_one(self.boto3_raw_data["snowflake"])

    @cached_property
    def athena(self):  # pragma: no cover
        return AthenaTableReference.make_one(self.boto3_raw_data["athena"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TableReferenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TableReferenceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisTemplate:
    boto3_raw_data: "type_defs.AnalysisTemplateTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    collaborationId = field("collaborationId")
    collaborationArn = field("collaborationArn")
    membershipId = field("membershipId")
    membershipArn = field("membershipArn")
    name = field("name")
    createTime = field("createTime")
    updateTime = field("updateTime")

    @cached_property
    def schema(self):  # pragma: no cover
        return AnalysisSchemaOutput.make_one(self.boto3_raw_data["schema"])

    format = field("format")

    @cached_property
    def source(self):  # pragma: no cover
        return AnalysisSourceOutput.make_one(self.boto3_raw_data["source"])

    description = field("description")

    @cached_property
    def sourceMetadata(self):  # pragma: no cover
        return AnalysisSourceMetadata.make_one(self.boto3_raw_data["sourceMetadata"])

    @cached_property
    def analysisParameters(self):  # pragma: no cover
        return AnalysisParameter.make_many(self.boto3_raw_data["analysisParameters"])

    @cached_property
    def validations(self):  # pragma: no cover
        return AnalysisTemplateValidationStatusDetail.make_many(
            self.boto3_raw_data["validations"]
        )

    @cached_property
    def errorMessageConfiguration(self):  # pragma: no cover
        return ErrorMessageConfiguration.make_one(
            self.boto3_raw_data["errorMessageConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnalysisTemplateTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisTemplateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CollaborationAnalysisTemplate:
    boto3_raw_data: "type_defs.CollaborationAnalysisTemplateTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    arn = field("arn")
    collaborationId = field("collaborationId")
    collaborationArn = field("collaborationArn")
    creatorAccountId = field("creatorAccountId")
    name = field("name")
    createTime = field("createTime")
    updateTime = field("updateTime")

    @cached_property
    def schema(self):  # pragma: no cover
        return AnalysisSchemaOutput.make_one(self.boto3_raw_data["schema"])

    format = field("format")
    description = field("description")

    @cached_property
    def source(self):  # pragma: no cover
        return AnalysisSourceOutput.make_one(self.boto3_raw_data["source"])

    @cached_property
    def sourceMetadata(self):  # pragma: no cover
        return AnalysisSourceMetadata.make_one(self.boto3_raw_data["sourceMetadata"])

    @cached_property
    def analysisParameters(self):  # pragma: no cover
        return AnalysisParameter.make_many(self.boto3_raw_data["analysisParameters"])

    @cached_property
    def validations(self):  # pragma: no cover
        return AnalysisTemplateValidationStatusDetail.make_many(
            self.boto3_raw_data["validations"]
        )

    @cached_property
    def errorMessageConfiguration(self):  # pragma: no cover
        return ErrorMessageConfiguration.make_one(
            self.boto3_raw_data["errorMessageConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CollaborationAnalysisTemplateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CollaborationAnalysisTemplateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationChangeRequestsOutput:
    boto3_raw_data: "type_defs.ListCollaborationChangeRequestsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def collaborationChangeRequestSummaries(self):  # pragma: no cover
        return CollaborationChangeRequestSummary.make_many(
            self.boto3_raw_data["collaborationChangeRequestSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationChangeRequestsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollaborationChangeRequestsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCollaborationChangeRequestOutput:
    boto3_raw_data: "type_defs.CreateCollaborationChangeRequestOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def collaborationChangeRequest(self):  # pragma: no cover
        return CollaborationChangeRequest.make_one(
            self.boto3_raw_data["collaborationChangeRequest"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCollaborationChangeRequestOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCollaborationChangeRequestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCollaborationChangeRequestOutput:
    boto3_raw_data: "type_defs.GetCollaborationChangeRequestOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def collaborationChangeRequest(self):  # pragma: no cover
        return CollaborationChangeRequest.make_one(
            self.boto3_raw_data["collaborationChangeRequest"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCollaborationChangeRequestOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCollaborationChangeRequestOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProtectedQueriesOutput:
    boto3_raw_data: "type_defs.ListProtectedQueriesOutputTypeDef" = dataclasses.field()

    @cached_property
    def protectedQueries(self):  # pragma: no cover
        return ProtectedQuerySummary.make_many(self.boto3_raw_data["protectedQueries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProtectedQueriesOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProtectedQueriesOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfiguredTableAssociationAnalysisRuleOutput:
    boto3_raw_data: (
        "type_defs.CreateConfiguredTableAssociationAnalysisRuleOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def analysisRule(self):  # pragma: no cover
        return ConfiguredTableAssociationAnalysisRule.make_one(
            self.boto3_raw_data["analysisRule"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConfiguredTableAssociationAnalysisRuleOutputTypeDef"
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
                "type_defs.CreateConfiguredTableAssociationAnalysisRuleOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfiguredTableAssociationAnalysisRuleOutput:
    boto3_raw_data: (
        "type_defs.GetConfiguredTableAssociationAnalysisRuleOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def analysisRule(self):  # pragma: no cover
        return ConfiguredTableAssociationAnalysisRule.make_one(
            self.boto3_raw_data["analysisRule"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConfiguredTableAssociationAnalysisRuleOutputTypeDef"
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
                "type_defs.GetConfiguredTableAssociationAnalysisRuleOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConfiguredTableAssociationAnalysisRuleOutput:
    boto3_raw_data: (
        "type_defs.UpdateConfiguredTableAssociationAnalysisRuleOutputTypeDef"
    ) = dataclasses.field()

    @cached_property
    def analysisRule(self):  # pragma: no cover
        return ConfiguredTableAssociationAnalysisRule.make_one(
            self.boto3_raw_data["analysisRule"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConfiguredTableAssociationAnalysisRuleOutputTypeDef"
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
                "type_defs.UpdateConfiguredTableAssociationAnalysisRuleOutputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfiguredTableAssociationAnalysisRuleInput:
    boto3_raw_data: (
        "type_defs.CreateConfiguredTableAssociationAnalysisRuleInputTypeDef"
    ) = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    configuredTableAssociationIdentifier = field("configuredTableAssociationIdentifier")
    analysisRuleType = field("analysisRuleType")
    analysisRulePolicy = field("analysisRulePolicy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConfiguredTableAssociationAnalysisRuleInputTypeDef"
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
                "type_defs.CreateConfiguredTableAssociationAnalysisRuleInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConfiguredTableAssociationAnalysisRuleInput:
    boto3_raw_data: (
        "type_defs.UpdateConfiguredTableAssociationAnalysisRuleInputTypeDef"
    ) = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    configuredTableAssociationIdentifier = field("configuredTableAssociationIdentifier")
    analysisRuleType = field("analysisRuleType")
    analysisRulePolicy = field("analysisRulePolicy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConfiguredTableAssociationAnalysisRuleInputTypeDef"
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
                "type_defs.UpdateConfiguredTableAssociationAnalysisRuleInputTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredTableAnalysisRulePolicyOutput:
    boto3_raw_data: "type_defs.ConfiguredTableAnalysisRulePolicyOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def v1(self):  # pragma: no cover
        return ConfiguredTableAnalysisRulePolicyV1Output.make_one(
            self.boto3_raw_data["v1"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfiguredTableAnalysisRulePolicyOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfiguredTableAnalysisRulePolicyOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConsolidatedPolicy:
    boto3_raw_data: "type_defs.ConsolidatedPolicyTypeDef" = dataclasses.field()

    @cached_property
    def v1(self):  # pragma: no cover
        return ConsolidatedPolicyV1.make_one(self.boto3_raw_data["v1"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConsolidatedPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConsolidatedPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredTableAnalysisRulePolicy:
    boto3_raw_data: "type_defs.ConfiguredTableAnalysisRulePolicyTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def v1(self):  # pragma: no cover
        return ConfiguredTableAnalysisRulePolicyV1.make_one(self.boto3_raw_data["v1"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ConfiguredTableAnalysisRulePolicyTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfiguredTableAnalysisRulePolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCollaborationPrivacyBudgetsOutput:
    boto3_raw_data: "type_defs.ListCollaborationPrivacyBudgetsOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def collaborationPrivacyBudgetSummaries(self):  # pragma: no cover
        return CollaborationPrivacyBudgetSummary.make_many(
            self.boto3_raw_data["collaborationPrivacyBudgetSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCollaborationPrivacyBudgetsOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCollaborationPrivacyBudgetsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListPrivacyBudgetsOutput:
    boto3_raw_data: "type_defs.ListPrivacyBudgetsOutputTypeDef" = dataclasses.field()

    @cached_property
    def privacyBudgetSummaries(self):  # pragma: no cover
        return PrivacyBudgetSummary.make_many(
            self.boto3_raw_data["privacyBudgetSummaries"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListPrivacyBudgetsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListPrivacyBudgetsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetSchemaOutput:
    boto3_raw_data: "type_defs.BatchGetSchemaOutputTypeDef" = dataclasses.field()

    @cached_property
    def schemas(self):  # pragma: no cover
        return Schema.make_many(self.boto3_raw_data["schemas"])

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchGetSchemaError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetSchemaOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetSchemaOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSchemaOutput:
    boto3_raw_data: "type_defs.GetSchemaOutputTypeDef" = dataclasses.field()

    @cached_property
    def schema(self):  # pragma: no cover
        return Schema.make_one(self.boto3_raw_data["schema"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetSchemaOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetSchemaOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCollaborationInput:
    boto3_raw_data: "type_defs.CreateCollaborationInputTypeDef" = dataclasses.field()

    @cached_property
    def members(self):  # pragma: no cover
        return MemberSpecification.make_many(self.boto3_raw_data["members"])

    name = field("name")
    description = field("description")
    creatorMemberAbilities = field("creatorMemberAbilities")
    creatorDisplayName = field("creatorDisplayName")
    queryLogStatus = field("queryLogStatus")
    creatorMLMemberAbilities = field("creatorMLMemberAbilities")

    @cached_property
    def dataEncryptionMetadata(self):  # pragma: no cover
        return DataEncryptionMetadata.make_one(
            self.boto3_raw_data["dataEncryptionMetadata"]
        )

    jobLogStatus = field("jobLogStatus")
    tags = field("tags")

    @cached_property
    def creatorPaymentConfiguration(self):  # pragma: no cover
        return PaymentConfiguration.make_one(
            self.boto3_raw_data["creatorPaymentConfiguration"]
        )

    analyticsEngine = field("analyticsEngine")
    autoApprovedChangeRequestTypes = field("autoApprovedChangeRequestTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCollaborationInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCollaborationInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMembersOutput:
    boto3_raw_data: "type_defs.ListMembersOutputTypeDef" = dataclasses.field()

    @cached_property
    def memberSummaries(self):  # pragma: no cover
        return MemberSummary.make_many(self.boto3_raw_data["memberSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListMembersOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMembersOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeInput:
    boto3_raw_data: "type_defs.ChangeInputTypeDef" = dataclasses.field()

    specificationType = field("specificationType")
    specification = field("specification")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChangeInputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChangeInputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMembershipsOutput:
    boto3_raw_data: "type_defs.ListMembershipsOutputTypeDef" = dataclasses.field()

    @cached_property
    def membershipSummaries(self):  # pragma: no cover
        return MembershipSummary.make_many(self.boto3_raw_data["membershipSummaries"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMembershipsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMembershipsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMembershipOutput:
    boto3_raw_data: "type_defs.CreateMembershipOutputTypeDef" = dataclasses.field()

    @cached_property
    def membership(self):  # pragma: no cover
        return Membership.make_one(self.boto3_raw_data["membership"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMembershipOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMembershipOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMembershipOutput:
    boto3_raw_data: "type_defs.GetMembershipOutputTypeDef" = dataclasses.field()

    @cached_property
    def membership(self):  # pragma: no cover
        return Membership.make_one(self.boto3_raw_data["membership"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMembershipOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMembershipOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateMembershipOutput:
    boto3_raw_data: "type_defs.UpdateMembershipOutputTypeDef" = dataclasses.field()

    @cached_property
    def membership(self):  # pragma: no cover
        return Membership.make_one(self.boto3_raw_data["membership"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateMembershipOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateMembershipOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListProtectedJobsOutput:
    boto3_raw_data: "type_defs.ListProtectedJobsOutputTypeDef" = dataclasses.field()

    @cached_property
    def protectedJobs(self):  # pragma: no cover
        return ProtectedJobSummary.make_many(self.boto3_raw_data["protectedJobs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListProtectedJobsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListProtectedJobsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProtectedJobOutput:
    boto3_raw_data: "type_defs.GetProtectedJobOutputTypeDef" = dataclasses.field()

    @cached_property
    def protectedJob(self):  # pragma: no cover
        return ProtectedJob.make_one(self.boto3_raw_data["protectedJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetProtectedJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProtectedJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartProtectedJobOutput:
    boto3_raw_data: "type_defs.StartProtectedJobOutputTypeDef" = dataclasses.field()

    @cached_property
    def protectedJob(self):  # pragma: no cover
        return ProtectedJob.make_one(self.boto3_raw_data["protectedJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartProtectedJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartProtectedJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProtectedJobOutput:
    boto3_raw_data: "type_defs.UpdateProtectedJobOutputTypeDef" = dataclasses.field()

    @cached_property
    def protectedJob(self):  # pragma: no cover
        return ProtectedJob.make_one(self.boto3_raw_data["protectedJob"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProtectedJobOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProtectedJobOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedQueryResultConfigurationOutput:
    boto3_raw_data: "type_defs.ProtectedQueryResultConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def outputConfiguration(self):  # pragma: no cover
        return ProtectedQueryOutputConfigurationOutput.make_one(
            self.boto3_raw_data["outputConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectedQueryResultConfigurationOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedQueryResultConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedQueryResultConfiguration:
    boto3_raw_data: "type_defs.ProtectedQueryResultConfigurationTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def outputConfiguration(self):  # pragma: no cover
        return ProtectedQueryOutputConfiguration.make_one(
            self.boto3_raw_data["outputConfiguration"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ProtectedQueryResultConfigurationTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ProtectedQueryResultConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisRulePolicy:
    boto3_raw_data: "type_defs.AnalysisRulePolicyTypeDef" = dataclasses.field()

    @cached_property
    def v1(self):  # pragma: no cover
        return AnalysisRulePolicyV1.make_one(self.boto3_raw_data["v1"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalysisRulePolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisRulePolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredTable:
    boto3_raw_data: "type_defs.ConfiguredTableTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")
    name = field("name")

    @cached_property
    def tableReference(self):  # pragma: no cover
        return TableReferenceOutput.make_one(self.boto3_raw_data["tableReference"])

    createTime = field("createTime")
    updateTime = field("updateTime")
    analysisRuleTypes = field("analysisRuleTypes")
    analysisMethod = field("analysisMethod")
    allowedColumns = field("allowedColumns")
    description = field("description")
    selectedAnalysisMethods = field("selectedAnalysisMethods")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ConfiguredTableTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ConfiguredTableTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAnalysisTemplateOutput:
    boto3_raw_data: "type_defs.CreateAnalysisTemplateOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def analysisTemplate(self):  # pragma: no cover
        return AnalysisTemplate.make_one(self.boto3_raw_data["analysisTemplate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAnalysisTemplateOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAnalysisTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAnalysisTemplateOutput:
    boto3_raw_data: "type_defs.GetAnalysisTemplateOutputTypeDef" = dataclasses.field()

    @cached_property
    def analysisTemplate(self):  # pragma: no cover
        return AnalysisTemplate.make_one(self.boto3_raw_data["analysisTemplate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAnalysisTemplateOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAnalysisTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAnalysisTemplateOutput:
    boto3_raw_data: "type_defs.UpdateAnalysisTemplateOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def analysisTemplate(self):  # pragma: no cover
        return AnalysisTemplate.make_one(self.boto3_raw_data["analysisTemplate"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAnalysisTemplateOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAnalysisTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetCollaborationAnalysisTemplateOutput:
    boto3_raw_data: "type_defs.BatchGetCollaborationAnalysisTemplateOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def collaborationAnalysisTemplates(self):  # pragma: no cover
        return CollaborationAnalysisTemplate.make_many(
            self.boto3_raw_data["collaborationAnalysisTemplates"]
        )

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchGetCollaborationAnalysisTemplateError.make_many(
            self.boto3_raw_data["errors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetCollaborationAnalysisTemplateOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetCollaborationAnalysisTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCollaborationAnalysisTemplateOutput:
    boto3_raw_data: "type_defs.GetCollaborationAnalysisTemplateOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def collaborationAnalysisTemplate(self):  # pragma: no cover
        return CollaborationAnalysisTemplate.make_one(
            self.boto3_raw_data["collaborationAnalysisTemplate"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCollaborationAnalysisTemplateOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCollaborationAnalysisTemplateOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAnalysisTemplateInput:
    boto3_raw_data: "type_defs.CreateAnalysisTemplateInputTypeDef" = dataclasses.field()

    membershipIdentifier = field("membershipIdentifier")
    name = field("name")
    format = field("format")
    source = field("source")
    description = field("description")
    tags = field("tags")

    @cached_property
    def analysisParameters(self):  # pragma: no cover
        return AnalysisParameter.make_many(self.boto3_raw_data["analysisParameters"])

    schema = field("schema")

    @cached_property
    def errorMessageConfiguration(self):  # pragma: no cover
        return ErrorMessageConfiguration.make_one(
            self.boto3_raw_data["errorMessageConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAnalysisTemplateInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAnalysisTemplateInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ConfiguredTableAnalysisRule:
    boto3_raw_data: "type_defs.ConfiguredTableAnalysisRuleTypeDef" = dataclasses.field()

    configuredTableId = field("configuredTableId")
    configuredTableArn = field("configuredTableArn")

    @cached_property
    def policy(self):  # pragma: no cover
        return ConfiguredTableAnalysisRulePolicyOutput.make_one(
            self.boto3_raw_data["policy"]
        )

    type = field("type")
    createTime = field("createTime")
    updateTime = field("updateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ConfiguredTableAnalysisRuleTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ConfiguredTableAnalysisRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCollaborationChangeRequestInput:
    boto3_raw_data: "type_defs.CreateCollaborationChangeRequestInputTypeDef" = (
        dataclasses.field()
    )

    collaborationIdentifier = field("collaborationIdentifier")

    @cached_property
    def changes(self):  # pragma: no cover
        return ChangeInput.make_many(self.boto3_raw_data["changes"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateCollaborationChangeRequestInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCollaborationChangeRequestInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ProtectedQuery:
    boto3_raw_data: "type_defs.ProtectedQueryTypeDef" = dataclasses.field()

    id = field("id")
    membershipId = field("membershipId")
    membershipArn = field("membershipArn")
    createTime = field("createTime")
    status = field("status")

    @cached_property
    def sqlParameters(self):  # pragma: no cover
        return ProtectedQuerySQLParametersOutput.make_one(
            self.boto3_raw_data["sqlParameters"]
        )

    @cached_property
    def resultConfiguration(self):  # pragma: no cover
        return ProtectedQueryResultConfigurationOutput.make_one(
            self.boto3_raw_data["resultConfiguration"]
        )

    @cached_property
    def statistics(self):  # pragma: no cover
        return ProtectedQueryStatistics.make_one(self.boto3_raw_data["statistics"])

    @cached_property
    def result(self):  # pragma: no cover
        return ProtectedQueryResult.make_one(self.boto3_raw_data["result"])

    @cached_property
    def error(self):  # pragma: no cover
        return ProtectedQueryError.make_one(self.boto3_raw_data["error"])

    @cached_property
    def differentialPrivacy(self):  # pragma: no cover
        return DifferentialPrivacyParameters.make_one(
            self.boto3_raw_data["differentialPrivacy"]
        )

    @cached_property
    def computeConfiguration(self):  # pragma: no cover
        return ComputeConfiguration.make_one(
            self.boto3_raw_data["computeConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ProtectedQueryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ProtectedQueryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisRule:
    boto3_raw_data: "type_defs.AnalysisRuleTypeDef" = dataclasses.field()

    collaborationId = field("collaborationId")
    type = field("type")
    name = field("name")
    createTime = field("createTime")
    updateTime = field("updateTime")

    @cached_property
    def policy(self):  # pragma: no cover
        return AnalysisRulePolicy.make_one(self.boto3_raw_data["policy"])

    @cached_property
    def collaborationPolicy(self):  # pragma: no cover
        return ConfiguredTableAssociationAnalysisRulePolicyOutput.make_one(
            self.boto3_raw_data["collaborationPolicy"]
        )

    @cached_property
    def consolidatedPolicy(self):  # pragma: no cover
        return ConsolidatedPolicy.make_one(self.boto3_raw_data["consolidatedPolicy"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnalysisRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnalysisRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfiguredTableOutput:
    boto3_raw_data: "type_defs.CreateConfiguredTableOutputTypeDef" = dataclasses.field()

    @cached_property
    def configuredTable(self):  # pragma: no cover
        return ConfiguredTable.make_one(self.boto3_raw_data["configuredTable"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConfiguredTableOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConfiguredTableOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfiguredTableOutput:
    boto3_raw_data: "type_defs.GetConfiguredTableOutputTypeDef" = dataclasses.field()

    @cached_property
    def configuredTable(self):  # pragma: no cover
        return ConfiguredTable.make_one(self.boto3_raw_data["configuredTable"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetConfiguredTableOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfiguredTableOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConfiguredTableOutput:
    boto3_raw_data: "type_defs.UpdateConfiguredTableOutputTypeDef" = dataclasses.field()

    @cached_property
    def configuredTable(self):  # pragma: no cover
        return ConfiguredTable.make_one(self.boto3_raw_data["configuredTable"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConfiguredTableOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConfiguredTableOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfiguredTableInput:
    boto3_raw_data: "type_defs.CreateConfiguredTableInputTypeDef" = dataclasses.field()

    name = field("name")
    tableReference = field("tableReference")
    allowedColumns = field("allowedColumns")
    analysisMethod = field("analysisMethod")
    description = field("description")
    selectedAnalysisMethods = field("selectedAnalysisMethods")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateConfiguredTableInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConfiguredTableInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConfiguredTableInput:
    boto3_raw_data: "type_defs.UpdateConfiguredTableInputTypeDef" = dataclasses.field()

    configuredTableIdentifier = field("configuredTableIdentifier")
    name = field("name")
    description = field("description")
    tableReference = field("tableReference")
    allowedColumns = field("allowedColumns")
    analysisMethod = field("analysisMethod")
    selectedAnalysisMethods = field("selectedAnalysisMethods")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateConfiguredTableInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConfiguredTableInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfiguredTableAnalysisRuleOutput:
    boto3_raw_data: "type_defs.CreateConfiguredTableAnalysisRuleOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def analysisRule(self):  # pragma: no cover
        return ConfiguredTableAnalysisRule.make_one(self.boto3_raw_data["analysisRule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConfiguredTableAnalysisRuleOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConfiguredTableAnalysisRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetConfiguredTableAnalysisRuleOutput:
    boto3_raw_data: "type_defs.GetConfiguredTableAnalysisRuleOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def analysisRule(self):  # pragma: no cover
        return ConfiguredTableAnalysisRule.make_one(self.boto3_raw_data["analysisRule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetConfiguredTableAnalysisRuleOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetConfiguredTableAnalysisRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConfiguredTableAnalysisRuleOutput:
    boto3_raw_data: "type_defs.UpdateConfiguredTableAnalysisRuleOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def analysisRule(self):  # pragma: no cover
        return ConfiguredTableAnalysisRule.make_one(self.boto3_raw_data["analysisRule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConfiguredTableAnalysisRuleOutputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConfiguredTableAnalysisRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateConfiguredTableAnalysisRuleInput:
    boto3_raw_data: "type_defs.CreateConfiguredTableAnalysisRuleInputTypeDef" = (
        dataclasses.field()
    )

    configuredTableIdentifier = field("configuredTableIdentifier")
    analysisRuleType = field("analysisRuleType")
    analysisRulePolicy = field("analysisRulePolicy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateConfiguredTableAnalysisRuleInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateConfiguredTableAnalysisRuleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateConfiguredTableAnalysisRuleInput:
    boto3_raw_data: "type_defs.UpdateConfiguredTableAnalysisRuleInputTypeDef" = (
        dataclasses.field()
    )

    configuredTableIdentifier = field("configuredTableIdentifier")
    analysisRuleType = field("analysisRuleType")
    analysisRulePolicy = field("analysisRulePolicy")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateConfiguredTableAnalysisRuleInputTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateConfiguredTableAnalysisRuleInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetProtectedQueryOutput:
    boto3_raw_data: "type_defs.GetProtectedQueryOutputTypeDef" = dataclasses.field()

    @cached_property
    def protectedQuery(self):  # pragma: no cover
        return ProtectedQuery.make_one(self.boto3_raw_data["protectedQuery"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetProtectedQueryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetProtectedQueryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartProtectedQueryOutput:
    boto3_raw_data: "type_defs.StartProtectedQueryOutputTypeDef" = dataclasses.field()

    @cached_property
    def protectedQuery(self):  # pragma: no cover
        return ProtectedQuery.make_one(self.boto3_raw_data["protectedQuery"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartProtectedQueryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartProtectedQueryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateProtectedQueryOutput:
    boto3_raw_data: "type_defs.UpdateProtectedQueryOutputTypeDef" = dataclasses.field()

    @cached_property
    def protectedQuery(self):  # pragma: no cover
        return ProtectedQuery.make_one(self.boto3_raw_data["protectedQuery"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateProtectedQueryOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateProtectedQueryOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartProtectedQueryInput:
    boto3_raw_data: "type_defs.StartProtectedQueryInputTypeDef" = dataclasses.field()

    type = field("type")
    membershipIdentifier = field("membershipIdentifier")
    sqlParameters = field("sqlParameters")
    resultConfiguration = field("resultConfiguration")

    @cached_property
    def computeConfiguration(self):  # pragma: no cover
        return ComputeConfiguration.make_one(
            self.boto3_raw_data["computeConfiguration"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartProtectedQueryInputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartProtectedQueryInputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetSchemaAnalysisRuleOutput:
    boto3_raw_data: "type_defs.BatchGetSchemaAnalysisRuleOutputTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def analysisRules(self):  # pragma: no cover
        return AnalysisRule.make_many(self.boto3_raw_data["analysisRules"])

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchGetSchemaAnalysisRuleError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.BatchGetSchemaAnalysisRuleOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetSchemaAnalysisRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSchemaAnalysisRuleOutput:
    boto3_raw_data: "type_defs.GetSchemaAnalysisRuleOutputTypeDef" = dataclasses.field()

    @cached_property
    def analysisRule(self):  # pragma: no cover
        return AnalysisRule.make_one(self.boto3_raw_data["analysisRule"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSchemaAnalysisRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSchemaAnalysisRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
