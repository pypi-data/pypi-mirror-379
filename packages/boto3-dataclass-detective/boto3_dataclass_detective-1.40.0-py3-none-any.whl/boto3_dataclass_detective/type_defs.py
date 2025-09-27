# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_detective import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AcceptInvitationRequest:
    boto3_raw_data: "type_defs.AcceptInvitationRequestTypeDef" = dataclasses.field()

    GraphArn = field("GraphArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AcceptInvitationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AcceptInvitationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Account:
    boto3_raw_data: "type_defs.AccountTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    EmailAddress = field("EmailAddress")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AccountTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AccountTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Administrator:
    boto3_raw_data: "type_defs.AdministratorTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    GraphArn = field("GraphArn")
    DelegationTime = field("DelegationTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AdministratorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AdministratorTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetGraphMemberDatasourcesRequest:
    boto3_raw_data: "type_defs.BatchGetGraphMemberDatasourcesRequestTypeDef" = (
        dataclasses.field()
    )

    GraphArn = field("GraphArn")
    AccountIds = field("AccountIds")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetGraphMemberDatasourcesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetGraphMemberDatasourcesRequestTypeDef"]
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
class UnprocessedAccount:
    boto3_raw_data: "type_defs.UnprocessedAccountTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    Reason = field("Reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.UnprocessedAccountTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnprocessedAccountTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetMembershipDatasourcesRequest:
    boto3_raw_data: "type_defs.BatchGetMembershipDatasourcesRequestTypeDef" = (
        dataclasses.field()
    )

    GraphArns = field("GraphArns")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetMembershipDatasourcesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetMembershipDatasourcesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UnprocessedGraph:
    boto3_raw_data: "type_defs.UnprocessedGraphTypeDef" = dataclasses.field()

    GraphArn = field("GraphArn")
    Reason = field("Reason")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.UnprocessedGraphTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UnprocessedGraphTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGraphRequest:
    boto3_raw_data: "type_defs.CreateGraphRequestTypeDef" = dataclasses.field()

    Tags = field("Tags")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGraphRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGraphRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TimestampForCollection:
    boto3_raw_data: "type_defs.TimestampForCollectionTypeDef" = dataclasses.field()

    Timestamp = field("Timestamp")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TimestampForCollectionTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TimestampForCollectionTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasourcePackageUsageInfo:
    boto3_raw_data: "type_defs.DatasourcePackageUsageInfoTypeDef" = dataclasses.field()

    VolumeUsageInBytes = field("VolumeUsageInBytes")
    VolumeUsageUpdateTime = field("VolumeUsageUpdateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DatasourcePackageUsageInfoTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasourcePackageUsageInfoTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteGraphRequest:
    boto3_raw_data: "type_defs.DeleteGraphRequestTypeDef" = dataclasses.field()

    GraphArn = field("GraphArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteGraphRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteGraphRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMembersRequest:
    boto3_raw_data: "type_defs.DeleteMembersRequestTypeDef" = dataclasses.field()

    GraphArn = field("GraphArn")
    AccountIds = field("AccountIds")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMembersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMembersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationConfigurationRequest:
    boto3_raw_data: "type_defs.DescribeOrganizationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    GraphArn = field("GraphArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrganizationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOrganizationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DisassociateMembershipRequest:
    boto3_raw_data: "type_defs.DisassociateMembershipRequestTypeDef" = (
        dataclasses.field()
    )

    GraphArn = field("GraphArn")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DisassociateMembershipRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DisassociateMembershipRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class EnableOrganizationAdminAccountRequest:
    boto3_raw_data: "type_defs.EnableOrganizationAdminAccountRequestTypeDef" = (
        dataclasses.field()
    )

    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.EnableOrganizationAdminAccountRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.EnableOrganizationAdminAccountRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StringFilter:
    boto3_raw_data: "type_defs.StringFilterTypeDef" = dataclasses.field()

    Value = field("Value")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.StringFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.StringFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FlaggedIpAddressDetail:
    boto3_raw_data: "type_defs.FlaggedIpAddressDetailTypeDef" = dataclasses.field()

    IpAddress = field("IpAddress")
    Reason = field("Reason")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FlaggedIpAddressDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FlaggedIpAddressDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetInvestigationRequest:
    boto3_raw_data: "type_defs.GetInvestigationRequestTypeDef" = dataclasses.field()

    GraphArn = field("GraphArn")
    InvestigationId = field("InvestigationId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInvestigationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInvestigationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMembersRequest:
    boto3_raw_data: "type_defs.GetMembersRequestTypeDef" = dataclasses.field()

    GraphArn = field("GraphArn")
    AccountIds = field("AccountIds")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GetMembersRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMembersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Graph:
    boto3_raw_data: "type_defs.GraphTypeDef" = dataclasses.field()

    Arn = field("Arn")
    CreatedTime = field("CreatedTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.GraphTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.GraphTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImpossibleTravelDetail:
    boto3_raw_data: "type_defs.ImpossibleTravelDetailTypeDef" = dataclasses.field()

    StartingIpAddress = field("StartingIpAddress")
    EndingIpAddress = field("EndingIpAddress")
    StartingLocation = field("StartingLocation")
    EndingLocation = field("EndingLocation")
    HourlyTimeDelta = field("HourlyTimeDelta")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImpossibleTravelDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImpossibleTravelDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NewAsoDetail:
    boto3_raw_data: "type_defs.NewAsoDetailTypeDef" = dataclasses.field()

    Aso = field("Aso")
    IsNewForEntireAccount = field("IsNewForEntireAccount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.NewAsoDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.NewAsoDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NewGeolocationDetail:
    boto3_raw_data: "type_defs.NewGeolocationDetailTypeDef" = dataclasses.field()

    Location = field("Location")
    IpAddress = field("IpAddress")
    IsNewForEntireAccount = field("IsNewForEntireAccount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NewGeolocationDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NewGeolocationDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class NewUserAgentDetail:
    boto3_raw_data: "type_defs.NewUserAgentDetailTypeDef" = dataclasses.field()

    UserAgent = field("UserAgent")
    IsNewForEntireAccount = field("IsNewForEntireAccount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.NewUserAgentDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.NewUserAgentDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelatedFindingDetail:
    boto3_raw_data: "type_defs.RelatedFindingDetailTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Type = field("Type")
    IpAddress = field("IpAddress")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RelatedFindingDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelatedFindingDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RelatedFindingGroupDetail:
    boto3_raw_data: "type_defs.RelatedFindingGroupDetailTypeDef" = dataclasses.field()

    Id = field("Id")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RelatedFindingGroupDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RelatedFindingGroupDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TTPsObservedDetail:
    boto3_raw_data: "type_defs.TTPsObservedDetailTypeDef" = dataclasses.field()

    Tactic = field("Tactic")
    Technique = field("Technique")
    Procedure = field("Procedure")
    IpAddress = field("IpAddress")
    APIName = field("APIName")
    APISuccessCount = field("APISuccessCount")
    APIFailureCount = field("APIFailureCount")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.TTPsObservedDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TTPsObservedDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class InvestigationDetail:
    boto3_raw_data: "type_defs.InvestigationDetailTypeDef" = dataclasses.field()

    InvestigationId = field("InvestigationId")
    Severity = field("Severity")
    Status = field("Status")
    State = field("State")
    CreatedTime = field("CreatedTime")
    EntityArn = field("EntityArn")
    EntityType = field("EntityType")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.InvestigationDetailTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.InvestigationDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasourcePackagesRequest:
    boto3_raw_data: "type_defs.ListDatasourcePackagesRequestTypeDef" = (
        dataclasses.field()
    )

    GraphArn = field("GraphArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDatasourcePackagesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasourcePackagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGraphsRequest:
    boto3_raw_data: "type_defs.ListGraphsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ListGraphsRequestTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGraphsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIndicatorsRequest:
    boto3_raw_data: "type_defs.ListIndicatorsRequestTypeDef" = dataclasses.field()

    GraphArn = field("GraphArn")
    InvestigationId = field("InvestigationId")
    IndicatorType = field("IndicatorType")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIndicatorsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIndicatorsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SortCriteria:
    boto3_raw_data: "type_defs.SortCriteriaTypeDef" = dataclasses.field()

    Field = field("Field")
    SortOrder = field("SortOrder")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SortCriteriaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SortCriteriaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvitationsRequest:
    boto3_raw_data: "type_defs.ListInvitationsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInvitationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvitationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMembersRequest:
    boto3_raw_data: "type_defs.ListMembersRequestTypeDef" = dataclasses.field()

    GraphArn = field("GraphArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMembersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMembersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationAdminAccountsRequest:
    boto3_raw_data: "type_defs.ListOrganizationAdminAccountsRequestTypeDef" = (
        dataclasses.field()
    )

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOrganizationAdminAccountsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationAdminAccountsRequestTypeDef"]
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
class RejectInvitationRequest:
    boto3_raw_data: "type_defs.RejectInvitationRequestTypeDef" = dataclasses.field()

    GraphArn = field("GraphArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RejectInvitationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RejectInvitationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartMonitoringMemberRequest:
    boto3_raw_data: "type_defs.StartMonitoringMemberRequestTypeDef" = (
        dataclasses.field()
    )

    GraphArn = field("GraphArn")
    AccountId = field("AccountId")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartMonitoringMemberRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartMonitoringMemberRequestTypeDef"]
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
class UpdateDatasourcePackagesRequest:
    boto3_raw_data: "type_defs.UpdateDatasourcePackagesRequestTypeDef" = (
        dataclasses.field()
    )

    GraphArn = field("GraphArn")
    DatasourcePackages = field("DatasourcePackages")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateDatasourcePackagesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDatasourcePackagesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateInvestigationStateRequest:
    boto3_raw_data: "type_defs.UpdateInvestigationStateRequestTypeDef" = (
        dataclasses.field()
    )

    GraphArn = field("GraphArn")
    InvestigationId = field("InvestigationId")
    State = field("State")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateInvestigationStateRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateInvestigationStateRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateOrganizationConfigurationRequest:
    boto3_raw_data: "type_defs.UpdateOrganizationConfigurationRequestTypeDef" = (
        dataclasses.field()
    )

    GraphArn = field("GraphArn")
    AutoEnable = field("AutoEnable")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateOrganizationConfigurationRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateOrganizationConfigurationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMembersRequest:
    boto3_raw_data: "type_defs.CreateMembersRequestTypeDef" = dataclasses.field()

    GraphArn = field("GraphArn")

    @cached_property
    def Accounts(self):  # pragma: no cover
        return Account.make_many(self.boto3_raw_data["Accounts"])

    Message = field("Message")
    DisableEmailNotification = field("DisableEmailNotification")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMembersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMembersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateGraphResponse:
    boto3_raw_data: "type_defs.CreateGraphResponseTypeDef" = dataclasses.field()

    GraphArn = field("GraphArn")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateGraphResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateGraphResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeOrganizationConfigurationResponse:
    boto3_raw_data: "type_defs.DescribeOrganizationConfigurationResponseTypeDef" = (
        dataclasses.field()
    )

    AutoEnable = field("AutoEnable")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeOrganizationConfigurationResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeOrganizationConfigurationResponseTypeDef"]
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
class GetInvestigationResponse:
    boto3_raw_data: "type_defs.GetInvestigationResponseTypeDef" = dataclasses.field()

    GraphArn = field("GraphArn")
    InvestigationId = field("InvestigationId")
    EntityArn = field("EntityArn")
    EntityType = field("EntityType")
    CreatedTime = field("CreatedTime")
    ScopeStartTime = field("ScopeStartTime")
    ScopeEndTime = field("ScopeEndTime")
    Status = field("Status")
    Severity = field("Severity")
    State = field("State")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetInvestigationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetInvestigationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListOrganizationAdminAccountsResponse:
    boto3_raw_data: "type_defs.ListOrganizationAdminAccountsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Administrators(self):  # pragma: no cover
        return Administrator.make_many(self.boto3_raw_data["Administrators"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListOrganizationAdminAccountsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListOrganizationAdminAccountsResponseTypeDef"]
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

    Tags = field("Tags")

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
class StartInvestigationResponse:
    boto3_raw_data: "type_defs.StartInvestigationResponseTypeDef" = dataclasses.field()

    InvestigationId = field("InvestigationId")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartInvestigationResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartInvestigationResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteMembersResponse:
    boto3_raw_data: "type_defs.DeleteMembersResponseTypeDef" = dataclasses.field()

    AccountIds = field("AccountIds")

    @cached_property
    def UnprocessedAccounts(self):  # pragma: no cover
        return UnprocessedAccount.make_many(self.boto3_raw_data["UnprocessedAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteMembersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteMembersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DatasourcePackageIngestDetail:
    boto3_raw_data: "type_defs.DatasourcePackageIngestDetailTypeDef" = (
        dataclasses.field()
    )

    DatasourcePackageIngestState = field("DatasourcePackageIngestState")
    LastIngestStateChange = field("LastIngestStateChange")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DatasourcePackageIngestDetailTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DatasourcePackageIngestDetailTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MembershipDatasources:
    boto3_raw_data: "type_defs.MembershipDatasourcesTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    GraphArn = field("GraphArn")
    DatasourcePackageIngestHistory = field("DatasourcePackageIngestHistory")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.MembershipDatasourcesTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.MembershipDatasourcesTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class MemberDetail:
    boto3_raw_data: "type_defs.MemberDetailTypeDef" = dataclasses.field()

    AccountId = field("AccountId")
    EmailAddress = field("EmailAddress")
    GraphArn = field("GraphArn")
    MasterId = field("MasterId")
    AdministratorId = field("AdministratorId")
    Status = field("Status")
    DisabledReason = field("DisabledReason")
    InvitedTime = field("InvitedTime")
    UpdatedTime = field("UpdatedTime")
    VolumeUsageInBytes = field("VolumeUsageInBytes")
    VolumeUsageUpdatedTime = field("VolumeUsageUpdatedTime")
    PercentOfGraphUtilization = field("PercentOfGraphUtilization")
    PercentOfGraphUtilizationUpdatedTime = field("PercentOfGraphUtilizationUpdatedTime")
    InvitationType = field("InvitationType")
    VolumeUsageByDatasourcePackage = field("VolumeUsageByDatasourcePackage")
    DatasourcePackageIngestStates = field("DatasourcePackageIngestStates")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MemberDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MemberDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DateFilter:
    boto3_raw_data: "type_defs.DateFilterTypeDef" = dataclasses.field()

    StartInclusive = field("StartInclusive")
    EndInclusive = field("EndInclusive")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DateFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DateFilterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class StartInvestigationRequest:
    boto3_raw_data: "type_defs.StartInvestigationRequestTypeDef" = dataclasses.field()

    GraphArn = field("GraphArn")
    EntityArn = field("EntityArn")
    ScopeStartTime = field("ScopeStartTime")
    ScopeEndTime = field("ScopeEndTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.StartInvestigationRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.StartInvestigationRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListGraphsResponse:
    boto3_raw_data: "type_defs.ListGraphsResponseTypeDef" = dataclasses.field()

    @cached_property
    def GraphList(self):  # pragma: no cover
        return Graph.make_many(self.boto3_raw_data["GraphList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListGraphsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListGraphsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IndicatorDetail:
    boto3_raw_data: "type_defs.IndicatorDetailTypeDef" = dataclasses.field()

    @cached_property
    def TTPsObservedDetail(self):  # pragma: no cover
        return TTPsObservedDetail.make_one(self.boto3_raw_data["TTPsObservedDetail"])

    @cached_property
    def ImpossibleTravelDetail(self):  # pragma: no cover
        return ImpossibleTravelDetail.make_one(
            self.boto3_raw_data["ImpossibleTravelDetail"]
        )

    @cached_property
    def FlaggedIpAddressDetail(self):  # pragma: no cover
        return FlaggedIpAddressDetail.make_one(
            self.boto3_raw_data["FlaggedIpAddressDetail"]
        )

    @cached_property
    def NewGeolocationDetail(self):  # pragma: no cover
        return NewGeolocationDetail.make_one(
            self.boto3_raw_data["NewGeolocationDetail"]
        )

    @cached_property
    def NewAsoDetail(self):  # pragma: no cover
        return NewAsoDetail.make_one(self.boto3_raw_data["NewAsoDetail"])

    @cached_property
    def NewUserAgentDetail(self):  # pragma: no cover
        return NewUserAgentDetail.make_one(self.boto3_raw_data["NewUserAgentDetail"])

    @cached_property
    def RelatedFindingDetail(self):  # pragma: no cover
        return RelatedFindingDetail.make_one(
            self.boto3_raw_data["RelatedFindingDetail"]
        )

    @cached_property
    def RelatedFindingGroupDetail(self):  # pragma: no cover
        return RelatedFindingGroupDetail.make_one(
            self.boto3_raw_data["RelatedFindingGroupDetail"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IndicatorDetailTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IndicatorDetailTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvestigationsResponse:
    boto3_raw_data: "type_defs.ListInvestigationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def InvestigationDetails(self):  # pragma: no cover
        return InvestigationDetail.make_many(
            self.boto3_raw_data["InvestigationDetails"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInvestigationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvestigationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDatasourcePackagesResponse:
    boto3_raw_data: "type_defs.ListDatasourcePackagesResponseTypeDef" = (
        dataclasses.field()
    )

    DatasourcePackages = field("DatasourcePackages")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListDatasourcePackagesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDatasourcePackagesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetGraphMemberDatasourcesResponse:
    boto3_raw_data: "type_defs.BatchGetGraphMemberDatasourcesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MemberDatasources(self):  # pragma: no cover
        return MembershipDatasources.make_many(self.boto3_raw_data["MemberDatasources"])

    @cached_property
    def UnprocessedAccounts(self):  # pragma: no cover
        return UnprocessedAccount.make_many(self.boto3_raw_data["UnprocessedAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetGraphMemberDatasourcesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetGraphMemberDatasourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BatchGetMembershipDatasourcesResponse:
    boto3_raw_data: "type_defs.BatchGetMembershipDatasourcesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def MembershipDatasources(self):  # pragma: no cover
        return MembershipDatasources.make_many(
            self.boto3_raw_data["MembershipDatasources"]
        )

    @cached_property
    def UnprocessedGraphs(self):  # pragma: no cover
        return UnprocessedGraph.make_many(self.boto3_raw_data["UnprocessedGraphs"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.BatchGetMembershipDatasourcesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BatchGetMembershipDatasourcesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CreateMembersResponse:
    boto3_raw_data: "type_defs.CreateMembersResponseTypeDef" = dataclasses.field()

    @cached_property
    def Members(self):  # pragma: no cover
        return MemberDetail.make_many(self.boto3_raw_data["Members"])

    @cached_property
    def UnprocessedAccounts(self):  # pragma: no cover
        return UnprocessedAccount.make_many(self.boto3_raw_data["UnprocessedAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CreateMembersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CreateMembersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetMembersResponse:
    boto3_raw_data: "type_defs.GetMembersResponseTypeDef" = dataclasses.field()

    @cached_property
    def MemberDetails(self):  # pragma: no cover
        return MemberDetail.make_many(self.boto3_raw_data["MemberDetails"])

    @cached_property
    def UnprocessedAccounts(self):  # pragma: no cover
        return UnprocessedAccount.make_many(self.boto3_raw_data["UnprocessedAccounts"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.GetMembersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.GetMembersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvitationsResponse:
    boto3_raw_data: "type_defs.ListInvitationsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Invitations(self):  # pragma: no cover
        return MemberDetail.make_many(self.boto3_raw_data["Invitations"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInvitationsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvitationsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListMembersResponse:
    boto3_raw_data: "type_defs.ListMembersResponseTypeDef" = dataclasses.field()

    @cached_property
    def MemberDetails(self):  # pragma: no cover
        return MemberDetail.make_many(self.boto3_raw_data["MemberDetails"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListMembersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListMembersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class FilterCriteria:
    boto3_raw_data: "type_defs.FilterCriteriaTypeDef" = dataclasses.field()

    @cached_property
    def Severity(self):  # pragma: no cover
        return StringFilter.make_one(self.boto3_raw_data["Severity"])

    @cached_property
    def Status(self):  # pragma: no cover
        return StringFilter.make_one(self.boto3_raw_data["Status"])

    @cached_property
    def State(self):  # pragma: no cover
        return StringFilter.make_one(self.boto3_raw_data["State"])

    @cached_property
    def EntityArn(self):  # pragma: no cover
        return StringFilter.make_one(self.boto3_raw_data["EntityArn"])

    @cached_property
    def CreatedTime(self):  # pragma: no cover
        return DateFilter.make_one(self.boto3_raw_data["CreatedTime"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.FilterCriteriaTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.FilterCriteriaTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Indicator:
    boto3_raw_data: "type_defs.IndicatorTypeDef" = dataclasses.field()

    IndicatorType = field("IndicatorType")

    @cached_property
    def IndicatorDetail(self):  # pragma: no cover
        return IndicatorDetail.make_one(self.boto3_raw_data["IndicatorDetail"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IndicatorTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IndicatorTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListInvestigationsRequest:
    boto3_raw_data: "type_defs.ListInvestigationsRequestTypeDef" = dataclasses.field()

    GraphArn = field("GraphArn")
    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def FilterCriteria(self):  # pragma: no cover
        return FilterCriteria.make_one(self.boto3_raw_data["FilterCriteria"])

    @cached_property
    def SortCriteria(self):  # pragma: no cover
        return SortCriteria.make_one(self.boto3_raw_data["SortCriteria"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListInvestigationsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListInvestigationsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListIndicatorsResponse:
    boto3_raw_data: "type_defs.ListIndicatorsResponseTypeDef" = dataclasses.field()

    GraphArn = field("GraphArn")
    InvestigationId = field("InvestigationId")

    @cached_property
    def Indicators(self):  # pragma: no cover
        return Indicator.make_many(self.boto3_raw_data["Indicators"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListIndicatorsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListIndicatorsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
