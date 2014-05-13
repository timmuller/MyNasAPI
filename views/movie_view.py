import tornado.web
from control import movie_manager

class MovieListView(tornado.web.RequestHandler):
    def get(self):
        for movie in movie_manager.list_movies('/share/MD0_DATA/Multimedia/Films/Films'):
            self.write(movie)