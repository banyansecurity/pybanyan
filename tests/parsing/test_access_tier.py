import unittest

from banyan.model.access_tier import AccessTier, AccessTierInfo, AccessTierTunnel
from tests.parsing import load_testdata

class AccessTierParserTest(unittest.TestCase):
    AT_NAME = "GCP-USWest"

    def test_parse_spec(self):
        at: AccessTier = AccessTier.Schema().loads(load_testdata("tests/data/access_tier_spec.json"))
        self.assertEqual(AccessTier.API_VERSION, at.apiVersion)
        self.assertEqual(AccessTierParserTest.AT_NAME, at.name)

    def test_parse_info(self):
        ati: AccessTierInfo = AccessTierInfo.Schema().loads(load_testdata("tests/data/access_tier_info.json"))
        self.assertEqual(AccessTierParserTest.AT_NAME, ati.name)
        self.assertEqual(AccessTierParserTest.AT_NAME, ati.access_tier_spec.name)
