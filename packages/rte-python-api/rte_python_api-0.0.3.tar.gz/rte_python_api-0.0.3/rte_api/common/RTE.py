from .API import API
from urllib.parse import urlparse

class RTEAPI(API):
    _date_time_format = "%Y-%m-%dT%H:%M:%SZ"

    def __init__(self, client_id: str, client_secret: str):
        self._base_url = urlparse("https://digital.iservices.rte-france.com/")
        self.auth(client_id=client_id, client_secret=client_secret)