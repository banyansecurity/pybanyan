import unittest

from banyan.model.connector import Connector, ConnectorInfo
from tests.parsing import load_testdata

class ConnectorParserTest(unittest.TestCase):
    CONN_NAME = "td-prod-AWS-Conn"

    def test_parse_spec(self):
        conn: Connector = Connector.Schema().loads(load_testdata("tests/data/connector_spec.json"))
        self.assertEqual(Connector.API_VERSION, conn.apiVersion)
        self.assertEqual(ConnectorParserTest.CONN_NAME, conn.name)


    def test_parse_info(self):
        conni: Connector = ConnectorInfo.Schema().loads(load_testdata("tests/data/connector_info.json"))
        self.assertEqual(ConnectorParserTest.CONN_NAME, conni.name)
        self.assertEqual(ConnectorParserTest.CONN_NAME, conni.connector_spec.name)
