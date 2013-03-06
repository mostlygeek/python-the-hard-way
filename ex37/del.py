a = range(1,5)
print a  # [1, 2, 3, 4]
del a[0]
print a  # [2, 3, 4]

def runMe(): 
    a = 100
    return a

print runMe()   # 100

# Throws a UnboundLocalError
def runMeWithDel(): 
    a = 100
    del a       # removes var out of the scope
    return a

try:
    print runMeWithDel()
except Exception, e:
    print "Caught %r " % e
finally:
    pass


