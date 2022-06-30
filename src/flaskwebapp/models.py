from flaskwebapp import db
from datetime import datetime

# first database
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(20), unique=True, nullable=False)
	username = db.Column(db.String(120), unique=True, nullable=False)
	posts = db.relationship('Post', backref='author', lazy=True)
	
	# how we'll print/display database
	def __repr__(self):
		return f"User('{self.username}', '{self.email}')"
		
# second database which is related to first
class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # specify relationship with User db
	
	# how we'll print/display database
	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}')"
		
# create a class for database called Collections (required)
class Collections(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	disease_term = db.Column(db.String(100), nullable=False)
	title = db.Column(db.String(100), nullable=False)
	samples = db.relationship('Samples', backref='author', lazy=True) # RE-CHECK THIS LINE
	
	# how we'll print/display database
	def __repr__(self):
		return f"Collections('{self.id}', '{self.disease_term}', '{self.title}')"
		
# create a class for database called Samples (required)
class Samples(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	collection_id = db.Column(db.Integer, db.ForeignKey('collections.id'), nullable=False) # here we specify relationship with Collections db
	donor_count = db.Column(db.Integer, nullable=False)
	material_type = db.Column(db.String(50), nullable=False)
	last_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	
	# how we'll print/display database
	def __repr__(self):
		return f"Samples('{self.id}', '{self.collection_id}', '{self.donor_count}', '{self.material_type}', '{self.last_updated}')"