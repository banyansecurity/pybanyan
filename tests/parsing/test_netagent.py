import unittest

from banyan.model.netagent import Netagent
from tests.parsing import load_testdata


class NetagentModelTest(unittest.TestCase):
    def test_parse_netagent(self):
        n: Netagent = Netagent.Schema().loads(load_testdata("tests/data/netagent.json"))
        self.assertEqual("ip-172-31-62-215.ec2.internal", n.hostname)
        self.assertEqual("Linux", n.host_data["Sysname"])
        self.assertEqual("transtar-test", n.site_name)
