from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp

from settings import MAX_LEN_CUSTOM_ID, MAX_LEN_ORG_LINK, PATTERN


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            Length(max=MAX_LEN_ORG_LINK),
            DataRequired(message='Обязательное поле'),
            URL(message='Не корректный URL')]
    )
    custom_id = URLField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(max=MAX_LEN_CUSTOM_ID,
                   message='Длина не должна превышать 16 символов'),
            Optional(),
            Regexp(
                regex=PATTERN,
                message='Использованы не корректные символы'
            )
        ]
    )
    submit = SubmitField('Создать')
