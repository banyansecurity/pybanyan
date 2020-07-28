import unittest

from banyan.model import API_VERSION
from banyan.model.policy import Policy, Conditions, Tags, PolicyInfo


class PolicyParserTest(unittest.TestCase):
    def test_parse_web_policy(self):
        p: Policy = Policy.Schema().loads(open("tests/data/policy_web.json").read())
        self.assertEqual(API_VERSION, p.apiVersion)
        self.assertEqual(Policy.KIND, p.kind)
        self.assertEqual("jupyter-allow", p.metadata.name)
        self.assertEqual(Tags.TEMPLATE_USER, p.metadata.tags.template)
        self.assertEqual(p.type, p.metadata.tags.template)
        self.assertEqual(True, p.spec.options.disable_tls_client_authentication)
        self.assertEqual("http", p.spec.options.l7_protocol)
        self.assertEqual(1, len(p.spec.access))
        a0 = p.spec.access[0]
        self.assertEqual(Conditions.TRUST_LEVEL_LOW, a0.rules.conditions.trust_level)
        self.assertEqual(["ANY"], a0.roles)
        self.assertEqual(1, len(a0.rules.l7_access))
        r0 = a0.rules.l7_access[0]
        self.assertEqual(["*"], r0.resources)
        self.assertEqual(["*"], r0.actions)

    def test_parse_info(self):
        i: PolicyInfo = PolicyInfo.Schema().loads((open("tests/data/policyinfo.json").read()))
        self.assertEqual("nginx-stage-mesh", i.name)
        self.assertEqual("nginx-stage-mesh", i.policy.name)
        self.assertEqual("0e599ef2-a9a3-45a2-855b-7c30e80f083f", str(i.id))
