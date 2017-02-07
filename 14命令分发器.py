import functools

def dispatcher():
    commands = {}

    def register(command, fn):
        @functools.wraps(fn)
        def wrap(*args, **kwargs):
            commands[command] = fn
            return fn
        return wrap


    def run():
        
        while True:
            command=input('>>>')
            if command.strip()=='quit':
                break
            commands[command]()
    return register, run

def add():
    print(123)

register, run = dispatcher

