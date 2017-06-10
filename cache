import inspect
import functools
import datetime
from collections import namedtuple

Node = {'data': '', 'prev': '', 'next': ''}

Item = namedtuple('Item', ['key', 'value', 'timestamp'])

def linked_list():
    _head = None
    _tail = None

    def put(item):
        nonlocal _head
        nonlocal _tail
        if _head is None:
            _head = {'data': item, 'prev': None, 'next': None}
        else:
            node = {'data': item, 'prev': None, 'next': _head}
            _head['prev'] = node
            _head = node
        if _tail is None:
            _tail = _head
        return _head

    def pop():
        nonlocal _tail
        if _tail is None:
            _head = None
            return None
        node = _tail
        _tail = node['prev']
        return node

    def remove(node):
        nonlocal _head
        nonlocal _tail
        if node is _head:
            _head = node['next']
        if node is _tail:
            pop()
            return
        node['prev']['next'] = node['next']
        node['next']['prev'] = node['prev']

    return put, pop, remove

def cache(maxsize=128, expire=0):
    def make_key(fn, args, kwargs):
        ret = []
        names = set()
        params = inspect.signature(fn).parameters
        keys = list(params.keys())
        for i, arg in enumerate(args):
            ret.append((keys[i], arg))
            names.add(keys[i])
        ret.extend(kwargs.items())
        names.update(kwargs.keys())
        for k, v in params.items():
            if k not in names:
                ret.append((k, v.default))
        ret.sort(key=lambda x: x[0])
        return '&'.join(['{}={}'.format(name, arg) for name, arg in ret])

    def _cache(fn):
        data = {}
        put, pop, remove = linked_list()

        @functools.wraps(fn)
        def wrap(*args, **kwargs):
            key = make_key(fn, args, kwargs)
            now = datetime.datetime.now().timestamp()
            if key in data.keys():
                node = data[key]
                item = node['data']
                remove(node)
                if expire == 0 or now - item.timestamp < expire:
                    data[key] = put(item)
                    return value
                else:
                    data.pop(key)
            value = fn(*args, **kwargs)
            if len(data) >= maxsize:
                # 过期清理
                if expire != 0:
                    expires = set()
                    for k, node in data.items():
                        if now - node['data'].timestamp >= expire:
                            pop(node)
                            expires.add(k)
                    for k in expires:
                        data.pop(k)
            if len(data) >= maxsize:
                # 换出
                # k = sorted(data.items(), key=lambda x: x[1][2])[0][0]
                node = pop()
                data.pop(node['data'].key)
            node = put(Item(key, value, now))
            data[key] = node
            return value

        return wrap

    return _cache

@cache(123,5)
def fish(x,y):
    return x+y

print(fish(1,2))