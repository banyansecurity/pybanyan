"""Handle Cloud Resource APIs
Returns:
    [type]: [description]
"""
import json


class CloudInventoryAPI:
    def __init__(self, client):
        self._client = client
        self.list_uri = '/cloud_resource/inventory'

    def list(self, include_tags=None, tag_name=None, tag_value=None,
             resource_type=None) -> list:
        list_url = self.list_uri
        payload = []
        if include_tags:
            payload.append(f"include_tags={include_tags}")

        if tag_name:
            payload.append(f"tag_name={tag_name}")

        if tag_value:
            payload.append(f"tag_value={tag_value}")

        if resource_type:
            payload.append(f"resource_type={resource_type}")

        if len(payload) > 0:
            list_url = f"{list_url}?{'&'.join(payload)}"
        res = self._client.api_request('GET', list_url)
        if res['data']:
            response_json = list(res['data'])
            return response_json
        return []

    def create(self, cloud_resource) -> object:
        json_data = json.dumps(cloud_resource)
        response = self._client.api_request(
            'POST', self.list_uri, data=json_data)
        return response
