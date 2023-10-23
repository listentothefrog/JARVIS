import os
from dotenv import find_dotenv, load_dotenv
from newsapi import NewsApiClient
from pprint import pprint
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
NEWS_API_KEY = os.getenv('NEWS_API')

newsapi = NewsApiClient(api_key=NEWS_API_KEY)


top_headlines = newsapi.get_top_headlines(q='tech',
                                          category='technology',
                                          language='en',
                                          country='us')


sources = newsapi.get_sources()
pprint(sources)