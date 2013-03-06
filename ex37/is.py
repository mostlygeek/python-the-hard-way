#
# Testing the `is` keyword in Python
#
# from: http://stackoverflow.com/a/2987975/445792
#   " `is` is for testing identity not equality, ie: comparing memory addresses

def testIt(code, globalVals=None, localVals=None):
    print "Code [ %-30s ] : %r" % (code, eval(code, globalVals, localVals))


testIt("'string' is 'string'")

# small strings are interned automatically, so this is True
testIt("""("a" * 10) is ("a" * 10)""")

# Large strings are not interned, so this is False
testIt(""" ("a" * 100) is ("a" * 100) """)

a = range(1,5)
b = range(1,5)
c = a

# returning references...
def echo(a): return a
def append(a):
    a.append(6)
    return a

globalVals = {'a': a, 'b': b, 'c': c, 'echo': echo, 'append': append}

from inspect import getsourcelines

print "\n`echo` function:"
print "------------------"
print "".join(getsourcelines(echo)[0])

tests = [
      "a == b"
    , "a is b"
    , "c is a"
    , "a == echo(a)"
    , "a is echo(a)"
]
for t in tests: 
    testIt(t, globalVals)


print "\n`append` function:"
print "------------------"
print "".join(getsourcelines(append)[0])

tests = [
      "a == append(a)"      # True
    , "a is append(a)"      # changes the object, so True
    , "c == a"              # points to the same thing, so True
]
for t in tests: 
    testIt(t, globalVals)

def gimme(val): 
    return val
print "\n`gimme()` function:"
print "------------------"
print "".join(getsourcelines(gimme)[0])

# value types should be interned
tests = [
      "5 == gimme(5)"
    , "5 is gimme(5)"
    , "gimme(5) == gimme(5)"
    , "gimme(5) is gimme(5)"
]
for t in tests: 
    testIt(t, {'gimme': gimme})

