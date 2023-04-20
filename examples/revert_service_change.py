from banyan.api import BanyanApiClient
from banyan.model.service_web import Service
import json

c = BanyanApiClient()
audit_client = c.audit
service_client = c.services_web

audit_rows = audit_client.list(event_type="registered_service", action="update", limit=2)
print("Found last 2 updates to registered_service:", audit_rows)

for idx, audit_row in enumerate(audit_rows):
	old = json.loads(audit_row.changes_old)
	new = json.loads(audit_row.changes_new)

	print("\n--> [%d] ServiceID: %s" % (idx+1, old["ServiceID"]))
	print("Current NEW Spec: ", new["ServiceSpec"])
	print("Reverting to OLD Spec: ", old["ServiceSpec"])

	svc = Service.Schema().load(json.loads(old["ServiceSpec"]))
	service_client.update(svc)
	