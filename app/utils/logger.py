import logging

#
# Will be used everywhere in the code
# USAGE : `from app import loki`
#

# create logger
logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('[%(levelname)s] [%(asctime)s] [%(funcName)s:%(filename)s:%(lineno)d] %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)