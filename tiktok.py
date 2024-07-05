from __future__ import annotations

import requests
from typing import Dict, Any, List


class Tiktok(:
    base_url = 'https://api.tiktok.com/'

    def __init__(self, user_agent: str = None) -> None:
        self.user_agent = user_agent if user_agent else 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

    def fetch_user_info(self, username: str) -> Dict[str, Any]:
        endpoint = f'{self.base_url}v1/user/'
        params = {
            'username': username,
            'user_agent': self.user_agent
        }
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error fetching user info: {response.status_code}, {response.text}")
