import unittest
from banyan.model.policy import Policy, Conditions, Tags, PolicyInfo
from banyan.model import API_VERSION


class PolicyParserTest(unittest.TestCase):
    def test_parse_web_policy(self):
        p: Policy = Policy.Schema().loads(open("tests/data/policy_web.json").read())
        self.assertEqual(p.apiVersion, API_VERSION)
        self.assertEqual(p.kind, Policy.KIND)
        self.assertEqual(p.metadata.name, "jupyter-allow")
        self.assertEqual(p.metadata.tags.template, Tags.TEMPLATE_USER)
        self.assertEqual(p.metadata.tags.template, p.type)
        self.assertEqual(
            p.spec.options.disable_tls_client_authentication, True)
        self.assertEqual(p.spec.options.l7_protocol, "http")
        self.assertEqual(len(p.spec.access), 1)
        a0 = p.spec.access[0]
        self.assertEqual(a0.rules.conditions.trust_level,
                         Conditions.TRUST_LEVEL_LOW)
        self.assertEqual(a0.roles, ["ANY"])
        self.assertEqual(len(a0.rules.l7_access), 1)
        r0 = a0.rules.l7_access[0]
        self.assertEqual(r0.resources, ["*"])
        self.assertEqual(r0.actions, ["*"])

    def test_parse_info(self):
        i: PolicyInfo = PolicyInfo.Schema().loads((open("tests/data/policyinfo.json").read()))
        self.assertEqual(i.name, "nginx-stage-mesh")
        self.assertEqual(i.policy.name(), "nginx-stage-mesh")
