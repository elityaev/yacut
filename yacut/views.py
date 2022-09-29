from urllib.parse import urljoin

from flask import render_template, flash, redirect, request

from . import app, db
from .forms import URLMapForm
from .models import URL_map
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    base_url = request.base_url
    print(base_url)
    form = URLMapForm()
    if form.validate_on_submit() and form.data is not None:
        if form.custom_id.data:
            short = form.custom_id.data
            if URL_map.query.filter_by(short=short).first():
                flash(f'Имя {short} уже занято!', 'used name')
                return render_template('index.html', form=form)
        else:
            short = get_unique_short_id()
        url_map = URL_map(
            original=form.original_link.data,
            short=short
        )
        db.session.add(url_map)
        db.session.commit()
        flash(f'{urljoin(base_url, short)}', 'short link')
    return render_template('index.html', form=form)


@app.route('/<string:id>')
def redirection_view(id):
    short = id
    url_map = URL_map.query.filter_by(short=short).first_or_404()
    original = url_map.original
    return redirect(original)
