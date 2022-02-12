import os

import flask
from tmdb import  get_trending,get_genres, movie_search
import requests
import MediaWiki


app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#Don't know how to have the main page link to the search page so I abandoned that for the mean time
"""
@app.route('/')
def hello_world():
    data = get_genres()
    return render_template(
        "search.html",
        genres = data['genres'],
        )
    """
    
@app.route('/', methods=["POST","GET"])
def search():
    data = get_genres()
    movies = get_trending()
    title = 'Trending'
    
    if flask.request.method == "POST":  
        query = flask.request.form.get("search")
        title = query
        movies = movie_search(query)
        
    titles = movies['titles']
    overviews = movies['overviews']
    posters = movies['posters']
    ids = movies['ids']
    taglines = movies['taglines']
    
    wikiLinks=[]
    for i in range(len(titles)):
        links = MediaWiki.get_wiki_link(titles[i])
        try:
            wikiLinks.append(links[3][0])#This is the part that has the link to the wikipedia page
        except:
            wikiLinks.append("#")#The links get out of order If I don't do this
            print("Link doesn't exist")
    
    return flask.render_template(
        "search.html",
        title = title,
        genres = data,
        titles = titles,
        overviews = overviews, 
        posters = posters,
        taglines = taglines,
        ids = ids,
        wikiLinks = wikiLinks,
        )
    
app.run(
    host=os.getenv('IP','0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug = True
)