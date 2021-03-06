from flask import render_template,request,redirect,url_for
from app import app
from .request import get_movies,get_movie,search_movie

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

    search_movie = request.args.get('movie_query')

    if search_movie:
        return redirect(url_for('search', movie_name = search_movie))
    else:
        return render_template('index.html', message = message, title = title, popular = popular_movies, upcoming = upcoming_movies, now_showing = now_showing_movies)
    return render_template('index.html', message = message, title = title, popular = popular_movies, upcoming = upcoming_movies, now_showing = now_showing_movies)

@app.route('/movie/<int:id>')
def movie(id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'
    return render_template('movie.html',title = title, movie = movie)

@app.route('/search/<movie_name>')
def search(movie_name):
    '''
    View function to display search results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html', movies = searched_movies)