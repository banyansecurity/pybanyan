import unittest
from banyan.model import cloud_resource

from banyan.model.cloud_resource import CloudResource, CloudResourceInfo, CloudResourceAssociateInfo
from tests.parsing import load_testdata

class CloudResourceParserTest(unittest.TestCase):

    def test_parse_cloud_resource(self):
        cr: CloudResourceInfo = CloudResourceInfo.Schema().loads(load_testdata("tests/data/cloud_resource.json"))
        self.assertEqual("1075cf45-6d65-42fb-b399-510cd3503b92", cr.id)
        self.assertEqual("AWS", cr.cloud_provider)
        self.assertEqual("EI-Crowdstrike Test", cr.tags[0].value)

    def test_parse_cloud_resource_service(self):
        cra: CloudResourceAssociateInfo = CloudResourceAssociateInfo.Schema().loads(load_testdata("tests/data/cloud_resource_service.json"))
        self.assertEqual("aff13145-e8a2-4bb5-aad1-542ba60b62a0", cra.id)
        self.assertEqual("e002082f-24af-4548-9396-7c582a8c13fe", cra.cloud_resource_id)
        self.assertEqual("dc-nginx.edge1.bnn", cra.service_id)
        self.assertEqual("published", cra.resource_status)
        self.assertFalse(hasattr(cra, 'status'))
