import tornado.web
from tornado.options import options
from control import movie_manager

class MovieListView(tornado.web.RequestHandler):
    def get(self):
        self.render('movies.html', **{'movies': movie_manager.list_movies(options.MOVIE_LOCATIONS)})
