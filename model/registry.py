
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
class AppRegistry():

    def __init__(self):
        self.apps = set() # <- Now redundant?
        self.by_alias = {}

    def register(self, app):
        self.apps.add(app)
        self.add_alias(app, app.name)
        for alias in app.aliases:
            self.add_alias(app, alias)

    def add_alias(self, app, alias):
        if (alias in self.by_alias):
            print "WARNING: Conflicting alias " + str(alias)
        self.by_alias[alias] = app

    def get(self, name):
        return self.by_alias[name] if name in self.by_alias else None

def get_app(name):
    """Returns an app by name"""
    registry = AppRegistry.getInstance()
    app = registry.get(name)
    return app

def get_all_apps():
    registry = AppRegistry.getInstance()
    return registry.apps
