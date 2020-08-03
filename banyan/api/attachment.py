from typing import List

from banyan.model.attachment import Attachment


class AttachmentAPI:
    def __init__(self, client):
        self._client = client

    def list(self) -> List[Attachment]:
        response_json = self._client.api_request('GET', '/policy/attachment')
        return Attachment.Schema().load(response_json, many=True)
