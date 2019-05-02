from flask import render_template
from app import app
from .request import get_movies,get_movie

#Views
@app.route('/')
def index():
    '''
    View  root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')    
    now_showing_movies = get_movies('now_playing')
    title = "Home - Welcome To The Best Movie Review Website Online"
    message = 'Hello from the other side!!'
    return render_template('index.html', message = message, title = title, popular = popular_movies, upcoming = upcoming_movies, now_showing = now_showing_movies)

@app.route('/movie/<int:id>')
def movie(id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'
    return render_template('movie.html',title = title, movie = movie)
