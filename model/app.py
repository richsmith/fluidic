import registry
import iotypes

class App(object):
    def __init__(self,
                 function,
                 name,
                 input = None,
                 output = None,
                 autoserial = True,
                 preferred_renderer = None,
                 aliases = []):
        self.function = function
        self.name = name
        self.aliases = aliases
        self.input = input
        self.output = output
        self.preferred_renderer = preferred_renderer

        if (autoserial):
            self._function = function
            self.function = self.execute_serially

    def __str__(self):
        return "App <" + str(self.name) + ">"

    def execute_serially(self, inputs, options, environment):
        if inputs == None or len(inputs) == 0: # bit of a hack?
            inputs = [None] # need one input so 0-arg apps will execute at all
        outputs = []
        for input in inputs:
            output = self._function(input, options, environment)
            #print "serial: output is " + str(output)
            if output == None:
                pass
            elif isinstance(output, list):
                for o in output:
                    outputs.append(o)
            else:
                outputs.append(output)
                

        return outputs

    def can_take(self, type):
        """Whether the specified type is a suitable input for the app"""
        # TODO
        # we need to consider hierarchies here; e.g. Any is superclass of all
        try:
            return (type in self.input) or (self.input == iotypes.Any)
        except TypeError:
            return type == self.input or self.input == iotypes.Any



def app(**kwargs):
    def app_wrapper(f):
        app = App(f, **kwargs)
        registry.AppRegistry.getInstance().register(app)
        return f
    return app_wrapper
