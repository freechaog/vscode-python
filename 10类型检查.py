import inspect
import functools

def typed(fn):
    @functools.wraps(fn)
    def wrap(*args, **kwargs):
        params = inspect.signature(fn).parameters
        for k, v in kwargs.items():
            param = params[k].annotation
            if param.annotation != inspect._empty and not isinstance(v, param.annotation):
                raise TypeError('parameter {} required {}, but {}'.format(k, param.annotation, type(v)))
        for i, arg in enumerate(args):
            param = list(params.values())[i]
            if param.annotation != inspect._empty and not isinstance(arg, param.annotation):
                raise TypeError('parameter {} required {}, but {}'.format(param.name, param.annotation, type(arg)))
        return fn(*args, **kwargs)
    return wrap


@typed
def add(x: int, y:int) -> int:
    return x + y

print(add(1,2))
print(add(1,'2'))
