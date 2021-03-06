from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from api import app as apiapp

metaapi = HTTPServer(WSGIContainer(apiapp))
metaapi.listen(5000)
IOLoop.instance().start()
