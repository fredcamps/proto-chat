#!/usr/bin/env python
"""Basic run script"""
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.autoreload
import tornado.web
from tornado.options import options

from proto_chat.urls import url_patterns
from settings import settings


class TornadoApplication(tornado.web.Application):
    '''Application'''

    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **settings)


def main():
    '''Driver function'''
    # settings.update({"debug": True})
    print("Running tornado webserver on port: {}".format(options.port))
    app = TornadoApplication()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
