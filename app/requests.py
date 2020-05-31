import urllib.request,json
from .models import TopHeadline

api_key = None
headlines_url = None

def configure_request(app):
    global api_key,headlines_url
    api_key = app.config['NEWS_API_KEY']
    headlines_url = app.config['TOP_HEADLINES_URL']