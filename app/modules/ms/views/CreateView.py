from flask.views import View
from flask import render_template, current_app, url_for
from flask_login import current_user

class CreateView(View):
    def __init__(self, template):
        self.template = template

    def dispatch_request(self):
        return render_template(self.template, user=current_user)