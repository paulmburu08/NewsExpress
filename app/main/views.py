from . import main
from flask import render_template
from ..requests import get_headlines,get_category

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    #getting news headlines
    us_news = get_headlines('us')
    german_news = get_headlines('ed')
    french_news = get_headlines('fr')
    russia_news = get_headlines('ru')
    saudi_news = get_headlines('sa')
    print(us_news)
    title = 'Welcome to newsExpress'
    return render_template('index.html', title = title, usheadlines = us_news, edheadlines = german_news, frheadlines = french_news, ruheadlines = russia_news, saheadlines = saudi_news)

@main.route('/category')
def category():
    '''
    View root page function that returns the index page and its data
    '''

    business = get_category('us','business')
    entertainment = get_category('us','entertainment')
    health = get_category('us','health')
    science = get_category('us','science')
    sports = get_category('us','sports')
    technology = get_category('us','technology')

    return render_template('navbar.html',business = business, entertainment = entertainment, health = health, science = science, sports = sports, technology = technology)

