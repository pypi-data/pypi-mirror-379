import requests

from nukiwebapi.account import Account
from nukiwebapi.account_user import AccountUser
from nukiwebapi.address import Address
from nukiwebapi.address_reservation import AddressReservation
from nukiwebapi.address_token import AddressToken
from nukiwebapi.advanced_api import AdvancedApi
from nukiwebapi.api_key import ApiKey
from nukiwebapi.company import Company
from nukiwebapi.notification import Notification
from nukiwebapi.opener import Opener
from nukiwebapi.service import Service
from nukiwebapi.smartlock import Smartlock
from nukiwebapi.smartlock_instance import SmartlockInstance
from nukiwebapi.smartlock_auth import SmartlockAuth
from nukiwebapi.smartlock_log import SmartlockLog


class NukiWebAPI:
    """Main Nuki Web API client."""

    def __init__(self, access_token: str, base_url: str = "https://api.nuki.io", smartlock_ids: list[str] = None):
        self.base_url = base_url.rstrip("/")
        self.access_token = access_token
        self.account = Account(self)
        self.account_user = AccountUser(self)
        self.address = Address(self)
        self.address_reservation = AddressReservation(self)
        self.address_token = AddressToken(self)
        self.api_key = ApiKey(self)
        self.smartlock = Smartlock(self)
        self._lock_instances = None
        self.advanced_api = AdvancedApi(self)
        self.company = Company(self)
        self.notification = Notification(self)
        self.opener = Opener(self)
        self.service = Service(self)
        self.smartlock_auth = SmartlockAuth(self)
        self.smartlock_log = SmartlockLog(self)

    @property
    def lock_instances(self):
        if self._lock_instances is None:
            self._lock_instances = self._fetch_smartlocks()
        return self._lock_instances
        
    def _fetch_smartlocks(self):
        """Fetch all smartlocks and create Smartlock objects mapped by ID."""
        response = self._request("GET", "/smartlock")
        smartlocks = {}
        if response.json():
            for item in response.json():
                smartlock_id = item.get("smartlockId")
                if not smartlock_id:
                    continue  # skip invalid entries
                smartlock = SmartlockInstance(
                    client=self,
                    smartlock_id=smartlock_id,
                    data=item
                )

                smartlocks[smartlock_id] = smartlock

        return smartlocks
        
    def _request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        headers = kwargs.pop("headers", {})
        headers["Authorization"] = f"Bearer {self.access_token}"
        headers["Accept"] = "application/json"

        response = requests.request(method, url, headers=headers, **kwargs)

        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            # Try to parse detailMessage if present
            try:
                error_json = response.json()
                detail = error_json.get("detailMessage", response.text)
            except ValueError:
                detail = response.text

            # Raise a new error with detail included
            raise requests.HTTPError(
                f"{e} | Detail: {detail}",
                response=response
            ) from None

        return response

