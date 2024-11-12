from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuration settings
    app.config.from_object('config')

    # Initialize extensions
    db.init_app(app)

    # Register blueprints or routes
    from .routes import main
    app.register_blueprint(main)

    return app
