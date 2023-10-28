import os
from flask import Blueprint
from flask_login import login_required
from .views.IndexView import IndexView
from .views.TopView import TopView
from .views.CreateView import CreateView
from .views.SheetView import SheetView

modulename = os.path.basename(os.path.dirname(__file__))
app = Blueprint(modulename, __name__, template_folder="templates", static_folder="satic")
app.add_url_rule("/", view_func=login_required(IndexView.as_view("index")))
app.add_url_rule("/top", view_func=login_required(TopView.as_view("top", modulename+"/top.html")))
app.add_url_rule("/create", view_func=login_required(CreateView.as_view("create", modulename+"/create.html")))
app.add_url_rule("/<sheetname>", view_func=login_required(SheetView.as_view("sheet", modulename+"/sheet.html")))
