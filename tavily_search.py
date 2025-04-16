from tavily import TavilyClient # type: ignore

# Replace this with your actual Tavily API key
client = TavilyClient("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")

# Perform the search with a valid query
response = client.search(
    query="latest updates with Nvidia",  # Replace this with your desired query
    max_results=5,  # Set the number of results you want
    search_depth="basic",  # You can adjust the depth (basic, advanced, etc.)
    include_answer=True,  # You can include or exclude answers
)

print(response)
