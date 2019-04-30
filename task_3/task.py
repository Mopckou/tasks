import sys
import time
import logging


def setup_logger(name_log, verbosity='debug'):
    LOG_LEVEL = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warn': logging.WARN,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    file_handler = logging.FileHandler(filename='%s.txt' % name_log)

    formatter1 = logging.Formatter(
        r'%(asctime)s [%(name)s] [%(levelname)s] %(message)s', "%Y-%m-%d %H:%M:%S")

    file_handler.setFormatter(formatter1)
    file_handler.setLevel(logging.DEBUG)

    logger = logging.getLogger(name_log)
    logger.addHandler(file_handler)
    logger.setLevel(LOG_LEVEL.get(verbosity))


setup_logger('time logging')
logger = logging.getLogger('time logging')


def measure(func):

    def _measure_time(*args, **kwargs):
        before = time.time()
        result = func(*args, **kwargs)
        after = time.time()

        result_time = int(after - before)
        min = result_time // 60
        sec = result_time % 60

        logger.debug('Method name: %s. Lead time: %s min, %s sec.' % (func.__name__, min, sec))

        return result

    return _measure_time


class SERVER:

    @measure
    def function_one(self, param):
        print(param)
        time.sleep(10)
        self.__internal_function()

    @measure
    def __internal_function(self):
        time.sleep(3)

    @measure
    def function_two(self, *args, **kwargs):
        print(args)

        for key, value in kwargs.items():
            print(key, value)


server = SERVER()
server.function_one('something')
server.function_two(1, 'something_string', [1, 3, 4, 5], param_one=3, param_two=None)
