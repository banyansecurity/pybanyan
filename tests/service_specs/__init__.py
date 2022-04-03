import unittest

from banyan.model.service import Service

def load_service_spec(filespec: str) -> str:
    filespec = "tests/data/service_specs/" + filespec
    with open(filespec) as f:
        return f.read()

def assert_specs_equal(test_case: unittest.TestCase, ref_obj: Service, svc_obj: Service):
    test_case.assertDictEqual(vars(ref_obj.metadata), vars(svc_obj.metadata))
    test_case.assertDictEqual(vars(ref_obj.spec.attributes), vars(svc_obj.spec.attributes))
    test_case.assertDictEqual(vars(ref_obj.spec.backend), vars(svc_obj.spec.backend))
    test_case.assertDictEqual(vars(ref_obj.spec.cert_settings), vars(svc_obj.spec.cert_settings))
    test_case.assertDictEqual(vars(ref_obj.spec.http_settings), vars(svc_obj.spec.http_settings))
