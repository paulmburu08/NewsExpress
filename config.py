import os

class Config:
    TOP_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?country={}&apiKey={}'
    CATEGORY_URL = 'https://newsapi.org/v2/top-headlines?country={}&category={}&apiKey={}'
    ARTICLES_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')