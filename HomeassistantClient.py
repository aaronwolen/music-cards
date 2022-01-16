"""
Communicate with Home Assistant's REST API.
"""
import requests
from urllib.parse import urlparse


class HomeassistantClient:
    """
    Client for Home Assistant's REST API.
    """

    def __init__(self, server: str, token: str, verify_ssl: bool = False):
        """
        Initialize Home Assistant client.
        """

        # assemble url and add scheme if missing
        server_url = urlparse(server)
        if server_url.scheme == "":
            if verify_ssl:
                self.server = f"https://{server}"
            else:
                self.server = f"http://{server}"
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    def call_api(self, method: str, url: str, data: dict = None) -> dict:
        """
        Call Home Assistant API.
        """
        if method == "GET":
            response = requests.get(url, headers=self.headers)
        elif method == "POST":
            response = requests.post(url, headers=self.headers, json=data)
        else:
            raise ValueError(f"Unknown method '{method}'")

        if response.status_code != 200:
            raise Exception(
                f"Error calling Home Assistant API: {response.status_code} {response.text}"
            )

        return response.json()

    def fire_event(self, event_type: str, data: dict = {None}) -> None:
        """
        Fires an event with 'event_type'.
        """
        self.call_api("POST", f"{self.server}/api/events/{event_type}", data)

    def get_states(self) -> dict:
        """
        Get all states from Home Assistant.
        """
        return self.call_api("GET", f"{self.server}/api/states")

    def get_state(self, entity_id: str) -> dict:
        """
        Get state from Home Assistant.
        """
        return self.call_api("GET", f"{self.server}/api/states/{entity_id}")
