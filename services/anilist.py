import httpx

URL = "https://graphql.anilist.co"

async def search_manga(name):
    query = """
    query ($search: String) {
      Media(search: $search, type: MANGA) {
        title { romaji }
        description(asHtml:false)
        genres
        coverImage { large }
      }
    }
    """

    async with httpx.AsyncClient() as client:
        r = await client.post(URL, json={
            "query": query,
            "variables": {"search": name}
        })

    return r.json()["data"]["Media"]
