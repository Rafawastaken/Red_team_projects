from phising import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    alias = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String(180), unique = False, nullable = False)

    def __repr__(self):
        return f"<User_{db.alias}"
    

class Target(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String, nullable = False, unique = False)
    password = db.Column(db.String(100), unique = False, nullable = False)

    def __repr__(self):
        return f"<Target_{db.email}>"

db.create_all()