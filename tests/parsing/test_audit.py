import unittest

from typing import List
from banyan.model.audit import AuditEvent
from marshmallow import INCLUDE


class AuditEventParserTest(unittest.TestCase):
    EVENT_ID = "c5913103-67af-4669-bc8b-b14d4114f0c1"

    def _test_specific_event(self, e):
        self.assertEqual(self.EVENT_ID, str(e.id))
        self.assertEqual(AuditEvent.ACTION_CREATE, e.action)
        self.assertEqual(AuditEvent.TYPE_REGISTERED_SERVICE, e.event_type)
        self.assertIsNone(e.changes_old)

    def test_parse_event(self):
        e: AuditEvent = AuditEvent.Schema().loads(open("tests/data/audit_event.json").read(), unknown=INCLUDE)
        self._test_specific_event(e)

    def test_parse_many(self):
        e: List[AuditEvent] = AuditEvent.Schema().loads(open("tests/data/audit_events.json").read(), many=True)
        self._test_specific_event(e[0])
