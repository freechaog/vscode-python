def command():
    commands = {}
    def register(command):
        def _register(fn):
            commands[command]=fn
            return fn
        return _register

    def default_fn():
        print('unknown command')
    
    def run():
        while True:
            cmd=input('>>>')
            if cmd.strip() == 'quit':
                return
            commands.get(cmd.strip(),default_fn)()
    return register,run


register,run=command()

@register('papa')
def papa():
    print('papa1')

run()


