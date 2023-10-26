import os
from flask import Blueprint
from flask_login import login_required
from .views.TriggerView import TriggerView
from .views.CreateView import CreateView
from .views.SheetView import SheetView

modulename = os.path.basename(os.path.dirname(__file__))
app = Blueprint(modulename, __name__, template_folder="templates", static_folder="satic")
app.add_url_rule("/", view_func=login_required(TriggerView.as_view("top", modulename+"/trigger.html")))
app.add_url_rule("/<tabname>", view_func=login_required(TriggerView.as_view("tab", modulename+"/trigger.html")))
app.add_url_rule("/gettab/top", view_func=login_required(CreateView.as_view("_top", modulename+"/_top.html")))
app.add_url_rule("/gettab/create", view_func=login_required(CreateView.as_view("_create", modulename+"/_create.html")))
app.add_url_rule("/gettab/<sheetname>", view_func=login_required(SheetView.as_view("_sheet", modulename+"/_sheet.html")))
