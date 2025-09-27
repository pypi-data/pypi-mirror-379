# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_auditmanager import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AWSAccount:
    boto3_raw_data: "type_defs.AWSAccountTypeDef" = dataclasses.field()

    id = field("id")
    emailAddress = field("emailAddress")
    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AWSAccountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AWSAccountTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AWSService:
    boto3_raw_data: "type_defs.AWSServiceTypeDef" = dataclasses.field()

    serviceName = field("serviceName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AWSServiceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AWSServiceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Delegation:
    boto3_raw_data: "type_defs.DelegationTypeDef" = dataclasses.field()

    id = field("id")
    assessmentName = field("assessmentName")
    assessmentId = field("assessmentId")
    status = field("status")
    roleArn = field("roleArn")
    roleType = field("roleType")
    creationTime = field("creationTime")
    lastUpdated = field("lastUpdated")
    controlSetId = field("controlSetId")
    comment = field("comment")
    createdBy = field("createdBy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DelegationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DelegationTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Role:
    boto3_raw_data: "type_defs.RoleTypeDef" = dataclasses.field()

    roleType = field("roleType")
    roleArn = field("roleArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RoleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RoleTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ControlComment:
    boto3_raw_data: "type_defs.ControlCommentTypeDef" = dataclasses.field()

    authorName = field("authorName")
    commentBody = field("commentBody")
    postedDate = field("postedDate")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ControlCommentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ControlCommentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentEvidenceFolder:
    boto3_raw_data: "type_defs.AssessmentEvidenceFolderTypeDef" = dataclasses.field()

    name = field("name")
    date = field("date")
    assessmentId = field("assessmentId")
    controlSetId = field("controlSetId")
    controlId = field("controlId")
    id = field("id")
    dataSource = field("dataSource")
    author = field("author")
    totalEvidence = field("totalEvidence")
    assessmentReportSelectionCount = field("assessmentReportSelectionCount")
    controlName = field("controlName")
    evidenceResourcesIncludedCount = field("evidenceResourcesIncludedCount")
    evidenceByTypeConfigurationDataCount = field("evidenceByTypeConfigurationDataCount")
    evidenceByTypeManualCount = field("evidenceByTypeManualCount")
    evidenceByTypeComplianceCheckCount = field("evidenceByTypeComplianceCheckCount")
    evidenceByTypeComplianceCheckIssuesCount = field(
        "evidenceByTypeComplianceCheckIssuesCount"
    )
    evidenceByTypeUserActivityCount = field("evidenceByTypeUserActivityCount")
    evidenceAwsServiceSourceCount = field("evidenceAwsServiceSourceCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssessmentEvidenceFolderTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentEvidenceFolderTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentFrameworkMetadata:
    boto3_raw_data: "type_defs.AssessmentFrameworkMetadataTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")
    type = field("type")
    name = field("name")
    description = field("description")
    logo = field("logo")
    complianceType = field("complianceType")
    controlsCount = field("controlsCount")
    controlSetsCount = field("controlSetsCount")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssessmentFrameworkMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentFrameworkMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentFrameworkShareRequest:
    boto3_raw_data: "type_defs.AssessmentFrameworkShareRequestTypeDef" = (
        dataclasses.field()
    )

    id = field("id")
    frameworkId = field("frameworkId")
    frameworkName = field("frameworkName")
    frameworkDescription = field("frameworkDescription")
    status = field("status")
    sourceAccount = field("sourceAccount")
    destinationAccount = field("destinationAccount")
    destinationRegion = field("destinationRegion")
    expirationTime = field("expirationTime")
    creationTime = field("creationTime")
    lastUpdated = field("lastUpdated")
    comment = field("comment")
    standardControlsCount = field("standardControlsCount")
    customControlsCount = field("customControlsCount")
    complianceType = field("complianceType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssessmentFrameworkShareRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentFrameworkShareRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FrameworkMetadata:
    boto3_raw_data: "type_defs.FrameworkMetadataTypeDef" = dataclasses.field()

    name = field("name")
    description = field("description")
    logo = field("logo")
    complianceType = field("complianceType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FrameworkMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FrameworkMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentReportsDestination:
    boto3_raw_data: "type_defs.AssessmentReportsDestinationTypeDef" = (
        dataclasses.field()
    )

    destinationType = field("destinationType")
    destination = field("destination")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssessmentReportsDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentReportsDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentReportEvidenceError:
    boto3_raw_data: "type_defs.AssessmentReportEvidenceErrorTypeDef" = (
        dataclasses.field()
    )

    evidenceId = field("evidenceId")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.AssessmentReportEvidenceErrorTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentReportEvidenceErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentReportMetadata:
    boto3_raw_data: "type_defs.AssessmentReportMetadataTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    description = field("description")
    assessmentId = field("assessmentId")
    assessmentName = field("assessmentName")
    author = field("author")
    status = field("status")
    creationTime = field("creationTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssessmentReportMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentReportMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentReport:
    boto3_raw_data: "type_defs.AssessmentReportTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    description = field("description")
    awsAccountId = field("awsAccountId")
    assessmentId = field("assessmentId")
    assessmentName = field("assessmentName")
    author = field("author")
    status = field("status")
    creationTime = field("creationTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssessmentReportTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentReportTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociateAssessmentReportEvidenceFolderRequest:
    boto3_raw_data: (
        "type_defs.AssociateAssessmentReportEvidenceFolderRequestTypeDef"
    ) = dataclasses.field()

    assessmentId = field("assessmentId")
    evidenceFolderId = field("evidenceFolderId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.AssociateAssessmentReportEvidenceFolderRequestTypeDef"
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
                "type_defs.AssociateAssessmentReportEvidenceFolderRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAssociateAssessmentReportEvidenceRequest:
    boto3_raw_data: "type_defs.BatchAssociateAssessmentReportEvidenceRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentId = field("assessmentId")
    evidenceFolderId = field("evidenceFolderId")
    evidenceIds = field("evidenceIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchAssociateAssessmentReportEvidenceRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchAssociateAssessmentReportEvidenceRequestTypeDef"]
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
class CreateDelegationRequest:
    boto3_raw_data: "type_defs.CreateDelegationRequestTypeDef" = dataclasses.field()

    comment = field("comment")
    controlSetId = field("controlSetId")
    roleArn = field("roleArn")
    roleType = field("roleType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDelegationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDelegationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteDelegationByAssessmentError:
    boto3_raw_data: "type_defs.BatchDeleteDelegationByAssessmentErrorTypeDef" = (
        dataclasses.field()
    )

    delegationId = field("delegationId")
    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteDelegationByAssessmentErrorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteDelegationByAssessmentErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteDelegationByAssessmentRequest:
    boto3_raw_data: "type_defs.BatchDeleteDelegationByAssessmentRequestTypeDef" = (
        dataclasses.field()
    )

    delegationIds = field("delegationIds")
    assessmentId = field("assessmentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteDelegationByAssessmentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteDelegationByAssessmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDisassociateAssessmentReportEvidenceRequest:
    boto3_raw_data: (
        "type_defs.BatchDisassociateAssessmentReportEvidenceRequestTypeDef"
    ) = dataclasses.field()

    assessmentId = field("assessmentId")
    evidenceFolderId = field("evidenceFolderId")
    evidenceIds = field("evidenceIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDisassociateAssessmentReportEvidenceRequestTypeDef"
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
                "type_defs.BatchDisassociateAssessmentReportEvidenceRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ManualEvidence:
    boto3_raw_data: "type_defs.ManualEvidenceTypeDef" = dataclasses.field()

    s3ResourcePath = field("s3ResourcePath")
    textResponse = field("textResponse")
    evidenceFileName = field("evidenceFileName")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ManualEvidenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ManualEvidenceTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ChangeLog:
    boto3_raw_data: "type_defs.ChangeLogTypeDef" = dataclasses.field()

    objectType = field("objectType")
    objectName = field("objectName")
    action = field("action")
    createdAt = field("createdAt")
    createdBy = field("createdBy")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ChangeLogTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ChangeLogTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvidenceInsights:
    boto3_raw_data: "type_defs.EvidenceInsightsTypeDef" = dataclasses.field()

    noncompliantEvidenceCount = field("noncompliantEvidenceCount")
    compliantEvidenceCount = field("compliantEvidenceCount")
    inconclusiveEvidenceCount = field("inconclusiveEvidenceCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvidenceInsightsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvidenceInsightsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SourceKeyword:
    boto3_raw_data: "type_defs.SourceKeywordTypeDef" = dataclasses.field()

    keywordInputType = field("keywordInputType")
    keywordValue = field("keywordValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SourceKeywordTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SourceKeywordTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ControlMetadata:
    boto3_raw_data: "type_defs.ControlMetadataTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")
    name = field("name")
    controlSources = field("controlSources")
    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ControlMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ControlMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssessmentFrameworkControl:
    boto3_raw_data: "type_defs.CreateAssessmentFrameworkControlTypeDef" = (
        dataclasses.field()
    )

    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAssessmentFrameworkControlTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssessmentFrameworkControlTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssessmentReportRequest:
    boto3_raw_data: "type_defs.CreateAssessmentReportRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    assessmentId = field("assessmentId")
    description = field("description")
    queryStatement = field("queryStatement")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAssessmentReportRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssessmentReportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefaultExportDestination:
    boto3_raw_data: "type_defs.DefaultExportDestinationTypeDef" = dataclasses.field()

    destinationType = field("destinationType")
    destination = field("destination")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DefaultExportDestinationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefaultExportDestinationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DelegationMetadata:
    boto3_raw_data: "type_defs.DelegationMetadataTypeDef" = dataclasses.field()

    id = field("id")
    assessmentName = field("assessmentName")
    assessmentId = field("assessmentId")
    status = field("status")
    roleArn = field("roleArn")
    creationTime = field("creationTime")
    controlSetName = field("controlSetName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DelegationMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DelegationMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAssessmentFrameworkRequest:
    boto3_raw_data: "type_defs.DeleteAssessmentFrameworkRequestTypeDef" = (
        dataclasses.field()
    )

    frameworkId = field("frameworkId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteAssessmentFrameworkRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAssessmentFrameworkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAssessmentFrameworkShareRequest:
    boto3_raw_data: "type_defs.DeleteAssessmentFrameworkShareRequestTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")
    requestType = field("requestType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeleteAssessmentFrameworkShareRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAssessmentFrameworkShareRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAssessmentReportRequest:
    boto3_raw_data: "type_defs.DeleteAssessmentReportRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentId = field("assessmentId")
    assessmentReportId = field("assessmentReportId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DeleteAssessmentReportRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAssessmentReportRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAssessmentRequest:
    boto3_raw_data: "type_defs.DeleteAssessmentRequestTypeDef" = dataclasses.field()

    assessmentId = field("assessmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAssessmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAssessmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteControlRequest:
    boto3_raw_data: "type_defs.DeleteControlRequestTypeDef" = dataclasses.field()

    controlId = field("controlId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteControlRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteControlRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterOrganizationAdminAccountRequest:
    boto3_raw_data: "type_defs.DeregisterOrganizationAdminAccountRequestTypeDef" = (
        dataclasses.field()
    )

    adminAccountId = field("adminAccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DeregisterOrganizationAdminAccountRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterOrganizationAdminAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregistrationPolicy:
    boto3_raw_data: "type_defs.DeregistrationPolicyTypeDef" = dataclasses.field()

    deleteResources = field("deleteResources")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeregistrationPolicyTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregistrationPolicyTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateAssessmentReportEvidenceFolderRequest:
    boto3_raw_data: (
        "type_defs.DisassociateAssessmentReportEvidenceFolderRequestTypeDef"
    ) = dataclasses.field()

    assessmentId = field("assessmentId")
    evidenceFolderId = field("evidenceFolderId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DisassociateAssessmentReportEvidenceFolderRequestTypeDef"
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
                "type_defs.DisassociateAssessmentReportEvidenceFolderRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EvidenceFinderEnablement:
    boto3_raw_data: "type_defs.EvidenceFinderEnablementTypeDef" = dataclasses.field()

    eventDataStoreArn = field("eventDataStoreArn")
    enablementStatus = field("enablementStatus")
    backfillStatus = field("backfillStatus")
    error = field("error")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EvidenceFinderEnablementTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EvidenceFinderEnablementTypeDef"]
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

    arn = field("arn")
    value = field("value")
    complianceCheck = field("complianceCheck")

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
class GetAssessmentFrameworkRequest:
    boto3_raw_data: "type_defs.GetAssessmentFrameworkRequestTypeDef" = (
        dataclasses.field()
    )

    frameworkId = field("frameworkId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAssessmentFrameworkRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssessmentFrameworkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssessmentReportUrlRequest:
    boto3_raw_data: "type_defs.GetAssessmentReportUrlRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentReportId = field("assessmentReportId")
    assessmentId = field("assessmentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAssessmentReportUrlRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssessmentReportUrlRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class URL:
    boto3_raw_data: "type_defs.URLTypeDef" = dataclasses.field()

    hyperlinkName = field("hyperlinkName")
    link = field("link")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.URLTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.URLTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssessmentRequest:
    boto3_raw_data: "type_defs.GetAssessmentRequestTypeDef" = dataclasses.field()

    assessmentId = field("assessmentId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAssessmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssessmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChangeLogsRequest:
    boto3_raw_data: "type_defs.GetChangeLogsRequestTypeDef" = dataclasses.field()

    assessmentId = field("assessmentId")
    controlSetId = field("controlSetId")
    controlId = field("controlId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetChangeLogsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChangeLogsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetControlRequest:
    boto3_raw_data: "type_defs.GetControlRequestTypeDef" = dataclasses.field()

    controlId = field("controlId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetControlRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetControlRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDelegationsRequest:
    boto3_raw_data: "type_defs.GetDelegationsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDelegationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDelegationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEvidenceByEvidenceFolderRequest:
    boto3_raw_data: "type_defs.GetEvidenceByEvidenceFolderRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentId = field("assessmentId")
    controlSetId = field("controlSetId")
    evidenceFolderId = field("evidenceFolderId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEvidenceByEvidenceFolderRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEvidenceByEvidenceFolderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEvidenceFileUploadUrlRequest:
    boto3_raw_data: "type_defs.GetEvidenceFileUploadUrlRequestTypeDef" = (
        dataclasses.field()
    )

    fileName = field("fileName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetEvidenceFileUploadUrlRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEvidenceFileUploadUrlRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEvidenceFolderRequest:
    boto3_raw_data: "type_defs.GetEvidenceFolderRequestTypeDef" = dataclasses.field()

    assessmentId = field("assessmentId")
    controlSetId = field("controlSetId")
    evidenceFolderId = field("evidenceFolderId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEvidenceFolderRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEvidenceFolderRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEvidenceFoldersByAssessmentControlRequest:
    boto3_raw_data: "type_defs.GetEvidenceFoldersByAssessmentControlRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentId = field("assessmentId")
    controlSetId = field("controlSetId")
    controlId = field("controlId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEvidenceFoldersByAssessmentControlRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEvidenceFoldersByAssessmentControlRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEvidenceFoldersByAssessmentRequest:
    boto3_raw_data: "type_defs.GetEvidenceFoldersByAssessmentRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentId = field("assessmentId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEvidenceFoldersByAssessmentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEvidenceFoldersByAssessmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEvidenceRequest:
    boto3_raw_data: "type_defs.GetEvidenceRequestTypeDef" = dataclasses.field()

    assessmentId = field("assessmentId")
    controlSetId = field("controlSetId")
    evidenceFolderId = field("evidenceFolderId")
    evidenceId = field("evidenceId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEvidenceRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEvidenceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInsightsByAssessmentRequest:
    boto3_raw_data: "type_defs.GetInsightsByAssessmentRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentId = field("assessmentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetInsightsByAssessmentRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInsightsByAssessmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InsightsByAssessment:
    boto3_raw_data: "type_defs.InsightsByAssessmentTypeDef" = dataclasses.field()

    noncompliantEvidenceCount = field("noncompliantEvidenceCount")
    compliantEvidenceCount = field("compliantEvidenceCount")
    inconclusiveEvidenceCount = field("inconclusiveEvidenceCount")
    assessmentControlsCountByNoncompliantEvidence = field(
        "assessmentControlsCountByNoncompliantEvidence"
    )
    totalAssessmentControlsCount = field("totalAssessmentControlsCount")
    lastUpdated = field("lastUpdated")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InsightsByAssessmentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InsightsByAssessmentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Insights:
    boto3_raw_data: "type_defs.InsightsTypeDef" = dataclasses.field()

    activeAssessmentsCount = field("activeAssessmentsCount")
    noncompliantEvidenceCount = field("noncompliantEvidenceCount")
    compliantEvidenceCount = field("compliantEvidenceCount")
    inconclusiveEvidenceCount = field("inconclusiveEvidenceCount")
    assessmentControlsCountByNoncompliantEvidence = field(
        "assessmentControlsCountByNoncompliantEvidence"
    )
    totalAssessmentControlsCount = field("totalAssessmentControlsCount")
    lastUpdated = field("lastUpdated")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.InsightsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.InsightsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceMetadata:
    boto3_raw_data: "type_defs.ServiceMetadataTypeDef" = dataclasses.field()

    name = field("name")
    displayName = field("displayName")
    description = field("description")
    category = field("category")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceMetadataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceMetadataTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSettingsRequest:
    boto3_raw_data: "type_defs.GetSettingsRequestTypeDef" = dataclasses.field()

    attribute = field("attribute")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssessmentControlInsightsByControlDomainRequest:
    boto3_raw_data: (
        "type_defs.ListAssessmentControlInsightsByControlDomainRequestTypeDef"
    ) = dataclasses.field()

    controlDomainId = field("controlDomainId")
    assessmentId = field("assessmentId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssessmentControlInsightsByControlDomainRequestTypeDef"
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
                "type_defs.ListAssessmentControlInsightsByControlDomainRequestTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssessmentFrameworkShareRequestsRequest:
    boto3_raw_data: "type_defs.ListAssessmentFrameworkShareRequestsRequestTypeDef" = (
        dataclasses.field()
    )

    requestType = field("requestType")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssessmentFrameworkShareRequestsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssessmentFrameworkShareRequestsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssessmentFrameworksRequest:
    boto3_raw_data: "type_defs.ListAssessmentFrameworksRequestTypeDef" = (
        dataclasses.field()
    )

    frameworkType = field("frameworkType")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssessmentFrameworksRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssessmentFrameworksRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssessmentReportsRequest:
    boto3_raw_data: "type_defs.ListAssessmentReportsRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssessmentReportsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssessmentReportsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssessmentsRequest:
    boto3_raw_data: "type_defs.ListAssessmentsRequestTypeDef" = dataclasses.field()

    status = field("status")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssessmentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssessmentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListControlDomainInsightsByAssessmentRequest:
    boto3_raw_data: "type_defs.ListControlDomainInsightsByAssessmentRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentId = field("assessmentId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListControlDomainInsightsByAssessmentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListControlDomainInsightsByAssessmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListControlDomainInsightsRequest:
    boto3_raw_data: "type_defs.ListControlDomainInsightsRequestTypeDef" = (
        dataclasses.field()
    )

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListControlDomainInsightsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListControlDomainInsightsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListControlInsightsByControlDomainRequest:
    boto3_raw_data: "type_defs.ListControlInsightsByControlDomainRequestTypeDef" = (
        dataclasses.field()
    )

    controlDomainId = field("controlDomainId")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListControlInsightsByControlDomainRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListControlInsightsByControlDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListControlsRequest:
    boto3_raw_data: "type_defs.ListControlsRequestTypeDef" = dataclasses.field()

    controlType = field("controlType")
    nextToken = field("nextToken")
    maxResults = field("maxResults")
    controlCatalogId = field("controlCatalogId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListControlsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListControlsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeywordsForDataSourceRequest:
    boto3_raw_data: "type_defs.ListKeywordsForDataSourceRequestTypeDef" = (
        dataclasses.field()
    )

    source = field("source")
    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListKeywordsForDataSourceRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKeywordsForDataSourceRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNotificationsRequest:
    boto3_raw_data: "type_defs.ListNotificationsRequestTypeDef" = dataclasses.field()

    nextToken = field("nextToken")
    maxResults = field("maxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNotificationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotificationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Notification:
    boto3_raw_data: "type_defs.NotificationTypeDef" = dataclasses.field()

    id = field("id")
    assessmentId = field("assessmentId")
    assessmentName = field("assessmentName")
    controlSetId = field("controlSetId")
    controlSetName = field("controlSetName")
    description = field("description")
    eventTime = field("eventTime")
    source = field("source")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NotificationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NotificationTypeDef"]],
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
class RegisterAccountRequest:
    boto3_raw_data: "type_defs.RegisterAccountRequestTypeDef" = dataclasses.field()

    kmsKey = field("kmsKey")
    delegatedAdminAccount = field("delegatedAdminAccount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterAccountRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterOrganizationAdminAccountRequest:
    boto3_raw_data: "type_defs.RegisterOrganizationAdminAccountRequestTypeDef" = (
        dataclasses.field()
    )

    adminAccountId = field("adminAccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegisterOrganizationAdminAccountRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterOrganizationAdminAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAssessmentFrameworkShareRequest:
    boto3_raw_data: "type_defs.StartAssessmentFrameworkShareRequestTypeDef" = (
        dataclasses.field()
    )

    frameworkId = field("frameworkId")
    destinationAccount = field("destinationAccount")
    destinationRegion = field("destinationRegion")
    comment = field("comment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartAssessmentFrameworkShareRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAssessmentFrameworkShareRequestTypeDef"]
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
class UpdateAssessmentControlRequest:
    boto3_raw_data: "type_defs.UpdateAssessmentControlRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentId = field("assessmentId")
    controlSetId = field("controlSetId")
    controlId = field("controlId")
    controlStatus = field("controlStatus")
    commentBody = field("commentBody")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAssessmentControlRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssessmentControlRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssessmentControlSetStatusRequest:
    boto3_raw_data: "type_defs.UpdateAssessmentControlSetStatusRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentId = field("assessmentId")
    controlSetId = field("controlSetId")
    status = field("status")
    comment = field("comment")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAssessmentControlSetStatusRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssessmentControlSetStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssessmentFrameworkShareRequest:
    boto3_raw_data: "type_defs.UpdateAssessmentFrameworkShareRequestTypeDef" = (
        dataclasses.field()
    )

    requestId = field("requestId")
    requestType = field("requestType")
    action = field("action")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAssessmentFrameworkShareRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssessmentFrameworkShareRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssessmentStatusRequest:
    boto3_raw_data: "type_defs.UpdateAssessmentStatusRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentId = field("assessmentId")
    status = field("status")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAssessmentStatusRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssessmentStatusRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidateAssessmentReportIntegrityRequest:
    boto3_raw_data: "type_defs.ValidateAssessmentReportIntegrityRequestTypeDef" = (
        dataclasses.field()
    )

    s3RelativePath = field("s3RelativePath")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ValidateAssessmentReportIntegrityRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidateAssessmentReportIntegrityRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScopeOutput:
    boto3_raw_data: "type_defs.ScopeOutputTypeDef" = dataclasses.field()

    @cached_property
    def awsAccounts(self):  # pragma: no cover
        return AWSAccount.make_many(self.boto3_raw_data["awsAccounts"])

    @cached_property
    def awsServices(self):  # pragma: no cover
        return AWSService.make_many(self.boto3_raw_data["awsServices"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScopeOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScopeOutputTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Scope:
    boto3_raw_data: "type_defs.ScopeTypeDef" = dataclasses.field()

    @cached_property
    def awsAccounts(self):  # pragma: no cover
        return AWSAccount.make_many(self.boto3_raw_data["awsAccounts"])

    @cached_property
    def awsServices(self):  # pragma: no cover
        return AWSService.make_many(self.boto3_raw_data["awsServices"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScopeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ScopeTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentMetadataItem:
    boto3_raw_data: "type_defs.AssessmentMetadataItemTypeDef" = dataclasses.field()

    name = field("name")
    id = field("id")
    complianceType = field("complianceType")
    status = field("status")

    @cached_property
    def roles(self):  # pragma: no cover
        return Role.make_many(self.boto3_raw_data["roles"])

    @cached_property
    def delegations(self):  # pragma: no cover
        return Delegation.make_many(self.boto3_raw_data["delegations"])

    creationTime = field("creationTime")
    lastUpdated = field("lastUpdated")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssessmentMetadataItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentMetadataItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentControl:
    boto3_raw_data: "type_defs.AssessmentControlTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")
    description = field("description")
    status = field("status")
    response = field("response")

    @cached_property
    def comments(self):  # pragma: no cover
        return ControlComment.make_many(self.boto3_raw_data["comments"])

    evidenceSources = field("evidenceSources")
    evidenceCount = field("evidenceCount")
    assessmentReportEvidenceCount = field("assessmentReportEvidenceCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssessmentControlTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentControlTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchAssociateAssessmentReportEvidenceResponse:
    boto3_raw_data: (
        "type_defs.BatchAssociateAssessmentReportEvidenceResponseTypeDef"
    ) = dataclasses.field()

    evidenceIds = field("evidenceIds")

    @cached_property
    def errors(self):  # pragma: no cover
        return AssessmentReportEvidenceError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchAssociateAssessmentReportEvidenceResponseTypeDef"
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
                "type_defs.BatchAssociateAssessmentReportEvidenceResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDisassociateAssessmentReportEvidenceResponse:
    boto3_raw_data: (
        "type_defs.BatchDisassociateAssessmentReportEvidenceResponseTypeDef"
    ) = dataclasses.field()

    evidenceIds = field("evidenceIds")

    @cached_property
    def errors(self):  # pragma: no cover
        return AssessmentReportEvidenceError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDisassociateAssessmentReportEvidenceResponseTypeDef"
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
                "type_defs.BatchDisassociateAssessmentReportEvidenceResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssessmentReportResponse:
    boto3_raw_data: "type_defs.CreateAssessmentReportResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assessmentReport(self):  # pragma: no cover
        return AssessmentReport.make_one(self.boto3_raw_data["assessmentReport"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAssessmentReportResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssessmentReportResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeregisterAccountResponse:
    boto3_raw_data: "type_defs.DeregisterAccountResponseTypeDef" = dataclasses.field()

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeregisterAccountResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeregisterAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAccountStatusResponse:
    boto3_raw_data: "type_defs.GetAccountStatusResponseTypeDef" = dataclasses.field()

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAccountStatusResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAccountStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEvidenceFileUploadUrlResponse:
    boto3_raw_data: "type_defs.GetEvidenceFileUploadUrlResponseTypeDef" = (
        dataclasses.field()
    )

    evidenceFileName = field("evidenceFileName")
    uploadUrl = field("uploadUrl")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetEvidenceFileUploadUrlResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEvidenceFileUploadUrlResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEvidenceFolderResponse:
    boto3_raw_data: "type_defs.GetEvidenceFolderResponseTypeDef" = dataclasses.field()

    @cached_property
    def evidenceFolder(self):  # pragma: no cover
        return AssessmentEvidenceFolder.make_one(self.boto3_raw_data["evidenceFolder"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEvidenceFolderResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEvidenceFolderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEvidenceFoldersByAssessmentControlResponse:
    boto3_raw_data: "type_defs.GetEvidenceFoldersByAssessmentControlResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def evidenceFolders(self):  # pragma: no cover
        return AssessmentEvidenceFolder.make_many(
            self.boto3_raw_data["evidenceFolders"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEvidenceFoldersByAssessmentControlResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEvidenceFoldersByAssessmentControlResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEvidenceFoldersByAssessmentResponse:
    boto3_raw_data: "type_defs.GetEvidenceFoldersByAssessmentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def evidenceFolders(self):  # pragma: no cover
        return AssessmentEvidenceFolder.make_many(
            self.boto3_raw_data["evidenceFolders"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEvidenceFoldersByAssessmentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEvidenceFoldersByAssessmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetOrganizationAdminAccountResponse:
    boto3_raw_data: "type_defs.GetOrganizationAdminAccountResponseTypeDef" = (
        dataclasses.field()
    )

    adminAccountId = field("adminAccountId")
    organizationId = field("organizationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetOrganizationAdminAccountResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetOrganizationAdminAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssessmentFrameworkShareRequestsResponse:
    boto3_raw_data: "type_defs.ListAssessmentFrameworkShareRequestsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assessmentFrameworkShareRequests(self):  # pragma: no cover
        return AssessmentFrameworkShareRequest.make_many(
            self.boto3_raw_data["assessmentFrameworkShareRequests"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssessmentFrameworkShareRequestsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssessmentFrameworkShareRequestsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssessmentFrameworksResponse:
    boto3_raw_data: "type_defs.ListAssessmentFrameworksResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def frameworkMetadataList(self):  # pragma: no cover
        return AssessmentFrameworkMetadata.make_many(
            self.boto3_raw_data["frameworkMetadataList"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssessmentFrameworksResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssessmentFrameworksResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssessmentReportsResponse:
    boto3_raw_data: "type_defs.ListAssessmentReportsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assessmentReports(self):  # pragma: no cover
        return AssessmentReportMetadata.make_many(
            self.boto3_raw_data["assessmentReports"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListAssessmentReportsResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssessmentReportsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListKeywordsForDataSourceResponse:
    boto3_raw_data: "type_defs.ListKeywordsForDataSourceResponseTypeDef" = (
        dataclasses.field()
    )

    keywords = field("keywords")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListKeywordsForDataSourceResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListKeywordsForDataSourceResponseTypeDef"]
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
class RegisterAccountResponse:
    boto3_raw_data: "type_defs.RegisterAccountResponseTypeDef" = dataclasses.field()

    status = field("status")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegisterAccountResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegisterOrganizationAdminAccountResponse:
    boto3_raw_data: "type_defs.RegisterOrganizationAdminAccountResponseTypeDef" = (
        dataclasses.field()
    )

    adminAccountId = field("adminAccountId")
    organizationId = field("organizationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.RegisterOrganizationAdminAccountResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegisterOrganizationAdminAccountResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartAssessmentFrameworkShareResponse:
    boto3_raw_data: "type_defs.StartAssessmentFrameworkShareResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assessmentFrameworkShareRequest(self):  # pragma: no cover
        return AssessmentFrameworkShareRequest.make_one(
            self.boto3_raw_data["assessmentFrameworkShareRequest"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.StartAssessmentFrameworkShareResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartAssessmentFrameworkShareResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssessmentFrameworkShareResponse:
    boto3_raw_data: "type_defs.UpdateAssessmentFrameworkShareResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assessmentFrameworkShareRequest(self):  # pragma: no cover
        return AssessmentFrameworkShareRequest.make_one(
            self.boto3_raw_data["assessmentFrameworkShareRequest"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAssessmentFrameworkShareResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssessmentFrameworkShareResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ValidateAssessmentReportIntegrityResponse:
    boto3_raw_data: "type_defs.ValidateAssessmentReportIntegrityResponseTypeDef" = (
        dataclasses.field()
    )

    signatureValid = field("signatureValid")
    signatureAlgorithm = field("signatureAlgorithm")
    signatureDateTime = field("signatureDateTime")
    signatureKeyId = field("signatureKeyId")
    validationErrors = field("validationErrors")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ValidateAssessmentReportIntegrityResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ValidateAssessmentReportIntegrityResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateDelegationByAssessmentError:
    boto3_raw_data: "type_defs.BatchCreateDelegationByAssessmentErrorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def createDelegationRequest(self):  # pragma: no cover
        return CreateDelegationRequest.make_one(
            self.boto3_raw_data["createDelegationRequest"]
        )

    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateDelegationByAssessmentErrorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateDelegationByAssessmentErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateDelegationByAssessmentRequest:
    boto3_raw_data: "type_defs.BatchCreateDelegationByAssessmentRequestTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def createDelegationRequests(self):  # pragma: no cover
        return CreateDelegationRequest.make_many(
            self.boto3_raw_data["createDelegationRequests"]
        )

    assessmentId = field("assessmentId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateDelegationByAssessmentRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateDelegationByAssessmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchDeleteDelegationByAssessmentResponse:
    boto3_raw_data: "type_defs.BatchDeleteDelegationByAssessmentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchDeleteDelegationByAssessmentError.make_many(
            self.boto3_raw_data["errors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchDeleteDelegationByAssessmentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchDeleteDelegationByAssessmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchImportEvidenceToAssessmentControlError:
    boto3_raw_data: "type_defs.BatchImportEvidenceToAssessmentControlErrorTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def manualEvidence(self):  # pragma: no cover
        return ManualEvidence.make_one(self.boto3_raw_data["manualEvidence"])

    errorCode = field("errorCode")
    errorMessage = field("errorMessage")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchImportEvidenceToAssessmentControlErrorTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchImportEvidenceToAssessmentControlErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchImportEvidenceToAssessmentControlRequest:
    boto3_raw_data: "type_defs.BatchImportEvidenceToAssessmentControlRequestTypeDef" = (
        dataclasses.field()
    )

    assessmentId = field("assessmentId")
    controlSetId = field("controlSetId")
    controlId = field("controlId")

    @cached_property
    def manualEvidence(self):  # pragma: no cover
        return ManualEvidence.make_many(self.boto3_raw_data["manualEvidence"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchImportEvidenceToAssessmentControlRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchImportEvidenceToAssessmentControlRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetChangeLogsResponse:
    boto3_raw_data: "type_defs.GetChangeLogsResponseTypeDef" = dataclasses.field()

    @cached_property
    def changeLogs(self):  # pragma: no cover
        return ChangeLog.make_many(self.boto3_raw_data["changeLogs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetChangeLogsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetChangeLogsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ControlDomainInsights:
    boto3_raw_data: "type_defs.ControlDomainInsightsTypeDef" = dataclasses.field()

    name = field("name")
    id = field("id")
    controlsCountByNoncompliantEvidence = field("controlsCountByNoncompliantEvidence")
    totalControlsCount = field("totalControlsCount")

    @cached_property
    def evidenceInsights(self):  # pragma: no cover
        return EvidenceInsights.make_one(self.boto3_raw_data["evidenceInsights"])

    lastUpdated = field("lastUpdated")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ControlDomainInsightsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ControlDomainInsightsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ControlInsightsMetadataByAssessmentItem:
    boto3_raw_data: "type_defs.ControlInsightsMetadataByAssessmentItemTypeDef" = (
        dataclasses.field()
    )

    name = field("name")
    id = field("id")

    @cached_property
    def evidenceInsights(self):  # pragma: no cover
        return EvidenceInsights.make_one(self.boto3_raw_data["evidenceInsights"])

    controlSetName = field("controlSetName")
    lastUpdated = field("lastUpdated")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ControlInsightsMetadataByAssessmentItemTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ControlInsightsMetadataByAssessmentItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ControlInsightsMetadataItem:
    boto3_raw_data: "type_defs.ControlInsightsMetadataItemTypeDef" = dataclasses.field()

    name = field("name")
    id = field("id")

    @cached_property
    def evidenceInsights(self):  # pragma: no cover
        return EvidenceInsights.make_one(self.boto3_raw_data["evidenceInsights"])

    lastUpdated = field("lastUpdated")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ControlInsightsMetadataItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ControlInsightsMetadataItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ControlMappingSource:
    boto3_raw_data: "type_defs.ControlMappingSourceTypeDef" = dataclasses.field()

    sourceId = field("sourceId")
    sourceName = field("sourceName")
    sourceDescription = field("sourceDescription")
    sourceSetUpOption = field("sourceSetUpOption")
    sourceType = field("sourceType")

    @cached_property
    def sourceKeyword(self):  # pragma: no cover
        return SourceKeyword.make_one(self.boto3_raw_data["sourceKeyword"])

    sourceFrequency = field("sourceFrequency")
    troubleshootingText = field("troubleshootingText")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ControlMappingSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ControlMappingSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateControlMappingSource:
    boto3_raw_data: "type_defs.CreateControlMappingSourceTypeDef" = dataclasses.field()

    sourceName = field("sourceName")
    sourceDescription = field("sourceDescription")
    sourceSetUpOption = field("sourceSetUpOption")
    sourceType = field("sourceType")

    @cached_property
    def sourceKeyword(self):  # pragma: no cover
        return SourceKeyword.make_one(self.boto3_raw_data["sourceKeyword"])

    sourceFrequency = field("sourceFrequency")
    troubleshootingText = field("troubleshootingText")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateControlMappingSourceTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateControlMappingSourceTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListControlsResponse:
    boto3_raw_data: "type_defs.ListControlsResponseTypeDef" = dataclasses.field()

    @cached_property
    def controlMetadataList(self):  # pragma: no cover
        return ControlMetadata.make_many(self.boto3_raw_data["controlMetadataList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListControlsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListControlsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssessmentFrameworkControlSet:
    boto3_raw_data: "type_defs.CreateAssessmentFrameworkControlSetTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def controls(self):  # pragma: no cover
        return CreateAssessmentFrameworkControl.make_many(
            self.boto3_raw_data["controls"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAssessmentFrameworkControlSetTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssessmentFrameworkControlSetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssessmentFrameworkControlSet:
    boto3_raw_data: "type_defs.UpdateAssessmentFrameworkControlSetTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def controls(self):  # pragma: no cover
        return CreateAssessmentFrameworkControl.make_many(
            self.boto3_raw_data["controls"]
        )

    id = field("id")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAssessmentFrameworkControlSetTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssessmentFrameworkControlSetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDelegationsResponse:
    boto3_raw_data: "type_defs.GetDelegationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def delegations(self):  # pragma: no cover
        return DelegationMetadata.make_many(self.boto3_raw_data["delegations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetDelegationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDelegationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSettingsRequest:
    boto3_raw_data: "type_defs.UpdateSettingsRequestTypeDef" = dataclasses.field()

    snsTopic = field("snsTopic")

    @cached_property
    def defaultAssessmentReportsDestination(self):  # pragma: no cover
        return AssessmentReportsDestination.make_one(
            self.boto3_raw_data["defaultAssessmentReportsDestination"]
        )

    @cached_property
    def defaultProcessOwners(self):  # pragma: no cover
        return Role.make_many(self.boto3_raw_data["defaultProcessOwners"])

    kmsKey = field("kmsKey")
    evidenceFinderEnabled = field("evidenceFinderEnabled")

    @cached_property
    def deregistrationPolicy(self):  # pragma: no cover
        return DeregistrationPolicy.make_one(
            self.boto3_raw_data["deregistrationPolicy"]
        )

    @cached_property
    def defaultExportDestination(self):  # pragma: no cover
        return DefaultExportDestination.make_one(
            self.boto3_raw_data["defaultExportDestination"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSettingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSettingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Settings:
    boto3_raw_data: "type_defs.SettingsTypeDef" = dataclasses.field()

    isAwsOrgEnabled = field("isAwsOrgEnabled")
    snsTopic = field("snsTopic")

    @cached_property
    def defaultAssessmentReportsDestination(self):  # pragma: no cover
        return AssessmentReportsDestination.make_one(
            self.boto3_raw_data["defaultAssessmentReportsDestination"]
        )

    @cached_property
    def defaultProcessOwners(self):  # pragma: no cover
        return Role.make_many(self.boto3_raw_data["defaultProcessOwners"])

    kmsKey = field("kmsKey")

    @cached_property
    def evidenceFinderEnablement(self):  # pragma: no cover
        return EvidenceFinderEnablement.make_one(
            self.boto3_raw_data["evidenceFinderEnablement"]
        )

    @cached_property
    def deregistrationPolicy(self):  # pragma: no cover
        return DeregistrationPolicy.make_one(
            self.boto3_raw_data["deregistrationPolicy"]
        )

    @cached_property
    def defaultExportDestination(self):  # pragma: no cover
        return DefaultExportDestination.make_one(
            self.boto3_raw_data["defaultExportDestination"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SettingsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SettingsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Evidence:
    boto3_raw_data: "type_defs.EvidenceTypeDef" = dataclasses.field()

    dataSource = field("dataSource")
    evidenceAwsAccountId = field("evidenceAwsAccountId")
    time = field("time")
    eventSource = field("eventSource")
    eventName = field("eventName")
    evidenceByType = field("evidenceByType")

    @cached_property
    def resourcesIncluded(self):  # pragma: no cover
        return Resource.make_many(self.boto3_raw_data["resourcesIncluded"])

    attributes = field("attributes")
    iamId = field("iamId")
    complianceCheck = field("complianceCheck")
    awsOrganization = field("awsOrganization")
    awsAccountId = field("awsAccountId")
    evidenceFolderId = field("evidenceFolderId")
    id = field("id")
    assessmentReportSelection = field("assessmentReportSelection")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EvidenceTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.EvidenceTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssessmentReportUrlResponse:
    boto3_raw_data: "type_defs.GetAssessmentReportUrlResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def preSignedUrl(self):  # pragma: no cover
        return URL.make_one(self.boto3_raw_data["preSignedUrl"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAssessmentReportUrlResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssessmentReportUrlResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInsightsByAssessmentResponse:
    boto3_raw_data: "type_defs.GetInsightsByAssessmentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def insights(self):  # pragma: no cover
        return InsightsByAssessment.make_one(self.boto3_raw_data["insights"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetInsightsByAssessmentResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInsightsByAssessmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInsightsResponse:
    boto3_raw_data: "type_defs.GetInsightsResponseTypeDef" = dataclasses.field()

    @cached_property
    def insights(self):  # pragma: no cover
        return Insights.make_one(self.boto3_raw_data["insights"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInsightsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInsightsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetServicesInScopeResponse:
    boto3_raw_data: "type_defs.GetServicesInScopeResponseTypeDef" = dataclasses.field()

    @cached_property
    def serviceMetadata(self):  # pragma: no cover
        return ServiceMetadata.make_many(self.boto3_raw_data["serviceMetadata"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetServicesInScopeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetServicesInScopeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListNotificationsResponse:
    boto3_raw_data: "type_defs.ListNotificationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def notifications(self):  # pragma: no cover
        return Notification.make_many(self.boto3_raw_data["notifications"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListNotificationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListNotificationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentMetadata:
    boto3_raw_data: "type_defs.AssessmentMetadataTypeDef" = dataclasses.field()

    name = field("name")
    id = field("id")
    description = field("description")
    complianceType = field("complianceType")
    status = field("status")

    @cached_property
    def assessmentReportsDestination(self):  # pragma: no cover
        return AssessmentReportsDestination.make_one(
            self.boto3_raw_data["assessmentReportsDestination"]
        )

    @cached_property
    def scope(self):  # pragma: no cover
        return ScopeOutput.make_one(self.boto3_raw_data["scope"])

    @cached_property
    def roles(self):  # pragma: no cover
        return Role.make_many(self.boto3_raw_data["roles"])

    @cached_property
    def delegations(self):  # pragma: no cover
        return Delegation.make_many(self.boto3_raw_data["delegations"])

    creationTime = field("creationTime")
    lastUpdated = field("lastUpdated")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssessmentMetadataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentMetadataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssessmentsResponse:
    boto3_raw_data: "type_defs.ListAssessmentsResponseTypeDef" = dataclasses.field()

    @cached_property
    def assessmentMetadata(self):  # pragma: no cover
        return AssessmentMetadataItem.make_many(
            self.boto3_raw_data["assessmentMetadata"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListAssessmentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListAssessmentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentControlSet:
    boto3_raw_data: "type_defs.AssessmentControlSetTypeDef" = dataclasses.field()

    id = field("id")
    description = field("description")
    status = field("status")

    @cached_property
    def roles(self):  # pragma: no cover
        return Role.make_many(self.boto3_raw_data["roles"])

    @cached_property
    def controls(self):  # pragma: no cover
        return AssessmentControl.make_many(self.boto3_raw_data["controls"])

    @cached_property
    def delegations(self):  # pragma: no cover
        return Delegation.make_many(self.boto3_raw_data["delegations"])

    systemEvidenceCount = field("systemEvidenceCount")
    manualEvidenceCount = field("manualEvidenceCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssessmentControlSetTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentControlSetTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssessmentControlResponse:
    boto3_raw_data: "type_defs.UpdateAssessmentControlResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def control(self):  # pragma: no cover
        return AssessmentControl.make_one(self.boto3_raw_data["control"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAssessmentControlResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssessmentControlResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchCreateDelegationByAssessmentResponse:
    boto3_raw_data: "type_defs.BatchCreateDelegationByAssessmentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def delegations(self):  # pragma: no cover
        return Delegation.make_many(self.boto3_raw_data["delegations"])

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchCreateDelegationByAssessmentError.make_many(
            self.boto3_raw_data["errors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchCreateDelegationByAssessmentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchCreateDelegationByAssessmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchImportEvidenceToAssessmentControlResponse:
    boto3_raw_data: (
        "type_defs.BatchImportEvidenceToAssessmentControlResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def errors(self):  # pragma: no cover
        return BatchImportEvidenceToAssessmentControlError.make_many(
            self.boto3_raw_data["errors"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchImportEvidenceToAssessmentControlResponseTypeDef"
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
                "type_defs.BatchImportEvidenceToAssessmentControlResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListControlDomainInsightsByAssessmentResponse:
    boto3_raw_data: "type_defs.ListControlDomainInsightsByAssessmentResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def controlDomainInsights(self):  # pragma: no cover
        return ControlDomainInsights.make_many(
            self.boto3_raw_data["controlDomainInsights"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListControlDomainInsightsByAssessmentResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListControlDomainInsightsByAssessmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListControlDomainInsightsResponse:
    boto3_raw_data: "type_defs.ListControlDomainInsightsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def controlDomainInsights(self):  # pragma: no cover
        return ControlDomainInsights.make_many(
            self.boto3_raw_data["controlDomainInsights"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListControlDomainInsightsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListControlDomainInsightsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListAssessmentControlInsightsByControlDomainResponse:
    boto3_raw_data: (
        "type_defs.ListAssessmentControlInsightsByControlDomainResponseTypeDef"
    ) = dataclasses.field()

    @cached_property
    def controlInsightsByAssessment(self):  # pragma: no cover
        return ControlInsightsMetadataByAssessmentItem.make_many(
            self.boto3_raw_data["controlInsightsByAssessment"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListAssessmentControlInsightsByControlDomainResponseTypeDef"
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
                "type_defs.ListAssessmentControlInsightsByControlDomainResponseTypeDef"
            ]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListControlInsightsByControlDomainResponse:
    boto3_raw_data: "type_defs.ListControlInsightsByControlDomainResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def controlInsightsMetadata(self):  # pragma: no cover
        return ControlInsightsMetadataItem.make_many(
            self.boto3_raw_data["controlInsightsMetadata"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListControlInsightsByControlDomainResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListControlInsightsByControlDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Control:
    boto3_raw_data: "type_defs.ControlTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")
    type = field("type")
    name = field("name")
    description = field("description")
    testingInformation = field("testingInformation")
    actionPlanTitle = field("actionPlanTitle")
    actionPlanInstructions = field("actionPlanInstructions")
    controlSources = field("controlSources")

    @cached_property
    def controlMappingSources(self):  # pragma: no cover
        return ControlMappingSource.make_many(
            self.boto3_raw_data["controlMappingSources"]
        )

    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    createdBy = field("createdBy")
    lastUpdatedBy = field("lastUpdatedBy")
    tags = field("tags")
    state = field("state")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ControlTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ControlTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateControlRequest:
    boto3_raw_data: "type_defs.UpdateControlRequestTypeDef" = dataclasses.field()

    controlId = field("controlId")
    name = field("name")

    @cached_property
    def controlMappingSources(self):  # pragma: no cover
        return ControlMappingSource.make_many(
            self.boto3_raw_data["controlMappingSources"]
        )

    description = field("description")
    testingInformation = field("testingInformation")
    actionPlanTitle = field("actionPlanTitle")
    actionPlanInstructions = field("actionPlanInstructions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateControlRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateControlRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateControlRequest:
    boto3_raw_data: "type_defs.CreateControlRequestTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def controlMappingSources(self):  # pragma: no cover
        return CreateControlMappingSource.make_many(
            self.boto3_raw_data["controlMappingSources"]
        )

    description = field("description")
    testingInformation = field("testingInformation")
    actionPlanTitle = field("actionPlanTitle")
    actionPlanInstructions = field("actionPlanInstructions")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateControlRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateControlRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssessmentFrameworkRequest:
    boto3_raw_data: "type_defs.CreateAssessmentFrameworkRequestTypeDef" = (
        dataclasses.field()
    )

    name = field("name")

    @cached_property
    def controlSets(self):  # pragma: no cover
        return CreateAssessmentFrameworkControlSet.make_many(
            self.boto3_raw_data["controlSets"]
        )

    description = field("description")
    complianceType = field("complianceType")
    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.CreateAssessmentFrameworkRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssessmentFrameworkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssessmentFrameworkRequest:
    boto3_raw_data: "type_defs.UpdateAssessmentFrameworkRequestTypeDef" = (
        dataclasses.field()
    )

    frameworkId = field("frameworkId")
    name = field("name")

    @cached_property
    def controlSets(self):  # pragma: no cover
        return UpdateAssessmentFrameworkControlSet.make_many(
            self.boto3_raw_data["controlSets"]
        )

    description = field("description")
    complianceType = field("complianceType")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAssessmentFrameworkRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssessmentFrameworkRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetSettingsResponse:
    boto3_raw_data: "type_defs.GetSettingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def settings(self):  # pragma: no cover
        return Settings.make_one(self.boto3_raw_data["settings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateSettingsResponse:
    boto3_raw_data: "type_defs.UpdateSettingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def settings(self):  # pragma: no cover
        return Settings.make_one(self.boto3_raw_data["settings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateSettingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateSettingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEvidenceByEvidenceFolderResponse:
    boto3_raw_data: "type_defs.GetEvidenceByEvidenceFolderResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def evidence(self):  # pragma: no cover
        return Evidence.make_many(self.boto3_raw_data["evidence"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetEvidenceByEvidenceFolderResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEvidenceByEvidenceFolderResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetEvidenceResponse:
    boto3_raw_data: "type_defs.GetEvidenceResponseTypeDef" = dataclasses.field()

    @cached_property
    def evidence(self):  # pragma: no cover
        return Evidence.make_one(self.boto3_raw_data["evidence"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetEvidenceResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetEvidenceResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssessmentRequest:
    boto3_raw_data: "type_defs.CreateAssessmentRequestTypeDef" = dataclasses.field()

    name = field("name")

    @cached_property
    def assessmentReportsDestination(self):  # pragma: no cover
        return AssessmentReportsDestination.make_one(
            self.boto3_raw_data["assessmentReportsDestination"]
        )

    scope = field("scope")

    @cached_property
    def roles(self):  # pragma: no cover
        return Role.make_many(self.boto3_raw_data["roles"])

    frameworkId = field("frameworkId")
    description = field("description")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAssessmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssessmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssessmentRequest:
    boto3_raw_data: "type_defs.UpdateAssessmentRequestTypeDef" = dataclasses.field()

    assessmentId = field("assessmentId")
    scope = field("scope")
    assessmentName = field("assessmentName")
    assessmentDescription = field("assessmentDescription")

    @cached_property
    def assessmentReportsDestination(self):  # pragma: no cover
        return AssessmentReportsDestination.make_one(
            self.boto3_raw_data["assessmentReportsDestination"]
        )

    @cached_property
    def roles(self):  # pragma: no cover
        return Role.make_many(self.boto3_raw_data["roles"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAssessmentRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssessmentRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssessmentFramework:
    boto3_raw_data: "type_defs.AssessmentFrameworkTypeDef" = dataclasses.field()

    id = field("id")
    arn = field("arn")

    @cached_property
    def metadata(self):  # pragma: no cover
        return FrameworkMetadata.make_one(self.boto3_raw_data["metadata"])

    @cached_property
    def controlSets(self):  # pragma: no cover
        return AssessmentControlSet.make_many(self.boto3_raw_data["controlSets"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssessmentFrameworkTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssessmentFrameworkTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssessmentControlSetStatusResponse:
    boto3_raw_data: "type_defs.UpdateAssessmentControlSetStatusResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def controlSet(self):  # pragma: no cover
        return AssessmentControlSet.make_one(self.boto3_raw_data["controlSet"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAssessmentControlSetStatusResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssessmentControlSetStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ControlSet:
    boto3_raw_data: "type_defs.ControlSetTypeDef" = dataclasses.field()

    id = field("id")
    name = field("name")

    @cached_property
    def controls(self):  # pragma: no cover
        return Control.make_many(self.boto3_raw_data["controls"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ControlSetTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ControlSetTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateControlResponse:
    boto3_raw_data: "type_defs.CreateControlResponseTypeDef" = dataclasses.field()

    @cached_property
    def control(self):  # pragma: no cover
        return Control.make_one(self.boto3_raw_data["control"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateControlResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateControlResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetControlResponse:
    boto3_raw_data: "type_defs.GetControlResponseTypeDef" = dataclasses.field()

    @cached_property
    def control(self):  # pragma: no cover
        return Control.make_one(self.boto3_raw_data["control"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetControlResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetControlResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateControlResponse:
    boto3_raw_data: "type_defs.UpdateControlResponseTypeDef" = dataclasses.field()

    @cached_property
    def control(self):  # pragma: no cover
        return Control.make_one(self.boto3_raw_data["control"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateControlResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateControlResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Assessment:
    boto3_raw_data: "type_defs.AssessmentTypeDef" = dataclasses.field()

    arn = field("arn")

    @cached_property
    def awsAccount(self):  # pragma: no cover
        return AWSAccount.make_one(self.boto3_raw_data["awsAccount"])

    @cached_property
    def metadata(self):  # pragma: no cover
        return AssessmentMetadata.make_one(self.boto3_raw_data["metadata"])

    @cached_property
    def framework(self):  # pragma: no cover
        return AssessmentFramework.make_one(self.boto3_raw_data["framework"])

    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AssessmentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AssessmentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Framework:
    boto3_raw_data: "type_defs.FrameworkTypeDef" = dataclasses.field()

    arn = field("arn")
    id = field("id")
    name = field("name")
    type = field("type")
    complianceType = field("complianceType")
    description = field("description")
    logo = field("logo")
    controlSources = field("controlSources")

    @cached_property
    def controlSets(self):  # pragma: no cover
        return ControlSet.make_many(self.boto3_raw_data["controlSets"])

    createdAt = field("createdAt")
    lastUpdatedAt = field("lastUpdatedAt")
    createdBy = field("createdBy")
    lastUpdatedBy = field("lastUpdatedBy")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FrameworkTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FrameworkTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssessmentResponse:
    boto3_raw_data: "type_defs.CreateAssessmentResponseTypeDef" = dataclasses.field()

    @cached_property
    def assessment(self):  # pragma: no cover
        return Assessment.make_one(self.boto3_raw_data["assessment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateAssessmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssessmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssessmentResponse:
    boto3_raw_data: "type_defs.GetAssessmentResponseTypeDef" = dataclasses.field()

    @cached_property
    def assessment(self):  # pragma: no cover
        return Assessment.make_one(self.boto3_raw_data["assessment"])

    @cached_property
    def userRole(self):  # pragma: no cover
        return Role.make_one(self.boto3_raw_data["userRole"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetAssessmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssessmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssessmentResponse:
    boto3_raw_data: "type_defs.UpdateAssessmentResponseTypeDef" = dataclasses.field()

    @cached_property
    def assessment(self):  # pragma: no cover
        return Assessment.make_one(self.boto3_raw_data["assessment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateAssessmentResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssessmentResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssessmentStatusResponse:
    boto3_raw_data: "type_defs.UpdateAssessmentStatusResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def assessment(self):  # pragma: no cover
        return Assessment.make_one(self.boto3_raw_data["assessment"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAssessmentStatusResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssessmentStatusResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateAssessmentFrameworkResponse:
    boto3_raw_data: "type_defs.CreateAssessmentFrameworkResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def framework(self):  # pragma: no cover
        return Framework.make_one(self.boto3_raw_data["framework"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.CreateAssessmentFrameworkResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateAssessmentFrameworkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetAssessmentFrameworkResponse:
    boto3_raw_data: "type_defs.GetAssessmentFrameworkResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def framework(self):  # pragma: no cover
        return Framework.make_one(self.boto3_raw_data["framework"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetAssessmentFrameworkResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetAssessmentFrameworkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAssessmentFrameworkResponse:
    boto3_raw_data: "type_defs.UpdateAssessmentFrameworkResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def framework(self):  # pragma: no cover
        return Framework.make_one(self.boto3_raw_data["framework"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAssessmentFrameworkResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAssessmentFrameworkResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
