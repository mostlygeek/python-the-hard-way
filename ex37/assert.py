def testAssert(a, b, c, d):
    assert a > 5      , "'A' must be greater than five"
    assert b == True  , "'B' must be True"
    assert c == False , "'C' must be False"
    assert d < 0      , "'D' must be a negative number"
    
# 
# Let's keep ourselve D.R.Y 
#
def runTest(f):
    assert hasattr(f, '__call__'), "Argument is not callable"

    try: 
        f()
    except AssertionError, e:
        print "Got: %r" % e

print "Running Assertions..."
runTest(lambda: testAssert(4, True, False, -1))
runTest(lambda: testAssert(6, False, False, -1))
runTest(lambda: testAssert(6, True, True, -1))
runTest(lambda: testAssert(6, True, False, 0))

# output looks like: 

# Running Assertions...
# Got: AssertionError("'A' must be greater than five",)
# Got: AssertionError("'B' must be True",)
# Got: AssertionError("'C' must be False",)
# Got: AssertionError("'D' must be a negative number",)
