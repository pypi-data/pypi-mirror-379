# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_controlcatalog import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class AssociatedDomainSummary:
    boto3_raw_data: "type_defs.AssociatedDomainSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociatedDomainSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociatedDomainSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AssociatedObjectiveSummary:
    boto3_raw_data: "type_defs.AssociatedObjectiveSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AssociatedObjectiveSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AssociatedObjectiveSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectiveResourceFilter:
    boto3_raw_data: "type_defs.ObjectiveResourceFilterTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ObjectiveResourceFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectiveResourceFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommonControlMappingDetails:
    boto3_raw_data: "type_defs.CommonControlMappingDetailsTypeDef" = dataclasses.field()

    CommonControlArn = field("CommonControlArn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommonControlMappingDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommonControlMappingDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImplementationFilter:
    boto3_raw_data: "type_defs.ImplementationFilterTypeDef" = dataclasses.field()

    Types = field("Types")
    Identifiers = field("Identifiers")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImplementationFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImplementationFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ControlMappingFilter:
    boto3_raw_data: "type_defs.ControlMappingFilterTypeDef" = dataclasses.field()

    ControlArns = field("ControlArns")
    CommonControlArns = field("CommonControlArns")
    MappingTypes = field("MappingTypes")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ControlMappingFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ControlMappingFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ControlParameter:
    boto3_raw_data: "type_defs.ControlParameterTypeDef" = dataclasses.field()

    Name = field("Name")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ControlParameterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ControlParameterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ImplementationSummary:
    boto3_raw_data: "type_defs.ImplementationSummaryTypeDef" = dataclasses.field()

    Type = field("Type")
    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImplementationSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImplementationSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainResourceFilter:
    boto3_raw_data: "type_defs.DomainResourceFilterTypeDef" = dataclasses.field()

    Arn = field("Arn")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainResourceFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainResourceFilterTypeDef"]
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

    Arn = field("Arn")
    Name = field("Name")
    Description = field("Description")
    CreateTime = field("CreateTime")
    LastUpdateTime = field("LastUpdateTime")

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
class FrameworkMappingDetails:
    boto3_raw_data: "type_defs.FrameworkMappingDetailsTypeDef" = dataclasses.field()

    Name = field("Name")
    Item = field("Item")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.FrameworkMappingDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.FrameworkMappingDetailsTypeDef"]
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

    ControlArn = field("ControlArn")

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
class ImplementationDetails:
    boto3_raw_data: "type_defs.ImplementationDetailsTypeDef" = dataclasses.field()

    Type = field("Type")
    Identifier = field("Identifier")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ImplementationDetailsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ImplementationDetailsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class RegionConfiguration:
    boto3_raw_data: "type_defs.RegionConfigurationTypeDef" = dataclasses.field()

    Scope = field("Scope")
    DeployableRegions = field("DeployableRegions")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.RegionConfigurationTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.RegionConfigurationTypeDef"]
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
class ListDomainsRequest:
    boto3_raw_data: "type_defs.ListDomainsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

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
class ObjectiveSummary:
    boto3_raw_data: "type_defs.ObjectiveSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def Domain(self):  # pragma: no cover
        return AssociatedDomainSummary.make_one(self.boto3_raw_data["Domain"])

    CreateTime = field("CreateTime")
    LastUpdateTime = field("LastUpdateTime")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ObjectiveSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ObjectiveSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommonControlSummary:
    boto3_raw_data: "type_defs.CommonControlSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    Description = field("Description")

    @cached_property
    def Domain(self):  # pragma: no cover
        return AssociatedDomainSummary.make_one(self.boto3_raw_data["Domain"])

    @cached_property
    def Objective(self):  # pragma: no cover
        return AssociatedObjectiveSummary.make_one(self.boto3_raw_data["Objective"])

    CreateTime = field("CreateTime")
    LastUpdateTime = field("LastUpdateTime")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommonControlSummaryTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommonControlSummaryTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class CommonControlFilter:
    boto3_raw_data: "type_defs.CommonControlFilterTypeDef" = dataclasses.field()

    @cached_property
    def Objectives(self):  # pragma: no cover
        return ObjectiveResourceFilter.make_many(self.boto3_raw_data["Objectives"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.CommonControlFilterTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.CommonControlFilterTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ControlFilter:
    boto3_raw_data: "type_defs.ControlFilterTypeDef" = dataclasses.field()

    @cached_property
    def Implementations(self):  # pragma: no cover
        return ImplementationFilter.make_one(self.boto3_raw_data["Implementations"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ControlFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ControlFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListControlMappingsRequest:
    boto3_raw_data: "type_defs.ListControlMappingsRequestTypeDef" = dataclasses.field()

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def Filter(self):  # pragma: no cover
        return ControlMappingFilter.make_one(self.boto3_raw_data["Filter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListControlMappingsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListControlMappingsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ControlSummary:
    boto3_raw_data: "type_defs.ControlSummaryTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Name = field("Name")
    Description = field("Description")
    Aliases = field("Aliases")
    Behavior = field("Behavior")
    Severity = field("Severity")

    @cached_property
    def Implementation(self):  # pragma: no cover
        return ImplementationSummary.make_one(self.boto3_raw_data["Implementation"])

    CreateTime = field("CreateTime")
    GovernedResources = field("GovernedResources")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ControlSummaryTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ControlSummaryTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ObjectiveFilter:
    boto3_raw_data: "type_defs.ObjectiveFilterTypeDef" = dataclasses.field()

    @cached_property
    def Domains(self):  # pragma: no cover
        return DomainResourceFilter.make_many(self.boto3_raw_data["Domains"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ObjectiveFilterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ObjectiveFilterTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Mapping:
    boto3_raw_data: "type_defs.MappingTypeDef" = dataclasses.field()

    @cached_property
    def Framework(self):  # pragma: no cover
        return FrameworkMappingDetails.make_one(self.boto3_raw_data["Framework"])

    @cached_property
    def CommonControl(self):  # pragma: no cover
        return CommonControlMappingDetails.make_one(
            self.boto3_raw_data["CommonControl"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.MappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.MappingTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class GetControlResponse:
    boto3_raw_data: "type_defs.GetControlResponseTypeDef" = dataclasses.field()

    Arn = field("Arn")
    Aliases = field("Aliases")
    Name = field("Name")
    Description = field("Description")
    Behavior = field("Behavior")
    Severity = field("Severity")

    @cached_property
    def RegionConfiguration(self):  # pragma: no cover
        return RegionConfiguration.make_one(self.boto3_raw_data["RegionConfiguration"])

    @cached_property
    def Implementation(self):  # pragma: no cover
        return ImplementationDetails.make_one(self.boto3_raw_data["Implementation"])

    @cached_property
    def Parameters(self):  # pragma: no cover
        return ControlParameter.make_many(self.boto3_raw_data["Parameters"])

    CreateTime = field("CreateTime")
    GovernedResources = field("GovernedResources")

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
class ListDomainsResponse:
    boto3_raw_data: "type_defs.ListDomainsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Domains(self):  # pragma: no cover
        return DomainSummary.make_many(self.boto3_raw_data["Domains"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

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
class ListControlMappingsRequestPaginate:
    boto3_raw_data: "type_defs.ListControlMappingsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def Filter(self):  # pragma: no cover
        return ControlMappingFilter.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListControlMappingsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListControlMappingsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainsRequestPaginate:
    boto3_raw_data: "type_defs.ListDomainsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectivesResponse:
    boto3_raw_data: "type_defs.ListObjectivesResponseTypeDef" = dataclasses.field()

    @cached_property
    def Objectives(self):  # pragma: no cover
        return ObjectiveSummary.make_many(self.boto3_raw_data["Objectives"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListObjectivesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectivesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCommonControlsResponse:
    boto3_raw_data: "type_defs.ListCommonControlsResponseTypeDef" = dataclasses.field()

    @cached_property
    def CommonControls(self):  # pragma: no cover
        return CommonControlSummary.make_many(self.boto3_raw_data["CommonControls"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCommonControlsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCommonControlsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCommonControlsRequestPaginate:
    boto3_raw_data: "type_defs.ListCommonControlsRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def CommonControlFilter(self):  # pragma: no cover
        return CommonControlFilter.make_one(self.boto3_raw_data["CommonControlFilter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.ListCommonControlsRequestPaginateTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCommonControlsRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListCommonControlsRequest:
    boto3_raw_data: "type_defs.ListCommonControlsRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def CommonControlFilter(self):  # pragma: no cover
        return CommonControlFilter.make_one(self.boto3_raw_data["CommonControlFilter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListCommonControlsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListCommonControlsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListControlsRequestPaginate:
    boto3_raw_data: "type_defs.ListControlsRequestPaginateTypeDef" = dataclasses.field()

    @cached_property
    def Filter(self):  # pragma: no cover
        return ControlFilter.make_one(self.boto3_raw_data["Filter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListControlsRequestPaginateTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListControlsRequestPaginateTypeDef"]
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

    NextToken = field("NextToken")
    MaxResults = field("MaxResults")

    @cached_property
    def Filter(self):  # pragma: no cover
        return ControlFilter.make_one(self.boto3_raw_data["Filter"])

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
class ListControlsResponse:
    boto3_raw_data: "type_defs.ListControlsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Controls(self):  # pragma: no cover
        return ControlSummary.make_many(self.boto3_raw_data["Controls"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

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
class ListObjectivesRequestPaginate:
    boto3_raw_data: "type_defs.ListObjectivesRequestPaginateTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ObjectiveFilter(self):  # pragma: no cover
        return ObjectiveFilter.make_one(self.boto3_raw_data["ObjectiveFilter"])

    @cached_property
    def PaginationConfig(self):  # pragma: no cover
        return PaginatorConfig.make_one(self.boto3_raw_data["PaginationConfig"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.ListObjectivesRequestPaginateTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectivesRequestPaginateTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListObjectivesRequest:
    boto3_raw_data: "type_defs.ListObjectivesRequestTypeDef" = dataclasses.field()

    MaxResults = field("MaxResults")
    NextToken = field("NextToken")

    @cached_property
    def ObjectiveFilter(self):  # pragma: no cover
        return ObjectiveFilter.make_one(self.boto3_raw_data["ObjectiveFilter"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListObjectivesRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListObjectivesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ControlMapping:
    boto3_raw_data: "type_defs.ControlMappingTypeDef" = dataclasses.field()

    ControlArn = field("ControlArn")
    MappingType = field("MappingType")

    @cached_property
    def Mapping(self):  # pragma: no cover
        return Mapping.make_one(self.boto3_raw_data["Mapping"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ControlMappingTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ControlMappingTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListControlMappingsResponse:
    boto3_raw_data: "type_defs.ListControlMappingsResponseTypeDef" = dataclasses.field()

    @cached_property
    def ControlMappings(self):  # pragma: no cover
        return ControlMapping.make_many(self.boto3_raw_data["ControlMappings"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    NextToken = field("NextToken")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListControlMappingsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListControlMappingsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
