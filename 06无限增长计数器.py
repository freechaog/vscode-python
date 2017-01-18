def make_inc():
    def counter():
        x=0
        while True:
            x+=1
            yield x
    c = counter()
    return lambda:next(c)