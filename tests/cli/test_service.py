# import unittest
#
# # noinspection PyPackageRequirements
# import pexpect
#
# from banyan.api import BanyanApiClient
#
#
# class ServiceCommandTest(unittest.TestCase):
#     SERVICE_NAME = 'foo'
#
#     def setUp(self) -> None:
#         c = BanyanApiClient()
#         if c.services.exists(self.SERVICE_NAME):
#             c.services.delete(self.SERVICE_NAME)
#
#     def test_service_cli(self):
#         child = pexpect.spawnu('python -m banyan.main service create @tests/data/service_create.json')
#         child.expect('"Description": "Test service"')
#         child.close()
#
#         child = pexpect.spawnu('python -m banyan.main service update @tests/data/service_update.json')
#         child.expect('"Description": "foobar"')
#         child.close()
#
#         child = pexpect.spawnu('python -m banyan.main service list')
#         child.expect(self.SERVICE_NAME)
#         child.close()
#
#         child = pexpect.spawnu(f'python -m banyan.main service get {self.SERVICE_NAME}')
#         child.expect(f'"description": "foobar"')
#         child.close()
#
#         child = pexpect.spawnu(f'python -m banyan.main service disable {self.SERVICE_NAME}')
#         child.expect('updated successfully')
#         child.close()
#
#         child = pexpect.spawnu(f'python -m banyan.main service disable {self.SERVICE_NAME}')
#         child.expect('no update was needed')
#         child.close()
#
#         child = pexpect.spawnu(f'python -m banyan.main service enable {self.SERVICE_NAME}')
#         child.expect('updated successfully')
#         child.close()
#
#         child = pexpect.spawnu(f'python -m banyan.main service enable {self.SERVICE_NAME}')
#         child.expect('no update was needed')
#         child.close()
#
#         child = pexpect.spawnu(f'python -m banyan.main service delete {self.SERVICE_NAME}')
#         child.expect('Successfully deleted registered service from db')
#         child.close()
#
#         child = pexpect.spawnu(f'python -m banyan.main service get {self.SERVICE_NAME}')
#         child.expect(f'does not exist: {self.SERVICE_NAME}')
#         child.close()
#
