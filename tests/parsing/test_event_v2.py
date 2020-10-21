import unittest

from typing import List
from banyan.model.event_v2 import EventV2


class EventV2ParserTest(unittest.TestCase):
    EVENT_ID = "26b10ef2-d31d-4ac1-bafa-7ee25da01722"

    def _test_specific_event(self, e):
        self.assertEqual(self.EVENT_ID, str(e.id))
        self.assertEqual(EventV2.SEVERITY_INFO, e.severity)
        self.assertIn("Banyan", e.user_principal.user.groups)
        self.assertIn("banyan", e.user_principal.user.roles)
        self.assertEqual("C02C40NTMD6M", e.user_principal.device.serial_number)
        self.assertIsNone(e.user_principal.device.last_mdm_data_synced_at)

    def test_parse_event(self):
        e: EventV2 = EventV2.Schema().loads(open("tests/data/event_v2.json").read())
        self._test_specific_event(e)

    def test_parse_many(self):
        e: List[EventV2] = EventV2.Schema().loads(open("tests/data/events_v2.json").read(), many=True)
        self._test_specific_event(e[0])
