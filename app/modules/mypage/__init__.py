import os
from flask import Blueprint
from flask_login import login_required
from .views.TopView import TopView

modulename = os.path.basename(os.path.dirname(__file__))
app = Blueprint(modulename, __name__, template_folder="templates", static_folder="satic")
app.add_url_rule("/", view_func=login_required(TopView.as_view("top", modulename+"/top.html")))
