from flask_sqlalchemy import SQLAlchemy
from flask import Flask,  request
from os import environ
from .models import Contact, db
from .config import Config


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URI


db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()


@app.route("/" )
def home():
    return "<p>Server is running</p>"



@app.route('/add_contact', methods=["POST"])
def add_contact():
	try:
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
	except:
		return "Server Error", 500

    


@app.route('/delete_contact', methods=["DELETE"])
def delete_contact():
	try:
		id = request.args.get('id')

		if id is None:
			return "Contact Id is required", 400

		contact = Contact.query.filter_by(id=id).first()
		if contact is None:
			return "No Contact Found", 404
		db.session.delete(contact)
		db.session.commit()
		return "Contact Deleted Successfully"
	except:
		return "Server Error", 500

if __name__ == '__main__':
    app.run(debug=True)