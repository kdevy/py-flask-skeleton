from flask import render_template
from .BaseView import BaseView

class TopView(BaseView):
    def __init__(self, template):
        super().__init__(template)

    def dispatch_request(self):
        return render_template(self.template, **self.contexts)