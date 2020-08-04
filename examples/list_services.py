from banyan.api import BanyanApiClient
c = BanyanApiClient()
for service in c.services.list():
    print(service.name)
