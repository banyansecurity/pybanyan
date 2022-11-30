import unittest

from banyan.model.role import Role, Metadata, Tags, Spec, RoleInfo, RoleTemplate
from tests.parsing import load_testdata


class RoleGeneratorTest(unittest.TestCase):
    def test_generate_workload_role(self):
        # noinspection PyArgumentList
        r = Role(apiVersion=Role.API_VERSION, kind=Role.KIND, type=Role.TYPE,
                 metadata=Metadata(name="Gitlab", description="Gitlab",
                                   tags=Tags(RoleTemplate.USER)),
                 spec=Spec(group=["Security"], known_device_only=True))
        j: dict = Role.Schema().dump(r)
        self.assertEqual(Role.API_VERSION, j["apiVersion"])
        self.assertEqual(Role.KIND, j["kind"])
        self.assertIn("metadata", j.keys())
        self.assertEqual("Gitlab", j["metadata"]["name"])
        self.assertIn("spec", j.keys())
        self.assertEqual("Security", j["spec"]["group"][0])


class RoleParserTest(unittest.TestCase):
    def test_parse_workload_role(self):
        r: Role = Role.Schema().loads(load_testdata("tests/data/role_workload.json"))
        self.assertEqual(Role.KIND, r.kind)
        self.assertEqual("vault-client", r.metadata.name)
        self.assertEqual(1, len(r.spec.label_selector))
        self.assertEqual("vault-client",
                         r.spec.label_selector[0]["com.banyanops.hosttag.role"])

    def test_parse_group_role(self):
        r: Role = Role.Schema().loads(load_testdata("tests/data/role_group.json"))
        self.assertEqual(Role.KIND, r.kind)
        self.assertEqual("Gitlab", r.metadata.name)
        self.assertEqual(["Security"], r.spec.group)
        self.assertEqual([], r.spec.device_ownership)

    def test_parse_email_role(self):
        r: Role = Role.Schema().loads(load_testdata("tests/data/role_email.json"))
        self.assertEqual(Role.KIND, r.kind)
        self.assertEqual("Email", r.metadata.name)
        self.assertEqual([], r.spec.group)
        self.assertEqual([], r.spec.device_ownership, [])
        self.assertEqual(["kunal@banyansecurity.io"], r.spec.email)

    def test_parse_info(self):
        i: RoleInfo = RoleInfo.Schema().loads(load_testdata("tests/data/roleinfo.json"))
        self.assertEqual("SecurityTeam", i.role_name)
        self.assertEqual("SecurityTeam", i.role_spec.name)
