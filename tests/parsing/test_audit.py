import unittest
from typing import List

from banyan.model.audit import AuditEvent, AuditAction, AuditEventType
from banyan.model.service import ServiceInfo
from tests.parsing import load_testdata


class AuditEventParserTest(unittest.TestCase):
    EVENT_ID = "c5913103-67af-4669-bc8b-b14d4114f0c1"

    def _test_specific_event(self, e):
        self.assertEqual(self.EVENT_ID, str(e.id))
        self.assertEqual(AuditAction.CREATE, e.action)
        self.assertEqual(AuditEventType.REGISTERED_SERVICE, e.event_type)
        self.assertIsNone(e.changes_old)
        o = e.object_new  # type: ServiceInfo
        self.assertEqual(o.cluster_name, "us-west1")
        self.assertEqual(o.service_name, "test-api")
        self.assertIn("bnndemos.com", o.oidc_client.trust_cb)
        self.assertEqual(o.service_name, o.service_spec.name)
        self.assertEqual(o.service_name, o.service_spec.metadata.name)

    def test_parse_event(self):
        e: AuditEvent = AuditEvent.Schema().loads(load_testdata("tests/data/audit_event.json"))
        self._test_specific_event(e)

    def test_parse_many(self):
        e: List[AuditEvent] = AuditEvent.Schema().loads(load_testdata("tests/data/audit_events.json"), many=True)
        self._test_specific_event(e[0])
