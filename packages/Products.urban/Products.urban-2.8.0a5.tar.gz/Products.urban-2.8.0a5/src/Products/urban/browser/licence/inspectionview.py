# -*- coding: utf-8 -*-

from Products.urban.browser.licence.licenceview import LicenceView
from Products.urban.browser.table.urbantable import InspectionReportsTable
from Products.urban.browser.table.urbantable import PlaintiffTable
from Products.urban.browser.table.urbantable import TenantTable
from Products.CMFPlone import PloneMessageFactory as _

from plone import api


class InspectionView(LicenceView):
    def __init__(self, context, request):
        super(InspectionView, self).__init__(context, request)
        self.context = context
        self.request = request
        # disable portlets on licences
        self.request.set("disable_plone.rightcolumn", 1)
        self.request.set("disable_plone.leftcolumn", 1)

    def getMacroViewName(self):
        return "inspection-macros"

    def getExpirationDate(self):
        return None

    def getInquiriesForDisplay(self):
        """
        Returns the inquiries to display on the buildlicence_view
        """
        return [self.context]

    def getInspectionFields(self, exclude=[]):
        return self.getSchemataFields("urban_inspection", exclude)

    def renderTenantListing(self):
        if not self.context.getTenants():
            return ""
        contacttable = TenantTable(self.context, self.request)
        return self.renderListing(contacttable)

    def renderPlaintiffListing(self):
        if not self.context.getPlaintiffs():
            return ""
        contacttable = PlaintiffTable(self.context, self.request)
        return self.renderListing(contacttable)

    def renderRepportsListing(self):
        reporttable = InspectionReportsTable(self.context, self.request)
        return self.renderListing(reporttable)

    def getPatrimonyFields(self):
        return self.getSchemataFields(schemata="urban_patrimony")

    def getRankingOrdinanceLink(self):
        liendoc = "http://spw.wallonie.be/dgo4/index.php?thema=bc_pat&details=57081-CLT-0239-01"
        return liendoc

    def getRankingOrdinanceTitle(self):
        code_dgo4 = "code dgo4"
        libelle = "libelle"
        historique_dossier = "historique_dossier"
        liendoc = "liendoc"
        return "{} - {} - {} - {}".format(
            code_dgo4, libelle, historique_dossier, liendoc
        )
