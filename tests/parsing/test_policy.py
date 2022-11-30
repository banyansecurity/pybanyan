import unittest

from banyan.model.policy import Policy, PolicyInfo, Template
from banyan.model.trustscore import TrustLevel
from tests.parsing import load_testdata


class PolicyParserTest(unittest.TestCase):
    def test_parse_web_policy(self):
        p: Policy = Policy.Schema().loads(load_testdata("tests/data/policy_web.json"))
        self.assertEqual(Policy.API_VERSION, p.apiVersion)
        self.assertEqual(Policy.KIND, p.kind)
        self.assertEqual("jupyter-allow", p.metadata.name)
        self.assertEqual(Template.USER, p.metadata.tags.template)
        self.assertEqual(p.type, p.metadata.tags.template)
        self.assertEqual(True, p.spec.options.disable_tls_client_authentication)
        self.assertEqual("http", p.spec.options.l7_protocol)
        self.assertEqual(1, len(p.spec.access))
        a0 = p.spec.access[0]
        self.assertEqual(TrustLevel.LOW, a0.rules.conditions.trust_level)
        self.assertEqual(["ANY"], a0.roles)
        self.assertEqual(1, len(a0.rules.l7_access))
        r0 = a0.rules.l7_access[0]
        self.assertEqual(["*"], r0.resources)
        self.assertEqual(["*"], r0.actions)

    def test_parse_info(self):
        i: PolicyInfo = PolicyInfo.Schema().loads(load_testdata("tests/data/policyinfo.json"))
        self.assertEqual("nginx-stage-mesh", i.name)
        self.assertEqual("nginx-stage-mesh", i.policy.name)
        self.assertEqual("0e599ef2-a9a3-45a2-855b-7c30e80f083f", str(i.id))
