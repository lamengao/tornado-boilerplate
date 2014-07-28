#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import, division, print_function

import os.path
# import logging
# import redis

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen

from os.path import dirname
from tornado.options import define, options

from basehandler import BaseHandler

define("port", default=8889, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/bower_components/(.*)", tornado.web.StaticFileHandler,
                {"path": os.path.join(dirname(__file__), "bower_components")}),
        ]
        settings = {
            "template_path": os.path.join(dirname(__file__), "templates"),
            "static_path": os.path.join(dirname(__file__), "static"),
            "cookie_secret": 'xxxxxxxxxxxxxx',
            "xsrf_cookies": True,
            "debug": True,
            "redis": {
                "host": "127.0.0.1",
                "port": 6379,
                "db": 0
            }
        }
        # self.redis = redis.StrictRedis(**settings['redis'])
        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(BaseHandler):

    def get(self):
        self.render('home.html')


if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(), xheaders=True)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
