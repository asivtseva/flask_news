from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

from . import app
from .models import Category


with app.app_context():
    def get_categories():
        return [(category.id, category.title) for category in Category.query.all()]

    class AddNewsForm(FlaskForm):
        title = StringField(
            'Название',
            validators=[
                DataRequired(message='Поле не должно быть пустым'),
                Length(max=255, message='Название должно быть не более 255 символов')
            ])
        text = TextAreaField(
            'Текст',
            validators=[DataRequired(message='Поле не должно быть пустым')]
        )
        category = SelectField(
            'Категория',
            choices=get_categories()
        )
        submit = SubmitField('Добавить')