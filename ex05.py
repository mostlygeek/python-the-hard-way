name = "Benson Wong"
age = 33 # really!
height = 72
weight = 184
eyes = "Brown"
teeth = "White"
hair = "Black"

print "Let's about %s" % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# tricky line
print "If I add %d, %d, and %d I get %d." % (
        age, height, weight, age + height + weight
        )
