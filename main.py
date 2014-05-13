import os
import logging
import tornado.web
import tornado.ioloop
import tornado.autoreload
from tornado.options import options
from views.movie_view import MovieListView
from views.test_view import TestView
import importlib

importlib.import_module(os.environ.get('TORNADO_SETTINGS', 'config.local'))

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

settings = dict(
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), 'static'),
)

application = tornado.web.Application([
    (r"/test/", TestView),
    (r"/movies/", MovieListView),
], **settings)

if __name__ == '__main__':
    logging.info('Start of application on port 8888')
    application.listen(8888)
    logging.info("Application started on port 8888")

    ioloop = tornado.ioloop.IOLoop.instance()

    if options.DEVELOPMENT:
        logging.info("Watching project changes for reload application")
        tornado.autoreload.watch('templates/')
        tornado.autoreload.watch('static/')
        tornado.autoreload.start(ioloop)

    ioloop.start()

    logging.info("Application stopped")
