# portfolio_app/app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configure your database URI and a secret key for Flask
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your_super_secret_key_here' # Change this to a strong, random key!

    db.init_app(app)

    # Import and register your blueprints
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    return app