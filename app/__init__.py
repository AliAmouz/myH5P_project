from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:your_password_for_mySQL@localhost/h5p_test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    db.init_app(app)
    login_manager.init_app(app)

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
