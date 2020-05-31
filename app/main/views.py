from . import main
from flask import render_template
from ..requests import get_headlines

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    #getting news headlines
    us_news = get_headlines('us')
    print(us_news)
    title = 'Welcome to newsExpress'
    return render_template('index.html', title = title, headlines = us_news)