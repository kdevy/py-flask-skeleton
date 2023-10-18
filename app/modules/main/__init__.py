import os
from flask import Blueprint
from flask_login import login_required
from .views.TopView import TopView

app = Blueprint(os.path.basename(os.path.dirname(__file__)), __name__, template_folder="templates", static_folder="satic")
app.add_url_rule("/", view_func=login_required(TopView.as_view("top", "top.html")))
