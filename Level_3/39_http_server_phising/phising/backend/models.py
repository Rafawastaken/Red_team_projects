from phising import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    alias = db.Colum(db.String, unique = True, nullable = False)
    password = db.Column(db.String(180), unique = False, nullable = False)

    def __repr__(self):
        return f"<User_{db.alias}"