import unittest

from banyan.model.service import Service
from banyan.model.service_web import ServiceWebStandard
from tests.service_specs import load_service_spec, assert_specs_equal

class ServiceWebTest(unittest.TestCase):

    def test_web_at(self):
        svc_web_at = ServiceWebStandard(
            name = "web-at",
            description = "pybanyan web-at",
            cluster = "cluster1",
            access_tier = "gcp-wg",
            domain = "test-web-at.bar.com",
            backend_domain = "10.10.1.1",
            backend_port = 8000
        )
        svc_obj: Service = svc_web_at.service_obj()
        ref_obj: Service = Service.Schema().loads(load_service_spec("web-at.json"))
        #print()
        #print(ref_obj.spec.backend)
        #print(svc_obj.spec.backend)
        assert_specs_equal(self, ref_obj, svc_obj)

    def test_web_conn(self):
        svc_web_conn = ServiceWebStandard(
            name = "web-conn",
            description = "pybanyan web-conn",
            cluster = "managed-cl-edge1",
            connector = "test-connector",
            domain = "test-web-conn" + ".tdupnsan.getbnn.com",
            backend_domain = "10.10.1.1",
            backend_port = 8080
        )
        svc_obj = svc_web_conn.service_obj()
        ref_obj: Service = Service.Schema().loads(load_service_spec("web-conn.json"))
        assert_specs_equal(self, ref_obj, svc_obj)

    def test_web_certs(self):
        svc_web_certs = ServiceWebStandard(
            name = "web-certs",
            description = "pybanyan web-certs",
            cluster = "managed-cl-edge1",
            connector = "test-connector",
            domain = "test-web-certs" + ".tdupnsan.getbnn.com",
            letsencrypt = True,
            backend_domain = "foo.backend.int",
            backend_port = 8080,
            backend_tls = True,
            backend_tls_insecure = True
        )
        svc_obj = svc_web_certs.service_obj()
        ref_obj: Service = Service.Schema().loads(load_service_spec("web-certs.json"))
        assert_specs_equal(self, ref_obj, svc_obj)
