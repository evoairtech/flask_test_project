from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TextForm(FlaskForm):
    UserInput = StringField('Enter text:', validators=[DataRequired()])
    submit = SubmitField('Submit')
