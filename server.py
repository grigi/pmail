#!/usr/bin/env python
import tornado.ioloop
from tornado import autoreload
from pmail import application, smtpd
import logging
logging.basicConfig(level=logging.INFO)

application.settings['debug'] = True
application.listen(8000)

global emlsvr
emlsvr = smtpd()

def arfun():
    global emlsvr
    emlsvr.stop()
    print("Restarted...")

ioloop = tornado.ioloop.IOLoop().instance()
autoreload.add_reload_hook(arfun)
autoreload.start(ioloop)

try:
    ioloop.start()
except KeyboardInterrupt:
    print("Caught Ctrl-C.")

emlsvr.stop()

print("Clean Exit.")

