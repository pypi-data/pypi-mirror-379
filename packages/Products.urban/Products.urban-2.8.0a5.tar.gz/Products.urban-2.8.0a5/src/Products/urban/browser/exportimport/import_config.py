# -*- coding: utf-8 -*-

from Acquisition import aq_parent
from OFS.interfaces import IApplication
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.urban.browser.exportimport.interfaces import IConfigImportMarker
from Products.urban.interfaces import ILicenceConfig
from Products.urban.interfaces import IUrbanTool
from collective.exportimport.import_content import ImportContent
from plone import api
from plone.restapi.interfaces import IDeserializeFromJson
from six.moves.urllib.parse import unquote
from six.moves.urllib.parse import urlparse
from zExceptions import NotFound
from zope.annotation.interfaces import IAnnotations
from zope.component import getMultiAdapter
from zope.component import getUtility
from zope.interface import alsoProvides
from zope.interface import noLongerProvides
from zope.schema.interfaces import IVocabularyFactory

import logging
import os


logger = logging.getLogger("Import Urban Config")

DEFERRED_KEY = "exportimport.deferred"
DEFERRED_FIELD_MAPPING = {
    "EventConfig": ["keyDates", "textDefaultValues"],
}
SIMPLE_SETTER_FIELDS = {"EventConfig": ["eventPortalType"]}


def to_str_utf8(value):
    return str(value).decode("utf-8")


class ConfigImportContent(ImportContent):
    template = ViewPageTemplateFile("templates/import_urban_config.pt")

    title = "Import Urban Config data"
    DROP_FIELDS = {
        "OpinionEventConfig": ["internal_service"],
        "UrbanTemplate": [
            "mailing_loop_template",
        ],
    }
    default_value_none = {
        "EventConfig": {"activatedFields": []},
        "TaskConfig": {
            "calculation_delay": [],
            "additional_delay_type": "absolute",
            "additional_delay": u"0",
        },
        "MacroTaskConfig": {
            "calculation_delay": [],
            "additional_delay_type": "absolute",
            "additional_delay": u"0",
        },
        "UrbanTemplate": {"style_modification_md5": u"no_md5"},
    }
    wrong_type = {
        "TaskConfig": {"additional_delay": {"type": str, "adapter": to_str_utf8}},
        "MacroTaskConfig": {"additional_delay": {"type": str, "adapter": to_str_utf8}},
    }

    def __call__(
        self,
        jsonfile=None,
        return_json=False,
        limit=None,
        server_file=None,
        iterator=None,
        import_to_current_lic_config_folder=False,
        import_in_same_instance=False,
        fix_parent_path=False,
    ):
        self.handle_missing_parent = int(self.request.get("handle_missing_parent", 0))
        self.handle_missing_parent_options = (
            ("0", "Raise error"),
            ("1", "Ignore error"),
        )
        self.import_to_current_lic_config_folder = import_to_current_lic_config_folder
        self.import_in_same_instance = import_in_same_instance
        self.fix_parent_path = fix_parent_path
        if not self.check_in_portal_urban():
            self.context = api.portal.get_tool("portal_urban")
        alsoProvides(self.request, IConfigImportMarker)
        output = super(ConfigImportContent, self).__call__(
            jsonfile, return_json, limit, server_file, iterator
        )
        noLongerProvides(self.request, IConfigImportMarker)
        return output

    def get_parent_as_container(self, item):
        if self.handle_missing_parent == 0:
            return super(ConfigImportContent, self).get_parent_as_container(item)

        if item["parent"].get("UID"):
            # For some reason api.content.get(UID=xxx) does not work sometimes...
            brains = api.content.find(UID=item["parent"]["UID"])
            if brains:
                return super(ConfigImportContent, self).get_parent_as_container(item)

        if item["parent"]["@type"] == "Plone Site":
            return super(ConfigImportContent, self).get_parent_as_container(item)

        # If the item is missing look for a item with the path of the old parent
        parent_url = unquote(item["parent"]["@id"])
        parent_path = urlparse(parent_url).path
        # physical path is bytes in Zope 2 (not in Zope 4)
        # so we need to encode parent_path before using plone.api.content.get
        if isinstance(self.context.getPhysicalPath()[0], bytes):
            parent_path = parent_path.encode("utf8")
        parent = None
        try:
            parent = api.content.get(path=parent_path)
        except NotFound:
            pass

        if parent:
            return super(ConfigImportContent, self).get_parent_as_container(item)

        return None

    def check_in_portal_urban(self):
        if IUrbanTool.providedBy(self.context):
            return True
        current = self.context
        while not IApplication.providedBy(current):
            if IUrbanTool.providedBy(current):
                return True
            current = aq_parent(current)
        return False

    def get_obj_from_path(self, path):
        if "portal_urban" not in path:
            return None
        split_path = path.split("portal_urban")[-1].lstrip("/")
        return api.content.get(path=os.path.join("/portal_urban/", split_path))

    def _get_uid_from_brain(self, brain):
        catalog = api.portal.get_tool("portal_catalog")
        rid = brain.getRID()
        return catalog.getIndexDataForRID(rid)["UID"]

    def get_uid_from_proximity_context(self, context, id, ignore_uid=[]):
        brains = api.content.find(context=context, portal_type="UrbanTemplate")
        for brain in brains:
            brain_uid = self._get_uid_from_brain(brain)
            if brain_uid in ignore_uid:
                continue
            obj = brain.getObject()
            merge_templates = obj.merge_templates
            for template in merge_templates:
                if template["template"] == "--NOVALUE--":
                    continue
                template_obj = api.content.get(UID=template["template"])
                if template_obj and template_obj.id == id:
                    return template["template"]
            ignore_uid.append(brain_uid)
        if ILicenceConfig.providedBy(context):
            return None
        return self.get_uid_from_proximity_context(aq_parent(context), id, ignore_uid)

    def get_template_uid(self, item, template):
        if isinstance(template["template"], str):
            obj = api.content.get(UID=template["template"])
            if obj:
                return template["template"]
            else:
                return None

        uid = template["template"]["uid"]
        obj = api.content.get(UID=uid)
        if obj:
            return uid

        context = self.get_obj_from_path(item["parent"]["@id"])
        if context:
            template_uid = self.get_uid_from_proximity_context(
                context, template["template"]["id"]
            )
            if template_uid:
                return template_uid

        path = template["template"]["path"]
        obj = self.get_obj_from_path(path)
        if not obj:
            return None
        return obj.UID()

    def dict_hook_urbantemplate(self, item):
        merge_templates = item.get("merge_templates", None)
        if merge_templates is None:
            return item
        output_template = []
        for template in merge_templates:
            uid = self.get_template_uid(item, template)
            if uid is None:
                msg = "Can't link the pod template : {}, in document : {}".format(
                    template.get("pod_context_name", "unknown"),
                    item.get("@id", "unknown").split("portal_urban")[-1],
                )
                logger.warning(msg)
                api.portal.show_message(msg, self.request, type="warning")
                uid = "--NOVALUE--"
            template["template"] = uid
            output_template.append(template)
        item["merge_templates"] = output_template
        return item

    def handle_environmentrubricterm_description(self, item):
        description = item.get("description", None)
        if not description:
            return item
        data_description = description.get("data", "")
        if not data_description.startswith("<p>"):
            data_description = u"<p>{}".format(data_description)
        if not data_description.endswith("</p>"):
            data_description = u"{}</p>".format(data_description)
        description["data"] = data_description
        description["content-type"] = u"text/html"
        item["description"] = description
        return item

    def dict_hook_environmentrubricterm(self, item):
        item = self.handle_environmentrubricterm_description(item)
        exploitation_condition = item.get("exploitationCondition", None)
        if not exploitation_condition:
            return item
        exploitation_condition_list = []
        for condition in exploitation_condition:
            obj = self.get_obj_from_path(condition)
            if not obj:
                logger.error(
                    "Can't find object for exploitationCondition : {}".format(condition)
                )
                continue
            exploitation_condition_list.append(obj.UID())
        item["exploitationCondition"] = exploitation_condition_list
        return item

    def handle_fix_parent_path(self, item):
        parent = item["parent"]
        path = parent["@id"]
        if "portal_urban" not in path:
            return item
        path_split = path.split("portal_urban")
        portal = api.portal.get()
        fix_path = os.path.join(
            portal.absolute_url(), "portal_urban", path_split[-1].lstrip("/")
        )
        parent["@id"] = fix_path
        item["parent"] = parent
        return item

    def global_dict_hook(self, item):
        item = self.handle_default_value_none(item)
        item = self.handle_scheduled_contenttype(item)
        item = self.handle_wrong_type(item)
        item = self.handle_textDefaultValues(item)

        if self.fix_parent_path:
            item = self.handle_fix_parent_path(item)

        if self.import_to_current_lic_config_folder:
            item = self.handle_change_id(item)

        if self.import_in_same_instance:
            del item["UID"]
            del item["parent"]["UID"]

        item[DEFERRED_KEY] = {}
        for fieldname in DEFERRED_FIELD_MAPPING.get(item["@type"], []):
            if item.get(fieldname):
                item[DEFERRED_KEY][fieldname] = item.pop(fieldname)

        simple = {}
        for fieldname in SIMPLE_SETTER_FIELDS.get("ALL", []):
            if fieldname in item:
                value = item.pop(fieldname)
                if value:
                    simple[fieldname] = value
        for fieldname in SIMPLE_SETTER_FIELDS.get(item["@type"], []):
            if fieldname in item:
                value = item.pop(fieldname)
                if value:
                    simple[fieldname] = value
        if simple:
            item["exportimport.simplesetter"] = simple

        return item

    def finish(self):
        self.results = []
        for brain in api.content.find(portal_type=DEFERRED_FIELD_MAPPING.keys()):
            obj = brain.getObject()
            self.import_deferred(obj)
        api.portal.show_message(
            "Imported deferred data for {} items!".format(len(self.results)),
            self.request,
        )

    def import_deferred(self, obj):
        annotations = IAnnotations(obj, {})
        deferred = annotations.get(DEFERRED_KEY, None)
        if not deferred:
            return
        deserializer = getMultiAdapter((obj, self.request), IDeserializeFromJson)
        try:
            obj = deserializer(validate_all=False, data=deferred)
        except Exception as e:
            logger.info(
                "Error while importing deferred data for %s",
                obj.absolute_url(),
                exc_info=True,
            )
            logger.info("Data: %s", deferred)
        else:
            self.results.append(obj.absolute_url())
        # cleanup
        del annotations[DEFERRED_KEY]

    def check_in_licence_config(self):
        if ILicenceConfig.providedBy(self.context):
            return True, self.context
        current = self.context
        while not IUrbanTool.providedBy(current):
            if ILicenceConfig.providedBy(current):
                return True, current
            current = aq_parent(current)
        return False, None

    def handle_change_id(self, item):
        check, context_licence = self.check_in_licence_config()
        licence_url = item.get("licence_url", None)
        if not check or not licence_url:
            return item
        context_path = context_licence.absolute_url()
        item["@id"] = item["@id"].replace(licence_url, context_path)
        item["parent"]["@id"] = item["parent"]["@id"].replace(licence_url, context_path)
        return item

    def handle_default_value_none(self, item):
        for key in self.default_value_none.get(item["@type"], {}):
            if item[key] is None:
                item[key] = self.default_value_none[item["@type"]][key]
        return item

    def handle_scheduled_contenttype(self, item):
        scheduled_contenttype = item.get("scheduled_contenttype", None)
        if scheduled_contenttype is None:
            return item

        scheduled_contenttype = (
            scheduled_contenttype[0],
            tuple(tuple(inner_list) for inner_list in scheduled_contenttype[1]),
        )
        factory_kwargs = item.get("factory_kwargs", {})
        factory_kwargs["scheduled_contenttype"] = scheduled_contenttype

        item["factory_kwargs"] = factory_kwargs
        return item

    def handle_wrong_type(self, item):
        config = self.wrong_type.get(item["@type"], {})
        for key in config:
            if key not in item:
                continue
            correct_type = config[key]["type"]
            if not isinstance(item[key], correct_type):
                adapter = config[key].get("adapter", None)
                if adapter is None:
                    item[key] = correct_type(item[key])
                else:
                    item[key] = adapter(item[key])
        return item

    def handle_textDefaultValues(self, item):
        if "textDefaultValues" not in item:
            return item
        text_default_values = item["textDefaultValues"]
        if not text_default_values:
            return item
        output = []
        for value in text_default_values:
            text = value["text"]
            fieldname = value["fieldname"]
            output.append(
                {
                    "text": text,
                    "fieldname": fieldname,
                }
            )
        item["textDefaultValues"] = output
        return item

    def global_obj_hook_before_deserializing(self, obj, item):
        """Hook to modify the created obj before deserializing the data."""
        # import simplesetter data before the rest
        for fieldname, value in item.get("exportimport.simplesetter", {}).items():
            setattr(obj, fieldname, value)
        return obj, item

    def global_obj_hook(self, obj, item):
        # Store deferred data in an annotation.
        deferred = item.get(DEFERRED_KEY, {})
        if deferred:
            annotations = IAnnotations(obj)
            annotations[DEFERRED_KEY] = {}
            for key, value in deferred.items():
                annotations[DEFERRED_KEY][key] = value

    def _handle_drop_in_dict(self, key, dict_value):
        dict_value.pop(key[0], None)
        return dict_value

    def _handle_drop_path(self, path, item):
        key = path[0]
        if type(item[key]) is list:
            new_list = []
            for value in item[key]:
                new_list.append(self._handle_drop_in_dict(path[1:], value))
            item[key] = new_list
        return item

    def handle_dropped(self, item):
        for key in self.DROP_FIELDS.get(item["@type"], []):
            split_key = key.split("/")
            if len(split_key) == 1:
                item.pop(key, None)
            if len(split_key) > 1:
                item = self._handle_drop_path(split_key, item)
        return item
