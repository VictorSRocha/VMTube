from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Regexp

class VideosForm(FlaskForm):
	videos = TextAreaField('Cole a URL dos seus vídeos:', render_kw={'placeholder': 'Youtube URLs...'})
	submit = SubmitField('Enviar')