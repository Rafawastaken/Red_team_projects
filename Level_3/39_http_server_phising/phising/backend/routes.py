from flask import Blueprint, render_template

# Blueprint for backend
backend = Blueprint('backend', __name__)


# Backend Routes
@backend.route('/')
def home_backend():
    return render_template('backend/home.html')