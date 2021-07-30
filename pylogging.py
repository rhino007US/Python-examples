# python's Logging
import logging
import logging.config
import traceback
logging.config.fileConfig('logging.conf')
# logging.config.dictConfig('logging.conf')
# logger = logging.getLogger(__name__)
logger = logging.getLogger('simpleExample')
logger.debug('this is a debug message')

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
# logging.debug('this is a debug message')
# logging.info('this is a info message')
# logging.warning('this is a warning message')
# logging.error('this is a error message')
# logging.critical('this is a critical message')
# import helper
# stream and file logging, with levels and handlers
logger = logging.getLogger(__name__)

# create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.out')

# level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('thei is an error')

try:
    a=[1,2,3]
    val = a[4]
# except IndexError as e:
#    logging.error(e, exc_info=True)

# except:   will show any kind of error, not just IndexError as above calling traceback
except:
    logging.error("The error is %s", traceback.format_exc())

from logging.handlers import RotatingFileHandler
# import time
# from logging.handlers import TimeRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 2KB, and keep backup logs app.log.1, app.log.2 etc.
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
# s, m,  h, d, midnight, w0 (monday)
# handler = TimeRotatingFileHandler('timed_test.log', when='s', interval=5 backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info("Hello World")
#   time.sleep(5)
