from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

with app.app_context():
    # App Config    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SECRET_KEY'] = 'SUPEROPSECRETKEYY'
    
    # App modules
    db = SQLAlchemy(app)

    # Login manager config
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'backend.login'
    login_manager.login_message_category = 'danger'
    login_manager.needs_refresh_message_category ='danger'
    login_manager.login_message = u'Necessário efetuar login para visualizar esta página'



    # Routes
    from .backend.routes import backend
    from .frontend.routes import frontend

    # Blueprints
    app.register_blueprint(backend, url_prefix ='/secret-backend')
    app.register_blueprint(frontend, url_prefix = '/')
    