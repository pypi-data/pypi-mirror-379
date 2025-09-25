import asyncio
from wikipedia_async import WikipediaClient, ClientConfig
from pprint import pprint


async def main():
    # Initialize client with optimal defaults
    client = WikipediaClient(ClientConfig(cache_type="file", cache_ttl=3600 * 24))

    # Search for articles
    results = await client.search("python", suggestion=True)
    # pprint(results)
    print("Search results:")
    for result in results:
        print(f"- {result.title} ({result.page_id})")
        print(f" URL: {result.url}")
        print(f" Summary: {result.snippet}")
        print("=" * 20)
    print(f"Suggestion: {results.suggestion}")

    # page = wikipedia.page("Python (programming language)")
    # print(page.title)

    # Get page content
    page = await client.get_page(page_id=21356332)
    # print(f"Title: {page.title}")
    # print()
    # # print(page.summary)
    # print(page.sections[:2])
    print(page.sections.tree_view(content_limit=100))
    # print()
    # print(list(page.sections))
    # print(page.content)
    # print(page.sections)

    # # Batch operations
    # pages = await client.get_pages_batch(["Python", "JavaScript", "Rust"])
    # for p in pages:
    #     print(f"Batch page: {p.title} - {p.summary[:100]}...")
    # # Close the client session

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
