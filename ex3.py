
print "I will now count my chickens:"

print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

# this equals 7 ... 
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

# this is what the above equation is w/ some brackets around what's 
# happening
print "Is this 7?", (3 + 2 + 1 - 5) + (4 % 2) - (1 / 4) + 6

print "Is it true that 3 + 2 < 5 - 7?"

# hmm... apparently no brackets necessary, 
# operator precedence ...
print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, what's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= 2

import math
x       = 5242424244
pent10  = math.floor(math.log(x, 10)) - 1
divisor = math.pow(10, pent10)
rounded = int(math.floor(x/divisor)*divisor)
print "What is %s rounded to the penultimate magnitude of 10?, well it is %s" % (x, rounded)

