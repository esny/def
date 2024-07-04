Example:

```python

async def main():
    async with aiohttp.ClientSession() as session:
        
        wikipedia = Wikipedia(language='en')
        search_results = await wikipedia.search(session, 'Python programming language')
        for result in search_results:
            print(f"- {result['title']}")

        summary = await wikipedia.get_summary(session, 'Python programming language')
        print("\nWikipedia Summary:")
        print(summary)
```
