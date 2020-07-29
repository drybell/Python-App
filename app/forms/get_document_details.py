from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import *

class DocumentDetailsForm(FlaskForm):
    url    = StringField('Feature Studio URL', validators=[DataRequired()])
    feature_title = StringField('Feature Studio Title', validators=[DataRequired()])
    image  = FileField('', validators=[FileRequired()])
    submit = SubmitField('Set Info')