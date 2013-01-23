class DummyFunction(object):
    def __init__(self, name):
        self.name = name

    def call(self, *args, **kwargs):
        self.info = "%s(%s, %s) called on Dummy object" % (self.name,
                ", ".join([repr(x) for x in args]), kwargs)
        print self.info

    def __repr__(self):
        return self.name


class DummyGPIO:
    def __init__(self):
        pass

    def __getattr__(self, name):
        return DummyFunction(name).call