from flask import Flask

app = Flask(__name__)

from app import views
from app import config

#
# Will be used everywhere in the code
# USAGE : `from app import loki`
#

import logging

# create logger
loki = logging.getLogger('Loki')
loki.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(config.LOG_LEVEL)

# create formatter
formatter = logging.Formatter('[%(levelname)s] [%(asctime)s] [%(funcName)s:%(filename)s:%(lineno)d] %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
loki.addHandler(ch)