from flask.views import View
from flask import render_template, current_app, url_for
from flask_login import current_user

class TopView(View):
    def __init__(self, template):
        self.template = template

    def dispatch_request(self):
        map = []
        for rule in current_app.url_map.iter_rules():

            options = {}
            for arg in rule.arguments:
                options[arg] = "[{0}]".format(arg)

            methods = ','.join(rule.methods)
            url = url_for(rule.endpoint, **options)
            route = {"endpoint": rule.endpoint, "methods": methods, "url": url}
            map.append(route)
        return render_template(self.template, user=current_user, map=map)