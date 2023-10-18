from flask.views import View
from flask import render_template, request, jsonify
from werkzeug.security import check_password_hash
from flask_login import login_user
from models.User import User

class LoginView(View):
    def __init__(self, template):
        self.template = template

    def dispatch_request(self):
        if (request.method == "POST"):
            action = request.form.get("action")

            if (action == "login"):
                return self.login_post()

        return render_template(self.template)

    def login_post(self):
        email = request.form.get("email")
        password = request.form.get("password")
        remember = True if request.form.get('remember') else False

        user = User.query.filter_by(email=email).first()

        errors = []
        if not email:
            errors.append("メールアドレスを入力してください。")
        if not password:
            errors.append("パスワードを入力してください。")
        if errors:
            return jsonify({"ok":False, "errors": errors})
        if not user or not check_password_hash(user.password, password):
            return jsonify({"ok":False, "errors": ["入力内容を確認してください。"]})

        login_user(user, remember=remember)
        return jsonify({"ok":True})
