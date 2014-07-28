#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import, division, print_function

#import logging
import tornado.web

class BaseHandler(tornado.web.RequestHandler):

    def initialize(self):
        self.template_values = {}
        self.template_values['debug'] = False

    def write_error(self, status_code, **kwargs):
        if status_code in [403, 404, 500, 503]:
            self.render("error/%d.html" % status_code)
