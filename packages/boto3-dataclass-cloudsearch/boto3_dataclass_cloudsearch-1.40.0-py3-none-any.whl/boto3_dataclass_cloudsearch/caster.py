# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_cloudsearch import type_defs as bs_td


class CLOUDSEARCHCaster:

    def build_suggesters(
        self,
        res: "bs_td.BuildSuggestersResponseTypeDef",
    ) -> "dc_td.BuildSuggestersResponse":
        return dc_td.BuildSuggestersResponse.make_one(res)

    def create_domain(
        self,
        res: "bs_td.CreateDomainResponseTypeDef",
    ) -> "dc_td.CreateDomainResponse":
        return dc_td.CreateDomainResponse.make_one(res)

    def define_analysis_scheme(
        self,
        res: "bs_td.DefineAnalysisSchemeResponseTypeDef",
    ) -> "dc_td.DefineAnalysisSchemeResponse":
        return dc_td.DefineAnalysisSchemeResponse.make_one(res)

    def define_expression(
        self,
        res: "bs_td.DefineExpressionResponseTypeDef",
    ) -> "dc_td.DefineExpressionResponse":
        return dc_td.DefineExpressionResponse.make_one(res)

    def define_index_field(
        self,
        res: "bs_td.DefineIndexFieldResponseTypeDef",
    ) -> "dc_td.DefineIndexFieldResponse":
        return dc_td.DefineIndexFieldResponse.make_one(res)

    def define_suggester(
        self,
        res: "bs_td.DefineSuggesterResponseTypeDef",
    ) -> "dc_td.DefineSuggesterResponse":
        return dc_td.DefineSuggesterResponse.make_one(res)

    def delete_analysis_scheme(
        self,
        res: "bs_td.DeleteAnalysisSchemeResponseTypeDef",
    ) -> "dc_td.DeleteAnalysisSchemeResponse":
        return dc_td.DeleteAnalysisSchemeResponse.make_one(res)

    def delete_domain(
        self,
        res: "bs_td.DeleteDomainResponseTypeDef",
    ) -> "dc_td.DeleteDomainResponse":
        return dc_td.DeleteDomainResponse.make_one(res)

    def delete_expression(
        self,
        res: "bs_td.DeleteExpressionResponseTypeDef",
    ) -> "dc_td.DeleteExpressionResponse":
        return dc_td.DeleteExpressionResponse.make_one(res)

    def delete_index_field(
        self,
        res: "bs_td.DeleteIndexFieldResponseTypeDef",
    ) -> "dc_td.DeleteIndexFieldResponse":
        return dc_td.DeleteIndexFieldResponse.make_one(res)

    def delete_suggester(
        self,
        res: "bs_td.DeleteSuggesterResponseTypeDef",
    ) -> "dc_td.DeleteSuggesterResponse":
        return dc_td.DeleteSuggesterResponse.make_one(res)

    def describe_analysis_schemes(
        self,
        res: "bs_td.DescribeAnalysisSchemesResponseTypeDef",
    ) -> "dc_td.DescribeAnalysisSchemesResponse":
        return dc_td.DescribeAnalysisSchemesResponse.make_one(res)

    def describe_availability_options(
        self,
        res: "bs_td.DescribeAvailabilityOptionsResponseTypeDef",
    ) -> "dc_td.DescribeAvailabilityOptionsResponse":
        return dc_td.DescribeAvailabilityOptionsResponse.make_one(res)

    def describe_domain_endpoint_options(
        self,
        res: "bs_td.DescribeDomainEndpointOptionsResponseTypeDef",
    ) -> "dc_td.DescribeDomainEndpointOptionsResponse":
        return dc_td.DescribeDomainEndpointOptionsResponse.make_one(res)

    def describe_domains(
        self,
        res: "bs_td.DescribeDomainsResponseTypeDef",
    ) -> "dc_td.DescribeDomainsResponse":
        return dc_td.DescribeDomainsResponse.make_one(res)

    def describe_expressions(
        self,
        res: "bs_td.DescribeExpressionsResponseTypeDef",
    ) -> "dc_td.DescribeExpressionsResponse":
        return dc_td.DescribeExpressionsResponse.make_one(res)

    def describe_index_fields(
        self,
        res: "bs_td.DescribeIndexFieldsResponseTypeDef",
    ) -> "dc_td.DescribeIndexFieldsResponse":
        return dc_td.DescribeIndexFieldsResponse.make_one(res)

    def describe_scaling_parameters(
        self,
        res: "bs_td.DescribeScalingParametersResponseTypeDef",
    ) -> "dc_td.DescribeScalingParametersResponse":
        return dc_td.DescribeScalingParametersResponse.make_one(res)

    def describe_service_access_policies(
        self,
        res: "bs_td.DescribeServiceAccessPoliciesResponseTypeDef",
    ) -> "dc_td.DescribeServiceAccessPoliciesResponse":
        return dc_td.DescribeServiceAccessPoliciesResponse.make_one(res)

    def describe_suggesters(
        self,
        res: "bs_td.DescribeSuggestersResponseTypeDef",
    ) -> "dc_td.DescribeSuggestersResponse":
        return dc_td.DescribeSuggestersResponse.make_one(res)

    def index_documents(
        self,
        res: "bs_td.IndexDocumentsResponseTypeDef",
    ) -> "dc_td.IndexDocumentsResponse":
        return dc_td.IndexDocumentsResponse.make_one(res)

    def list_domain_names(
        self,
        res: "bs_td.ListDomainNamesResponseTypeDef",
    ) -> "dc_td.ListDomainNamesResponse":
        return dc_td.ListDomainNamesResponse.make_one(res)

    def update_availability_options(
        self,
        res: "bs_td.UpdateAvailabilityOptionsResponseTypeDef",
    ) -> "dc_td.UpdateAvailabilityOptionsResponse":
        return dc_td.UpdateAvailabilityOptionsResponse.make_one(res)

    def update_domain_endpoint_options(
        self,
        res: "bs_td.UpdateDomainEndpointOptionsResponseTypeDef",
    ) -> "dc_td.UpdateDomainEndpointOptionsResponse":
        return dc_td.UpdateDomainEndpointOptionsResponse.make_one(res)

    def update_scaling_parameters(
        self,
        res: "bs_td.UpdateScalingParametersResponseTypeDef",
    ) -> "dc_td.UpdateScalingParametersResponse":
        return dc_td.UpdateScalingParametersResponse.make_one(res)

    def update_service_access_policies(
        self,
        res: "bs_td.UpdateServiceAccessPoliciesResponseTypeDef",
    ) -> "dc_td.UpdateServiceAccessPoliciesResponse":
        return dc_td.UpdateServiceAccessPoliciesResponse.make_one(res)


cloudsearch_caster = CLOUDSEARCHCaster()
