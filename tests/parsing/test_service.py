from ipaddress import IPv4Interface
import unittest
from typing import List

from banyan.model.attachment import Attachment, AttachmentType
from banyan.model.service import ExemptedPaths, Pattern, Service, ServiceInfo, Tags, ServiceTemplate, ServiceAppType
from tests.parsing import load_testdata


class ServiceParserTest(unittest.TestCase):
    SERVICE_NAME = "jenkins"
    SERVICE_DOMAIN = "jenkins.bnndemos.com"

    def test_parse_web_service(self):
        s: Service = Service.Schema().loads(load_testdata("tests/data/service_web.json"))
        self.assertEqual(Service.API_VERSION, s.apiVersion)
        self.assertEqual(ServiceParserTest.SERVICE_NAME, s.metadata.name)
        self.assertEqual(ServiceParserTest.SERVICE_DOMAIN, s.metadata.tags.domain)
        self.assertEqual(ServiceTemplate.WEB, s.metadata.tags.template)
        self.assertEqual(ServiceAppType.WEB, s.metadata.tags.service_app_type)

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
        self.assertTrue(a[0].enabled)

    def test_exempted_paths(self):
        s: Service = Service.Schema().loads(load_testdata("tests/data/exempted_paths.json"))
        self.assertEqual("pipelines.bnndemos.com", s.name)
        self.assertTrue(s.spec.http_settings.exempted_paths.enabled)
        self.assertEqual(2, len(s.spec.http_settings.exempted_paths.patterns))
        ep0: Pattern = s.spec.http_settings.exempted_paths.patterns[0]
        self.assertEqual(2, len(ep0.source_cidrs))
        # self.assertIsInstance(ep0.source_cidrs[0], IPv4Interface)
        self.assertIn("12.34.56.0/24", ep0.source_cidrs)
        self.assertIn("56.78.90.12", ep0.source_cidrs)
        self.assertIn("/api/*", ep0.paths)
        self.assertEqual(1, len(ep0.hosts))
        self.assertEqual(1, len(ep0.hosts[0].target))
        self.assertEqual("https://pipelines.bnndemos.com:443", ep0.hosts[0].target[0])


class TagParserTest(unittest.TestCase):
    def test_parse_tags(self):
        t: Tags = Tags.Schema().loads(load_testdata("tests/data/service_tags.json"))
        self.assertEqual(ServiceParserTest.SERVICE_DOMAIN, t.domain)
        self.assertEqual(ServiceTemplate.WEB, t.template)
        self.assertEqual(ServiceAppType.WEB, t.service_app_type)
