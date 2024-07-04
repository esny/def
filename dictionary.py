from __future__ import annotations

import aiohttp, asyncio
from typing import Any, Dict, List, Optional


class Definition:
    def __init__(self, name: str, meaning: str, brief: str) -> None:
        self.name: str = name
        self.meaning: str = meaning
        self.brief: str = brief


class Dictionary():

  
    @staticmethod
    async def fetch(session: aiohttp.ClientSession, url: str) -> Optional[List[Dict[str, Any]]]:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            return None

  
    @staticmethod
    async def define(session: aiohttp.ClientSession, word: str) -> Definition:
        url: str = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        definition_data = await Dictionary.fetch(session, url)
        
        if definition_data:
            name: str = definition_data[0]['word']
            meanings: List[Dict[str, Any]] = definition_data[0].get('meanings', [])
            meaning_list: List[str] = []

            for meaning in meanings:
                part_of_speech: str = meaning.get('partOfSpeech', '')
                definitions: List[Dict[str, Any]] = meaning.get('definitions', [])
                
                for definition in definitions:
                    definition_text: str = definition.get('definition', '')
                    meaning_list.append(f"{part_of_speech}: {definition_text}")
                    
            brief: str = meaning_list[0] if meaning_list else 'No brief available'
            meaning: str = "\n".join(meaning_list)
            
            return Definition(name, meaning, brief)
        
        return Definition(word, "No definitions found.", "No brief available")
