from rte_api.common import RTEAPI
from datetime import datetime
from typing import Optional

class BigAdjustedAPI(RTEAPI):
    def __init__(self, client_id: str, client_secret: str):
        super().__init__(client_id, client_secret)
        self._api_path = "private_api/adjusted_consumption/v2/"

    def get_updated_data(self, update_date: datetime, update_time_slot: Optional[int] = None, range: str = "0-9999", service_point_type: Optional[str] = None):
        params = {
            "update_date": update_date.strftime(self._date_time_format),
            "range": range
        }

        if update_time_slot is not None:
            params["update_time_slot"] = str(update_time_slot)

        if service_point_type is not None:
            params["service_point_type"] = service_point_type
        
        response = self.get(self._api_path + "updated_data", params)
        return response.json()