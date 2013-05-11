class Builtin(object):
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

def builtin(**kwargs):
    def builtin_wrapper(f):
        builtin = Builtin(f, **kwargs)
        BuiltinRegistry.getInstance().register(builtin)
        return f
    return builtin_wrapper



        



# from http://stackoverflow.com/questions/42558/python-and-the-singleton-pattern
class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Other than that, there are
    no restrictions that apply to the decorated class.

    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.

    Limitations: The decorated class cannot be inherited from and the
    type of the singleton instance cannot be checked with `isinstance`. 

    """

    def __init__(self, decorated):
        self._decorated = decorated

    def getInstance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.

        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        """
        Call method that raises an exception in order to prevent creation
        of multiple instances of the singleton. The `Instance` method should
        be used instead.

        """
        raise TypeError(
            'Singletons must be accessed through the `Instance` method.')


@Singleton
class BuiltinRegistry():

    def __init__(self):
        self.builtins = set()

    def register(self, builtin):
        print "Registering " + builtin.name
        self.builtins.add(builtin)

    def get(self, name):
        #print "getting something from " + str(self.builtins)
        for b in self.builtins:
            if b.name == name:
                return b
