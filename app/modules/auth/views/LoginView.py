from flask.views import View
from flask import render_template, request, jsonify
from werkzeug.security import check_password_hash
from flask_login import login_user
from models.User import User
from ..forms.LoginForm import LoginForm

class LoginView(View):
    def __init__(self, template):
        self.template = template
        self.form = LoginForm()

    def dispatch_request(self):
        if (request.method == "POST"):
            action = request.form.get("action")

            if (action == "login"):
                return self.login_post()

        return render_template(self.template, form=self.form)

    def login_post(self):
        user = User.query.filter_by(email=self.form.email.data).first()

        if not self.form.validate_on_submit():
            return jsonify({"ok":False, "errors": self.form.errors})
        if not user or not check_password_hash(user.password, self.form.password.data):
            return jsonify({"ok":False, "errors": ["入力内容を確認してください。"]})

        login_user(user, remember=self.form.remember.data)
        return jsonify({"ok":True})
