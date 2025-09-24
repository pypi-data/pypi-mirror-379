from requests import Response
from rte_api.common import RTEAPI
from typing import Dict, Any

class WholesaleMarketAPI(RTEAPI):
    def __init__(self, client_id: str, client_secret: str):
        super().__init__(client_id, client_secret)
        self._api_path = "open_api/wholesale_market/v2/"

    def france_power_exchanges(self) -> Dict[str, Any]:
        """
        Returns day ahead french power exchange prices.
        """
        response = self.get(self._api_path + "france_power_exchanges")
        return response.json()

    def _if_successful(self, response: Response) -> Response:
        code = response.status_code
        match response.status_code:
            case 509:
                raise RuntimeError(f"{code} Bandwidth Limit Exceeded")
            case _:
                return super()._if_successful(response)
        