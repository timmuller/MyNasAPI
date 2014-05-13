import logging
import tornado.web
import tornado.ioloop

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == '__main__':
    logging.info('Start of application on port 8888')
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
    logging.info("Application started on port 8888")
