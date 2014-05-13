import logging
import tornado.web
import tornado.ioloop
from views.movie_view import MovieListView
from views.test_view import TestView
import importlib

importlib.import_module('config.local')

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

application = tornado.web.Application([
    (r"/test/", TestView),
    (r"/movies/", MovieListView),
])

if __name__ == '__main__':
    logging.info('Start of application on port 8888')
    application.listen(8888)
    logging.info("Application started on port 8888")
    tornado.ioloop.IOLoop.instance().start()
    logging.info("Application stopped")
