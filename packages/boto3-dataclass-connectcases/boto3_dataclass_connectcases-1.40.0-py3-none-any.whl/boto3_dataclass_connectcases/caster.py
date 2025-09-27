# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_connectcases import type_defs as bs_td


class CONNECTCASESCaster:

    def batch_get_case_rule(
        self,
        res: "bs_td.BatchGetCaseRuleResponseTypeDef",
    ) -> "dc_td.BatchGetCaseRuleResponse":
        return dc_td.BatchGetCaseRuleResponse.make_one(res)

    def batch_get_field(
        self,
        res: "bs_td.BatchGetFieldResponseTypeDef",
    ) -> "dc_td.BatchGetFieldResponse":
        return dc_td.BatchGetFieldResponse.make_one(res)

    def batch_put_field_options(
        self,
        res: "bs_td.BatchPutFieldOptionsResponseTypeDef",
    ) -> "dc_td.BatchPutFieldOptionsResponse":
        return dc_td.BatchPutFieldOptionsResponse.make_one(res)

    def create_case(
        self,
        res: "bs_td.CreateCaseResponseTypeDef",
    ) -> "dc_td.CreateCaseResponse":
        return dc_td.CreateCaseResponse.make_one(res)

    def create_case_rule(
        self,
        res: "bs_td.CreateCaseRuleResponseTypeDef",
    ) -> "dc_td.CreateCaseRuleResponse":
        return dc_td.CreateCaseRuleResponse.make_one(res)

    def create_domain(
        self,
        res: "bs_td.CreateDomainResponseTypeDef",
    ) -> "dc_td.CreateDomainResponse":
        return dc_td.CreateDomainResponse.make_one(res)

    def create_field(
        self,
        res: "bs_td.CreateFieldResponseTypeDef",
    ) -> "dc_td.CreateFieldResponse":
        return dc_td.CreateFieldResponse.make_one(res)

    def create_layout(
        self,
        res: "bs_td.CreateLayoutResponseTypeDef",
    ) -> "dc_td.CreateLayoutResponse":
        return dc_td.CreateLayoutResponse.make_one(res)

    def create_related_item(
        self,
        res: "bs_td.CreateRelatedItemResponseTypeDef",
    ) -> "dc_td.CreateRelatedItemResponse":
        return dc_td.CreateRelatedItemResponse.make_one(res)

    def create_template(
        self,
        res: "bs_td.CreateTemplateResponseTypeDef",
    ) -> "dc_td.CreateTemplateResponse":
        return dc_td.CreateTemplateResponse.make_one(res)

    def get_case(
        self,
        res: "bs_td.GetCaseResponseTypeDef",
    ) -> "dc_td.GetCaseResponse":
        return dc_td.GetCaseResponse.make_one(res)

    def get_case_audit_events(
        self,
        res: "bs_td.GetCaseAuditEventsResponseTypeDef",
    ) -> "dc_td.GetCaseAuditEventsResponse":
        return dc_td.GetCaseAuditEventsResponse.make_one(res)

    def get_case_event_configuration(
        self,
        res: "bs_td.GetCaseEventConfigurationResponseTypeDef",
    ) -> "dc_td.GetCaseEventConfigurationResponse":
        return dc_td.GetCaseEventConfigurationResponse.make_one(res)

    def get_domain(
        self,
        res: "bs_td.GetDomainResponseTypeDef",
    ) -> "dc_td.GetDomainResponse":
        return dc_td.GetDomainResponse.make_one(res)

    def get_layout(
        self,
        res: "bs_td.GetLayoutResponseTypeDef",
    ) -> "dc_td.GetLayoutResponse":
        return dc_td.GetLayoutResponse.make_one(res)

    def get_template(
        self,
        res: "bs_td.GetTemplateResponseTypeDef",
    ) -> "dc_td.GetTemplateResponse":
        return dc_td.GetTemplateResponse.make_one(res)

    def list_case_rules(
        self,
        res: "bs_td.ListCaseRulesResponseTypeDef",
    ) -> "dc_td.ListCaseRulesResponse":
        return dc_td.ListCaseRulesResponse.make_one(res)

    def list_cases_for_contact(
        self,
        res: "bs_td.ListCasesForContactResponseTypeDef",
    ) -> "dc_td.ListCasesForContactResponse":
        return dc_td.ListCasesForContactResponse.make_one(res)

    def list_domains(
        self,
        res: "bs_td.ListDomainsResponseTypeDef",
    ) -> "dc_td.ListDomainsResponse":
        return dc_td.ListDomainsResponse.make_one(res)

    def list_field_options(
        self,
        res: "bs_td.ListFieldOptionsResponseTypeDef",
    ) -> "dc_td.ListFieldOptionsResponse":
        return dc_td.ListFieldOptionsResponse.make_one(res)

    def list_fields(
        self,
        res: "bs_td.ListFieldsResponseTypeDef",
    ) -> "dc_td.ListFieldsResponse":
        return dc_td.ListFieldsResponse.make_one(res)

    def list_layouts(
        self,
        res: "bs_td.ListLayoutsResponseTypeDef",
    ) -> "dc_td.ListLayoutsResponse":
        return dc_td.ListLayoutsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)

    def list_templates(
        self,
        res: "bs_td.ListTemplatesResponseTypeDef",
    ) -> "dc_td.ListTemplatesResponse":
        return dc_td.ListTemplatesResponse.make_one(res)

    def search_cases(
        self,
        res: "bs_td.SearchCasesResponseTypeDef",
    ) -> "dc_td.SearchCasesResponse":
        return dc_td.SearchCasesResponse.make_one(res)

    def search_related_items(
        self,
        res: "bs_td.SearchRelatedItemsResponseTypeDef",
    ) -> "dc_td.SearchRelatedItemsResponse":
        return dc_td.SearchRelatedItemsResponse.make_one(res)

    def tag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)

    def untag_resource(
        self,
        res: "bs_td.EmptyResponseMetadataTypeDef",
    ) -> "dc_td.EmptyResponseMetadata":
        return dc_td.EmptyResponseMetadata.make_one(res)


connectcases_caster = CONNECTCASESCaster()
