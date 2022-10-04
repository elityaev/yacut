import re
from http import HTTPStatus
from urllib.parse import urljoin

from flask import request, jsonify

from settings import MAX_LEN_CUSTOM_ID, PATTERN
from . import app
from .error_handlers import InvalidAPIUsage
from .models import URL_map


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
        if (len(data['custom_id']) > MAX_LEN_CUSTOM_ID or
                re.match(PATTERN, data['custom_id']) is None):
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки',
            )
        elif URL_map.short_id_exists(data['custom_id']):
            raise InvalidAPIUsage(f'Имя "{data["custom_id"]}" уже занято.')
        else:
            short = data['custom_id']
    else:
        short = URL_map.get_unique_short_id()
    url_map = URL_map.create(data['url'], short)
    return jsonify({
        'url': url_map.original,
        'short_link': urljoin(base_url, short),
    }), HTTPStatus.CREATED


@app.route('/api/id/<path:short_id>/', methods=['GET'])
def get_url(short_id):
    url_map = URL_map.short_id_exists(short_id)
    if url_map is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': url_map.original}), HTTPStatus.OK
