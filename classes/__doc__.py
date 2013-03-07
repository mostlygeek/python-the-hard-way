class MyClass():
    """Really I can access this with __doc__?"""

    # these are attributes on MyClass, not 
    # "instance" variables... 
    v = 10

    # special member, that creates instance variables 
    #...
    def __init__(self):
        # this will over-ride MyClass.v
        self.v = 9

        # Should be able to inject functions too...
        self.whoa = lambda : "Whoa... Lambda! "

    def f(self):
        return "hello"

    # this decorator is required...
    @staticmethod
    def g():
        return "world"

    # Why does this work? Well it seems that python
    # is really quite dynamic... so all the `def` declarations
    # are within the MyClass namespace so they create
    # new attributes, i guess we can jam arbitrary code into
    # here?
    print "I'm printing in the MyClass block...wtf?"

print "MyClass' __doc__: ", MyClass.__doc__

x = MyClass()
print x.f()
print MyClass.g()

# the injected lambda function...
print x.whoa()

# messing around with namespaces ...
print x.v, MyClass.v
MyClass.v = "changed"
print x.v, MyClass.v

