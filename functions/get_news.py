import os
import time
from dotenv import find_dotenv, load_dotenv
from newsapi import NewsApiClient
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
NEWS_API_KEY = os.getenv('NEWS_API')
import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices') #getProperty(‘voices’) returns an array of all available voices
engine.setProperty('voice', voices[0].id)


newsapi = NewsApiClient(api_key=NEWS_API_KEY)

def get_top_news_articles(source, num_articles=5):
    top_headlines = newsapi.get_top_headlines(sources=source)
    articles = top_headlines['articles'][:num_articles]

    engine = pyttsx3.init()
    time.sleep(5)
    engine.runAndWait()
    for i, article in enumerate(articles):
        print(f"Article {i + 1}:")
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")

        engine.say(f"{article['title']}")
        print(article["url"])
        engine.runAndWait()
        
        engine.say(f"{article['description']}")
        engine.runAndWait()

    time.sleep(5)
    print("")
    engine.say("Please check your messages, where I have attached all the links to these articles.")
    engine.runAndWait()
    
get_top_news_articles('bbc-news', num_articles=2)

engine.runAndWait()