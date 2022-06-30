from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, DateField
from wtforms.validators import DataRequired

# form to add new collection
class CollectionForm(FlaskForm):
	disease_term = StringField('Disease Term', validators = [DataRequired()])
	title = StringField('Title', validators = [DataRequired()])
	submit = SubmitField('Submit Collection')
	
# form to add new sample
class SampleForm(FlaskForm):
	collection_id = IntegerField('Collection ID', validators = [DataRequired()])
	donor_count = IntegerField('Donor Count', validators = [DataRequired()])
	material_type = StringField('Material Type', validators = [DataRequired()])
	last_updated = DateField('Last Updated', validators = [DataRequired()])
	submit = SubmitField('Submit Sample')