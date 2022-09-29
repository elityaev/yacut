import re
from urllib.parse import urljoin

from flask import request, jsonify

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URL_map
from .views import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def create_id():
    base_url = request.root_url
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    elif 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    elif (
            'custom_id' in data and
            data.get('custom_id') != '' and
            data.get('custom_id') is not None):
        if (len(data['custom_id']) > 16 or
                re.match('[a-zA-Z0-9]*$', data['custom_id']) is None):
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки',
            )
        elif URL_map.query.filter_by(short=data['custom_id']).first() is not None:
            raise InvalidAPIUsage(f'Имя "{data["custom_id"]}" уже занято.')
        else:
            short = data['custom_id']
    else:
        short = get_unique_short_id()
    url_map = URL_map(
        original=data['url'],
        short=short
    )
    db.session.add(url_map)
    db.session.commit()
    return jsonify({
        'url': url_map.original,
        'short_link': urljoin(base_url, short),
    }), 201


@app.route('/api/id/<path:short_id>/', methods=['GET'])
def get_url(short_id):
    url_map = URL_map.query.filter_by(short=short_id).first()
    if url_map is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': url_map.original}), 200
