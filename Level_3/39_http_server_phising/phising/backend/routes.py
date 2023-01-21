from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user, logout_user, login_user


from phising import app, db
from .forms import AddUserForm, LoginUserForm
from .models import User

# Blueprint for backend
backend = Blueprint('backend', __name__)


# Backend Routes
@backend.route('/')
@login_required
def home_backend():
    return render_template('backend/home.html')

# Add user to backend
@backend.route('/add-user', methods = ['POST', 'GET'])
@login_required
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
        return redirect(url_for('backend.allowed_users'))
    else:
        flash("Something went wrong", "danger")

    return render_template('backend/register.html', form = form)

# Login User to backend
@backend.route('/login', methods = ['POST', 'GET'])
def login():
    form = LoginUserForm()

    if form.validate_on_submit():
        user_login = User.query.filter_by(alias = form.alias.data).first()
        if user_login:
            login_user(user_login)
            flash(f"Welcome back {user_login.alias}", "success")
            return redirect(url_for('backend.home_backend'))

    return render_template('backend/login.html', form = form)

@backend.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Goodbye!", "success")
    return redirect(url_for('backend.login'))

# View all users
@backend.route('/users', methods = ['POST', 'GET'])
def allowed_users():
    users = User.query.all()
    return render_template('backend/allowed_users.html', users = users)

# Delete User
@backend.route('/delete/<int:id>', methods = ['POST'])
def delete_user(id):
    user_delete = User.query.filter_by(id = id).first()
    db.session.delete(user_delete)
    db.session.commit()
    flash(f"User: {user_delete.alias} removed", "success")
    return redirect(url_for('backend.allowed_users'))