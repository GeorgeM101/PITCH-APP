from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,SelectField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Edit bio',validators=[DataRequired()])
    submit = SubmitField('submit')

class PitchNow(FlaskForm):
    title = StringField('Pitch title',validators=[DataRequired()])
    category =SelectField ('Category',choices=[('Business','Business'),('Production','Production'),('Interview','Interview'),('Promotion','Promotion'),('Sales','Sales'),('Marketing','Marketing')],validators=[DataRequired()])
    description = TextAreaField('Pitch my idea',validators=[DataRequired()])
    submit = SubmitField('submit')

class MyComment(FlaskForm):
    comment = TextAreaField('Your comment',validators=[DataRequired()])
    submit = SubmitField('submit')

class UpVote(FlaskForm):
    upvote = SubmitField('submit')

class DownVote(FlaskForm):
    downvote = SubmitField('submit')