from dataclasses import dataclass

import requests

from .exceptions import InvalidResponse


@dataclass
class ThreeCXClient:
    fqdn: str
    username: str
    password: str
    access_token: str = None
    refresh_token: str = None

    def __post_init__(self):
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Content-Type": "application/json",
            }
        )
        self.base_url = f"https://{self.fqdn}"
        self._authenticate = False

    def authenticate(self):
        url = f"{self.base_url}/webclient/api/Login/GetAccessToken"
        payload = {
            "SecurityCode": "",
            "Password": self.password,
            "Username": self.username,
        }
        response = self.session.post(url, json=payload)
        data = response.json()
        status = data.get("Status")
        if status != "AuthSuccess":
            raise InvalidResponse("Authentication failed", response=response)

        token = data.get("Token", {})
        self.access_token = token.get("access_token")
        self.refresh_token = token.get("refresh_token")
        self.session.headers.update({"Authorization": f"Bearer {self.access_token}"})
        self._authenticate = True

    def _request(
        self,
        method: str,
        endpoint: str,
        params=None,
        json_body=None,
        return_full_response=False,
    ):
        if not self._authenticate:
            self.authenticate()

        url = f"{self.base_url}{endpoint}"

        request_params = {"url": url}

        if params is not None:
            request_params["params"] = params
        if json_body is not None:
            request_params["json"] = json_body

        response = self.session.request(method=method, **request_params)
        status = response.status_code

        try:
            if status != 204:
                json_result = response.json()
            else:
                json_result = None
        except ValueError as error:
            raise InvalidResponse("Failed to decode API response", error, response=response)

        if 100 <= status < 300:
            if return_full_response:
                return response
            return json_result

        raise InvalidResponse(f"Unexpected status code: {status}", response=response)

    def get(self, endpoint: str, params=None):
        return self._request("GET", endpoint, params=params)

    def post(self, endpoint: str, json_body=None):
        return self._request("POST", endpoint, json_body=json_body)

    def patch(self, endpoint: str, json_body=None):
        return self._request("PATCH", endpoint, json_body=json_body)

    def delete(self, endpoint: str, params=None):
        return self._request("DELETE", endpoint, params=params)

    def version(self):
        params = {"select": "Id"}
        response = self._request("GET", "/xapi/v1/Defs", params, return_full_response=True)
        if response.status_code != 200:
            return False

        headers = response.headers
        return headers.get("X-3CX-Version", "No X-3CX-Version in headers")


