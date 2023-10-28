from flask.views import View
from flask import redirect

class IndexView(View):
    def __init__(self):
        pass

    def dispatch_request(self):
        return redirect("./top")