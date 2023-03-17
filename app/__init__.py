from flask_sqlalchemy import SQLAlchemy
from flask import Flask,  request
from .models import  db
from config import Config

def create_app(config_class=Config): 

	app = Flask(__name__)
	app.config.from_object(config_class)

	# setup db
	app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URI
	db.init_app(app)

	@app.before_first_request
	def create_table():
		db.create_all()


	# setup contacts route
	from app.contacts import bp as contacts_bp
	app.register_blueprint(contacts_bp, url_prefix='/')
	


	@app.route("/" )
	def home():
		return "<p>Server is running</p>"

	if __name__ == '__main__':
		app.run(debug=True)

	return app