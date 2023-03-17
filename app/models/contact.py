from .db import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    middle_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    phone_no = db.Column(db.String(13))
    phone_ext = db.Column(db.String(3))