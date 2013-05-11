class Pipeline:

    def __init__(self):
        self.commands = []


    def get_input(self):
        if len(self.commands) == 0:
            return None
        else :
            return self.commands[0].app.input
    input = property(get_input)


    def get_output(self):
        if len(self.commands) == 0:
            return None
        else:
            return self.commands[-1].app.output
    output = property(get_output)


    def get_preferred_renderer(self):
        if len(self.commands) == 0:
            return None
        else:
            return self.commands[-1].app.preferred_renderer
    preferred_renderer = property(get_preferred_renderer)

    def execute(self, environment):
        data = None
        for command in self.commands:
            print 'executing ' + str(command) + ' for data ' + str(data)
            assert command.options != None
            data = command.app.function(data, command.options, environment)
            print 'pipeline: after executing ' + str(command) + \
                ', data is ' + str(data)
        return data


    def add(self, command):
        self.commands.append(command)


    def describe(self):
        description = '/ (Start of pipeline)\n'
        for command in self.commands:
            description += '\n' + str(command.app) + ' ' + str(command.options)
        description += '\n\\ (End of pipeline)\n'
        return description


    def __str__(self):
        return self.describe()
            


class Command:
    def __init__(self, app, options):
        self.app = app
        self.options = options

    def __str__(self):
        return '[Pipeline part command=' + str(self.app) + ']'
