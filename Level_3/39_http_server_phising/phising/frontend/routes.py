from flask import Blueprint

# Register frontend blueprint
frontend = Blueprint('frontend', __name__)

# Frontend blueprints

@frontend.route('/')
def home_frontend():
    return "This is the frontend"