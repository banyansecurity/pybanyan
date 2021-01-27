import unittest
from typing import List

from banyan.model.event_v2 import EventV2, EventV2Severity
from tests.parsing import load_testdata


class EventV2ParserTest(unittest.TestCase):
    EVENT_ID = "26b10ef2-d31d-4ac1-bafa-7ee25da01722"

    def _test_specific_event(self, e):
        self.assertEqual(self.EVENT_ID, str(e.id))
        self.assertEqual(EventV2Severity.INFO, e.severity)
        self.assertIn("Banyan", e.user_principal.user.groups)
        self.assertIn("banyan", e.user_principal.user.roles)
        self.assertEqual("C02C40NTMD6M", e.user_principal.device.serial_number)
        self.assertIsNone(e.user_principal.device.last_mdm_data_synced_at)

    def test_parse_event(self):
        e: EventV2 = EventV2.Schema().loads(load_testdata("tests/data/event_v2.json"))
        self._test_specific_event(e)

    def test_parse_many(self):
        e: List[EventV2] = EventV2.Schema().loads(load_testdata("tests/data/events_v2.json"), many=True)
        self._test_specific_event(e[0])

    def test_parse_more(self):
        e: List[EventV2] = EventV2.Schema().loads(load_testdata("tests/data/more_events_v2.json"), many=True)
