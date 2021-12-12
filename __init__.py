from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

load_dotenv()

db = SQLAlchemy()
bcrypt=Bcrypt()
def create_app():
    app = Flask(__name__) 
    app.config['SECRET_KEY'] = os.urandom(12)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("sql_url")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager = LoginManager(app)
    login_manager.login_view = 'routes.index'
    login_manager.login_message_category = 'info'
    from models import User
    @login_manager.user_loader
    def load_user(user_id):  
        return User.query.get(int(user_id))
    from routes import routes as routes_blueprint
    app.register_blueprint(routes_blueprint)
    return app
