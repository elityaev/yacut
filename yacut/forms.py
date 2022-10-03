from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp

from settings import MIN_LEN_CUSTOM_ID, MAX_LEN_CUSTOM_ID


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    URL(message='Не корректный URL')]
    )
    custom_id = URLField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(MIN_LEN_CUSTOM_ID,
                   MAX_LEN_CUSTOM_ID,
                   message='Длина не должна превышать 16 символов'),
            Optional(),
            Regexp(
                regex=r'[a-zA-Z0-9]*$',
                message='Использованы не корректные символы'
            )
        ]
    )
    submit = SubmitField('Создать')
