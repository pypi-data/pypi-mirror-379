# -*- coding: utf-8 -*-
#
from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.MasterSelectWidget.MasterSelectWidget import MasterSelectWidget
from zope.interface import implements

from Products.urban import UrbanMessage as _
from Products.urban import interfaces
from Products.urban.config import PROJECTNAME
from Products.urban.config import URBAN_TYPES
from Products.urban.content.licence.GenericLicence import GenericLicence
from Products.urban.utils import setOptionalAttributes
from Products.urban.UrbanVocabularyTerm import UrbanVocabulary
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import (
    ReferenceBrowserWidget,
)
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from Products.MasterSelectWidget.MasterBooleanWidget import MasterBooleanWidget
from plone import api

from zope.i18n import translate

from collective.archetypes.select2.select2widget import MultiSelect2Widget


full_patrimony_slave_fields = (
    {
        "name": "patrimony_site",
        "action": "hide",
        "hide_values": ("none",),
    },
    {
        "name": "patrimony_architectural_complex",
        "action": "hide",
        "hide_values": ("none",),
    },
    {
        "name": "archeological_site",
        "action": "hide",
        "hide_values": ("none",),
    },
    {
        "name": "protection_zone",
        "action": "hide",
        "hide_values": ("none",),
    },
    {
        "name": "regional_inventory_building",
        "action": "hide",
        "hide_values": ("none",),
    },
    {
        "name": "small_popular_patrimony",
        "action": "hide",
        "hide_values": ("none",),
    },
    {
        "name": "communal_inventory",
        "action": "hide",
        "hide_values": ("none",),
    },
    {
        "name": "regional_inventory",
        "action": "hide",
        "hide_values": ("none",),
    },
    {
        "name": "patrimony_archaeological_map",
        "action": "hide",
        "hide_values": ("none",),
    },
    {
        "name": "patrimony_project_gtoret_1ha",
        "action": "hide",
        "hide_values": ("none",),
    },
    {
        "name": "observation",
        "action": "hide",
        "hide_values": ("none",),
    },
    {
        "name": "patrimony_monument",
        "action": "hide",
        "hide_values": ("none", "patrimonial"),
    },
    {
        "name": "classification_order_scope",
        "action": "hide",
        "hide_values": ("none", "patrimonial"),
    },
    {
        "name": "patrimony_analysis",
        "action": "hide",
        "hide_values": ("none",),
    },
    {
        "name": "patrimony_observation",
        "action": "hide",
        "hide_values": ("none",),
    },
)


slave_fields_bound_inspection = (
    {
        "name": "workLocations",
        "action": "hide",
        "hide_values": (True,),
    },
)

optional_fields = [
    "managed_by_prosecutor",
    "inspectionDescription",
    "patrimony",
    "archeological_site",
    "protection_zone",
    "regional_inventory_building",
    "small_popular_patrimony",
    "communal_inventory",
    "regional_inventory",
    "patrimony_analysis",
    "patrimony_architectural_complex",
    "patrimony_site",
    "patrimony_archaeological_map",
    "patrimony_project_gtoret_1ha",
    "patrimony_monument",
    "patrimony_observation",
    "classification_order_scope",
    "general_disposition",
]

schema = Schema(
    (
        StringField(
            name="referenceProsecution",
            widget=StringField._properties["widget"](
                size=60,
                label=_(
                    "urban_label_referenceProsecution", default="Referenceprosecution"
                ),
            ),
            schemata="urban_description",
        ),
        StringField(
            name="policeTicketReference",
            widget=StringField._properties["widget"](
                size=60,
                label=_(
                    "urban_label_policeTicketReference", default="Policeticketreference"
                ),
            ),
            schemata="urban_description",
        ),
        ReferenceField(
            name="bound_inspection",
            widget=ReferenceBrowserWidget(
                allow_search=True,
                allow_browse=False,
                force_close_on_insert=True,
                startup_directory="urban",
                show_indexes=False,
                wild_card_search=True,
                restrict_browsing_to_startup_directory=True,
                label=_("urban_label_bound_inspection", default="Bound inspection"),
            ),
            allowed_types=["Inspection"],
            schemata="urban_description",
            multiValued=False,
            relationship="bound_inspection",
        ),
        BooleanField(
            name="use_bound_inspection_infos",
            default=False,
            widget=MasterBooleanWidget(
                slave_fields=slave_fields_bound_inspection,
                label=_(
                    "urban_label_use_bound_inspection_infos",
                    default="Use_bound_inspection_infos",
                ),
            ),
            schemata="urban_description",
        ),
        ReferenceField(
            name="bound_licences",
            widget=ReferenceBrowserWidget(
                allow_search=True,
                allow_browse=False,
                force_close_on_insert=True,
                startup_directory="urban",
                show_indexes=False,
                wild_card_search=True,
                restrict_browsing_to_startup_directory=True,
                label=_("urban_label_bound_licences", default="Bound licences"),
            ),
            allowed_types=[
                t
                for t in URBAN_TYPES
                if t
                not in [
                    "Ticket",
                    "Inspection",
                    "ProjectMeeting",
                    "PatrimonyCertificate",
                    "CODT_UrbanCertificateOne",
                    "UrbanCertificateOne",
                ]
            ],
            schemata="urban_description",
            multiValued=True,
            relationship="bound_licences",
        ),
        BooleanField(
            name="managed_by_prosecutor",
            default=False,
            widget=BooleanField._properties["widget"](
                label=_(
                    "urban_label_managed_by_prosecutor", default="Managed_by_prosecutor"
                ),
            ),
            schemata="urban_description",
        ),
        TextField(
            name="inspectionDescription",
            widget=RichWidget(
                label=_(
                    "urban_label_inspectionDescription", default="Inspectiondescription"
                ),
            ),
            default_content_type="text/html",
            allowable_content_types=("text/html",),
            schemata="urban_inspection",
            default_method="getDefaultText",
            default_output_type="text/x-html-safe",
        ),
        StringField(
            name="patrimony",
            default="none",
            widget=MasterSelectWidget(
                slave_fields=full_patrimony_slave_fields,
                label=_("urban_label_patrimony", default="Patrimony"),
            ),
            vocabulary="list_patrimony_types",
            schemata="urban_patrimony",
        ),
        BooleanField(
            name="archeological_site",
            default=False,
            widget=BooleanField._properties["widget"](
                label=_("urban_label_archeological_site", default="Archeological_site"),
            ),
            schemata="urban_patrimony",
        ),
        BooleanField(
            name="protection_zone",
            default=False,
            widget=BooleanField._properties["widget"](
                label=_("urban_label_protection_zone", default="Protection_zone"),
            ),
            schemata="urban_patrimony",
        ),
        BooleanField(
            name="regional_inventory_building",
            default=False,
            widget=BooleanField._properties["widget"](
                label=_(
                    "urban_label_regional_inventory_building",
                    default="Regional_inventory_building",
                ),
            ),
            schemata="urban_patrimony",
        ),
        BooleanField(
            name="small_popular_patrimony",
            default=False,
            widget=BooleanField._properties["widget"](
                label=_(
                    "urban_label_small_popular_patrimony",
                    default="Small_popular_patrimony",
                ),
            ),
            schemata="urban_patrimony",
        ),
        BooleanField(
            name="communal_inventory",
            default=False,
            widget=BooleanField._properties["widget"](
                label=_("urban_label_communal_inventory", default="Communal_inventory"),
            ),
            schemata="urban_patrimony",
        ),
        BooleanField(
            name="regional_inventory",
            default=False,
            widget=BooleanField._properties["widget"](
                label=_("urban_label_regional_inventory", default="Regional_inventory"),
            ),
            schemata="urban_patrimony",
        ),
        TextField(
            name="patrimony_analysis",
            widget=RichWidget(
                label=_("urban_label_patrimony_analysis", default="Patrimony_analysis"),
            ),
            default_content_type="text/html",
            allowable_content_types=("text/html",),
            schemata="urban_patrimony",
            default_method="getDefaultText",
            default_output_type="text/x-html-safe",
            accessor="PatrimonyAnalysis",
        ),
        BooleanField(
            name="patrimony_architectural_complex",
            default=False,
            widget=BooleanField._properties["widget"](
                label=_(
                    "urban_label_patrimony_architectural_complex",
                    default="Patrimony_architectural_complex",
                ),
            ),
            schemata="urban_patrimony",
        ),
        BooleanField(
            name="patrimony_site",
            default=False,
            widget=BooleanField._properties["widget"](
                label=_("urban_label_patrimony_site", default="Patrimony_site"),
            ),
            schemata="urban_patrimony",
        ),
        BooleanField(
            name="patrimony_archaeological_map",
            default=False,
            widget=BooleanField._properties["widget"](
                label=_(
                    "urban_label_patrimony_archaeological_map",
                    default="Patrimony_archaeological_map",
                ),
            ),
            schemata="urban_patrimony",
        ),
        BooleanField(
            name="patrimony_project_gtoret_1ha",
            default=False,
            widget=BooleanField._properties["widget"](
                label=_(
                    "urban_label_patrimony_project_gtoret_1ha",
                    default="Patrimony_project_gtoret_1ha",
                ),
            ),
            schemata="urban_patrimony",
        ),
        BooleanField(
            name="patrimony_monument",
            default=False,
            widget=BooleanField._properties["widget"](
                label=_("urban_label_patrimony_monument", default="Patrimony_monument"),
            ),
            schemata="urban_patrimony",
        ),
        TextField(
            name="patrimony_observation",
            widget=RichWidget(
                label=_(
                    "urban_label_patrimony_observation", default="Patrimony_observation"
                ),
            ),
            default_content_type="text/html",
            allowable_content_types=("text/html",),
            schemata="urban_patrimony",
            default_method="getDefaultText",
            default_output_type="text/x-html-safe",
            accessor="PatrimonyObservation",
        ),
        LinesField(
            name="classification_order_scope",
            widget=MultiSelect2Widget(
                format="checkbox",
                label=_(
                    "urban_label_classification_order_scope",
                    default="Classification_order_scope",
                ),
            ),
            schemata="urban_patrimony",
            multiValued=1,
            vocabulary=UrbanVocabulary(
                "classification_order_scope", inUrbanConfig=False
            ),
            default_method="getDefaultValue",
        ),
        StringField(
            name="general_disposition",
            widget=SelectionWidget(
                label=_(
                    "urban_label_general_disposition", default="General_disposition"
                ),
            ),
            schemata="urban_patrimony",
            vocabulary=UrbanVocabulary(
                "general_disposition", inUrbanConfig=False, with_empty_value=True
            ),
        ),
    ),
)

setOptionalAttributes(schema, optional_fields)

Ticket_schema = (
    BaseFolderSchema.copy()
    + getattr(GenericLicence, "schema", Schema(())).copy()
    + schema.copy()
)


class Ticket(BaseFolder, GenericLicence, BrowserDefaultMixin):
    """ """

    security = ClassSecurityInfo()
    implements(interfaces.ITicket)

    meta_type = "Ticket"
    _at_rename_after_creation = True
    schema = Ticket_schema

    security.declarePublic("getApplicants")

    def getWorkLocations(self):
        if self.getUse_bound_inspection_infos():
            bound_licence = self.getBound_inspection()
            if bound_licence:
                return bound_licence.getWorkLocations()

        field = self.getField("workLocations")
        worklocations = field.get(self)
        return worklocations

    def getParcels(self):
        if self.getUse_bound_inspection_infos():
            bound_inspection = self.getBound_inspection()
            if bound_inspection:
                return bound_inspection.getParcels()

        return super(Ticket, self).getParcels()

    security.declarePublic("getOfficialParcels")

    def getOfficialParcels(self):
        if self.getUse_bound_inspection_infos():
            bound_inspection = self.getBound_inspection()
            if bound_inspection:
                return bound_inspection.getOfficialParcels()

        return super(Ticket, self).getOfficialParcels()

    security.declarePublic("updateTitle")

    def updateTitle(self):
        """
        Update the title to clearly identify the licence
        """
        proprietary = ""
        proprietaries = self.getProprietaries() or self.getApplicants()
        if proprietaries:
            proprietary = ", ".join([prop.Title() for prop in proprietaries])
        else:
            proprietary = translate(
                "no_proprietary_defined", "urban", context=self.REQUEST
            ).encode("utf8")
        if self.getWorkLocations():
            worklocations = self.getWorkLocationSignaletic().split("  et ")[0]
        else:
            worklocations = translate(
                "no_address_defined", "urban", context=self.REQUEST
            ).encode("utf8")
        title = "{}{} - {} - {} - {}".format(
            self.getReference(),
            self.getPoliceTicketReference()
            and " - " + self.getPoliceTicketReference()
            or "",
            self.getLicenceSubject(),
            worklocations,
            proprietary,
        )
        self.setTitle(title)
        self.reindexObject(
            idxs=(
                "Title",
                "sortable_title",
            )
        )

    security.declarePublic("getApplicants")

    def getApplicants(self):
        """ """
        applicants = super(Ticket, self).getApplicants()
        if self.getUse_bound_inspection_infos():
            bound_inspection = self.getBound_inspection()
            if bound_inspection:
                applicants.extend(bound_inspection.getApplicants())

        return list(set(applicants))

    security.declarePublic("get_applicants_history")

    def get_applicants_history(self):
        applicants = super(Ticket, self).get_applicants_history()
        if self.getUse_bound_inspection_infos():
            bound_inspection = self.getBound_inspection()
            if bound_inspection:
                applicants.extend(bound_inspection.get_applicants_history())

        return list(set(applicants))

    security.declarePublic("getProprietaries")

    def getProprietaries(self):
        """ """
        proprietaries = super(Ticket, self).getProprietaries()
        if self.getUse_bound_inspection_infos():
            bound_inspection = self.getBound_inspection()
            if bound_inspection:
                proprietaries.extend(bound_inspection.getProprietaries())

        return proprietaries

    security.declarePublic("getCorporations")

    def getCorporations(self):
        corporations = [
            corp
            for corp in self.objectValues("Corporation")
            if corp.portal_type == "Corporation"
            and api.content.get_state(corp) == "enabled"
        ]
        if self.getUse_bound_inspection_infos():
            bound_inspection = self.getBound_inspection()
            if bound_inspection:
                corporations.extend(bound_inspection.getCorporations())
        return list(set(corporations))

    security.declarePublic("get_corporations_history")

    def get_corporations_history(self):
        corporations = [
            corp
            for corp in self.objectValues("Corporation")
            if corp.portal_type == "Corporation"
            and api.content.get_state(corp) == "disabled"
        ]
        if self.getUse_bound_inspection_infos():
            bound_inspection = self.getBound_inspection()
            if bound_inspection:
                corporations.extend(bound_inspection.get_corporations_history())
        return list(set(corporations))

    security.declarePublic("getTenants")

    def getTenants(self):
        """
        Return the list of plaintiffs for the Licence
        """
        tenants = [
            app for app in self.objectValues("Applicant") if app.portal_type == "Tenant"
        ]
        corporations = self.getCorporationTenants()
        tenants.extend(corporations)
        if self.getUse_bound_inspection_infos():
            bound_inspection = self.getBound_inspection()
            if bound_inspection:
                tenants.extend(bound_inspection.getTenants())
        return list(set(tenants))

    security.declarePublic("getCorporationTenants")

    def getCorporationTenants(self):
        corporations = [
            corp
            for corp in self.objectValues("Corporation")
            if corp.portal_type == "CorporationTenant"
        ]
        return corporations

    security.declarePublic("getPlaintiffs")

    def getPlaintiffs(self):
        """
        Return the list of plaintiffs for the Licence
        """
        plaintiffs = [
            app
            for app in self.objectValues("Applicant")
            if app.portal_type == "Plaintiff"
        ]
        corporations = self.getCorporationPlaintiffs()
        plaintiffs.extend(corporations)
        if self.getUse_bound_inspection_infos():
            bound_inspection = self.getBound_inspection()
            if bound_inspection:
                plaintiffs.extend(bound_inspection.getPlaintiffs())
        return plaintiffs

    security.declarePublic("getCorporationPlaintiffs")

    def getCorporationPlaintiffs(self):
        corporations = [
            corp
            for corp in self.objectValues("Corporation")
            if corp.portal_type == "CorporationPlaintiff"
        ]
        return corporations

    def getLastDeposit(self):
        return self.getLastEvent(interfaces.IDepositEvent)

    def getLastMissingPart(self):
        return self.getLastEvent(interfaces.IMissingPartEvent)

    def getLastMissingPartDeposit(self):
        return self.getLastEvent(interfaces.IMissingPartDepositEvent)

    def getLastTheTicket(self):
        return self.getLastEvent(interfaces.ITheTicketEvent)

    def getLastSettlement(self):
        return self.getLastEvent(interfaces.ISettlementEvent)

    def getLastReportEvent(self):
        return self.getLastEvent(interfaces.IUrbanEventInspectionReport)

    def list_patrimony_types(self):
        """ """
        vocabulary = (
            ("none", "aucune incidence"),
            ("patrimonial", "incidence patrimoniale"),
            ("classified", "bien classé"),
        )
        return DisplayList(vocabulary)


registerType(Ticket, PROJECTNAME)


def finalize_schema(schema, folderish=False, moveDiscussion=True):
    """
    Finalizes the type schema to alter some fields
    """
    schema["folderCategory"].widget.visible = {"edit": "invisible", "view": "invisible"}
    schema.moveField("referenceProsecution", after="reference")
    schema.moveField("policeTicketReference", after="referenceProsecution")
    schema.moveField("bound_inspection", before="workLocations")
    schema.moveField("use_bound_inspection_infos", after="bound_inspection")
    schema.moveField("bound_licences", after="use_bound_inspection_infos")
    schema.moveField("managed_by_prosecutor", after="foldermanagers")
    schema.moveField("description", after="managed_by_prosecutor")
    schema.moveField("general_disposition", after="protectedBuilding")
    schema.moveField("patrimony", after="general_disposition")
    schema["parcellings"].widget.label = _("urban_label_parceloutlicences")
    schema["isInSubdivision"].widget.label = _("urban_label_is_in_parceloutlicences")
    schema["subdivisionDetails"].widget.label = _(
        "urban_label_parceloutlicences_details"
    )
    schema["pca"].vocabulary = UrbanVocabulary(
        "sols", vocType="PcaTerm", inUrbanConfig=False
    )
    schema["pca"].widget.label = _("urban_label_sol")
    schema["pcaZone"].vocabulary_factory = "urban.vocabulary.SOLZones"
    schema["pcaZone"].widget.label = _("urban_label_solZone")
    schema["isInPCA"].widget.label = _("urban_label_is_in_sol")
    schema["pcaDetails"].widget.label = _("urban_label_sol_details")
    schema["complementary_delay"].schemata = "urban_description"
    return schema


finalize_schema(Ticket_schema)
