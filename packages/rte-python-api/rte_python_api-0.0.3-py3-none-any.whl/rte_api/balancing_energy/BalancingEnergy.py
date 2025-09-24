from requests import Response
from rte_api.common import RTEAPI, ContentType
from datetime import datetime
from zoneinfo import ZoneInfo
from typing import Optional, Dict


class BalancingEnergyAPI(RTEAPI):
    def __init__(self, client_id: str, client_secret: str):
        super().__init__(client_id, client_secret)
        self._api_path = "open_api/balancing_energy/v4/"

    def tso_offers(self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None):
        params: dict[str, str] = self._construct_optional_date_range_params(start_date, end_date)
        response = self.get(self._api_path + "tso_offers", params)
        return response.json()
    
    def imbalance_data(self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None, responseType: ContentType = ContentType.JSON):
        params: dict[str, str] = self._construct_optional_date_range_params(
                self._to_valid_date(start_date),
                self._to_valid_date(end_date)
            )
        response = self.get(self._api_path + "imbalance_data", params, {"Accept": responseType.value})

        match responseType:
            case ContentType.JSON:
                return response.json()
            case ContentType.CSV:
                return response.content.decode()
        
    def _to_valid_date(self, date: Optional[datetime]) -> datetime | None:
        if date is not None:
            if date.tzinfo is None:
                raise ValueError('Dates must be localized.')
            elif isinstance((zoneinfo := date.tzinfo), ZoneInfo):
                if zoneinfo.tzname == 'Europe/Paris':
                    return date
                else:
                    return date.astimezone(ZoneInfo('Europe/Paris'))
        else:
            # it is valid not to send a date
            return date
    
    def _construct_optional_date_range_params(self, start_date: Optional[datetime] = None, end_date: Optional[datetime] = None) -> Dict[str, str]:
        params: dict[str, str] = {}

        if start_date is not None and end_date is not None:
            params["start_date"] = start_date.isoformat(timespec='seconds')
            params["end_date"] = end_date.isoformat(timespec='seconds')
        elif start_date is None and end_date is None:
            pass # No params are provided, which is a correct usage of this API
        else:
            raise ValueError("Both start_date and end_date must be provided or excluded.")
        
        return params
    
    def _if_successful(self, response: Response) -> Response:
        code = response.status_code
        match response.status_code:
            case 400:
                raise RuntimeError(f"{code} Bad Request", response.json()['error_description'])
            case _:
                return super()._if_successful(response)