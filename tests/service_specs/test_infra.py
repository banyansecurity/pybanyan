import unittest

from banyan.model.service import Service
from banyan.model.service_infra import ServiceInfraSSH, ServiceInfraRDP, ServiceInfraK8S, ServiceInfraDatabase, ServiceInfraTCP
from tests.service_specs import load_service_spec, assert_specs_equal

class ServiceInfraSSHTest(unittest.TestCase):

    def test_ssh_at(self):
        svc_ssh_at = ServiceInfraSSH(
            name = "ssh-at",
            description = "pybanyan ssh-at",
            cluster = "cluster1",
            access_tier = "gcp-wg",
            domain = "test-ssh-at.bar.com",
            backend_http_connect = True,
            client_ssh_host_directive = "10.10.1.*"
        )
        svc_obj: Service = svc_ssh_at.service_obj()
        ref_obj: Service = Service.Schema().loads(load_service_spec("ssh-at.json"))
        #print()
        #print(ref_obj.metadata.tags)
        #print(svc_obj.metadata.tags)
        assert_specs_equal(self, ref_obj, svc_obj)

    def test_ssh_conn(self):
        svc_ssh_conn = ServiceInfraSSH(
            name = "ssh-conn",
            description = "pybanyan ssh-conn",
            cluster = "managed-cl-edge1",
            connector = "test-connector",
            domain = "test-ssh-conn" + ".tdupnsan.getbnn.com",
            backend_domain = "10.10.1.1",
            backend_port = 22
        )
        svc_obj: Service = svc_ssh_conn.service_obj()
        ref_obj: Service = Service.Schema().loads(load_service_spec("ssh-conn.json"))
        assert_specs_equal(self, ref_obj, svc_obj)


class ServiceInfraK8STest(unittest.TestCase):

    def test_k8s_conn(self):
        svc_k8s_conn = ServiceInfraK8S(
            name = "k8s-conn",
            description = "pybanyan k8s-conn",
            cluster = "managed-cl-edge1",
            connector = "test-connector",
            domain = "test-k8s-conn" + ".tdupnsan.getbnn.com",
            backend_dns_override_for_domain = "myoidcproxy.amazonaws.com",
            client_banyanproxy_listen_port = 9199,
            client_kube_cluster_name = "eks-hero",
            client_kube_ca_key = "AAAA1234"
        )
        svc_obj: Service = svc_k8s_conn.service_obj()
        ref_obj: Service = Service.Schema().loads(load_service_spec("k8s-conn.json"))
        #print()
        #print(ref_obj.spec.backend)
        #print(svc_obj.spec.backend)
        assert_specs_equal(self, ref_obj, svc_obj)


class ServiceInfraRDPTest(unittest.TestCase):

    def test_rdp_conn(self):
        svc_rdp_conn = ServiceInfraRDP(
            name = "rdp-conn",
            description = "pybanyan rdp-conn",
            cluster = "managed-cl-edge1",
            connector = "test-connector",
            domain = "test-rdp-conn" + ".tdupnsan.getbnn.com",
            backend_domain = "10.10.2.1",
            backend_port = 3309,
            client_banyanproxy_listen_port = 9109
        )
        svc_obj: Service = svc_rdp_conn.service_obj()
        ref_obj: Service = Service.Schema().loads(load_service_spec("rdp-conn.json"))
        assert_specs_equal(self, ref_obj, svc_obj)

    def test_rdp_collection(self):
        svc_rdp_collection = ServiceInfraRDP(
            name = "rdp-collection",
            description = "pybanyan rdp-collection",
            cluster = "managed-cl-edge1",
            connector = "test-connector",
            domain = "test-rdp-collection" + ".tdupnsan.getbnn.com",
            backend_http_connect = True,
            client_banyanproxy_listen_port = 9108
        )
        svc_obj: Service = svc_rdp_collection.service_obj()
        ref_obj: Service = Service.Schema().loads(load_service_spec("rdp-collection.json"))
        assert_specs_equal(self, ref_obj, svc_obj)

        
class ServiceInfraDatabaseTest(unittest.TestCase):

    def test_database_at(self):
        svc_database_conn = ServiceInfraDatabase(
            name = "database-conn",
            description = "pybanyan database-conn",
            cluster = "managed-cl-edge1",
            connector = "test-connector",
            domain = "test-database-conn" + ".tdupnsan.getbnn.com",
            backend_domain = "10.10.1.123",
            backend_port = 3306,
            client_banyanproxy_listen_port = 9299
        )
        svc_obj: Service = svc_database_conn.service_obj()
        ref_obj: Service = Service.Schema().loads(load_service_spec("database-conn.json"))
        assert_specs_equal(self, ref_obj, svc_obj)


class ServiceInfraTCPTest(unittest.TestCase):

    def test_tcp_at(self):
        svc_tcp_at = ServiceInfraTCP(
            name = "tcp-at",
            description = "pybanyan tcp-at",
            cluster = "cluster1",
            access_tier = "gcp-wg",
            domain = "test-tcp-at.bar.com",
            backend_domain = "10.10.1.6",
            backend_port = 6006,
            client_banyanproxy_listen_port = 9119
        )
        svc_obj: Service = svc_tcp_at.service_obj()
        ref_obj: Service = Service.Schema().loads(load_service_spec("tcp-at.json"))
        assert_specs_equal(self, ref_obj, svc_obj)

    def test_tcp_conn(self):
        svc_tcp_conn = ServiceInfraTCP(
            name = "tcp-conn",
            description = "pybanyan tcp-conn",
            cluster = "managed-cl-edge1",
            connector = "test-connector",
            domain = "test-tcp-conn" + ".tdupnsan.getbnn.com",
            backend_domain = "10.10.1.100",
            backend_port = 5000,
            client_banyanproxy_listen_port = 9118
        )
        svc_obj: Service = svc_tcp_conn.service_obj()
        ref_obj: Service = Service.Schema().loads(load_service_spec("tcp-conn.json"))
        assert_specs_equal(self, ref_obj, svc_obj)
