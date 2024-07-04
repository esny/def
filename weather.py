from __future__ import annotations

import aiohttp
import asyncio
from typing import Any, Dict, Optional


class WeatherInfo:
    def __init__(self, location: str, temperature: str, description: str) -> None:
        self.location: str = location
        self.temperature: str = temperature
        self.description: str = description


class Weather:
    def __init__(self, api_key: str) -> None:
        self.api_key: str = api_key
        self.base_url: str = "http://api.openweathermap.org/data/2.5/weather"

  
    async def fetch(self, session: aiohttp.ClientSession, params: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        async with session.get(self.base_url, params=params) as response:
          
            if response.status == 200:
                return await response.json()
              
            return None

  
    async def get_weather(self, session: aiohttp.ClientSession, location: str) -> WeatherInfo:
        params = {
            'q': location,
            'appid': self.api_key,
            'units': 'metric'
        }
        data = await self.fetch(session, params)
        
        if data:
            location_name: str = data['name']
            temperature: str = f"{data['main']['temp']}°C"
            description: str = data['weather'][0]['description']
            
            return WeatherInfo(location_name, temperature, description)
        
        return WeatherInfo(location, "N/A", "Weather data not available")
