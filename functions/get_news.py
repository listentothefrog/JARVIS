import os
from dotenv import find_dotenv, load_dotenv
from newsapi import NewsApiClient
from pprint import pprint
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
NEWS_API_KEY = os.getenv('NEWS_API')

newsapi = NewsApiClient(api_key=NEWS_API_KEY)

def get_top_news_articles(source, num_articles=5):
    top_headlines = newsapi.get_top_headlines(sources=source)
    articles = top_headlines['articles'][:num_articles]

    for i, article in enumerate(articles):
        print(f"Article {i+1}:")
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print("")

get_top_news_articles('cnn', num_articles=5)


