import random
import string

from yacut.constants import LEN_SHORT_ID


def get_unique_short_id():
    return ''.join(random.choices
                   (string.ascii_letters + string.digits, k=LEN_SHORT_ID))
