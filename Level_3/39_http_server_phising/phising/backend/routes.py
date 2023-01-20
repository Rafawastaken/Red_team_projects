from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user, logout_user, login_user


from phising import app, db
from .forms import AddUserForm
from .models import User

# Blueprint for backend
backend = Blueprint('backend', __name__)


# Backend Routes
@backend.route('/')
def home_backend():
    return render_template('backend/home.html')

@backend.route('/add-user', methods = ['POST', 'GET'])
def add_user():
    form = AddUserForm()

    # add user to database
    if form.validate_on_submit():
        alias = form.alias.data
        password = form.password.data

        new_user = User(alias = alias, password = password)
        db.session.add(new_user)
        db.session.commit()

        flash(f"User - {alias} - added with success!", "success")
        return "User adicionado"
    else:
        flash("Something went wrong", "danger")

    return render_template('backend/register.html', form = form)

@backend.route('/login')
def login():
    return "Login page"