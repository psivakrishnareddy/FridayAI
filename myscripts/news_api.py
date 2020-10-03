
import requests
import random


def send_top_news():
    api_key = "xxx"

    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=" + api_key

    response = requests.get(url)

    news = response.json()
    articles = news['articles']
    return articles
