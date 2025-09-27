# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cloudsearch import type_defs


def field(name: str):
    def getter(self):
        return self.boto3_raw_data[name]

    return cached_property(getter)


@dataclasses.dataclass(frozen=True)
class OptionStatus:
    boto3_raw_data: "type_defs.OptionStatusTypeDef" = dataclasses.field()

    CreationDate = field("CreationDate")
    UpdateDate = field("UpdateDate")
    State = field("State")
    UpdateVersion = field("UpdateVersion")
    PendingDeletion = field("PendingDeletion")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.OptionStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.OptionStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisOptions:
    boto3_raw_data: "type_defs.AnalysisOptionsTypeDef" = dataclasses.field()

    Synonyms = field("Synonyms")
    Stopwords = field("Stopwords")
    StemmingDictionary = field("StemmingDictionary")
    JapaneseTokenizationDictionary = field("JapaneseTokenizationDictionary")
    AlgorithmicStemming = field("AlgorithmicStemming")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnalysisOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnalysisOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BuildSuggestersRequest:
    boto3_raw_data: "type_defs.BuildSuggestersRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BuildSuggestersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BuildSuggestersRequestTypeDef"]
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
class CreateDomainRequest:
    boto3_raw_data: "type_defs.CreateDomainRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")

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
class DateArrayOptions:
    boto3_raw_data: "type_defs.DateArrayOptionsTypeDef" = dataclasses.field()

    DefaultValue = field("DefaultValue")
    SourceFields = field("SourceFields")
    FacetEnabled = field("FacetEnabled")
    SearchEnabled = field("SearchEnabled")
    ReturnEnabled = field("ReturnEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DateArrayOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DateArrayOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DateOptions:
    boto3_raw_data: "type_defs.DateOptionsTypeDef" = dataclasses.field()

    DefaultValue = field("DefaultValue")
    SourceField = field("SourceField")
    FacetEnabled = field("FacetEnabled")
    SearchEnabled = field("SearchEnabled")
    ReturnEnabled = field("ReturnEnabled")
    SortEnabled = field("SortEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DateOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DateOptionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Expression:
    boto3_raw_data: "type_defs.ExpressionTypeDef" = dataclasses.field()

    ExpressionName = field("ExpressionName")
    ExpressionValue = field("ExpressionValue")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExpressionTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ExpressionTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAnalysisSchemeRequest:
    boto3_raw_data: "type_defs.DeleteAnalysisSchemeRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    AnalysisSchemeName = field("AnalysisSchemeName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAnalysisSchemeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAnalysisSchemeRequestTypeDef"]
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

    DomainName = field("DomainName")

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
class DeleteExpressionRequest:
    boto3_raw_data: "type_defs.DeleteExpressionRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    ExpressionName = field("ExpressionName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteExpressionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteExpressionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIndexFieldRequest:
    boto3_raw_data: "type_defs.DeleteIndexFieldRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    IndexFieldName = field("IndexFieldName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIndexFieldRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIndexFieldRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSuggesterRequest:
    boto3_raw_data: "type_defs.DeleteSuggesterRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    SuggesterName = field("SuggesterName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSuggesterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSuggesterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAnalysisSchemesRequest:
    boto3_raw_data: "type_defs.DescribeAnalysisSchemesRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    AnalysisSchemeNames = field("AnalysisSchemeNames")
    Deployed = field("Deployed")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAnalysisSchemesRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAnalysisSchemesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAvailabilityOptionsRequest:
    boto3_raw_data: "type_defs.DescribeAvailabilityOptionsRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    Deployed = field("Deployed")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAvailabilityOptionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAvailabilityOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDomainEndpointOptionsRequest:
    boto3_raw_data: "type_defs.DescribeDomainEndpointOptionsRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    Deployed = field("Deployed")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDomainEndpointOptionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainEndpointOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDomainsRequest:
    boto3_raw_data: "type_defs.DescribeDomainsRequestTypeDef" = dataclasses.field()

    DomainNames = field("DomainNames")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDomainsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeExpressionsRequest:
    boto3_raw_data: "type_defs.DescribeExpressionsRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    ExpressionNames = field("ExpressionNames")
    Deployed = field("Deployed")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeExpressionsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExpressionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIndexFieldsRequest:
    boto3_raw_data: "type_defs.DescribeIndexFieldsRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    FieldNames = field("FieldNames")
    Deployed = field("Deployed")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeIndexFieldsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIndexFieldsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScalingParametersRequest:
    boto3_raw_data: "type_defs.DescribeScalingParametersRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeScalingParametersRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScalingParametersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServiceAccessPoliciesRequest:
    boto3_raw_data: "type_defs.DescribeServiceAccessPoliciesRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    Deployed = field("Deployed")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeServiceAccessPoliciesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServiceAccessPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSuggestersRequest:
    boto3_raw_data: "type_defs.DescribeSuggestersRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")
    SuggesterNames = field("SuggesterNames")
    Deployed = field("Deployed")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSuggestersRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSuggestersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DocumentSuggesterOptions:
    boto3_raw_data: "type_defs.DocumentSuggesterOptionsTypeDef" = dataclasses.field()

    SourceField = field("SourceField")
    FuzzyMatching = field("FuzzyMatching")
    SortExpression = field("SortExpression")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DocumentSuggesterOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DocumentSuggesterOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainEndpointOptions:
    boto3_raw_data: "type_defs.DomainEndpointOptionsTypeDef" = dataclasses.field()

    EnforceHTTPS = field("EnforceHTTPS")
    TLSSecurityPolicy = field("TLSSecurityPolicy")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainEndpointOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainEndpointOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Limits:
    boto3_raw_data: "type_defs.LimitsTypeDef" = dataclasses.field()

    MaximumReplicationCount = field("MaximumReplicationCount")
    MaximumPartitionCount = field("MaximumPartitionCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LimitsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LimitsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ServiceEndpoint:
    boto3_raw_data: "type_defs.ServiceEndpointTypeDef" = dataclasses.field()

    Endpoint = field("Endpoint")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ServiceEndpointTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.ServiceEndpointTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DoubleArrayOptions:
    boto3_raw_data: "type_defs.DoubleArrayOptionsTypeDef" = dataclasses.field()

    DefaultValue = field("DefaultValue")
    SourceFields = field("SourceFields")
    FacetEnabled = field("FacetEnabled")
    SearchEnabled = field("SearchEnabled")
    ReturnEnabled = field("ReturnEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DoubleArrayOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DoubleArrayOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DoubleOptions:
    boto3_raw_data: "type_defs.DoubleOptionsTypeDef" = dataclasses.field()

    DefaultValue = field("DefaultValue")
    SourceField = field("SourceField")
    FacetEnabled = field("FacetEnabled")
    SearchEnabled = field("SearchEnabled")
    ReturnEnabled = field("ReturnEnabled")
    SortEnabled = field("SortEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DoubleOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DoubleOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IndexDocumentsRequest:
    boto3_raw_data: "type_defs.IndexDocumentsRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IndexDocumentsRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IndexDocumentsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntArrayOptions:
    boto3_raw_data: "type_defs.IntArrayOptionsTypeDef" = dataclasses.field()

    DefaultValue = field("DefaultValue")
    SourceFields = field("SourceFields")
    FacetEnabled = field("FacetEnabled")
    SearchEnabled = field("SearchEnabled")
    ReturnEnabled = field("ReturnEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IntArrayOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IntArrayOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IntOptions:
    boto3_raw_data: "type_defs.IntOptionsTypeDef" = dataclasses.field()

    DefaultValue = field("DefaultValue")
    SourceField = field("SourceField")
    FacetEnabled = field("FacetEnabled")
    SearchEnabled = field("SearchEnabled")
    ReturnEnabled = field("ReturnEnabled")
    SortEnabled = field("SortEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IntOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IntOptionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LatLonOptions:
    boto3_raw_data: "type_defs.LatLonOptionsTypeDef" = dataclasses.field()

    DefaultValue = field("DefaultValue")
    SourceField = field("SourceField")
    FacetEnabled = field("FacetEnabled")
    SearchEnabled = field("SearchEnabled")
    ReturnEnabled = field("ReturnEnabled")
    SortEnabled = field("SortEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LatLonOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LatLonOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LiteralArrayOptions:
    boto3_raw_data: "type_defs.LiteralArrayOptionsTypeDef" = dataclasses.field()

    DefaultValue = field("DefaultValue")
    SourceFields = field("SourceFields")
    FacetEnabled = field("FacetEnabled")
    SearchEnabled = field("SearchEnabled")
    ReturnEnabled = field("ReturnEnabled")

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.LiteralArrayOptionsTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.LiteralArrayOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class LiteralOptions:
    boto3_raw_data: "type_defs.LiteralOptionsTypeDef" = dataclasses.field()

    DefaultValue = field("DefaultValue")
    SourceField = field("SourceField")
    FacetEnabled = field("FacetEnabled")
    SearchEnabled = field("SearchEnabled")
    ReturnEnabled = field("ReturnEnabled")
    SortEnabled = field("SortEnabled")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.LiteralOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.LiteralOptionsTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextArrayOptions:
    boto3_raw_data: "type_defs.TextArrayOptionsTypeDef" = dataclasses.field()

    DefaultValue = field("DefaultValue")
    SourceFields = field("SourceFields")
    ReturnEnabled = field("ReturnEnabled")
    HighlightEnabled = field("HighlightEnabled")
    AnalysisScheme = field("AnalysisScheme")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TextArrayOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.TextArrayOptionsTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class TextOptions:
    boto3_raw_data: "type_defs.TextOptionsTypeDef" = dataclasses.field()

    DefaultValue = field("DefaultValue")
    SourceField = field("SourceField")
    ReturnEnabled = field("ReturnEnabled")
    SortEnabled = field("SortEnabled")
    HighlightEnabled = field("HighlightEnabled")
    AnalysisScheme = field("AnalysisScheme")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.TextOptionsTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.TextOptionsTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalingParameters:
    boto3_raw_data: "type_defs.ScalingParametersTypeDef" = dataclasses.field()

    DesiredInstanceType = field("DesiredInstanceType")
    DesiredReplicationCount = field("DesiredReplicationCount")
    DesiredPartitionCount = field("DesiredPartitionCount")

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ScalingParametersTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalingParametersTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAvailabilityOptionsRequest:
    boto3_raw_data: "type_defs.UpdateAvailabilityOptionsRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    MultiAZ = field("MultiAZ")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateAvailabilityOptionsRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAvailabilityOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceAccessPoliciesRequest:
    boto3_raw_data: "type_defs.UpdateServiceAccessPoliciesRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")
    AccessPolicies = field("AccessPolicies")

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateServiceAccessPoliciesRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceAccessPoliciesRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AccessPoliciesStatus:
    boto3_raw_data: "type_defs.AccessPoliciesStatusTypeDef" = dataclasses.field()

    Options = field("Options")

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AccessPoliciesStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AccessPoliciesStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AvailabilityOptionsStatus:
    boto3_raw_data: "type_defs.AvailabilityOptionsStatusTypeDef" = dataclasses.field()

    Options = field("Options")

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AvailabilityOptionsStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AvailabilityOptionsStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisScheme:
    boto3_raw_data: "type_defs.AnalysisSchemeTypeDef" = dataclasses.field()

    AnalysisSchemeName = field("AnalysisSchemeName")
    AnalysisSchemeLanguage = field("AnalysisSchemeLanguage")

    @cached_property
    def AnalysisOptions(self):  # pragma: no cover
        return AnalysisOptions.make_one(self.boto3_raw_data["AnalysisOptions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.AnalysisSchemeTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.AnalysisSchemeTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class BuildSuggestersResponse:
    boto3_raw_data: "type_defs.BuildSuggestersResponseTypeDef" = dataclasses.field()

    FieldNames = field("FieldNames")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.BuildSuggestersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.BuildSuggestersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IndexDocumentsResponse:
    boto3_raw_data: "type_defs.IndexDocumentsResponseTypeDef" = dataclasses.field()

    FieldNames = field("FieldNames")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.IndexDocumentsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IndexDocumentsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ListDomainNamesResponse:
    boto3_raw_data: "type_defs.ListDomainNamesResponseTypeDef" = dataclasses.field()

    DomainNames = field("DomainNames")

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ListDomainNamesResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ListDomainNamesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefineExpressionRequest:
    boto3_raw_data: "type_defs.DefineExpressionRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")

    @cached_property
    def Expression(self):  # pragma: no cover
        return Expression.make_one(self.boto3_raw_data["Expression"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DefineExpressionRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefineExpressionRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ExpressionStatus:
    boto3_raw_data: "type_defs.ExpressionStatusTypeDef" = dataclasses.field()

    @cached_property
    def Options(self):  # pragma: no cover
        return Expression.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.ExpressionStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ExpressionStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class Suggester:
    boto3_raw_data: "type_defs.SuggesterTypeDef" = dataclasses.field()

    SuggesterName = field("SuggesterName")

    @cached_property
    def DocumentSuggesterOptions(self):  # pragma: no cover
        return DocumentSuggesterOptions.make_one(
            self.boto3_raw_data["DocumentSuggesterOptions"]
        )

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SuggesterTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SuggesterTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainEndpointOptionsStatus:
    boto3_raw_data: "type_defs.DomainEndpointOptionsStatusTypeDef" = dataclasses.field()

    @cached_property
    def Options(self):  # pragma: no cover
        return DomainEndpointOptions.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DomainEndpointOptionsStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DomainEndpointOptionsStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainEndpointOptionsRequest:
    boto3_raw_data: "type_defs.UpdateDomainEndpointOptionsRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")

    @cached_property
    def DomainEndpointOptions(self):  # pragma: no cover
        return DomainEndpointOptions.make_one(
            self.boto3_raw_data["DomainEndpointOptions"]
        )

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDomainEndpointOptionsRequestTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainEndpointOptionsRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DomainStatus:
    boto3_raw_data: "type_defs.DomainStatusTypeDef" = dataclasses.field()

    DomainId = field("DomainId")
    DomainName = field("DomainName")
    RequiresIndexDocuments = field("RequiresIndexDocuments")
    ARN = field("ARN")
    Created = field("Created")
    Deleted = field("Deleted")

    @cached_property
    def DocService(self):  # pragma: no cover
        return ServiceEndpoint.make_one(self.boto3_raw_data["DocService"])

    @cached_property
    def SearchService(self):  # pragma: no cover
        return ServiceEndpoint.make_one(self.boto3_raw_data["SearchService"])

    Processing = field("Processing")
    SearchInstanceType = field("SearchInstanceType")
    SearchPartitionCount = field("SearchPartitionCount")
    SearchInstanceCount = field("SearchInstanceCount")

    @cached_property
    def Limits(self):  # pragma: no cover
        return Limits.make_one(self.boto3_raw_data["Limits"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.DomainStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.DomainStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IndexField:
    boto3_raw_data: "type_defs.IndexFieldTypeDef" = dataclasses.field()

    IndexFieldName = field("IndexFieldName")
    IndexFieldType = field("IndexFieldType")

    @cached_property
    def IntOptions(self):  # pragma: no cover
        return IntOptions.make_one(self.boto3_raw_data["IntOptions"])

    @cached_property
    def DoubleOptions(self):  # pragma: no cover
        return DoubleOptions.make_one(self.boto3_raw_data["DoubleOptions"])

    @cached_property
    def LiteralOptions(self):  # pragma: no cover
        return LiteralOptions.make_one(self.boto3_raw_data["LiteralOptions"])

    @cached_property
    def TextOptions(self):  # pragma: no cover
        return TextOptions.make_one(self.boto3_raw_data["TextOptions"])

    @cached_property
    def DateOptions(self):  # pragma: no cover
        return DateOptions.make_one(self.boto3_raw_data["DateOptions"])

    @cached_property
    def LatLonOptions(self):  # pragma: no cover
        return LatLonOptions.make_one(self.boto3_raw_data["LatLonOptions"])

    @cached_property
    def IntArrayOptions(self):  # pragma: no cover
        return IntArrayOptions.make_one(self.boto3_raw_data["IntArrayOptions"])

    @cached_property
    def DoubleArrayOptions(self):  # pragma: no cover
        return DoubleArrayOptions.make_one(self.boto3_raw_data["DoubleArrayOptions"])

    @cached_property
    def LiteralArrayOptions(self):  # pragma: no cover
        return LiteralArrayOptions.make_one(self.boto3_raw_data["LiteralArrayOptions"])

    @cached_property
    def TextArrayOptions(self):  # pragma: no cover
        return TextArrayOptions.make_one(self.boto3_raw_data["TextArrayOptions"])

    @cached_property
    def DateArrayOptions(self):  # pragma: no cover
        return DateArrayOptions.make_one(self.boto3_raw_data["DateArrayOptions"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IndexFieldTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls, boto3_raw_data_list: T.Optional[T.Iterable["type_defs.IndexFieldTypeDef"]]
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class ScalingParametersStatus:
    boto3_raw_data: "type_defs.ScalingParametersStatusTypeDef" = dataclasses.field()

    @cached_property
    def Options(self):  # pragma: no cover
        return ScalingParameters.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.ScalingParametersStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.ScalingParametersStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateScalingParametersRequest:
    boto3_raw_data: "type_defs.UpdateScalingParametersRequestTypeDef" = (
        dataclasses.field()
    )

    DomainName = field("DomainName")

    @cached_property
    def ScalingParameters(self):  # pragma: no cover
        return ScalingParameters.make_one(self.boto3_raw_data["ScalingParameters"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateScalingParametersRequestTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateScalingParametersRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeServiceAccessPoliciesResponse:
    boto3_raw_data: "type_defs.DescribeServiceAccessPoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccessPolicies(self):  # pragma: no cover
        return AccessPoliciesStatus.make_one(self.boto3_raw_data["AccessPolicies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeServiceAccessPoliciesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeServiceAccessPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateServiceAccessPoliciesResponse:
    boto3_raw_data: "type_defs.UpdateServiceAccessPoliciesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AccessPolicies(self):  # pragma: no cover
        return AccessPoliciesStatus.make_one(self.boto3_raw_data["AccessPolicies"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateServiceAccessPoliciesResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateServiceAccessPoliciesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAvailabilityOptionsResponse:
    boto3_raw_data: "type_defs.DescribeAvailabilityOptionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AvailabilityOptions(self):  # pragma: no cover
        return AvailabilityOptionsStatus.make_one(
            self.boto3_raw_data["AvailabilityOptions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeAvailabilityOptionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAvailabilityOptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateAvailabilityOptionsResponse:
    boto3_raw_data: "type_defs.UpdateAvailabilityOptionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AvailabilityOptions(self):  # pragma: no cover
        return AvailabilityOptionsStatus.make_one(
            self.boto3_raw_data["AvailabilityOptions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateAvailabilityOptionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateAvailabilityOptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class AnalysisSchemeStatus:
    boto3_raw_data: "type_defs.AnalysisSchemeStatusTypeDef" = dataclasses.field()

    @cached_property
    def Options(self):  # pragma: no cover
        return AnalysisScheme.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.AnalysisSchemeStatusTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.AnalysisSchemeStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefineAnalysisSchemeRequest:
    boto3_raw_data: "type_defs.DefineAnalysisSchemeRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")

    @cached_property
    def AnalysisScheme(self):  # pragma: no cover
        return AnalysisScheme.make_one(self.boto3_raw_data["AnalysisScheme"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DefineAnalysisSchemeRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefineAnalysisSchemeRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefineExpressionResponse:
    boto3_raw_data: "type_defs.DefineExpressionResponseTypeDef" = dataclasses.field()

    @cached_property
    def Expression(self):  # pragma: no cover
        return ExpressionStatus.make_one(self.boto3_raw_data["Expression"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DefineExpressionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefineExpressionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteExpressionResponse:
    boto3_raw_data: "type_defs.DeleteExpressionResponseTypeDef" = dataclasses.field()

    @cached_property
    def Expression(self):  # pragma: no cover
        return ExpressionStatus.make_one(self.boto3_raw_data["Expression"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteExpressionResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteExpressionResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeExpressionsResponse:
    boto3_raw_data: "type_defs.DescribeExpressionsResponseTypeDef" = dataclasses.field()

    @cached_property
    def Expressions(self):  # pragma: no cover
        return ExpressionStatus.make_many(self.boto3_raw_data["Expressions"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeExpressionsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeExpressionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefineSuggesterRequest:
    boto3_raw_data: "type_defs.DefineSuggesterRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")

    @cached_property
    def Suggester(self):  # pragma: no cover
        return Suggester.make_one(self.boto3_raw_data["Suggester"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DefineSuggesterRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefineSuggesterRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class SuggesterStatus:
    boto3_raw_data: "type_defs.SuggesterStatusTypeDef" = dataclasses.field()

    @cached_property
    def Options(self):  # pragma: no cover
        return Suggester.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.SuggesterStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[T.Iterable["type_defs.SuggesterStatusTypeDef"]],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDomainEndpointOptionsResponse:
    boto3_raw_data: "type_defs.DescribeDomainEndpointOptionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DomainEndpointOptions(self):  # pragma: no cover
        return DomainEndpointOptionsStatus.make_one(
            self.boto3_raw_data["DomainEndpointOptions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeDomainEndpointOptionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainEndpointOptionsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateDomainEndpointOptionsResponse:
    boto3_raw_data: "type_defs.UpdateDomainEndpointOptionsResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def DomainEndpointOptions(self):  # pragma: no cover
        return DomainEndpointOptionsStatus.make_one(
            self.boto3_raw_data["DomainEndpointOptions"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.UpdateDomainEndpointOptionsResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateDomainEndpointOptionsResponseTypeDef"]
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

    @cached_property
    def DomainStatus(self):  # pragma: no cover
        return DomainStatus.make_one(self.boto3_raw_data["DomainStatus"])

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
class DeleteDomainResponse:
    boto3_raw_data: "type_defs.DeleteDomainResponseTypeDef" = dataclasses.field()

    @cached_property
    def DomainStatus(self):  # pragma: no cover
        return DomainStatus.make_one(self.boto3_raw_data["DomainStatus"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteDomainResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteDomainResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeDomainsResponse:
    boto3_raw_data: "type_defs.DescribeDomainsResponseTypeDef" = dataclasses.field()

    @cached_property
    def DomainStatusList(self):  # pragma: no cover
        return DomainStatus.make_many(self.boto3_raw_data["DomainStatusList"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeDomainsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeDomainsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefineIndexFieldRequest:
    boto3_raw_data: "type_defs.DefineIndexFieldRequestTypeDef" = dataclasses.field()

    DomainName = field("DomainName")

    @cached_property
    def IndexField(self):  # pragma: no cover
        return IndexField.make_one(self.boto3_raw_data["IndexField"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DefineIndexFieldRequestTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefineIndexFieldRequestTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class IndexFieldStatus:
    boto3_raw_data: "type_defs.IndexFieldStatusTypeDef" = dataclasses.field()

    @cached_property
    def Options(self):  # pragma: no cover
        return IndexField.make_one(self.boto3_raw_data["Options"])

    @cached_property
    def Status(self):  # pragma: no cover
        return OptionStatus.make_one(self.boto3_raw_data["Status"])

    @classmethod
    def make_one(cls, boto3_raw_data: T.Optional["type_defs.IndexFieldStatusTypeDef"]):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.IndexFieldStatusTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeScalingParametersResponse:
    boto3_raw_data: "type_defs.DescribeScalingParametersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ScalingParameters(self):  # pragma: no cover
        return ScalingParametersStatus.make_one(
            self.boto3_raw_data["ScalingParameters"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional[
            "type_defs.DescribeScalingParametersResponseTypeDef"
        ],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeScalingParametersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class UpdateScalingParametersResponse:
    boto3_raw_data: "type_defs.UpdateScalingParametersResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def ScalingParameters(self):  # pragma: no cover
        return ScalingParametersStatus.make_one(
            self.boto3_raw_data["ScalingParameters"]
        )

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.UpdateScalingParametersResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.UpdateScalingParametersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefineAnalysisSchemeResponse:
    boto3_raw_data: "type_defs.DefineAnalysisSchemeResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AnalysisScheme(self):  # pragma: no cover
        return AnalysisSchemeStatus.make_one(self.boto3_raw_data["AnalysisScheme"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DefineAnalysisSchemeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefineAnalysisSchemeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteAnalysisSchemeResponse:
    boto3_raw_data: "type_defs.DeleteAnalysisSchemeResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AnalysisScheme(self):  # pragma: no cover
        return AnalysisSchemeStatus.make_one(self.boto3_raw_data["AnalysisScheme"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteAnalysisSchemeResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteAnalysisSchemeResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeAnalysisSchemesResponse:
    boto3_raw_data: "type_defs.DescribeAnalysisSchemesResponseTypeDef" = (
        dataclasses.field()
    )

    @cached_property
    def AnalysisSchemes(self):  # pragma: no cover
        return AnalysisSchemeStatus.make_many(self.boto3_raw_data["AnalysisSchemes"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls,
        boto3_raw_data: T.Optional["type_defs.DescribeAnalysisSchemesResponseTypeDef"],
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeAnalysisSchemesResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefineSuggesterResponse:
    boto3_raw_data: "type_defs.DefineSuggesterResponseTypeDef" = dataclasses.field()

    @cached_property
    def Suggester(self):  # pragma: no cover
        return SuggesterStatus.make_one(self.boto3_raw_data["Suggester"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DefineSuggesterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefineSuggesterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteSuggesterResponse:
    boto3_raw_data: "type_defs.DeleteSuggesterResponseTypeDef" = dataclasses.field()

    @cached_property
    def Suggester(self):  # pragma: no cover
        return SuggesterStatus.make_one(self.boto3_raw_data["Suggester"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteSuggesterResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteSuggesterResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeSuggestersResponse:
    boto3_raw_data: "type_defs.DescribeSuggestersResponseTypeDef" = dataclasses.field()

    @cached_property
    def Suggesters(self):  # pragma: no cover
        return SuggesterStatus.make_many(self.boto3_raw_data["Suggesters"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeSuggestersResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeSuggestersResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DefineIndexFieldResponse:
    boto3_raw_data: "type_defs.DefineIndexFieldResponseTypeDef" = dataclasses.field()

    @cached_property
    def IndexField(self):  # pragma: no cover
        return IndexFieldStatus.make_one(self.boto3_raw_data["IndexField"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DefineIndexFieldResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DefineIndexFieldResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DeleteIndexFieldResponse:
    boto3_raw_data: "type_defs.DeleteIndexFieldResponseTypeDef" = dataclasses.field()

    @cached_property
    def IndexField(self):  # pragma: no cover
        return IndexFieldStatus.make_one(self.boto3_raw_data["IndexField"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DeleteIndexFieldResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DeleteIndexFieldResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]


@dataclasses.dataclass(frozen=True)
class DescribeIndexFieldsResponse:
    boto3_raw_data: "type_defs.DescribeIndexFieldsResponseTypeDef" = dataclasses.field()

    @cached_property
    def IndexFields(self):  # pragma: no cover
        return IndexFieldStatus.make_many(self.boto3_raw_data["IndexFields"])

    @cached_property
    def ResponseMetadata(self):  # pragma: no cover
        return ResponseMetadata.make_one(self.boto3_raw_data["ResponseMetadata"])

    @classmethod
    def make_one(
        cls, boto3_raw_data: T.Optional["type_defs.DescribeIndexFieldsResponseTypeDef"]
    ):
        if boto3_raw_data is None:
            return None
        return cls(boto3_raw_data=boto3_raw_data)

    @classmethod
    def make_many(
        cls,
        boto3_raw_data_list: T.Optional[
            T.Iterable["type_defs.DescribeIndexFieldsResponseTypeDef"]
        ],
    ):
        if boto3_raw_data_list is None:
            return None
        return [
            cls(boto3_raw_data=boto3_raw_data) for boto3_raw_data in boto3_raw_data_list
        ]
