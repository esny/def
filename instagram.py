from __future__ import annotations

import requests
from typing import Dict, Any, List


class Instagram:
    base_url = 'https://graph.instagram.com/v12.0/'

    def __init__(self, access_token: str) -> None:
        self.access_token = access_token

    def fetch_profile(self, username: str) -> Dict[str, Any]:
        endpoint = f'{self.base_url}/{username}'
        params = {
            'fields': 'id,username,account_type,media_count,followers_count,follows_count',
            'access_token': self.access_token
        }
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching profile: {response.status_code}, {response.text}")
