import tornado.web
from tornado.options import options

class TestView(tornado.web.RequestHandler):
    def get(self):
        self.write("none testing")