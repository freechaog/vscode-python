import functools
import datetime
import time

def logger(s):
    def _logger(fn):
        @functools.wraps(fn)
        def wrap(*args, **kwargs):
            start = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            end = datetime.datetime.now()
            if (end-start).total_seconds() > s:
                print('call {} took {}'.format(fn.__name__, end-start))
            return ret
        return wrap
    return _logger

@logger(2)
def sleep(x):
    time.sleep(x)


sleep(4)