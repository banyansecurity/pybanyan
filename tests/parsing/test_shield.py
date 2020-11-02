import unittest

from banyan.model.shield import Shield, ShieldLastActivity, ShieldConfig
from tests.parsing import load_testdata


class ShieldParserTest(unittest.TestCase):
    SHIELD_UUID = "d8b99ed8-7d0c-425f-a64f-ec5d66611c81"

    def test_parse_shield(self):
        s: Shield = Shield.Schema().loads(load_testdata("tests/data/shield.json"))
        self.assertEqual("us-east-1", s.name)
        self.assertEqual(self.SHIELD_UUID, str(s.id))

    def test_parse_last_activity(self):
        la: ShieldLastActivity = ShieldLastActivity.Schema().loads(load_testdata("tests/data/shield_activity.json"))
        self.assertEqual(self.SHIELD_UUID, str(la.uuid))

    def test_parse_config(self):
        c: ShieldConfig = ShieldConfig.Schema().loads(load_testdata("tests/data/shields.json"))
        self.assertIn(ShieldParserTest.SHIELD_UUID, [str(x.id) for x in c.shields])
        self.assertIn(ShieldParserTest.SHIELD_UUID, c.last_activity_map.keys())
        self.assertIn(ShieldParserTest.SHIELD_UUID, c.netagent_map.keys())
