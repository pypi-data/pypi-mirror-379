# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_connectcases import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AuditEventFieldValueUnion:
    boto3_raw_data: "type_defs.AuditEventFieldValueUnionTypeDef" = dataclasses.field()

    booleanValue = field("booleanValue")
    doubleValue = field("doubleValue")
    emptyValue = field("emptyValue")
    stringValue = field("stringValue")
    userArnValue = field("userArnValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuditEventFieldValueUnionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuditEventFieldValueUnionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UserUnion:
    boto3_raw_data: "type_defs.UserUnionTypeDef" = dataclasses.field()

    customEntity = field("customEntity")
    userArn = field("userArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UserUnionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.UserUnionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaseRuleIdentifier:
    boto3_raw_data: "type_defs.CaseRuleIdentifierTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CaseRuleIdentifierTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CaseRuleIdentifierTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaseRuleError:
    boto3_raw_data: "type_defs.CaseRuleErrorTypeDef" = dataclasses.field()

    errorCode = field("errorCode")
    id = field("id")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CaseRuleErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CaseRuleErrorTypeDef"]],
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
class FieldIdentifier:
    boto3_raw_data: "type_defs.FieldIdentifierTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldIdentifierTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FieldIdentifierTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldError:
    boto3_raw_data: "type_defs.FieldErrorTypeDef" = dataclasses.field()

    errorCode = field("errorCode")
    id = field("id")
    message = field("message")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FieldErrorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetFieldResponse:
    boto3_raw_data: "type_defs.GetFieldResponseTypeDef" = dataclasses.field()

    fieldArn = field("fieldArn")
    fieldId = field("fieldId")
    name = field("name")
    namespace = field("namespace")
    type = field("type")
    createdTime = field("createdTime")
    deleted = field("deleted")
    description = field("description")
    lastModifiedTime = field("lastModifiedTime")
    tags = field("tags")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetFieldResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetFieldResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldOption:
    boto3_raw_data: "type_defs.FieldOptionTypeDef" = dataclasses.field()

    active = field("active")
    name = field("name")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldOptionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FieldOptionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldOptionError:
    boto3_raw_data: "type_defs.FieldOptionErrorTypeDef" = dataclasses.field()

    errorCode = field("errorCode")
    message = field("message")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldOptionErrorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldOptionErrorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OperandOne:
    boto3_raw_data: "type_defs.OperandOneTypeDef" = dataclasses.field()

    fieldId = field("fieldId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OperandOneTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OperandOneTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OperandTwoOutput:
    boto3_raw_data: "type_defs.OperandTwoOutputTypeDef" = dataclasses.field()

    booleanValue = field("booleanValue")
    doubleValue = field("doubleValue")
    emptyValue = field("emptyValue")
    stringValue = field("stringValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OperandTwoOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.OperandTwoOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class OperandTwo:
    boto3_raw_data: "type_defs.OperandTwoTypeDef" = dataclasses.field()

    booleanValue = field("booleanValue")
    doubleValue = field("doubleValue")
    emptyValue = field("emptyValue")
    stringValue = field("stringValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OperandTwoTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OperandTwoTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaseRuleSummary:
    boto3_raw_data: "type_defs.CaseRuleSummaryTypeDef" = dataclasses.field()

    caseRuleArn = field("caseRuleArn")
    caseRuleId = field("caseRuleId")
    name = field("name")
    ruleType = field("ruleType")
    description = field("description")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CaseRuleSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CaseRuleSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaseSummary:
    boto3_raw_data: "type_defs.CaseSummaryTypeDef" = dataclasses.field()

    caseId = field("caseId")
    templateId = field("templateId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CaseSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CaseSummaryTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommentContent:
    boto3_raw_data: "type_defs.CommentContentTypeDef" = dataclasses.field()

    body = field("body")
    contentType = field("contentType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CommentContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CommentContentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactContent:
    boto3_raw_data: "type_defs.ContactContentTypeDef" = dataclasses.field()

    channel = field("channel")
    connectedToSystemTime = field("connectedToSystemTime")
    contactArn = field("contactArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContactContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContactContentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ContactFilter:
    boto3_raw_data: "type_defs.ContactFilterTypeDef" = dataclasses.field()

    channel = field("channel")
    contactArn = field("contactArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContactFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContactFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Contact:
    boto3_raw_data: "type_defs.ContactTypeDef" = dataclasses.field()

    contactArn = field("contactArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ContactTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ContactTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainRequest:
    boto3_raw_data: "type_defs.CreateDomainRequestTypeDef" = dataclasses.field()

    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFieldRequest:
    boto3_raw_data: "type_defs.CreateFieldRequestTypeDef" = dataclasses.field()

    domainId = field("domainId")
    name = field("name")
    type = field("type")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFieldRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFieldRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LayoutConfiguration:
    boto3_raw_data: "type_defs.LayoutConfigurationTypeDef" = dataclasses.field()

    defaultLayout = field("defaultLayout")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LayoutConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LayoutConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequiredField:
    boto3_raw_data: "type_defs.RequiredFieldTypeDef" = dataclasses.field()

    fieldId = field("fieldId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RequiredFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.RequiredFieldTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TemplateRule:
    boto3_raw_data: "type_defs.TemplateRuleTypeDef" = dataclasses.field()

    caseRuleId = field("caseRuleId")
    fieldId = field("fieldId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TemplateRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TemplateRuleTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCaseRequest:
    boto3_raw_data: "type_defs.DeleteCaseRequestTypeDef" = dataclasses.field()

    caseId = field("caseId")
    domainId = field("domainId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DeleteCaseRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteCaseRuleRequest:
    boto3_raw_data: "type_defs.DeleteCaseRuleRequestTypeDef" = dataclasses.field()

    caseRuleId = field("caseRuleId")
    domainId = field("domainId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteCaseRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteCaseRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteDomainRequest:
    boto3_raw_data: "type_defs.DeleteDomainRequestTypeDef" = dataclasses.field()

    domainId = field("domainId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDomainRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteFieldRequest:
    boto3_raw_data: "type_defs.DeleteFieldRequestTypeDef" = dataclasses.field()

    domainId = field("domainId")
    fieldId = field("fieldId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteFieldRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteFieldRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteLayoutRequest:
    boto3_raw_data: "type_defs.DeleteLayoutRequestTypeDef" = dataclasses.field()

    domainId = field("domainId")
    layoutId = field("layoutId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteLayoutRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteLayoutRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteRelatedItemRequest:
    boto3_raw_data: "type_defs.DeleteRelatedItemRequestTypeDef" = dataclasses.field()

    caseId = field("caseId")
    domainId = field("domainId")
    relatedItemId = field("relatedItemId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteRelatedItemRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteRelatedItemRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteTemplateRequest:
    boto3_raw_data: "type_defs.DeleteTemplateRequestTypeDef" = dataclasses.field()

    domainId = field("domainId")
    templateId = field("templateId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainSummary:
    boto3_raw_data: "type_defs.DomainSummaryTypeDef" = dataclasses.field()

    domainArn = field("domainArn")
    domainId = field("domainId")
    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelatedItemEventIncludedData:
    boto3_raw_data: "type_defs.RelatedItemEventIncludedDataTypeDef" = (
        dataclasses.field()
    )

    includeContent = field("includeContent")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RelatedItemEventIncludedDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelatedItemEventIncludedDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldItem:
    boto3_raw_data: "type_defs.FieldItemTypeDef" = dataclasses.field()

    id = field("id")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldItemTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FieldItemTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldSummary:
    boto3_raw_data: "type_defs.FieldSummaryTypeDef" = dataclasses.field()

    fieldArn = field("fieldArn")
    fieldId = field("fieldId")
    name = field("name")
    namespace = field("namespace")
    type = field("type")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FieldSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldValueUnionOutput:
    boto3_raw_data: "type_defs.FieldValueUnionOutputTypeDef" = dataclasses.field()

    booleanValue = field("booleanValue")
    doubleValue = field("doubleValue")
    emptyValue = field("emptyValue")
    stringValue = field("stringValue")
    userArnValue = field("userArnValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FieldValueUnionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldValueUnionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldValueUnion:
    boto3_raw_data: "type_defs.FieldValueUnionTypeDef" = dataclasses.field()

    booleanValue = field("booleanValue")
    doubleValue = field("doubleValue")
    emptyValue = field("emptyValue")
    stringValue = field("stringValue")
    userArnValue = field("userArnValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldValueUnionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FieldValueUnionTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileContent:
    boto3_raw_data: "type_defs.FileContentTypeDef" = dataclasses.field()

    fileArn = field("fileArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FileContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FileContentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FileFilter:
    boto3_raw_data: "type_defs.FileFilterTypeDef" = dataclasses.field()

    fileArn = field("fileArn")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FileFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FileFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCaseAuditEventsRequest:
    boto3_raw_data: "type_defs.GetCaseAuditEventsRequestTypeDef" = dataclasses.field()

    caseId = field("caseId")
    domainId = field("domainId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCaseAuditEventsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCaseAuditEventsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCaseEventConfigurationRequest:
    boto3_raw_data: "type_defs.GetCaseEventConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    domainId = field("domainId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.GetCaseEventConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCaseEventConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetDomainRequest:
    boto3_raw_data: "type_defs.GetDomainRequestTypeDef" = dataclasses.field()

    domainId = field("domainId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDomainRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLayoutRequest:
    boto3_raw_data: "type_defs.GetLayoutRequestTypeDef" = dataclasses.field()

    domainId = field("domainId")
    layoutId = field("layoutId")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetLayoutRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLayoutRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTemplateRequest:
    boto3_raw_data: "type_defs.GetTemplateRequestTypeDef" = dataclasses.field()

    domainId = field("domainId")
    templateId = field("templateId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LayoutSummary:
    boto3_raw_data: "type_defs.LayoutSummaryTypeDef" = dataclasses.field()

    layoutArn = field("layoutArn")
    layoutId = field("layoutId")
    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LayoutSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LayoutSummaryTypeDef"]],
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
class ListCaseRulesRequest:
    boto3_raw_data: "type_defs.ListCaseRulesRequestTypeDef" = dataclasses.field()

    domainId = field("domainId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCaseRulesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCaseRulesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCasesForContactRequest:
    boto3_raw_data: "type_defs.ListCasesForContactRequestTypeDef" = dataclasses.field()

    contactArn = field("contactArn")
    domainId = field("domainId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCasesForContactRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCasesForContactRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainsRequest:
    boto3_raw_data: "type_defs.ListDomainsRequestTypeDef" = dataclasses.field()

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFieldOptionsRequest:
    boto3_raw_data: "type_defs.ListFieldOptionsRequestTypeDef" = dataclasses.field()

    domainId = field("domainId")
    fieldId = field("fieldId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    values = field("values")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFieldOptionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFieldOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFieldsRequest:
    boto3_raw_data: "type_defs.ListFieldsRequestTypeDef" = dataclasses.field()

    domainId = field("domainId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListFieldsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFieldsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLayoutsRequest:
    boto3_raw_data: "type_defs.ListLayoutsRequestTypeDef" = dataclasses.field()

    domainId = field("domainId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLayoutsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLayoutsRequestTypeDef"]
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

    arn = field("arn")

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
class ListTemplatesRequest:
    boto3_raw_data: "type_defs.ListTemplatesRequestTypeDef" = dataclasses.field()

    domainId = field("domainId")
    maxResults = field("maxResults")
    nextToken = field("nextToken")
    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTemplatesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTemplatesRequestTypeDef"]
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

    name = field("name")
    status = field("status")
    templateArn = field("templateArn")
    templateId = field("templateId")

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
class SlaFilter:
    boto3_raw_data: "type_defs.SlaFilterTypeDef" = dataclasses.field()

    name = field("name")
    status = field("status")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SlaFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SlaFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Sort:
    boto3_raw_data: "type_defs.SortTypeDef" = dataclasses.field()

    fieldId = field("fieldId")
    sortOrder = field("sortOrder")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SortTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SortTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TagResourceRequest:
    boto3_raw_data: "type_defs.TagResourceRequestTypeDef" = dataclasses.field()

    arn = field("arn")
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

    arn = field("arn")
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
class UpdateFieldRequest:
    boto3_raw_data: "type_defs.UpdateFieldRequestTypeDef" = dataclasses.field()

    domainId = field("domainId")
    fieldId = field("fieldId")
    description = field("description")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateFieldRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateFieldRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuditEventField:
    boto3_raw_data: "type_defs.AuditEventFieldTypeDef" = dataclasses.field()

    eventFieldId = field("eventFieldId")

    @cached_property
    def newValue(self):  # pragma: no cover
        return AuditEventFieldValueUnion.make_one(self.boto3_raw_data["newValue"])

    @cached_property
    def oldValue(self):  # pragma: no cover
        return AuditEventFieldValueUnion.make_one(self.boto3_raw_data["oldValue"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AuditEventFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AuditEventFieldTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuditEventPerformedBy:
    boto3_raw_data: "type_defs.AuditEventPerformedByTypeDef" = dataclasses.field()

    iamPrincipalArn = field("iamPrincipalArn")

    @cached_property
    def user(self):  # pragma: no cover
        return UserUnion.make_one(self.boto3_raw_data["user"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AuditEventPerformedByTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AuditEventPerformedByTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetCaseRuleRequest:
    boto3_raw_data: "type_defs.BatchGetCaseRuleRequestTypeDef" = dataclasses.field()

    @cached_property
    def caseRules(self):  # pragma: no cover
        return CaseRuleIdentifier.make_many(self.boto3_raw_data["caseRules"])

    domainId = field("domainId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetCaseRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetCaseRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCaseResponse:
    boto3_raw_data: "type_defs.CreateCaseResponseTypeDef" = dataclasses.field()

    caseArn = field("caseArn")
    caseId = field("caseId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCaseResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCaseResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCaseRuleResponse:
    boto3_raw_data: "type_defs.CreateCaseRuleResponseTypeDef" = dataclasses.field()

    caseRuleArn = field("caseRuleArn")
    caseRuleId = field("caseRuleId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCaseRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCaseRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateDomainResponse:
    boto3_raw_data: "type_defs.CreateDomainResponseTypeDef" = dataclasses.field()

    domainArn = field("domainArn")
    domainId = field("domainId")
    domainStatus = field("domainStatus")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateDomainResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateFieldResponse:
    boto3_raw_data: "type_defs.CreateFieldResponseTypeDef" = dataclasses.field()

    fieldArn = field("fieldArn")
    fieldId = field("fieldId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateFieldResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateFieldResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLayoutResponse:
    boto3_raw_data: "type_defs.CreateLayoutResponseTypeDef" = dataclasses.field()

    layoutArn = field("layoutArn")
    layoutId = field("layoutId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLayoutResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLayoutResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRelatedItemResponse:
    boto3_raw_data: "type_defs.CreateRelatedItemResponseTypeDef" = dataclasses.field()

    relatedItemArn = field("relatedItemArn")
    relatedItemId = field("relatedItemId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRelatedItemResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRelatedItemResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTemplateResponse:
    boto3_raw_data: "type_defs.CreateTemplateResponseTypeDef" = dataclasses.field()

    templateArn = field("templateArn")
    templateId = field("templateId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTemplateResponseTypeDef"]
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
class GetDomainResponse:
    boto3_raw_data: "type_defs.GetDomainResponseTypeDef" = dataclasses.field()

    createdTime = field("createdTime")
    domainArn = field("domainArn")
    domainId = field("domainId")
    domainStatus = field("domainStatus")
    name = field("name")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetDomainResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetDomainResponseTypeDef"]
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
class BatchGetFieldRequest:
    boto3_raw_data: "type_defs.BatchGetFieldRequestTypeDef" = dataclasses.field()

    domainId = field("domainId")

    @cached_property
    def fields(self):  # pragma: no cover
        return FieldIdentifier.make_many(self.boto3_raw_data["fields"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetFieldRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetFieldRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaseEventIncludedDataOutput:
    boto3_raw_data: "type_defs.CaseEventIncludedDataOutputTypeDef" = dataclasses.field()

    @cached_property
    def fields(self):  # pragma: no cover
        return FieldIdentifier.make_many(self.boto3_raw_data["fields"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CaseEventIncludedDataOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CaseEventIncludedDataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaseEventIncludedData:
    boto3_raw_data: "type_defs.CaseEventIncludedDataTypeDef" = dataclasses.field()

    @cached_property
    def fields(self):  # pragma: no cover
        return FieldIdentifier.make_many(self.boto3_raw_data["fields"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CaseEventIncludedDataTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CaseEventIncludedDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCaseRequest:
    boto3_raw_data: "type_defs.GetCaseRequestTypeDef" = dataclasses.field()

    caseId = field("caseId")
    domainId = field("domainId")

    @cached_property
    def fields(self):  # pragma: no cover
        return FieldIdentifier.make_many(self.boto3_raw_data["fields"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetCaseRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetCaseRequestTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetFieldResponse:
    boto3_raw_data: "type_defs.BatchGetFieldResponseTypeDef" = dataclasses.field()

    @cached_property
    def errors(self):  # pragma: no cover
        return FieldError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def fields(self):  # pragma: no cover
        return GetFieldResponse.make_many(self.boto3_raw_data["fields"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetFieldResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetFieldResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutFieldOptionsRequest:
    boto3_raw_data: "type_defs.BatchPutFieldOptionsRequestTypeDef" = dataclasses.field()

    domainId = field("domainId")
    fieldId = field("fieldId")

    @cached_property
    def options(self):  # pragma: no cover
        return FieldOption.make_many(self.boto3_raw_data["options"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchPutFieldOptionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutFieldOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFieldOptionsResponse:
    boto3_raw_data: "type_defs.ListFieldOptionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def options(self):  # pragma: no cover
        return FieldOption.make_many(self.boto3_raw_data["options"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFieldOptionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFieldOptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchPutFieldOptionsResponse:
    boto3_raw_data: "type_defs.BatchPutFieldOptionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def errors(self):  # pragma: no cover
        return FieldOptionError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchPutFieldOptionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchPutFieldOptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BooleanOperandsOutput:
    boto3_raw_data: "type_defs.BooleanOperandsOutputTypeDef" = dataclasses.field()

    @cached_property
    def operandOne(self):  # pragma: no cover
        return OperandOne.make_one(self.boto3_raw_data["operandOne"])

    @cached_property
    def operandTwo(self):  # pragma: no cover
        return OperandTwoOutput.make_one(self.boto3_raw_data["operandTwo"])

    result = field("result")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BooleanOperandsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BooleanOperandsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BooleanOperands:
    boto3_raw_data: "type_defs.BooleanOperandsTypeDef" = dataclasses.field()

    @cached_property
    def operandOne(self):  # pragma: no cover
        return OperandOne.make_one(self.boto3_raw_data["operandOne"])

    @cached_property
    def operandTwo(self):  # pragma: no cover
        return OperandTwo.make_one(self.boto3_raw_data["operandTwo"])

    result = field("result")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BooleanOperandsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BooleanOperandsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCaseRulesResponse:
    boto3_raw_data: "type_defs.ListCaseRulesResponseTypeDef" = dataclasses.field()

    @cached_property
    def caseRules(self):  # pragma: no cover
        return CaseRuleSummary.make_many(self.boto3_raw_data["caseRules"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCaseRulesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCaseRulesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCasesForContactResponse:
    boto3_raw_data: "type_defs.ListCasesForContactResponseTypeDef" = dataclasses.field()

    @cached_property
    def cases(self):  # pragma: no cover
        return CaseSummary.make_many(self.boto3_raw_data["cases"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCasesForContactResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCasesForContactResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateTemplateRequest:
    boto3_raw_data: "type_defs.CreateTemplateRequestTypeDef" = dataclasses.field()

    domainId = field("domainId")
    name = field("name")
    description = field("description")

    @cached_property
    def layoutConfiguration(self):  # pragma: no cover
        return LayoutConfiguration.make_one(self.boto3_raw_data["layoutConfiguration"])

    @cached_property
    def requiredFields(self):  # pragma: no cover
        return RequiredField.make_many(self.boto3_raw_data["requiredFields"])

    @cached_property
    def rules(self):  # pragma: no cover
        return TemplateRule.make_many(self.boto3_raw_data["rules"])

    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetTemplateResponse:
    boto3_raw_data: "type_defs.GetTemplateResponseTypeDef" = dataclasses.field()

    createdTime = field("createdTime")
    deleted = field("deleted")
    description = field("description")
    lastModifiedTime = field("lastModifiedTime")

    @cached_property
    def layoutConfiguration(self):  # pragma: no cover
        return LayoutConfiguration.make_one(self.boto3_raw_data["layoutConfiguration"])

    name = field("name")

    @cached_property
    def requiredFields(self):  # pragma: no cover
        return RequiredField.make_many(self.boto3_raw_data["requiredFields"])

    @cached_property
    def rules(self):  # pragma: no cover
        return TemplateRule.make_many(self.boto3_raw_data["rules"])

    status = field("status")
    tags = field("tags")
    templateArn = field("templateArn")
    templateId = field("templateId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetTemplateResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetTemplateResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateTemplateRequest:
    boto3_raw_data: "type_defs.UpdateTemplateRequestTypeDef" = dataclasses.field()

    domainId = field("domainId")
    templateId = field("templateId")
    description = field("description")

    @cached_property
    def layoutConfiguration(self):  # pragma: no cover
        return LayoutConfiguration.make_one(self.boto3_raw_data["layoutConfiguration"])

    name = field("name")

    @cached_property
    def requiredFields(self):  # pragma: no cover
        return RequiredField.make_many(self.boto3_raw_data["requiredFields"])

    @cached_property
    def rules(self):  # pragma: no cover
        return TemplateRule.make_many(self.boto3_raw_data["rules"])

    status = field("status")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateTemplateRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateTemplateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainsResponse:
    boto3_raw_data: "type_defs.ListDomainsResponseTypeDef" = dataclasses.field()

    @cached_property
    def domains(self):  # pragma: no cover
        return DomainSummary.make_many(self.boto3_raw_data["domains"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldGroupOutput:
    boto3_raw_data: "type_defs.FieldGroupOutputTypeDef" = dataclasses.field()

    @cached_property
    def fields(self):  # pragma: no cover
        return FieldItem.make_many(self.boto3_raw_data["fields"])

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldGroupOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldGroupOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldGroup:
    boto3_raw_data: "type_defs.FieldGroupTypeDef" = dataclasses.field()

    @cached_property
    def fields(self):  # pragma: no cover
        return FieldItem.make_many(self.boto3_raw_data["fields"])

    name = field("name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldGroupTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FieldGroupTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListFieldsResponse:
    boto3_raw_data: "type_defs.ListFieldsResponseTypeDef" = dataclasses.field()

    @cached_property
    def fields(self):  # pragma: no cover
        return FieldSummary.make_many(self.boto3_raw_data["fields"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListFieldsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListFieldsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldValueOutput:
    boto3_raw_data: "type_defs.FieldValueOutputTypeDef" = dataclasses.field()

    id = field("id")

    @cached_property
    def value(self):  # pragma: no cover
        return FieldValueUnionOutput.make_one(self.boto3_raw_data["value"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldValueOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FieldValueOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlaConfiguration:
    boto3_raw_data: "type_defs.SlaConfigurationTypeDef" = dataclasses.field()

    name = field("name")
    status = field("status")
    targetTime = field("targetTime")
    type = field("type")
    completionTime = field("completionTime")
    fieldId = field("fieldId")

    @cached_property
    def targetFieldValues(self):  # pragma: no cover
        return FieldValueUnionOutput.make_many(self.boto3_raw_data["targetFieldValues"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SlaConfigurationTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlaConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListLayoutsResponse:
    boto3_raw_data: "type_defs.ListLayoutsResponseTypeDef" = dataclasses.field()

    @cached_property
    def layouts(self):  # pragma: no cover
        return LayoutSummary.make_many(self.boto3_raw_data["layouts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListLayoutsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListLayoutsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCaseRulesRequestPaginate:
    boto3_raw_data: "type_defs.ListCaseRulesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    domainId = field("domainId")

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCaseRulesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCaseRulesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListTemplatesResponse:
    boto3_raw_data: "type_defs.ListTemplatesResponseTypeDef" = dataclasses.field()

    @cached_property
    def templates(self):  # pragma: no cover
        return TemplateSummary.make_many(self.boto3_raw_data["templates"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListTemplatesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListTemplatesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelatedItemTypeFilter:
    boto3_raw_data: "type_defs.RelatedItemTypeFilterTypeDef" = dataclasses.field()

    comment = field("comment")

    @cached_property
    def contact(self):  # pragma: no cover
        return ContactFilter.make_one(self.boto3_raw_data["contact"])

    @cached_property
    def file(self):  # pragma: no cover
        return FileFilter.make_one(self.boto3_raw_data["file"])

    @cached_property
    def sla(self):  # pragma: no cover
        return SlaFilter.make_one(self.boto3_raw_data["sla"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RelatedItemTypeFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelatedItemTypeFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AuditEvent:
    boto3_raw_data: "type_defs.AuditEventTypeDef" = dataclasses.field()

    eventId = field("eventId")

    @cached_property
    def fields(self):  # pragma: no cover
        return AuditEventField.make_many(self.boto3_raw_data["fields"])

    performedTime = field("performedTime")
    type = field("type")

    @cached_property
    def performedBy(self):  # pragma: no cover
        return AuditEventPerformedBy.make_one(self.boto3_raw_data["performedBy"])

    relatedItemType = field("relatedItemType")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AuditEventTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AuditEventTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventIncludedDataOutput:
    boto3_raw_data: "type_defs.EventIncludedDataOutputTypeDef" = dataclasses.field()

    @cached_property
    def caseData(self):  # pragma: no cover
        return CaseEventIncludedDataOutput.make_one(self.boto3_raw_data["caseData"])

    @cached_property
    def relatedItemData(self):  # pragma: no cover
        return RelatedItemEventIncludedData.make_one(
            self.boto3_raw_data["relatedItemData"]
        )

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventIncludedDataOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventIncludedDataOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventIncludedData:
    boto3_raw_data: "type_defs.EventIncludedDataTypeDef" = dataclasses.field()

    @cached_property
    def caseData(self):  # pragma: no cover
        return CaseEventIncludedData.make_one(self.boto3_raw_data["caseData"])

    @cached_property
    def relatedItemData(self):  # pragma: no cover
        return RelatedItemEventIncludedData.make_one(
            self.boto3_raw_data["relatedItemData"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.EventIncludedDataTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventIncludedDataTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BooleanConditionOutput:
    boto3_raw_data: "type_defs.BooleanConditionOutputTypeDef" = dataclasses.field()

    @cached_property
    def equalTo(self):  # pragma: no cover
        return BooleanOperandsOutput.make_one(self.boto3_raw_data["equalTo"])

    @cached_property
    def notEqualTo(self):  # pragma: no cover
        return BooleanOperandsOutput.make_one(self.boto3_raw_data["notEqualTo"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BooleanConditionOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BooleanConditionOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BooleanCondition:
    boto3_raw_data: "type_defs.BooleanConditionTypeDef" = dataclasses.field()

    @cached_property
    def equalTo(self):  # pragma: no cover
        return BooleanOperands.make_one(self.boto3_raw_data["equalTo"])

    @cached_property
    def notEqualTo(self):  # pragma: no cover
        return BooleanOperands.make_one(self.boto3_raw_data["notEqualTo"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BooleanConditionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BooleanConditionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SectionOutput:
    boto3_raw_data: "type_defs.SectionOutputTypeDef" = dataclasses.field()

    @cached_property
    def fieldGroup(self):  # pragma: no cover
        return FieldGroupOutput.make_one(self.boto3_raw_data["fieldGroup"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SectionOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SectionOutputTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Section:
    boto3_raw_data: "type_defs.SectionTypeDef" = dataclasses.field()

    @cached_property
    def fieldGroup(self):  # pragma: no cover
        return FieldGroup.make_one(self.boto3_raw_data["fieldGroup"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SectionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SectionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCaseResponse:
    boto3_raw_data: "type_defs.GetCaseResponseTypeDef" = dataclasses.field()

    @cached_property
    def fields(self):  # pragma: no cover
        return FieldValueOutput.make_many(self.boto3_raw_data["fields"])

    tags = field("tags")
    templateId = field("templateId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetCaseResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GetCaseResponseTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchCasesResponseItem:
    boto3_raw_data: "type_defs.SearchCasesResponseItemTypeDef" = dataclasses.field()

    caseId = field("caseId")

    @cached_property
    def fields(self):  # pragma: no cover
        return FieldValueOutput.make_many(self.boto3_raw_data["fields"])

    templateId = field("templateId")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchCasesResponseItemTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchCasesResponseItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlaContent:
    boto3_raw_data: "type_defs.SlaContentTypeDef" = dataclasses.field()

    @cached_property
    def slaConfiguration(self):  # pragma: no cover
        return SlaConfiguration.make_one(self.boto3_raw_data["slaConfiguration"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SlaContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SlaContentTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldValue:
    boto3_raw_data: "type_defs.FieldValueTypeDef" = dataclasses.field()

    id = field("id")
    value = field("value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldValueTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FieldValueTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlaInputConfiguration:
    boto3_raw_data: "type_defs.SlaInputConfigurationTypeDef" = dataclasses.field()

    name = field("name")
    targetSlaMinutes = field("targetSlaMinutes")
    type = field("type")
    fieldId = field("fieldId")
    targetFieldValues = field("targetFieldValues")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SlaInputConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SlaInputConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchRelatedItemsRequestPaginate:
    boto3_raw_data: "type_defs.SearchRelatedItemsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    caseId = field("caseId")
    domainId = field("domainId")

    @cached_property
    def filters(self):  # pragma: no cover
        return RelatedItemTypeFilter.make_many(self.boto3_raw_data["filters"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.SearchRelatedItemsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchRelatedItemsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchRelatedItemsRequest:
    boto3_raw_data: "type_defs.SearchRelatedItemsRequestTypeDef" = dataclasses.field()

    caseId = field("caseId")
    domainId = field("domainId")

    @cached_property
    def filters(self):  # pragma: no cover
        return RelatedItemTypeFilter.make_many(self.boto3_raw_data["filters"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchRelatedItemsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchRelatedItemsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCaseAuditEventsResponse:
    boto3_raw_data: "type_defs.GetCaseAuditEventsResponseTypeDef" = dataclasses.field()

    @cached_property
    def auditEvents(self):  # pragma: no cover
        return AuditEvent.make_many(self.boto3_raw_data["auditEvents"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCaseAuditEventsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCaseAuditEventsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventBridgeConfigurationOutput:
    boto3_raw_data: "type_defs.EventBridgeConfigurationOutputTypeDef" = (
        dataclasses.field()
    )

    enabled = field("enabled")

    @cached_property
    def includedData(self):  # pragma: no cover
        return EventIncludedDataOutput.make_one(self.boto3_raw_data["includedData"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.EventBridgeConfigurationOutputTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventBridgeConfigurationOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EventBridgeConfiguration:
    boto3_raw_data: "type_defs.EventBridgeConfigurationTypeDef" = dataclasses.field()

    enabled = field("enabled")

    @cached_property
    def includedData(self):  # pragma: no cover
        return EventIncludedData.make_one(self.boto3_raw_data["includedData"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.EventBridgeConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EventBridgeConfigurationTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequiredCaseRuleOutput:
    boto3_raw_data: "type_defs.RequiredCaseRuleOutputTypeDef" = dataclasses.field()

    @cached_property
    def conditions(self):  # pragma: no cover
        return BooleanConditionOutput.make_many(self.boto3_raw_data["conditions"])

    defaultValue = field("defaultValue")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RequiredCaseRuleOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequiredCaseRuleOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RequiredCaseRule:
    boto3_raw_data: "type_defs.RequiredCaseRuleTypeDef" = dataclasses.field()

    @cached_property
    def conditions(self):  # pragma: no cover
        return BooleanCondition.make_many(self.boto3_raw_data["conditions"])

    defaultValue = field("defaultValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.RequiredCaseRuleTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RequiredCaseRuleTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LayoutSectionsOutput:
    boto3_raw_data: "type_defs.LayoutSectionsOutputTypeDef" = dataclasses.field()

    @cached_property
    def sections(self):  # pragma: no cover
        return SectionOutput.make_many(self.boto3_raw_data["sections"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LayoutSectionsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LayoutSectionsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LayoutSections:
    boto3_raw_data: "type_defs.LayoutSectionsTypeDef" = dataclasses.field()

    @cached_property
    def sections(self):  # pragma: no cover
        return Section.make_many(self.boto3_raw_data["sections"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LayoutSectionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LayoutSectionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchCasesResponse:
    boto3_raw_data: "type_defs.SearchCasesResponseTypeDef" = dataclasses.field()

    @cached_property
    def cases(self):  # pragma: no cover
        return SearchCasesResponseItem.make_many(self.boto3_raw_data["cases"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchCasesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchCasesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelatedItemContent:
    boto3_raw_data: "type_defs.RelatedItemContentTypeDef" = dataclasses.field()

    @cached_property
    def comment(self):  # pragma: no cover
        return CommentContent.make_one(self.boto3_raw_data["comment"])

    @cached_property
    def contact(self):  # pragma: no cover
        return ContactContent.make_one(self.boto3_raw_data["contact"])

    @cached_property
    def file(self):  # pragma: no cover
        return FileContent.make_one(self.boto3_raw_data["file"])

    @cached_property
    def sla(self):  # pragma: no cover
        return SlaContent.make_one(self.boto3_raw_data["sla"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RelatedItemContentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelatedItemContentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SlaInputContent:
    boto3_raw_data: "type_defs.SlaInputContentTypeDef" = dataclasses.field()

    @cached_property
    def slaInputConfiguration(self):  # pragma: no cover
        return SlaInputConfiguration.make_one(
            self.boto3_raw_data["slaInputConfiguration"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SlaInputContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SlaInputContentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCaseEventConfigurationResponse:
    boto3_raw_data: "type_defs.GetCaseEventConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def eventBridge(self):  # pragma: no cover
        return EventBridgeConfigurationOutput.make_one(
            self.boto3_raw_data["eventBridge"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.GetCaseEventConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCaseEventConfigurationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaseRuleDetailsOutput:
    boto3_raw_data: "type_defs.CaseRuleDetailsOutputTypeDef" = dataclasses.field()

    @cached_property
    def required(self):  # pragma: no cover
        return RequiredCaseRuleOutput.make_one(self.boto3_raw_data["required"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CaseRuleDetailsOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CaseRuleDetailsOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaseRuleDetails:
    boto3_raw_data: "type_defs.CaseRuleDetailsTypeDef" = dataclasses.field()

    @cached_property
    def required(self):  # pragma: no cover
        return RequiredCaseRule.make_one(self.boto3_raw_data["required"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CaseRuleDetailsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CaseRuleDetailsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BasicLayoutOutput:
    boto3_raw_data: "type_defs.BasicLayoutOutputTypeDef" = dataclasses.field()

    @cached_property
    def moreInfo(self):  # pragma: no cover
        return LayoutSectionsOutput.make_one(self.boto3_raw_data["moreInfo"])

    @cached_property
    def topPanel(self):  # pragma: no cover
        return LayoutSectionsOutput.make_one(self.boto3_raw_data["topPanel"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BasicLayoutOutputTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BasicLayoutOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BasicLayout:
    boto3_raw_data: "type_defs.BasicLayoutTypeDef" = dataclasses.field()

    @cached_property
    def moreInfo(self):  # pragma: no cover
        return LayoutSections.make_one(self.boto3_raw_data["moreInfo"])

    @cached_property
    def topPanel(self):  # pragma: no cover
        return LayoutSections.make_one(self.boto3_raw_data["topPanel"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.BasicLayoutTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.BasicLayoutTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchRelatedItemsResponseItem:
    boto3_raw_data: "type_defs.SearchRelatedItemsResponseItemTypeDef" = (
        dataclasses.field()
    )

    associationTime = field("associationTime")

    @cached_property
    def content(self):  # pragma: no cover
        return RelatedItemContent.make_one(self.boto3_raw_data["content"])

    relatedItemId = field("relatedItemId")
    type = field("type")

    @cached_property
    def performedBy(self):  # pragma: no cover
        return UserUnion.make_one(self.boto3_raw_data["performedBy"])

    tags = field("tags")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.SearchRelatedItemsResponseItemTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchRelatedItemsResponseItemTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCaseRequest:
    boto3_raw_data: "type_defs.CreateCaseRequestTypeDef" = dataclasses.field()

    domainId = field("domainId")
    fields = field("fields")
    templateId = field("templateId")
    clientToken = field("clientToken")

    @cached_property
    def performedBy(self):  # pragma: no cover
        return UserUnion.make_one(self.boto3_raw_data["performedBy"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CreateCaseRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FieldFilter:
    boto3_raw_data: "type_defs.FieldFilterTypeDef" = dataclasses.field()

    contains = field("contains")
    equalTo = field("equalTo")
    greaterThan = field("greaterThan")
    greaterThanOrEqualTo = field("greaterThanOrEqualTo")
    lessThan = field("lessThan")
    lessThanOrEqualTo = field("lessThanOrEqualTo")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FieldFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FieldFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCaseRequest:
    boto3_raw_data: "type_defs.UpdateCaseRequestTypeDef" = dataclasses.field()

    caseId = field("caseId")
    domainId = field("domainId")
    fields = field("fields")

    @cached_property
    def performedBy(self):  # pragma: no cover
        return UserUnion.make_one(self.boto3_raw_data["performedBy"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UpdateCaseRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCaseRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelatedItemInputContent:
    boto3_raw_data: "type_defs.RelatedItemInputContentTypeDef" = dataclasses.field()

    @cached_property
    def comment(self):  # pragma: no cover
        return CommentContent.make_one(self.boto3_raw_data["comment"])

    @cached_property
    def contact(self):  # pragma: no cover
        return Contact.make_one(self.boto3_raw_data["contact"])

    @cached_property
    def file(self):  # pragma: no cover
        return FileContent.make_one(self.boto3_raw_data["file"])

    @cached_property
    def sla(self):  # pragma: no cover
        return SlaInputContent.make_one(self.boto3_raw_data["sla"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RelatedItemInputContentTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelatedItemInputContentTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class PutCaseEventConfigurationRequest:
    boto3_raw_data: "type_defs.PutCaseEventConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    domainId = field("domainId")
    eventBridge = field("eventBridge")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.PutCaseEventConfigurationRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.PutCaseEventConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetCaseRuleResponse:
    boto3_raw_data: "type_defs.GetCaseRuleResponseTypeDef" = dataclasses.field()

    caseRuleArn = field("caseRuleArn")
    caseRuleId = field("caseRuleId")
    name = field("name")

    @cached_property
    def rule(self):  # pragma: no cover
        return CaseRuleDetailsOutput.make_one(self.boto3_raw_data["rule"])

    createdTime = field("createdTime")
    deleted = field("deleted")
    description = field("description")
    lastModifiedTime = field("lastModifiedTime")
    tags = field("tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetCaseRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetCaseRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LayoutContentOutput:
    boto3_raw_data: "type_defs.LayoutContentOutputTypeDef" = dataclasses.field()

    @cached_property
    def basic(self):  # pragma: no cover
        return BasicLayoutOutput.make_one(self.boto3_raw_data["basic"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LayoutContentOutputTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LayoutContentOutputTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LayoutContent:
    boto3_raw_data: "type_defs.LayoutContentTypeDef" = dataclasses.field()

    @cached_property
    def basic(self):  # pragma: no cover
        return BasicLayout.make_one(self.boto3_raw_data["basic"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LayoutContentTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LayoutContentTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchRelatedItemsResponse:
    boto3_raw_data: "type_defs.SearchRelatedItemsResponseTypeDef" = dataclasses.field()

    @cached_property
    def relatedItems(self):  # pragma: no cover
        return SearchRelatedItemsResponseItem.make_many(
            self.boto3_raw_data["relatedItems"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    nextToken = field("nextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchRelatedItemsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchRelatedItemsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaseFilterPaginator:
    boto3_raw_data: "type_defs.CaseFilterPaginatorTypeDef" = dataclasses.field()

    andAll = field("andAll")

    @cached_property
    def field(self):  # pragma: no cover
        return FieldFilter.make_one(self.boto3_raw_data["field"])

    not_ = field("not")
    orAll = field("orAll")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CaseFilterPaginatorTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CaseFilterPaginatorTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CaseFilter:
    boto3_raw_data: "type_defs.CaseFilterTypeDef" = dataclasses.field()

    andAll = field("andAll")

    @cached_property
    def field(self):  # pragma: no cover
        return FieldFilter.make_one(self.boto3_raw_data["field"])

    not_ = field("not")
    orAll = field("orAll")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.CaseFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.CaseFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateRelatedItemRequest:
    boto3_raw_data: "type_defs.CreateRelatedItemRequestTypeDef" = dataclasses.field()

    caseId = field("caseId")

    @cached_property
    def content(self):  # pragma: no cover
        return RelatedItemInputContent.make_one(self.boto3_raw_data["content"])

    domainId = field("domainId")
    type = field("type")

    @cached_property
    def performedBy(self):  # pragma: no cover
        return UserUnion.make_one(self.boto3_raw_data["performedBy"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateRelatedItemRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateRelatedItemRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetCaseRuleResponse:
    boto3_raw_data: "type_defs.BatchGetCaseRuleResponseTypeDef" = dataclasses.field()

    @cached_property
    def caseRules(self):  # pragma: no cover
        return GetCaseRuleResponse.make_many(self.boto3_raw_data["caseRules"])

    @cached_property
    def errors(self):  # pragma: no cover
        return CaseRuleError.make_many(self.boto3_raw_data["errors"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BatchGetCaseRuleResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetCaseRuleResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateCaseRuleRequest:
    boto3_raw_data: "type_defs.CreateCaseRuleRequestTypeDef" = dataclasses.field()

    domainId = field("domainId")
    name = field("name")
    rule = field("rule")
    description = field("description")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateCaseRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateCaseRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateCaseRuleRequest:
    boto3_raw_data: "type_defs.UpdateCaseRuleRequestTypeDef" = dataclasses.field()

    caseRuleId = field("caseRuleId")
    domainId = field("domainId")
    description = field("description")
    name = field("name")
    rule = field("rule")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateCaseRuleRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateCaseRuleRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetLayoutResponse:
    boto3_raw_data: "type_defs.GetLayoutResponseTypeDef" = dataclasses.field()

    @cached_property
    def content(self):  # pragma: no cover
        return LayoutContentOutput.make_one(self.boto3_raw_data["content"])

    createdTime = field("createdTime")
    deleted = field("deleted")
    lastModifiedTime = field("lastModifiedTime")
    layoutArn = field("layoutArn")
    layoutId = field("layoutId")
    name = field("name")
    tags = field("tags")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetLayoutResponseTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetLayoutResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchCasesRequestPaginate:
    boto3_raw_data: "type_defs.SearchCasesRequestPaginateTypeDef" = dataclasses.field()

    domainId = field("domainId")

    @cached_property
    def fields(self):  # pragma: no cover
        return FieldIdentifier.make_many(self.boto3_raw_data["fields"])

    @cached_property
    def filter(self):  # pragma: no cover
        return CaseFilterPaginator.make_one(self.boto3_raw_data["filter"])

    searchTerm = field("searchTerm")

    @cached_property
    def sorts(self):  # pragma: no cover
        return Sort.make_many(self.boto3_raw_data["sorts"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchCasesRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchCasesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SearchCasesRequest:
    boto3_raw_data: "type_defs.SearchCasesRequestTypeDef" = dataclasses.field()

    domainId = field("domainId")

    @cached_property
    def fields(self):  # pragma: no cover
        return FieldIdentifier.make_many(self.boto3_raw_data["fields"])

    @cached_property
    def filter(self):  # pragma: no cover
        return CaseFilter.make_one(self.boto3_raw_data["filter"])

    maxResults = field("maxResults")
    nextToken = field("nextToken")
    searchTerm = field("searchTerm")

    @cached_property
    def sorts(self):  # pragma: no cover
        return Sort.make_many(self.boto3_raw_data["sorts"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.SearchCasesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.SearchCasesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateLayoutRequest:
    boto3_raw_data: "type_defs.CreateLayoutRequestTypeDef" = dataclasses.field()

    content = field("content")
    domainId = field("domainId")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateLayoutRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateLayoutRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateLayoutRequest:
    boto3_raw_data: "type_defs.UpdateLayoutRequestTypeDef" = dataclasses.field()

    domainId = field("domainId")
    layoutId = field("layoutId")
    content = field("content")
    name = field("name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UpdateLayoutRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateLayoutRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
