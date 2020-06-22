from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class DocumentDetailsForm(FlaskForm):
    did = StringField('Document ID (did)', validators=[DataRequired()])
    wid = StringField('Workspace ID (wid)', validators=[DataRequired()])
    eid = StringField('Element ID (eid)', validators=[DataRequired()])
    submit = SubmitField('Set Info')