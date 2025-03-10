import re
import html
import feedparser
from django.shortcuts import render

def google_news_feed(request):
    rss_url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(rss_url)
    articles =[]

    for entry in feed.entries[:10]:
        clean_summary = re.sub(r"<[^>]*>", "", entry.summary) 
        clean_summary = html.unescape(clean_summary)

        # Extract image from the description field
        image_url = None
        match = re.search(r'<img[^>]+src="([^">]+)"', entry.summary)
        if match:
            image_url = match.group(1)

        articles.append(
            {
                "title": entry.title,
                "link": entry.link,
                "published": entry.published,
                "summary": clean_summary,
                "image": image_url if image_url else "https://via.placeholder.com/150",  # Fallback image
            }
        )

    return render(request, "news_feed.html", {"articles": articles})
