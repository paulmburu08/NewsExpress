from . import main
from flask import render_template
from ..requests import get_headlines,get_category,get_sources

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    #getting news headlines
    us_news = get_headlines('us')
    title = 'Welcome to newsExpress'
    return render_template('index.html', title = title, usheadlines = us_news)

@main.route('/germany')
def country1():
    german_news = get_headlines('de')
    return render_template('german.html',edheadlines = german_news)
@main.route('/france')
def country2():
    french_news = get_headlines('fr')
    return render_template('french.html',frheadlines = french_news)
@main.route('/russia')
def country3():
    russia_news = get_headlines('ru')
    return render_template('russia.html',ruheadlines = russia_news)
@main.route('/saudiarabia')
def country4():
    saudi_news = get_headlines('sa')
    return render_template('saudi.html',saheadlines = saudi_news)

@main.route('/bbc')
def source1():
    '''
    View root page function that returns the index page and its data
    '''
    bbc = get_sources('bbc-news')
    return render_template('bbc.html', bbc = bbc)
@main.route('/aljazeera')
def source2():
    aljazeera = get_sources('al-jazeera-english')
    return render_template('aljazeera.html', aljazeera = aljazeera)
@main.route('/cnn')
def source3():
    cnn = get_sources('cnn')
    return render_template('cnn.html', cnn = cnn)
@main.route('/cbs')
def source4():
    cbs = get_sources('cbs-news')
    return render_template('cbs.html', cbs = cbs)
@main.route('/foxnews')
def source5():
    fox = get_sources('fox-news')
    return render_template('fox.html', fox = fox)
@main.route('/usatoday')
def source6():
    usa = get_sources('usa-today')
    return render_template('usa.html', usa = usa)


@main.route('/business')
def category1():
    '''
    View root page function that returns the index page and its data
    '''
    business = get_category('us','business')
    return render_template('business.html',business = business, entertainment = entertainment, health = health, science = science, sports = sports, technology = technology)
@main.route('/entertainment')
def category2():
    entertainment = get_category('us','entertainment')
    return render_template('entertainment.html', entertainment = entertainment)
@main.route('/health')
def category3():
    health = get_category('us','health')
    return render_template('health.html', health = health)
@main.route('/science')
def category4():
    science = get_category('us','science')
    return render_template('science.html', science = science)
@main.route('/sports')
def category5():
    sports = get_category('us','sports')
    return render_template('sports.html', sports = sports)
@main.route('/technology')
def category6():
    technology = get_category('us','technology')
    return render_template('technology.html', technology = technology)