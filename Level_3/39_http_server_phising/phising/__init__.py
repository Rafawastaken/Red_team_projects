from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

with app.app_context():
    # App Config    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    
    # App modules
    db = SQLAlchemy(app)

    # Routes
    from backend.routes import backend
    from frontend.routes import frontend

    # Blueprints
    app.register_blueprint(backend, '/secret-backend')
    app.register_blueprint(frontend, '/')
    