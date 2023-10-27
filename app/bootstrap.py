from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import URL
from werkzeug.urls import url_encode
from flask_login import LoginManager
import os
import logging
import time

db = None

start_time = time.time()

def create_app():
    global db
    db = SQLAlchemy()
    app = Flask(__name__)

    app.config["DEBUG"] = True

    app.secret_key = "TL3kMJFVYseSEDNhjPW5kcRDVQLtXdRwNpGUuBbz"

    app.logger.setLevel(logging.DEBUG)
    log_handler = logging.FileHandler(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "status/app.log"))
    log_formatter = logging.Formatter(
        '[%(asctime)s][%(levelname)s][%(module)s]: %(message)s')
    log_handler.setFormatter(log_formatter)
    log_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(log_handler)

    app.config["SQLALCHEMY_DATABASE_URI"] = URL.create(
        "mysql",
        username=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306,
        database=os.getenv("MYSQL_DATABASE"),
    )

    @app.before_request
    def before_request_callback():
        app.logger.info("init application -----------------")
        app.logger.info("request : path = %s, method = %s, remote addr = %s"% (request.path, request.method, request.remote_addr))
        app.logger.info("UA : %s"% (request.user_agent.string))

    @app.after_request
    def after_request_callback(response):
        global start_time
        lap = time.time() - start_time
        app.logger.info("lap : %s s"% (lap))
        app.logger.info("exsit")

        return response

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from models.User import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.context_processor
    def system():
        system = {
            "lang": "ja",
            "charset": "UTF-8",
        }
        return {"system": system}

    from modules import auth, main
    app.register_blueprint(auth.app)
    app.register_blueprint(main.app, url_prefix="/main")

    return app
