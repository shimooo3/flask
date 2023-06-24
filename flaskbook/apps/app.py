from pathlib import Path
from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from apps.config import config


db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()
login_manager.login_view = "auth.signup"
login_manager.login_message = ""

def create_app(config_key):
    app = Flask(__name__)
    
    app.config.from_object(config[config_key])
    
    csrf.init_app(app)    
    db.init_app(app)
    Migrate(app, db)
    login_manager.init_app(app)
    
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)
    
    from apps.crud import views as crud_views
    app.register_blueprint(crud_views.crud, url_prefix="/crud")
    
    from apps.auth import views as atuth_views
    app.register_blueprint(atuth_views.auth, url_prefix = "/auth")
    
    from apps.detector import views as dt_views
    app.register_blueprint(dt_views.dt)

    return app

def page_not_found(e):
    """"404 not found"""
    return render_template("404.html"), 404

def internal_server_error(e):
    """500 internal server error"""
    return render_template("500.html"), 500