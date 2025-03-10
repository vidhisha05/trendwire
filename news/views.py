from django.shortcuts import render

def home(request):
    trending_articles = [
        {"title": "AI Revolution in 2025", "summary": "AI is changing the world rapidly.", "image_url": "https://source.unsplash.com/400x250/?technology", "link": "#"},
        {"title": "Climate Change Updates", "summary": "New studies show global warming effects.", "image_url": "https://source.unsplash.com/400x250/?nature", "link": "#"}
    ]

    articles = [
        {"title": "Sports Highlights", "summary": "Latest sports news from around the world.", "image_url": "https://source.unsplash.com/400x250/?sports", "link": "#"},
        {"title": "Stock Market Trends", "summary": "Markets are fluctuating in Q1 2025.", "image_url": "https://source.unsplash.com/400x250/?finance", "link": "#"}
    ]

    return render(request, "home.html", {"trending_articles": trending_articles, "articles": articles})
