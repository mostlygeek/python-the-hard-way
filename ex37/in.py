def testIn(val): 
    assert isinstance(val, int), "Expecting a number"

    a = range(1,10)

    if val in a:
        print "Yup, %d is in there!" % val
    else:
        print "No , %d is not there" % val

testIn(0)
testIn(1)
testIn(5)
testIn(10)
testIn("A")

# Output
# 
# No , 0 is not there
# Yup, 1 is in there!
# Yup, 5 is in there!
# No , 10 is not there
# Traceback (most recent call last):
#   File "in.py", line 15, in <module>
#     testIn("A")
#   File "in.py", line 2, in testIn
#     assert isinstance(val, int), "Expecting a number"
# AssertionError: Expecting a number
