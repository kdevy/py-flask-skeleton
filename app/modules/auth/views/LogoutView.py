from flask.views import View
from flask import redirect
from flask_login import logout_user

class LogoutView(View):
    def dispatch_request(self):
        logout_user()
        return redirect("/login")