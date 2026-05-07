# World News API MCP Server

A Model Context Protocol (MCP) server that provides access to the World News API, allowing you to search, extract, and analyze news articles from around the world.

## Features

This MCP server provides the following tools:

- **search_news**: Search for news articles based on various criteria (text, country, language, sentiment, dates, etc.)
- **extract_news**: Extract and analyze news article content from a URL
- **top_news**: Get top news headlines for a specific country and language
- **get_geo_coordinates**: Get geographic coordinates for location-based news filtering
- **extract_news_links**: Extract news article links from a news website

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get Your API Key

1. Visit [World News API](https://worldnewsapi.com/)
2. Sign up for a free account
3. Get your API key from the dashboard

### 3. Set Environment Variable

Set your World News API key as an environment variable:

**Windows (PowerShell):**
```powershell
$env:WORLD_NEWS_API_KEY="your-api-key-here"
```

**Windows (Command Prompt):**
```cmd
set WORLD_NEWS_API_KEY=your-api-key-here
```

**Linux/Mac:**
```bash
export WORLD_NEWS_API_KEY="your-api-key-here"
```

For permanent setup, add it to your system environment variables.

### 4. Run the Server

```bash
python server.py
```

The server will start on `http://0.0.0.0:8000`

## Usage Examples

### Search News

Search for news articles about technology in the US:

```python
search_news(
    text="artificial intelligence",
    source_countries="us",
    language="en",
    number=10
)
```

### Extract News

Extract and analyze content from a news article URL:

```python
extract_news(
    url="https://example.com/news-article",
    analyze=True
)
```

### Get Top News

Get today's top news headlines from the UK:

```python
top_news(
    source_country="uk",
    language="en",
    headlines_only=False
)
```

### Get Geo Coordinates

Get coordinates for location-based filtering:

```python
get_geo_coordinates(location="New York")
```

### Extract News Links

Extract all news links from a news website:

```python
extract_news_links(
    url="https://news-website.com",
    analyze=False
)
```

## Tool Parameters

### search_news

- `text`: Search text (min 3 chars, max 1000)
- `source_countries`: Comma-separated country codes (e.g., 'us,uk,de')
- `language`: Language code (e.g., 'en')
- `min_sentiment`: Minimum sentiment score (-1 to 1)
- `max_sentiment`: Maximum sentiment score (-1 to 1)
- `earliest_publish_date`: Earliest date (ISO 8601 format)
- `latest_publish_date`: Latest date (ISO 8601 format)
- `news_sources`: Comma-separated news source domains
- `authors`: Comma-separated author names
- `entities`: Comma-separated entity names
- `location_filter`: Location filter (latitude,longitude,radius)
- `sort`: Sort field (publish-time or sentiment)
- `sort_direction`: Sort direction (ASC or DESC)
- `offset`: Pagination offset
- `number`: Number of results (max 100, default 10)

### extract_news

- `url`: URL of the news article
- `analyze`: Whether to analyze the article (default: True)

### top_news

- `source_country`: Country code (e.g., 'us', 'uk', 'de')
- `language`: Language code (e.g., 'en')
- `headlines_only`: Return only headlines for faster response (default: False)

### get_geo_coordinates

- `location`: Location name (e.g., 'New York', 'London')

### extract_news_links

- `url`: URL of the news website
- `analyze`: Whether to analyze the articles (default: False)

## API Rate Limits

The free tier of World News API has rate limits. Check your plan details at [worldnewsapi.com](https://worldnewsapi.com/) for specific limits.

## Troubleshooting

### "API key not found" error

Make sure you've set the `WORLD_NEWS_API_KEY` environment variable correctly.

### Import errors

Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Connection errors

Check that:
1. Your API key is valid
2. You have an active internet connection
3. You haven't exceeded your API rate limits

## Resources

- [World News API Documentation](https://worldnewsapi.com/docs/)
- [Quick Start Tutorial](https://worldnewsapi.com/docs/quick-start-tutorial/)
- [MCP Documentation](https://modelcontextprotocol.io/)

## License

This project is open source and available under the MIT License.
