import re, html
import requests
import feedparser
from django.shortcuts import render

def google_news_feed(request):
    rss_url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(rss_url)
    articles =[]

    for entry in feed.entries[:10]:
        clean_summary = re.sub(r"<[^>]*>", "", entry.summary) 
        clean_summary = html.unescape(clean_summary)

        # Extract image 
        image_url = get_google_image(entry.title)

        articles.append(
            {
                "title": entry.title,
                "link": entry.link,
                "published": entry.published,
                "summary": clean_summary,
                "image": image_url  # Fallback image
            }
        )

    return render(request, "news_feed.html", {"articles": articles})

# SerpAPI details change this when limit of 100 is over
SERPAPI_KEY = "9ce3aab6d473dead5b8c2ae73b1824943789135ed677227f58f8056b01f09f2e"

def get_google_image(query):
    search_url = "https://serpapi.com/search"
    params = {
        "q": query,
        "tbm": "isch",  # Search for images
        "api_key": SERPAPI_KEY,
        "num": 1  # Get only 1 image
    }
    response = requests.get(search_url, params=params)

    if response.status_code == 200:
        results = response.json()
        if "images_results" in results and len(results["images_results"]) > 0:
            return results["images_results"][0]["original"]  # First image URL
    return "https://via.placeholder.com/150"  # Fallback image

def fact_check_feed(request):
    rss_url = "https://factly.in/category/english/feed/"
    feed = feedparser.parse(rss_url)

    articles = []
    for entry in feed.entries:
        # Get the content where blockquotes exist
        content_html = entry.content[0].value if hasattr(entry, "content") else ""

        # Extract <blockquote> content
        match = re.search(r'<blockquote.*?>(.*?)</blockquote>', content_html, re.DOTALL)

        # Initialize variables with default values
        claim = "No claim found"
        fact = "No fact found"

        if match:
            blockquote_content = match.group(1)
            # More flexible regex to extract Claim and Fact
            claim_match = re.search(r'<p>\s*<strong>\s*Claim\s*:?\s*</strong>\s*(.*?)</p>', blockquote_content, re.DOTALL)
            fact_match = re.search(r'<p>\s*<strong>\s*Fact\s*:?\s*</strong>\s*(.*?)</p>', blockquote_content, re.DOTALL)

            if claim_match:
                claim = re.sub(r'<.*?>', '', claim_match.group(1)).strip()  # Remove HTML tags

            if fact_match:
                fact = re.sub(r'<.*?>', '', fact_match.group(1)).strip()  # Remove HTML tags
        
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published,
            'claim' : claim,
            'fact' : fact
            })

    return render(request, 'fact_check.html', {'articles': articles})