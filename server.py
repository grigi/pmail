#!/usr/bin/env python
import tornado.ioloop
from tornado import autoreload
from pmail import application

def arfun():
    print("Restarting...")

def logfun(self):
    print("%s: %s %s %s %.2fms %s" % (
        self.request.remote_ip,
        self.request.method,
        self.request.host,
        self.request.path,
        self.request.request_time()*1000.0,
        self.request.arguments if self.request.arguments else ""
    ))

application.settings = {
    'debug': True,
    'log_function': logfun
}
application.listen(8000)

ioloop = tornado.ioloop.IOLoop().instance()
autoreload.add_reload_hook(arfun)
autoreload.start(ioloop)
ioloop.start()
