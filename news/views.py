from django.shortcuts import render
import requests

def home(request):
    API_KEY = "8ac3b9a486974824a3c3f60521c63185"  # Replace with your actual API key
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"  
    
    response = requests.get(url)
    news_data = response.json()
    print(news_data)

    articles = news_data.get("articles", [])  # Get news articles
    if not articles:
        print("No articles found:", news_data) 

    return render(request, "home.html", {"articles": articles})