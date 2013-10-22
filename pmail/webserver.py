import logging
from tornado import web
import os

class MainHandler(web.RequestHandler):
    def get(self):
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("template.html", title="My title", items=items)

application = web.Application(
    [
        (r"/", MainHandler),
    ], 
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "static")
)

