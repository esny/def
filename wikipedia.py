from __future__ import annotations

from typing import Any, Dict, List
from aiohttp import ClientSession as Session


class Wikipedia():
    def __init__(self: Wikipedia, language: str = 'en') -> None:
        self.base_url: str = f'https://{language}.wikipedia.org/w/api.php'
    
    
    async def fetch(self: Wikipedia, session: Session, params: Dict[str, Any]) -> Dict[str, Any]:
        async with session.get(self.base_url, params=params) as response:
            return await response.json()
    
    
    async def search(self: Wikipedia, session: Session, query: str) -> List[Dict[str, Any]]:
        params = {
            'action': 'query',
            'list': 'search',
            'srsearch': query,
            'format': 'json'
        }
        data = await self.fetch(session, params)
        return data['query']['search']
    
    
    async def get_summary(self: Wikipedia, session: Session, title: str) -> str:
        params = {
            'action': 'query',
            'prop': 'extracts',
            'exintro': 'True',
            'explaintext': 'True',
            'titles': title,
            'format': 'json'
        }
        data = await self.fetch(session, params)
        pages = data['query']['pages']
        return next(iter(pages.values()))['extract']
