from flask import Blueprint, render_template
from flask_login import login_required, current_user, logout_user, login_user

from .forms import AddUserForm
from .models import User

# Blueprint for backend
backend = Blueprint('backend', __name__)


# Backend Routes
@backend.route('/')
def home_backend():
    return render_template('backend/home.html')

@backend.route('/add-user')
def add_user():
    form = AddUserForm()
    return render_template('backend/register.html', form = form)

@backend.route('/login')
def login():
    return "Login page"