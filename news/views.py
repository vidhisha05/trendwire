
import feedparser
from django.shortcuts import render

def google_news_feed(request):
    rss_url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(rss_url)

    articles = [
        {
            "title": entry.title,
            "link": entry.link,
            "published": entry.published,
            "summary": entry.summary,
        }
        for entry in feed.entries[:10]
    ]

    return render(request, "news_feed.html", {"articles": articles})
