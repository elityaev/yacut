import random
import string
from datetime import datetime

from settings import MAX_LEN_CUSTOM_ID, LEN_SHORT_ID
from yacut import db


class URL_map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, nullable=False)
    short = db.Column(db.String(MAX_LEN_CUSTOM_ID), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())

    def to_dict(self):
        return dict(
            id=self.id,
            original=self.original,
            short=self.short,
            timestamp=self.timestamp,
        )

    def from_dict(self, data):
        for field in ['original', 'short', 'timestamp']:
            if field in data:
                setattr(self, field, data[field])

    @staticmethod
    def get_unique_short_id():
        return ''.join(random.choices
                       (string.ascii_letters + string.digits, k=LEN_SHORT_ID))

    @staticmethod
    def create(original, short):
        url_map = URL_map(
            original=original,
            short=short
        )
        db.session.add(url_map)
        db.session.commit()
        return url_map

    @staticmethod
    def short_id_exists(value):
        return URL_map.query.filter_by(short=value).first()

    @staticmethod
    def short_id_exists_or_404(value):
        return URL_map.query.filter_by(short=value).first_or_404()