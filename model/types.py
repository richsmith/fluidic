class Builtin2(object):
    def __init__(self,
                 function,
                 name,
                 input = None,
                 output = None,
                 output_collection = None):
        self.function = function
        self.name = name
        self.input = input
        self.output = output
        self.output_collection = output_collection

    def __str__(self):
        return "Builtin <" + str(self.name) + ">"

# IO types
class Html(object):
    def foo():
        pass


