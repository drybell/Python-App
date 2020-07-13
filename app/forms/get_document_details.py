from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import *

class DocumentDetailsForm(FlaskForm):
    did    = StringField('Document ID (did)', validators=[DataRequired()])
    wid    = StringField('Workspace ID (wid)', validators=[DataRequired()])
    eid    = StringField('Element ID (eid)', validators=[DataRequired()])
    feature_title = StringField('Feature Studio Title', validators=[DataRequired()])
    image  = FileField('Image File', validators=[FileRequired()])
    submit = SubmitField('Set Info')