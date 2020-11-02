import unittest
from typing import List

from banyan.model import API_VERSION
from banyan.model.attachment import Attachment, AttachmentType
from banyan.model.service import Service, ServiceInfo, Tags
from tests.parsing import load_testdata


class ServiceParserTest(unittest.TestCase):
    SERVICE_NAME = "jenkins"
    SERVICE_DOMAIN = "jenkins.bnndemos.com"

    def test_parse_web_service(self):
        s: Service = Service.Schema().loads(load_testdata("tests/data/service_web.json"))
        self.assertEqual(API_VERSION, s.apiVersion)
        self.assertEqual(ServiceParserTest.SERVICE_NAME, s.metadata.name)
        self.assertEqual(ServiceParserTest.SERVICE_DOMAIN, s.metadata.tags.domain)
        self.assertEqual(Tags.TEMPLATE_WEB, s.metadata.tags.template)
        self.assertEqual(Tags.APP_TYPE_WEB, s.metadata.tags.service_app_type)

    def test_parse_info(self):
        i: ServiceInfo = ServiceInfo.Schema().loads(load_testdata("tests/data/serviceinfo.json"))
        self.assertEqual(ServiceParserTest.SERVICE_NAME, i.service_name)
        self.assertEqual(ServiceParserTest.SERVICE_NAME, i.service.name)

    def test_parse_attachments(self):
        a: List[Attachment] = Attachment.Schema().loads(load_testdata("tests/data/attachments.json"), many=True)
        self.assertEqual(13, len(a))
        self.assertEqual("005b23d0-3f5a-471a-8c7a-05f4599c5453", str(a[0].policy_id))
        self.assertEqual("vault-api", a[0].attached_to_name)
        self.assertEqual("vault-api.us-east-1.bnn", a[0].attached_to_id)
        self.assertEqual(AttachmentType.SERVICE, a[0].attached_to_type)
        self.assertEqual(True, a[0].enabled)


class TagParserTest(unittest.TestCase):
    def test_parse_tags(self):
        t: Tags = Tags.Schema().loads(load_testdata("tests/data/service_tags.json"))
        self.assertEqual(ServiceParserTest.SERVICE_DOMAIN, t.domain)
        self.assertEqual(Tags.TEMPLATE_WEB, t.template)
        self.assertEqual(Tags.APP_TYPE_WEB, t.service_app_type)
