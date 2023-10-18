from flask.views import View
from flask import render_template, request, jsonify, current_app
from models.User import User
from werkzeug.security import generate_password_hash, check_password_hash
from bootstrap import db

class SginUpView(View):
    def __init__(self, template):
        self.template = template

    def dispatch_request(self):
        if (request.method == "POST"):
            action = request.form.get("action")

            if (action == "sginup"):
                return self.sginup_post()

        return render_template(self.template)

    def sginup_post(self):
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        user = User.query.filter_by(email=email).first()

        errors = []
        if not name:
            errors.append("名前を入力してください。")
        if not email:
            errors.append("メールアドレスを入力してください。")
        if not password:
            errors.append("パスワードを入力してください。")
        if len(password) < 8:
            errors.append("パスワードは8文字以上で入力してください。")
        if not confirm_password:
            errors.append("確認用パスワードを入力してください。")
        if password != confirm_password:
            errors.append("パスワードが一致しません。")
        if errors:
            return jsonify({"ok":False, "errors": errors})

        if user:
            return jsonify({"ok":False, "errors": ["入力内容を確認してください。"]})

        new_user = User(email=email, name=name, password=generate_password_hash(password, method='pbkdf2:sha256'))
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"ok":True})
