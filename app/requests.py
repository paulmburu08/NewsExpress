import urllib.request,json
from .models import TopHeadline

api_key = None
headlines_url = None

def configure_request(app):
    global api_key,headlines_url
    api_key = app.config['NEWS_API_KEY']
    headlines_url = app.config['TOP_HEADLINES_URL']

def get_headlines(country):
    '''
    Function that gets the json response to our url request
    '''
    get_headlines_url = headlines_url.format(country,api_key)

    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        headlines_results = None

        if get_headlines_response['articles']:
            headlines_list = get_headlines_response['articles']
            headlines_results = process_results(headlines_list)

    return headlines_results

def process_results(headlines_list):

    headlines_result = []

    for item in headlines_list:
        author = item.get('author')
        title = item.get('title')
        description = item.get('description')
        url = item.get('url')
        urlToImage = item.get('urlToImage')
        publishedAt = item.get('publishedAt')

        if urlToImage:
            new_headline = TopHeadline(author,title,description,url,urlToImage,publishedAt)
            headlines_result.append(new_headline)

    return headlines_result
    

    