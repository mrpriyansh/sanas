
from flask import request 
from ..models import db, Contact

from app.contacts import bp

@bp.route('/add_contact', methods=["POST"])
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

    


@bp.route('/delete_contact', methods=["DELETE"])
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