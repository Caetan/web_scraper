from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, Form
from wtforms.validators import DataRequired


# This must inherit from base form class:
class AircraftForm(FlaskForm):
	id = TextField('ID')
	operator = TextField('Operator name', validators=[DataRequired()])
	model = TextField('Aircraft model', validators=[DataRequired()])
	registration = StringField('Aircraft registration', validators=[DataRequired()])
	cn_fl = StringField('CN/FL', validators=[DataRequired()])
	submit = SubmitField('Create Aircraft')


class UpdateForm(FlaskForm):
	id = TextField('ID')
	operator = TextField('Operator name', validators=[DataRequired()])
	model = TextField('Aircraft model', validators=[DataRequired()])
	registration = StringField('Aircraft registration', validators=[DataRequired()])
	cn_fl = StringField('CN/FL', validators=[DataRequired()])
	submit = SubmitField('Update Aircraft')


class SearchForm(FlaskForm):
	#id = TextField('ID')
	operator = TextField('Operator name', validators=[DataRequired()])
	#model = TextField('Aircraft model')
	#registration = StringField('Aircraft registration')
	#cn_fl = StringField('CN/FL')
	submit = SubmitField('Search Aircraft')