#
# Demonstration of `yield` keyword to work with a generator
# 
# see: http://stackoverflow.com/a/231855/445792
#  ... awesome answer on SO
#

def yieldTest(): 
    myList = range(3)
    for i in myList:
        yield i

def counter(upTo): 
    c = 0
    while c < upTo:
        c = c + 1
        yield c

def infinite(): 
    c = 0
    while True:
        c = c + 1
        yield c

myGenerator = yieldTest()
print myGenerator
for i in myGenerator: print "My Generator: %d" % i

print "------"

for v in counter(5): print "Counter: %d" % v

print "------"
# Demo of an infinite generator, we will break our own 
# loop when the user enters a 'q'
for c in infinite():
    print "Infinite %d" % c
    stop = raw_input("enter 'q' to quit> ")
    if stop == "q": break;

# OUTPUT
# ----------------
# Counter: 1
# Counter: 2
# Counter: 3
# Counter: 4
# Counter: 5
# ------
# Infinite 1
# enter 'q' to quit> 
# Infinite 2
# enter 'q' to quit> 
# Infinite 3
# enter 'q' to quit> 
# Infinite 4
# enter 'q' to quit> 
# Infinite 5
# enter 'q' to quit> q

# -----------

