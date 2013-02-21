# interpolate 10 into the string
x = "There are %d types of people." % 10

# var assignment
binary = "binary"
do_not = "don't"

# multiple string interpolation
y = "Those who know %s and those who %s" % (binary, do_not)

# duh
print x
print y

# the `%r` in there will auto quote the string `x`
print "I said: %r." % x

# the %s means string
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# you can interpolate a var w/ another var
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# string concatenation
print w + e
