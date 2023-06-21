from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_wtf.form import FlaskForm
from wtforms.fields.simple import TextAreaField
from wtforms import SubmitField

class UploadImageForm(FlaskForm):
    image = FileField(
        validators=[
            FileRequired("choose a picture"),
            FileAllowed(["png", "jpg", "jpeg"], "not allowed")
        ]
    )
    submit = SubmitField("Upload")
    
class DetectorForm(FlaskForm):
    submit = SubmitField("Detect")
    
class DeleteForm(FlaskForm):
    submit = SubmitField("Delete")