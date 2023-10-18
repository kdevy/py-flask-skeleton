from flask.views import View
from flask import render_template
from flask_login import current_user

class TopView(View):
    def __init__(self, template):
        self.template = template

    def dispatch_request(self):
        values = current_user
        return render_template(self.template, data=values)