"""Handle Cloud Resource APIs
Returns:
    [type]: [description]
"""
import json
from banyan.core.exc import BanyanError


class ResourceAPI:
    def __init__(self, client):
        self._client = client
        self.find_uri = '/cloud_discovery/find'
        self.find_auto_uri = '/cloud_discovery/findmatch'
        self.spec_uri = '/cloud_discovery/spec'

    def find(self, tag_name: str, tag_value: str) -> object:
        find_uri = self.find_uri
        if tag_name is None:
            raise BanyanError('invalid or missing tag name')
        if tag_value is None:
            raise BanyanError('invalid or missing tag value')

        payload = []
        payload.append(f"tag_name={tag_name}")
        payload.append(f"tag_value={tag_value}")

        if len(payload) > 0:
            find_uri = f"{find_uri}?{'&'.join(payload)}"
        response = self._client.api_request('GET', find_uri)
        if response['error_code'] > 0:
            raise BanyanError(response['error_description'])
        return response

    def findAutoMatch(self) -> list:
        response = self._client.api_request('GET', self.find_auto_uri)
        if response['error_code'] > 0:
            raise BanyanError(response['error_description'])
        return response

    def add(self, tag_name: str, tag_value: str) -> object:
        if tag_name is None:
            raise BanyanError('invalid or missing tag_name')
        if tag_value is None:
            raise BanyanError('invalid or missing tag_value')
        tagData = {}
        tagData['name'] = tag_name
        tagData['value'] = tag_value
        json_data = json.dumps(tagData)
        return self._client.api_request('POST', self.spec_uri, data=json_data)

    def remove(self, tag_name: str, tag_value: str) -> object:
        if tag_name is None:
            raise BanyanError('invalid or missing tag_name')
        if tag_value is None:
            raise BanyanError('invalid or missing tag_value')
        tagData = {}
        tagData['name'] = tag_name
        tagData['value'] = tag_value
        jdata = json.dumps(tagData)
        return self._client.api_request('DELETE', self.spec_uri, data=jdata)
