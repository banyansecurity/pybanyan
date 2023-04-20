from banyan.api import BanyanApiClient
c = BanyanApiClient()
for service in c.services_web.list():
    print(service.name)
