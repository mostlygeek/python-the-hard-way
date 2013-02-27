def print_two(*args): 
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1): 
    print "arg1: %r" % arg1

def print_none():
    print "I got nothin'."

# This can take a variable number of args and print them
# out w/ their position
def print_args(*args):
    # *args is a tuple, meanin any number of arguments
    for i,val in enumerate(args): # `enumerate` gives us an index
        print "arg%d: %r, " % (i, val),
    print

# this can print out an arbitrary number of keyword arguments
def print_kargs(**kwargs):
    # `**kargs` is a dictionary, meaning any number of keyword args
    for k in kwargs.iterkeys():
        print "arg[%r]: %r" % (k, kwargs[k])

print_two("Ben", "Wong") 
print_two_again("Benson", "Wong")
print_one("First!")
print_none()

# what happens when we give 3?
try:
    print_two("one", "two", "three")
except ValueError: 
    print "It blows up w/ too many values to unpack"

print_args(1, "hello", "world", 3, "bar")

print_kargs(name="Benson", age="33")
