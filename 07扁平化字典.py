def flatten(d):
    def _flatten(src, dst, prefix = ""):
        for k, v in src.items():
            key = k if prefix == "" else "{}.{}".format(prefix, k)
            if isinstance(v,dict):
                _flatten(v, dst, k)
            else:
                dst[key] = v
    result = {}
    _flatten(d,result)
    return result
s=flatten({'a':1, 'b':{'c':2,'d':3}})
print(s)

