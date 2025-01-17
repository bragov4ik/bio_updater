import datetime
import pytz

from credentials import credentials


CHECK_INTERVAL = 3

TIME_ZONE = 'Etc/GMT-3'

INTERNET_CHECK_URL = '1.1.1.1'

BIO_MESSAGES = [
    'Сейчас %s.',
    'Кстати, сейчас %s.',
    'Кстати, сейчас уже %s.',
    'Уже %s.',
    'На часах %s',
    '%s',
    'Точное время: %s',
    'МСК время: %s',
    ]

DATE_FROM = datetime.datetime(2022, 2, 24, 3, 0, 0, tzinfo=pytz.UTC) 

TIME_LEFT_MESSAGE = 'Прошло уже %s'