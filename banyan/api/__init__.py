import logging
import os
from typing import Dict, Any

import requests
from requests.auth import AuthBase

from banyan.api.attachment import AttachmentAPI
from banyan.api.device import DeviceAPI
from banyan.api.netagent import NetagentAPI
from banyan.api.policy import PolicyAPI
from banyan.api.role import RoleAPI
from banyan.api.service import ServiceAPI
from banyan.api.shield import ShieldAPI
from banyan.api.user import UserAPI
from banyan.core.exc import BanyanError


class BanyanApiClient:
    DEFAULT_API_URL = 'https://net.banyanops.com'
    JSON_TYPE = 'application/json'

    class _Auth(AuthBase):
        def __init__(self, parent) -> None:
            self._obj = parent

        def __call__(self, r: requests.Request) -> requests.Request:
            token = self._obj.access_token or self._obj.refresh_token
            r.headers['Authorization'] = f'Bearer {token}'
            return r

    def __init__(self, api_server_url: str = None, refresh_token: str = None, debug: bool = False,
                 log: logging.Logger = None) -> None:
        self._debug = debug
        self._log = log
        self._api_url = self._normalize_url(api_server_url or BanyanApiClient.DEFAULT_API_URL)
        self._access_token = None
        self._refresh_token = refresh_token
        if not self._refresh_token:
            raise BanyanError("Refresh token must be set")
        if self._debug:
            requests_log = logging.getLogger('requests.packages.urllib3')
            requests_log.setLevel(logging.DEBUG)
            requests_log.propagate = True
        self._http = self._create_session()
        self._services = ServiceAPI(self)
        self._policies = PolicyAPI(self)
        self._attach = AttachmentAPI(self)
        self._roles = RoleAPI(self)
        self._shields = ShieldAPI(self)
        self._agents = NetagentAPI(self)
        self._users = UserAPI(self)
        self._devices = DeviceAPI(self)

    # noinspection PyMethodMayBeStatic
    def _normalize_url(self, url: str) -> str:
        if '/api' not in url:
            url += '/api/v1'
        # if not url.endswith('/'):
        #     url += '/'
        return url

    def _create_session(self) -> requests.Session:
        http = requests.session()
        http.headers['Accept'] = 'application/json'
        http.auth = self._Auth(self)
        if self._debug:
            requests_log = logging.getLogger("requests.packages.urllib3")
            requests_log.setLevel(logging.DEBUG)
            requests_log.propagate = True
        return http

    def get_access_token(self) -> str:
        content = self._request('POST', '/refresh_token').json()
        self._access_token = content['Message']
        return self._access_token

    def _request(self, method: str, url: str, params: Dict[str, str] = None, data: Any = None,
                 headers: Dict[str, str] = None, cookies: Dict[str, str] = None,
                 files=None, auth=None, timeout=None, allow_redirects=True, proxies=None,
                 hooks=None, stream=None, verify=None, cert=None, json=None) -> requests.Response:
        if '://' not in url:
            url = self._api_url + url
        response = self._http.request(method, url, params, data, headers, cookies, files, auth or self._http.auth,
                                      timeout, allow_redirects, proxies, hooks, stream, verify, cert, json)
        if response.status_code >= 400:
            try:
                content = response.json()
                if 'Message' in content:
                    raise BanyanError(f'{response.status_code} Client Error: {response.reason} for '
                                      f'url: {response.url}: {content["Message"]}')
            except ValueError:
                raise BanyanError(f'{response.status_code} Client Error: {response.reason} for url: {response.url}')
        return response

    def api_request(self, method: str, uri: str, params: Dict[str, str] = None, data: Any = None,
                    json: Any = None, headers: Dict[str, str] = None, accept: str = None) -> requests.Response:
        if not self._access_token:
            self.get_access_token()
        headers = headers or dict()
        headers['Accept'] = accept or self.JSON_TYPE
        if data:
            headers['Content-Type'] = self.JSON_TYPE
        return self._request(method=method, url=uri, params=params, data=data, headers=headers, json=json).json()

    @property
    def access_token(self) -> str:
        return self._access_token

    @property
    def refresh_token(self) -> str:
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, value: str) -> None:
        self._refresh_token = value
        if self._access_token:
            self._access_token = None
            self.get_access_token()

    @property
    def api_url(self) -> str:
        return self._api_url

    @api_url.setter
    def api_url(self, value: str) -> None:
        self._api_url = self._normalize_url(value)

    @property
    def services(self) -> ServiceAPI:
        return self._services

    @property
    def policies(self) -> PolicyAPI:
        return self._policies

    @property
    def roles(self) -> RoleAPI:
        return self._roles

    @property
    def attachments(self) -> AttachmentAPI:
        return self._attach

    @property
    def shields(self) -> ShieldAPI:
        return self._shields

    @property
    def netagents(self) -> NetagentAPI:
        return self._agents

    @property
    def users(self):
        return self._users

    @property
    def devices(self):
        return self._devices


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    c = BanyanApiClient(api_server_url='https://gcstage.banyanops.com', refresh_token=os.getenv('BANYAN_REFRESH_TOKEN'),
                        debug=True)
    print(c.get_access_token())
    print(c.services.list())
