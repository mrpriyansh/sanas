from flask_sqlalchemy import SQLAlchemy
from flask import Flask,  request
from os import environ

app = Flask(__name__)

DATABASE_URI = environ.get("DATABASE_URI")
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

db = SQLAlchemy()

db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    middle_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    phone_no = db.Column(db.String(13))
    phone_ext = db.Column(db.String(3))
    
@app.route("/" )
def home():
    return "<p>Server is running</p>"



@app.route('/add_contact', methods=["POST"])
def add_contact():
    request_data = request.get_json()

    required_field = ["phone_no", "phone_ext"]

    for field in required_field:
        if request_data[field] is None:
             response = field +" is required!"
             return response , 400

    first_name = request_data['first_name']
    middle_name = request_data['middle_name']
    last_name = request_data['last_name']
    phone_no = request_data['phone_no']
    phone_ext = request_data['phone_ext']

    contact = Contact(first_name=first_name, middle_name=middle_name, last_name=last_name, phone_no=phone_no, phone_ext=phone_ext)

    db.session.add(contact)
    db.session.commit()
    return "Contact Added Successfully"


@app.route('/delete_contact', methods=["DELETE"])
def delete_contact():
    id = request.args.get('id')

    if id is None:
        return "Contact Id is required", 400

    contact = Contact.query.filter_by(id=id).first()
    if contact is None:
        return "No Contact Found", 404
    db.session.delete(contact)
    db.session.commit()
    return "Contact Deleted Successfully"

if __name__ == '__main__':
    app.run(debug=True)