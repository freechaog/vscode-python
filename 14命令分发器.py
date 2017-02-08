import functools

def dispatcher():
    commands = {}

    def register(command):
        
        def _register(fn):
            commands[command] = fn
            return fn
        return _register


    def run():
        
        while True:
            command=input('>>>')
            if command.strip()=='quit':
                break
            commands.get(command)()
    return register, run

register, run = dispatcher()

@register('add')
def add():
    print(123)

run()