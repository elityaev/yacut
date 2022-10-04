from urllib.parse import urljoin

from flask import render_template, flash, redirect, request

from . import app
from .forms import URLMapForm
from .models import URL_map


@app.route('/', methods=['GET', 'POST'])
def index_view():
    base_url = request.base_url
    form = URLMapForm()
    if form.validate_on_submit() and form.data is not None:
        if form.custom_id.data:
            short = form.custom_id.data
            if URL_map.short_id_exists(short):
                flash(f'Имя {short} уже занято!', 'used name')
                return render_template('index.html', form=form)
        else:
            short = URL_map.get_unique_short_id()
        URL_map.create(form.original_link.data, short)
        flash(f'{urljoin(base_url, short)}', 'short link')
    return render_template('index.html', form=form)


@app.route('/<string:id>')
def redirection_view(id):
    url_map = URL_map.short_id_exists_or_404(id)
    original = url_map.original
    return redirect(original)
