from abc import ABC
from json import loads
from urllib.parse import urlparse, ParseResult
from requests import post, get, Response

class API(ABC):
    _base_url: ParseResult = urlparse("")
    _tokens: dict[str, str] = {}

    def auth(self, client_id: str, client_secret: str):
        token_url = self._base_url._replace(path="/token/oauth/").geturl()
        data = {'grant_type': 'client_credentials'}
        access_token_response = self._if_successful(post(token_url, data=data, verify=True, allow_redirects=False, auth=(client_id, client_secret)))
        self._tokens = loads(access_token_response.text)
    
    def get(self, path: str, params: dict[str, str] = {}, headers: dict[str, str] = {}) -> Response:
        endpoint = self._base_url._replace(path=path).geturl()
        api_call_headers = {'Authorization': 'Bearer ' + self._tokens['access_token']}
        api_call_headers.update(headers)
        return self._if_successful(get(endpoint, headers=api_call_headers, params=params, verify=True))
    
    def post(self, path: str, data: dict[str, str], headers: dict[str, str] = {}) -> Response:
        endpoint = self._base_url._replace(path=path).geturl()
        api_call_headers = {'Authorization': 'Bearer ' + self._tokens['access_token']}
        api_call_headers.update(headers)
        return self._if_successful(post(endpoint, headers=api_call_headers, json=data, verify=True))
    
    def _if_successful(self, response: Response) -> Response:
        code = response.status_code
        match code:
            case 200:
                return response
            case 400:
                raise RuntimeError(f"{code} Bad Request")
            case 401:
                raise RuntimeError(f"{code} Unauthorized")
            case 402:
                raise RuntimeError(f"{code} Payment Required")
            case 403:
                raise RuntimeError(f"{code} Forbidden")
            case 404:
                raise RuntimeError(f"{code} Not Found")
            case 405:
                raise RuntimeError(f"{code} Method Not Allowed")
            case 406:
                raise RuntimeError(f"{code} Not Acceptable")
            case 407:
                raise RuntimeError(f"{code} Proxy Authentication Required")
            case 408:
                raise RuntimeError(f"{code} Request Timeout")
            case 409:
                raise RuntimeError(f"{code} Conflict")
            case 410:
                raise RuntimeError(f"{code} Gone")
            case 411:
                raise RuntimeError(f"{code} Length Required")
            case 412:
                raise RuntimeError(f"{code} Precondition Failed")
            case 413:
                raise RuntimeError(f"{code} Content Too Large")
            case 414:
                raise RuntimeError(f"{code} URI Too Long")
            case 415:
                raise RuntimeError(f"{code} Unsupported Media Type")
            case 416:
                raise RuntimeError(f"{code} Range Not Satisfiable")
            case 417:
                raise RuntimeError(f"{code} Expectation Failed")
            case 429:
                raise RuntimeError(f"{code} Too Many Requests")
            case 500:
                raise RuntimeError(f"{code} Internal Server Error")
            case 503:
                raise RuntimeError(f"{code} Service Unavailable")
            case _:
                raise RuntimeError(f"HTTP Error Code {code} Unknown")