#
# More `with` hacking
#

class MyThing():
    # 
    # ... the constructor takes an argument
    #
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        return MyThing("New Thing: %s" % self.name)
    def __exit__(self, type, value, traceback):
        print "Exiting"
        return True

thing = MyThing("Test")

# .. the __init__ takes an arg, so we need it when using `with`
with MyThing("Boom") as thing:
    print thing.name   #New Thing: Boom


