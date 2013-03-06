# 
# The 'with' statement allows code to be run, and torn down without
# having to use verbose try/except/finally. Useful to more succinctly 
# create resources, do stuff and tear down resources. 
# 
# Particularily with working with files, or IO when exceptions can occure
#
# ref: http://effbot.org/zone/python-with-statement.htm
#  ... good description

class BombError(BaseException):
    def __init__(self):
        self.message = "BOOM!"

class BombShelter:
    def __enter__(self): 
        print "You are in the bomb shelter"

    def __exit__(self, type, value, traceback):
        # return True will tell `with` not to re-raise any errors 
        # that were caught, anything else will cause errors to be 
        # reraised
        if isinstance(value, BombError):
            print "Caught the BOMB!"
            return True
        elif isinstance(value, Exception):
            print "Oh no! That's not a bomb!? re-raise the error"
            return False
        else:
            print "OK, finishing cleanly..."
            return True

class MegaBombShelter:
    def __enter__(self):
        pass
    def __exit__(self, type, value, traceback):
        if isinstance(value, Exception):
            print "!!!! MegaBombShelter Shielding Powers !!!"

        return True

print "This catching errors that we recognize..."
print "---------------------------"
with BombShelter():
    raise BombError()

print "\nEverything should be fine"
print "---------------------------"
with BombShelter():
    print "Whew, made it out alive!"

print "\nNested `with` contexts ..."
print "---------------------------"
with MegaBombShelter():
    with BombShelter():
        raise Exception("NOT A BOMB!")
        # program would normally crash here... but 
        # MegaBombShelter's __exit__ will save us

# OUTPUT
# ------------
#
# This catching errors that we recognize...
# ---------------------------
# You are in the bomb shelter
# Caught the BOMB!
# 
# Everything should be fine
# ---------------------------
# You are in the bomb shelter
# Whew, made it out alive!
# OK, finishing cleanly...
# 
# Nested `with` contexts ...
# ---------------------------
# You are in the bomb shelter
# Oh no! That's not a bomb!? re-raise the error
# !!!! MegaBombShelter Shielding Powers !!!
# 
