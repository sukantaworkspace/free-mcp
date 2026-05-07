from fastmcp import FastMCP
from worldnewsapi.api.news_api import NewsApi
from worldnewsapi.exceptions import ApiException
from worldnewsapi.configuration import Configuration
from worldnewsapi.api_client import ApiClient
import os
from typing import Optional, List

mcp = FastMCP(name="WorldNewsAPI")

# Initialize the API client
# Users should set WORLD_NEWS_API_KEY environment variable
api_key = os.getenv("WORLD_NEWS_API_KEY", "")
configuration = Configuration()
configuration.api_key['api-key'] = api_key
api_instance = NewsApi(ApiClient(configuration))

@mcp.tool
def search_news(
    text: str,
    source_countries: Optional[str] = None,
    language: Optional[str] = None,
    min_sentiment: Optional[float] = None,
    max_sentiment: Optional[float] = None,
    earliest_publish_date: Optional[str] = None,
    latest_publish_date: Optional[str] = None,
    news_sources: Optional[str] = None,
    authors: Optional[str] = None,
    entities: Optional[str] = None,
    location_filter: Optional[str] = None,
    sort: Optional[str] = None,
    sort_direction: Optional[str] = None,
    offset: Optional[int] = None,
    number: Optional[int] = 10
) -> str:
    """
    Search for news articles. Only 'text' parameter is required, all others are optional filters.
    
    Args:
        text: (REQUIRED) The text to search for in news content (at least 3 characters)
        source_countries: (Optional) Comma-separated country codes (e.g., 'us,uk,de')
        language: (Optional) Language code (e.g., 'en')
        min_sentiment: (Optional) Minimum sentiment score (-1 to 1)
        max_sentiment: (Optional) Maximum sentiment score (-1 to 1)
        earliest_publish_date: (Optional) Earliest publish date (ISO 8601 format)
        latest_publish_date: (Optional) Latest publish date (ISO 8601 format)
        news_sources: (Optional) Comma-separated news source domains
        authors: (Optional) Comma-separated author names
        entities: (Optional) Comma-separated entity names
        location_filter: (Optional) Location filter (e.g., 'latitude,longitude,radius')
        sort: (Optional) Sort field (publish-time or sentiment)
        sort_direction: (Optional) Sort direction (ASC or DESC)
        offset: (Optional) Offset for pagination
        number: (Optional) Number of results to return (default: 10, max: 100)
    
    Returns:
        JSON string with search results
    """
    try:
        api_response = api_instance.search_news(
            text=text,
            source_country=source_countries,
            language=language,
            min_sentiment=min_sentiment,
            max_sentiment=max_sentiment,
            earliest_publish_date=earliest_publish_date,
            latest_publish_date=latest_publish_date,
            news_sources=news_sources,
            authors=authors,
            entities=entities,
            location_filter=location_filter,
            sort=sort,
            sort_direction=sort_direction,
            offset=offset,
            number=number
        )
        return str(api_response)
    except ApiException as e:
        return f"Exception when calling NewsApi->search_news: {e}"

@mcp.tool
def extract_news(
    url: str,
    analyze: bool = True
) -> str:
    """
    Extract news article content from a URL.
    
    Args:
        url: The URL of the news article to extract
        analyze: Whether to analyze the article (sentiment, entities, etc.)
    
    Returns:
        JSON string with extracted article content and analysis
    """
    try:
        api_response = api_instance.extract_news(url=url, analyze=analyze)
        return str(api_response)
    except ApiException as e:
        return f"Exception when calling NewsApi->extract_news: {e}"

@mcp.tool
def top_news(
    source_country: str = "us",
    language: str = "en",
    headlines_only: bool = False
) -> str:
    """
    Get top news headlines. All parameters are optional with sensible defaults.
    
    Args:
        source_country: (Optional) Country code (default: 'us', examples: 'uk', 'de', 'fr')
        language: (Optional) Language code (default: 'en')
        headlines_only: (Optional) Whether to return only headlines for faster response (default: False)
    
    Returns:
        JSON string with top news articles
    """
    try:
        api_response = api_instance.top_news(
            source_country=source_country,
            language=language,
            headlines_only=headlines_only
        )
        return str(api_response)
    except ApiException as e:
        return f"Exception when calling NewsApi->top_news: {e}"

@mcp.tool
def get_geo_coordinates(
    location: str
) -> str:
    """
    Get geographic coordinates (latitude and longitude) for a location.
    Useful for location-based news filtering.
    
    Args:
        location: Location name (e.g., 'New York', 'London', 'Tokyo')
    
    Returns:
        JSON string with latitude, longitude, and location details
    """
    try:
        api_response = api_instance.get_geo_coordinates(location=location)
        return str(api_response)
    except ApiException as e:
        return f"Exception when calling NewsApi->get_geo_coordinates: {e}"

@mcp.tool
def extract_news_links(
    url: str,
    analyze: bool = False
) -> str:
    """
    Extract news article links from a news website.
    
    Args:
        url: (REQUIRED) The URL of the news website
        analyze: (Optional) Whether to analyze the articles (default: False)
    
    Returns:
        JSON string with extracted news links
    """
    try:
        api_response = api_instance.extract_news_links(url=url, analyze=analyze)
        return str(api_response)
    except ApiException as e:
        return f"Exception when calling NewsApi->extract_news_links: {e}"

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)

# Made with Bob
