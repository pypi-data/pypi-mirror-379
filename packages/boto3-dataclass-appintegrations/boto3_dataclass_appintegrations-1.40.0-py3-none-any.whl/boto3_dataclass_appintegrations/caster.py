# -*- coding: utf-8 -*-

import typing as T

from . import type_defs as dc_td

if T.TYPE_CHECKING:  # pragma: no cover
    from mypy_boto3_appintegrations import type_defs as bs_td


class APPINTEGRATIONSCaster:

    def create_application(
        self,
        res: "bs_td.CreateApplicationResponseTypeDef",
    ) -> "dc_td.CreateApplicationResponse":
        return dc_td.CreateApplicationResponse.make_one(res)

    def create_data_integration(
        self,
        res: "bs_td.CreateDataIntegrationResponseTypeDef",
    ) -> "dc_td.CreateDataIntegrationResponse":
        return dc_td.CreateDataIntegrationResponse.make_one(res)

    def create_data_integration_association(
        self,
        res: "bs_td.CreateDataIntegrationAssociationResponseTypeDef",
    ) -> "dc_td.CreateDataIntegrationAssociationResponse":
        return dc_td.CreateDataIntegrationAssociationResponse.make_one(res)

    def create_event_integration(
        self,
        res: "bs_td.CreateEventIntegrationResponseTypeDef",
    ) -> "dc_td.CreateEventIntegrationResponse":
        return dc_td.CreateEventIntegrationResponse.make_one(res)

    def get_application(
        self,
        res: "bs_td.GetApplicationResponseTypeDef",
    ) -> "dc_td.GetApplicationResponse":
        return dc_td.GetApplicationResponse.make_one(res)

    def get_data_integration(
        self,
        res: "bs_td.GetDataIntegrationResponseTypeDef",
    ) -> "dc_td.GetDataIntegrationResponse":
        return dc_td.GetDataIntegrationResponse.make_one(res)

    def get_event_integration(
        self,
        res: "bs_td.GetEventIntegrationResponseTypeDef",
    ) -> "dc_td.GetEventIntegrationResponse":
        return dc_td.GetEventIntegrationResponse.make_one(res)

    def list_application_associations(
        self,
        res: "bs_td.ListApplicationAssociationsResponseTypeDef",
    ) -> "dc_td.ListApplicationAssociationsResponse":
        return dc_td.ListApplicationAssociationsResponse.make_one(res)

    def list_applications(
        self,
        res: "bs_td.ListApplicationsResponseTypeDef",
    ) -> "dc_td.ListApplicationsResponse":
        return dc_td.ListApplicationsResponse.make_one(res)

    def list_data_integration_associations(
        self,
        res: "bs_td.ListDataIntegrationAssociationsResponseTypeDef",
    ) -> "dc_td.ListDataIntegrationAssociationsResponse":
        return dc_td.ListDataIntegrationAssociationsResponse.make_one(res)

    def list_data_integrations(
        self,
        res: "bs_td.ListDataIntegrationsResponseTypeDef",
    ) -> "dc_td.ListDataIntegrationsResponse":
        return dc_td.ListDataIntegrationsResponse.make_one(res)

    def list_event_integration_associations(
        self,
        res: "bs_td.ListEventIntegrationAssociationsResponseTypeDef",
    ) -> "dc_td.ListEventIntegrationAssociationsResponse":
        return dc_td.ListEventIntegrationAssociationsResponse.make_one(res)

    def list_event_integrations(
        self,
        res: "bs_td.ListEventIntegrationsResponseTypeDef",
    ) -> "dc_td.ListEventIntegrationsResponse":
        return dc_td.ListEventIntegrationsResponse.make_one(res)

    def list_tags_for_resource(
        self,
        res: "bs_td.ListTagsForResourceResponseTypeDef",
    ) -> "dc_td.ListTagsForResourceResponse":
        return dc_td.ListTagsForResourceResponse.make_one(res)


appintegrations_caster = APPINTEGRATIONSCaster()
