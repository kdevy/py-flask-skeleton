import os
from flask import Blueprint, redirect
from flask_login import login_required
from .views.LoginView import LoginView
from .views.SginUpView import SginUpView
from .views.LogoutView import LogoutView

app = Blueprint(os.path.basename(os.path.dirname(__file__)), __name__, template_folder="templates", static_folder="satic")

app.add_url_rule("/", view_func=lambda: redirect("/login"))
app.add_url_rule("/login", view_func=LoginView.as_view("login", "login.html"), methods=["GET", "POST"])
app.add_url_rule("/sginup", view_func=SginUpView.as_view("sginup", "sginup.html"), methods=["GET", "POST"])
app.add_url_rule("/logout", view_func=login_required(LogoutView.as_view("logout")))
