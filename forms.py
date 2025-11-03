from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired

class TextForm(FlaskForm):
    x = IntegerField('Enter x:', validators=[DataRequired()])
    y = IntegerField('Enter y:', validators=[DataRequired()])
    name = StringField('Enter name (optional)')
    submit = SubmitField('Calculate')
