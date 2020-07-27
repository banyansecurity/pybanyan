import unittest
from banyan.model.service import Service, ServiceInfo, Tags
from banyan.model import API_VERSION
# import marshmallow


class ServiceParserTest(unittest.TestCase):
    def test_parse_web_service(self):
        # s: Service = Service.from_json_str(open("tests/data/service_web.json").read())
        s: Service = Service.Schema().loads(open("tests/data/service_web.json").read())
        self.assertEqual(API_VERSION, s.apiVersion)
        self.assertEqual("*.staging.earnest.com", s.metadata.name)
        self.assertEqual(Tags.TEMPLATE_WEB, s.metadata.tags.template)
        self.assertEqual(Tags.APP_TYPE_WEB, s.metadata.tags.service_app_type)

    def test_parse_info(self):
        # i: ServiceInfo = ServiceInfo.from_json_str((open("tests/data/serviceinfo.json").read()))
        i: ServiceInfo = ServiceInfo.Schema().loads(open("tests/data/serviceinfo.json").read())
        self.assertEqual("*.staging.earnest.com", i.name)
        self.assertEqual("*.staging.earnest.com", i.service.name)


class TagParserTest(unittest.TestCase):
    def test_parse_tags(self):
        s = Tags.Schema()
        t: Tags = s.loads(open("tests/data/service_tags.json").read())
        self.assertEqual("*.staging.earnest.com", t.domain)
        self.assertEqual(Tags.TEMPLATE_WEB, t.template)
        self.assertEqual(Tags.APP_TYPE_WEB, t.service_app_type)