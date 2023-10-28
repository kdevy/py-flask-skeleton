from flask.views import View
from flask import request
from flask_login import current_user

class BaseView(View):
    def __init__(self, template):
        self.template = template
        self.contexts = {
          "user": current_user,
          "extend_template":  "ms/mainframe.html",
        }

        if request.args.get("inner"):
            self.contexts["extend_template"] = "ms/emptyframe.html"