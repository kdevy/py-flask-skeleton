from flask.views import View
from flask import render_template, request, jsonify, current_app
from models.User import User
from werkzeug.security import generate_password_hash
from bootstrap import db
from ..forms.SginUpForm import SginUpForm

class SginUpView(View):
    def __init__(self, template):
        self.template = template
        self.form = SginUpForm()

    def dispatch_request(self):
        if (request.method == "POST"):
            action = request.form.get("action")

            if (action == "sginup"):
                return self.sginup_post()

        return render_template(self.template, form=self.form)

    def sginup_post(self):
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        user = User.query.filter_by(email=email).first()

        if not self.form.validate_on_submit():
            return jsonify({"ok":False, "errors": self.form.errors})
        if user:
            return jsonify({"ok":False, "errors": ["入力内容を確認してください。"]})

        new_user = User(email=email, name=name, password=generate_password_hash(password, method='pbkdf2:sha256'))
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"ok":True})
