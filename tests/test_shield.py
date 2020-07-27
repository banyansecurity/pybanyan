import unittest
from banyan.model.shield import Shield, ShieldLastActivity, ShieldConfig


class ShieldParserTest(unittest.TestCase):
    SHIELD_UUID = "d8b99ed8-7d0c-425f-a64f-ec5d66611c81"

    def test_parse_shield(self):
        s: Shield = Shield.Schema().loads(open("tests/data/shield.json").read())
        self.assertEqual("us-east-1", s.name)
        self.assertEqual(self.SHIELD_UUID, str(s.uuid))

    def test_parse_last_activity(self):
        la: ShieldLastActivity = ShieldLastActivity.Schema().loads(open("tests/data/shield_activity.json").read())
        self.assertEqual(self.SHIELD_UUID, str(la.uuid))

    def test_parse_config(self):
        c: ShieldConfig = ShieldConfig.Schema().loads(open("tests/data/shields.json").read())
        self.assertIn(ShieldParserTest.SHIELD_UUID, [str(x.uuid) for x in c.shields])
        self.assertIn(ShieldParserTest.SHIELD_UUID, c.last_activity_map.keys())
        self.assertIn(ShieldParserTest.SHIELD_UUID, c.netagent_map.keys())

